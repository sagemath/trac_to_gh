# Issue 126: maxima -- doctest hang

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-11 15:07:20

Assignee: was


```
OK, this looks like a bug for 64-bit linux systems only.  I'll look into it.
The tests actually pass fine in about 8 seconds), but for some reasons when 
using the automated test system it hangs.  I'll look into it.  in the meantime
you could put 
"""nodoctest
as the first line of maxima.py, and it will skip testing it. 

On Wed, 11 Oct 2006 01:23:43 -0700, Jaap Spies <j.spies`@`hccnet.nl> wrote:

>
> In sage-1.4 make test hangs forever on
> sage -t  devel/sage-main/sage/interfaces/maxima.py
>
>
```



---

Comment by dmharvey created at 2006-10-11 16:33:57

Duplicate of #125


---

Comment by dmharvey created at 2006-10-11 16:33:57

Resolution: duplicate
