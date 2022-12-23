# Issue 6788: 1 doctest timed out in devel/sage/sage/symbolic/assumptions.py

Issue created by migration from https://trac.sagemath.org/ticket/6788

Original creator: drkirkby

Original creation time: 2009-08-20 22:14:12

Assignee: tbd


```
sage -t  "devel/sage/sage/symbolic/assumptions.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [360.3 s]
```



---

Comment by AlexGhitza created at 2009-08-20 23:54:58

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-21 01:35:18

On the various machines I tried (no Solaris though!) I don't get a timeout but rather a doctest failure.  I'm attaching a patch fixing it.  David, is the timeout you get reproducible, or does it only happen sporadically?


---

Attachment

apply after spkg's at #6564 and #6699


---

Comment by kcrisman created at 2009-09-28 20:05:34

To release manager: Was this fixed elsewhere?


---

Comment by drkirkby created at 2009-10-08 09:34:53

This still fails for me, but what is worrying is how the CPU usage keeps climbing after the test failure. 

http://groups.google.com/group/sage-devel/browse_thread/thread/f5502f8489cc2b31

This is nothing to do with this particular test, but this test is an example of which shows that doctest failures are handled badly. 

Dave


---

Comment by AlexGhitza created at 2009-10-19 06:25:04

Changing component from algebra to packages.


---

Comment by AlexGhitza created at 2009-10-19 06:25:04

Changing assignee from tbd to mabshoff.


---

Comment by kcrisman created at 2009-12-24 03:34:06

To drkirkby - can you try this with the spkg for 5.20.1 in #7745?


---

Comment by drkirkby created at 2009-12-28 21:56:42

Hi, 
sorry for not replying earlier, but I did not see the request. The .spkg for Maxima 5.20.1 does fix this:


```
This does fix the problem. 


kirkby@t2:[~/sage-4.3] $ ./sage -t  "devel/sage/sage/symbolic/assumptions.py"
sage -t  "devel/sage/sage/symbolic/assumptions.py"          
         [60.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 60.8 seconds
```



---

Comment by mhansen created at 2010-03-19 23:16:18

Resolution: invalid
