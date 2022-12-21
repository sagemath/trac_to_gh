# Issue 6948: powers of exp are over simplified

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-09-17 13:48:17

Assignee: burcin

Francois Maltey wrote on sage-support:


```
var("a,b,c")
exp(a)^2 # returns exp(2a) is right
exp(a)^(1/2) # returns exp (a/2) is wrong, with a=2*i*pi we get -1=1
exp(a)^b # returns exp(a*b) is wrong
```


The thread is here:

http://groups.google.com/group/sage-support/browse_thread/thread/330a015bf640a4f3/0ddfdd5a4e021579


---

Attachment


---

Comment by burcin created at 2009-09-19 15:08:49

Changing status from new to assigned.


---

Comment by burcin created at 2009-09-19 15:08:49

This is fixed in my pynac tree, attachment:trac_6948-exp_power.patch is the corresponding patch for Sage. I will release a pynac spkg with some more fixes and post instructions for review.


---

Comment by burcin created at 2009-09-22 19:27:33

New pynac package available at #6993.


---

Comment by kcrisman created at 2009-09-23 01:58:54

Nice, but does it actually fix the examples provided?  

```
sage: exp(a)^(1/2)
sqrt(e^a)
```

I guess that's okay.  But

```
sage: exp(a)^(1/3)
e^a^(1/3)
sage: exp(a^(1/3))
e^(a^(1/3))
```

I think there are missing parentheses in the first example, particularly because it's not typeset.   Even if that is a convention, which I'm not so sure of, the dictum is that it's better to be explicit.  

I also get a doctest failure (not mentioned in the Pynac upgrade ticket) in product and quotient rule differentiation in calculus/tests.py, but it looks like that's the one in #6524, so it's properly speaking another issue, I guess.


---

Comment by burcin created at 2009-09-24 06:30:50

This package should fix this problem:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg

I'll attach a patch with some more doctests now.


---

Attachment

Positive review!


---

Comment by mvngu created at 2009-09-25 22:44:21

Resolution: fixed


---

Comment by mvngu created at 2009-09-25 22:44:21

Merged both patches.


---

Comment by mvngu created at 2009-09-27 10:38:42

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
