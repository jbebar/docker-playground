class machineState():

    ipAddress = ""
    state = ""

    def __init__(self, state, ipAddress):
        self.state = state
        self.ipAddress = ipAddress

    def __new__(self, state, ipAddress):
        self.state = state
        self.ipAddress = ipAddress
