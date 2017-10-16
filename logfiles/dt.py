import gzip
import datetime
#F=gzip.open('dcf.log.gz')
offset=datetime.timedelta(hours=0)
F=open('dcf.log')
for l in F:
     if 'Decoded' in l :
        f=l.split()
        try:
          t0=datetime.datetime.strptime(f[0]+' '+f[1],'[%Y-%m-%d %H:%M:%S.%f]')+offset
          t1=datetime.datetime.strptime('20'+f[4]+' '+f[6],'%Y-%m-%d %H:%M:%S')
        except ValueError:
          print l,
          continue
        dt = abs( (t1-t0).total_seconds())
        if dt > 1:
           print t0,t1
