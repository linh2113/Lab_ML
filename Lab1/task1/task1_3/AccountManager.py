class AccountManager:

    def __init__(self):
        self.__accounts = list()

    def get_Accounts(self):
        return self.__accounts

    def add_account(self, account):
        self.__accounts.append(account)

    def groupAccountsByPostLike(self):
        list_under10 = list()
        list_over10 = list()
        d = {True: list_over10, False: list_under10}
        if self.get_Accounts():
            for account in self.get_Accounts():
                if len(account.get_Posts()) < 10:
                    list_under10.append(account)
                else:
                    list_over10.append(account)
        return d

    def filterAccounts(self, country):
        filtered_accounts = set()
        if self.get_Accounts():
            for account in self.get_Accounts():
                if country == account.get_Country():
                    filtered_accounts.add(account)
        sorted_filtered_accounts = sorted(filtered_accounts, key=lambda x: (-len(x.get_Posts()), x.get_LastName()))
        return sorted_filtered_accounts
