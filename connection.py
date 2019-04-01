#STUTI RANA
#ID:85039361
import json
import urllib.parse
import urllib.request
import urllib.error

MAIN_API='https://api.iextrading.com/1.0/stock/'

def first_line()->str:
    company = input()
    return company

def time_range()->int:
    days =  input()
    return int(days)

def make_url_stats(company:str)->str:
    return MAIN_API + '/'+company + '/stats'
def make_url(company:str,time_range:int)->str:
    '''
    Takes the company and time range of interest and puts them into a qeury
    '''
    query_param = [
        ('symbols',company),('types','quote,chart'),
        ('range','5y'),('chartLast',time_range)
        ]
    return MAIN_API+'market' + '/batch?'+ urllib.parse.urlencode(query_param)

def get_data(url:str)->dict:
    '''
    given the url of the item, this scrapes the data and closes the url
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()

def run_connection()->dict:
    '''
    this allows you to call one fucntion and connect and get all the information
    you need
    '''
    company_name = first_line()
    total_shares = get_data(make_url_stats(company_name))
    data = get_data(make_url(company_name,time_range()))
    return data,total_shares
