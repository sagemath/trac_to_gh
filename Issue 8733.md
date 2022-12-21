# Issue 8733: clean up documentation of c_graph.pyx

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-21 04:57:50

Assignee: jason, ncohen, rlm

As the subject says. The goal here is to make the documentation of the module `c_graph.pyx` consistent and also to better document the module itself.


---

Comment by mvngu created at 2010-04-23 02:41:17

The method `degree()` in the class `CGraphBackend` of the module `c_graph.pyx` has a bug in its implementation. This issue is tracked at #8395.


---

Comment by mvngu created at 2010-04-23 02:41:17

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-04-23 02:59:38

Changes proposed by the patch include:

 * Remove trailing white spaces.
 * Don't go over 79 characters wherever possible.
 * Cross link methods and classes.
 * Add more documentation to methods.
 * Stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).
 * Use "in" instead of "has_key()" for dictionaries.


---

Comment by ncohen created at 2010-04-24 15:02:13

Well.. What can I say besides "good work" ? :-)

Definitely cleaner, still passes all tests, the documentation is clearly improved, and I was responsible for some of the mistakes you corrected (the dictionaries, for examples) :-)

Positive review, and thank you very muuuuuuuuch !

Nathann


---

Comment by ncohen created at 2010-04-24 15:02:13

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:40:02

Resolution: fixed
