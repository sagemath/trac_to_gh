# Issue 3123: blacklist "gcc version 4.1.0 (SUSE Linux)"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-07 14:27:31

Assignee: mabshoff

gcc version 4.1.0 (SUSE Linux) from OpenSuSE 10.1 is know broken and will fail to file Sage with

```
sage/modules/real_double_vector.c: In function ‘__pyx_pf_4sage_7modules_18real_double_vector_28RealDoubleVectorSpaceElement_
__init__’:
sage/modules/real_double_vector.c:2012: internal compiler error: in merge_alias_info, at tree-ssa-copy.c:235
Please submit a full bug report,
with preprocessed source if appropriate.
See <URL:http://www.suse.de/feedback> for instructions.
error: command 'gcc' failed with exit status 1
```

Blacklist it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-07 14:27:40

Changing status from new to assigned.


---

Comment by was created at 2009-06-15 23:19:17

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2013-05-19 13:02:20

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:02:20

Fixed by the GCC spkg.


---

Comment by jdemeyer created at 2013-05-19 13:02:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:23:36

Resolution: invalid
