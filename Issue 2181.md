# Issue 2181: pari 2.3.3 on osx -- gets build without readline

Issue created by migration from https://trac.sagemath.org/ticket/2181

Original creator: was

Original creation time: 2008-02-16 21:29:24

Assignee: mabshoff


```
                                                                GP/PARI CALCULATOR Version 2.3.3 (released)
                                                        i386 running darwin (ix86/GMP-4.2.1 kernel) 32-bit version
                                                         compiled: Feb 15 2008, gcc-4.0.1 (Apple Inc. build 5465)
                                                            (readline not compiled in, extended help available)
```


The above should not say "readline not compiled in".  It didn't with older versions of the pari spkg.  So something broke this.   

I once installed Sage on OS X for Ken Ribet specifically because gp's readline does work in OS X with Sage, and he couldn't get a very that worked without Sage no matter what he tried.  Now this is broken, which is bad. 

We should have a doctest that runs gp as a subprocess and verifies that readline is compiled in.  E.g.,


```
sage: import pexpect; p = pexpect.spawn('gp')
sage: p.expect('\?')
0
sage: assert 'readline not compiled in' not in p.before
```


Then this problem will never happen again. 


---

Comment by mabshoff created at 2008-02-16 21:34:39

Is this OSX 10.4, 10.5 or both? On 10.5 the dynamic readline is currently broken, see 1259, so those issues might be related if it happens on 10.5 only.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 21:34:39

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-24 00:03:28

This is fixed with #2282.


---

Comment by craigcitro created at 2008-02-24 00:03:28

Resolution: duplicate
