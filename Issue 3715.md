# Issue 3715: trivial to do bug fix

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-23 18:39:20

Assignee: cwitty


```
While debugging the new release of the FriCAS optional package Waldek
Hebisch discovered a small bug in the script that starts clisp. There
are missing argument quotes that can cause problems if some spkg (such
as fricas-1.0.3.spkg) needs to pass arguments containing spaces.

http://sage.math.washington.edu/home/page/packages/lisp.diff

--- lisp.orig   2008-07-20 17:22:27.000000000 -0400
+++ lisp        2008-07-20 03:04:00.000000000 -0400
`@``@` -1,2 +1,2 `@``@`
 #!/bin/sh
-"$SAGE_ROOT/local/bin/clisp.bin" -B "$SAGE_ROOT/local/lib/clisp-2.46" $`@`
+"$SAGE_ROOT/local/bin/clisp.bin" -B "$SAGE_ROOT/local/lib/clisp-2.46" "$`@`"

-----

Regards,
Bill Page.
```



---

Comment by mabshoff created at 2008-07-29 16:00:31

The spgk at #3712 fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 16:52:35

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-07-29 16:52:35

Due to the positive review at #3712 I am changing this ticket to a positive review also.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 16:52:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-29 16:55:51

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 16:55:51

Merged in Sage 3.0.6.final
