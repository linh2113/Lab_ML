from Lab1.task1.task1_3.Account import Account


class VerifiedAccount(Account):

    def __init__(self, name, email, country, fromDate):
        super().__init__(name, email, country)
        self.__fromDate = fromDate

    def get_FromDate(self):
        return self.__fromDate

    def __repr__(self):
        return "VerifiedAccount[" + super().get_Name() + ", " + super().get_Email() + ", " + super().get_Country() + \
            ", " + str(len(super().get_Posts())) + ", " + str(self.get_FromDate().strftime("%m/%d/%Y")) + "]"

