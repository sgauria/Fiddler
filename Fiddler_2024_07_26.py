# Fiddler 2024 07 26
# https://thefiddler.substack.com/p/can-you-even-the-odds

# Let a,b,c be the probabilities that A wins, B wins, and no one wins ("Continue playing").
# And let a_k, b_k, c_k be the probabilities after k rounds of Thue-Morse.
# Let j = k-1.

# Because round k consists of round j plus an inverted copy of round j, we can derive

# a_k = a_j + c_j*b_j
# b_k = b_j + c_j*a_j
# c_k = c_j * c_j

# And we know that
# a_1 = 1/6
# b_1 = 0
# c_1 = 5/6

# With this, we can calculate forward the a,b,c values for higher k.
# On my computer's precision, this python code "converged" after 13 rounds to 
# Thue-Morse: round=13, a=0.5015903392042692, b=0.4984096607957311, c=0.0

# This compares well to :
# Snake: AB:BA:  a =  0.5081967213114754

# And the classic:
# AB:AB:  a =  0.5454545454545454

from fractions import Fraction

N = 12
USE_FRAC = False

if (USE_FRAC):
    a = Fraction(1,6)
    b = Fraction(0,1)
    c = Fraction(5,6)
else:
    a = 1/6
    b = 0
    c = 5/6
r = 1

for i in range(N):
    a_new = a + c*b
    b_new = b + a*c
    c_new = c*c
    a,b,c,r = a_new,b_new,c_new,(r+1)
    # print (f"Thue-Morse: round={r}, a={a}, b={b}, c={c}")
   
print ("Turns: AB:AB:  a = ", 6/11)
print ("Snake: AB:BA:  a = ", 31/61)
print (f"Thue-Morse: round={r}, a={a}, b={b}, c={c}")

