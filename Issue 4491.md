# Issue 4491: finance.TimeSeries from numpy array doesn't work correctly

Issue created by migration from Trac.

Original creator: ghtdak

Original creation time: 2008-11-11 03:31:26

Assignee: ghtdak

Looks like initializing a TimeSeries from a column of a numpy array doesn't work properly


```
testp.shape
```

(373389, 4)

```
t1=finance.TimeSeries(testp[:,3]); t1             # wrong
```


[962.5000, 1225742099742.0000, 4.0000, 4.0000, 962.5000 ... 999.2500,
1225850900622.0000, 4.0000, 5.0000, 999.2500]

```
t1=finance.TimeSeries(testp[:,3].tolist()); t1     # correct
```

[962.5000, 962.5000, 962.5000, 962.5000, 962.5000 ... 954.5000,
954.5000, 954.5000, 954.5000, 954.5000]


---

Comment by mabshoff created at 2008-11-11 04:32:14

Welcome back :)

Cheers,

Michael


---

Comment by jason created at 2008-11-11 09:41:12

This might be affected by #4206.


---

Comment by was created at 2008-11-11 20:04:31

> `t1=finance.TimeSeries(testp[:,3]); t1`

I probably never implemented such initialization when the numpy array doesn't have trivial stride.  This is certainly a valid bug; fixing it should be a high priority.


---

Comment by jason created at 2008-11-22 17:52:23

Changing status from new to assigned.


---

Comment by jason created at 2008-11-22 17:52:23

Changing assignee from ghtdak to jason.


---

Comment by jason created at 2008-11-22 17:52:23

I'm looking at this as part of the RDF/CDF vector rewrite.


---

Comment by jason created at 2008-11-22 21:05:35

Okay, this will taken care of as part of the vector RDF/CDF rewrite (since that already touched the relevant parts of the timeseries code).  Timing results for the case that worked before (simple double numpy arrays) indicate a 3x slowdown.  The new code should work for any numpy datatype (the current code does not) and any sort of numpy array.

before patch:

```
sage: import numpy as np
sage: a=np.array(range(1e2), dtype='double')
sage: %timeit b=finance.TimeSeries(a)
100000 loops, best of 3: 2.13 µs per loop
sage: a=np.array(range(1e3), dtype='double')
sage: %timeit b=finance.TimeSeries(a)
100000 loops, best of 3: 3.51 µs per loop
sage: a=np.array(range(1e4), dtype='double')
sage: %timeit b=finance.TimeSeries(a)
10000 loops, best of 3: 21.6 µs per loop
sage: a=np.array(range(1e5), dtype='double')
sage: %timeit b=finance.TimeSeries(a)
100 loops, best of 3: 1.85 ms per loop
sage: a=np.array(range(1e6), dtype='double')
sage: %timeit b=finance.TimeSeries(a)
10 loops, best of 3: 18.5 ms per loop
sage: a=np.array(range(1e7), dtype='double')
sage: %timeit b=finance.TimeSeries(a)double')
10 loops, best of 3: 189 ms per loop
```


after patch:


```
sage: sage: import numpy as np
sage: sage: a=np.array(range(1e2), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
100000 loops, best of 3: 5.77 µs per loop
sage: sage: a=np.array(range(1e3), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
100000 loops, best of 3: 8.74 µs per loop
sage: sage: a=np.array(range(1e4), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
10000 loops, best of 3: 52.3 µs per loop
sage: sage: a=np.array(range(1e5), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
100 loops, best of 3: 3.83 ms per loop
sage: sage: a=np.array(range(1e6), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
10 loops, best of 3: 36.3 ms per loop
sage: sage: a=np.array(range(1e7), dtype='double')
sage: sage: %timeit b=finance.TimeSeries(a)
10 loops, best of 3: 365 ms per loop
```



---

Comment by jason created at 2008-11-24 22:03:36

This is solved in #4206


---

Comment by mabshoff created at 2008-12-09 09:09:54

Since there is a doctest in #4206

```
[01:04am] mabshoff: I haven't checked, but I will close that ticket of #4206 has a doctest.
[01:04am] jason-: yes
[01:04am] jason-:             sage: finance.TimeSeries(v)
[01:04am] jason-:             [1.0000, 2.0000, 3.0000, 4.0000]
[01:04am] jason-:             sage: finance.TimeSeries(v[:,0])
[01:04am] jason-:             [1.0000, 3.0000]
```

this ticket is closed as fixed in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-09 09:09:54

Resolution: fixed
