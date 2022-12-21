# Issue 3585: time_series -- lots of numerical noise in the doctests

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 15:24:47

Assignee: tbd

On Debian 32-bit Vmware intel

```
sage -t  devel/sage/sage/finance/time_series.pyx            **********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 571:
    sage: v.autoregressive_forecast(F)
Expected:
    11.782029861181114
Got:
    11.782029861181117
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1278:
    sage: v.autocovariance(0)
Expected:
    24.954106897195892
Got:
    24.954106897196283
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1280:
    sage: v.autocovariance(1)
Expected:
    -0.0050839047886276651
Got:
    -0.0050839047886275012
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1282:
    sage: v.autocovariance(2)
Expected:
    0.022056325329509487
Got:
    0.022056325329509536
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1284:
    sage: v.autocovariance(3)
Expected:
    -0.019020003743134766
Got:
    -0.019020003743134842
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1308:
    sage: v.correlation(w)
Expected:
    -0.55804160922502144
Got:
    -0.55804160922502155
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1310:
    sage: v.covariance(w)/(v.standard_deviation() * w.standard_deviation())
Expected:
    -0.55804160922502144
Got:
    -0.55804160922502155
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1419:
    sage: set_random_seed(0); finance.TimeSeries(10^6).randomize('normal').sums().range_statistic()
Expected:
    1873.9206979719115
Got:
    1873.9206979719406
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1421:
    sage: set_random_seed(0); finance.TimeSeries(10^6).randomize('normal',0,100).sums().range_statistic()
Expected:
    1873.920697971955
Got:
    1873.9206979719447
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1445:
    sage: bm.hurst_exponent()
Expected:
    0.5174890556918027
Got:
    0.51748905569180337
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1453:
    sage: fbm.hurst_exponent()
Expected:
    0.667870279214...
Got:
    0.66787027921789599
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1848:
    sage: v.randomize('uniform').mean()
Expected:
    0.50069085504319877
Got:
    0.50069085504316591
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1881:
    sage: v.randomize('normal').mean()
Expected:
    6.2705472723385207e-05
Got:
    6.2705472723392213e-05
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1888:
    sage: v.randomize('normal', 2, 5).mean()
Expected:
    2.0003135273636117
Got:
    2.000313527363617
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1930:
    sage: v.randomize('semicircle').mean()
Expected:
    0.00072074971804614557
Got:
    0.00072074971804620411
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1936:
    sage: v.randomize('semicircle', 2).mean()
Expected:
    2.0007207497179227
Got:
    2.0007207497180461
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/time_series.py", line 1974:
    sage: v.randomize('lognormal').mean()
Expected:
    1.6473519736548801
Got:
    1.6473519736548257
**********************************************************************
9 items had failures:
   1 of   6 in __main__.example_16
   4 of  14 in __main__.example_40
   2 of   4 in __main__.example_41
   2 of   3 in __main__.example_45
   2 of   9 in __main__.example_46
   1 of   7 in __main__.example_54
   2 of  10 in __main__.example_55
   2 of  10 in __main__.example_56
   1 of  12 in __main__.example_57
***Test Failed*** 17 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_time_series.py
         [9.0 s]
sage -t  devel/sage/sage/finance/markov_multifractal.py

```



---

Attachment


---

Comment by craigcitro created at 2008-07-07 18:48:59

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-07-07 18:48:59

Changing assignee from tbd to craigcitro.


---

Comment by craigcitro created at 2008-07-07 18:48:59

Added `...` a lot to make doctests reasonable.


---

Comment by was created at 2008-07-07 20:17:11

It works and all doctests pass on the machine in question.  Plus Robertwb looked it over.


---

Comment by was created at 2008-07-07 21:48:14

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 21:51:36

Merged in Sage 3.0.4.rc0
