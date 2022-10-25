class User:
    def __init__(self, name, email, account, bank):
        self.name = name
        self.email = email
        self.account = account
        self.bank = bank

    def __str__(self):
        return f"User {self.name} has account {self.account} with {self.bank}"


class Transaction:
    def __init__(self, user: User, amount, date):
        self.user = user
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.user} spent {self.amount} on {self.date}"
