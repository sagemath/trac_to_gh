# Issue 651: [with patch] memory leak in gmp_globals.c

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-13 21:55:58

Assignee: mabshoff

In gmp_globals.c we init tmp again instead of clearing it. This leaks about 16 bytes. For a patch see

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-fix-small-mpq-leak-in-gmp_globals.c.patch

Without the patch:

```
==32229== LEAK SUMMARY:
==32229==    definitely lost: 2,548 bytes in 7 blocks.
==32229==      possibly lost: 364,814 bytes in 1,127 blocks.
==32229==    still reachable: 137,021,540 bytes in 18,327 blocks.
==32229==         suppressed: 0 bytes in 0 blocks.
```

With the patch:

```
==14532== LEAK SUMMARY:
==14532==    definitely lost: 2,532 bytes in 5 blocks.
==14532==      possibly lost: 364,878 bytes in 1,128 blocks.
==14532==    still reachable: 137,021,460 bytes in 18,324 blocks.
==14532==         suppressed: 0 bytes in 0 blocks.
```


Every byte counts ;)

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-13 21:56:07

Changing status from new to assigned.


---

Comment by was created at 2007-09-14 02:54:46

Resolution: fixed
