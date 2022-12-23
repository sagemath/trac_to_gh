# Issue 363: maxima completion list

Issue created by migration from https://trac.sagemath.org/ticket/363

Original creator: was

Original creation time: 2007-05-13 15:42:18

Assignee: was


```
"Brandon.Barker
show details
	 8:18 am (20 minutes ago) 

In sage 2.5.0.2 I'm having trouble building maxima's command list
(tried this on a linux powerpc machine where I compiled SAGE from the
source, as well as an x64 machine with precompiled binaries):

sage: maxima.diff
Building Maxima command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/brandon/.sage//
maxima_commandlist_cache.sobj.

The file listed is never created, and no matter how long I wait, the
message above will still appear when I try to do tab completion.
However, I can still execute maxima.diff ok, but not some other
commands (like maxima.index):

sage: maxima.diff(x^2,x)
2*x
sage: maxima.index(x^2)
index(x^2)

Of course, this is probably because there is no index call function in
devel/sage-main/sage/interfaces/maxima.py
```



---

Comment by was created at 2007-05-18 15:53:23

the fix


---

Attachment

Fixed.


---

Comment by was created at 2007-05-18 15:53:41

Resolution: fixed
