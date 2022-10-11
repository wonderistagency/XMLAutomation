from logging import root
from wsgiref import headers
import requests
import json
import xml.etree.cElementTree as xmlparser

def xml_parser(monday_board, item_id, thirty_day_report, ninety_day_report, keyword_report):
    xml_directory = "test_file.xml"
    xml_file = xmlparser.ElementTree(file=xml_directory)
    root = xml_file.getroot()
    
    for i in root:
        if i.tag == "monday_board":
            monday_board = i.text
        
        if i.tag == "item_id":
            item_id = i.text

        if i.tag == "thirty_day_report":
            thirty_day_report = i.text
        
        if i.tag == "ninety_day_report":
            ninety_day_report = i.text

        if i.tag == "keyword_report":
            keyword_report = i.text

    return [monday_board, item_id, thirty_day_report, ninety_day_report, keyword_report]


if __name__== '__main__':
    
    monday_board=""
    item_id=""
    thirty_day_report=""
    ninety_day_report=""
    keyword_report=""

    #call to the parse fucntion
    xml_list = xml_parser(monday_board, item_id, thirty_day_report, ninety_day_report, keyword_report)
    
    monday_board=xml_list[0]
    item_id=xml_list[1]
    thirty_day_report=xml_list[2]
    ninety_day_report=xml_list[3]
    keyword_report=xml_list[4]


    url = "https://api.monday.com/v2" #API URL  
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE3ODE0NTQ0NiwidWlkIjozMzc0OTY1MywiaWFkIjoiMjAyMi0wOC0zMFQwODo0NToyMS4zMDNaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTMyNTYxNDgsInJnbiI6InVzZTEifQ.UXdEKYBPzt7tmW0WMiRkSVjV6jMXLwhR8ELpFJgGzAU"
    app_headers = {"Content-Type":"application/Json","Authorization" : api_key}

    query2 = """
        mutation {
            create_update (item_id: 3159884603, body: "%s") {
        id
    }
}
""" % (thirty_day_report)
    data = {'query' : query2}
    response = requests.post(url, json=data, headers=app_headers)

    if response.status_code == 200:
        print(response.content)
