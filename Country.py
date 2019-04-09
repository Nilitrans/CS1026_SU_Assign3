#class cs1026
class Country:
    def __init__(self,name,pop,area,countinent):

        self._name=name
        self._pop=pop
        self._area=area
        self._countinent=countinent
        #initiate the class
    def _repr_(self):
        return str(self._name)+"in"+str(self._countinent)
    #return the  string representation of the class
    def setPopulation(self,pop):
        self._pop=pop# set population as specified
    def getName(self):
        return self._name
        #get the name of the object
    def getArea(self):
        return self._area
    #get the area of the object
    def getPopulation(self):
        return self._pop
    #get the population of the object
    def getCountinent(self):
        return self._countinent
    #get the continent of the object
    def getPopDensity(self):
        self._PopDensity=self._pop/self._area
        #calculate and return the density of the object

#test part#
