# Issue 6171: [with patch, needs review] make 'prec' work with sqrt more of the time

Issue created by migration from https://trac.sagemath.org/ticket/6171

Original creator: jhpalmieri

Original creation time: 2009-05-31 21:40:16

Assignee: jhpalmieri

Before this patch:

```
sage: sqrt(10.1, prec=100)
...
TypeError: sqrt() got an unexpected keyword argument 'prec'
```

This is despite the fact that the docstring for sqrt lists as one of its inputs

```
            -  ``prec`` - integer (default: None): if None, returns
               an exact square root; otherwise returns a numerical square root if
               necessary, to the given bits of precision.
```

After this patch:

```
sage: sqrt(10.1, prec=100)
3.1780497164141406804582045589
sage: sqrt(10.1, prec=200)
3.1780497164141406804582045589354800553656236461562686475080
```



---

Comment by was created at 2009-05-31 21:59:15

Please add doctests to the patch illustrating that it fixes the bug.


---

Comment by jhpalmieri created at 2009-05-31 22:42:12

> Please add doctests to the patch illustrating that it fixes the bug.

Yes, sorry about that.  I was just sitting down to produce a new patch when I saw this comment.  Here's a new patch.


---

Attachment


---

Comment by mhansen created at 2009-05-31 23:32:09

Looks good to me.

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-05-31 23:32:09

Resolution: fixed
