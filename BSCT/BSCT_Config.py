import json
import os

#load json data

configFilePath = os.path.abspath('') + '/config.json'

with open(configFilePath, 'r') as configdata:
    data=configdata.read()

# parse file
configData = json.loads(data)

pancakeSwapRouterAddress = configData['pancakeSwapRouterAddress'] #load config data from JSON file into program
pancakeSwapFactoryAddress = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73' #read from JSON later
walletAddress = configData['walletAddress']
walletPrivateKey = configData['walletPrivateKey'] #private key is kept safe and only used in the program

bscNode = configData['bscNode']

snipeBNBAmount = float(configData['amountToSpendPerSnipe'])
transactionRevertTime = int(configData['transactionRevertTimeSeconds']) #number of seconds after transaction processes to cancel it if it hasn't completed
gasAmount = int(configData['gasAmount'])
gasPrice = int(configData['gasPrice'])
bscScanAPIKey = configData['bscScanAPIKey']
observeOnly = configData['observeOnly']
liquidityPairAddress = configData['liquidityPairAddress']
targetAddress = configData['targetAddress']
snipeDelay = configData['snipeDelay']


checkSourceCode = configData['checkSourceCode']
checkValidPancakeV2 = configData['checkValidPancakeV2']
checkMintFunction = configData['checkMintFunction']
checkHoneypot = configData['checkHoneypot']
checkPancakeV1Router = configData['checkPancakeV1Router']
checkForTest = configData['checkForTest']
checkForWhiteList = configData['checkForWhiteList']
minLiquidityAmount = float(configData['minLiquidityAmount'])