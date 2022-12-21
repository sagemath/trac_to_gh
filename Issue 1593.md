# Issue 1593: m4ri -- the documentation of the echelon command only lists 1 algorithm but >= 2 algorithms are supported

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-24 17:36:31

Assignee: tba




---

Comment by was created at 2007-12-24 17:37:26

Also, there is a bug in algorithm = "classical", since it doesn't
check for mutability and doesn't clear the cache.


---

Comment by was created at 2007-12-24 17:37:26

Changing assignee from tba to malb.


---

Attachment


---

Comment by malb created at 2007-12-25 16:19:44

Changing status from new to assigned.


---

Comment by malb created at 2007-12-25 16:19:44

the attached patch adds 'classical' to the docstring of `echelonize`. The remark about `algorithm="classical"` is invalid because the called method `_echelon_in_place_classical` does check for mutability and clears the cache. See `matrix2.pyx` for details.


---

Comment by mabshoff created at 2008-01-25 17:34:01

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 17:34:21

Resolution: fixed


---

Comment by mabshoff created at 2008-01-25 17:34:21

Merged in Sage 2.10.1.alpha2
