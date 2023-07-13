from model.account.models import Account


class UserRepository:
    def get_list(self):
        return Account.objects.all()
