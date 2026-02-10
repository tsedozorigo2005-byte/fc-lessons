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



# def student_average(students):
#     niit =[]

#     for i in students:
#         name = i[0]
#         grades = i[1:]
#         average = sum(grades) / len(grades)
#         niit.append([name, average])
#     return niit

# # student = [
# #     ["bat", 85, 90, 95]
# # ]
# # print(student_average(student))

# def all_averages(students):
#     onoo = []
#     for i in students:
#         onoo.append(student_average(i))
#     return onoo 

# students = [["bold", [80,90]], ["bat", [70.80]]]
# print(all_averages(students))


# def create_matrix(n, m):
#     matrix = []
#     for i in range(n):
#         egnee = [0] * m
#         matrix.append(egnee)
#     return matrix

# # print(create_matrix(2,3))

# def print_matrix(matrix):
#     for egnee in matrix:
#         print (egnee, "\n") #print(*egnee)
# matrix = [[1, 2, 3], [4, 5, 6]]
# # print_matrix(matrix)

# def add_matrices(m1, m2):
#     a = len(m1)
#     b = len(m1[0]) 
#     result = create_matrix(a,b)

#     for i in range(a):
#         for j in range(b):
#             result[i][j] = m1[i][j] +m2[i][j]
#     return result

# m1 = [[1, 2], [3, 4]]
# m2 = [[5, 6], [7, 8]]

# # print(add_matrices(m1, m2))


# def create_board(n):
#     board = []
#     for i in range(n):
#         board.append((".") * n)
#     return board

# print(create_board(3))

# def place_player(board, row, col, symbol):
#     board[row][col] = symbol
#     return board

# board = create_board(3)
# place_player(board, 1, 1, "X")
# print(board)

# def is_board_full(board):
#     for r in board:
#         if "." in r:
#             return False
#     return True

# print(is_board_full([[".","X"], ["O"],["x"]]))




