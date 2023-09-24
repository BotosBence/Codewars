# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
# def solution(string):
#     return string[::-1]
#
#
# print(solution("world"))


# def greet():
#     return "".join({1: [i for i in "hello world!"]}.get(1))
#
#
# print(greet())


# def square_digits(num):
#     p, o = '', lambda x: str(int(x)**2)
#     return int("".join([o(i) for i in str(num)]))
#
#
# print(square_digits(239))


# def find_short(s):
#     return min(len(i) for i in s.split())
#
#
# print(find_short("bitcoin take over the world maybe who knows perhaps"))


# def expanded_form(num):
#     a, b = [str(int(list(reversed(str(num)))[i]) * (10 ** i)) for i in range(len(str(num)))][::-1], []
#     [b.append(k) if k != "0" else "HELLO WORLD!" for k in a]
#     return " + ".join(b)
#
# print(expanded_form(70304))


# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"
#
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))