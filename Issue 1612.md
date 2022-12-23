# Issue 1612: Finding eigenforms within spaces of ModularForms

Issue created by migration from https://trac.sagemath.org/ticket/1612

Original creator: ljpk

Original creation time: 2007-12-27 16:23:08

Assignee: was

There doesn't seem to be a way to find eigenforms within spaces of modular forms.

Also, the sturm_bound and hecke_bound methods seem not to work:


```
S37=CuspForms(37,2)
S37.sturm_bound()}}}

{{{Exception (click to the left for traceback):
...
AttributeError: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'}}}


---

Comment by AlexGhitza created at 2008-01-09 12:41:36

These are two separate issues.  The second one is now #1736.


---

Comment by craigcitro created at 2008-06-15 02:04:27

This is already fixed. (Most of this came in with the new modular abelian varieties code.)


---

Comment by craigcitro created at 2008-06-15 02:04:27

Resolution: fixed
