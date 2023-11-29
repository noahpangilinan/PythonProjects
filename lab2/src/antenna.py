from cmath import sqrt
import turtle
import math
"""
This program generates an antenna fractal in 2 ways
One recursively draws line segments while the other recursivly draws squares
Using turtle to draw, this program asks for a side length and a depth/level and
fits the fractal to the side length and level

Author: Noah Pangilinan
nap2906@rit.edu

"""
def draw_side(n : float, level : int)-> float:
    '''
    This function draws 1 quarter of a fractal by recursivly calling itself to draw more line segments at a decreasing length and turn pattern
    This function takes a float for the full length and a level for the depth of the recursion
    It returns the total length of the drawing


    :param n: the length of one side of the entire fractal
    :param level: the depth of the recursion
    :return: the distance the turtle/tracer drew
    '''
    turtle.speed(0)
    if level == 1:
        turtle.forward(n)
        return(n)
    else:
        length = 0
        length += draw_side(n/3,level-1)
        turtle.left(90)
        length += draw_side(n/3,level-1)
        turtle.right(90)
        length += draw_side(n/3,level-1)
        turtle.right(90)
        length += draw_side(n/3,level-1)
        turtle.left(90)
        length += draw_side(n/3,level-1)
        return length


def strategy1(n : float, level : int)-> float:
    '''
    This function takes the parameters of the draw_side function and passes it to the draw_side function 4 times after turning the turtle
    this way it completes the entire fractal drawing and total length


    :param n: the length of one side of the entire fractal
    :param level: the depth of the recursion
    :return: the distance the turtle/tracer drew
    '''
    length = 0
    turtle.up()
    turtle.forward(200)
    turtle.down()
    turtle.left(135)
    for i in range(4):
        length += draw_side(n, level)
        turtle.left(90)
    return(length)



def strategy2(n : float, level : int)-> float:
    '''
    This function draws a fractal by recursivly calling itself to draw more squares in a rotating pattern
    This function takes a float for the full length and a level for the depth of the recursion
    It returns the total length of the drawing


    :param n: the length of one side of the entire fractal
    :param level: the depth of the recursion
    :return: the distance the turtle/tracer drew
    '''
    turtle.speed(0)
    if level == 1:
        turtle.up()
        turtle.forward(((n*math.sqrt(2))/2))
        turtle.down()
        turtle.left(135)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.right(45)
        turtle.up()
        turtle.backward(((n*math.sqrt(2))/2))
        turtle.down()
        return(n*4)
    else:
        length = 0
        

        for b in  range(4):
            turtle.up()
            
            x = (pow(3, (level - 2))) * (n*math.sqrt(2))
            turtle.forward(x)
            turtle.down()
            length += strategy2(n,level-1)
            turtle.up()
            turtle.backward(x)
            turtle.down()
            turtle.left(90)
        length += strategy2(n,level-1)
        return length



def main()-> None:
    '''
    This function is the main loop for the program. It askes for a side length and depth for the first strategy, and once the first image is drawn, 
    "Enter" must me hit on the keyboard to reset the window and re-request data for the second strategy

    :return: None 
    '''
    n = float(input("Length of initial side: "))
    level = int(input("Number of levels: "))
    print("Total length is " + str(strategy1(n,level)))
    i = input()
    turtle.reset()

    n = float(input("Length of initial side: "))
    level = int(input("Number of levels: "))
    n = (pow((1/3), (level - 1))) * (n)
    print("Total length is " + str(strategy2(n,level)))
    turtle.done()



if __name__ == "__main__":
    main()