# Issue 3006: missing elliptic integrals in special.py

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-04-23 14:27:55

Assignee: was

The following problem was reported by Dustin Vaselaar to sage-support:


Hello,
I am looking to use a complete elliptic integral of the first kind in
sage, however I'm not sure if this has been implemented.  The link
http://www.sagemath.org/doc/html/ref/module-sage.functions.special.html
mentions a function "elliptic_kc", but it doesn't seem to be
implemented in sage version 3.0, judging from the result of this
command:


```
sage: elliptic_kc?
Object `elliptic_kc` not found.
```


Any insights on using a a complete elliptic integral of the first kind
in sage?




---

Comment by wdj created at 2008-04-23 14:31:57

Clearly this is a problem with "documentation" but I filed it under "calculus" since that seemed closer. It is a matter of adding a wrapper to Maxima's function elliptic_kc.


```
sage: RR(maxima.eval("elliptic_kc (0.5)"))
1.85407467730137
```


I'll submit a patch soon.


---

Attachment

Thinking about this problem more, I think it is my fault. In any case, a patch is attached.  It is based on 3.0 and passes sage -t but my (old) machine froze (as it very often does) during the sage -testall. No errors were reported before the freeze.


---

Comment by AlexGhitza created at 2008-04-24 03:38:53

Looks good.


---

Comment by mabshoff created at 2008-04-24 04:00:13

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-24 04:00:13

Resolution: fixed
