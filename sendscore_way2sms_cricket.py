from lxml import html
import requests
import time
import urllib2, sys
import cookielib


def sendscore(body):
    
    username = "" #Way2Sms username
    passwd = "" #Way2SMS password
    message = body
    number = "" #Recipient's Number

    message = "+".join(message.split(' '))

    #Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
    try:
        usock = opener.open(url, data)

    except IOError:
        print "Error while logging in."

        sys.exit(1)

    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)

    except IOError:
        print "Error while sending message"

    print "SMS has been sent."

while True:
    page=requests.get('http://sports.ndtv.com/cricket/live-scores')
    tree=html.fromstring(page.text)
    team_name=tree.xpath('//div[@class="ckt-nm"]/text()')
    team_name= [x.strip() for x in team_name]
    vs_name=tree.xpath('//span[@class="ckt-vs"]/text()')
    vs_name=[x.strip() for x in vs_name]
    team_score=tree.xpath('//div[@class="ckt-scr"]/text()')
    team_score=[x.strip() for x in team_score]
    team_result = tree.xpath('//div[@class="ckt-mtch-rslt"]/text()')
    print team_name[0],"  ",team_score[0]," ",vs_name[0]," ",team_name[1]," ",team_score[1]," ",team_result[0]   #add team_score when live matches are going on
    score = team_name[0]+" "+team_score[0]+"\n"+team_name[1]+" "+team_score[1]+"\n"+team_result[0].strip()  #add team_score when live matches are going on
    sendscore(score)
    
    print "%s sent at:%s "%(score,time.ctime())
    
    time.sleep(120)     #After 'n' seconds the site will be scrapped again to fetch new scores and message will be sent