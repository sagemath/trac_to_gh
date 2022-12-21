# Issue 8578: method int_repr only works for small finite fields

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-03-22 12:00:54

Assignee: AlexGhitza

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f41d594281e843d9):

```
For a finite field of, say 2^6 elements, an object representing an
element of such a field has a method called int_repr() that returns
the object's integer representation. However, if we are dealing with,
say GF(7^100), an object representing an element of such a field
doesn't have a corresponding int_repr() method. The report below
includes such a method, which is meant to work for a finite field of
any order.
```



---

Comment by kcrisman created at 2016-04-04 14:53:25

Apparently this is still an issue, see [this stack overflow question](http://stackoverflow.com/questions/36391931/how-do-i-get-the-int-representation-of-a-big-field-in-sage).


---

Comment by @DaveWitteMorris created at 2021-04-05 01:27:27

Changing status from new to needs_review.


---

Comment by @DaveWitteMorris created at 2021-04-05 01:27:27

Changing priority from major to minor.


---

Comment by @DaveWitteMorris created at 2021-04-05 01:27:27

Duplicate of #31605.


---

Comment by tscrim created at 2021-04-11 23:05:41

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-06-24 20:15:37

Resolution: invalid
