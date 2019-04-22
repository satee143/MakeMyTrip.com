import datetime
import random
URL='http://makemytrip.com'
FROM='Delhi'
TO='Bangalore'



now=datetime.datetime.now()
nexday=now+datetime.timedelta(days=3)
fromdate=nexday.strftime('%a %b %d %Y')
tddate=nexday+datetime.timedelta(days=7)
todate=tddate.strftime('%a %b %d %Y')
rand=random.randint(1,10)
rand1=random.randint(1,10)

#def Price_Conversion(value):
