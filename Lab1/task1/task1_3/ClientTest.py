from datetime import datetime
from Lab1.task1.task1_3.Account import Post, getPostHasMaxLikesIn,AccountManager, VerifiedAccount, NormalAccount

                                    
def main():
   
    p1 = Post("Tai nạn giao thông tại cầu vượt linh xuân", "Giao thông", 16)
    p2 = Post("Việt nam đang trong trạng suy thoái kinh tế", "Kinh tế", 15)
    p3 = Post("Mạng xã hội gặp sự cố toàn cầu", "Thế giới", 10)
    p4 = Post("Ronaldo là cầu thủ chạy nhanh nhất thế giới", "Thể thao",19)
    p5 = Post("Hôm nay là ngày quốc tế phụ nữ", "Đời sống", 10)

    acc1 = VerifiedAccount("Đoàn Nhất Linh", "21130091@st.hcmuaf.edu.vn", "Việt Nam", datetime(2003, 7, 19))
    acc2 = NormalAccount("Ronaldo", "ronaldo@gmail.com", "Portugal")

    postsOf1 = list()
    postsOf2 = list()

    postsOf1.append(p1)
    postsOf1.append(p2)
    postsOf1.append(p3)
    postsOf1.append(p4)
    postsOf1.append(p5)
  
    postsOf2.append(p4)
    postsOf2.append(p5)
  
    acc1.set_posts(postsOf1)
    acc2.set_posts(postsOf2)

    friendsOf1 = list()
    friendsOf2 = list()

    friendsOf1.append(acc2)
    friendsOf2.append(acc1)

    acc1.set_friends(friendsOf1)
    acc2.set_friends(friendsOf2)

    manager = AccountManager()

    accsOfManager = list()

    accsOfManager.append(acc1)
    accsOfManager.append(acc2)
  
    manager.set_accounts(accsOfManager)

    print(getPostHasMaxLikesIn(acc1))
    print(getPostHasMaxLikesIn(acc2))
    print(acc1.getMaxLikePostByFriend())
    print(manager.groupAccountsByPostLike())
    print(manager.filterAccounts("Việt Nam"))

if __name__ == "__main__":
    main()
