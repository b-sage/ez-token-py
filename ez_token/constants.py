import json

ADDRESS_MAP = {
    100: "0x29Df8ca4F6bC9d22d23437e1910fDF0D1f3ce664", #gnosis
    11155420: "0x99F78055cE097B23B43d7190cDd314b6A44edc87", #OP sepolia
    84532: "0x29F8Af45A5dEe510F3C81331CFF222e97E3D76f7", #Base sepolia
    1301: "0x6D0D6efc7336d3057aCfBDa71866C398537D4587", #unichain sepolia
    11155111: "0x6D0D6efc7336d3057aCfBDa71866C398537D4587", #sepolia
}

EZTOKEN_ABI = json.loads('''
[{"type":"function","name":"decimals","inputs":[{"name":"target","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"name","inputs":[{"name":"target","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"symbol","inputs":[{"name":"target","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"token","inputs":[{"name":"target","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"string","internalType":"string"},{"name":"","type":"string","internalType":"string"},{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"}]
''')
