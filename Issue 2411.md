# Issue 2411: Missing references in Sage tutorial

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2008-03-06 22:36:13

Assignee: tba

On the page

http://www.sagemath.org/doc/html/tut/node16.html

in the second paragraph the following sentence has problems.

"Note that the Sage kernel of a matrix $A$ is the ``left kernel'', i.e. the space of vectors 33#1 such that 34#2."

I'm not exactly sure what 33#1 and 34#2 should be, but these symbols certainly don't make sense.


---

Comment by mabshoff created at 2008-03-07 22:27:38

The tex file says:

```
Note that the \sage kernel of a matrix $A$ is the ``left kernel'', i.e.
the space of vectors $w$ such that $wA=0$.
```

I assume that ```left kernel''` confuses tex2html, so changing that to emph might fix the issue.

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-08-25 21:15:55

This was a latex2html issue.  It's been fixed by #3347, so this ticket should be closed.


---

Comment by mabshoff created at 2008-08-25 21:23:21

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 21:23:21

Thanks  John. Closed as suggested.

Cheers,

Michael
