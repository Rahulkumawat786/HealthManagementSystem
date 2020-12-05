"""
class to define all the method to write in file for healsth management system
"""
class HealthManagement:
    @staticmethod
    #this is a static method that return the current date and time
    #thsi is not member of class
    def getdate():
        import datetime
        return datetime.datetime.now()
    #writing into file
    def writeInFile(self,name,manag,content):
        file_name = name+str(manag)+".txt" #generating name of file saved according to this folder
        f = open(file_name,"a")
        date = self.getdate()
        f.write(str(date))
        f.write(" "+content+"\n")
        f.close()
        print("Successfully updated file")
    #function for reading the content of file and return it
    def readFromFile(self,name,manag):
        file_name = name+str(manag)+".txt"
        f = open(file_name,"r")
        content = f.read()
        return content

#strating of our code:
print("*****Welcome To Health Management System*****\n")
key = "N"
x = ""  #string variable for management
while key=="N":
    #till now i am adding only three condidate we can add more with the help of a file
    print("Condidate available--")
    print("\t1.Rahul Kumawat")
    print("\t2.Rohan Kumar")
    print("\t3.Sunil Kumar\n")

    user_input = input("Enter condidate name shopwn above: ")
    name = (user_input.split(" ")[0]).capitalize()
    print("we have following management system--")
    print("\t1.food management")
    print("\t2.Exercise management")
    while True:
        manag = int(input("Enter your choice(1/2) = "))
        if manag<1 or manag>2:
            print("Please! enter correct choice!")
        elif manag==1:
            x = "dite"
            break
        else:
            x = "exercise"
            break
    ans = input("If you want to write press 'w' else press'r'(no other input): ").capitalize()
    if ans=="W":
        condidate = HealthManagement()

        content = input(f"Write your {x} here = ")
        condidate.writeInFile(name,manag,content)
        #print("you have successfully written!")
        key = input("Do you want to exit(Y/N): ").capitalize()
    else:
        condidate = HealthManagement()
        content = condidate.readFromFile(name,manag)
        print(content)
        key = input("Do you want to exit(Y/N): ").capitalize()

print("Thankyou! we will glad to see you soon:)")