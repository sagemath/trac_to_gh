# Issue 3925: Wrap Bernstein 's primegen

Issue created by migration from https://trac.sagemath.org/ticket/3925

Original creator: robertwb

Original creation time: 2008-08-22 08:06:19

Assignee: was

CC:  mvngu kevin.stueve

See http://cr.yp.to/primegen.html

Some code at http://thread.gmane.org/gmane.comp.python.cython.devel/2579/focus=2581



---

Comment by wjp created at 2009-07-12 12:25:46

I added some checks and doctests, and made Primes() use this.

This is still a work-in-progress. TODO:

* Turn primegen-0.97 into a .spkg. It needs an added -fPIC option since it will be linked into a cython extension module.

* Make sage.rings.arith.primes(start,stop) also use this for n not too small and not too large.

* Determine if there are predefined portable uint32/uint64 types available for use in cython.


---

Attachment


---

Attachment


---

Comment by wjp created at 2009-07-13 22:00:44

I've added an attempt at an .spkg for primegen-0.97 as an attachment, and also took the liberty of patching (untested...) spkg/install and spkg/standard/deps to build it automatically when installing sage. (In the 'spkg_deps' patch.)

I'm not entirely confident the build system of the library will work everywhere, since it is rather non-standard, but hopefully it is portable enough.

The library is tiny, with the .spkg only 32KB, and the compiled (Linux x86_64) library only 17KB.

Timing:

```
def f():    
    P = Primes()
    for p in P:
        if p > 10^8:
            break
time f()
```


goes from 84.17s (without this spkg+patch) to 20.77s (with spkg+patch) on a 2GHz Opteron.


---

Attachment

Hello Willem.  I successfully installed the spkg and the second patch but I don't know how to install the first patch as it changes files not in the usual code tree.  If you tell me how, I would like to test this.  -- John


---

Comment by wjp created at 2009-07-24 23:27:33

Hi John. The first patch isn't necessary to use the spkg. It's only for making a fresh 'make' of sage automatically build the spkg. I'm not too sure sure if that patch is right, actually; that part should probably be left to a release manager.


---

Comment by cremona created at 2009-07-25 09:00:33

Replying to [comment:6 wjp]:
> Hi John. The first patch isn't necessary to use the spkg. It's only for making a fresh 'make' of sage automatically build the spkg. I'm not too sure sure if that patch is right, actually; that part should probably be left to a release manager.

OK, I'll have another go sometime this weekend.  I'm glad about the first patch, since I'm not really competent to say if it's right (though it looks ok).


---

Comment by cremona created at 2009-07-26 09:58:23

To adopt this spkg as part of Sage
proper would need a vote on sage-devel.  I suggest that wjp helps that process
by collecting some data (before and after).  For example:

```
sage: time P = prime_range(10^8)
CPU times: user 1.83 s, sys: 0.50 s, total: 2.32 s
Wall time: 2.33 s
sage: len(P)
5761455
```

but this does not use the new PrimeGen class.  I tried this (with the
new spkg + patch):

```
sage: pg=Primes().pg
sage: pg.reset()
sage: N=pg.count(10^8)
sage: pg.reset()
sage: time P=[pg.next() for _ in range(N)]
CPU times: user 4.98 s, sys: 0.03 s, total: 5.01 s
Wall time: 5.02 s
```

which is slower but it's using a more stupid method to collect the
primes that in prime_range().


---

Comment by AlexGhitza created at 2009-08-16 08:27:32

Changing this to "needs work" given John's latest comments.  Note that "work" here would mean making the case to sage-devel that the spkg should be adopted, and asking for a vote.
