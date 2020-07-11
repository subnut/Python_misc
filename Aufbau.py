# Aufbau
class Aufbau:
    def __init__(self, args=None):
        if args is not None:
            self.updateInput(args)

    def updateInput(self, args=None):
        if args is not None:
            if isinstance(args, str):
                self.globalOrbitalList = args
                self.generateFromOrbitalList()
            if isinstance(args, int):
                self.globalLastOrbit = args
                self.generateFromLastOrbit()

    def generateFromOrbitalList(self, orbitalList=None):
        if not orbitalList:
            try:
                orbitalList = self.globalOrbitalList
            except NameError:
                raise NameError("Orbital list not defined")
        orbitList = [None]
        for orbitNo in range(1, 2*len(orbitalList)+1):
            orbitList.append(str(orbitNo))
        self.globalOrbitList = orbitList
        self.generateOutput()

    def generateFromLastOrbit(self, lastOrbit=None):
        if not lastOrbit:
            try:
                lastOrbit = self.globalLastOrbit
            except NameError:
                raise NameError('Last orbit number not specified')
        if lastOrbit not in range(1, 25):
            print("Last orbit must be an integer from 1 to 24")
            return
        if lastOrbit % 2 != 0:
            print("""WARNING: Provided outermost orbital number is odd
Rounding off to next even number ...""")
        lastOrbit = (lastOrbit + 1) // 2
        self.globalOrbitalList = "spdfghijklmnopqrstuvwxyz"[:lastOrbit]
        self.generateFromOrbitalList()

    def generateOutput(self):
        orbitalList = self.globalOrbitalList
        orbitList = self.globalOrbitList
        returnList = []
        for currentEnergy in range(1, 2*len(orbitalList)+1):
            for currentOrbitEnergy in range(len(orbitList)):
                for currentOrbitalEnergy in range(currentOrbitEnergy):
                    if currentOrbitEnergy + currentOrbitalEnergy == currentEnergy:
                        returnList.append(orbitList[currentOrbitEnergy]
                                          + orbitalList[currentOrbitalEnergy])
                        break
                    else:
                        continue
                    break
        self.globalOutput = returnList

    def printList(self):
        for orbital in self.globalOutput:
            print(orbital)

    def printChart(self):
        for orbit in self.globalOrbitList:
            for orbital in self.globalOutput:
                if orbital[:-1] == str(orbit):
                    if len(self.globalOrbitList[-1]) > 1 and len(orbital) < 3:
                        print('0' + orbital, end=' ')
                    else:
                        print(orbital, end=' ')
            if orbit and int(orbit) > len(self.globalOrbitalList):
                print('...', end=' ')
            print()
        print()


def main(userObject):
    print("""What do you have?
    1. Orbital List
    2. Last Orbit number""")
    userInput = input("Enter your option: ")
    if userInput not in ('1', '2'):
        print("Invalid option!")
        return
    elif userInput == '1':
        userInput = input("Please enter the order of the orbitals WITHOUT whitespace: ")
    elif userInput == '2':
        userInput = input("Please enter the last orbit number: ")
        if not userInput.isalnum():
            print("Invalid number")
            return
        userInput = int(userInput)
    userObject.updateInput(userInput)
    print("""What do you want to print?
    1. Aufbau Chart
    2. Aufbau List""")
    userInput = input("Enter your option: ")
    if userInput not in ('1', '2'):
        print("Invalid option!")
        return
    elif userInput == '1': userObject.printChart()
    elif userInput == '2': userObject.printList()


if __name__ == '__main__':
    userObject = Aufbau()
    print("To quit,  press Ctrl-C anytime")
    while True:
        try:
            main(userObject)
        except KeyboardInterrupt:
            print("\nExiting ...")
            break
