import requests
#import selenium
from bs4 import BeautifulSoup
import webbrowser
 

def main():



    MPM = r'MPM012390529'
    issueCatgory = 'Swiper'
    issueDescription = "This is a test"


    signInurl = 'https://www.mycryptopay.com/devel/genesys/'
    RMAurl = 'https://www.mycryptopay.com/devel/genesys/index.php?page=newticket&siteid=' + MPM
    loginInfo = {'username': 'config.username',
               'password': 'config.password',
               'submit_login': ''}
    createNewTicket = {'siteid': MPM,
                       'catagory': issueCatgory,
                       'category': 'NR |',
                       'description': issueDescription,
                       'submit_newticket': ''}




    '''
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")
    #print(soup.select('input[name]'))
    '''
    #print(buttonPress)

    s = requests.Session()
    # all cookies received will be stored in the session object

    r = s.get(signInurl)
    print(r.content)
    r = s.post(signInurl, data=loginInfo)
    print(r.content)
    s.get(RMAurl)
    r = s.post(RMAurl, data=createNewTicket)
    print(r.content)



    print(r.history)
    print(r.cookies)
    print(r.url)


main()



















'''
    #url = 'https://www.mycryptopay.com/devel/genesys/index.php?page=customer&siteid=' + MPM
    o = requests.post(r.url, data=siteMPM)
    print(o.content)
    print(o.url)

    print(r.history)
    
    print("\n\n\n\n")


    if r.history:
        print("Request was redirected")
        for resp in r.history:
            print(resp.status_code, resp.url)
        print("Final destination:")
        print(r.status_code, r.url)
    else:
        print("Request was not redirected")
    

    r = requests.post(url, data=siteMPM)
'''



