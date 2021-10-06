class PassStrength:

    # Two objectives
    # 1. Make a password
    # 2. Guess the strength of the password
    # 1a. This is the easy part
    # 1b. There are several things that make a bad password
    # 2b. Using words,
    # names, a group of numbers (birthday: 0801000), short password
    #commitance
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

        def lowerCase(self, letter:str):
            lower = False
            lowList = list(range(97, 123))
            asciiVal = ord(letter)

            if(lowList.count(asciiVal) == 1):
                return True
            else:
                return lower