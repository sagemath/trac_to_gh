# Issue 1676: memleak and unused variable in pAdicCappedAbsoluteElement

Issue created by migration from https://trac.sagemath.org/ticket/1676

Original creator: wjp

Original creation time: 2008-01-03 21:41:02

Assignee: mabshoff

Attached patch fixes a memleak in pAdicCappedAbsoluteElement.multiplicate_order,
and removes an unused variable in pAdicCappedAbsoluteElement.__pow__ .


---

Attachment


---

Comment by mabshoff created at 2008-01-03 22:21:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 22:21:03

With this and the patch from #1675 applied I get:
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

Comment by mabshoff created at 2008-01-03 22:21:53

Oops:

After:

```
==16192== LEAK SUMMARY:
==16192==    definitely lost: 0 bytes in 0 blocks.
==16192==      possibly lost: 261,881 bytes in 713 blocks.
==16192==    still reachable: 39,070,317 bytes in 19,102 blocks.
==16192==         suppressed: 0 bytes in 0 blocks.
```

