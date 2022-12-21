# Issue 9044: Use mpmath for the erf() function

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-05-25 03:56:52

Assignee: jason, jkantor

CC:  fredrik.johansson kcrisman

Appears the current erf() function is limited to 53-bit accuracy, while using mpmath instead will provide greater accuracy and also greater speed.  This is from an IRC session - an edited version is below.


```
[09:55] --> E1ephant has joined this channel (~E1ephant`@`e1ephant.broker.freenet6.net).
[09:55] <E1ephant> hi =)
[09:57] <E1ephant> could you tell me please something? after integrating: integrate( (2/sqrt(2*pi)) * exp(-x^2/2), x, 0, 2)  a have erf(sqrt(2))
[09:57] <E1ephant> how can i calculate than that value numerically?
[09:57] <E1ephant> i mean erf(sqrt(2))
[09:58] <rbeezer> E1ephant: N(erf(sqrt(2)))
[09:59] <E1ephant> :-* thx
[09:59] <rbeezer> N?  will give you documentation about using this to get different precision
[10:46] <schilly> interesting, erf only works for the default 53 bits. if somebody needs more digits, resort to mpmath
[10:46] <schilly> import mpmath; mpmath.mp.dps=200; mpmath.erf(mpmath.sqrt(2))
[10:50] <schilly> mpmath is also neary 4 times faster for that one on my machine. i think the erf definition should be changed
[10:51] <rbeezer> schilly: interesting (and even better that it is faster!)
[11:00] <schilly> ah. end 16.5 times faster for the same 53bits prec (i still had it at 200 for the benachmark, where it was also faster)
[11:02] <logix> mpmath is faster for 200 bits precision than sage is for 53 bits? uh :)
[11:03] <schilly> logix: yes
```



---

Comment by schilly created at 2010-05-25 09:00:03

For a complete switch this probably needs a bit more analysis. I tested this on another (much faster) machine again and the timing numbers were different. No fast binding for mpmath installed?

But in any situation, using `mpmath.erf` to calculate the erf for a precision other than 53 bits is a necessary addition. It seems that it also depends on the magnitude of the input argument.


```
import mpmath

sage: %timeit erf(0.001)
625 loops, best of 3: 74.6 µs per loop   #winner
sage: %timeit mpmath.erf(0.001)
625 loops, best of 3: 101 µs per loop

sage: %timeit erf(1.001)
625 loops, best of 3: 82.7 µs per loop   #winner
sage: %timeit mpmath.erf(1.001)
625 loops, best of 3: 120 µs per loop

sage: %timeit erf(10010)
625 loops, best of 3: 52.3 µs per loop
sage: %timeit mpmath.erf(10010)
625 loops, best of 3: 12.8 µs per loop   #winner
```



---

Comment by kcrisman created at 2010-06-09 01:40:56

See also #1173; we should probably do this just because it allows complex input.


---

Comment by kcrisman created at 2011-06-17 19:30:06

It looks like this is pretty much done at #1173.   I'll put a comment there to add `erf(sqrt(2))` just to address the point here, though other tests on that patch basically test the same thing.


---

Comment by kcrisman created at 2011-06-17 19:30:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-08-19 14:15:44

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-08-19 14:15:44

This is now in the 'needs work' of #1173 and will be trivial to include there, so this should be closed as a dup.


---

Comment by jdemeyer created at 2011-08-22 08:09:11

Resolution: duplicate
