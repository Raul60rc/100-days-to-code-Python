print("welcome to the treasure island")

input('you are at in the jungle where do you want to go? type' "left" or "right").lower()
choice_right = "right"
choice_left = "left"

situation1 = input('walking on in the dark near the trees & a lion arrives turn' "left" or "right").lower()
if situation1 == choice_left:
    print("you have succesfully evaded the lion!")
    situation2 = input('The female lion has located you now & she is coming slowly but you have to move'"left" or "right").lower()
    if situation2 == choice_left:
        print("Your still running but not fast enough now the whole lion army is coming after you")
        situation3 = input('Keep running unless you want to be eaten & turn'"right" or "left").lower()
        if situation3 == choice_left:
            print("")
else:
    print("the lion ate you GAME OVER")

    situation2 = input()

