#Arrays have a fixed size

class Array:
    def __init__(self, Datatype, Arraylength):
        self.data_type=type
        self.array_length=Arraylength
        self.array = []

    def insert(self,value,index):
        if(self.data_type==type(value) and index<= self.array_length-1 and self.array[index]==None):
            self.array[index]=value
            
    def access(self,index):
        if(index<= self.array_length-1):
            return self.array[index]
                  
    def remove(self,index): #Deletion in arrays usually involves shifting elements to fill the gap.?
        if(self.data_type==type(value) and index<= self.array_length-1):
            self.array[index]=value
            
    def delete(self):