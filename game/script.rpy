# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")

image teacher = "owl-teacher.png"
image cat = "images/cat.png"

# The game starts here.

label start:

    # Start with a score of zero.
    $ score = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show teacher at left

    # These display lines of dialogue.

    t "Hi there. I'm your teacher, McHooter."
    t "Let's see what you already know."
    menu:
        "What is the amount of space an object takes up?"
        "Mass":
            jump q1_wrong
        "Volume":
            $ score += 1
            jump q1_right
        "Footprint":
            jump q1_wrong

    # Note: Labels can't contain dashes or start with numbers.
    label q1_wrong:
        t "Oh, sorry, the correct answer was Volume."
        t "Let's do some easier questions for now."
        jump remedial_course

    label q1_right:
        t "Excellent! That's the right answer. Let's do a few harder questions."
        jump advanced_course

    label remedial_course:
        show cat at right
        menu:
            "What animal is this?"
            "Horse":
                 "Oh, so close. That's a cat."
            "Elephant":
                 "Oh, so close. That's a cat."
            "Cat":
                $ score += 1
                t "Correct! That is a cat."


        menu:
            "Which of these is a prime number?"
            "2":
                "That was actually a trick question. Both 2 and 3 are prime numbers!"
                $ score += 1
            "3":
                "That was actually a trick question. Both 2 and 3 are prime numbers!"
                $ score += 1
            "10":
                "Sorry, 10 is not a prime number. Better look next time."

        jump the_end


    label advanced_course:
        # Renpy tries to do something with the percent symbol. So I had to put a backslash in front of it.
        t "A discount store takes 50\% off of the retail price of a desk."
        t "For the store’s holiday sale, it takes an additional 20\% off of all furniture."
        t "The desk’s retail price was $320."
        menu:
            "How much is the desk on sale for during the holiday sale?"
            "$107":
                jump a2_wrong
            "$114":
                jump a2_wrong
            "$128":
                $ score += 1
                jump a2_right
            "$136":
                jump a2_wrong
            "$192":
                jump a2_wrong

        label a2_wrong:
            t "Sorry, the answer is $144. Take half off $320 to get $160,"
            t "then 20\% off of $160 to get $128."
            jump advanced_2

        label a2_right:
            t "Yes, very good!"
            jump advanced_2

        label advanced_2:
            menu:
                "Which of the following is a true statement?"
                "The product of two negative numbers is negative.":
                    jump a3_wrong
                "The product of one negative and one positive number is positive.":
                    jump a3_wrong
                "When dividing a positive number by a negative number, the results are negative.":
                    $ score += 1
                    jump a3_right
                "When dividing a negative number by a positive number, the results are positive.":
                    jump a3_wrong
                "When dividing a negative number by a negative number the results are negative.":
                    jump a3_wrong

            label a3_wrong:
                t "Sorry, the true statement is:"
                t "When dividing a positive number by a negative number, the results are negative."
                jump the_end

            label a3_right:
                t "Yes, that is correct!"
                jump the_end

    label the_end:

        t "Thanks for stopping by! Your score is [score] out of 3!"

    # This ends the game.

    return
