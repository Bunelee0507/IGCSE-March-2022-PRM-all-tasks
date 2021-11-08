# Golf program by Anurag in Python

# Some flags

correct1 = int(0)
correct2 = int(0)
correct3 = int(0)

# Some variables
choice = 0
hole_num = int(0)
con = int(0)
con1 = int(1)
k=0
num_players=int(0)

# While loop to get the player numbers and check.

while correct1 == 0 or (num_players !=2 and num_players!=3 and num_players!=4):

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

if(holes==9):

    List_Score_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Avg = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    Hole_list1= [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

if(holes==18):

    List_Score_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    List_Score_p4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    Hole_list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Hole_list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for j in range(0, holes):
    k=0
    hole_num += 1
    con=con1+1000
    while con != con1:
        c_score = 0
        c_score = int(
            input("Do you want to see your score, " + str(List[k]) + "? 1 for yes, any other integer for no."))
        if (c_score == 1):
            print(List_score[k])
        con = int(input("How many strokes did " + str(List[k]) + " take for hole number " + str(j+1) + "?"))
        con1 = int(input("Enter again: How many strokes did " + str(List[k]) + " take for hole number " + str(j+1)+ "? Chance for error correction here."))
        if (con != con1):
            print("Please enter again. The first and second input do not match. Press enter to continue.")
            con=con1+1023484
        if (con == con1):
            List_score[k] += con

            if(k == 0):
                List_Score_p1[j] = con
            if (k == 1):
                List_Score_p2[j] = con
            if (k == 2):
                List_Score_p3[j] = con
            if (k == 3):
                List_Score_p4[j] = con

        if(con == 1 and con == con1):
            List_holes_in_one[k] += 1
            if(k == 0):
                Hole_list1[j] = 1
            if (k == 1):
                Hole_list2[j] = 1
            if (k == 2):
                Hole_list3[j] = 1
            if (k == 3):
                Hole_list4[j] = 1
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
    print(str(min(list_score_final)) + " was the winning score, achieved by player " + str(list_score_final.index(min(list_score_final))+1))


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

#Choice variable (integer)

#Options

while(choice!=-1):
    choice = int(input(
        "What do you want to see? -1 to abort the program. 1 for round average, 2 for per hole average, 3 for Hole in one score for the players (ignore certain numbers in this list if inapplicable), and 4 for the Winning score in relation to par. Press 5 to see every player's score in each hole. Press 6 in order to see all the hole in ones of the player's hole in ones. Press 7 to find the average strokes taken for each hole."))
    if choice==1:

        print("round average was: " + str(sum(List_score)/num_players))
        choice=-2

    if choice==2:

        print("per hole average was: " + str((sum(List_score)/num_players)/holes))
        choice = -2

    if choice==3:

        print("Hole in one score for players 1, 2, 3, 4 (ignore certain numbers in this list if inapplicable): " + str(List_holes_in_one))
        choice = -2
    if choice == 4:
        print("Winning score in relation to par: ")

        par_diff = min(list_score_final) - par

        if(par_diff>0):
            print(str(par_diff) + " above par.")
        else:
            if(par_diff<0):
                print(str(-1*par_diff) + " below par.")
            else:
                print("exactly the same as the par.")
        choice = -2

    if choice == 5:
        if (num_players == 2):
            print(*List_Score_p1, sep = ',')
            print(*List_Score_p2, sep = ',')
        if (num_players == 3):
            print(*List_Score_p1, sep = ',')
            print(*List_Score_p2, sep = ',')
            print(*List_Score_p3, sep = ',')
        if (num_players == 4):
            print(*List_Score_p1, sep = ',')
            print(*List_Score_p2, sep = ',')
            print(*List_Score_p3, sep = ',')
            print(*List_Score_p4, sep = ',')

        choice = -2

    if(choice == 6):

        if(num_players == 2):
            print(str(List[0]) + str(Hole_list1))
            print(str(List[1]) + str(Hole_list2))
        if (num_players == 3):
            print(str(List[0]) + str(Hole_list1))
            print(str(List[1]) + str(Hole_list2))
            print(str(List[2]) + str(Hole_list3))
        if (num_players == 4):
            print(str(List[0]) + str(Hole_list1))
            print(str(List[1]) + str(Hole_list2))
            print(str(List[2]) + str(Hole_list3))
            print(str(List[3]) + str(Hole_list4))

        choice = -2
    if(choice==7):

        # Calculating average for every hole.

        for m in range(0, holes):
            Avg[m] = (List_Score_p1[m] + List_Score_p2[m] + List_Score_p3[m] + List_Score_p4[m]) / num_players
        print(*Avg, sep = ",")

        choice=-2

    if(choice==-1):
        # Quit after done
        exit()