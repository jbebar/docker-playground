#!/bin/bash
FILEREAD=$1
CENTRALHOST=$2

titles='|IPAdress|lastLaunched|version|lastAverageFrameRate|status'

echo "--------------------------------------------------------------"
echo "Started log analyse."
echo "--------------------------------------------------------------"
echo "Start looking for data from the machine logs file : $FILEREAD."

if [ -f "$FILEREAD" ]
then
	echo "Log file $FILEREAD found."
else
	echo "ERROR: Log $FILEREAD not found!"
    echo "Exit log analyse."
    echo "--------------------------------------------------------------"
    exit 2
fi

###Determine status
IPAdress=`egrep -o 'IPs: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' $FILEREAD`
IPAdress=${IPAdress:5}
lastLaunched=`grep 'Welcome to WeedEngine' $FILEREAD | tail -1`
lastLaunched=${lastLaunched:1:23}
version=`egrep -o -f versionPattern.txt $FILEREAD | tail -1`
lastFrameRate=`egrep -o '[0-9]{1}\.[0-9]{5}\/s' $FILEREAD | tail -1`

status="None"
###Determine status
countBuildingCache=`grep -c 'Start camera notify build cache' $FILEREAD`
countRunning=`grep -c 'Start Recorder' $FILEREAD`
countStopped=`egrep -c '\[weedengine\] \[info\] Leaving main\.' $FILEREAD`

if  [ $countBuildingCache -gt 0 ]; then
    echo "Found builing cache pattern."
    status="BuildingCache"
fi
if  [ "$countRunning" -gt 0 ]; then
    echo "Found running pattern."
    status="Running"
fi
if  [ "$countStopped" -gt 0 ]; then
    echo "Found stopped pattern."
    status="Stopped"
fi

echo "$titles"

tableValues="|$IPAdress|$lastLaunched|$version|$lastFrameRate|$status|"
echo $tableValues
curl -d "$tableValues" "http://$2:8080/report"
echo "SUCESS : Finished log analyse on  $FILEREAD"