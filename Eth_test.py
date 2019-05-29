#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:53:14 2019

@author: kylekoshiyama
"""

import json
from web3 import Web3

#infura_url = "https://mainnet.infura.io/v3/5eb130e372e7436099ee6f593b928072"
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))


'''abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"withdrawEther","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"unfreeze","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"freezeOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"freeze","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"decimalUnits","type":"uint8"},{"name":"tokenSymbol","type":"string"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Freeze","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Unfreeze","type":"event"}]')
adress = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"

contract = web3.eth.contract(address = adress, abi = abi)
#print(contract)

#totalSupply = contract.functions.totalSupply().call()
#print(web3.fromWei(totalSupply, 'ether'))
#print(contract.functions.name().call())
#balance = contract.functions.balanceOf('0x030e37ddd7df1b43db172b23916d523f1599c6cb').call()
#print(web3.fromWei(balance, 'ether'))

account_1 = '0xbE27d174ABeb19cD15165F921fAEcCE4bb2CCdbf'
account_2 = '0x7E6F4E4E3332dD23637cf2fb62ca24D728ce893C'

private_key = '375880da207ac23f4fad28b6a85738066ddca6b03b5d8973a39d8bf2790c93da'

nonce = web3.eth.getTransactionCount(account_1)
tx = {
      'nonce':nonce,
      'to': account_2,
      'value':web3.toWei(1,'ether'),
      'gas':2000000,
      'gasPrice':web3.toWei('50','gwei')
      }

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

address = web3.toChecksumAddress('0x08a171749b8a82994c01871c3a74d5ae3f311842')
abi = json.loads('[{"constant":false,"inputs":[],"name":"Greeter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

contract =  web3.eth.contract(address = address, abi = abi)
print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('yeet').transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print(contract.functions.greet().call())'''



web3.eth.defaultAccount = web3.eth.accounts[0]
abi = json.loads('[{"constant":false,"inputs":[],"name":"Greeter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
bytecode = '606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063777256c414610067578063a41368621461007c578063cfae3217146100d9578063ef690cc014610167575b600080fd5b341561007257600080fd5b61007a6101f5565b005b341561008757600080fd5b6100d7600480803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050610243565b005b34156100e457600080fd5b6100ec61025d565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561012c578082015181840152602081019050610111565b50505050905090810190601f1680156101595780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561017257600080fd5b61017a610305565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101ba57808201518184015260208101905061019f565b50505050905090810190601f1680156101e75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6040805190810160405280600581526020017f48656c6c6f000000000000000000000000000000000000000000000000000000815250600090805190602001906102409291906103a3565b50565b80600090805190602001906102599291906103a3565b5050565b610265610423565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102fb5780601f106102d0576101008083540402835291602001916102fb565b820191906000526020600020905b8154815290600101906020018083116102de57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561039b5780601f106103705761010080835404028352916020019161039b565b820191906000526020600020905b81548152906001019060200180831161037e57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103e457805160ff1916838001178555610412565b82800160010185558215610412579182015b828111156104115782518255916020019190600101906103f6565b5b50905061041f9190610437565b5090565b602060405190810160405280600081525090565b61045991905b8082111561045557600081600090555060010161043d565b5090565b905600a165627a7a723058209e1bfe8d4cdf0d396824c0312e8859b955bf27c9809ab0856c0d92468c58c1400029'
Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()

tx_rec = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(
        address=tx_rec.contractAddress,
        abi=abi)

print(contract.functions.greet().call())

