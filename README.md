# ez-token-py
Python client for interacting with the [EzToken contract](https://github.com/b-sage/ez-token)

## Purpose
When extracting ERC20 data offchain, there are a few issues you are likely to encounter:
* Contracts that appear to be ERC20, but do not implement all methods, causing reverts in our calls
* Contracts with non-standard return types for name, symbol or decimals

With ez-token (and ez-token-py), we are able to resolve both of these issues. For reverts, these simply get recognized in the ez-token 
contract and return a default value rather than reverting (empty string for name/symbol, 0 for decimals). ez-token also normalizes all names 
and symbols to string and decimals as uint256, regardless of return type specified by the token contract.

## Installation

Clone the repo, then:
```bash
pip install -e .
```

## Usage
```python3
from ez_token import EzToken
from evm_client.sync_client import SyncEthClient

your_rpc = ''
client = SyncEthClient(your_rpc)
ez = EzToken(client)

token_address = ''
name, symbol, decimals = ez.get_token(token_address)
```
