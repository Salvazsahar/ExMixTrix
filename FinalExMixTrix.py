def printboard(num):
    for i in range(9):
        a = num & 3
        if a == 3:
            print "o",
        elif a == 2:
            print "x",
        else:
            print ".",
        num >>= 2
        if i == 2 or i == 5 or i == 8:
            print


def checkwin(num, listwin1):
    for mask in listwin1:
        if num & mask*3 == mask*3:
            return -1
        if num & mask*3 == mask*2:
            return 1
    return 0


def exmixtrix1(board1, color, listwin1, placesavailable):
    bestplace = 0
    best = -1 if color == 2 else 1
    placesavailable2 = placesavailable
    while(placesavailable2 != 0):
        place = 1
        while (place & placesavailable2 == 0):
            place <<= 2
        placesavailable2 ^= place
        s = checkwin(board1 + place*color, listwin1)
        if s == 0 and (placesavailable^place) != 0:
            s, p = exmixtrix1(board1 + place*color, color ^ 1, listwin1, placesavailable^place)
        if (color == 3 and s < best) or (color == 2 and s > best):
            best = s
            bestplace = place
    return best, bestplace


def exmixtrixreal(board1, turn, listwin1, placesavailable):
    flag = 0
    while (placesavailable != 0 and flag == 0):
        printboard(board1)
        if turn & 1 == 1:
            print turn, " - ", turn & 1
            place = int(raw_input("Enter the place in which you wish to place the X: "))
            place = 1 << 2 * place
            while placesavailable & place != place:
                place = int(raw_input("try again: "))
                place = 1 << 2 * place
            board1 += place * 2
            placesavailable = placesavailable ^ place
            win = checkwin(board1, listwin1)
            if win == 1:
                print "you have defeated the computer"
                flag = 1
        else:
            print "a"
            s,p = exmixtrix1(board1,3,listwin1,placesavailable)
            print "i choose to place here:", p
            board1 += p*3
            placesavailable ^= p
            if checkwin(board1,listwin1) == -1:
                print "the computer has beaten you"
                flag = 1
        turn += 1
    if flag == 0:
        print "it was a draw"


p = 87381
listplace = [0, 2, 3]
listwin = [21, 1344, 86016, 4161, 16644, 66576, 4368, 65793]
exmixtrixreal(0, 1, listwin, p)
