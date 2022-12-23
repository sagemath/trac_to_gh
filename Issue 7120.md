# Issue 7120: [with patch, needs review] document Sphinx/reST markup for INPUT/OUTPUT

Issue created by migration from https://trac.sagemath.org/ticket/7120

Original creator: jhpalmieri

Original creation time: 2009-10-05 05:20:03

Assignee: jhpalmieri

CC:  mhansen

Instead of using

```
INPUT:

- ``x`` - integer (default: 1) blah
```

Sphinx has specific markup for this:

```
:param x: blah
:type x: integer, default 1
```

The resulting output isn't quite the same, but it looks nice.

There are two patches here; one adds a little to the developer's guide to document this.  The other patch implements this (applied to the file sage/homology/simplicial_complex.py) so you can build the documentation and see what it looks like.  The patches are independent; either or both could be merged, although it would not really accomplish the purpose of the ticket to just merge the simplicial complex patch...


---

Attachment


---

Comment by awebb created at 2009-10-10 10:44:14

Changing status from needs_review to positive_review.


---

Attachment

The patch looks good to me and -docbuild works. I take it that is just an introduction and some information and not a conversion. I like the style though. Is the intent to slowly convert or to have both styles? ~Adam


---

Comment by mhansen created at 2009-10-15 10:00:26

Resolution: fixed
