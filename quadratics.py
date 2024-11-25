import math
from math import pow
from math import factorial
import functools
import sys


mainquestion = input(
    "Enter A for quadratic calculater, B for expanding double brackets, C for expanding triple brackets, D for half solved triple brackets, E for cubic calculator, F for (a+b)^x, G for\
             \n(btw the letter needs to be capitalized)\n")
if (mainquestion == "A"):
    print("quick note: ax^2+bx+c")
    a = int(input("A=\n"))
    b = int(input("B=\n"))
    c = int(input("C=\n"))
    d = (pow(b, 2)) - (4*a*c)
    cOutputQ1 = (int(math.sqrt(d)))
    aOutputQ1 = b*-1 + cOutputQ1
    bOutputQ1 = b*-1 - cOutputQ1
    answerAQ1 = int(str(aOutputQ1)) / (2*(a))
    answerBQ1 = int(str(bOutputQ1)) / (2*(a))
    print("= ", answerAQ1, "\n= ", answerBQ1)
    # this is calculating the 0's of the quadratic
    vertexXQ1 = (answerAQ1 + answerBQ1)/2
    vertexanswer = (pow(vertexXQ1, 2))*a+vertexXQ1*b+c
    print("vertex is at ", vertexXQ1, ", ", vertexanswer)
