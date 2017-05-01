import serial
import datetime
help_string = '''
  D: debug modes                                                                                                                                             
    q: quiet                                                                                                                                                 
    d: debug quality factors                                                                                                                                 
    s: scope                                                                                                                                                 
    S: scope high resolution                                                                                                                                 
    m: multi mode debug + scope                                                                                                                              
    a: analyze frequency                                                                                                                                     
    A: Analyze phase drift, more details                                                                                                                     
    b: demodulator bins                                                                                                                                      
    B: detailed demodulator bins                                                                                                                             
    r: raw output                                                                                                                                            
    c: CET/CEST                                                                                                                                              
    u: UTC                                                                                                                                                   
  *: persist current modes to EEPROM                                                                                                                         
  ~: restore modes from EEPROM
'''
f=open('dcf.txt','a')
s=serial.Serial('/dev/ttyACM0',115200)
s.write('D')
s.write('m')
while True:
 try:
   l=s.readline()
   n=datetime.datetime.utcnow()
   print format(n,'%Y-%m-%d %H:%M:%S'),l,
   print >>f,format(n,'%Y-%m-%d %H:%M:%S'),l,
   f.flush()
 except KeyboardInterrupt:
   c=raw_input(help_string)
   if c == 'Quit': break
   s.write(c)
   

