# CIS129 Module 12 Lab
# Author: Micah Turpin
# 5/16/2024

# main module
def main():

    # create a Pet object
    Animal = Pet()

    # Get values for a pet
    print("Enter a pet name:")
    inputName = input()
    Animal.setName(inputName)

    print("Enter a pet type:")
    inputType = input()
    Animal.setType(inputType)

    print("Enter a pet age:")
    inputAge = int(input())
    Animal.setAge(inputAge)

    # Show values for this pet
    print("The pet name:", Animal.getName())
    print("The pet type:", Animal.getType())
    print("The pet age:", Animal.getAge())


class Pet:
  	# Constructor
    def _init_(self):
        self.name = n
        self.type = t
        self.age = a

  	# Mutators
    def setName(self, n):
        self.name = n
    def setType(self, t):
        self.type = t
    def setAge(self, a):
        self.age = a

  	# Accessors
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age

# Call main function
main()
