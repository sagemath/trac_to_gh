# Issue 486: number_of_partitions() could be faster.

Issue created by migration from https://trac.sagemath.org/ticket/486

Original creator: bober

Original creation time: 2007-08-24 01:37:08

Assignee: bober

CC:  sage-combinat

Keywords: partitions, number_of_partitions, partitions_c.cc

The implementation of `number_of_partitions()` in `partition_c.cc` should use `quaddoubles `and `doubledoubles`, and should also select the necessary precision more carefully.

Also, number_of_partitions() should have more tests.


---

Attachment

Patch for the improvements described in this ticket. Touches files setup.py, combinat.py, and partitions_c.cc


---

Comment by bober created at 2007-08-29 16:14:06

NOTE: The attached patch depends on the patch attached to ticket #468 being applied (or on that bug being fixed in some other way, of course).

Some more notes on the attached file:
Many changes were made to partitions_c.cc to do some code cleanup, templatize some code, attempt to make the use of long doubles behave nicely across different platforms, to use qd_real and dd_real types, and to select the precision much more carefully.

The changes to combinat.py are just some doctest additions.

The change to setup.py is just to link partitions_c.cc with the qd library when it builds. (I think that it adds 5 characters to setup.py.)

Some timing results on a core duo T2400 (1.83 ghz):

before patch:

```
sage: time a = number_of_partitions(100000000)
CPU times: user 7.50 s, sys: 0.00 s, total: 7.50 s
Wall time: 7.50
sage: time a = number_of_partitions(1000000000)
CPU times: user 102.16 s, sys: 0.12 s, total: 102.28 s
Wall time: 102.94
```

after patch:

```
sage: time a = number_of_partitions(100000000)
CPU times: user 4.00 s, sys: 0.01 s, total: 4.01 s
Wall time: 4.11
sage: time a = number_of_partitions(1000000000)
CPU times: user 38.08 s, sys: 0.06 s, total: 38.14 s
Wall time: 39.24
```



---

Comment by mhansen created at 2007-10-13 02:49:39

bundle with both the patches for 468 and 486


---

Attachment


---

Comment by was created at 2007-10-13 07:47:59

Resolution: fixed
