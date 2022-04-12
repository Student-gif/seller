from requests import get, head, post


class cheker:
    def proxyCheker():
        heads = post("https://spys.one/en/http-proxy-list/").headers
        return get("https://spys.one/en/http-proxy-list/",headers=heads).content
    #def NordVpnCheker():
    #    #узнать как узнать билнг на акке
    #    return post("https://ucp.nordvpn.com/api/v1/users/login",data={'username':"970adityadas@gmail.com","password":"7099390154"}).text
    #    post("https://my.nordaccount.com/billing/billing-history/", )
    #def WinnscribeCheker():
    #    return post('https://res.windscribe.com/res/logintoken').text        
print(cheker.proxyCheker())         
