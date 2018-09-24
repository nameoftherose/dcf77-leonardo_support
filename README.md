# dcf77 library
## Branch-1 
This is an attempt to deal with the fading signal issue.
Following a 31 days continuous test,during which the Clock synchronized every night without a single occurence of synchronization to the wrong time, it is reasonable to conclude that the code of this branch deals satisfactory with the fading issue when used with the Conrad module in central Crete.
### 2017-10-15
The following changes were made:
-  .ino L724 A manual reset added ('t')
-  .h L1285 `static const uint8_t lock_threshold = 99/*12*/;` second's threshold increased from 12 to 99.  
These modifications are under test in the period 2017-10-15 ÷ 2017-10-22. They stop the decoder chain if the `Second_Decoder. quality` is less than 99.Results are encouraging. While in `useless` state no year 00 was observed. There was though a side effect: As the state transitions are governed by the `overall_quality_factor` (which is calculated from the individual `quality_factor`s and not from `quality`, there was a case where the clock remained in `synced` state while the decoder chain was stopped. As a result the clock was stopped and diplayed second 95.
### 2017-10-20
-  .ino L399 parser_mode = debug_output_command /* waiting*/;
-  .h L1344, L1354.. `dirty` transition threshold changed from `1` to `quality_factor_sync_threshold-1`
-  .h L1997 `get_overall_quality_factor()` returns 0 `if (Second_Decoder.quality < lock_threshold)`. It is hoped this will remove above  side effect.
-  .h L1998 `get_overall_quality_factor()` returns 0 `if (Year_Decoder.get_time_value().val<0x17)`. Transitions to `synced` and `dirty` should occur only  `if (decoded_time.year.val>=0x17)`.
-  .h L1433 In function `process_1_Hz_tick(...)` the code for the `free` state was modified to call `Clock_Controller::phase_lost_event_handler()` `if (decoded_time.year.val<0x17)`. This is provisionary, if successful, a more specific handler will be written, and the `locked` and `unlocked` states will be treated similarly. `(decoded_time.year.val<0x17)` should reset the decoders.
  
  These modifications were tested, were an imporovement but are not sufficient. The modification of `get_overall_quality_factor()` caused a transition from `synced` to `locked`, but the clock still stopped. The modification of function `process_1_Hz_tick(...)` was also unsuccessful because `decoded_time` is not the time estimated by the decoder chain.  
### 2017-10-26
  In Function `process_1_Hz_tick(...)` (dcf77.h L1331) code was added to
  -  reset `Year_Decoder`, `Month_Decoder`, `Day_Decoder` and `WeekDay_Decoder`  `if (Year_Decoder.get_time_value().val<0x17)`. 
  -  transition `locked` → `unlocked` is forced `if (Year_Decoder.get_time_value().val<0x17)`.
  -  transition `unlocked` → `locked` is executed only `if (Year_Decoder.get_time_value().val>=0x17)`.
  -  Debug variables `year_val`, `year_error_count` monitor the effects of these modifications. 
  
Function `DCF77_Local_Clock.setup()` (dcf77.h L1319) was modified to put the clock in `free` state on boot.

Function `DCF77_Encoder::reset()` (dcf77.cpp L736) was modified to set `local_clock_time` to the desired time. (This is not a good idea, a separate function should have been created.) 

  Function `DCF77_Clock_Controller.setup()` (dcf77.h L2156) was modified to call `Local_Clock.setup();`. (May be it was better to call it from the main application if the user wants to set the clock time to a specific time.)

In Swiss_Army_Debug_Helper.ino code was added to
  -  Print the values of the above debug variables.
  -  print the state when `free`. 
  
  These modifications are under test since 2017.10.26 18:06, with very encouraging results. During these 10 days no case of wrong date/time has occured. Clock has syncronized every night, it is in synced state for 36% of the time.
  ![a](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master-1/logfiles/qf_2017-10-26.png)
  Source code has been uploaded.  
  ### 2017-12-17
-  The modifications to initialize the Clock to the free state and a compile-time time stamp was removed, as it did not improve performance.
- The debug variables monitoring year error were moved from Swiss_Army_Debug_Helper.ino to dcf77.h L 1303, are now members of `struct DCF77_Local_Clock` 
- `static const int16_t max_total_adjust` (dcf77.h L1564) was redefined from 6400 to 1600 corresponding to 100ppm  
This version has been operating till August 2018. During these 8 months only two cases of error (in the hour field) have been observed and the algorithm self-corrected (Of course there may have been other errors that remainded unobserved).  
This version assumes that  the dcf77 module will default to zero signal when the signal fades, that is why the `if (decoded_time.year.val<0x17)` test has been so successful. But this behaviour, which applies to the Conrad module used, can not be expected of other modules.

### 2018-09-21
This version implements a week day inconsistency constraint
- `max_unlocked_seconds` initialized
- `get_overall_quality_factor()` modified to return 0 in case of weekday inconsistency
   and set the inconsistentWeekDay flag
-  hour decoder reset added (dcf77.h `process_1_Hz_tick` )
-  date and hour decoders reset when weekday inconsistency is detected
-  Swiss_Army_Debug_Helper `loop()` `scopeCount` calculation modified
- dcf77.h L1340 `year_error_count` calculation has been corrected
   `inconsistentWeekDayCounter` calculation added
- The weekday calculation in `get_overall_quality_factor()` is only done
           `if (date_quality_factor > 0 && weekday_quality_factor > 0)`
   This delays the inconsistency detection, should be done every time.  
   Code has been modified so that the calculation always takes place.  

This is under test since 2018-09-21. Test successful so far.  
Source code in [Swiss_Army_Debug_Helper_20180921.zip](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master-1/Swiss_Army_Debug_Helper_20180921.zip)
