# for i in range(1, 11):
#     for b in range(1, 11):
#         print(f"{i} * {b} = {i * b}")


# n = int(input("n iig oruul"))
# for i in range(1, n+1):
#     print("*" * i)


# a = 3
# b = 5
# def urgun_undur(a, b):
#     for i in range(1, a+1):
#         print("*" * b) 
# urgun_undur(a, b)


# too = [10, 20, 30, 40, 50]


def niilberOloh(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

# arr = [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
# ]

# for arh in arr:
#     print(niilberOloh(arh))

def sondgoi_too(numbers):
    if numbers % 2== 0:
        return False
    else:
        return True

# arr = [ 1, 2, 3, 4, 5, 6]
# for i in arr:
#     num = i
#     if sondgoi_too(num):
#         print(num)

def arr_oloh (negt, hyrt):
    for i in negt:
        if i == hyrt:
            return True
    return False
        
        

# arr = [3,5,8,6,8]
# a = 6
# print(arr_oloh(arr,a))
        
arr = [1, 2, 3, 4, 5, 6]
a = niilberOloh(arr)
print(sondgoi_too(a))