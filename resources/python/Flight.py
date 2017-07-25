__author__ = 'inatiwari'

"""Model for AirCraft Flights"""


class Flight(object):

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No Airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code is '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid Route Number '{}".format(number))

        self._number = number

    def number(self):
        return self._number

    def addition(self):
        a=  1
        b=  2
        c=  a + b
        assert c == 1,  "Calculation is wrong and function should return {}".format(c)
        return c

    def multiplecation(self,x,y):
        x=  int(x)
        y= int(y)
        k= int(10)
        z = x * y
        assert z == x * y * k,  "Calculation is wrong and function should return {}".format(z)
        return z

    def airline(self):
        return self._number[:2]

    def airthmaticoperators(self,num1,num2):
        num1 = int(num1)
        num2 = int(num2)
        print ("num1 + num2 =", num1 + num2)
        print ("num1 * num2 =", num1 * num2)
        print ("num1 - num2 =", num1 - num2)
        print ("num1 / num2 =", num1 / num2)
        print ("exponential power of 5 like 5^3 =", 5**3)
        print ("Modulas operator of 20 % 3  =", 20 % 3)
        print ("Float devision 20 // 7 =", 22 // 7)
        print ("Float devision 3.8 // 2 =", 3.8 // 2)

    def assignmentoperators(self,num1,num2,num3,num4):
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        num1/=20
        num2%=20
        num3//=20
        num4**=20
        print (num1)
        print (num2)
        print (num3)
        print (num4)

    def bitwiseoperator(self,num1,num2):
        num1 = int(num1)    #0110
        num2 = int(num2)    #0010
        print("Bitwise and =", num1 & num2)
        print("Bitwise OR =", num1 | num2)
        print("Bitwise XOR =", num1 ^ num2)
        print("num1 right shift by 2", num1 >> 2)
        print("num2 left shift by 2", num2 << 2)

    def forloop(self,n):
        n = int(n)
        for number in range(n):
            print number

    def fibnaci(self,n):
        n = int(n)
        f1, f2 = 0, 1
        for number in range(n):
            f1 = f2
            f2 += f1
            print f2



