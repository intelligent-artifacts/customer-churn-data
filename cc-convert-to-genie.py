from future__ import division
import os, sys
import string
import json

'''Convert the dataset to Genie digestible format.'''

#===============================================================================
# Columns:
# State,Account Length,Area Code,Phone,Int'l Plan,VMail Plan,
# VMail Message,Day Mins,Day Calls,Day Charge,Eve Mins,Eve Calls,Eve Charge,
# Night Mins,Night Calls,Night Charge,Intl Mins,Intl Calls,Intl Charge,CustServ Calls,Churn?
# Sample row:
# KS,128,415,382-4657,no,yes,25,265.100000,110,45.070000,197.400000,99,16.780000,244.700000,91,11.010000,10.000000,3,2.700000,1,False.
#===============================================================================

remaining_columns = ['State', 'Account Length', 'Area Code', "Intl Plan", 
                        'VMail Plan', 'VMail Message', 'Day Mins', 'Day Calls', 
                        'Day Charge', 'Eve Mins', 'Eve Calls', 'Eve Charge', 'Night Mins', 
                        'Night Calls', 'Night Charge', 'Intl Mins', 'Intl Calls', 'Intl Charge', 'CustServ Calls']

f = open(os.path.expanduser('~/Desktop/churn.csv'))
for line in f:
    line = line.rstrip()
    line = line.split(',')
#    line[4] = 'Intl_plan_%s' %(line[4])
#    line[5] = 'Vmail_plan_%s' %(line[5])
    utility = line.pop(-1)
    if utility == 'True.':
        utility = -100
    elif utility == 'False.':
        utility = 100
    else:
        print 'No utility?'
    print line
    continue
    
    area_code = line[2]
    phone = line.pop(3)
    s = []
    for index in range(len(remaining_columns)):
        s.append("%s|%s" %(remaining_columns[index], line[index]))
    data = {"scalars": [utility], "vectors": [], "strings": s}
    data = json.dumps(data)
    output = open(os.path.expanduser('~/Desktop/churn/%s' %(area_code + '-' + phone)), 'w')
    output.write(data + '\n')
    output.close()
f.close()
