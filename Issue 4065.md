# Issue 4065: plot3d takes "forever" to plot x^2*y

Issue created by migration from https://trac.sagemath.org/ticket/4065

Original creator: jwmerrill

Original creation time: 2008-09-05 01:20:27

Assignee: was

CC:  jason


```
sage: var('y')
sage: plot3d(x^2*y,(-1,1),(-1,1))
```


This takes for ever, even when run as the first command after restarting a notebook.  On the other hand, it takes about 1 second to do


```
sage: var('y')
sage: plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))
```



---

Comment by mhansen created at 2008-09-05 16:42:43

What version of Sage are you running?


---

Comment by jwmerrill created at 2008-09-05 17:03:23

3.1.2.alpha2


---

Comment by mabshoff created at 2008-09-09 04:56:18

Yep, this computation still calls Maxima. Any idea why _fast_float is not used?

Cheers,

Michael


---

Comment by mhansen created at 2008-09-09 05:07:30

I can't duplicate this on 3.1.2.rc0.


---

Comment by mhansen created at 2008-09-09 05:08:10

On bsd


```
sage: var('y')
y
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.16 s, sys: 0.08 s, total: 0.24 s
Wall time: 0.78 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.14 s, sys: 0.06 s, total: 0.21 s
Wall time: 0.44 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.15 s, sys: 0.07 s, total: 0.22 s
Wall time: 0.48 s
```



---

Comment by mabshoff created at 2008-09-09 05:21:14

This is very strange to say the least:

```
sage: time p=plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))
CPU times: user 0.34 s, sys: 0.08 s, total: 0.42 s
Wall time: 3.07 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.16 s, sys: 0.06 s, total: 0.22 s
Wall time: 1.61 s
```

I must have started an old Sage. If someone can reproduce this with Sage 3.1.2.rc0 or later please give detailed information how to reproduce this. Fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-09 05:21:14

Resolution: fixed


---

Comment by jwmerrill created at 2008-09-09 20:04:37

Resolution changed from fixed to 


---

Comment by jwmerrill created at 2008-09-09 20:04:37

I just reproduced this problem on a freshly built 3.1.2.rc1, on OS X 10.5.4 intel macbook.  All I did was start sage in the terminal:


```
sage: version()
'SAGE Version 3.1.2.rc1, Release Date: 2008-09-08'
sage: var('y')
y
sage: plot3d(x^2*y,(-1,1),(-1,1))
```


This is still going 5 minutes later.  There is a process called lisp.run eating up about 90% of my processor power, with memory usage steady around 17 MB.  The same thing happens in the notebook.  Pressinc ctrl-c gives


```
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
```


Which also seems to persist indefinitely.  I eventually killed things by closing the terminal window.

Here's something else that takes virtually no time to run:


```
sage: plot3d(x^2*y,(x,-1,1),(y,-1,1))
```


But these commands also run indefinitely


```
sage: plot3d(x + y,(-1,1),(-1,1))
sage: plot3d(y*x,(-1,1),(-1,1))
```



---

Comment by jwmerrill created at 2008-09-09 20:04:37

Changing status from closed to reopened.


---

Comment by jwmerrill created at 2008-09-09 20:58:54

Changing assignee from was to jwmerrill.


---

Comment by jwmerrill created at 2008-09-09 20:58:54

Changing status from reopened to new.


---

Comment by mabshoff created at 2008-10-31 19:30:10

Resolution: invalid


---

Comment by mabshoff created at 2008-10-31 19:30:10

The problem here is likely a clisp linked against either the system or a MacPorts/Fink libpng.dylib. Various people have attempted to reproduce this problem and have failed. So I am closing it as invalid since one can no longer build with MacPorts/Fink in $PATH.

Cheers,

Michael
