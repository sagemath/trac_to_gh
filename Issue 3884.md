# Issue 3884: change banner in "sage -advanced"

Issue created by migration from https://trac.sagemath.org/ticket/3884

Original creator: was

Original creation time: 2008-08-17 19:40:27

Assignee: cwitty

From Ralf Hemmecke:


```
woodpecker:~/scratch/SAGE>./sage -advanced
-----------------------------------------------------------
-----------------------------------------------------------
| SAGE: Software for Algebra and Geometry Experimentation |
Didn't I hear you saying at ISSAC that SAGE is no longer an abbreviation?
```


It should be the normal Sage banner. 


---

Attachment

This patch changes the banner printed to something very similar at the startup of Sage.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 23:40:07

With the patch applied we now get:
{{
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
}}}
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 23:40:51

With the patch we now get (better formatting):

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
```



---

Comment by mabshoff created at 2008-08-23 00:06:40

Merged in Sage 3.1.2.alpha0


---

Comment by mabshoff created at 2008-08-23 00:06:40

Resolution: fixed
