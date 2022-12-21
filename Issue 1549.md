# Issue 1549: Sage 2.9: fix optional doctests in tut.tex

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-17 13:37:02

Assignee: mabshoff


```
File "tut.py", line 3390:
    : G
Expected:
    Group([ (1,2,3)(4,5), (3,4) ])
Got:
    Group( [ (1,2,3)(4,5), (3,4) ] )
**********************************************************************
File "tut.py", line 3392:
    : G.Center()
Expected:
    Group(())
Got:
    Group( () ) 
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2008-04-25 00:07:24

doc patch, apply second


---

Attachment

I am attaching two patches.  The first changes the _repr_ of Galois groups from the current clunky


```
Galois group PARI group [8, 1, 3, "E(8)=2[x]2[x]2"] of degree 8 of the number field Number Field in a with defining polynomial x^2 + 1 over its base field
```


to


```
Galois group PARI group [8, 1, 3, "E(8)=2[x]2[x]2"] of degree 8 of the Number Field in a with defining polynomial x^2 + 1 over its base field
```


The second patch is a documentation patch and fixes the optional doctest failures in tut.tex (and removes the #optional tag from one of them, since now by default GaloisGroup uses PARI instead of optional GAP packages).


---

Comment by cremona created at 2008-04-27 17:14:55

Looks good to me.  There's a tiny typo in the first patch ("isreducible" needs a space), otherwise fine.


---

Attachment


---

Comment by AlexGhitza created at 2008-04-27 17:53:21

I've replaced the first patch with one that fixes the typo pointed out by John.


---

Comment by mabshoff created at 2008-04-28 00:08:06

Resolution: fixed


---

Comment by mabshoff created at 2008-04-28 00:08:06

Merged both patches in Sage 3.0.1.alpha1
