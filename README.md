# ez-token-py
Python client for interacting with the [EzToken contract](https://github.com/b-sage/ez-token)

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
