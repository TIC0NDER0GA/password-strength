class PassStrength:

    # Two objectives
    # 1. Make a password
    # 2. Guess the strength of the password
    # 1a. This is the easy part
    # 1b. There are several things that make a bad password
    # 2b. Using words,
    # names, a group of numbers (birthday: 0801000), short password
    # commitance

        def __init__(self):
            self.password = ""


        def hasNum(self, p: str):
            num = False
            for x in p:
                if ord(x) < 59:
                    if ord(x) > 47:
                        num = True
                if ord(x) > 47:
                    if ord(x) < 59:
                        num = True
            return num


        def numOfNum(self, p:str):
            count = 0;
            for x in p:
                if (self.isANum(x)):
                    count = count + 1
            return count


        def isANum(self, p:str):
            num = False;
            numList = list(range(47,59))
            asciiVal = ord(p)
            if (numList.count(asciiVal) == 1):
                return True
            else:
                return num;

        def isLowerCase(self, letter:str):
            lower = False
            lowList = list(range(97, 123))
            asciiVal = ord(letter)

            if(lowList.count(asciiVal) == 1):
                return True
            else:
                return lower

        def isUpperCase(self, letter: str):
            lower = False
            lowList = list(range(65, 91))
            asciiVal = ord(letter)

            if (lowList.count(asciiVal) == 1):
                return True
            else:
                return lower


        def lowerCaseWhole(self, letter: str):
            checker = False
            for x in letter:
                if (self.isLowerCase(x) == True):
                    checker = True
            return checker


        def upperCaseWhole(self, letter: str):
            checker = False
            for x in letter:
                if (self.isUpperCase(x) == True):
                    checker = True
            return checker

        def numOfUpper(self, letter:str):
            count = 0;
            for x in letter:
                if (self.isUpperCase(x)):
                    count = count + 1
            return count


        def numOfLower(self, p:str):
            count = 0;
            for x in p:
                if (self.isLowerCase(x)):
                    count = count + 1

            return count

