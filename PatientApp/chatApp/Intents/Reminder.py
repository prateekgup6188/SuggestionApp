def format_date(date):
    formatted_date = date.split('-')
    formatted_date.reverse()
    new_date = ('-').join(formatted_date)
    return new_date

def Remind_Handler(params):

    mssg = "Set a reminder"

    if(params.get('actions')):
        mssg = mssg + " to " + params.get('actions')

    if(params.get('any')):
        mssg = mssg + " " + params.get('any')

    if(params.get('triggers')):
        mssg = mssg + " " + params.get('triggers')
    
    if(params.get('date-time')):
        date_time_obj = params.get('date-time')
        if(type(date_time_obj) == str):
            date = format_date(date_time_obj.split('T')[0])
            mssg = mssg + " on " + date
            print(date)

        elif(type(date_time_obj) == dict):
            if(date_time_obj.get('date_time')):
                date = format_date(date_time_obj['date_time'].split('T')[0])
                time = date_time_obj['date_time'].split('T')[1]
                time = time.split('+')[0]
                mssg = mssg + " at " + time + " on " + date
                print(date,time) 

            elif(date_time_obj.get('startDate') and date_time_obj.get('endDate')):
                startDate = format_date(date_time_obj.get('startDate').split('T')[0])
                endDate = format_date(date_time_obj.get('endDate').split('T')[0])
                mssg = mssg + " between " + startDate + " and " + endDate 
                print(startDate,endDate)

    return mssg