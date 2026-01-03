class Students():
    def __init__ (self, name, height, age, allergies, ecn):
        self.name = name
        self.height = height
        self.age = age
        self.allergies = allergies
        self.ecn = ecn

    def ChangeDetails(self):
        answer1 = input("What is your name? ")
        self.name = answer1
        answer2 = input("What is your height? ")
        self.height = answer2
        answer3 = input("What is your age? ")
        self.age = answer3
        answer4 = input("What is your allergies? ")
        self.allergies = answer4
        answer5 = input("What is your ecn? ")
        self.ecn = answer5

    def PrintDetails(self):
        list = [self.name, self.height, self.age, self.allergies, self.ecn]
        for item in list:
            print(f"<{item}>,", end = " ")
        print("")

    def Main(self):
        while True:
            answer = input("Do you want to Change Details or Print Details? ").lower().strip()
            if answer == "change details":
                self.ChangeDetails()
            elif answer == "print details":
                self.PrintDetails()
            else:
                print("Answer is not correct")

s1 = Students("Andy Segment", "1.5 metres", "12 yrs", "None", "05828392739")
s1.Main()