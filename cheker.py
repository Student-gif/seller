from requests import get, head, post
from bs4 import BeautifulSoup


ports_url = 'http://spys.one/proxy-port/'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0" }

soup = BeautifulSoup(post(ports_url, headers=headers, data={'xpp': 5}).content, 'html.parser')
for f in soup.select('td[colspan="2"] > a > font.spy6'):
    u = 'http://spys.one/proxy-port/' + f.text + '/'
    s = BeautifulSoup(post(u, headers=headers, data={'xpp': 5}).content, 'html.parser')
    for ff in s.select('tr > td:nth-child(1) > font.spy14'):
        print(ff.text)

class cheker:

    
    def proxyScraper():
        #make object bs 
        soup = BeautifulSoup(post(ports_url, headers=headers, data={'xpp': 5}).content, 'html.parser')

        for f in soup.select('td[colspan="2"] > a > font.spy6'):
            u = 'http://spys.one/proxy-port/' + f.text + '/'
            s = BeautifulSoup(post(u, headers=headers, data={'xpp': 5}).content, 'html.parser')
            for ff in s.select('tr > td:nth-child(1) > font.spy14'):
                print(ff.text)
        #return get("http://free-proxy.cz/ru/proxylist/main/2",).content
        
        
    def NordVpnCheker():
        #узнать как узнать билнг на акке
        return post("https://ucp.nordvpn.com/api/v1/users/login",data={'username':"970adityadas@gmail.com","password":"7099390154"}).text
        post("https://my.nordaccount.com/billing/billing-history/", )
        
    def WinnscribeCheker():
        return post('https://res.windscribe.com/res/logintoken').text        
cheker.proxyCheker()         
