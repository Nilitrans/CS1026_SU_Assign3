#class cs1026
from Country import Country
class CountryCatalogue:
    def __init__(self,continentFileName,countryFileName):#open the file
        cDictionary=dict()
        catalogue=[]#create the variables
        fileContinent=open(continentFileName,"r")
        allContentinContinent=fileContinent.readlines()
        for line in allContentinContinent:
            line=line.strip("\n")
            line=line.split(",")
            cDictionary[str(line[0])]=line[1]
        cDictionary.pop("Country")
        self._cDictionary=cDictionary
        #create the dictionary
        fileCountry=open(countryFileName,"r")
        allContentinCountry=fileCountry.readlines()
        for line in allContentinCountry:
            line=line.strip("\n")
            line=line.split("|")
            if line[0]=="Country":
                continue
            else:
                temp=Country(line[0],line[1],line[2],self._cDictionary[line[0]])
                catalogue.append(temp)
        self._catalogue=catalogue
        #create the catalogue within which the element is country class object
        fileContinent.close()
        fileCountry.close()


    def addCountry(self,countryName,countryPopulation,countryArea,countryContinent):
        if countryName in self._cDictionary.keys():
            return False
        else:
            temp2=Country(countryName,countryPopulation,countryArea,countryContinent)
            self._catalogue.append(temp2)
            (self._cDictionary)[countryName]=countryContinent
###
            return True

    def deleteCountry(self,countryName):
        if countryName in self._cDictionary.keys():
            self._cDictionary.pop(str(countryName))
 ###c
            for i in range(len(self._catalogue)):
                if self._catalogue[i-1].getName()==countryName:
                    self._catalogue.pop(i-1)
                    print("The country has been successfully removed")

        else:
            print("The country has not been successfully removed")

            # self._catalogue.pop(countryName)
            # if countryName not in self._catalogue:
            #     print("The country has been successfully removed")
            # if countryName in self._catalogue:
            #     print("The country has not been successfully removed")

    def findCountry(self,countryName):
        for i in range(len(self._catalogue)):
            if self._catalogue[i-1].getName()==countryName:
                return countryName


    def filterCountry(self,continentName):
        temp=[]
        for i in range(len(self._cDictionary)):
            if continentName==self._cDictionary[self._catalogue[i-1]]:
                temp.append(self._catalogue[i-1])
        return temp


    def printCountryCatalogue(self):
        for i in range(len(self._catalogue)):
            print(self._catalogue[i-1]._repr_())

    def setPopulationOfSelectedCountry(self,countryName,countryPopulation):
        for i in range(len(self._catalogue)):
            if self._catalogue[i-1].getName()==countryName:
                self._catalogue[i-1].setPopulation(countryPopulation)
                return True
            else:
                return False


    def findCountryWithLargestPop(self):
        large=self._catalogue[0]
        for i in range(len(self._catalogue)):
            if self._catalogue[i-1].getPopulation()>=self._catalogue[i].getPopulation():
                large=self._catalogue[i-1]

    def findCountryWithSmallestPop(self):
        small=self._catalogue[0]
        for i in range(len(self._catalogue)):
            if self._catalogue[i-1].getPopulation()<=self._catalogue[i].getPopulation():
                small=self._catalogue[i-1]

    def filterCountriesByPopDensity(self,lowerBound,upperBound):
        temp=[]
        for i in range(len(self._catalogue)):
            if lowerBound<=self._catalogue[i-1].getPopulation()<=upperBound:
                temp.append(self._catalogue[i-1].getName())
        return temp
    def findMostPopulousContinent(self):
        mostPopCont=""
        popMaxCont=0
        temp=dict()
        temp2=[]
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        for i in range(len(self._catalogue)):
            if self._catalogue[i-1].getContinent()=="Asia":
                count1=count1+self._catalogue[i-1].getPopulation
            elif self._catalogue[i-1].getContinent()=="Africa":
                count2=count2+self._catalogue[i-1].getPopulation
            elif self._catalogue[i-1].getContinent()=="Europe":
                count3=count3+self._catalogue[i-1].getPopulation
            elif self._catalogue[i-1].getContinent()=="North America":
                count4=count4+self._catalogue[i-1].getPopulation
            else:
                count5=count5+self._catalogue[i-1].getPopulation
        temp["Asia"]=count1
        temp["Africa"]=count2
        temp["Europe"]=count3
        temp["North America"]=count4
        temp["South America"]=count5
        temp2.append(count1)
        temp2.append(count2)
        temp2.append(count3)
        temp2.append(count4)
        temp2.append(count5)
        popMaxCont=max(temp2)
        for i in range(len(temp)):
            if temp[i]==popMaxCont:
                mostPopCont==temp[i].key()

        return (mostPopCont,popMaxCont)
    def saveCountryCatalogue(self,filename):
        count=0
        file=open(filename,"w")
        for i in range(len(self._catalogue)):
            string=self._catalogue[i-1].getName()+"|"+self._catalogue[i-1].getContinent()+"|"+str(self._catalogue[i-1].getPopulation())+"|"+str(self._catalogue[i-1].getPopDensity())
            file.writelines(string)
        file.close()





