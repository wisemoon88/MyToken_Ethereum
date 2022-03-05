from brownie import MyToken, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_OurToken():
    account = get_account()
    myToken = MyToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"deployed! {myToken.name()}")
    return myToken


def main():
    deploy_OurToken()
