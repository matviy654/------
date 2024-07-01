# task1
# a = int(input("введіть число1: "))
# b = int(input("введіть число1: "))
# for i in range (a,b,1) :
#  if i%7==0 :
#   print(i)
# task2
# def get_input():
#     start = int(input("Введіть число1: "))
#     end = int(input("Введіть число2: "))
#     return start, end
# def analyze_range(start, end):
#     all_numbers = list(range(start, end + 1))
#     print("Всі числа діапазону:")
#     print(all_numbers)
#     all_numbers_desc = all_numbers[::-1]
#     print("Всі числа діапазону в спадному порядку:")
#     print(all_numbers_desc)
#     multiples_of_7 = [num for num in all_numbers if num % 7 == 0]
#     print("Всі числа, кратні 7:")
#     print(multiples_of_7)
#     multiples_of_5_count = sum(1 for num in all_numbers if num % 5 == 0)
#     print(f"Кількість чисел, кратних 5: {multiples_of_5_count}")
# start, end = get_input()
# analyze_range(start, end)
#task3
# def get_input():
#     start = int(input("Введіть початок діапазону: "))
#     end = int(input("Введіть кінець діапазону: "))
#     return start, end

# def analyze_range(start, end):
#     for num in range(start, end + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print("Fizz Buzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         else:
#             print(num)

# start, end = get_input()
# analyze_range(start, end)
#task4
# def get_input():
#     start = int(input("Введіть початок діапазону: "))
#     end = int(input("Введіть кінець діапазону: "))
#     return start, end

# def analyze_range(start, end):
#     even_sum = 0
#     even_count = 0
#     odd_sum = 0
#     odd_count = 0
#     multiples_of_9_sum = 0
#     multiples_of_9_count = 0
    
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             even_sum += num
#             even_count += 1
#         else:
#             odd_sum += num
#             odd_count += 1
        
#         if num % 9 == 0:
#             multiples_of_9_sum += num
#             multiples_of_9_count += 1
    
#     if even_count > 0:
#         even_avg = even_sum / even_count
#     else:
#         even_avg = 0
    
#     if odd_count > 0:
#         odd_avg = odd_sum / odd_count
#     else:
#         odd_avg = 0
    
#     if multiples_of_9_count > 0:
#         multiples_of_9_avg = multiples_of_9_sum / multiples_of_9_count
#     else:
#         multiples_of_9_avg = 0
    
#     print(f"Сума парних чисел: {even_sum}")
#     print(f"Середнє арифметичне парних чисел: {even_avg}")
    
#     print(f"Сума непарних чисел: {odd_sum}")
#     print(f"Середнє арифметичне непарних чисел: {odd_avg}")
    
#     print(f"Сума чисел, кратних 9: {multiples_of_9_sum}")
#     print(f"Середнє арифметичне чисел, кратних 9: {multiples_of_9_avg}")

# start, end = get_input()
# analyze_range(start, end)
#task5
# def get_input():
#     length = int(input("Введіть довжину лінії: "))
#     symbol = input("Введіть символ для заповнення лінії: ")
#     return length, symbol
# def draw_vertical_line(length, symbol):
#     for _ in range(length):
#         print(symbol)
# length, symbol = get_input()
# draw_vertical_line(length, symbol)
#task6
# while True:
#     number = float(input("Введіть число: "))
#     if number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     elif number == 0:
#         print("Number is equal to zero")
#     if number == 7:
#         print("Good bye!")
#         break
#task7
# def main():
#     total_sum = 0
#     max_num = None
#     min_num = None

#     while True:
#         number = float(input("Введіть число: "))

#         if number == 7:
#             print("Good bye!")
#             break

#         total_sum += number

#         if max_num is None or number > max_num:
#             max_num = number

#         if min_num is None or number < min_num:
#             min_num = number

#         print(f"Сума: {total_sum}, Максимум: {max_num}, Мінімум: {min_num}")

# main()
