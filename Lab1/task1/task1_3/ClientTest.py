from datetime import datetime
from Lab1.task1.task1_3.AccountManager import AccountManager
from Lab1.task1.task1_3.NormalProduct import NormalProduct
from Lab1.task1.task1_3.Post import Post
from Lab1.task1.task1_3.VerifiedAccount import VerifiedAccount


def main():
    p1 = Post("Việt nam đang trong trạng suy thoái kinh tế", "Kinh tế", 15)
    p2 = Post("Tai nạn giao thông tại cầu vượt linh xuân", "Giao thông", 16)
    p3 = Post("Mạng xã hội gặp sự cố toàn cầu", "Thế giới", 10)
    p4 = Post("Ronaldo là cầu thủ chạy nhanh nhất thế giới", "Thể thao",19)
    p5 = Post("Hôm nay là ngày quốc tế phụ nữ", "Đời sống", 10)
    
    acc1 = VerifiedAccount("Đoàn Nhất Linh", "21130091@st.hcmuaf.edu.vn", "Việt Nam", datetime(2003, 7, 19))
    acc2 = NormalProduct("Ronaldo", "ronaldo@gmail.com", "Portugal")

    manager = AccountManager()

    manager.add_account(acc1)
    manager.add_account(acc2)

    acc1.add_post(p1)
    acc1.add_post(p2)

    acc2.add_post(p3)
    acc2.add_post(p4)
    acc2.add_post(p5)


    acc1.add_friend(acc2)
    acc2.add_friend(acc1)

    print(acc1.getMaxLikePostByFriend())
    print(acc2.getMaxLikePostInListFriends())
    print(manager.groupAccountsByPostLike())
    print(manager.filterAccounts("Portugal"))


if __name__ == "__main__":
    main()
