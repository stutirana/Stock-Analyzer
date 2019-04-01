#STUTI RANA
#ID:85039361
class true_range_signal():
    #THIS IS A TRUE_RANGE SIGNAL CLASS
    
    def __init__(self, buy_threshold:str,sell_threshold:str,indicator:tuple):
        '''
        I wanted these as the attributes so that multiple functions can access
        them and because the thresholds and indicator should define what this class
        is.
        '''
        self._buyo= (buy_threshold[0])
        self._buy = float(buy_threshold[1::])
        self._sello=(sell_threshold[0])
        self._sell = float(sell_threshold[1::])
        self._ind = indicator

    def _greater_than_buy(self)->tuple:
        #given the buy threshold is greater than a number
        #the fucntion iterates through the indicator to see
        #where the threshold is greater than a value in the indicator
        buy_tuple=()
        copy = self._ind
        for val in copy:
            if type(val) == float:
                if self._buy < val:
                    buy_tuple+=('BUY',)
                else:
                    buy_tuple+=('',)
            else:
                buy_tuple+=('',)
        return buy_tuple
    
    def _less_than_buy(self)->tuple:
        #given the buy threshold is less than a number
        #the fucntion iterates through the indicator to see
        #where the threshold is less than a value in the indicator
        buy_tuple=()
        copy = self._ind
        for val in copy:
            if type(val) == float:
                if self._buy>val:
                    buy_tuple+=('BUY',)
                else:
                    buy_tuple+=('',)
            else:
                buy_tuple+=('',)
        return buy_tuple
    
    def _greater_than_sell(self)->tuple:
        #given the sell threshold is greater than a number
        #the fucntion iterates through the indicator to see
        #where the threshold is greater than a value in the indicator
        sell_tuple=()
        copy = self._ind
        for val in copy:
            if type(val) == float:
                if self._sell<val:
                    sell_tuple+=('SELL',)
                else:
                    sell_tuple+=('',)
            else:
                sell_tuple+=('',)
        return sell_tuple
    def _less_than_sell(self)->tuple:
        #given the sell threshold is less than a number
        #the fucntion iterates through the indicator to see
        #where the threshold is less than a value in the indicator
        sell_tuple=()
        copy = self._ind
        for val in copy:
            if type(val) == float:
                if self._sell>val:
                    #print(val)
                    sell_tuple+=('SELL',)
                else:
                    sell_tuple+=('',)
            else:
                sell_tuple+=('',)
        return sell_tuple

    def calc(self)->tuple:
        '''
withour using the operator module, by directly discerning what the user inputed, I
pass the buy/sell threshold
to a greater or less than function
        '''
        if self._buyo == '>' :
            buy_tuple = self._greater_than_buy()
        elif self._buyo == '<':
            buy_tuple = self._less_than_buy()
        if self._sello == '>':
            sell_tuple = self._greater_than_sell()
        elif self._sello == '<':
            sell_tuple = self._less_than_sell()
        return buy_tuple,sell_tuple

class moving_average_signal():
    def __init__(self,indicator:tuple,interest:tuple,num:str):
        '''
        I wanted these as the attributes so that multiple functions can access
        them and because the closing_price or volumes and the indicators
        should always define what other objects of this class.
        '''
        self._intr =interest
        self._ind = indicator
        self._days= int(num)
    def _generate(self)->tuple:
        #the first elements are empty becuase the indicator also has
        #no values for those slots since there a N day moving average.
        i=0
        buy_tuple=()
        sell_tuple=()
        
        while i+1<=self._days:
            buy_tuple+=('',)
            sell_tuple+=('',)
            i+=1
        return buy_tuple,sell_tuple
            
    def calc(self)->tuple:
        '''
        if the closing_prices/volume of the current day is greater/less than current days
        indicator value AND the previous day's closing_price/volume is greater/less
        than yesterday indicator we generate a Buy or Sell signal
        '''
        buy_tuple,sell_tuple= self._generate()#we intialize the first elements of the tuple
        i=self._days
        while i < len(self._intr):
            if type(self._ind[i]) == float:
                if self._intr[i]<self._ind[i] and self._ind[i-1]<self._intr[i-1]:
                    sell_tuple+=('SELL',)
                else:
                    sell_tuple+=('',)
                if self._intr[i]>self._ind[i] and self._ind[i-1]>self._intr[i-1]:
                    buy_tuple+=('BUY',)
                else:
                    buy_tuple += ('',)
                i+=1
            else:
                buy_tuple += ('',)
                sell_tuple+=('',)
        return buy_tuple,sell_tuple
                



class directional_signal():
    def __init__(self,buy_threshold:str,sell_threshold:str,indicator:tuple):
        '''
        I wanted these as the attributes so that multiple functions can access
        them and because the thresholds and indicators
        should always define what other objects of this class.
        '''
        self._b= int(buy_threshold)
        self._s=int(sell_threshold)
        self._intr = indicator
    def _convert(self):
        new=[]
        indicator= list(self._intr)
        for i in indicator:
            if type(i)== str and '+' in i:
                i=i.replace('+','')
                i=int(i)
                new.append(i)
            else:
                new.append(i)
        return tuple(new)
    def calc(self)->tuple:
        '''
        while the buy threshold of current day is less than the indicator of that day
        and the buy threshold is greater than or equal to yesterday's indicator then we generate a Buy
        signal
        while the sell threshold of the current day is greater than the indicator of today and the
        sell threshold is less than or equal to yesterday's indicator then we generate a sell signal
        '''
        buy_tuple=()
        sell_tuple=()
        indc= self._convert()
        for i in range(len(indc)):
            if i!=0:
                if type(indc[i]) == int:
                    if indc[i]>self._b and indc[i-1]<=self._b:
                        buy_tuple+=('BUY',)
                    else:
                        buy_tuple+=('',)
                    if indc[i]<self._s and indc[i-1]>= self._s:
                        sell_tuple+=('SELL',)
                    else:
                        sell_tuple+=('',)
                else:
                    sell_tuple+=('',)
                    buy_tuple+=('',)
            else:
                sell_tuple+=('',)
                buy_tuple+=('',)
        return buy_tuple,sell_tuple        
