#1 word = input("ugiig oruulna uu?")
# print(word[0])
# print(word[-1])

#2 word = input("ugiig oruulna uu?")
# print(word[::-1])

#3 sentence = "tavtai morilno uu"
# print(sentence.upper())
# print(sentence.lower())

#4 sentence = input("uguulberiig oruul")
# words = sentence.split()
# print(len(words))

#5 word1 = input("ehnii ugee oruulna uu?")
# word2 = input("hoyrdoh ugee oruulna uu?")
# word3 = input("3dh ugee oruulna uu?")

# result = "-".join([word1, word2, word3])
# print(result)

#6 sentence = input("uguulberiig oruul")
# result = (sentence. replace(" ", "_"))
# print(result)

#7 ner = input("neree oruulna uu?")
# nas = input("nasaa oruulna uu?")
# hot = input("hotoo oruulna uu?")
# print(f"minii ner {ner}, bi {nas} nastai, bi {hot}d amidardag.")

# def mail_zuv(str):
#     mail = email.split("@")
#     if len(mail) < 2:
#         return False
#     domain = mail[1].split(".")
#     if len(domain) < 2:
#         return False
#     return True

# email = "tsedozorigo@gmail.com" 
# print(mail_zuv(email))


# fruits = ["alim", "banana", "liir"]

# for i, fruit in enumerate (fruits):
#     print(f"{i}: {fruit}")

# n = int(input("n iig oruul"))
# for i in range(1, n+1):
#     print("*" * i)

# matrix = [
#     [1, 2, 3],
#     [7, 8, 9],
#     [4, 5, 6],
# ]
# for i in matrix:
#     for b in i:
#         print(b)
    
# matrix = [
#     [1, 2, 3],
#     [7, 8, 9],
#     [4, 5, 6],
#  ]

# sum = 0
# for i in matrix:
#     for b in i:
        
#         sum += b # sum = sum + b
# print(sum)

# matrix = [
#      [1, 2, 3],
#      [7, 8, 9],
#      [4, 5, 6],

# even_counter = []

# for i in matrix:
#     for b in i:
#         if b % 2== 0:
#             even_counter.append(b)

#         ###  sum += b # sum = sum + b
# print(len(even_counter)


# max = 0
# min = matrix[0][0]

# for i in matrix:
#      for b in i:
        
#         if max < b:
#             max = b
#         if min > b:
#             min = b
# print(min, max)
            
# sum = 0
# n = [[5,7],[4,3],[34,98]]
# n1 = [[5,7],
#       [4,3],
#       [34,98],
#       [3,7]]
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i, mt in enumerate(matrix):
    sum = 0
    for j, val in enumerate(mt):
        print("sum = ",matrix[j][i])
        sum += matrix[j][i]
    print(sum)

        