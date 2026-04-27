"""
Types of Tokens:-
Punctuators:- are symbols to organize sentence structure in programming.

() , {}, [], # etc.

"""

# Expression Execution

# 1) String and Numeric values can operate with *.

A,B = 2 , 3

TXT= "@"
print(2*TXT*3)


# 2) Strings & Stirng can operate with +

A,B = "2",3
TXT = "@"
print((A+TXT)*B)

# 3) Numeric values can operate with all arithmetic Operators.

A,B = 3 , 4
C = 5
print(A+B*C)


# 4) Arithmetic Expressions with integer and float will result in float.

A,B=10,5.0
C=A*B
print(C)

# 5) Result of division operator with two integers will be float

A,B = 1,2
C = A/B
print(C)

# 6) Integer Division with float and int will give int displayed as float 

A,B = 1.5,3
C = A//B
print(C , A/B)

# 7) floor gives closest integer , which is lesser than or equal to the float value 
# Result of (A//B) is same as floor(A/B)

A,B = 10 , 5
C = A//B
print(C)

A,B = -12 , 5
C = A//B
print(C)

A,B = 12 , -5
C = A//B
print(C)

# 8) Remainder is -ve when denominator is -ve.

A,B = -5 , 2
C = A%B
print(C)

A,B = 5 , 2
C = A % B
print(C)

A,B = 5 , -2
C = A % B
print(C)
