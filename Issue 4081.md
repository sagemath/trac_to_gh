# Issue 4081: [with patch, needs review] memleaks in nonlinear binary codes

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-09 01:17:00

Assignee: mabshoff




---

Attachment

Should fix this:

```
==5224== 728 bytes in 91 blocks are definitely lost in loss record 6,852 of 13,463
==5224==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==5224==    by 0x20BC8B55: __pyx_f_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_bitset_init (refinement_binary.c:1757)
==5224==    by 0x20BCCF24: __pyx_pf_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_25NonlinearBinaryCodeStruct___new__ (refinement_binary.c:5642)
==5224==    by 0x20BD9124: __pyx_tp_new_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_NonlinearBinaryCodeStruct (refinement_binary.c:11409)
...
```



---

Comment by rlm created at 2008-09-09 02:22:47

For valgrind logs after, see

http://sage.math.washington.edu/home/rlmill/sage-memcheck.14554


---

Comment by mabshoff created at 2008-09-09 02:24:39

Doctests pass and the valgrind log is clean. rlm and I also went over the patch in person. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-09 02:39:45

Resolution: fixed


---

Comment by mabshoff created at 2008-09-09 02:39:45

Merged in Sage 3.1.2.rc1
