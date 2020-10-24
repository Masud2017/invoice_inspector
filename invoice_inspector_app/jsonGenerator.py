import json

class Json:
    date = ''
    productName = []
    prices = []
    count = []

    def addProductName(self,productName):
        self.productName.append(productName)

    def addPrices(self,price):
        self.prices.append(price)

    def addCount(self,count):
        self.count.append(count)

    def getJson(self):
        jsonDict = {}
        for x in range(len(self.productName)):
            jsonDict.update({x:{"name":self.productName[x],"price":self.prices[x],"count":self.count[x]}})
        jsn = json.dumps(jsonDict)
        
        return jsn
'''
if __name__ == "__main__":
    obj = Json()
    for _ in range(10):
        obj.addProductName("masud")
    for x in range(10):
        obj.addPrices(x+1)

    for x in range(10):
        obj.addCount(x)

    jsn = obj.getJson()
    jsn = json.loads(jsn)

    for x in jsn:
        print(x,jsn[x])
'''
