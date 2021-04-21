import json, difflib, numpy

class Thesaurus:
    def __init__(self, pathToDataset):
        self.data = json.load(open(pathToDataset))

    def loadData(self, pathToDataset):
        self.data = json.load(open(pathToDataset))

    def getEntry(self, phrase):
        return self.data[phrase]

    def hasEntry(self, phrase):
        return phrase in self.data
    
    def getSimilar(self, phrase):
        similar = []
        for p in numpy.unique([phrase, phrase.title(), phrase.upper(), phrase.lower()]):
            similar += difflib.get_close_matches(p, list(self.data.keys()))
        return numpy.unique(similar)

def main():
    t = Thesaurus("./data.json")

    print("Welcome to the Thesaurus. Type a phrase to see the definition.")

    while True:
        userInput = input("Enter a phrase (!q to quit): ")

        if userInput in ["!q", "!exit", "!quit"]:
            break
        
        similarInput = t.getSimilar(userInput)

        if t.hasEntry(userInput):
            for entry in t.getEntry(userInput):
                print(entry)
        elif len(similarInput) == 1:
            print("Showing result for: " + similarInput[0])
            for entry in t.getEntry(similarInput[0]):
                print(entry)
        elif len(similarInput) > 1:
            print("Did you mean: ")
            for i in similarInput:
                print(i)
        else:
            print("Input not recognized.")

if __name__ == "__main__":
    main()