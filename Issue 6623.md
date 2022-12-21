# Issue 6623: Memory leak when calling binomial

Issue created by migration from Trac.

Original creator: hartke

Original creation time: 2009-07-26 01:41:23

Keywords: binomial, leak

There appears to be a memory leak when repeatedly calling binomial with different parameters.  This sometimes also appears when the parameters to binomial are not varied, but is not consistent.  This is a problem for the Combinations rank code, which makes many repeated calls to binomial.


```
sage: import random
print get_memory_usage()
for i in xrange(100000):
    x=random.randint(10,100)
    y=random.randint(0,x)
    r=binomial(x,y)
print get_memory_usage()

730.6328125
736.5625
```


The output is from running the code in Sage 4.1 on sagenb.org.  I think the same problem may involve the symbolic backend and GiNaC, since the same problem also occurs with log.


---

Comment by kcrisman created at 2009-09-29 03:12:44

Perhaps Pari, or our wrapping of it, is the problem.  Do the same thing as above, but replace

```
    r=binomial(x,y)
```

with

```
    r=pari(x).binomial(y)
```

and you get the same thing.  Interestingly, the memory change is *exactly* 3 MB.  I can also get similar results using pari(x).gcd(y), except exactly twice the memory is lost.  Also, changing the size of the xrange makes less memory get lost, and then seems to break the spell a bit. 

At any rate, it doesn't seem to happen for small ranges, does for bigger ones, with more memory lost.  If input is not random, definitely hard to reproduce.  Totally naively, could there be too many new_gen's for Pari to handle after a certain point?


---

Comment by dsm created at 2011-12-14 00:18:30

Is this leak still alive? I can't reproduce on sagenb 4.7.2 or linux 4.8.alpha1/2, the only two I have at hand.


---

Comment by mhansen created at 2013-07-23 15:02:36

Resolution: invalid


---

Comment by mhansen created at 2013-07-23 15:02:36

I don't get this either:


```
sage: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:sage: import random
:print get_memory_usage()
:for i in xrange(100000):
:    x=random.randint(10,100)
:    y=random.randint(0,x)
:    r=binomial(x,y)
:print get_memory_usage()
:
:--
1072.046875
1072.046875
```

