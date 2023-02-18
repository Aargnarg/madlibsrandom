#
#this is my code that aims to generate random madlib stories then fill them randomly
#it will ask for 10 words of each category that will show up (some used less than others)
#then will choose a random madlib (out of 10) and fill it with random words from the apropriate categories
#some stories do need aditional inputs. 
#
#then the program will print out the story and you can choose to redo the same story (with new random words) or random story
#

#using the random library to use random.choise to choose random stories and random words
import random

#this is if the user wants to redo the words they created.
def RedoWords(allWords):
    allWords = GetWordLists()
    return allWords

#GetWordLists() will return list of lists of the words that the user inputs. they are subcategoried into their appropriate categories
def GetWordLists(): 

    #note that since I split using comma, people generally put a space before every word besides the first one.
    #to keep the words from being saved with the leading whitespace I use strip()
    properNouns = [x.strip() for x in input("\nPlease give me proper nouns separated by commas: ").split(",")]    #using comma as delimiter since some proper nouns have spaces like New Vegas and Bob Smith.
    nouns = [x.strip() for x in input("Please give me nouns separated by commas: ").split(",")]
    adjs = [x.strip() for x in input("Please give me adjectives separated by commas: ").split(",")]
    verbs = [x.strip() for x in input("Please give me verbs separated by commas: ").split(",")]
    adverbs = [x.strip() for x in input("Please give me adverbs spaced by commas: ").split(",")]
    colors = [x.strip() for x in input("Please give me colors separated by a commas: ").split(",")]
    foods = [x.strip() for x in input("Please give me foods separated by commas: ").split(",")]
    numbers = [x.strip() for x in input("Please give me numbers separated by commas: ").split(",")]

    allWords = {'noun' : nouns, 'properNoun' : properNouns, 'adj': adjs, 'verb' : verbs, 'color' : colors, 'food' : foods, 'adverb':adverbs,'number':numbers}
    return allWords

