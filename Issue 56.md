# Issue 56: fundamental speed issues

Issue created by migration from https://trac.sagemath.org/ticket/56

Original creator: was

Original creation time: 2006-09-13 23:40:58

Assignee: somebody

We're not sure what to make of this yet:


```
MAGMA:
was@sage:~$ magma
Magma V2.12-20    Wed Sep 13 2006 16:02:30 on sage     [Seed = 4122492641]
Type ? for help.  Type <Ctrl>-D to quit.
> two := 2;
> A := [0..10^5-1];
> time B := [i + two : i in A];
Time: 0.030 

SAGE int's:

sage: two=int(2)
sage: A = range(10^5)
sage: time B = [i+two for i in A]
CPU times: user 0.03 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04

SAGE GMP ints:

sage: two=2
sage: A = srange(10^5)
sage: time B = [i+two for i in A]
CPU times: user 0.36 s, sys: 0.01 s, total: 0.37 s
Wall time: 0.37
```



---

Comment by mabshoff created at 2007-08-20 00:01:51

Hello,

I just revisited this and now the speed difference (on a different system) with Sage 2.8.1:

sage: two=int(2)
sage: A = range(10^5)
sage: time B = [i+two for i in A]
CPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08
sage:
sage:
sage: two=2
sage: A = srange(10^5)
sage: time B = [i+two for i in A]
CPU times: user 0.16 s, sys: 0.02 s, total: 0.18 s
Wall time: 0.18

I don't have Magma installed on that machine, so no comparable numbers from there.

Thoughts?

Michael


---

Comment by was created at 2007-08-23 06:33:13

Some numbers with the latest SAGE and latest magma:

```
sage: sage: A = srange(10^6)
sage: sage: time B = [i+two for i in A]
CPU times: user 0.22 s, sys: 0.69 s, total: 0.91 s
Wall time: 0.92

> A := [0..10^6-1];
> time B := [i + two : i in A];
Time: 0.220
```



---

Comment by was created at 2007-08-23 06:34:16

Python

```
sage: A = range(10^6)
sage: two = int(2)
sage: time B = [i+two for i in A]
CPU times: user 0.47 s, sys: 0.03 s, total: 0.50 s
```



---

Comment by jason created at 2008-03-03 23:19:27

on 2.10.2 on my system, comparing the original ticket:


```
sage: sage: two=int(2)
sage: sage: A = range(10^5)
sage: sage: time B = [i+two for i in A]
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04
sage: sage: two=2
sage: sage: A = srange(10^5)
sage: sage: time B = [i+two for i in A]
CPU times: user 0.06 s, sys: 0.01 s, total: 0.07 s
Wall time: 0.07
```



and comparing the comments (with 10^6, not 10^5)


```
sage: sage: A = range(10^6)
sage: sage: two = int(2)
sage: sage: time B = [i+two for i in A]
CPU times: user 0.32 s, sys: 0.01 s, total: 0.33 s
Wall time: 0.33
sage: two=2
sage: sage: sage: A = srange(10^6)
sage: sage: sage: time B = [i+two for i in A]
CPU times: user 0.54 s, sys: 0.05 s, total: 0.60 s
Wall time: 0.60
```


So the issue seems to be not to show up like the original post, but I'm still seeing speed decreases as pointed out in the comments.


---

Comment by was created at 2008-06-16 00:05:57

TODAY we have with Magma2.14 and Sage on OS X 10 32-bit core2duo.


```
two := 2;                      
A := [0..10^5-1];             
time B := [i + two : i in A]; 
```



```
sage: two=2
sage: A = srange(10^5)
sage: time B = [i+two for i in A]
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
```




The *right* benchmark:

```
two := 2;                      
A := [0..10^5-1];  
time for i in A do b := i + two; end for;
Time: 0.020
```


In Sage:


```
%cython
from sage.all import srange, Integer
from sage.rings.integer cimport Integer

cdef object two=Integer(2)
cdef list A = srange(Integer(100000))

def foo4():
   for i in A:
      (<Integer>two)._add_c(<Integer>i)
```


This takes 0.17s, beating magma.

And in pure python

```
two=2
A = srange(100000)
def bar():
    for i in A:
        c = i + two

timeit('bar()')
///
25 loops, best of 3: 24.6 ms per loop
```



---

Comment by was created at 2008-06-16 00:05:57

Resolution: fixed
