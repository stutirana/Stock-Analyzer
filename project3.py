#STUTI RANA
#ID:85039361
from indicator import *
from signl import *
import connection

def interest()->str:#gets the third input
    interest = input()
    return interest

def get_dict(data:dict,total_shares:str)->dict:
    '''
    This function prints all the information in the beginning and seperates
    the quote and the chart in json data dictionary
    '''
    keyValues = []
    for i in data.keys():
        keyValues.append(i)
    data = data[keyValues[0]]
    quote = data['quote']
    chart = data['chart']
    print(quote['symbol'])
    print(quote['companyName'])
    print(total_shares)
    return quote,chart

def _organize_data(chart:list)->tuple:
    '''
    This gives you a list of closing prices, the volumes, lows and highs.
    Made them a tuple so there was possiblity that the values would be altered.
    '''
    highs =()
    lows=()
    closings=()
    volume=()
    for day in chart:
        highs+=(float(day['high']),)
        lows+=(float(day['low']),)
        closings += (float(day['close']),)
        volume += (float(day['volume']),)
    return highs,lows,closings,volume

def create_indicator(chart:list, interest:[str])->true_range_indicator or moving_average_indicator or directional_indicator:
    '''
    This function initializes the the indicator object given the input
    and the highs,lows, closing prices or volumes (depending on what kind
    of object it is).
    '''
    highs,lows,closing,volume=_organize_data(chart)

    if interest[0].upper() == "TR":
       indicator = true_range_indicator(highs,lows,closing)
    elif interest[0] =='MP':
        indicator= moving_average_indicator(closing,int(interest[1]))
    elif interest[0] =='MV':
        indicator = moving_average_indicator(volume,int(interest[1]))
    elif interest[0] == 'DP':
        indicator = directional_indicator(closing,interest[1])
    elif interest[0] =='DV':
        indicator = directional_indicator(volume,interest[1])
    return indicator

def create_signl(interest:[str],indicator:tuple)->moving_average_signal or true_range_signal or directional_signal:
    '''
    This is will initialize a signal object given the indicators and
    the input. Also calls and organizes the needed information and passes
    it to the the class initialization.
    '''
    highs,lows,closing,volume=_organize_data(chart)
    if interest[0].upper() == "TR":
        signl = true_range_signal(interest[1], interest[2],indicator)
    elif interest[0] =='MP':
        signl= moving_average_signal(indicator,closing,interest[1])
    elif interest[0] =='MV':
         signl = moving_average_signal(indicator,volume,interest[1])
    elif interest[0] == 'DP':
        signl = directional_signal(interest[2],interest[3],indicator)
    elif interest[0] =='DV':
        signl = directional_signal(interest[2],interest[3],indicator)
    return signl


def analysis(quote:dict,chart:list,interest:str)->None:
    '''
    This initializes and calculates the the signal and indicator objects.
    It utilizes duck-typing since it creates and object or indicator or signal
    by calling the create functions respectively; and then it calls the calc()
    method which is in all of the classes. Then it calls the print_info() method
    and the inforamtion is printed.
    '''
    
    interest=interest.split()
    indicator= create_indicator(chart,interest)
    indicator = indicator.calc()
    sig = create_signl(interest,indicator)
    buy,sell = sig.calc()
    print_info(chart, indicator,buy,sell)

    

def print_info(chart:list,indicator:tuple,buy:tuple,sell:tuple)->None:
    '''
    This function prints the information, by using string formatting.
    '''    
    print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?')
    i= 0
    for day in chart:
        if type(indicator[i]) == float:
            print('{}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{}\t{:.4f}\t{}\t{}'.format(day["date"],\
                                                                       float(day['open']), \
                                                                       float(day['high']), \
                                                                       float(day['low']), \
                                                                       float(day['close']),\
                                                                       int(day['volume']),\
                                                                           indicator[i], buy[i], sell[i]))
        else:
            print('{}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{}\t{}\t{}\t{}'.format(day["date"],\
                                                                       float(day['open']), \
                                                                       float(day['high']), \
                                                                       float(day['low']), \
                                                                       float(day['close']),\
                                                                       int(day['volume']),\
                                                                           indicator[i], buy[i], sell[i]))
        i+=1
        
if __name__ == "__main__":
    data,total_shares = connection.run_connection()#runs the connection
    total_shares = total_shares['sharesOutstanding']#gets the value needed from total_shares
    quote,chart = get_dict(data,total_shares)#print the first information
    analysis(quote,chart, interest())#ask for input about indicator/signal and calls the analysis function
