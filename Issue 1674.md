# Issue 1674: memleak in pAdicCappedRelativeElement.__pow__

Issue created by migration from https://trac.sagemath.org/ticket/1674

Original creator: wjp

Original creation time: 2008-01-03 21:07:41

Assignee: mabshoff

The attached patch plugs a small memleak in pAdicCappedRelativeElement.__pow__ .


---

Attachment


---

Comment by mabshoff created at 2008-01-03 21:18:03

Merged in 2.9.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 21:18:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 21:25:07

Some statistics on running memcheck on `padic_capped_relative_element.py`:
Before:

```
==6186== LEAK SUMMARY:
==6186==    definitely lost: 312 bytes in 30 blocks.
==6186==      possibly lost: 261,425 bytes in 712 blocks.
==6186==    still reachable: 39,070,789 bytes in 19,104 blocks.
==6186==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

6 blocks with 48 bytes, but those leaks should add up quickly.

Cheers,

Michael
