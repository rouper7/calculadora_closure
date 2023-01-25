# calculadora_closure
1.Define a main function called "sinal" that takes in a parameter "sinal" as input, which can be '+' for addition, '-' for subtraction, '/' for division, '*' for multiplication.

2.Inside the "sinal" function, define a nested function called "calcular" that takes in two parameters, "x" and "y".

3.Inside the "calcular" function, check the value of the "sinal" parameter passed to the main "sinal" function and return the corresponding mathematical operation result between "x" and "y" (for example, "x-y" for "sinal" = "-"). If the passed sign is not recognized, return an error message.

4.Return the "calcular" function at the end of the "sinal" function.
Example of use:
sub = sinal("-")
result = sub(5,3)
print(result)  # Output: 2

In this example, we create a variable called "sub" by calling the "sinal" function with "-" as an argument. Then we use the returned function, "calcular" to perform the subtraction operation with 5 and 3 and store the result in the variable "result" and finally we print the result.
