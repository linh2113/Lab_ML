from abc import ABC

class Post:
    def __init__(self, content, subject, likes):
        self.__content = content
        self.__subject = subject
        self.__likes = likes

    def get_likes(self):
        return self.__likes

    def __repr__(self):
        return "Post(content:" + self.__content + ", subject:" + self.__subject +\
            ", likes:" + str(self.__likes) + ")"


def getPostHasMaxLikesIn(account):
    posts = account.get_posts()
    if not posts:
        return None

    max_like_post = posts[0]
    for post in posts:
        if post.get_likes() > max_like_post.get_likes():
            max_like_post = post

    return max_like_post


class Account(ABC):
    def __init__(self, name, email, country):
        self.__name = name
        self.__email = email
        self.__country = country
        self.__friends = list()
        self.__posts = list()

    def __repr__(self):
        return "name:" + self.__name + ", email:" + self.__email + ", country:" + self.__country

    def get_lastname(self):
        parts = self.__name.split()
        if parts:
            return parts[-1]
        return None

    def get_country(self):
        return self.__country

    def get_posts(self):
        return self.__posts

    def set_friends(self, friends):
        if friends:
            self.__friends.extend(friends)

    def set_posts(self, posts):
        if posts:
            self.__posts.extend(posts)

    def getMaxLikePostByFriend(self):
        if not self.__friends:
            return None

        friend_with_max_like_post = None
        max_likes = -1
        for friend in self.__friends:
            post = getPostHasMaxLikesIn(friend)
            if post and post.get_likes() > max_likes:
                friend_with_max_like_post = friend
                max_likes = post.get_likes()

        return friend_with_max_like_post


class AccountManager:
    def __init__(self):
        self.__accounts = list()

    def set_accounts(self, accounts):
        if accounts:
            self.__accounts.extend(accounts)

    def groupAccountsByPostLike(self):
        if not self.__accounts:
            return None

        list_under_10 = list()
        list_over_10 = list()
        for account in self.__accounts:
            posts_len = len(account.get_posts())
            if posts_len < 10:
                list_under_10.append(account)
            else:
                list_over_10.append(account)

        return {False: list_under_10, True: list_over_10}

    def filterAccounts(self, country):
        if not self.__accounts:
            return None

        filter_set = set()
        for account in self.__accounts:
            if country == account.get_country():
                filter_set.add(account)

        return sorted(filter_set, key=lambda x: (-len(x.get_posts()), x.get_lastname()))


class VerifiedAccount(Account):
    def __init__(self, name, email, country, fromDate):
        super().__init__(name, email, country)
        self.__fromDate = fromDate

    def __repr__(self):
        return "VerifiedAccount[" + super().__repr__() + ", verified_date: " +\
            str(self.__fromDate.strftime("%d/%m/%Y")) + "]"


class NormalAccount(Account):
    def __init__(self, name, email, country):
        super().__init__(name, email, country)

    def __repr__(self):
        return "NormalAccount[" + super().__repr__() + "]"
