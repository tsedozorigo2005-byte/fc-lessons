# # Бодлого 1: Нэр форматлах
# # Овог, нэр авч "Овог Н." форматаар буцаах format_name(ovog, ner) функц бич.
# # Жишээ: format_name("Батбаяр", "Төмөр") → "Батбаяр Т."
# # Бодлого 2: Үнэ тооцоолох
# # Үнэ болон хөнгөлөлтийн хувь авч эцсийн үнийг буцаах calc_price(price, discount) функц бич.
# # Жишээ: calc_price(10000, 20) → 8000  (20% хөнгөлөлт)
# # Бодлого 3: Температур хөрвүүлэх
# # Цельсийг Фаренгейт руу хөрвүүлэх to_fahrenheit(celsius) функц бич.
# # Томьёо: F = C × 9/5 + 32
# # Жишээ: to_fahrenheit(0) → 32, to_fahrenheit(100) → 212
# # Бодлого 4: Нууц үг шалгах
# # Нууц үг 8-аас дээш тэмдэгттэй эсэхийг шалгах is_valid_password(password) функц бич.
# # Жишээ: is_valid_password("abc123") → False, is_valid_password("secure1234") → True
# # Бодлого 5: Тоглоомын оноо
# # Оноо авч түвшин буцаах get_rank(score) функц бич.
# # 0-49: "Bronze", 50-79: "Silver", 80-99: "Gold", 100: "Master"
# # Жишээ: get_rank(75) → "Silver", get_rank(100) → "Master"
# # Түвшин 2: Array-тай ажиллах
# # Бодлого 6: Хэрэглэгчдийн нэрс
# # Нэрсийн жагсаалт авч format_name() ашиглан бүгдийг форматлах format_users(users) функц бич.
# # Санамж: Бодлого 1-ийн функцээ ашигла.
# # Оролт: [["Бат", "Болд"], ["Дорж", "Сүх"]]
# # Гаралт: ["Бат Б.", "Дорж С."]
 
# # Бодлого 7: Хямдралтай бүтээгдэхүүн
# # Үнийн жагсаалт болон хөнгөлөлт авч бүх үнийг шинэчлэх apply_discount(prices, discount) функц бич.
# # Санамж: calc_price() функцээ ашигла.
# # Жишээ: apply_discount([1000, 2000, 3000], 10) → [900, 1800, 2700]
# # khuderchuluun.hdr — Yesterday at 21:29
# # Бодлого 8: Дундаж температур
# # Температурын жагсаалт (Цельс) авч дундаж Фаренгейтийг буцаах avg_temp_f(temps) функц бич.
# # Санамж: to_fahrenheit() функцээ ашигла.
# # Жишээ: avg_temp_f([0, 10, 20]) → 50.0
# # Бодлого 9: Тоглогчдын түвшин
# # Онооны жагсаалт авч түвшингүүдийн жагсаалт буцаах get_all_ranks(scores) функц бич.
# # Санамж: get_rank() функцээ ашигла.
# # Жишээ: get_all_ranks([30, 60, 85, 100]) → ["Bronze", "Silver", "Gold", "Master"]
# # Бодлого 10: Хүчтэй нууц үгүүд
# # Нууц үгийн жагсаалтаас зөвхөн хүчинтэй нууц үгүүдийг буцаах filter_valid_passwords(passwords) функц бич.
# # Санамж: is_valid_password() функцээ ашигла.
# # Жишээ: filter_valid_passwords(["abc", "password123", "hi"]) → ["password123"]
# # Түвшин 3: 2D Array эхлэл
# # Бодлого 11: Оюутны дүн
# # Оюутны нэр болон дүнгүүдийн 2D array-аас дундаж дүнг тооцох student_average(student) функц бич.
# # student = ["Болд", [80, 90, 85]]
# # Жишээ: student_average(["Болд", [80, 90, 85]]) → 85.0
# # Бодлого 12: Бүх оюутны дундаж
# # Олон оюутны мэдээлэл авч бүгдийн дундаж дүнг буцаах all_averages(students) функц бич.
# # Санамж: student_average() функцээ ашигла.
# # Оролт: [["Болд", [80,90]], ["Бат", [70,80]]]
# # Гаралт: [["Болд", 85.0], ["Бат", 75.0]]
# # Бодлого 13: Матриц үүсгэх
# # n×m хэмжээтэй матриц үүсгэж 0-ээр дүүргэх create_matrix(n, m) функц бич.
# # Жишээ: create_matrix(2, 3) → [[0,0,0], [0,0,0]]
# # Бодлого 14: Матриц хэвлэх
# # Матрицыг үзэмжтэй хэвлэх print_matrix(matrix) функц бич.
# # Оролт: [[1,2,3], [4,5,6]]
# # Гаралт:
# # 1 2 3
# # 4 5 6
# # Бодлого 15: Матрицын нийлбэр
# # Хоёр матриц нэмэх add_matrices(m1, m2) функц бич.
# # Санамж: create_matrix() ашиглаж үр дүнгийн матриц үүсгэ.
# # Жишээ: add_matrices([[1,2],[3,4]], [[5,6],[7,8]]) → [[6,8],[10,12]]
# # Түвшин 4: Бодит төсөл
# # Бодлого 16: Тоглоомын самбар
# # n×n хэмжээтэй тоглоомын самбар үүсгэж "." тэмдэгтээр дүүргэх create_board(n) функц бич.
# # Санамж: create_matrix() төстэй логик.
# # Жишээ: create_board(3) → [[".",".","."], [".",".","."], [".",".","."]]
# # Бодлого 17: Тоглогч байрлуулах
# # Самбар дээр тоглогч байрлуулах place_player(board, row, col, symbol) функц бич.
# # Жишээ: 
# # board = create_board(3)
# # place_player(board, 1, 1, "X")
# # → [[".",".","."], [".","X","."], [".",".","."]]
# # Бодлого 18: Самбар дүүрсэн эсэх
# # Самбар дээр хоосон зай (".") байгаа эсэхийг шалгах is_board_full(board) функц бич.
# # Жишээ: is_board_full([[".","X"],["O","X"]]) → False
# # Бодлого 19: Мөр шалгах
# # Тухайн мөрөнд бүгд ижил тэмдэгт байгаа эсэхийг шалгах check_row_win(board, row, symbol) функц бич.
# # Жишээ: 
# # board = [["X","X","X"], [".",".","."]]
# # check_row_win(board, 0, "X") → True
# # Бодлого 20: Ялагч олох
# # Мөр, багана, диагоналаар ялагч байгаа эсэхийг шалгах check_winner(board, symbol) функц бич.
# # Санамж: check_row_win() функцээ ашигла + багана, диагонал шалга.
# # Жишээ:
# # board = [["X","O","O"], ["X","X","."], ["X",".",".]]
# # check_winner(board, "X") → True  (эхний багана)
# # Функцүүдийн хамаарал
# # Түвшин 1 (Үндсэн):
# # format_name() ──────→ format_users()
# # calc_price() ───────→ apply_discount()
# # to_fahrenheit() ────→ avg_temp_f()
# # get_rank() ─────────→ get_all_ranks()
# # is_valid_password() → filter_valid_passwords()

