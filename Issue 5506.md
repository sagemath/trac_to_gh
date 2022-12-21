# Issue 5506: symbolic vectors class

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-12 23:07:38

Assignee: was

CC:  eviatarbach

We really should make symbolic vectors a subclass of the generic free modules.  That way we can have a .args() function, a variables function, and a few other functions that make sense for symbolic vectors, but maybe not for arbitrary vectors.

We can also make them callable, so vector-valued functions work.


---

Comment by jason created at 2010-03-17 05:57:58

Changing type from defect to enhancement.


---

Comment by jason created at 2010-05-11 18:08:21

#8947 is a start on this.  We could add to that an args() function, a variables function, etc.


---

Comment by jason created at 2010-05-11 18:15:26

See #3021 for more things we could add to the class.
