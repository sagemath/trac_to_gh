# Issue 923: change all "sage.:"'s to "sage: blah # not tested"

Issue created by migration from https://trac.sagemath.org/ticket/923

Original creator: was

Original creation time: 2007-10-18 19:43:58

Assignee: failure


```
> I think "sage.:" should be replaced by
>
>   sage: f.factor_padic()       # not tested
>
> i.e., "putting not tested" as  a comment has the same effect
> as sage.:.  I wrote the"sage." notation before there were
> doctesting comment modifiers.
>
> Does this seem ok with everybody?   Comment modifiers are definitely
> much clearer than "sage.:".

Sounds better to me.
```



---

Comment by was created at 2007-10-20 02:01:35

Changing assignee from failure to was.


---

Comment by was created at 2007-10-20 02:01:49

Changing status from new to assigned.


---

Comment by was created at 2007-10-20 02:01:49

I'm doing this for sage-2.8.8.


---

Comment by was created at 2007-10-20 11:41:42

Resolution: fixed
