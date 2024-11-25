import math
from math import pow
from math import factorial
import functools
import sys
import tkinter as tk
from tkinter.constants import END
import tkinter.font as TkFont
import time

HEIGHT = 750
WIDTH = 1000


def MainPage():
    frameOne = tk.Frame(root, bg="#ff5454", bd=5)
    frameOne.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")

    label = tk.Label(frameOne, bg="gray",
                     text="Welcome to my calculator!", font=("Arial", 18))
    label.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    label = tk.Label(frameOne, bg="#ff5454",
                     text="What would you like to solve?", font=("Arial", 32))
    label.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    QuadraticButton = tk.Button(frameOne, text="Quadratics", bg="gray",
                                fg="white", font=("Arial", 18), command=Quadratic)
    QuadraticButton.place(relx=0, rely=0.4, relwidth=0.3, relheight=0.15)

    DoubleBracketExpansionButton = tk.Button(frameOne, text="Double Bracket Expansion", bg="gray",
                                             fg="white", font=("Arial", 18), command=DoubleBracketExpansion)
    DoubleBracketExpansionButton.place(
        relx=0.35, rely=0.4, relwidth=0.3, relheight=0.15)

    TripleBracketExpansionButton = tk.Button(frameOne, text="Triple Bracket Expansion", bg="gray",
                                             fg="white", font=("Arial", 18), command=TripleBracketExpansion)
    TripleBracketExpansionButton.place(
        relx=0.7, rely=0.4, relwidth=0.3, relheight=0.15)

    CubicExpansionButton = tk.Button(frameOne, text="Cubic Expansion", bg="gray",
                                     fg="white", font=("Arial", 18), command=CubicExpansion)
    CubicExpansionButton.place(
        relx=0.0, rely=0.6, relwidth=0.3, relheight=0.15)

    CubicButton = tk.Button(frameOne, text="Cubic Expansion (Proceed with caution", bg="gray",
                            fg="white", font=("Arial", 18), command=Cubic)
    CubicButton.place(
        relx=0.0, rely=0.8, relwidth=1, relheight=0.15)