# # Түвшин 2 (Array):
# # student_average() ──→ all_averages()
# # create_matrix() ────→ add_matrices(), create_board()

# # Түвшин 3 (2D Array - Тоглоом):
# # create_board() ─────→ place_player() → is_board_full()
# # check_row_win() ────→ check_winner()

# def niilberOloh(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum

# def ovog_ner(ovog, ner):
#     return(f"{ner}, {ovog[0]}")

# # print(ovog_ner("chinzorigt", "tserendolgor"))

# def calc_price(price, discount):
#     for price in prices:
#         print(price-(price * (discount / 100)))
        

# # calc_price(100, 50)

# def to_fahrenheit(celsius):
#     avarage = sum(celcius) / len(celcius)
#     return(avarage * 9/5 + 32)
     

# # to_fahrenheit(45)

# def is_valid_password(password):
#         return len(password) > 8
# # def filter_vaid_password(passwordd):
# #    return ( passurt for passurt in passwordd)
    
# # print(is_valid_password("TSe002"))

# def get_rank(scores):
#     onoo = []
#     for score in scores:
#         if score == 100:
#          onoo.append("Master")
#         elif 80 <= scores <= 99:
#          onoo.append("Gold")
#         elif 50 <= scores <= 79:
#          onoo.append("silver")
#         else:
#          onoo.append ("Bronze")
#     return(onoo)
    

# # print(get_rank(88))

# # orolt: [["Бат", "Болд"], ["Дорж", "Сүх"]]
# # for ovog, ner in orolt:
# #     print(ovog_ner(orolt))

# prices = [1000, 2000, 3000] 
# print(calc_price(prices, 10))

# # celcius = (10 , 20 , 30, 40)
# # print(to_fahrenheit(celcius))

# # list= [40, 50, 60, 70, 90]
# # print(get_rank(list))

# passwords = ["abcdjf", "ksjfbhsfb", "jsfsdk122345"]
# # print(is_valid_password(passwords))

# Жишээ: filter_valid_passwords(["abc", "password123", "hi"]) → ["password123"]
# def filter_valid_passwords(strs):
#    valid_passwords = []
#    for password in strs:
#       if len(password) > 8:
#          valid_passwords.append(password)
#    return valid_passwords
# print(filter_valid_passwords(passwords))


# price = int(input("unee oruul"))
# def thing(price, discount=20):
#     return price-(price * (discount / 100))
# print(thing(price))


# def average_all(*numbers):
#     # sum = 0 
#     # for number in numbers:
#         # sum += number
#     return sum(numbers) / len(numbers)
    
# print(average_all(1, 2, 3, 4, 5))
        

