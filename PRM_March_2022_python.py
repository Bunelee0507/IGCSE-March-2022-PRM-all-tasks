# Golf program by Anurag in Python

# Some flags
correct1 = int(0)
correct2 = int(0)
correct3 = int(0)

# Some variables

hole_num = int(0)
con = int(0)
con1 = int(1)
k=0

# While loop to get the player numbers and check.
while correct1 == 0:

    num_players = int(input("Enter the number of players playing: 2, 3 or 4."))
    correct1 = int(input("Confirm: There are " + str(num_players) + " people playing? 1 for yes, 0 for no."))

# List of the names initalised with all being N/A at first

List = ["N/A", "N/A", "N/A", "N/A"]
List_score = [0, 0, 0, 0]
List_holes_in_one = [0, 0, 0, 0]

# For loop, to get the names for the List.

for i in range (0, num_players):
    List[i] = input("player number " + str(i+1) + "'s" + " name")

# Holes checking.

while correct2 == 0 or (holes != 9 and holes != 18):
    holes = int(input("How many holes to be played? 9 or 18?"))
    if(holes != 9 and holes != 18):
        print(input("Error. Holes must be 9 or 18 only. Press enter to continue."))
    if(holes == 9 or holes == 18):
        correct2 = int(input("Confirm: there are " + str(holes) + " holes to be played? 1 for yes, 0 for no"))

while correct3 == 0:
    par = int(input("What is the par for this course?"))
    correct3 = int(input("Confirm: The par for this course is " + str(par) + " strokes? 1 for yes, 0 for no"))

# A while loop (that acts like a for loop) nested inside a for loop to loop the player strokes inputs for each player
# and for each hole.

for j in range(0, holes):
    k=0;
    hole_num += 1
    print("Score in order: " + str(List_score))
    con=con1+1000
    while con != con1:
        con = int(input("How many strokes did player " + str(k+1) + " take for hole number " + str(j+1) + "?"))
        con1 = int(input("Enter again: How many strokes did " + str(k+1) + " take for hole number " + str(j+1)+ "? Chance for error correction here."))
        if (con != con1):
            print("Please enter again. The first and second input do not match. Press enter to continue.")
            con=con1+1023484
        if (con == con1):
            List_score[k] += con
        if(con == 1 and con == con1):
            List_holes_in_one[k] += 1
        if(k < num_players-1 and con == con1):
            k += 1
            con = con1 + 90

# Not the most efficient but gets the job done decently ^

# This part is to determine the winner. Probably would be cleaner with case of... But this works.
# Makes a new list and utilises min(List) to get the job done efficiently.

print("Score in order: " + str(List_score))

if (num_players == 2):
    list_score_final = [List_score[0], List_score[1]]
    print(str(min(list_score_final)) + " was the winning score, achieved by player " + str(list_score_final.index(min(list_score_final))+1))
    name=list_score_final.index(min(list_score_final))
    if(List_score[0] == List_score[1]):
        print("Player 2 also achieved a winning score. It is a tie.")
        print(List[0])
        print(List[1])
    else:
        print(List[list_score_final.index(min(list_score_final))])

if (num_players == 3):
    list_score_final = [List_score[0], List_score[1], List_score[2]]
    print(str(min(list_score_final)) + " was the winning score, achieved by player " + str(list_score_final.index(min(list_score_final))+1))


    if (List_score[0] == List_score[1] == List_score[2]):
        print("Player 2 and 3 also achieved a winning score. It is a tie.")
        print(List[0])
        print(List[1])
        print(List[2])
    else:
        if(list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[1]):
            print("Player 2 also achieved a winning score. It is a tie.")
            print(List[0])
            print(List[1])
        else:
            if (list_score_final.index(min(list_score_final)) == 1 and List_score[1] == List_score[2]):
                print("Player 3 also achieved a winning score. It is a tie.")
                print(List[1])
                print(List[2])
            else:
                if (list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[2]):
                    print("Player 3 also achieved a winning score. It is a tie.")
                    print(List[0])
                    print(List[2])
                else:
                    print(List[list_score_final.index(min(list_score_final))])


if (num_players == 4):
    list_score_final = [List_score[0], List_score[1], List_score[2], List_score[3]]
    print(str(min(list_score_final)) + " was the winning score, achieved by player " + str(list_score_final.index(min(list_score_final))))


    if (List_score[0] == List_score[1] == List_score[2] == List_score[3]):
        print("Player 2, 3 and 4 also achieved a winning score. It is a tie.")
        print(List[0])
        print(List[1])
        print(List[2])
        print(List[3])
    else:
        #////////////////////////////////////////////////////////////////////////// groups of 2 tie

        if(list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[1]):
            print("Player 2 also achieved a winning score. It is a tie.")
            print(List[0])
            print(List[1])
        else:
            if (list_score_final.index(min(list_score_final)) == 1 and List_score[1] == List_score[2]):
                print("Player 3 also achieved a winning score. It is a tie.")
                print(List[1])
                print(List[2])
            else:
                if (list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[2]):
                    print("Player 3 also achieved a winning score. It is a tie.")

                    print(List[0])
                    print(List[2])

                else:

    #/////////////////////////////////////////////////////////////////////////////////// groups of 3 tie

                    if (list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[1] and List_score[0] == List_score[2]):
                        print("Player 2 and 3 also achieved a winning score. It is a tie.")
                        print(List[0])
                        print(List[1])
                        print(List[2])
                    else:
                        if (list_score_final.index(min(list_score_final)) == 1 and List_score[1] == List_score[2] and List_score[1] == List_score[3] ):
                            print("Player 3 and 4 also achieved a winning score. It is a tie.")

                            print(List[1])
                            print(List[2])
                            print(List[3])

                        else:
                            if (list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[2] and List_score[0] == List_score[3]):
                                print("Player 3 and 4 also achieved a winning score. It is a tie.")

                                print(List[0])
                                print(List[2])
                                print(List[3])

                            else:
                                if (list_score_final.index(min(list_score_final)) == 0 and List_score[0] == List_score[1] and List_score[0] == List_score[3]):
                                    print("Player 2 and 4 also achieved a winning score. It is a tie.")

                                    print(List[0])
                                    print(List[1])
                                    print(List[3])

                                else:
                                    print(List[list_score_final.index(min(list_score_final))])
# Printing whatever they asked us to.

print("round average was: " + str(sum(List_score)/num_players))

print("per hole average was: " + str((sum(List_score)/num_players)/holes))

print("Hole in one score for players 1, 2, 3, 4 (ignore certain numbers in this list if inapplicable): " + str(List_holes_in_one))