import math

hex_dict = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

def solve_quadratic(a, b, c):
    if a == 0:
        return
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        return (((-b + sqrt_val) / (2 * a)), ((-b - sqrt_val) / (2 * a)))
    
    elif dis == 0:
        return (-b / (2 * a))

def to_hex(x):
    quotient = x // 16;
    remainder = x % 16;

    if remainder > 9:
        remainder = hex_dict[remainder]
    
    if quotient == 0:
        return remainder
    else:
        return str(to_hex(quotient)) + str(remainder)

def hex_code(a, b, c):
    numbers = [a, b, c]
    
    a = to_hex(a)
    b = to_hex(b)
    c = to_hex(c)
    
    if len(a) < 2: 
        a = "0" + a
    if len(b) < 2: 
        b = "0" + b
    if len(c) < 2: 
        c = "0" + c

    return "#" + a + b + c
     
def my_range(m,n):
    my_list = []

    while m < n:
        my_list.append(m)
        m += 1
    
    return my_list

def my_reverse(l):
    reversed_list = []
    i = len(l) - 1
    while i >= 0:
        reversed_list.append(l[i])
        i -= 1
    return reversed_list

def big_fibonacci(n):
    num = 1
    num_1 = 1
    while len(str(num)) != n:
        num_2 = num_1
        num_1 = num
        num = num_1 + num_2
    return num

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    return

def is_prime(n):
    if n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

def primes_below(n):
    primes_list = []
    for i in range(0, n):
        if is_prime(i):
            primes_list.append(i)
    return primes_list

def palindrom_primes():
    pali_list = []
    for i in range(10000, 100000):
        if is_prime(i):
            if str(i) == str(i)[::-1]:
                pali_list.append(i)
    return pali_list

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        return (1/4) * math.sqrt((self.a ** 2 + self.b ** 2 + self.c ** 2)**2 - 2*(self.a ** 4 + self.b ** 4 + self.c ** 4))

    def perimeter(self):
        return self.a + self.b + self.c
    
    def scale(self, scale_factor):
        return Triangle(self, scale_factor * self.b, scale_factor * self.a,scale_factor * self.c)

    def is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False
    
    def is_right(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2:
            return True
        if self.a ** 2 + self.c ** 2 == self.b ** 2:
            return True
        if self.c ** 2 + self.b ** 2 == self.a ** 2:
            return True
