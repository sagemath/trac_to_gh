# Issue 8891: sage -t doesn't accept . as current directory

Issue created by migration from Trac.

Original creator: wjlaffin

Original creation time: 2010-05-05 16:31:01

Assignee: tbd




---

Attachment

It was explicitly disabled long ago (before Trac), but I don't see any reason why it should be now.


---

Comment by mhansen created at 2010-05-05 16:48:11

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-06-12 08:56:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-06-12 08:56:50

Without the patch, I get, e.g.,

```sh
mpatel`@`sage monoids$ sage -t .
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
mpatel`@`sage monoids$ 
```

With the patch, I get

```sh
mpatel`@`sage monoids$ sage -t .
sage -t  "./string_monoid_element.py"                       
         [2.1 s]
[...]
```



---

Comment by rlm created at 2010-06-25 15:42:54

Resolution: fixed
