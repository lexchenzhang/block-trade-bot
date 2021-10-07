const EthCrypto = require('eth-crypto');
const web3 = require('web3');

async function sendTx() {
    const identity = EthCrypto.createIdentity();
    const rawTx = {
        from: identity.address,
        to: '0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0',
        value: 1000000000000000000,
        gasPrice: 5000000000,
        nonce: 0,
        gasLimit: 21000
    };
    const signedTx = EthCrypto.signTransaction(
        rawTx,
        identity.privateKey
    );
    console.log(signedTx);
    // > '071d3a2040a2d2cb...'

    // you can now send the tx to the node
    const receipt = await web3.eth.sendSignedTransaction(signedTx);
}

sendTx();