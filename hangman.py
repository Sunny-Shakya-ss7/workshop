import random
import turtle

class Hangman:
    def __init__(self):
        self.word, self.hint = self.pickAword()
        self.wordList = [self.word[i] for i in range(len(self.word))]
        self.guessList = ['-' for _ in range(len(self.word))]
        self.pastGuess = []
        self.guessCount = 0
        self.game_over = False

    def checkWord(self, guess):
        if self.game_over:
            return

        # Check if the character has been guessed before
        if guess in self.guessList:
            return

        # Add the guess to past guesses
        self.pastGuess.append(guess)

        # Variable to track if the guess is correct
        result = False
        for i, ch in enumerate(self.wordList):
            if guess == ch:
                self.guessList[i] = ch
                result = True

        if result == False:
            self.guessCount += 1

        ## game end conditions - start ##

        # Check if game should end due to too many incorrect guesses
        if self.guessCount >= 6:
            self.game_over = True
            twrite.goto(-100, 400)
            twrite.write("YOU LOST!!!", font = ("Arial", 20, "bold"))

            # reveal word if game lost
            twrite.goto(-300, -150)
            twrite.write("Word was: ")
            twrite.goto(-200, -150)
            twrite.write(hm.word, font = ("Arial", 10, "bold"))

        # Check if player has won
        elif '-' not in self.guessList:
            self.game_over = True
            twrite.goto(-100, 400)
            twrite.write("You WON!!!", font = ("Arial", 20, "bold"))

        ## game end conditions - start ##

        return result

    def pickAword(self):
        wordList = [
            ("python", "A snake that doesn't bite."),
            ("ruby", "A type of jewel."),
            ("apple", "Keeps the doctor away!"),
            ("banana", "Monkeys love this!"),
            ("cookie", "The internet tracks you with this treat!"),
            ("spider", "Eight legs and loves corners."),
            ("broom", "Witches love flying on it."),
            ("cloud", "Fluffy thing in the sky."),
            ("ghost", "A spooky friend you can't see!"),
            ("pillow", "Your head's best friend at night."),
            ("blanket", "Keeps you warm and cozy."),
            ("pizza", "Everyone’s favorite triangle."),
            ("socks", "Keep your feet warm, and often go missing."),
            ("jelly", "Wobbles on a plate, great on toast."),
            ("shampoo", "Keeps your hair fresh and clean."),
            ("dinosaur", "Big, extinct lizards from a movie!"),
            ("whale", "A giant that sings in the sea."),
            ("cactus", "Prickly plant that loves deserts."),
            ("unicorn", "A magical horse with a horn!"),
            ("robot", "A metal friend who follows commands."),
            ("carrot", "Bugs Bunny’s favorite snack."),
            ("beach", "Sand, sun, and waves."),
            ("toothbrush", "Keeps your smile bright!"),
            ("panda", "A cute black-and-white bamboo eater."),
            ("kangaroo", "Jumps around with a pouch."),
            ("snowman", "Only around in winter, likes to melt."),
            ("guitar", "Rock stars love to play this."),
            ("chocolate", "Melts in your mouth, not in your hand!"),
            ("dragon", "Breathes fire and loves treasure."),
            ("wizard", "A magical person with a long beard."),
            ("donut", "Round treat with a hole in the middle."),
            ("chair", "Sit on it, but don’t stand on it!"),
            ("window", "Let's you see outside without going out."),
            ("pirate", "Loves treasure and says 'Arrr!'"),
            ("lemon", "Sour, yellow, and makes lemonade."),
            ("alien", "A friend from outer space?"),
            ("burger", "Stacked with buns, lettuce, and more."),
            ("giraffe", "Tall animal with a long neck."),
            ("vampire", "Avoids garlic and loves the night."),
            ("popcorn", "Best snack at the movies."),
            ("kitten", "A baby cat with tiny paws."),
            ("rainbow", "Comes after rain, full of colors."),
            ("cheese", "Mice love it, comes in slices."),
            ("puzzle", "Pieces come together to make a picture."),
            ("treasure", "Pirates love searching for this."),
            ("lighthouse", "Guides ships safely at night."),
            ("koala", "Cute and cuddly, loves eucalyptus."),
            ("butterfly", "Starts as a caterpillar, becomes pretty."),
            ("sushi", "Fish and rice rolled up tight."),
            ("rocket", "Blasts off to space!"),
            ("icecream", "Cold treat on a hot day."),
            ("popstar", "Sings and has lots of fans."),
            ("hamster", "Small, furry, and loves to run in wheels."),
            ("puzzle", "Has pieces that fit together to make a picture."),
            ("firefly", "Tiny insect that lights up at night."),
        ]

        return random.choice(wordList)


