# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(file_size, units, bandwith, bandwith_units):
    hour = 0
    minute = 0
    second = 0
    hour_word = ''
    minute_word = ''
    second_word = ''
    download_speed = 0
    
    
    download_speed_hour = 60 * 60
    download_speed_minute = 60
    
    kb_download_speed = 2 ** 10 
    kB_download_speed = 2 ** 10 * 8
    Mb_download_speed = 2 ** 20 
    MB_download_speed = 2 ** 20 * 8
    Gb_download_speed = 2 ** 30  
    GB_download_speed = 2 ** 30 * 8 
    Tb_download_speed = 2 ** 40 
    TB_download_speed = 2 ** 40 * 8  

    if bandwith_units == 'kb':
        download_speed = bandwith * kb_download_speed
        
    elif bandwith_units == 'kB':
        download_speed = bandwith * kB_download_speed
        
    elif bandwith_units == 'Mb':
        download_speed = bandwith * Mb_download_speed
        
    elif bandwith_units == 'MB':
        download_speed = bandwith * MB_download_speed
        
    elif bandwith_units == 'Gb':
        download_speed = bandwith * Gb_download_speed
        
    elif bandwith_units == 'GB':
        download_speed = bandwith * GB_download_speed
        print download_speed
        
    elif bandwith_units == 'Tb':
        download_speed = bandwith * Tb_download_speed
        
    elif bandwith_units == 'TB':
        download_speed = bandwith * TB_download_speed
        
        
    if units == 'kb':
        file_size = file_size * kb_download_speed
        
    elif units == 'kB':
        file_size = file_size * kB_download_speed
        
    elif units == 'Mb':
        file_size = file_size * Mb_download_speed
        
    elif units == 'MB':
        file_size = file_size * MB_download_speed
        
    elif units == 'Gb':
        file_size = file_size * Gb_download_speed
        
    elif units == 'GB':
        file_size = file_size * GB_download_speed
        print file_size
        
    elif units == 'Tb':
        file_size = file_size * Tb_download_speed
        
    elif units == 'TB':
        file_size = file_size * TB_download_speed
        
    while file_size != 0:
        print 'size', file_size
        print 'speed', download_speed
        if file_size >= download_speed * download_speed_hour:
            hour = hour + 1
            file_size = file_size - download_speed * download_speed_hour
        
        elif file_size >= download_speed * download_speed_minute:
            minute = minute + 1
            file_size = file_size - download_speed * download_speed_minute
        
        elif file_size >= download_speed:
            second = second + 1
            file_size = file_size - download_speed
            
        elif file_size != 0:
            second = float(second) + float(file_size)/download_speed
            
            file_size = 0
            
            
    if hour == 1:
        hour_word = 'hour'
    else:
        hour_word = 'hours'
        
    if minute == 1:
        minute_word = 'minute'
    else:
        minute_word = 'minutes'
    
    if second == 1:
        second_word = 'second'
    else:
        second_word = 'seconds'
    
    return str(hour) + ' ' + hour_word + ', ' + str(minute) + ' ' + minute_word + ', ' + str(second) + ' ' + second_word


#print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

#print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

#print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

#print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

#print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

#print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


