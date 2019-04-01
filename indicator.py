#STUTI RANA
#ID:85039361
class true_range_indicator():
    #THIS IS THE TRUE RANGE INDICATOR CLASS
    
    def __init__(self,highs:tuple,lows:tuple,closing:tuple):
        '''
        IT PUTS THE NECESSARY INFORMATION AS ITS ATTRIBUTES
        I chose to put these as attributes because all true range
        indicators will have these properties in common.
        '''
        self._highs = highs
        self._lows = lows
        self._close = closing
        self._days = len(highs)
        
    def calc(self)->tuple:
        '''
        Based on the if the close of yesterday is greater or less than the
        high of today, we append the range of prices divided yesterday's close*100
        becuase we a percent.It returns a tuple of indicators.
        '''
        tr_days=('',)
        i = 1
        while i <= (len(self._highs)-1):
            if self._close[i-1]>self._highs[i]:
                obj = ((self._close[i-1]-self._lows[i])/self._close[i-1])*100
                tr_days+=(obj,)
            elif self._close[i-1] < self._lows[i]:
                obj = ((self._highs[i]-self._close[i-1])/self._close[i-1])*100
                tr_days+=(obj,)
            else:
                obj = ((self._highs[i]-self._lows[i])/self._close[i-1])*100
                tr_days+=(obj,)
            i+=1 
        return tr_days        
    
class moving_average_indicator():
    #THIS IS MOVING_AVERAGE INDICATOR
    def __init__(self,interest:tuple,interval:int):
        '''
        I wanted these as the attributes so that multiple functions can access
        them and because the closing_price or volumes and the days/interval
        should always define what other objects of this class.
        '''
        self._intr = interest
        self._interval = interval
        
    def calc(self)->tuple:
        '''
        This calculates the moving average.
        It first puts an empty string until the N-1 day is hit.
        From there it makes a 'moving' list of the closing_prices or volumes.
        It makes a list of every 10 objects and sums them and then divided by
        the N days(number of objects), giving you the average of every 10 days.
        Then we returna tuple of averages
        '''
        j=0
        i=0
        averages=()        
        copy = list(self._intr)
        sum_list=[]
        while j+1 < self._interval:
            averages+=('',)
            j+=1
        while i < len(self._intr)-(self._interval-1):
            copy=self._intr[i::]
            sum_list=copy[0:self._interval]
            obj = sum(sum_list)/self._interval
            averages+=(obj,)
            i+=1
        return averages


class directional_indicator():
    
    def __init__(self, interest:tuple,rangez:str):
        '''
        I wanted these as the attributes so that multiple functions can access
        them and because the closing_price or volumes and the days/interval
        should always define what other objects of this class.
        '''
        self._range= int(rangez)
        self._intr = interest
    def initial_days(self):
        #until it hits the Number or days specified, it keeps only comparing todays
        #and yesterday's prices/volumes
        i=0
        itr=0
        copy = list(self._intr)
        indicator_list=[]
        directionality = (0,)
        while i < self._range-1:
            copy = self._intr[i::]
            if copy[0]>copy[1]:
                itr-=1
                directionality+=(itr,)
            elif copy[0]<copy[1]:
                itr+=1
                directionality+=(itr,)
            elif copy[0] == copy[1]:
                prev= directionality[-1]
                directionality+=(prev,)
            i+=1
        return directionality
    def calc(self)->tuple:
        '''
        after getting values until N. We make a 'moving' list of sorts with N number of objects
        the function compares the overall rise and fall in that list and outputs if
        during that N day time period how much the stock incresed or decreased.
        '''
        i=0
        new=[]
        directionality=list(self.initial_days())

        while i<=(len(self._intr)-self._range-1):
            copy=list(self._intr[i:self._range+i+1])
            j=0
            count=0
            #print(copy)
            while j<self._range:
                
                sum_list=copy[j:j+2]
                #print(sum_list,end='')
                if sum_list[0]>sum_list[1]:
                    count-=1
                elif sum_list[0]<sum_list[1]:
                    count+=1
                elif sum_list[0] == sum_list[1]:
                    count+=0
                #print(count)
                j+=1
            
            new.append(count)
            i+=1
        directionality.extend(new)
        ult=[]
        for i in directionality:
            if i > 0:
                i= '+'+str(i)
                ult.append(i)
            else:
                ult.append(i)
        directionality = tuple(ult)
        return directionality
                
        
        