####################
### Turtle ###
####################

scale = 50

# for drawing
t = turtle.Turtle()
t.speed(0)
t.ht()

# for writing
twrite = turtle.Turtle()
twrite.speed(0)
twrite.ht()
twrite.penup()

scr = turtle.Screen()

def drawHangman(stage):
    t.clear()
    t.penup()
    t.goto(200,-60)
    t.seth(0)
    t.pendown()

    # frame
    t.width(5)
    t.forward(scale * 2)
    t.backward(scale)
    t.seth(90)
    t.forward(scale * 4)
    t.seth(180)
    t.forward(scale)
    t.seth(270)
    t.forward(scale)

    if stage < 1: return

    ## Man ##

    # head
    t.seth(180)
    t.circle(scale // 2)

    if stage < 2: return

    # body
    t.seth(270)
    t.penup()
    t.forward(scale)
    t.pendown()
    t.forward(scale)

    # legs

    if stage < 3: return

    t.right(30)
    t.forward(scale // 2)
    t.backward(scale // 2)

    if stage < 4: return

    t.left(60)
    t.forward(scale // 2)
    t.backward(scale // 2)

    # hands

    if stage < 5: return

    t.seth(90)
    t.forward(scale // 1.5)
    t.seth(270)
    t.right(30)
    t.forward(scale // 2)
    t.backward(scale // 2)

    if stage < 6: return

    t.left(60)
    t.forward(scale // 2)
    t.backward(scale // 2)

    t.seth(90)
    t.penup()
    t.forward(scale // 1.5)
    t.seth(180)
    t.forward(scale // 3.5)
    t.write("DEAD")




####################
### Main Program ###
####################

hm = Hangman()

drawHangman(hm.guessCount)

def display():
    # guess list
    twrite.goto(-300, 100)
    for ec in hm.guessList:
        twrite.write(ec, font = ("Arial", 16, "bold"))
        twrite.forward(30)

    # hint
    twrite.goto(-300, -20)
    twrite.write("Hint:")
    twrite.goto(-200, -20)
    twrite.write(hm.hint)

    # past guesses
    twrite.goto(-300, -50)
    twrite.write("Past Guess: ")
    twrite.goto(-200, -50)
    for ec in hm.pastGuess:
        twrite.write(ec)
        twrite.forward(10)

    # chances left
    twrite.goto(-300, -80)
    twrite.write("Chances Left: ")
    twrite.goto(-200, -80)
    twrite.write(6 - hm.guessCount)

    # Ensure it's shown in a visible location
    if hm.game_over:
        if '-' not in hm.guessList:
            twrite.goto(-100, 200)
            twrite.write("You WON!!!", font=("Arial", 20, "bold"))
        elif hm.guessCount >= 6:
            twrite.goto(-100, 200)
            twrite.write("YOU LOST!!!", font=("Arial", 20, "bold"))

twrite.goto(-100, 0)
display()

def keyANY(guess):
    global hm
    twrite.clear()

    # Check game over flag before allowing input
    if hm.game_over:
        return

    hm.checkWord(guess)

    display()

    drawHangman(hm.guessCount)

# for accepting letters in turtle
for letter in 'abcdefghijklmnopqrstuvwxyz':
    scr.onkey(lambda letter=letter: keyANY(letter), letter)

scr.listen()
scr.mainloop()