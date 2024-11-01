# Random Password Generator (Beginner)

Create a program that will ask:

+ How many letters would you like in your password?
+ How many symbols would you like?
+ How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password.

## Easy Version

Generate the password in sequence. Letters, then symbols, then numbers.

If the user wants:
4 letters 2 symbols and 3 numbers then the password might look like this:

`fgdx$*924`

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well.

## Hard Version

In the advanced version of this project the final password does not follow a pattern.

So the example above might look like this:

`x$d24g*f9`

And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.
