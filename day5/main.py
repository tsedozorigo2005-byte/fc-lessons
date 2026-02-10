# def is_prime(n):
#     if n <= 1 and n % 2 == 0:
#         return False
        
#     if n == 2:
#         return True
   

#     a = 3
#     while a * a <= n:
#         if n % a == 0:
#             return False
#         i += 2

#     return True
# print(is_prime (8))

# def week(n):
#     if n == 1:
#         print("monday")
#     elif n == 2:
#         print("tuesday")
#     elif n == 3:
#         print("Wednesday")
#     elif n == 4:
#         print("Thursday")
#     elif n == 5:
#         print("Friday")
#     elif n == 6:
#         print("Saturday")
#     elif n == 7:
#         print("Sunday")
#     else:
#         print("Invalid day")
# week(9)


# numbers = [1, 2, 3, 4, 5]
# names = ["bold", "saraa", "dorj"]
# mixed = [1, "hello"]

# # too = [1, 2, 3]
# # for index, value in enumerate(too):
# #     print(index, value)


# # too = [1, 2, 3, 4, 5, 6]
# # print(too[2:4])

# # too = [1 ,2 ,3 ,4, 0]
# # max = 0
# # for i in too:
# #     if max < i:
# #         max = i
# # print(max)

# # too = [1, 2, 3]
# # min = 30
# # for i in too:
# #     if min > i:
# #         min = i
# # print(min)


# Day 1: print() ба input()
# 1. Өөрийн нэр, нас, дуртай өнгийг print() ашиглан 3 мөрөнд хэвлэ.
# 2. Хэрэглэгчээс нэр асууж, "Сайн байна уу, [нэр]! Танд амжилт хүсье!" гэж хэвлэх програм бич.
# 3. Хэрэглэгчээс 2 тоо авч, тэдгээрийн нийлбэрийг хэвлэ.
# 4. Хэрэглэгчээс нэр, хот асууж, "[Нэр] нь [Хот] хотод амьдардаг." гэж хэвлэ.

# Day 2: Хувьсагч ба үйлдлүүд
# 5. Хэрэглэгчээс радиус авч, тойргийн талбайг тооцоол. (Талбай = 3.14 × r²)
# 6. Цельсийн температур асууж, Фаренгейт руу хөрвүүл. (F = C × 9/5 + 32)
# 7. Хэрэглэгчээс 3 тоо авч, дунджийг нь олж хэвлэ.
# 8. Секундын тоо асууж, хэдэн минут, хэдэн секунд болохыг тооцоол. (Жишээ: 125 секунд = 2 минут 5 секунд)

# Day 3: Нөхцөлт үйлдлүүд (if/elif/else)
# 9. Тоо асууж, тэгш эсвэл сондгой эсэхийг шалга.
# 10. Хэрэглэгчээс нас асууж:
#   0-12: "Хүүхэд"
#   13-19: "Өсвөр нас"
#   20+: "Насанд хүрсэн"
# 11. Хоёр тоо асууж, аль нь их болохыг хэвлэ. Тэнцүү бол "Тэнцүү" гэж хэвлэ.
# 12. Нууц үг асууж, хэрэв "python123" бол "Зөв!", бусад үед "Буруу!" гэж хэвлэ.

# Day 4: Давталт ба функц
# 13. 1-ээс 10 хүртэлх тоонуудыг for давталт ашиглан хэвлэ.
# 14. Хэрэглэгчээс N тоо авч, 1-ээс N хүртэлх тоонуудын нийлбэрийг олох програм бич.
# 15. Үржвэрийн хүснэгт хэвлэх функц бич. (Жишээ: 5 өгвөл 5×1=5, 5×2=10, ... 5×10=50)
# 16. Тоо авч, factorial тооцоолох функц бич. (5! = 5×4×3×2×1 = 120)

# Day 5: List (Жагсаалт)
# 17. 5 тооны list үүсгэж, нийлбэр болон дунджийг олох програм бич.
# 18. Нэрсийн list үүсгэж, хэрэглэгчээс нэр асууж, тэр нэр list-д байгаа эсэхийг шалга.
# 19. Тоонуудын list өгөгдөхөд хамгийн их ба хамгийн бага утгыг олох функц бич.
# 20. List-ийн бүх тэгш тоонуудыг шинэ list-д хадгалж буцаах функц бич.


