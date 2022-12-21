# Issue 4345: Make a system for default variable names

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-10-23 07:06:35

Assignee: cwitty

There are several places in Sage where one often has to specify variable names; it would be nice to have a uniform system in place for having defaults. For instance, these behaviors: 


```
sage: x = polygen(ZZ)
sage: F = NumberField(x^3-2)
Traceback (most recent call last):
...
TypeError: You must specify the name of the generator.

sage: CuspForms(23,2).newforms()
Traceback (most recent call last):
...
ValueError: Please specify a name to be used when generating names for generators of Hecke eigenvalue fields corresponding to the newforms.

```


can be annoying at times, especially for new users. 

A good model for the system might be the system-wide proof flags, for instance.


---

Comment by AlexGhitza created at 2009-01-23 02:47:25

Changing type from defect to enhancement.
