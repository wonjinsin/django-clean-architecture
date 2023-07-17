from repository.user import UserRepository

class UserService:
    userRepo = UserRepository()

    def get_list(self) -> object:
        return self.userRepo.get_list()