def Quadratic():

    def QuadraticSolver():

        AInput = int(str(A.get()))
        BInput = int(str(B.get()))
        CInput = int(str(C.get()))

        D = pow(BInput, 2) - (4*AInput*CInput)
        if (D < 0):
            Answer = tk.Label(QuadraticFrame, fg="#525252", bg="#ff5454",
                              text="No real roots", font=("Arial", 28))
            Answer.place(relx=0.7, rely=0.3, relwidth=0.4,
                         relheight=0.4, anchor="n")
            Answer.after(4000, Answer.destroy)
        else:

            cOutputQ1 = (int(math.sqrt(D)))
            aOutputQ1 = (int(BInput))*-1 + cOutputQ1
            bOutputQ1 = (int(BInput))*-1 - cOutputQ1
            answerAQ1 = int(str(aOutputQ1)) / (2*AInput)
            answerBQ1 = int(str(bOutputQ1)) / (2*AInput)
            print("= ", answerAQ1, "\n= ", answerBQ1)
            # this is calculating the 0's of the quadratic
            vertexXQ1 = (answerAQ1 + answerBQ1)/2
            vertexanswer = (pow(vertexXQ1, 2))*AInput + \
                vertexXQ1*BInput+CInput
            print("vertex is at ", vertexXQ1, ", ", vertexanswer)
            Answer1 = tk.Label(QuadraticFrame, fg="#525252", bg="#ff5454",
                               text=("= ", answerAQ1), font=("Arial", 24))
            Answer1.place(relx=0.7, rely=0.4, relwidth=0.4,
                          relheight=0.1, anchor="n")
            Answer1.after(4000, Answer1.destroy)

            Answer2 = tk.Label(QuadraticFrame, fg="#525252", bg="#ff5454",
                               text=("= ", answerBQ1), font=("Arial", 24))
            Answer2.place(relx=0.7, rely=0.5, relwidth=0.4,
                          relheight=0.1, anchor="n")
            Answer2.after(4000, Answer2.destroy)

            Vertex = tk.Label(QuadraticFrame, fg="#525252", bg="#ff5454",
                              text=("vertex is at: ", vertexXQ1, ",", vertexanswer), font=("Arial", 24))
            Vertex.place(relx=0.7, rely=0.6, relwidth=0.6,
                         relheight=0.1, anchor="n")
            Vertex.after(4000, Vertex.destroy)

    QuadraticFrame = tk.Frame(root, bg="#ff5454", bd=5)
    QuadraticFrame.place(relx=0.5, rely=0.1, relwidth=0.8,
                         relheight=0.8, anchor="n")

    Title = tk.Label(QuadraticFrame, bg="gray",
                     text="Quadratic calculator", font=("Arial", 18))
    Title.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    Note = tk.Label(QuadraticFrame, bg="#ff5454",
                    text="ax^2 + bx + c", font=("Arial", 32))
    Note.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    ACoefficient = tk.Label(QuadraticFrame, bg="#ff5454",
                            text="A=", font=("Arial", 20))
    ACoefficient.place(relx=0.05, rely=0.4, relwidth=0.05,
                       relheight=0.05, anchor="w")

    BCoefficient = tk.Label(QuadraticFrame, bg="#ff5454",
                            text="B=", font=("Arial", 20))
    BCoefficient.place(relx=0.05, rely=0.5, relwidth=0.05,
                       relheight=0.05, anchor="w")

    CCoefficient = tk.Label(QuadraticFrame, bg="#ff5454",
                            text="C=", font=("Arial", 20))
    CCoefficient.place(relx=0.05, rely=0.6, relwidth=0.05,
                       relheight=0.05, anchor="w")

    a = str
    b = str
    c = str

    A = tk.Entry(QuadraticFrame, font=("Arial", 20), textvariable=a)
    A.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.08, anchor="w")

    B = tk.Entry(QuadraticFrame, font=("Arial", 20), textvariable=b)
    B.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.08, anchor="w")

    C = tk.Entry(QuadraticFrame, font=("Arial", 20), textvariable=c)
    C.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.08, anchor="w")

    button = tk.Button(QuadraticFrame, text="Calculate", bg="gray",
                       fg="white", font=40, command=lambda: QuadraticSolver())
    button.place(relx=0.05, rely=0.8, relwidth=0.3, relheight=0.1, anchor="w")


def DoubleBracketExpansion():

    def DoubleBracketExpansionSolver():

        AInput = int(str(A.get()))
        BInput = int(str(B.get()))
        CInput = int(str(C.get()))
        DInput = int(str(D.get()))

        print("quick note: (ax+b)(cx+b)")
        outputAQ2 = AInput*CInput
        outputBQ2 = AInput*DInput+BInput*CInput
        outputCQ2 = BInput*DInput
        Answer = tk.Label(DoubleBracketFrame, fg="#525252", bg="#ff5454",
                          text=(outputAQ2, "x^2 +", outputBQ2, "x +", outputCQ2), font=("Arial", 28))
        Answer.place(relx=0.6, rely=0.3, relwidth=0.6,
                     relheight=0.4, anchor="n")
        Answer.after(4000, Answer.destroy)
        print("\n", outputAQ2, "x^2 +", outputBQ2, "x +", outputCQ2,)

    DoubleBracketFrame = tk.Frame(root, bg="#ff5454", bd=5)
    DoubleBracketFrame.place(relx=0.5, rely=0.1, relwidth=0.8,
                             relheight=0.8, anchor="n")

    Title = tk.Label(DoubleBracketFrame, bg="gray",
                     text="Double Bracket Expansion", font=("Arial", 18))
    Title.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    Note = tk.Label(DoubleBracketFrame, bg="#ff5454",
                    text="(ax+b)(cx+d)", font=("Arial", 32))
    Note.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    ACoefficient = tk.Label(DoubleBracketFrame, bg="#ff5454",
                            text="A=", font=("Arial", 20))
    ACoefficient.place(relx=0.05, rely=0.4, relwidth=0.05,
                       relheight=0.05, anchor="w")

    BCoefficient = tk.Label(DoubleBracketFrame, bg="#ff5454",
                            text="B=", font=("Arial", 20))
    BCoefficient.place(relx=0.05, rely=0.5, relwidth=0.05,
                       relheight=0.05, anchor="w")

    CCoefficient = tk.Label(DoubleBracketFrame, bg="#ff5454",
                            text="C=", font=("Arial", 20))
    CCoefficient.place(relx=0.05, rely=0.6, relwidth=0.05,
                       relheight=0.05, anchor="w")

    DCoefficient = tk.Label(DoubleBracketFrame, bg="#ff5454",
                            text="D=", font=("Arial", 20))
    DCoefficient.place(relx=0.05, rely=0.7, relwidth=0.05,
                       relheight=0.05, anchor="w")

    a = str
    b = str
    c = str
    d = str

    A = tk.Entry(DoubleBracketFrame, font=("Arial", 20), textvariable=a)
    A.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.08, anchor="w")

    B = tk.Entry(DoubleBracketFrame, font=("Arial", 20), textvariable=b)
    B.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.08, anchor="w")

    C = tk.Entry(DoubleBracketFrame, font=("Arial", 20), textvariable=c)
    C.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.08, anchor="w")

    D = tk.Entry(DoubleBracketFrame, font=("Arial", 20), textvariable=d)
    D.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.08, anchor="w")

    button = tk.Button(DoubleBracketFrame, text="Calculate", bg="gray",
                       fg="white", font=40, command=lambda: DoubleBracketExpansionSolver())
    button.place(relx=0.05, rely=0.85, relwidth=0.3, relheight=0.1, anchor="w")


