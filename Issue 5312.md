# Issue 5312: command line -- bug in preparser and "time"

Issue created by migration from https://trac.sagemath.org/ticket/5312

Original creator: was

Original creation time: 2009-02-19 08:31:41

Assignee: cwitty

CC:  mjo

There is a weird interaction between time and preparser, almost as if input to time is being preparsed *twice*:


```
wstein@sage:~/build/sage-3.3.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: k = 3r
sage: type(k)
<type 'int'>
sage: time k = 3r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: type(k)
<type 'sage.rings.integer.Integer'>
sage: preparse('k = 3r')
'k = 3'
sage: preparse('time k = 3r')
'time k = 3'
```

| Sage Version 3.3.rc1, Release Date: 2009-02-16                     |
| Type notebook() for the GUI, and license() for information.        |
In the above, type(k) should have been int in all cases.  Why isn't it the second time.  WEIRD.


---

Comment by mjo created at 2012-01-09 02:17:26

This works now:


```
sage: k = 3r
sage: type(k)
<type 'int'>
sage: time k = 3r
Time: CPU 0.00 s, Wall: 0.00 s
sage: type(k)
<type 'int'>
```


Where's the best place to add a doctest?


---

Comment by mhansen created at 2013-07-23 12:21:53

Resolution: invalid


---

Comment by mhansen created at 2013-07-23 12:21:53

I think we can just mark it as invalid since "%time" is now handled by IPython.