#1 ner = input(("Нэрээ оруулна уу?"))
# nas = input(("Насаа оруулна уу?"))
# ungu = input(("Дуртай өнгө өө оруулна уу?"))
# print(ner)
# print(nas)
# print(ungu)

#2 ner = input("Нэрээ оруулна уу?")
# print(f"Сайн байна уу, {ner} . Таньд амжилт хүсье")

#3 a = int(input("A toog oruulna uu?"))
# b = int(input("B toog oruulna uu?"))
# print(f"{a} + {b} = {a+b}")

#4 ner = input("neree n oruulna uu")
# hot = input("hotoo oruulna uu")
# print(f"{ner} ni {hot}d amidardag.")

#5 r = int(input("radiusiin toog oruulna uu?"))
# s = 3.14 * (r*r)
# print(s)

#6 c = int(input("celcius iin temperature iig oruulna uu?"))
# f = c * 9/5 + 32
# print(f)

#7 a = int(input("a toog oruulna uu?"))
# b = int(input("b toog oruulna uu?"))
# c = int(input("c toog oruulna uu?"))
# average = (a+b+c)/3
# print(average)

#8 sec = int(input("heden second ve?"))
# min = sec // 60 
# second = sec % 60
# print(f"{sec} second = {min} minute {second} second")

#9 a = int(input(" a toog oruul"))
# if a % 2 == 0:
#     print(" tegsh too baina")
# else:
#     print("sondgoi too baina")

# 10 age = int(input("how old are you"))
# if age <= 12:
#     print("Huuhed")
# elif 13<= age <= 19:
#     print("usvur nas")
# else:
#     print("nasand hursen")

#11 a = int(input("a toog oruul"))
# b = int(input("b toog oruul"))
# if a > b:
#     print(" a too ih baina")
# elif a < b:
#     print(" b too ih baina")
# else:
#     print("tentsuu baina")

# 12 password = input("nuuts ugee oruulna uu?")
# if password == "python123":
#     print("correct")
# else:
#     print("wrong!")

#13 i = (1, 10)
# for i in range(1, 11):
#     print(i)


#14 n = int(input("N toog oruulna uu"))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     print(sum)


# 15 n = int(input("urjih toogoo oruul"))
# for i in range (1, 11):
#     print(f"{n} * {i} = {n*i}")


# 16 def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(4))  

# 17 num = [1, 2, 3, 4, 5]
# niilber = sum(num)
# too = len(num)
# average = niilber/ too
# print(niilber)
# print(average)

# 18 ner = ["bold", "saraa", "zumbe", "dorjo"]
# name = input("neree oruulna uu?")
# if name in ner:
#     print("Tanii ner list d baina")
# else:
#     print("Tanii ner listed baihgui baina")


# 19 too = [1 ,2 ,3 ,4, 6]
# max = 0
# for i in too:
#      if max < i:
#          max = i
# print(max)

# too = [1, 2, 3]
# min = 30
# for i in too:
#      if min > i:
#          min = i
#          print(min)



# numberList = [1, 2, 3, 4, 5, 6]
# def tegsh_too_butsaah(numberList):
#     too = []
#     neg = []
#     for number in numberList:
      
#         if number % 2 == 0:
            
#             too.append(number)
#         else:
#             neg.append(number)
#     return too, neg

# a, b = tegsh_too_butsaah(numberList)

# print(a, b)

# def tavaas_ih ():
#     too = []
#     num = []
#     for i in range(1, 11):
#         too.append(i)
#     for number in too:
#         if number > 5:
#             num.append(number)
#     return num
# print(tavaas_ih())


# def ner_jagsaalt(list):
#     ner = input("nere oruulna uu")
#     for i in list:
#         if i == ner:
#             return True
#     return False

# name_list = ["dorjo", "saraa"]

# print(ner_jagsaalt(["dorjo", "saraa", "olr"]))

