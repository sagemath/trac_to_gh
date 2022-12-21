# Issue 1256: mwrank*.spkg now redundant, included in cremona*.spkg

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2007-11-24 21:22:42

Assignee: was

The code in the new cremona* package contains all of what was in the mwrank* package.  So the latter can be abandoned as soon as the wrappings for mwrank functions have been migrated.  This will only be really serious when I next fix a bug in mwrank -- since from now on I'll only be editing the version which is part of cremona*.

I'm sure this is an easy job for someone who is familiar with the mwrank wrappings (not me, alas, though I suppose I should be).



---

Comment by mabshoff created at 2007-12-05 19:03:09

I am taking care of this. The following things need to be done:

```
[18:17] <was_> Definitely the solution is to (1) remove the mwrank*spkg.
[18:17] <was_> (2) copy over the mwrank executable which gets build as part of cremona*.spkg
[18:17] <was_> (3) Change things in setup.py so that all the prober mwrank-related libraries are linked in (it's maybe 4 libraries now instead of 1)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-05 19:03:15

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-05 19:03:15

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-12-05 19:26:37

Ok, the following binaries are installed my mwrank:
 * mwrank
 * tmrank
 * ratpoint
 * findinf
 * tate
 * conductor
 * torsion
 * twist
 * allisog
 * indep
 * tconic


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2007-12-06 02:01:51

Ok, I updated cremona.spkg to also install all mwrank binaries. It is at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 02:04:33

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 02:04:33

Merged in 2.9.alpha0.
