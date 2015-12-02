print "Welcome to my Awesome Python Quiz Game!" + "\n"
name = raw_input("What is your name? ")

# these strings will be used to provide the quiz questions.  Some of these definitions are from https://en.wikibooks.org and www.tutorialspoint.com.
easy_quiz = """A __1__ is a list of characters in order that can be created by enclosing the characters in quotes.  A __2__ is something that holds a value that may change.  A __3__ is a data type that holds an ordered collection of values surrounded by square bracket, which can be of any type.	A function that displays the output of a program is called __4__. """
medium_quiz = """A __1__  loop permits code to run until a defined condition is met.  However a __2__ loop is used when you want to run a piece of code n number of times.  A __3__ is a block of organized, reusable code that is used to perform a single related action. To create one of these you will start with the __4__ keyword followed by whatever name you want to use, followed by parentheses."""
hard_quiz = """__1__  is the process of figuring out what the computer is doing and then getting it to do what YOU want it to do. One of the best ways to fix bugs in your code is to add __2__ statements to your program to see when things stop behaving correctly. You can also examine error messages called __3__ which will tell you what went wrong. The most relevant information can be found on the last line.  If you can't figure out the problem after an hour or so take a __4__ and come back to it."""

# These are the correct answers to the various levels of questions
easy_word = ["string", "variable", "list", "print"]
medium_word = ["while", "for", "function", "def"]
hard_word = ["debugging", "print", "tracebacks", "break"]

blank_position = ["__1__", "__2__", "__3__", "__4__"]  # These are the blank positions which will be replaced eventually with the users answers.
quiz = [easy_quiz, medium_quiz, hard_quiz]  #Creates a global variable for the quiz list
words = [easy_word, medium_word, hard_word] #Creates a global variable for the words list


# This plays the actual game.  We pass in two varaibles quiz and words which are used to ask the user to fill in the blanks.  
def play_game(quiz, words):
    index = 0
    while index < 4:
        answer = raw_input("What goes in blank " + str(index + 1) + ":")
        if answer == words[index]:
            quiz = quiz.replace(blank_position[index], answer, 1)
            print "Great Job!"
            index += 1
        else:
            print "Sorry please guess again!"
    end_game(quiz)  # calls the end game function


# This tells the program which level of questions/answers, depending on the select_difficulty entry.
def difficulty():
    select_difficulty = raw_input("When Ready Please select a level -->> (Easy/Medium/Hard): ".lower())
    if select_difficulty == "easy":
        print easy_quiz
        play_game(easy_quiz, easy_word)
    elif select_difficulty == "medium":
        print medium_quiz
        play_game(medium_quiz, medium_word)
    elif select_difficulty == "hard":
        print hard_quiz
        play_game(hard_quiz, hard_word)
    else:
        print ("Sorry, please enter your selection again!")
        difficulty()

# this function calls the end of the game and asks the user if they want another quiz otherwise the game is over.
def end_game(quiz):
	print (quiz + "\n" + "You beat my game Congrats! " + name)
	replay = raw_input("Do you want to play again?")
	if replay == "yes":
		difficulty()
	else:
		print ("Thanks for playing")

difficulty()