def TripleBracketExpansion():

    def TripleBracketSolver():
        print("quick note: (aX+b)(cX+d)(eX+f)")
        AInput = int(str(A.get()))
        BInput = int(str(B.get()))
        CInput = int(str(C.get()))
        DInput = int(str(D.get()))
        EInput = int(str(E.get()))
        FInput = int(str(F.get()))
        outputc = AInput*BInput
        outputd = AInput*DInput+BInput*CInput
        outpute = BInput*DInput
        outputA = EInput*outputc
        outputB = EInput*outputd+FInput*outputc
        outputC = EInput*outpute+FInput*outputd
        outputD = FInput*outpute
        Answer = tk.Label(TripleBracketFrame, fg="#525252", bg="#ff5454",
                          text=(outputA, "x^3 +", outputB, "x^2 +", outputC, "x +", outputD), font=("Arial", 28))
        Answer.place(relx=0.6, rely=0.3, relwidth=0.6,
                     relheight=0.4, anchor="n")
        Answer.after(5000, Answer.destroy)

    TripleBracketFrame = tk.Frame(root, bg="#ff5454", bd=5)
    TripleBracketFrame.place(relx=0.5, rely=0.1, relwidth=0.8,
                             relheight=0.8, anchor="n")

    Title = tk.Label(TripleBracketFrame, bg="gray",
                     text="Triple Bracket Expansion", font=("Arial", 18))
    Title.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    Note = tk.Label(TripleBracketFrame, bg="#ff5454",
                    text="(ax+b)(cx+d)(ex+f)", font=("Arial", 32))
    Note.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    ACoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="A=", font=("Arial", 20))
    ACoefficient.place(relx=0.05, rely=0.3, relwidth=0.05,
                       relheight=0.05, anchor="w")

    BCoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="B=", font=("Arial", 20))
    BCoefficient.place(relx=0.05, rely=0.4, relwidth=0.05,
                       relheight=0.05, anchor="w")

    CCoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="C=", font=("Arial", 20))
    CCoefficient.place(relx=0.05, rely=0.5, relwidth=0.05,
                       relheight=0.05, anchor="w")

    DCoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="D=", font=("Arial", 20))
    DCoefficient.place(relx=0.05, rely=0.6, relwidth=0.05,
                       relheight=0.05, anchor="w")

    ECoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="E=", font=("Arial", 20))
    ECoefficient.place(relx=0.05, rely=0.7, relwidth=0.05,
                       relheight=0.05, anchor="w")

    FCoefficient = tk.Label(TripleBracketFrame, bg="#ff5454",
                            text="F=", font=("Arial", 20))
    FCoefficient.place(relx=0.05, rely=0.8, relwidth=0.05,
                       relheight=0.05, anchor="w")

    a = str
    b = str
    c = str
    d = str
    e = str
    f = str

    A = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=a)
    A.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.08, anchor="w")

    B = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=b)
    B.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.08, anchor="w")

    C = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=c)
    C.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.08, anchor="w")

    D = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=d)
    D.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.08, anchor="w")

    E = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=e)
    E.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.08, anchor="w")

    F = tk.Entry(TripleBracketFrame, font=("Arial", 20), textvariable=f)
    F.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.08, anchor="w")

    button = tk.Button(TripleBracketFrame, text="Calculate", bg="gray",
                       fg="white", font=40, command=lambda: TripleBracketSolver())
    button.place(relx=0.05, rely=0.9, relwidth=0.3, relheight=0.1, anchor="w")


