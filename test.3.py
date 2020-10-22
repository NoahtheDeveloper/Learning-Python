# This uses a if food= then the response responds with x


# Importing Time
import time


def fave_food():
    print("What is your favorite food?")
    food = input()
    if food == "pizza":
        response = "Mmm, Italian!"
    if food == "wings":
        response = "Mmm, lemmon pepper!"
    elif food == "veggies":
        response = "So healthy!"
    else:
        response = "Meh, not one of my favorites."
    print('I like, ' + food)
    
    # Another 5 Seccond wait
    time.sleep(3)

    return(response)





opinion = fave_food()


# Prints response to anwser
print(opinion)

# Another 5 Seccond wait
time.sleep(5)


# End of command script
print("The function has run. sNothing has been printed. It is now finished.")

#done
