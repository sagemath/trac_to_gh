# Issue 5600: Cleanup of integer compositions

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-03-24 21:10:07

Assignee: nthiery

CC:  sage-combinat jbandlow

Fix  some weirdness of http://wiki.sagemath.org/combinat/Weirdness:
See compositions-cleanup-....-nt.patch

Accept any iterable as input
Adds concatenation of compositions


---

Comment by nthiery created at 2009-05-03 02:17:01

Changing keywords from "" to "integer compositions".


---

Attachment


---

Comment by nthiery created at 2009-05-19 06:24:25

Changing status from new to assigned.


---

Comment by ddrake created at 2009-05-25 06:16:09

I very much want this patch to get in, since I almost opened a ticket for one of the problems that it fixes. (`Composition()` doesn't take tuples as input.) One thing that needs to change, though, is with the docstring for Composition: right now, it tells the user to do `Composition_class?`, but that doesn't work since `Composition_class` is not in the default namespace. I think `Composition?` should simply display the correct docstring; there's no need to annoy the user by sending him or her bouncing from one docstring to the next.

Another issue is that the AUTHORS block is deleted from the head of the file. This should not be done. In fact, you should add yourself to it as the [developer's guide suggests](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files): something like "Nicolas M. Thiery (2009-05-25): several cleanups, new functions, and improvements (trac #5600)". I like listing ticket numbers because interested developers can go see exactly what you changed.

Tiny grammar/spelling issues:

  * At the top of compositions.py, you write "a compositions c of..."; you should use the singular. "A composition c of..."
  * line 56: you say a composition is a list of _positive_ integers, but it should be a list of _nonnegative_ integers.

Finally, I am seeing a doctest failure with this patch applied to vanilla 4.0.rc0:

```
**********************************************************************
File "/var/tmp/sage-4.0.rc0/devel/sage/sage/combinat/ribbon_tableau.py", line 875:
    sage: SemistandardMultiSkewTableaux([sp[0], sp[-1]],[2,2,2]).list()
Expected:
    [[[[1], [2], [3]], [This is the Trac macro *1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 3-macro)]]
Got:
    [This is the Trac macro *[[1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[[1, 1, 2-macro), [[None, None, 3], [None, 3], [2]]], [This is the Trac macro *[1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 2-macro), [[None, None, 3], [None, 3], [1]]], [This is the Trac macro *[1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2-macro), [[None, None, 3], [None, 2], [3]]], [This is the Trac macro *[1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 2-macro), [[None, None, 3], [None, 1], [3]]], [This is the Trac macro *[1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2-macro), [[None, None, 2], [None, 3], [3]]], [This is the Trac macro *[1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 2-macro), [[None, None, 1], [None, 3], [3]]], [This is the Trac macro *[1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 3-macro), [[None, None, 3], [None, 2], [2]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 3], [None, 2], [1]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 3], [None, 1], [2]]], [This is the Trac macro *[2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 2, 3-macro), [[None, None, 3], [None, 1], [1]]], [This is the Trac macro *[1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 3-macro), [[None, None, 2], [None, 3], [2]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 2], [None, 3], [1]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 1], [None, 3], [2]]], [This is the Trac macro *[2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 2, 3-macro), [[None, None, 1], [None, 3], [1]]], [This is the Trac macro *[1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 3-macro), [[None, None, 2], [None, 2], [3]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 2], [None, 1], [3]]], [This is the Trac macro *[1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 2, 3-macro), [[None, None, 1], [None, 2], [3]]], [This is the Trac macro *[2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 2, 3-macro), [[None, None, 1], [None, 1], [3]]], [This is the Trac macro *[1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 3, 3-macro), [[None, None, 2], [None, 2], [1]]], [This is the Trac macro *[1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 3, 3-macro), [[None, None, 2], [None, 1], [2]]], [This is the Trac macro *[1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 3, 3-macro), [[None, None, 1], [None, 2], [2]]], [This is the Trac macro *[2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 3, 3-macro), [[None, None, 2], [None, 1], [1]]], [This is the Trac macro *[2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 3, 3-macro), [[None, None, 1], [None, 2], [1]]], [This is the Trac macro *[2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[2, 3, 3-macro), [[None, None, 1], [None, 1], [2]]]]
**********************************************************************
```



---

Comment by nthiery created at 2009-07-29 11:53:21

The updated patch fixes the (the failure was actually actually a trivial thing in the doctest; thanks to Jason for spotting this!)


---

Attachment

Apply only this one, yes, this one!


---

Comment by jbandlow created at 2009-07-29 16:37:31

Doctests pass, and it looks like Dan's issues have been resolved.  Positive review from me.


---

Attachment

reviewer patch


---

Comment by mvngu created at 2009-08-22 23:05:42

I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:

 1. `trac_5600-compositions_cleanup-nt.patch`
 1. `trac_5600-reviewer.patch`


---

Comment by nthiery created at 2009-08-22 23:13:48

Replying to [comment:10 mvngu]:
> I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:
> 
>  1. `trac_5600-compositions_cleanup-nt.patch`
>  1. `trac_5600-reviewer.patch`

Thanks much for fixing all those typos! positive review on your reviewer's patch.


---

Comment by mvngu created at 2009-08-23 01:04:10

Merged patches in this order:

 1. `trac_5600-compositions_cleanup-nt.patch`
 1. `trac_5600-reviewer.patch`


---

Comment by mvngu created at 2009-08-23 01:04:10

Resolution: fixed
