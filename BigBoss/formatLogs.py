import re

def prettyPrintBody(req):
    values = re.split("\|", req)
    for v in values:
        values
    return re.split("\|", req, 2)[1]

def extractAddressFromRequest(req):
    return re.split("\|", req, 2)[1]