def CubicExpansion():

    def CubicExpansionSolver():
        print("quick note: (aX+b)(cX^2+dx+e)")
        AInput = int(str(A.get()))
        BInput = int(str(B.get()))
        CInput = int(str(C.get()))
        DInput = int(str(D.get()))
        EInput = int(str(E.get()))
        outputA = AInput*CInput
        outputB = AInput*DInput+BInput*CInput
        outputC = AInput*EInput+BInput*DInput
        outputD = BInput*EInput
        Answer = tk.Label(CubicExpansionFrame, fg="#525252", bg="#ff5454",
                          text=(outputA, "x^3 +", outputB, "x^2 +", outputC, "x +", outputD), font=("Arial", 28))
        Answer.place(relx=0.65, rely=0.3, relwidth=0.6,
                     relheight=0.4, anchor="n")
        Answer.after(5000, Answer.destroy)

        print(outputA, "x^3 +", outputB, "x^2 +", outputC, "x +", outputD)

    CubicExpansionFrame = tk.Frame(root, bg="#ff5454", bd=5)
    CubicExpansionFrame.place(relx=0.5, rely=0.1, relwidth=0.8,
                              relheight=0.8, anchor="n")

    Title = tk.Label(CubicExpansionFrame, bg="gray",
                     text="Triple Bracket Expansion", font=("Arial", 18))
    Title.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    Note = tk.Label(CubicExpansionFrame, bg="#ff5454",
                    text="(aX+b)(cX^2+dx+e)", font=("Arial", 32))
    Note.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    ACoefficient = tk.Label(CubicExpansionFrame, bg="#ff5454",
                            text="A=", font=("Arial", 20))
    ACoefficient.place(relx=0.05, rely=0.35, relwidth=0.05,
                       relheight=0.05, anchor="w")

    BCoefficient = tk.Label(CubicExpansionFrame, bg="#ff5454",
                            text="B=", font=("Arial", 20))
    BCoefficient.place(relx=0.05, rely=0.45, relwidth=0.05,
                       relheight=0.05, anchor="w")

    CCoefficient = tk.Label(CubicExpansionFrame, bg="#ff5454",
                            text="C=", font=("Arial", 20))
    CCoefficient.place(relx=0.05, rely=0.55, relwidth=0.05,
                       relheight=0.05, anchor="w")

    DCoefficient = tk.Label(CubicExpansionFrame, bg="#ff5454",
                            text="D=", font=("Arial", 20))
    DCoefficient.place(relx=0.05, rely=0.65, relwidth=0.05,
                       relheight=0.05, anchor="w")

    ECoefficient = tk.Label(CubicExpansionFrame, bg="#ff5454",
                            text="E=", font=("Arial", 20))
    ECoefficient.place(relx=0.05, rely=0.75, relwidth=0.05,
                       relheight=0.05, anchor="w")

    a = str
    b = str
    c = str
    d = str
    e = str

    A = tk.Entry(CubicExpansionFrame, font=("Arial", 20), textvariable=a)
    A.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.08, anchor="w")

    B = tk.Entry(CubicExpansionFrame, font=("Arial", 20), textvariable=b)
    B.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.08, anchor="w")

    C = tk.Entry(CubicExpansionFrame, font=("Arial", 20), textvariable=c)
    C.place(relx=0.1, rely=0.55, relwidth=0.2, relheight=0.08, anchor="w")

    D = tk.Entry(CubicExpansionFrame, font=("Arial", 20), textvariable=d)
    D.place(relx=0.1, rely=0.65, relwidth=0.2, relheight=0.08, anchor="w")

    E = tk.Entry(CubicExpansionFrame, font=("Arial", 20), textvariable=e)
    E.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.08, anchor="w")

    button = tk.Button(CubicExpansionFrame, text="Calculate", bg="gray",
                       fg="white", font=40, command=lambda: CubicExpansionSolver())
    button.place(relx=0.05, rely=0.9, relwidth=0.3, relheight=0.1, anchor="w")