else:
    if (mainquestion == "B"):
        print("quick note: (ax+b)(cx+b)")
        a = int(input("A=\n"))
        b = int(input("B=\n"))
        c = int(input("C=\n"))
        d = int(input("D=\n"))
        outputAQ2 = a*c
        outputBQ2 = a*d+b*c
        outputCQ2 = b*d
        print("\n", outputAQ2, "x^2 +", outputBQ2, "x +", outputCQ2,)
    else:
        if (mainquestion == "C"):
            print("quick note: (aX+b)(cX+d)(eX+f)")
            a = int(input("A=\n"))
            b = int(input("B=\n"))
            c = int(input("C=\n"))
            d = int(input("D=\n"))
            e = int(input("E=\n"))
            f = int(input("F=\n"))
            outputc = a*b
            outputd = a*d+b*c
            outpute = b*d
            outputA = e*outputc
            outputB = e*outputd+f*outputc
            outputC = e*outpute+f*outputd
            outputD = f*outpute
            print(outputA, "x^3 +", outputB, "x^2 +", outputC, "x +", outputD)
        else:
            if (mainquestion == "D"):
                print("quick note: (aX+b)(cX^2+dx+e)")
                a = int(input("A=\n"))
                b = int(input("B=\n"))
                c = int(input("C=\n"))
                d = int(input("D=\n"))
                e = int(input("E=\n"))
                outputA = a*c
                outputB = a*d+b*c
                outputC = a*e+b*d
                outputD = b*e
                print(outputA, "x^3 +", outputB,
                      "x^2 +", outputC, "x +", outputD)
            else:
                if (mainquestion == "E"):
                    print("\n\nquick note: ax^3+bx^2+cx+d\n\ngood luck\n(btw i did not write all of the code for this, based off of \nhttps://github.com/shril/CubicEquationSolver) \nCredits go to Devojoyti Halder and Shril Kumar.")
                    a = int(input("A=\n"))
                    b = int(input("B=\n"))
                    c = int(input("C=\n"))
                    d = int(input("D=\n"))

                    def findF(a, b, c):
                        return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0

                    def findG(a, b, c, d):
                        return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0

                    def findH(g, f):
                        return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
                    f = findF(a, b, c)
                    g = findG(a, b, c, d)
                    h = findH(g, f)
                    if f == 0 and g == 0 and h == 0:  # 3 Real Roots are Equal
                        if (d / a) >= 0:
                            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
                        else:
                            x = (-d / (1.0 * a)) ** (1 / 3.0)
                        Output1 = x
                    elif h <= 0:    # Three Real Roots
                        i = math.sqrt(((g ** 2.0) / 4.0) - h)
                        j = i ** (1 / 3.0)
                        k = math.acos(-(g / (2 * i)))
                        L = j * -1
                        M = math.cos(k / 3.0)
                        N = math.sqrt(3) * math.sin(k / 3.0)
                        P = (b / (3.0 * a)) * -1
                        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
                        x2 = L * (M + N) + P
                        x3 = L * (M - N) + P
                        Output1 = x1
                        Output2 = x2
                        Output3 = x3
                    elif h > 0:     # One Real Root and two Complex Roots
                        R = -(g / 2.0) + math.sqrt(h)
                        if R >= 0:
                            S = R ** (1 / 3.0)
                        else:
                            S = (-R) ** (1 / 3.0) * -1
                        T = -(g / 2.0) - math.sqrt(h)
                        if T >= 0:
                            U = (T ** (1 / 3.0))
                        else:
                            U = ((-T) ** (1 / 3.0)) * -1
                        x1 = (S + U) - (b / (3.0 * a))
                        x2 = -(S + U) / 2 - (b / (3.0 * a)) + \
                            (S - U) * math.sqrt(3) * 0.5j
                        x3 = -(S + U) / 2 - (b / (3.0 * a)) - \
                            (S - U) * math.sqrt(3) * 0.5j
                        Output1 = x1
                        Output2 = x2
                        Output3 = x3
                    print("Root 1:", Output1, "\n", "Root 2:",
                          Output2, "\n", "Root 3:", Output3)

                else:
                    if (mainquestion == "F"):
                        print("quick note: (a+b)^x")
                        a = input("A=\n")
                        b = input("B=\n")
                        exponent = (input(
                            "What is the exponent of the question\n(quick note: (a+b)^x, the (x) part of that)\n"))
                        if (exponent == "one"):
                            print("bro why do u even need a python script to do that\n\nbru-\n\n\nwell...\
                                \nmight aswell give you the answer")
                            print("(", a, "+", b, ")")
                        else:
                            if (exponent == "two"):
                                print("(", a, "^2 )+( 2 *", a, "*", b, ")+(", b,
                                      "^2 )\n honestly you probaby didn't need a python script to do that for you")
                            else:
                                if (exponent == "three"):
                                    print("(", a, "^3 )+( 3 *", a, "^2 *", b,
                                          ")+( 3 *", a, "*", b, "^2 )+(", b, "^3 )")
                                else:
                                    if (exponent == "four"):
                                        print("(", a, "^4 )+( 4 *", a, "^3 *", b, ")+( 6 *", a,
                                              "^2 *", b, "^2 )+( 4 *", a, "*", b, "^3 )+(", b, "^4 )")
                                    else:
                                        if (exponent == "five"):
                                            print("(", a, "^5)+( 5 *", a, "^4 *", b, ")+( 10 *", a, "^3 *", b,
                                                  "^2 )+( 10 *", a, "^2 *", b, "^3 )+( 5 *", a, "*", b, "^4 )+(", b, "^5 )")
                                        else:
                                            if (exponent == "six"):
                                                print("(", a, "^6)+( 6 *", a, "^5 *", b, ")+( 15 *", a, "^4 *", b, "^2 )+( 20 *", a,
                                                      "^3 *", b, "^3 )+( 15 *", a, "^2 *", b, "^4 )+( 6 *", a, "*", b, "^5 )+(", b, "^6 )")
                                            else:
                                                if (exponent == "seven"):
                                                    print("(", a, "^7)+( 7 *", a, "^6 *", b, ")+( 21 *", a, "^5 *", b, "^2 )+( 35 *", a, "^4 *", b,
                                                          "^3 )+( 35 *", a, "^3 *", b, "^4 )+( 21 *", a, "^2 *", b, "^5 )+( 7 *", a, "*", b, "^6 )+(", b, "^7 )")
                                                else:
                                                    if (exponent == "eight"):
                                                        print("(", a, "^8)+( 8 *", a, "^7 *", b, ")+( 28 *", a, "^6 *", b, "^2 )+( 56 *", a, "^5 *", b,
                                                              "^3 )+( 70 *", a, "^4 *", b, "^4 )+( 56 *", a, "^3 *", b, "^5 )+( 28 *", a, "^2 *", b, "^6 )+( 8 *", a, "*", b, "^7 )+(", b, "^8 )")
                                                    else:
                                                        if (exponent == "nine"):
                                                            print("(", a, "^9)+( 9 *", a, "^8 *", b, ")+( 36 *", a, "^7 *", b, "^2 )+( 84 *", a, "^6 *", b,
                                                                  "^3 )+( 126 *", a, "^5 *", b, "^4 )+( 126 *", a, "^4 *", b, "^5 )+( 84 *", a, "^3 *", b, "^6 )+( 36 *", a, "^2 *", b, "^7 )+( 9 *", a, "*", b, "^8 )+(", b, "^9 )")
                                                        else:
                                                            if (exponent == "ten"):
                                                                print("(", a, "^10)+( 10 *", a, "^9 *", b, ")+( 45 *", a, "^8 *", b, "^2 )+( 120 *", a, "^7 *", b,
                                                                  "^3 )+( 210 *", a, "^6 *", b, "^4 )+( 256 *", a, "^5 *", b, "^5 )+( 210 *", a, "^4 *", b, "^6 )+( 120 *", a, "^3 *", b, "^7 )+( 45 *", a, "^2 *", b, "^8 )+( 10 *",a,"*", b, "^9 )+(",b,"^10 )")
                    else:
                        if (mainquestion == "G"):
                            print("Pascal's traingle\n(quick note: a= the row)")
                            a = int(input("A=\n"))
                            answer = 11**a
                            print("\nRow", a, "of pascal's triangle:", answer)
