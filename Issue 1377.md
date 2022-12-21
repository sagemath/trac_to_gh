# Issue 1377: [with patch] technically incorrect code in integer_mod.pyx

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-03 00:02:29

Assignee: was

There is code in integer_mod.pyx that coerces a Python int into an int_fast32_t.  This is wrong, since a Python int can hold a C long; so this might truncate if sizeof(int_fast32_t) < sizeof(long).

However, the bug has little or no practical effect, since:
1) on 64-bit x86 Linux, sizeof(int_fast32_t) == sizeof(long);
2) the problem only occurs if you call `IntegerMod_int` directly (which nobody should); it looks like all the wrappers do the modulo before they create the `IntegerMod_int`.


---

Attachment


---

Comment by robertwb created at 2007-12-04 08:13:29

Changing assignee from was to somebody.


---

Comment by robertwb created at 2007-12-04 08:13:29

Changing component from algebraic geometry to basic arithmetic.


---

Comment by robertwb created at 2007-12-04 08:13:29

Looks good to me.


---

Comment by mabshoff created at 2007-12-06 02:15:10

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 02:15:10

Merged in 2.9.alpha0.
