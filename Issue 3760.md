# Issue 3760: sage -t -long ell_finite_field.py fails with an out of memory error on 32-bit intel os x.

Issue created by migration from https://trac.sagemath.org/ticket/3760

Original creator: was

Original creation time: 2008-08-02 19:05:06

Assignee: was


```
Trying:
    for p in prime_range(Integer(10000)):           #long time (~20s)###line 1014:_sage_    >>> for p in prime_range(10000):           #long time (~20s)
          if p != Integer(389):
              G=E.change_ring(GF(p)).abelian_group()
Expecting nothing

error: no more memory
System 5116k:5116k Appl 4666k/449k Malloc 4088k/3k Valloc 1024k/445k Pages 159/97 Regions 2:2

halt 14  

         [19.0 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t -long --verbose devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py
Total time for all tests: 19.0 seconds
bsd:sage-3.1.alpha0 was$ 
```



---

Comment by cremona created at 2008-09-04 16:27:49

Could someone with 32-bit intel os x try this again, since it is possible that the patch for #3961 (merged in 3.1.2.alpha2) fixes this.

If not I can try to look into it but I'm not sure how to as it works fine on my laptop.


---

Comment by mabshoff created at 2008-09-24 08:30:00

#4179 is a duplicate of this ticket and has some additional info.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-15 22:02:43

Just for the record: I had tried to get a grip on this issue, the outcome is trac ticket #4181 --- once that ticket is fixed, this one will (most probably) be resolved, too. Hopefully.

Cheers,

gsw


---

Comment by mabshoff created at 2008-12-17 03:34:00

The following code specifically seems to expose the problem:

```
E = EllipticCurve('389a')
for p in prime_range(Integer(10000)): 
    if p != Integer(389):
        G=E.change_ring(GF(p)).abelian_group()
```

On sage.math the memory increase is about 70 MB with Sage 3.2.2.rc0, so I have no idea how this could fail on OSX.

Cheers,

Michael


---

Comment by was created at 2009-02-19 18:53:11

This exposes the problem much more clearly on my MacBook Pro:

```
teragon:sage-3.3.rc2 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E = EllipticCurve('389a')
sage: time v = [E.change_ring(GF(p)) for p in prime_range(10000) if p != 389]
| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |
| Type notebook() for the GUI, and license() for information.        |
error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2

halt 14
```



---

Comment by was created at 2009-02-19 19:15:52

This is really a problem with Singular.  It has nothing to do with elliptic curve:


```
teragon:sage-3.3.rc2 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: v = prime_range(4974); len(v)
666
sage: w = [GF(p)['x,y'] for p in v]
| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |
| Type notebook() for the GUI, and license() for information.        |
error: no more memory (mminit.cc)
System 4608k:4608k Appl 4510k/97k Malloc 4093k/2k Valloc 512k/95k Pages 121/7 Regions 1:1

halt 14
teragon:sage-3.3.rc2 wstein$ uname -a
Darwin teragon.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386
```



Argh!


---

Comment by was created at 2009-02-19 19:16:50

By the way, it says "mminit.cc" in the above, since I hardcoded that into the singular library -- the message is being printed from a hardcoded message in mminit.cc in the singular *kernel*.


---

Comment by GeorgSWeber created at 2009-02-22 22:16:06

Yippieh:

```
sage: v = prime_range(4974); len(v)
666
sage: w = [GF(p)['x,y'] for p in v]
sage: 
```



---

Comment by mabshoff created at 2009-02-22 23:06:02

Unless someone fixes #5344 in the next 24 hours this will not go into 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 23:06:02

Changing priority from blocker to critical.


---

Comment by GeorgSWeber created at 2009-02-23 08:25:16

For the record:

The underlying problem is now known: Singular/omalloc relies on a version 2.6.5 of dlmalloc from 1998, and that version behaves bad on Macs.

In the course of the investigation, another Singular/kernel bug got in the way.

I think I know how to *circumvent* this Singular/kernel bug ("just" drop in the recent dlmalloc 2.8.3 at the place of the old version, and/or prevent omalloc's "configure" from setting the macro "OMALLOC_USES_MALLOC"), but I thought I try and fix that other bug first.


BTW:
From the historical remarks in v2.8.3 in dlmalloc it seems plausible that the old v2.6.5 is the culprit also for the bad behaviour on Fedora 9/10 systems --- but this is ticket #5278. Which probably should be closed as a dupe (to this ticket here).


---

Comment by mabshoff created at 2009-02-24 19:39:21

Fixed in Sage 3.4.alpha0 via #4181 and #5344.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:39:21

Resolution: fixed
