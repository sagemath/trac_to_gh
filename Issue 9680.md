# Issue 9680: Don't greedily replace 'self' with classname in documentation

Issue created by migration from https://trac.sagemath.org/ticket/9680

Original creator: boothby

Original creation time: 2010-08-03 23:32:00

Assignee: mvngu

I just found this gem.  Apparently, something replaces "self" with the current classname in the documentation.  Amusingly, this almost made something comprehensible by accident.


```
sage: DLXMatrix?
...
The 0 entry is reserved internally... Blame the original author, or fix it yourDLXMatrix.
```


where it should read "yourself" at the end of the sentence.


---

Comment by jhpalmieri created at 2010-08-04 00:14:25

I only see this in the notebook.  The cause for the replacement lies in the file sagenb/misc/sageinspect.py, the line

```
        s = s.replace('self.','%s.'%obj_name)
```

in the function sage_getdoc.  There is an identical line in sage/misc/sageinspect.py, so I'm not sure why this doesn't show up in the command line, but I don't remember all the intricacies of how docstrings are produced in the two settings.


---

Comment by mmezzarobba created at 2015-04-13 13:11:31

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2015-04-13 13:11:31

`DLXMatrix?` now (6.6.rc3) displays

```
  ...
   Note: The 0 entry is reserved internally for headers in the
     sparse representation, so rows and columns begin their indexing
     with 1. Apologies for any heartache this causes. Blame the
     original author, or fix it yourself.
   ...
```

as expected.


---

Comment by vdelecroix created at 2015-04-22 19:26:29

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 01:45:07

Resolution: wontfix
