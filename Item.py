class Item:
    
    def __init__(self, barcode, rgbCode, location = 0, name = '', servings = 0, servingSize = 0 ):
        self.barcode = barcode
        self.colorCode = rgbCode
        self.location = location
        self.name = name
        self.servings = servings
        self.servingSize = servingSize
