from Lab1.task1.task1_3.Account import Account


class NormalProduct(Account):

    def __init__(self, name, email, country):
        super().__init__(name, email, country)

    def __repr__(self):
        return "NormalProductAccount[" + super().get_Name() + ", " + super().get_Email() + ", " + super().get_Country() +\
            ", " + str(len(super().get_Posts())) + "]"
