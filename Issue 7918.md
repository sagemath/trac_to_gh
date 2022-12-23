# Issue 7918: log(float(_)) is really slow

Issue created by migration from https://trac.sagemath.org/ticket/7918

Original creator: bober

Original creation time: 2010-01-13 06:55:34

Assignee: tbd

CC:  mvngu

Keywords: log

Somewhere between 4.1 and 4.3, log(x) got really slow when x is a float.

Example:



```
sage: version()
'Sage Version 4.3, Release Date: 2009-12-24'
sage: x = float(5)
sage: x
5.0
sage: timeit('log(x)')
625 loops, best of 3: 362 µs per loop
```



```
sage: version()
'Sage Version 4.1, Release Date: 2009-07-09'
sage: x = float(5)
sage: timeit('log(x)')
625 loops, best of 3: 7.26 µs per loop
```





---

Comment by burcin created at 2010-01-13 09:14:52

Although it is not the same issue, this will be fixed by #7822. I have a new patch for that problem which brings the timings back to comparable values.


---

Comment by burcin created at 2010-02-19 11:59:26

Resolution: fixed


---

Comment by burcin created at 2010-02-19 11:59:26

I'm closing this since #7822 was merged and it addresses this issue.
