"""
Noah Pangilinan
nap2906
nap2906@rit.edu

CSAPX Lab 1: Secret Messages

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.
    trade - Ta[,n] switches character at index a with the character at index n
    removedupe La[,n] - Removes n duplicate characters at index a 
All indices numbers (the subscript parameters) are 0-based.

author: NOAH PANGILINAN
"""

def shift(x : str, pos : int = 0, exp : int = 1) -> str:
    """
    takes string and 2 optional integers as an input
    Uses string slicing and concatination to shift certain letters in a string exp many times
    uses mod to wrap around alphabet
    :return: string

    """
    char = x[pos]
    i = ord(char) - 65
    i = chr(( (i+ exp) % 26) + 65 )
    x = x[:pos] + i + x[pos+1:]
    return x





def rotate(x : str, exp : int = 1) -> str:
    """
    takes string and integer (optional) as an input
    Uses string slicing and concatination to rotate around string exp times
    :return: string
    """
    return(x[-exp:] + x[:-exp])




def duplicate(x : str, pos : int = 0, exp : int = 1) -> str:
    """
    takes string and 2 optional integers as an input
    Uses string slicing and concatination to duplicate certain letters in a string exp many times
    :return: string

    """
    return(x[:pos] + (x[pos])*exp + x[pos:])


def trade(x : str, fir : int = 0, sec : int = 0 ) -> str:
    """
    takes string and 2 optional integers as an input
    Uses string slicing and concatination to swap certain letters in a string
    :return: string

    """
    return(x[:fir] + x[sec] + x[fir+1:sec] + x[fir] + x[sec+1:])




def get_transformations(x : str) -> list:
    """
    takes string as input
    get_transformations reads the string of input and converts it into a list of lists of strings

    splits seperate instructions by semi-colons

    Gets seperate position and exponent numbers by seperating by comma 

    puts into list formatted like:
        [["T1,4"],["S1"], ["D3, 2"]]
    so it is easy to read

    :return: list

    """
    translist = x.split(";")
    convlist = []
    #print(x)
    #print(translist)
    for i in range(len(translist)):
        firstchar = translist[i][0]
        pos = 0
        exp = 1
        if  not translist[i].find(",") == -1:
            pos = translist[i][1:translist[i].find(",")]
            exp = translist[i][translist[i].find(",")+1:]
            convlist.append([firstchar,int(pos),int(exp)])

        else:
            pos = translist[i][1:]
            if  pos == '':
                convlist.append([firstchar, 0])
            else:
                convlist.append([firstchar, int(pos)])

    return convlist


def removedupe(x : str, pos : int = 0, exp : int = 1) -> str:
    """
    Removes duplicated letters as duplicate cannot be reversed
    skips over amount of letters duplicated


    :return: list
    
    """
    return(x[:pos] + x[pos+exp:])


def transform(msg : str, m : list) -> None:
    """
    This function preforms the operations on the string

    Takes a list of instructions and a string
    Iterates through instructions and calls each respective function
    ex) "T" calls "trade"
        "D" calls "duplicate"

    prints updated string

    :return: None
    
    """
    for i in range(len(m)):
        if m[i][0] == "S":
            if len(m[i]) == 2:
                msg = (shift(msg, m[i][1]))
            else:
                msg = (shift(msg, m[i][1],m[i][2]))




        elif m[i][0] == "D":
            if len(m[i]) == 2:
                msg = (duplicate(msg, m[i][1]))
            else:
                msg = (duplicate(msg, m[i][1],m[i][2]))




        elif m[i][0] == "L":
            if len(m[i]) == 2:
                msg = (removedupe(msg, m[i][1]))
            else:
                msg = (removedupe(msg, m[i][1],m[i][2]))



        elif m[i][0] == "T":
            msg = (trade(msg, m[i][1],m[i][2]))


        elif m[i][0] == "R":
            if not m[i][1] == 0:
                msg = (rotate(msg, m[i][1]))
            else:
                msg = (rotate(msg))
        
    print(msg)


def translate(instructions : list) -> list:
    """
    This function takes a list of instructions as an input and converts them to be used for decoding

    trade stays the same
    duplicate needs a new function that removes as many letters as were duplicated
    rotate is converted to the negative value
    shift is converted to the negative value

    reverses order of instructions

    :return: list
    """
    for i in range(len(instructions)):
        if instructions[i][0] == "S":
            if len(instructions[i]) == 2:
                instructions[i].append(-1)
            else:
                instructions[i][2] = -instructions[i][2]




        elif instructions[i][0] == "D":
            instructions[i][0] = "L"




        elif instructions[i][0] == "R":
            if not instructions[i][1] == 0:
                instructions[i][1] = -instructions[i][1]
            else:
                instructions[i][1] = (-1)


    return instructions.reverse()

def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None
    """
    while(True):
        choice = input("""Welcome to Secret Messages!\nWhat do you want to do: (E)ncrypt, (D)ecrypt or (Q)uit?""")
        if choice == "Q":
            return None
        msg = input("Enter the message:")
        instructions = input("Enter the encrypting transformation operations: Generating output ...")
        instructions = get_transformations(instructions)
        if choice == "E":
            transform(msg, instructions)
        elif(choice == "D"):
            translate(instructions)
            transform(msg, instructions)

    
    
        
    




if __name__ == '__main__':
    main()
