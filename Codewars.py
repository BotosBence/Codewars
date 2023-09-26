# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
# def solution(string):
#     return string[::-1]
#
#
# print(solution("world"))
#
#
# def greet():
#     return "".join({1: [i for i in "hello world!"]}.get(1))
#
#
# print(greet())
#
#
# def square_digits(num):
#     p, o = '', lambda x: str(int(x) ** 2)
#     return int("".join([o(i) for i in str(num)]))
#
#
# print(square_digits(239))
#
#
# def find_short(s):
#     return min(len(i) for i in s.split())
#
#
# print(find_short("bitcoin take over the world maybe who knows perhaps"))
#
#
# def expanded_form(num):
#     a, b = [str(int(list(reversed(str(num)))[i]) * (10 ** i)) for i in range(len(str(num)))][::-1], []
#     [b.append(k) if k != "0" else "HELLO WORLD!" for k in a]
#     return " + ".join(b)

#
# print(expanded_form(70304))
#
#
# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"
#
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
#
#
# def simple_multiplication(number):
#     return number * 9 if number % 2 == 1 else number * 8
#
#
# print(simple_multiplication(2))
#
#
# def area_or_perimeter(l, w):
#     return l * w if l == w else (l + w) * 2
#
#
# print(area_or_perimeter(6, 10))
#
#
# def solution(s):
#     return "".join([" " + i if i.lower() != i else i for i in s])
#
#
# print(solution("helloWorld"))
#
#
# def double_integer(i):
#     return int(i) * 2
#
#
# print(double_integer(2))
#
#
# def find_smallest_int(arr):
#     return min(arr)
#
#
# print(find_smallest_int([3, 534, 23, -4, 55]))
#
#
# def bmi(weight, height):
#     return ["Underweight" if (weight / height ** 2) <= 18.5 else "Normal" if (
#                                                                                          weight / height ** 2) <= 25.0 else "Overweight" if (
#                                                                                                                                                         weight / height ** 2) <= 30.0 else "Obese"]
#
#
# print(bmi(50, 1.80))  # Underweight
#
#
# def basic_op(operator, value1, value2):
#     return value1 + value2 if operator == "+" else value1 - value2 if operator == "-" else value1 / value2 if operator == "/" else value1 * value2
#
#
# print(basic_op("+", 3, 4))
#
#
# def find_average(numbers):
#     return float(sum(numbers) / len(numbers)) if len(numbers) > 0 else 0
#
#
# print(find_average([1, 2]))
#
#
# def no_space(x):
#     return x.replace(" ", "")
#
#
# print(no_space("232 sad2e f"))
#
#
# def get_volume_of_cuboid(length, width, height):
#     return length * width * height


def count_smileys(arr):
    return int()


print(count_smileys([':D', ':~)', ';~D', ':)']))
