import json
import urllib.request
from bs4 import BeautifulSoup


def write_chargebee_events(html_file_path = None, output_path = 'table_events.json'):
    if html_file_path:
        with open(html_file_path) as f:
            soup = BeautifulSoup(f, 'html.parser')
    else:
        with urllib.request.urlopen('https://apidocs.chargebee.com/docs/api/events?prod_cat_ver=2') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
    results = soup.find(id='cb-container') 
    cb_list = results.find_all('div', class_='cb-list cb-list-action') 

    table_events = {}
    for i in cb_list:
        sample = i.find('samp')
        
        try:
            event = sample['id']
        except KeyError:
            pass
        
        if event.startswith('event_') or event.startswith('list_events_'): # hard-coded, to remove event attributes and list_events return type.
            pass    
        else: 
            tables = i.find('dfn', class_='text-muted').text.strip().split(', ')
            for table in tables:
                table = table.replace('(optional)', '')
                if table in table_events:
                    table_events[table].append(event)
                else:
                    table_events[table] = [event]

    with open(output_path, 'w') as f:
        json.dump(table_events, f)
    
    return table_events

if __name__ == '__main__':
    write_chargebee_events(output_path='2.json', html_file_path='chargebee_events.html')

