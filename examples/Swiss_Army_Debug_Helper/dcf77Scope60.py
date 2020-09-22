#
# Displays 60 seconds of Swiss_Army_Debug_Helper mode m output in realtime
# Needs timestamps in the log file, either from the Decoded time line,
#  or minicom style timestamps
# Run as follows
# tail -f putty.log |TZ=Europe/Berlin python -u dcf77Scope60.py 2>c.txt
from time import sleep
import curses
import re
# https://github.com/smre/DCF77/blob/master/DCF77.py
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import math
import signal
import sys

# Signal timezone (Default is Europe/Berlin UTC+1)
signal_timezone = 'Europe/Berlin'


# Convert int to DCF77 compatible binary string
def to_binary(value, size):
    binary_value = '{0:b}'.format(int(value))
    return binary_value[::-1] + ('0' * (size - len(binary_value)))


# Convert int to BCD
def bcd(value, size):
    if size <= 4:
        return to_binary(value, size)
    else:
        ones = to_binary(math.floor(value % 10), 4)
        tens = to_binary(math.floor(value / 10), size - 4)
        return ones + tens


# Calculate even parity bit
def even_parity(value):
    return str(value.count('1') % 2)


# Is it DST?
def is_dst(tzone):
    tz = pytz.timezone(tzone)
    now = pytz.utc.localize(datetime.utcnow())
    return now.astimezone(tz).dst() != timedelta(0)


# Add n minutes to time
def add_minutes(time, minutes):
    return time + timedelta(minutes=minutes)


# Generate one minute string
def generate_minute(time):
    global signal_timezone

    # first 17 "useless" bits
    minute = '0'+ 'X'* 14 +'0'*2

    # DST data
    minute += str(int(is_dst(signal_timezone)))
    minute += str(int(not is_dst(signal_timezone)))

    # start time code
    minute += '01'

    # minutes + parity bit
    minute += bcd(time.minute, 7)
    minute += even_parity(bcd(time.minute, 7))

    # hours + parity bit
    minute += bcd(time.hour, 6)
    minute += even_parity(bcd(time.hour, 6))

    # day of month
    minute += bcd(time.day, 6)

    # day of week
    minute += bcd(time.weekday() + 1, 3)

    # month number
    minute += bcd(time.month, 5)

    # year (within century) + parity bit for all date bits
    minute += bcd(time.year - 2000, 8)
    minute += even_parity(bcd(time.day, 6) + bcd(time.weekday() + 1, 3) + bcd(time.month, 5) + bcd(time.year - 2000, 8))

    # special "59th" second (no amplitude modulation)
    minute += '-'

    return minute


# Generate 11 minutes of DCF77 signal
def generate_bits(n):
    global signal_timezone
    bits = ''

    # Get signal timezone time
    zero_date = pytz.utc.localize(datetime.utcnow())
    signal_tz = timezone(signal_timezone)
    time = zero_date.astimezone(signal_tz)

    for i in range(1, n+1):
        bits += generate_minute(add_minutes(time, i))

    return bits

txt=[' 0 ']+[' X ']*14+['ATO','TZC','CES','CET','LSA','SET','M01','M02','M04','M08','M10','M20','M40',
        'MP1','H01','H02','H04','H08','H10','H20','HP2','D01','D02','D04','D08','D10','D20','WD1','WD2',
        'WD4','M01','M02','M04','M08','M10','Y01','Y02','Y04','Y08','Y10','Y20','Y40','Y80','DP3','MSM']
def main(w):
    height,width=w.getmaxyx()
   #print >>sys.stderr,height,width
    try:assert height >=60 and width >=150
    except:
        w.addstr(0,0,      'screen size: (%dx%d). Should be at least (60x150)'%(height,width))
        w.refresh()
        sleep(10)
       #print >>sys.stderr,'screen size: (%dx%d). Should be at least (60x150)'%(height,width)
       #sys.stderr.flush()
        return
   #f=readlines_then_tail(open('putty.log'))
    t=None;ts='';t0=datetime.now().replace(second=0,microsecond=0)
    timestampRE=re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\.\d{3})?\] ');timestamp=None
    d=re.compile('Decoded time:')
    s=re.compile('^\s+[0-9]+, ')
    csRE=re.compile('Clock state: ');clockstate=None
    triples=re.compile(r'\s+........\(.,.\)..:..:\d{2,3} MES{0,1}Z \d,\d (\d+) (p\(\d+-\d+\:\d+\)).+ \d+,\d+,\d+,(\d+)')
    tripleSummary=''
    seq=None
    counter = 0;staleCounter=0
    while True:
        l=sys.stdin.readline().rstrip();staleCounter+=1 ;#print >>sys.stderr,l
        if timestampRE.match(l):
           timestamp=l[1:20]
           l=l[l.index(']')+2:]
          #print >>sys.stderr,'Timestamp',timestamp;sys.stderr.flush()
        else:timestamp=None
          #print >>sys.stderr,timestamp,l
        if d.match(l):
          #print >>sys.stderr,'Decoded time';sys.stderr.flush()
           try:
              ts=l[14:22]+l[24:33]
              t=datetime.strptime(ts,'%y-%m-%d %H:%M:%S')+timedelta(seconds=-1)
              staleCounter=0
           except ValueError: t = None;ts=''
       #print >>sys.stderr,'line 172';sys.stderr.flush()
        if (t is None or staleCounter > 10) and timestamp is not None :
           ts=timestamp[2:]
          #print >>sys.stderr,'No Decoded Time',ts,timestamp;sys.stderr.flush()
           try:
               t=datetime.strptime(ts,'%y-%m-%d %H:%M:%S')+timedelta(seconds=-1)
           except ValueError: t = None;ts='';#print >>sys.stderr,'line 177 exception';sys.stderr.flush()
       #print >>sys.stderr,'line 179',t is None,t0 is None,t<t0 if t is not None else '',t0,t if t is not None else '' #, t<t0;sys.stderr.flush()
        if t is None or t<t0: continue
        if csRE.match(l):clockstate=l[13:]
        tripleObject=triples.match(l)
        if tripleObject:
           tripleSummary = '%-2s %-18s %-3s'%tripleObject.groups()
       #print >>sys.stderr,'line 185',tripleSummary;sys.stderr.flush()
        if s.match(l) and t is not None:
           ln=t.second
           if ln == 0 or seq is None:
               seq=generate_minute(t+timedelta(seconds=60))
              #w.refresh()
              #sleep(60);
           w.addstr(ln,0,t.strftime('%H:%M:%S')+' '+txt[ln]+' '+seq[ln]+'%-104s'%l[10:]+' '+'%-8s'%clockstate+' '+tripleSummary)
           try:
             max_index=int(l[10:].split(' ')[2])
             delta=20 if seq[ln]=='1' else 10 if seq[ln]=='0' else 1
             w.addstr(ln,15+max_index,l[11:][max_index:min(100,max_index+delta)],curses.A_REVERSE)
             if max_index+delta>99:
                w.addstr(ln,15+0,l[11:][:(max_index+delta)%100],curses.A_REVERSE)
           except IndexError:pass
           w.refresh()
          # print >>sys.stderr,counter,t,datetime(2020,8,21,0,0,0),t<datetime(2020,8,21,0,0,0);sys.stderr.flush()
           counter += 1
          #if counter > 180: break
           sleep(.1)
           t=None;ts='';clockstate='';tripleSummary = '%-2s %-18s %-2s'%('','','')
    sleep(60)
#main(0)
try:
   curses.wrapper(main)
   pass
except KeyboardInterrupt:pass
