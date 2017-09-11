# -*- coding: utf-8 -*-
import sys

#reload(sys)
sys.setdefaultencoding('utf8')

import requests, json

data = '''{
    "addBedPrice": "",
    "addValue": "",
    "allowAddBed": "",
    "commissionTypeLocal": "0",
    "commissionValue": "22",
    "computingMethodLocal": "2",
    "currencyCode": "",
    "isEffective": "1",
    "netValue": "120",
    "saleCost": "",
    "salePrice": "",
    "beginDate": "2017-07-15",
    "endDate": "2017-07-15",
    "maxProfit": "",
    "minProfit": "",
    "productID": {
        "hotelID": "90000064",
        "ratePlanID": "475938",
        "roomTypeID": "0008"
    }
} '''
data_ = json.dumps(data)

print( 'data_: ', data_)
print(type(data_))
data__ = eval(data_)
print ('data__: ', data__)
print (type(data__))
data_dic = eval(data__)
print ('data_dic: ', data_dic)
print (type(data_dic))

url = 'http://192.168.230.128:8373/product/productForWin/calculatePrice:8373'
headers = {'content-type':'application/json;charset=UTF-8'}
headers2 = {'content-type':'application/json'}

if __name__ == '__main__':
    r = requests.post(url, headers=headers2, data=data_dic)
    r.encoding = 'utf-8'
    print (r.text)
    print (r.headers)

    print (r.status_code)