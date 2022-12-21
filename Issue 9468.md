# Issue 9468: Extend ClasscallMetaclass to allow for membership testing

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-07-10 02:38:16

Assignee: jason

CC:  sage-combinat

From the doc:

```
        Let ``cls`` be a class in :class:`ClasscallMetaclass`, and consider
        a call of the form:

            ``x in cls``

        If ``cls`` defines a method ``__classcontains__``, then this
        results in a call to::

         - ``cls.__classcontains__(cls, x)``

        EXAMPLES:

        We construct a class which implements membership testing, and
        which contains ``1`` and no other x::

            sage: from sage.misc.classcall_metaclass import ClasscallMetaclass
            sage: class Foo(object):
            ...       __metaclass__ = ClasscallMetaclass
            ...       `@`staticmethod
            ...       def __classcontains__(cls, x):
            ...           return x == 1
            sage: 1 in Foo
            True
            sage: 2 in Foo
            False
```


This patch also fixes some typos and such in the documentation of ClassCallMetaclass


---

Comment by nthiery created at 2010-07-10 03:02:09

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-07-10 03:02:09

Florent: the documentation should really include the __*__ methods. Here, this makes the link for __get__ wrongly point to the corresponding Python doc (with the intersphinx option).


---

Comment by hivert created at 2011-04-22 22:19:00

Replying to [comment:2 nthiery]:

I just pushed on sage-combinat a trivial doc-fix patch. Otherwise it is ready to go.


---

Comment by nthiery created at 2011-04-23 01:46:44

Final version including review patch by Florent


---

Comment by nthiery created at 2011-04-23 01:47:27

Changing status from needs_review to positive_review.


---

Attachment

Checked, folded, posted. Thanks!


---

Comment by jdemeyer created at 2011-06-08 07:12:25

Resolution: fixed
