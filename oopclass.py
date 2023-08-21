# class Masin:
#     pass
# masin=Masin()
# print(masin)
# print(type(masin))
# 
#             init 
# class telefon():
#     def __init__(self):
#         self.name="iphone 11"
#         print("nesne olusturuldu")
# t1=telefon()
# t2=telefon()
# print(t1.name,t2.name)
# 
# class Comment:
#     def __init__(self,username,text,likes,dislikes):
#         self.username=username,
#         self.text=text,
#         self.likes=likes,
#         self.dislikes=dislikes,
# list=[]
# for i in range(1,6):
#     username=input("username")
#     text=input("text")
#     likes=input("likes")
#     dislikes=input("dislikes")
#     c=Comment(username,text,likes,dislikes)
#     list.append(c)
# for i in list:
#     print(i.username)
#     print(i.text)
#     print(i.likes)
#     print(i.dislikes)
# 

# class BankAccount:
#     def __init__(self,owner):
#         self.owner=owner
#         self.balance=0
#     def intro(self,deposit):
#         self.balance+=deposit
#     def cixaris(self,geri):
#         if self.balance>geri:
#             self.balance-=geri
#             print(geri, "manat cekildi")
#             print("sizin balansiniz",self.balance)
#         else:
#             print("balansinizda kifayet qeder mebleg yoxdur")
# b1=BankAccount("gulu")
# b1.intro(250)
# print(b1.balance)
# b1.cixaris(100)

# quiz
# class Question:
#     def __init__(self,text,chocies,answer):
#         self.text=text
#         self.chocies=chocies
#         self.answer=answer
#     def intro(self,checkAnswer):
#         if self.answer==checkAnswer:
#             print("True")
#         else:
#             print("False")
# q1=Question("hangisi?",["python","java","c#"],"python")
# print(q1.answer)
# q1.intro("java")
#
#
# class Kart:
#     def __init__(self,tip,deyer):
#         self.tip=tip
#         self.deyer=deyer
#     def kartiGetir(self):
#         return f"{self.tip} {self.deyer}"
# k1=Kart("sinek",5)
# print(k1.tip)
# print(k1.deyer)
# k1.kartiGetir()

