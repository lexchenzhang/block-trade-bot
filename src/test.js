const Web3 = require('web3');

// Variables definition
const privKey =
    'ab4b77f621c0d398a830aef9374b5ac60374beec13f16b62ce160ae7cd1f5d04'; // Genesis private key
const addressFrom = '0xaa26F181C3E08339f285a750fD5F9093eC1297DD';
const addressTo = '0xa8dC83000D5630DA5893a4593b1890a7fAfb0D72';
const web3 = new Web3('http://localhost:8545');

// Create transaction
const deploy = async() => {
    console.log(
        `Attempting to make transaction from ${addressFrom} to ${addressTo}`
    );

    const createTransaction = await web3.eth.accounts.signTransaction({
            from: addressFrom,
            to: addressTo,
            value: web3.utils.toWei('1', 'ether'),
            gas: '21000',
        },
        privKey
    );

    // Deploy transaction
    const createReceipt = await web3.eth.sendSignedTransaction(
        createTransaction.rawTransaction
    );
    console.log(
        `Transaction successful with hash: ${createReceipt.transactionHash}`
    );
};

deploy();