#GetMadLibs() will return a list that is composed of 10 tuples. the first tuple is a random story, the second is a list of tuples
#the second list of tuples will give the information of what types of words are there and how many (adj, nouns, etc)
#this is needed for when the program will combine the words with the stories
def GetMadLibs():
    madLibs1 = """\nToday I went to the zoo. I saw a(n) {0[adj][0]}
{0[noun][0]} jumping up and down in its tree.
It {0[verb][0]}ed (past tense) {0[adverb][0]}
through the large tunnel that led to its {0[adj][1]}
{0[noun][1]}. I got some peanuts and passed
them through the cage to a gigantic gray {0[noun][2]}
towering above my head. Feeding that animal made
me hungry. I went to get a {0[adj][2]} scoop
of ice cream. It filled my stomach. Afterwards I had to
{0[verb][1]} {0[adverb][1]} to catch our bus.
When I got home I {0[verb][2]}ed (past tense) my
mom for a {0[adj][3]} day at the zoo."""

    madLibs1Det = [("adj", 4), ("noun", 3), ("verb", 3), ("adverb", 2)]

    madLibs2 = """\nToday, my fabulous camp group went to a (an)
{0[adj][0]} amusement park. It was a
fun park with lots of cool {0[noun][0]}s (plural)
and enjoyable play structures. When we got there, my
kind counselor shouted loudly, "Everybody off the
{0[noun][1]}." We all pushed out in a terrible
hurry. My counselor handed out yellow tickets, and
we scurried in. I was so excited! I couldn't figure out
what exciting thing to do first. I saw a scary roller
coaster I really liked so, I {0[adverb][0]} ran
over to get in the long line that had about
{0[number][0]} people in it. When I finally
got on the roller coaster I was {0[verb][0]}ed (past tense). 
In fact I was so nervous my two knees
were knocking together. This was the {0[adj][1]}est
ride I had ever been on! In about two
minutes I heard the crank and grinding of the gears.
That's when the ride began! When I got to the bottom,
I was a little {0[verb][1]}ed (past tense) but I
was proud of myself. The rest of the day went
{0[adverb][1]}. It was a(n) {0[adj][1]} 
day at the fun park."""

    madLibs2Det = [("adj", 2), ("noun", 2), ("adverb", 2), ("number", 1), ("verb", 2)]

    madLibs3 = """\nWhen I go to the arcade with my {0[noun][0]}s (plural)
there are lots of games to play. I spend
lots of time there with my friends. In the game X-Men
you can be different {0[noun][1]}s (plural). The
point of the game is to {0[verb][0]} every
robot. You also need to save people. Then you can
go to the next level.
 In the game Star Wars you are Luke Skywalker
and you try to destroy every {0[noun][2]}. In
a car racing/motorcycle racing game you need to beat
every computerized vehicle that you are
{0[verb][1]}ing against.
There are a whole lot of other cool games. When
you play some games you win {0[noun][3]}s (plural)
for certain scores. Once you're done you can
cash in your tickets to get a big {0[noun][4]}. You
can save your {0[noun][5]}s (plural) for
another time. When I went to this arcade I didn't
believe how much fun it would be. So far I have had a
lot of fun every time I've been to this great arcade!"""

    madLibs3Det = [("noun", 6), ("verb", 2)]

    madLibs4 = """\nOne very nice morning near the end of summer,
my mother woke me up at 4:00 A.M. and said, "Wake
up and smell the grass, sleepy head! Today is your
first day of school and you can't be late." I groaned in
my bed for twenty seconds, but eventually I got
dressed. I wore a blue and white striped, long sleeve
{0[noun][0]} with a collar on it, a red tie,
dark gray pants, white socks, black shoes, and a(n)
{0[adj][0]} hat. In ten minutes I made
lunch and ate my breakfast. {0[number][0]}
minutes later, the bus came. A few minutes later, I
was at school.
In school, I met two really
{0[adj][1]} kids. All of us became
friends very fast. That day we had Science, and
luckily my friends and I were at the same
{0[noun][1]}. My friends' names are
{0[properNoun][0]} and
{0[properNoun][1]}. In Math we weren't
together, and that really bugged me. We learned what
{0[noun][2]}s (plural) were, and when to use
them. At snack and recess, we played a game
together. It was extremely fun. At P. E., we were
{0[verb][0]}ing off of the ropes onto
{0[noun][3]}s (plural). I thought it was a very
{0[adj][2]} idea. In swimming class,
we needed to swim extremely
{0[adverb][0]}, or else we would have to
swim longer.
Before I knew it, school was over. I grabbed all
my belongings and put them into my backpack. In two
minutes, the bus came. As I stepped into the bus I
shouted, "Goodbye, adios amigos, and shalom," to
my friends. Then I went into the bus. In a flash, I was
back home. This day was an extremely exciting day!"""

    madLibs4Det = [("noun", 4), ("adj", 3), ("number", 1), ("properNoun", 2), ("verb", 1), ("adverb", 1)]

    madLibs5 = """\nI walk through the {0[color][0]} jungle. I take out my
{0[adj][0]} canteen. There's a
{0[adj][1]} parrot with a {0[adj][2]}
{0[noun][0]} in its mouth right there in front
of me in the {0[adj][3]} trees! I gaze at its
{0[adj][4]} {0[noun][1]}. A sudden
sound awakes me from my daydream! A panther's
{0[verb][0]} in front of my head! I
{0[verb][1]} his {0[adj][5]}
breath. I remember I have a packet of {0[noun][2]}
that makes anything go into a deep slumber! I
{0[verb][2]} it away from me in front of the
{0[noun][3]}. Yes it's eating it! I
{0[verb][3]} away through the
{0[adj][6]} jungle. I meet my parents at the
tent. Phew! It's been an exciting day in the jungle."""

    madLibs5Det = [("color", 1), ("adj", 7), ("noun", 4), ("verb", 4)]

    madLibs6 = """\nThe day I saw the Monkey King {0[verb][0]} was one of the most
interesting days of the year.\n
After he did that, the king played chess on his brother's
{0[noun][0]} and then combed his {0[adj][0]} hair with a
comb made out of old fish bones. Later that same day, I saw the
Monkey King dance {0[adverb][0]}
in front of an audience of kangaroos and wombats."""

    madLibs6Det = [("verb", 1), ("noun", 1), ("adj", 1), ("adverb", 1)]

    madLibs7 = """\nToday a """ + input("Please input an occupation (a job): ") + """ named 
{0[properNoun][0]} came to our school to talk to us about her job. 
She said the most important skill you need to know 
to do her job is to be able to {0[verb][0]} around 
(a) {0[adj][0]} {0[noun][0]}. She said it was easy for her to learn 
her job because she loved to {0[verb][1]} when she was 
my age--and that helps a lot! If you're considering her profession, 
I hope you can be near (a) {0[adj][1]} {0[noun][1]}. 
That's very important! If you get too distracted in that situation 
you won't be able to {0[verb][2]} next to (a) {0[noun][2]}!"""

    madLibs7Det = [("properNoun", 1), ("verb", 3), ("adj", 2), ("noun", 3)]

    madLibs8 = """\nKindergarten is great! Today we did an art project from {0[properNoun][0]}. 
We started by gluing {0[noun][0]}s (plural) together to form a {0[noun][1]}. 
Then we decorated it with paints we made from {0[food][0]}. 
After the art project, {0[properNoun][1]} brought in their dog named Mrs. {0[color][0]} for show and tell. 
Can you believe the dog could {0[verb][0]}? Right before the day was done, 
my teacher read us a new book called 'The {0[adj][0]} {0[noun][2]} 
from """+input("Please give me a made-up word: ")+"""'. I can't believe how fast the day went!"""

    madLibs8Det = [("properNoun", 2), ("noun", 3), ("food", 1), ("color", 1), ("verb", 1), ("adj", 1)]

    madLibs9 = """\nToday, every student has a computer small enough to fit into their
{0[noun][0]}. They can solve any math problemby simply
pushing the computer's little {0[noun][1]}s (plural). Computers 
can add, multiply, divide, and {0[verb][0]}ed (past tense). They 
can also {0[verb][1]}ed (past tense) better than a human. Some 
computers are """+input("Please give me a part of the body (plural): ")+""". Others have a/an 
{0[adj][0]} screen that shows all kinds of {0[noun][2]}s (plural) 
and {0[adj][1]} figures."""

    madLibs9Det = [("noun", 3), ("verb", 2), ("adj", 2)]

    madLibs10 = """\nOnce upon a time, I was working on a coding assignment for my internship 
in automating with python. The task was to create a program that 
would automate a tedious process that the company had been doing 
manually for years. I knew I had to get it done quickly and efficiently, 
but my mind was blank. I needed some inspiration.
So I took a break and went for a walk outside. The sun was shining and the birds 
were singing. I saw a group of {0[noun][0]} playing in the park, 
and a {0[adj][0]} dog chasing after a {0[color][0]} frisbee. 
I felt a rush of inspiration and ran back to my desk to start coding.
As I worked, I realized that I needed to use a {0[adverb][0]} approach 
to the problem. I decided to break the task down into smaller, 
more manageable pieces. I wrote a script that would {0[verb][0]} the data, 
and another that would {0[verb][1]} the results. I even added 
some fancy graphs and charts to make the output look more {0[adj][1]}.
After hours of coding, I finally finished the assignment. 
I hit the run button and held my breath as the program executed. 
To my relief, it worked perfectly! I had successfully automated the tedious task, 
and the company was impressed with my work. They offered me a job as a 
full-time developer, and I happily accepted.
Looking back, I'm grateful for that walk in the park. 
It gave me the inspiration and energy I needed to complete the coding 
assignment and start my career in automation with python."""

    madLibs10Det = [("noun", 1), ("adj", 2), ("color", 1), ("adverb", 1), ("verb", 2)]

    #here we finally create the list of tuples
    madLibsList = []
    madLibsList.append([madLibs1, madLibs1Det])
    madLibsList.append([madLibs2, madLibs2Det])
    madLibsList.append([madLibs3, madLibs3Det])
    madLibsList.append([madLibs4, madLibs4Det])
    madLibsList.append([madLibs5, madLibs5Det])
    madLibsList.append([madLibs6, madLibs6Det])
    madLibsList.append([madLibs7, madLibs7Det])
    madLibsList.append([madLibs8, madLibs8Det])
    madLibsList.append([madLibs9, madLibs9Det])
    madLibsList.append([madLibs10, madLibs10Det])

    return madLibsList

