# Issue 1068: turn off inplace optimizations

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-02 19:04:12

Assignee: mabshoff


```
> The inplace optimizations should be something that have to be
> > explicitly turned on, and they should be off by default.  I know they
> > make certain things faster, but correctness by default is *always* a
> > much more important consideration with serious mathematical software
> > such as Sage.  Always.
> >
> > I will very likely disable in-place optimization for sage-2.8.11,
> > until this issue gets properly discussed and resolved.

:-(, but I have to concede to your logic. The line to change is 148  
of coerce.pxi. Setting this value to 0 will turn them completely off.  
Other than numpy, (and the builtin libraries), do we use any other  
extension types? If there is a finite list of things for which it  
won't work, it would be possible to disable it just for those.

- Robert
```



---

Comment by mabshoff created at 2007-11-02 19:04:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-02 19:20:12

Resolution: duplicate


---

Comment by mabshoff created at 2007-11-02 19:20:12

Oops, dupe of #1018.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-02 19:20:34

Nope, dupe of #1038!
