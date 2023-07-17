from model.account.models import Account

def repo_deco(func):
    def _wrapper(self, *args, **kwargs):
        try:
            obj = func(self, *args, **kwargs)
            if obj.is_valid() != True:
                return None
            return obj
        except Exception as e:
            print('not valid')
            return None
    return _wrapper


class UserRepository:
    @repo_deco
    def get_list(self) -> object:
        return Account.objects.all()

