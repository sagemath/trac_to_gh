# Issue 3135: bug in solve_mod -- variable sorting

Issue created by migration from https://trac.sagemath.org/ticket/3135

Original creator: was

Original creation time: 2008-05-08 18:21:40

Assignee: was


```
Carlo Hamalainen: 
>  OK, but in solve_mod() perhaps the line
>  
>     vars.sort()
>  
>  should be
>  
>     vars.sort(cmp)
>  
>  so that the variables are actually sorted?
>  

Yes, *that* is certainly a bug!

William
```



---

Comment by AlexGhitza created at 2009-01-21 23:58:48

This is fixed by the patch up at #3124, so should be closed when #3124 gets closed.


---

Comment by mabshoff created at 2009-01-23 08:36:01

Fixed in Sage 3.3.alpha1 by merging #3124.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 08:36:01

Resolution: fixed
