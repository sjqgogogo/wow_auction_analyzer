class AHitem():
    def __init__(self, id, df):
        self.item_id = id
        self.name = id
        for i in range(len(df['id'])):
            if df['id'][i]==id:
                self.name = df['name'][i]
                break
        self.current_price = []
        self.median_price = []
        self.mean_price = []
        self.quantity = []

    def show(self,df):
        print(self.name, end=': ')
        for i in range(len(df['id'])):
            if df['id'][i]==self.item_id:
                index = i
                break
        wtb = df['wtb'][index]
        wts = df['wts'][index]
        try:
            # wtb
            if self.current_price<=wtb*0.8:
                print('very cheap')
            elif self.current_price<=wtb:
                print('cheap')

            # wts
            elif self.current_price>=wts*1.2:
                print('very expensive')
            elif self.current_price>=wts:
                print('expensive')
            else:
                print('just another day')
            print('price:', self.current_price, '\tquantity:', self.quantity,
                  '\tmedian price:', self.median_price, '\tmean price:', self.mean_price)
        except:
            print('error collecting data from the website')
            self.showall()


    def showall(self):
        print(self.__dict__)