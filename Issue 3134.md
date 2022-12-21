# Issue 3134: binomial doesn't take big integers

Issue created by migration from Trac.

Original creator: gebner

Original creation time: 2008-05-08 17:05:33

Assignee: mhansen

CC:  sage-combinat

I'm running sage-3.0.1 on linux/amd64 (using the precompiled binary) and binomial throws an exception if its second argument is greater than 2^63.


```
sage: binomial(2^100, 2^100)
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/<ipython console> in <module>()

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/arith.py in binomial(x, m)
   2009             raise TypeError, 'Either m or x-m must be an integer'
   2010     if isinstance(x, (int, long, integer.Integer)):
-> 2011         return integer_ring.ZZ(pari(x).binomial(m))
   2012     try:
   2013         P = x.parent()

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/gen.pyx in sage.libs.pari.gen.gen.binomial (sage/libs/pari/gen.c:13841)()

<type 'exceptions.OverflowError'>: long int too large to convert to int
```



---

Attachment


---

Comment by mhansen created at 2008-12-02 09:45:30

Changing status from new to assigned.


---

Attachment

I've attached two patches each of which fixes the problem.  I couldn't decide which one is better so I've left it up to the reviewer.  In my tests, PARI seemed to be a bit faster than the GMP routine.


---

Comment by mabshoff created at 2008-12-02 15:56:11

rlm, 

I know you are busy, but can you give this a review? :)

Cheers,

Michael


---

Comment by rlm created at 2008-12-02 22:07:32

Everything looks good here, but I haven't run tests or anything...


---

Comment by mabshoff created at 2008-12-02 22:09:31

I guess we are going with the PARI version then for speed reasons. And I will run doctests shortly to check if there are any issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 15:37:02

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 15:37:02

Merged trac_3134-2.patch in Sage 3.2.2.alpha0
