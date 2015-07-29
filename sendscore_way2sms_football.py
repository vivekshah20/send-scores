from lxml import html
import requests
import time
import urllib2, sys
import cookielib


def sendscore(body):
    #Login Details
    username = "" #Way2SMS Username
    passwd = "" #Way2SMS Password
    
    #Recipient's Number and Message
    message = body
    number = ""

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
    page=requests.get('http://www.sportsmole.co.uk/football/arsenal/live-commentary/live-commentary-chelsea-vs-arsenal_180857.html')
    tree=html.fromstring(page.text)

    team_name_home=tree.xpath('//div[@class="game_header_bar_team left"]/text()')
    team_name_home=[x.strip() for x in team_name_home]

    team_name_away=tree.xpath('//div[@class="game_header_bar_team"]/text()')
    team_name_away= [x.strip() for x in team_name_away]

    team_score=tree.xpath('//div[@class="game_header_score"]/text()')
    team_score=[x.strip() for x in team_score]

    match_news=tree.xpath('//div[@id="period"]/text()')
    match_news=[x.strip() for x in match_news]

    goals=tree.xpath('//div[@class="game_header_goals left"]//text()')
    goals =[x.strip() for x in goals]
    print goals
    print match_news
    print team_name_home[0]," v/s ", team_name_away[0],"  ",team_score[0]
    #score = team_name[6]+" "+team_score[6]
    sendscore(score)
    print "%s sent at:%s "%(score,time.ctime())
    time.sleep(60)