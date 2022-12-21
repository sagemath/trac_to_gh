# Issue 6336: optional doctest failure -- constructions calculus tests hang forever

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 15:20:05

Assignee: tbd


```
	 [32.9 s]
sage -t -long --optional devel/sage/doc/en/constructions/calculus.rst
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
xprop:  unable to open display ''
Error: no "view" rule for type "application/x-dvi" passed its test case
       (for more information, add "--debug=1" on the command line)
xprop:  unable to open display ''
Error: no "view" rule for type "application/x-dvi" passed its test case
       (for more information, add "--debug=1" on the command line)
*** *** Error: TIMED OUT! *** ***
	 [1800.1 s]
```



---

Attachment


---

Comment by jhpalmieri created at 2009-06-16 19:11:05

Here's a patch.  This seems to fix this bug, but exposes another optional doctest failure (related to octave, I think): on sage.math, before the patch, I see the error message printed above.  After the patch, I don't, although I see this:

```
sage -t -optional "devel/sage/doc/en/constructions/calculus.rst"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [360.1 s]
```

So this patch is a partial fix.  Any takers for the octave timeout?


---

Comment by wdj created at 2009-06-16 22:59:55

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine.


---

Comment by rlm created at 2009-06-24 10:01:54

Resolution: fixed
