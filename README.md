# dcf77 library
## Branch-1 
This is an attempt to deal with the fading signal issues, whether successful or not yet unknown

This is **a copy of the dcf77-leonardo-support branch** of [Udo Klein's Noise resilent DCF77 decoder library for Arduino ](https://github.com/udoklein/dcf77). This branch was deleted/merged to the master branch by its author before I had the time to create a proper fork, so I had to create this repository from the zip file I had. Here is the original [README](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master/README_original.md)

As it now stands this repository documents an effort to use the library with the Conrad module in a residential area in central Crete. So far the only changes in the sources are in [Swiss_Army_Debug_Helper](https://github.com/nameoftherose/dcf77-leonardo_support/tree/master/examples/Swiss_Army_Debug_Helper). The [logfiles](https://github.com/nameoftherose/dcf77-leonardo_support/tree/master/logfiles) directory contains logs produced by Swiss_Army_Debug_Helper over the testing period.
This effort was very frustrating and so far basically unssucceful. This is not due to a library deficiency but due to:
- the great periods of time that the signal disappears,
- the noise coming through the USB power supply lines  
- the small antenna of the Conrand module, just 50mm.
- the long testing times (nightime actually as the signal appears during night) necessary to evaluate performance. 

The logs are further discussed in [logfiles README](https://github.com/nameoftherose/dcf77-leonardo_support/blob/master/logfiles/README.md).

The library was originally tested on **Arduino leonardo**, which, at the time, was unsupported, support for it was kindly added by Udo Klein to help me. The **leonardo** was destroyed during the experiment, an **UNO on breadboard with crystal** was then assembled and used.

From the very beginning, the Clock performed much better when fed from battery or from a tablet  running on battery. The logs from this period are discontinuous and not reliable. Only after the power supply filtering was added, it became possible to have successful operation while connected to a desktop PC. The resulting logs document the large periods of signal fading.

Even so problems remain:
- When the Clock starts at the beginning of a long period of signal fading it will not sync, has to be reset.
- Long periods of signal fading may cause large delays in resynchronization. Even worse the Clock may decode the _wrong time_.

The overall conclusion is that even with this extra resilient library, the Conrad module with its small antena should not be used in this location. Other experiments in Greece report that the situation improved greatly with larger (100mm) antennas.

It should be added that two commercial clocks in the same location, running on batteries, also have large periods of non-synchronization. 
## Remarks / Advice
- Buy the best device you can afford.
- If you can not find a long antenna, abandon the project
- Get yourself a DCF clock that displays time of last sync, note the periods of signal availability and perform your experiments during these periods.
- USB power supplies have a lot of noise, the receiver modules are susceptible to that noise. [Filter the power supply](http://andybrown.me.uk/2015/07/24/usb-filtering/) as best as you can. In the initial phase of the experiment feed your arduino/receiver from batteries.
- Even if you finally succeed with a short antenna, it is going to be frustrating.
