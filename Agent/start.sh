DELAY="2"
OFFSET=$1
HOSTCENTRAL="big-boss"

LOGPATH="./agent.log"
LOGTEMPLATEPATH="./agentTemplate.log"

./machine/readAndPrintLogs.py $LOGTEMPLATEPATH $LOGPATH -d $DELAY -o $OFFSET >logsSimulator.log 2>&1 & watch -n1 ./client.sh $LOGPATH $HOSTCENTRAL