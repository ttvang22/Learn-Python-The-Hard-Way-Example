#Exercise: 1 A Good First Program

print "Hello World"
print "Hello Again"
print "I like typing this"
print "This is fun"
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

#Exercise 2: Comments and Pound Characters
#This Is A Comment and This is how you do it

#Exercise 3: Numbers and Math
$ python ex3.py
print "I will now count my chickens"

print "Hens" , 25 + 30 / 6
print "Roosters" , 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 < 5 - 7

print "What is 3 + 2" , 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's false"

print "How about some more."

print "Is it greater?" ,  5> -2
print "Is it greater or equal?" ,  5 >= -2
print "Is it less or equal?" , 5 <= -2

#Exercise 4:  Variables And Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capcity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are" , cars, "cars available."
print "There are only" , drivers, "drivers availbale."
print "There will be" , cars_not_driven, "empty cars today."
print "We can transport" , carpool_capcity, "people today."
print "We need to put about" , average_passengers_per_car, "in each car."

#Exercise 5 More Variables and Printing
my_name = "Tou T. Vang"
my_age = 26 #For Real
my_height = 65 #inches
my_weight = 175 #pounds
my_eyes = 'Brown'
my_teeth = 'White' #kinda yellow
my_hair= 'Black'

print "Let's talk about %s" % my_name
print "He's %d inches talk" % my_height
print "He's %d pound heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

 #this line is tricky, try to get it exactly right

print "If I ad %d, %d, and %d I get %d." %( my_age, my_height, my_weight, my_age + my_height + my_weight)

#Exercise 6: Strings and Text
x = "There are &d types of people" % 10
binary = "binary"
do_not = "don't"
y= "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

#Exercise 7: More Printing

print "Mary had a little lamb."
print "Its fleece was white as %s." % "snow"
print "And everywhere that Mary went."
print "." * 10 #What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#Exercise 8: Printing, Printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right."
    "Bud it didn't sing."
    "So I said goodnight."
)

#Exercise 9: Printing, Printing, Printing
#Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJuly\nAug"

print "Here are the days: ", days
print "Here are the months: " , months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#Exercise 10: What Was That?
tabby_cat = "\iI'm tabbed in."
persian_cat = "I'm slit\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Escape	What it does.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (u'' string only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

#Exercise 11: Asking Questions
print "How old are you?" ,
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Exercise 12: Prompting People
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Exercise 13: Parameters, Unpacking, Variables
from sys import argv

script, first, second, third = argv

print "The script is called: " , script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Exercise 14: Prompting and Passing
from sys import argv

script, user_name = argv
prompt = ">"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes - raw_input(prompt)

print "Where do you live %s?" %user_name
lives= raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you say %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)

#Exercise 15: Reading Files
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = raw_input("> ")

print txt_again.read()

#Exercise 16: Reading and Writing Files
#close -- Closes the file. Like File->Save.. in your editor.
#read -- Reads the contents of the file. You can assign the result to a variable.
#readline -- Reads just one line of a text file.
#truncate -- Empties the file. Watch out if you care about the file.
#write('stuff') -- Writes "stuff" to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that , hit RETURN."

raw_input("?")

