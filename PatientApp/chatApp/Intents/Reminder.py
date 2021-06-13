def Remind_Handler(params):

    mssg = "Remind"

    if(params.get('Honorifics')):
        mssg = mssg + " " + params.get('Honorifics')
    
    if(params.get('person')):
        name = params.get('person')['name']
        mssg =mssg + " " + name

    if(params.get('actions')):
        mssg = mssg + " to " + params.get('actions')

    if(params.get('any')):
        mssg = mssg + " " + params.get('any')

    if(params.get('triggers')):
        mssg = mssg + " " + params.get('triggers')
    
    if(params.get('time')):
        time = params.get('time').split('T') 
        t = time[1].split('+')
        mssg = mssg + " at " + str(t[0])
    
    if(params.get('date-slot')):
        mssg = mssg + " from " + params.get('date-slot')
    
    if(params.get('date')):
        date = params.get('date').split('T')
        mssg = mssg + " on "+ date[0]

    return mssg