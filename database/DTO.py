from dataclasses import dataclass
@dataclass
class retailerDTO:
    code:str
    name:str

    def __hash__(self):
        return hash(self.code)

    def __eq__(self,other):
        return self.code==other.code


@dataclass
class vendita_ricavo:
    codeRetailer:str
    numProdotto:int
    ricavo: int
    data:str

    def __hash__(self):
        return hash(self.codeRetailer,self.numProdotto,self.data)
