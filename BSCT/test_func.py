import json

def isWhiteList(token):
    with open('whitelist.json', 'r') as configdata:
        data=configdata.read()
    whiteList = json.loads(data)
    if 'list' in whiteList:
        for sub_token in whiteList['list']:
            if token == sub_token:
                return True
    return False

if (0.5 < float("0.3")):
    print("[FAIL] Liquidity amount too low.")
    boolLid = False
else:
    print("[SUCCESS] Liquidity is " + "0.2")
    boolLid = True
print(boolLid)