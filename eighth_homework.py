class Data:
    def __init__(self, data):
        self.data = str(data)
    
    @classmethod
    def my_method(cls, data):
        my_date = []

        for i in data.split():
            if i != '-': data.append(i)
        
        return int(date[0]), int(my_date[1])
    
    @staticmethod
    def my_staticmethod(param):
        pass
    
    today = Data ('11 - 1 - 2001')
    print(today)
    print(Data.my_method(23 - 3 - 1997))
    print(today.my_method(23 - 3 - 1997))