# def too_haih(arr, target):
#     for i in range(0, len(arr)):
#         if arr[i] == target:
#             return target
#     return -1

# too = [1, 2, 3, 4, 5, 6]
# a = 6
# print(too_haih(too, a))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr\
    

# arr= [1,3,5 ,6,4, 6]

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j] = arr[j+1]
#                 arr[j+1] = arr[j]
#                 # arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubble_sort(arr))





















# arr = [1, 6, 7]

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return(arr)
# print(bubble_sort(arr))


# Нууц үгийн жагсаалтаас зөвхөн хүчинтэй нууц үгүүдийг буцаах filter_valid_passwords(passwords) функц бич.
# Санамж: is_valid_password() функцээ ашигла.
# Жишээ: filter_valid_passwords(["abc", "password123", "hi"]) → ["password123"]
# Түвшин 3: 2D Array эхлэл
# Бодлого 11: Оюутны дүн
# Оюутны нэр болон дүнгүүдийн 2D array-аас дундаж дүнг тооцох student_average(student) функц бич.
# student = ["Болд", [80, 90, 85]]
# Жишээ: student_average(["Болд", [80, 90, 85]]) → 85.0
# Бодлого 12: Бүх оюутны дундаж
# Олон оюутны мэдээлэл авч бүгдийн дундаж дүнг буцаах all_averages(students) функц бич.
# Санамж: student_average() функцээ ашигла.
# Оролт: [["Болд", [80,90]], ["Бат", [70,80]]]
# Гаралт: [["Болд", 85.0], ["Бат", 75.0]]
# Бодлого 13: Матриц үүсгэх
# n×m хэмжээтэй матриц үүсгэж 0-ээр дүүргэх create_matrix(n, m) функц бич.
# Жишээ: create_matrix(2, 3) → [[0,0,0], [0,0,0]]
# Бодлого 14: Матриц хэвлэх
# Матрицыг үзэмжтэй хэвлэх print_matrix(matrix) функц бич.
# Оролт: [[1,2,3], [4,5,6]]
# Гаралт:
# 1 2 3
# 4 5 6
# Бодлого 15: Матрицын нийлбэр
# Хоёр матриц нэмэх add_matrices(m1, m2) функц бич.
# Санамж: create_matrix() ашиглаж үр дүнгийн матриц үүсгэ.
# Жишээ: add_matrices([[1,2],[3,4]], [[5,6],[7,8]]) → [[6,8],[10,12]]
# Түвшин 4: Бодит төсөл
# Бодлого 16: Тоглоомын самбар
# n×n хэмжээтэй тоглоомын самбар үүсгэж "." тэмдэгтээр дүүргэх create_board(n) функц бич.
# Санамж: create_matrix() төстэй логик.
# Жишээ: create_board(3) → [[".",".","."], [".",".","."], [".",".","."]]
# Бодлого 17: Тоглогч байрлуулах
# Самбар дээр тоглогч байрлуулах place_player(board, row, col, symbol) функц бич.
# Жишээ: 
# board = create_board(3)
# place_player(board, 1, 1, "X")
# → [[".",".","."], [".","X","."], [".",".","."]]
# Бодлого 18: Самбар дүүрсэн эсэх
# Самбар дээр хоосон зай (".") байгаа эсэхийг шалгах is_board_full(board) функц бич.
# Жишээ: is_board_full([[".","X"],["O","X"]]) → False
# Бодлого 19: Мөр шалгах
# Тухайн мөрөнд бүгд ижил тэмдэгт байгаа эсэхийг шалгах check_row_win(board, row, symbol) функц бич.
# Жишээ: 
# board = [["X","X","X"], [".",".","."]]
# check_row_win(board, 0, "X") → True
# Бодлого 20: Ялагч олох
# Мөр, багана, диагоналаар ялагч байгаа эсэхийг шалгах check_winner(board, symbol) функц бич.
# Санамж: check_row_win() функцээ ашигла + багана, диагонал шалга.
# Жишээ:
# board = [["X","O","O"], ["X","X","."], ["X",".",".]]
# check_winner(board, "X") → True  (эхний багана)
# Функцүүдийн хамаарал
# Түвшин 1 (Үндсэн):
# format_name() ──────→ format_users()
# calc_price() ───────→ apply_discount()
# to_fahrenheit() ────→ avg_temp_f()
# get_rank() ─────────→ get_all_ranks()
# is_valid_password() → filter_valid_passwords()

# Түвшин 2 (Array):
# student_average() ──→ all_averages()
# create_matrix() ────→ add_matrices(), create_board()

# Түвшин 3 (2D Array - Тоглоом):
# create_board() ─────→ place_player() → is_board_full()
# check_row_win() ────→ check_winner()



def student_average(student):
    niit =[]

    for i in student:
        name = i[0]
        grades = i[1:]
        average = sum(grades) / len(grades)
        niit.append([name, average])

student = [
    ["bat", 85, 90, 95],
    ["tsedo", 100, 90, 96]
]
print(student_average(student))