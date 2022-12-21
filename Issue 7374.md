# Issue 7374: wrong docstring for is_isomorphic() in permgroup.py

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-11-02 06:18:33

Assignee: joyner

The docstring for `is_isomorphic()` for permutation groups claims "If mode="verbose" then an isomorphism is printed."

However, that's not the case.  This is probably just left over from a previous version of the method.  In any case, the attached trivial patch removes this from the docstring.


---

Attachment


---

Comment by AlexGhitza created at 2009-11-02 06:47:32

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-03 15:39:27

Looks good to me.


---

Comment by mhansen created at 2009-11-03 15:39:27

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-04 14:46:33

Resolution: fixed