#CreateRandomMadLibs will fill in the given story (given a random story of the 10 with their info) with the words from allWords
def CreateRandomMadLibs(madLibs, allWords):
    randomWords = {}    #will put the word choices here (adj list, noun list, etc) depending on what is needed for the given story

    for type, amount in madLibs[1]: #puts the type and list of the correct number of them in the randomWords dict to be placed into story
        randomWords[type] = [random.choice(allWords[type]) for _ in range(amount)]  #adds amount of the type of word to randomWords to be used in story
    
    #print(allWords) #for testing the word list (inputs from user) from which randomWords will be taken
    #print(randomWords) #for testing what the words will be put in 
    #print(madLibs[0])  #testing what the story is before woords
    #print(madLibs[1])  #testing what info is on the story (how many words and types)
    print(madLibs[0].format(randomWords))

#run the program on a loop until quit
def RunMadLibs(madLibsList, allWords):

    #for x, y in enumerate(madLibsList):               #testing all 10 stories
    #    CreateRandomMadLibs(y, allWords)
    #    print("Finished MadLibs story #"+str(x+1))
    #print("done")
    #return

    randomMadLib = random.choice(madLibsList)   #this is for the option to repeat same story
    CreateRandomMadLibs(randomMadLib, allWords)

    choice = (input("""\nNow choose what to do next:\n
    Again - run the same story but the words will be randomized again
    Different - run a random story with randomized words
    Redo - redo what words will be available to be randomized in the stories
    Quit - any input that isn't of the above will default to quit\n
    """)).upper()       #please note that I had to put the input() in () before doing .upper(), otherwise it would not work

    #first will check for AGAIN, since that will cause it to rerun same story, then it will check for other cases as both call this method again
    while choice == "AGAIN":    #
        CreateRandomMadLibs(randomMadLib, allWords) #same story, will be different words
        print("choice = " + choice)
        choice = (input("""\nNow choose what to do next:\n
    Again - run the same story but the words will be randomized again
    Different - run a random story with randomized words
    Redo - redo what words will be available to be randomized in the stories
    Quit - any input that isn't of the above will default to quit\n
    """)).upper()     #note here I had to put the input() in () again before doing .upper() or else it wouldn't read right
        
        print("back to RunMadLibs() under if choice, inside while choice")
        print("choice = " + choice)         #for testing to see if we get here

    if choice == "DIFFERENT":
        RunMadLibs(madLibsList, allWords)   #different story, just calls parent function (recursion)
    elif choice == "REDO":
        allWords = GetWordLists()      #gets new words from inputs again
        RunMadLibs(madLibsList, allWords)   #reruns this method, so different story (and different new words)
    else:    
        return  #returns, doesn't really need to be here but I'll keep it
    #since any choice keeps the code from reaching here, the else isn't needed as when it reaches here it will quit automatically.

print("\nHello and welcome to my MadLibs game. There are 10 MadLib stories that will be chosen from randomly.")
print("You will be asked to input verbs, nouns, etc. The stories will be filled randomly by those.")
print("Some stories require some additional input, others do not. You will be given a chance to redo the words besides the first three you give after each story.")
print("You can either redo the words, get another random story, or redo the same story but the words will be randomized again.\n")

madLibsList = GetMadLibs()  #list of tuples containing stories and their details on which types of words and how many
#this will be a dict of lists of words the user input for us to later use randomly
allWords = GetWordLists()

RunMadLibs(madLibsList, allWords)    #starts the program loop

print("Thank you for playing my madlibs game. I hope it was enjoyable.")