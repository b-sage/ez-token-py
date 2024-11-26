import re
from evm_client.sync_client import SyncEthClient
from evm_client.contract import Contract
from .constants import ADDRESS_MAP, EZTOKEN_ABI

def sanitize(string):
    return re.sub('[,\r\n\r\x00-\x1f]','', string).lstrip(' ')

class EzToken:

    def __init__(self, client: SyncEthClient, abi=EZTOKEN_ABI):
        self.client = client
        chain_id = self.client.chain_id()
        address = ADDRESS_MAP[chain_id]
        self.contract = Contract(address, abi)

    def get_token_decimals(self, target: str):
        tx = self.contract.functions.decimals.build_transaction(target)
        return self.client.call(tx, decoder=self.contract.functions.decimals.decode_result)

    def get_token_symbol(self, target: str):
        tx = self.contract.functions.symbol.build_transaction(target)
        return sanitize(self.client.call(tx, decoder=self.contract.functions.symbol.decode_result))

    def get_token_name(self, target: str):
        tx = self.contract.functions.name.build_transaction(target)
        return sanitize(self.client.call(tx, decoder=self.contract.functions.name.decode_result))

    def get_token(self, target: str):
        tx = self.contract.functions.token.build_transaction(target)
        name, symbol, decimals = self.client.call(tx, decoder=self.contract.functions.token.decode_result)
        return sanitize(name), sanitize(symbol), decimals

    #TODO: add batch client attribute, create batch methods
    #TODO: add multicall methods
