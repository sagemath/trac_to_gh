# Issue 2956: generic multivariate polynomials are buggy on exponent overflow

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-04-19 15:26:41

Assignee: somebody

CC:  mjo

Long exponents are silently truncated to word-size exponents:

```
sage: K.<x,y> = AA[]
sage: x^(2^64 + 12345)
x^12345
```


In one test, I also saw a crash, but I can't reproduce it.

```
sage: K.<x,y> = ZZ[]
sage: (x^12345)^54321


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
...
```

(The crash was on 32-bit x86 Debian testing.  The first test fails with the same answer on both 32-bit and 64-bit x86.)


---

Comment by zimmerma created at 2008-10-19 13:16:32

For the 2nd example, I do not get a crash, but a funny result with 3.1.4 on a 32-bit computer:

```
sage: K.<x,y> = ZZ[]
sage: (x^12345)^54321
x^28393*y^10232
```

Note that y does not appear in the input!

Possible explanation: 12345*54321 = 10232*2^16+28393.
Apparently the low 16 bits are used to store the exponent of x, and the upper 16 bits
for the exponent of y, but no check for overflow is done!!!


---

Comment by zimmerma created at 2008-10-19 13:18:21

Replying to [comment:2 zimmerma]:

I realize this was already noticed by Carl in #2957.


---

Comment by malb created at 2009-01-25 19:00:35

Changing assignee from somebody to malb.


---

Comment by malb created at 2009-01-25 19:00:35

Changing status from new to assigned.


---

Comment by mjo created at 2012-01-07 23:38:55

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-07 23:38:55

I think these are both fixed, so I've added doctests. I have only tested on x64: I think the first example should overflow on both, the second should work on both. But a reviewer should give it a try on x32.


---

Comment by zimmerma created at 2012-01-08 10:50:15

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2012-01-08 10:50:15

I tried on a 32-bit machine with vanilla 4.7.2. The first doctest is ok, for the second one I get:

```
sage: (x^12345)^54321
...
OverflowError: Exponent overflow (670592745).
```

thus the patch needs work.

Paul Zimmermann


---

Comment by mjo created at 2012-01-08 17:07:19

Hmm, I wonder how big we can make the exponent. I was guessing `(2^31 - 1)`, but `670592745` is way smaller than that.

Since the crash was on a 32-bit machine, we can assume (i.e. hope) that it was due to the overflow. With that in mind, maybe we should just ignore the output with "..." and consider the test a success if it doesn't crash?


---

Comment by mjo created at 2012-01-09 00:44:54

Changing status from needs_work to needs_review.


---

Attachment

Updated patch, should also work on x32.


---

Comment by zimmerma created at 2012-01-09 08:08:01

Changing keywords from "" to "sd35.5".


---

Comment by zimmerma created at 2012-01-09 08:28:07

note: for `K.<x,y> = AA[]` the maximum exponent seems to be 2147483647 both on 32- and 64-bit,
while for `K.<x,y> = ZZ[]` on 32-bit the maximum is 32768, and on 64-bit it is 1073741824.

Paul


---

Comment by zimmerma created at 2012-01-09 08:32:25

both doctests now pass on x32. I'm running the doctests on x32.

Paul


---

Comment by zimmerma created at 2012-01-10 08:43:09

my installation of Sage on x32 was corrupted, I will try again with sage.4.8.alpha6.

Paul


---

Comment by zimmerma created at 2012-01-11 07:09:47

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-01-11 07:09:47

I confirm all doctests pass on x32 (I got one failure in `rings/real_mpfi.pyx` but this was due
to the spkg from #12171 I had installed). Thus positive review.

Paul


---

Comment by jdemeyer created at 2012-01-18 08:07:13

Resolution: fixed
