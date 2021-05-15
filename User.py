class User:
    def __init__(self, username, walletAmount):
        self.username = username
        self.walletAmount = walletAmount
    def getUserWalletAmount(self):
        print("Username=>",self.username)
        print("WalletAmount=>",self.walletAmount)
    def setUserWalletAmount(self, amount):
        self.walletAmount = amount