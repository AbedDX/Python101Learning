class IConverter():
    def convert(self,amount,currency):
        pass
        
class DollarConverter(IConverter):
    def convert(self,amount,currency):
        if currency == "euro":
            return amount * 1.07
        if currency == "yen":
            return amount * 0.0068
        return amount
        
class EuroConverter(IConverter):
    def convert(self,amount,currency):
        if currency == "dollar":
            return amount * 0.93
        if currency == "yen":
            return amount * 0.0064
        return amount
        
class YenConverter(IConverter):
    def convert(self,amount,currency):
        if currency == "dollar":
            return amount * 146.78
        if currency == "euro":
            return amount * 157.39
        return amount
        
def Factory(currency = "dollar"):
    currencyconverters = {
        "dollar":DollarConverter,
        "euro":EuroConverter,
        "yen":YenConverter
    }
    
    return currencyconverters[currency]()
    
def main():
    
    converters = []
    converters.append(Factory("dollar"))
    converters.append(Factory("euro"))
    converters.append(Factory("yen"))
    
    for c in converters:
        print("Dollars:",str(c.convert(100,"dollar")))
        print("Euros:",str(c.convert(100,"euro")))
        print("Yen:",str(c.convert(10000,"yen")))
        
if __name__ == "__main__":
	main()  