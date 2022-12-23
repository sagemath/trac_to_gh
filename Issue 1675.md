# Issue 1675: memleak in pAdicCappedRelativeElement._set_from_Rational

Issue created by migration from https://trac.sagemath.org/ticket/1675

Original creator: wjp

Original creation time: 2008-01-03 21:28:48

Assignee: mabshoff

The attached patch fixes a memleak in pAdicCappedRelativeElement._set_from_Rational


---

Attachment

With this and the patch from 1676 applied I get:
Before:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

Patch applied to Sage 2.9.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 22:20:51

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 22:21:59

Oops:

After:

```
==16192== LEAK SUMMARY:
==16192==    definitely lost: 0 bytes in 0 blocks.
==16192==      possibly lost: 261,881 bytes in 713 blocks.
==16192==    still reachable: 39,070,317 bytes in 19,102 blocks.
==16192==         suppressed: 0 bytes in 0 blocks.
```

