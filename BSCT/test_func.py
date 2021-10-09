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

ret = isWhiteList('0xaba')
print(ret)