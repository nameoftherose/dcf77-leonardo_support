This directory contains log files from the leonardo dcf77 library.

- minicom.log:
>leonardo being fed by dcf77-generator running on UNO.

The remaining logs were produced by leonardo connected to the Conrad module.

- dcf.zip: 
>The signal is dominated by noise produced by computers in the room and their power supplies. The signal is useless.  
When the leonardo is connected to a tablet running from batteries the signal is much cleaner.  
During nighttime the signal is quite clear, but battery run out before synchronization was achieved. The log was lost. During the same night the Eurochron clock achieved synchronization.
- dcf2017-04-29-07.zip:
>2 hour log, clean signal, dirty state achieved, minutes and seconds were correct. 
- dcf2017-04-29-11.zip
> 3 hour log, relatively clean signal, remained in useless state, eeprom cleared. At a certain stage all fields apart from year were correct, but deteriorated.
- dcf2017-04-29-14.zip
> 5 hour log. sync achieved at around 22:00 o'clock with the tablet on battery. Around this time signal was very clean and the Eurochron clock syncronized too.
- dcfdcf2017-04-29-22.zip
> Continuation of previous log. Tablet on powersupply from 29Z20:41:18 to 30Z05:11:06.
- dcf_20170503T210938Z.zip
> 9 hour log starting with reset. Night time no synchronization
- dcf_20170504T060939Z.zip
> 15 hour log, no synchronizatio, eurochron clock synchronized.
-  	dcf_20170504T210939Z.zip
> 9 hour log, night time, dirty status for some minutes, eurochron synchronized for about 7 hours
- dcf_20170505T060939Z.zip
> 24 hour log, dirty status for some minutes during night time, eurochron synchronized
- dcf_20170819T183813.zip
> 12 hour log synced for almost 2 hours then drowned in noise  
> 2017-08-19 20:38:13	Start of Log	  
> 2017-08-19 21:04:43	synced	    00:26   
> 2017-08-19 21:12:43	locked	    00:08  
> 2017-08-19 21:15:33	free	      00:02   
> 2017-08-19 21:54:43	synced	    00:39  
> 2017-08-19 23:50:15	lasy synced 01:55  
> then restatrt without synchronization due to power supply noise
- dcf_20170820T195715Z.zip
> 2017-08-20 21:57:15 CEST Start of Log  
> 2017-08-23 07:44:00 CEST End of Log  
> Tablet alternatively on battery and power outlet  
> Performance significantly better when on battery 

State   |Count  |  %   |
--------|-------|------|
useless	|   584	|  0.3%|
dirty	  |   107	|  0.1%|
synced	| 49195	| 23.7%|
free	  | 23576	| 11.3%|
locked	| 43153	| 20.7%|
unlocked|	91392	| 43.9%|
total	  |208007	|100.0%|

- dcf_2017-09-07_2158.zip  

State   |Count   |Duration |  %   |  
--------|--------|---------|------|  
useless	|    466 |  0:07:46|  0.1%|  
dirty	  |    896 |  0:14:56|  0.1%|  
synced	|267,727 | 74:22:07| 41.8%|  
free	  | 33,677 |  9:21:17|  5.3%|  
locked	| 49,614 | 13:46:54|  7.7%|  
unlocked|288,105 | 80:01:45| 45.0%|  
total	  |640,485 |177:54:45|100.0%|  

![phase lock accuracy](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master/logfiles/phaselock.png)  
![prediction match accuracy](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master/logfiles/predictionmatch.png)
