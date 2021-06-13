def Schedule_Handler(params):
    mssg = "Schedule "

    if(params.get('actions')):
        action = params.get("actions")
        if(action[0] in "aeiouAEIOU"):
            mssg  = mssg + "an " + action
        else:
                mssg = mssg + "a " + action

    if(params.get('actions') and params.get('actions')=="visit"):
        mssg = mssg + " to"

    elif(params.get("Honorifics") or params.get('any') or params.get('person')):
        mssg = mssg + " with"

    if(params.get('Honorifics')):
        mssg = mssg + " " + params.get('Honorifics') 

    if(params.get('any')):
        mssg = mssg + " " + params.get('any') 

    if(params.get('person')):
        name = params.get('person')['name']
        mssg =mssg + " " + name

    if(params.get('time')):
        time = params.get('time').split('T') 
        t = time[1].split('+')
        mssg = mssg + " at " + str(t[0])
    
    if(params.get('date-slot')):
        mssg = mssg + " for " + params.get('date-slot')
    
    if(params.get('date')):
        date = params.get('date').split('T')
        mssg = mssg + " on "+ date[0] 
    
    return mssg