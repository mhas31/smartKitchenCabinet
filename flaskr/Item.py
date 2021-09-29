import json

class Item():
    
    def __init__(self, barcode, rgbCode, location = 0, name = '', servings = 0, servingSize = 0, weight=0 ):
        #dict.__init__(self, barcode = barcode, rgbCode = rgbCode, location = 0, name = '', servings = 0, servingSize = 0)
        self.barcode = barcode
        self.colorCode = rgbCode
        self.location = location
        self.name = name
        self.servings = servings
        self.servingSize = servingSize
        self.weight = weight

    def todict(self):

        dic = {
            "barcode" : self.barcode,
            "color code" : self.colorCode,
            "location" : self.location,
            "name" : self.name,
            "servings" : self.servings,
            "serving size" : self.servingSize,
            "weight" : self.weight
        }

        return dic