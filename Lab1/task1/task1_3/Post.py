class Post:
    def __init__(self, content, subject, likes):
        self.__content = content
        self.__subject = subject
        self.__likes = likes

    def get_Likes(self):
        return self.__likes

    def get_Content(self):
        return self.__content

    def get_Subject(self):
        return self.__subject

    def __repr__(self):
        return "Post:<<Nội dung:" + self.get_Content() + ", Chủ đề:" + self.get_Subject() + ", " + str(self.get_Likes()) +\
            " likes>>"