def Cubic():

    def CubicSolver():
        print("\n\nquick note: ax^3+bx^2+cx+d\n\ngood luck\n(btw i did not write all of the code for this, based off of \nhttps://github.com/shril/CubicEquationSolver) \nCredits go to Devojoyti Halder and Shril Kumar.")
        a = int(str(A.get()))
        b = int(str(B.get()))
        c = int(str(C.get()))
        d = int(str(D.get()))

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

    CubicFrame = tk.Frame(root, bg="#ff5454", bd=5)
    CubicFrame.place(relx=0.5, rely=0.1, relwidth=0.8,
                     relheight=0.8, anchor="n")

    Title = tk.Label(CubicFrame, bg="gray",
                     text="Cubic Solver", font=("Arial", 18))
    Title.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor="n")

    Credits = tk.Label(CubicFrame, bg="#ff5454",
                       text="btw I did not write all of the code for this, based off of \nhttps://github.com/shril/CubicEquationSolver \nCredits go to Devojoyti Halder and Shril Kumar.", font=("Arial", 18))
    Credits.place(relx=0.5, rely=0.16, relwidth=1, relheight=0.25, anchor="n")

    Note = tk.Label(CubicFrame, bg="#ff5454",
                    text="ax^3+bx^2+cx+d", font=("Arial", 32))
    Note.place(relx=0.5, rely=0.125, relwidth=1, relheight=0.1, anchor="n")

    ACoefficient = tk.Label(CubicFrame, bg="#ff5454",
                            text="A=", font=("Arial", 20))
    ACoefficient.place(relx=0.05, rely=0.4, relwidth=0.05,
                       relheight=0.05, anchor="w")

    BCoefficient = tk.Label(CubicFrame, bg="#ff5454",
                            text="B=", font=("Arial", 20))
    BCoefficient.place(relx=0.05, rely=0.5, relwidth=0.05,
                       relheight=0.05, anchor="w")

    CCoefficient = tk.Label(CubicFrame, bg="#ff5454",
                            text="C=", font=("Arial", 20))
    CCoefficient.place(relx=0.05, rely=0.6, relwidth=0.05,
                       relheight=0.05, anchor="w")

    DCoefficient = tk.Label(CubicFrame, bg="#ff5454",
                            text="D=", font=("Arial", 20))
    DCoefficient.place(relx=0.05, rely=0.7, relwidth=0.05,
                       relheight=0.05, anchor="w")

    a = str
    b = str
    c = str
    d = str

    A = tk.Entry(CubicFrame, font=("Arial", 20), textvariable=a)
    A.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.08, anchor="w")

    B = tk.Entry(CubicFrame, font=("Arial", 20), textvariable=b)
    B.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.08, anchor="w")

    C = tk.Entry(CubicFrame, font=("Arial", 20), textvariable=c)
    C.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.08, anchor="w")

    D = tk.Entry(CubicFrame, font=("Arial", 20), textvariable=d)
    D.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.08, anchor="w")

    button = tk.Button(CubicFrame, text="Calculate", bg="gray",
                       fg="white", font=40, command=lambda: CubicSolver())
    button.place(relx=0.05, rely=0.85, relwidth=0.3, relheight=0.1, anchor="w")


def BinomialExpansion():
    a = int(input("A=\n"))
    b = int(input("B=\n"))
    exponent = (input(
        "What is the exponent of the question\n(quick note: (a+b)^x, the (x) part of that)\n"))
    if (exponent == "one"):
        print("bro why do u even need a python script to do that\n")
        time.sleep(2)
        print("\n\nbru-\n\n\n")
        time.sleep(1)
        print("well...\
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
                                print(
                                    "That is not a valid number, please type out the number instead of using just the integer.")


def PascalsTriangle():
    print("Not completed yet")


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(
    file="/Users/nathan/Documents/Coding/Dog background copy.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0.5, y=0.5, relwidth=1, relheight=1)

MainPage()

root.mainloop()
