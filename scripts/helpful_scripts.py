from brownie import accounts, config, network

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# this helpful_scripts.py script is where we store useful functions that we will want to deploy across scripts
def get_account(index=None, id=None):
    # accounts
    if index:
        return accounts[index]
    if id:
        return accounts.load[id]

    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]

    # default account if if statement is not triggered
    return accounts.add(config["wallets"]["from_key"])
