# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

mul_of_3 = []
mul_of_5 = []
sum_of_3 = 0
sum_of_5 = 0

#Multiples of 3
for i in range(1000):
    if (i) % 3 == 0:
        mul_of_3.append(i)
        sum_of_3 = sum_of_3 + (i)

#Multiples of 5 - Mltiples of 3
for i in range(1000):
    if (i) % 5 == 0:
        if (i) % 3 != 0:
            mul_of_5.append(i)
            sum_of_5 = sum_of_5 + (i)

print("Sum of threes: " + str(sum_of_3) + "\nSum of fives: " + str(sum_of_5) +
 "\nSum: " + str((sum_of_3+sum_of_5)))
