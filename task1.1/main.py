n = int(input("Введите число: "))


one = n % 10
tens = (n % 100) // 10
hundreds = (n % 1000) // 100

sum = hundreds + tens + one
res = sum 

print(res, '(',hundreds, '+', tens, '+', one, ')')