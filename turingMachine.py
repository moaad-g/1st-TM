#Turing machine

class turingMachine:
    def __init__(self, tapeToRead):
        print(tapeToRead)
        self.readingTape = tapeToRead
        self.tape = []
        self.tapePosition = 0
        self.transitionCount = 0

    def no(self):
        print("----------------")
        print("no")
        print(self.readingTape)

    def yes(self):
        print ("yes")
        print(self.readingTape)

#---------------------------------------------

    def state1(self):
        print("----------------")
        self.transitionCount +=1
        print("transition count:"+str(self.transitionCount))

        print(self.readingTape)
        if len(self.readingTape) > self.tapePosition >= 0:
            tapeInput = self.readingTape[self.tapePosition]
        else:
            tapeInput = " "

        print("State 1: reading "+ tapeInput+" at position "+ str(self.tapePosition))
        if tapeInput == "a":
            self.readingTape[self.tapePosition] = "x"
            self.tapePosition += 1
            self.state2()

        elif tapeInput == "b":
            self.no()

        elif tapeInput == "c":
            self.no()

        elif tapeInput == "x":
            self.tapePosition += 1
            self.state1()

        elif tapeInput == " ":
            self.yes()

#---------------------------------------------
    def state2(self):
        print("----------------")
        self.transitionCount +=1
        print("transition count:"+str(self.transitionCount))

        print(self.readingTape)
        if len(self.readingTape) > self.tapePosition >= 0:
            tapeInput = self.readingTape[self.tapePosition]
        else:
            tapeInput = " "

        print("State 2: reading "+ tapeInput+" at position "+ str(self.tapePosition))
        if tapeInput == "a":
            self.tapePosition += 1
            self.state2()

        elif tapeInput == "b":
            self.readingTape[self.tapePosition] = "x"
            self.tapePosition += 1
            self.state3()

        elif tapeInput == "c":
            self.no()

        elif tapeInput == "x":
            self.tapePosition += 1
            self.state2()

        elif tapeInput == " ":
            self.no()

#---------------------------------------------
    def state3(self):
        print("----------------")
        self.transitionCount +=1
        print("transition count:"+str(self.transitionCount))

        print(self.readingTape)
        if len(self.readingTape) > self.tapePosition >= 0:
            tapeInput = self.readingTape[self.tapePosition]
        else:
            tapeInput = " "

        print("State 3: reading "+ tapeInput+" at position "+ str(self.tapePosition))
        if tapeInput == "a":
            self.no()

        elif tapeInput == "b":
            self.readingTape[self.tapePosition] = "b"
            self.tapePosition += 1
            self.state3()

        elif tapeInput == "c":
            self.readingTape[self.tapePosition] = "x"
            self.tapePosition -= 1
            self.state4()

        elif tapeInput == "x":
            self.tapePosition += 1
            self.state3()

        elif tapeInput == " ":
            self.no()

#---------------------------------------------

    def state4(self):
        print("----------------")
        self.transitionCount +=1
        print("transition count:"+str(self.transitionCount))

        print(self.readingTape)
        if len(self.readingTape) > self.tapePosition >= 0:
            tapeInput = self.readingTape[self.tapePosition]
        else:
            tapeInput = " "

        print("State 4: reading "+ tapeInput+" at position "+ str(self.tapePosition))
        if tapeInput == "a":
            self.tapePosition -= 1
            self.state4()

        elif tapeInput == "b":
            self.tapePosition -= 1
            self.state4()

        elif tapeInput == "c":
            self.tapePosition -= 1
            self.state4()

        elif tapeInput == "x":
            self.tapePosition -= 1
            self.state4()

        elif tapeInput == " ":
            self.tapePosition += 1
            self.state1()



#length is 6
turing = turingMachine(["a","a","b","b","c","c"])
turing.state1()


