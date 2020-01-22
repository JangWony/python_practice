# numeric type
## Integer
Int_a = 123
Int_b = -123
Int_c = 0
## float
float_a = 1.2
float_b = -1.23
float_c = 1.23E10
float_d = 1.23E-10
## Octal
Oct_a = 0o123
## Hex
Hex_a = 0x1FE
## Operation
a = 3
b = 4
a + b # addition
a - b # subtraction
a * b # multiplication
a / b # distribution
a % b # remainder
a // b # quotient
a ** b # power

# string type
'Hello, World!'
"Bye, World..."
'''Nice to meet you, World'''
"""Look  so cool, World"""
##escape code
""" 
\n is change line
\t is tap
\\ is just '\'
\' is just '
\" is just "
\r is carriage return,  move cursor to first
\f is form feed, move cursor to next line
\a is alarm
\b is back space
\000 is null character
""" 
## string operation
head = "Hello, "
tail = "World!"
body = head + tail # Hello, World!
twobody = body * 2 # Hello, World!Hello, World!

anything = 'all ok'
## length
len(anything) # 6
## indexing
anything[4] # o
## slicing
anything[0:3] # 'all'
anything[:3] # 'all'
anything[4:] # 'ok'

##formatting
"I eat %d apples." % 3 # 'I eat 3 apples'
"I eat %s apples." % "five" #  'I eat five apples'
number = 3
"I eat %d apples." % number # 'I eat 3 apples'
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
#'I ate 10 apples. so I was sick for three days."

#String format code
'''
%s : string
%c : character
%d : Integer
%f : floating-point
%o : octal digit(8)
%x : hexadecimal digit(16)
%% : Literal %
''' 
