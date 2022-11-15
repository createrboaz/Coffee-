class BMI:
    def getdata(self):
        height=float(input('Enter Height in m'))
        mass=float(input('Enter Mass in kg'))   
    def bodymassindex(self,):
        self.bmi=(self.mass/(self.height**self.height))
            print(self.bmi)
    def suggestions(self):
        if self.bmi <=18:
            print('A BMI of under 18.5 indicates that a person has insufficient weight,\n so they may need to put on some weight. They should ask a doctor \n or dietitian for advice.')
        elif self.bmi >18 and self.bmi<=25:
            print("A BMI of 18.5 - 24.9 indicates that a person has a healthy weight for \ntheir height. By maintaining a healthy weight, they can lower their\n risk of developing serious health problems.")
        elif self.bmi >25 and self.bmi<=30:
            print("A BMI of 25 - 29.9 indicates that a person is slightly overweight. A \n doctor may advise them to lose some weight for health reasons. They \n should talk with a doctor or dietitian for advice.")
        elif self.bmi >30:
            print("A BMI of over 30 indicates that a person has obesity. Their health may \n be at risk if they do not lose weight. They should talk with a \n doctor or dietitian for advice.")
ob=BMI()
ob.getdata()
ob.bodymassindex()
ob.suggestions() 
