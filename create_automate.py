import csv
file=open('automate.bat','w')


urls=open('urls_list.csv','r')
csvreader=csv.reader(urls)
# next(csvreader)

def get_url(url):
    url=url.lower()
    
    if url.startswith('www'):
        return 'https://'+url
    if not url.startswith('http'):
        return 'https://www.'+url
    s=url.split('//')
    if s[1].startswith('www'):
        return 'https://'+s[1]
    else:
        return 'https://www.'+s[1]
def get_domain(url):
    return url[12:].split('/')[0]
for i in csvreader:
    
    company_name=i[0]
    company_name.strip('"')
    start_url=get_url(i[1])
    allowed_domain=get_domain(start_url).lower().split('/')[0]
    file.write('scrapy crawl multi_spider -a url=\''+start_url+'\' -a domain=\''+allowed_domain+'\' -O .\\files2\\'+''.join(company_name.split())+'.csv --nolog\n')

file.close()

