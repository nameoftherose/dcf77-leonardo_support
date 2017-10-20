# dcf77 library
## Branch-1 
This is an attempt to deal with the fading signal issues, whether successful or not yet unknown
### 2017-10-15
The following changes were made:
-  .ino L724 A manual reset added ('t')
-  .h L1285 `static const uint8_t lock_threshold = 99/*12*/;` second's threshold increased from 12 to 99.  
These modifications are under test in the period 2017-10-15 2017-10-22. They stop the decoder chain if the `Second_Decoder. quality` is less than 99.Results are encouraging. While in `useless` state no year 00 was observed. There was though a side effect: As the state transitions are governed by the `overall_quality_factor` (which is calculated from the individual `quality_factor`s and not from `quality`, there was a case where the clock remained in `synced` case while the decoder chain was stopped. As a result the clock was stopped and diplayed second 95.
### 2017-10-20
-  .ino L399 parser_mode = debug_output_command /* waiting*/;
-  .h L1997 `get_overall_quality_factor()` returns 0 if `Second_Decoder.quality < lock_threshold`
-  .h L1433 In function `process_1_Hz_tick(...)` the code for the `free` state was modified to call `Clock_Controller::phase_lost_event_handler()` `if (decoded_time.year.val<0x17)`  
  
  These modifications are not yet tested

