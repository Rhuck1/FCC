def add_time(start, duration, starting_dow=None):
    
    # AM --> PM, need full 24hrs bf next day is signaled
    # PM --> AM, only need difference in hrs bf next day is signalled
    
    time_pieces = start.split()
    initial = time_pieces[0].split(':')
    period = time_pieces[1]
    hr_initial  = initial[0]
    min_initial = initial[1]
    duration = duration.split(':')
    hr_duration = duration[0]
    min_duration = duration[1]
    

    minutes = int(min_initial) + int(min_duration)
    final_hr = int(hr_initial) + int(hr_duration) + 0
    
    period_selection = {0: "AM", 1: "PM"}
    
    # Need a 24 hr counter
    days = hr_dur // 24
    days += final_hr // 24
    
    # Need a 12 hr counter
    half_day = final_hr // 12
    
#     # While dow greater than 7 continue to modulo by 7 
#     while days > 8:
#     if days > 8:
#         day = 0
#         dow = dow % 7
#     dow = days % 7 # or multple floor divisions by 7 until zero reached?? or remainder %



    return minutes, final_hr, days, half_day


add_time("5:00 PM", "3:10")