print "Opening the file..."
target = open (filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it"
target.close()

#Exercise 17: More Files
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to _file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" %  exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input

out_file = open(to_file, "w")
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()

#Exercise 18: Names, Variables, Code, Functions

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actuall pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no agruments
def print_none():
    print "I got nothing'."

print_two("Zed" , "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#"To 'run,' 'call,' or 'use' a function all mean the same thing."

#Exercise 19: Functions and Variables
def cheese_and-crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese= 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too: "
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+ 100, amount_of_crackers + 1000)

#Exercise 20: Functions and Files
from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#Exercise 21: Functions Can Return something
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - # BUG:

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height =  subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#Exercise 22: What Do You Know So Far?
#No Exercise/ Just Review

#Exercise 23: Read Some code
#No Exercise/ Got On Git Hub To Read Some Codes
#User_name = ttvang22

#Exercise 24: More Practice
print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \\tabs.'

poem = """
\t The lovely World
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requres an explanation
\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point"
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

#Exercise 25: Even More Practice

#import ex25
#sentence = "All good things come to those who wait."
#words = ex25.break_words(sentence)
#words
#sorted_words = ex25.sort_words(words)
#sorted_words
#ex25.print_first_word(words)
#ex25.print_last_word(words)
#words
#ex25.print_first_word(sorted_words)
#ex25.print_last_word(sorted_words)
#sorted_words
#sorted_words = ex25.sort_sentence(sentence)
#sorted_words
#ex25.print_first_and_last(sentence)
#ex25.print_first_and_last_sorted(sentence)

def break_word(stuff):
    """ This functions will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """ Printst the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

 def sort_sentence(sentence):
     """Take in a full sentence and return sorted words"""
     words = break_words(sentence)
     return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Exercise 26: Congratulations, Take A Test

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off. """
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sorted_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

print_first_a_last_sorted(senence)

#Exercis 27: Memorizing Logic

#The Truth Terms
#In Python we have the following terms (characters and phrases) for determining if something is "True" or "False." Logic on a computer is all about seeing if some combination of these characters and some variables is True at that point in the program.

and
or
not
!= (not equal)
== (equal)
>= (greater-than-equal)
<= (less-than-equal)
True
False

#The Truth Tables
#We will now use these characters to make the truth tables you need to memorize.

NOT	True?
not False	True
not True	False
OR	True?
True or False	True
True or True	True
False or True	True
False or False	False
AND	True?
True and False	False
True and True	True
False and True	False
False and False	False
NOT OR	True?
not (True or False)	    False
not (True or True)	    False
not (False or True)	    False
not (False or False)	True
NOT AND	True?
not (True and False)	True
not (True and True)	    False
not (False and True)	True
not (False and False)	True
!=	True?
1 != 0	True
1 != 1	False
0 != 1	True
0 != 0	False
==	True?
1 == 0	False
1 == 1	True
0 == 1	False
0 == 0	True

#Exercise 28: Boolean Practice

True and True =     True
False and True =    False
1==1 and 2==1 =     False
"test" == "test"=   True
1 == 1 or 2 != 1 =  True
True and 1 == 1 =   True
False and 0 != 0 =  False
True == 1 == 1 =    True
"test" == "testing"=False
"test" == 1 =       True
not (True and False) =      True
not (1 == 1 and 0 != 1) =   True
not (10 == 1 and 3 == 4 ) = True
not ("testing" == "testing" and "Zed" == "Cool Guy") = True
1 == 1 and (not ("testing" == 1 or 1 == 0)) = False
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) =     True
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) = True

# Exercise 29: What if

people = 20
cats = 30
dogs = 15

if people (20) < cats: (30)
    print "Too many cats! The world is doom"

if people (20) > cats (30):
    print "Not many cats! The world is save"

if people (20) < dogs (15):
    print "The world is drooled on!"

if people (20) > dogs(15):
    print "The world is dry"

dogs += 5

if people(20) >= dogs(15 + 5):
    print "People are greater than or equal to dogs."

if people (20) <= dogs:(15 + 5)
    print "People are less than or equal to dogs"

if people (20) == dogs (15+5):
    print "People are dogs."

#Exercise 30: Else and If

people = 30
cars = 40
trucks = 15


if cars (40) > people (30):
    print "We should take the cars."
elif cars (40) < people (30):
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks (15) > cars (40):
    print "That's too many trucks."
elif trucks (15) < cars (40):
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people (30) > trucks (15):
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."


#Exercise 31: Making Decision

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"

#Exercise 32: Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i


#Exercis 33: While Loops
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

#Exercise 34: Accessing Elements of Lists
#List Goes by [0, 1, 2, 3, 4, 5]

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
bear = animals[0]

python = animals[1]
peacock = animals[2]
bear = animals[0]
kangaroo = animals[3]
whale = animals[5]
peacock = animals[2]
platypus = animals[6]
whale = animals[4]

#Exercise 35: Branches and Functions

from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

#Exercise 36: Designing and Debugging

#Exercise 37: Symbol Review

#Exercise 38:  Doing Things to Lists

ten_things = "Apples Oranges Crow Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff= ["Day" , "Night", "Song", "Frisbee", "Corn" , "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding: " , next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do somethings with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

#Exercise 39: Dictionaries, Oh Lovely Dictionaries

#Exercise 40: Modules, Classes, and Objects

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics:

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday= Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"]
                )

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song

#Exercise 41: Learning to Speak Object Oriented

#Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-A
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## has-a
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## has-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## has-a
mary.pet = satan

## has-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## is-a
harry = Halibut()

#Exercise 43: Basic Object-Oriented Analysis and Design
 Blah Blah
