class AHitem():
    def __init__(self, id, df):
        self.item_id = id
        self.name = id
        for i in range(len(df['id'])):
            if df['id'][i]==id:
                self.name = df['name'][i]
                break
        self.min_price = 0
        self.market_price = 0
        # self.average_median_price = 0
        self.current_num = 0
        self.sold_per_day = 0

    def show(self,df):
        print(self.name, ': ', end=' ')
        for i in range(len(df['id'])):
            if df['id'][i]==self.item_id:
                index = i
                break
        wtb = df['wtb'][index]
        wts = df['wts'][index]
        try:
            if self.market_price<=wtb*0.8:
                print('我tm氪爆')
            elif self.market_price<=wtb:
                print('看情况买点')
            elif self.min_price<=wtb:
                print('有空可以偷鸡')
            # elif self.market_price<=self.average_median_price*0.8:
            #     print("低于平均水平")

            elif self.min_price>=wts*1.2:
                print('抓紧时间清仓')
            elif self.min_price>=wts:
                print('可以考虑回血')
            elif self.market_price>=wts:
                print('随便摆摆吧')
            # elif self.market_price>self.average_median_price*1.2:
            #     print('高于平均水平')
            else:
                print('今天又是平平无奇的一天')
            print('min price:', self.min_price, '\tmarket price:', self.market_price, '\tdemand:', self.sold_per_day)
        except:
            print('error loading data from wowuction')
            self.showall()


    def showall(self):
        print(self.__dict__)