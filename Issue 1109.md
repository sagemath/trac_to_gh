# Issue 1109: [with patch] gp interface raises stack overflow exception if gp stack exceeds available memory

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-06 02:43:37

Assignee: was

The gp interface automatically runs allocatemem() to double the Pari stack size if it gets a response back from gp that includes "the PARI stack overflows", and then re-executes the failing command.  However, if gp cannot grow the stack further, allocatemem() will simply print a warning message and do nothing; then the interface gets stuck in a loop.  (This gives a stack overflow, rather than an infinite loop, because the re-execution is handled by a recursive call.)

I'm attaching a patch that shows one way to fix this; it notices when allocatemem() fails and simply returns the original stack-overflow error message.  (I'm not sure if this is the best approach; would it be better to raise an exception here?  Somebody familiar with the gp interface should comment.)


---

Attachment


---

Comment by cwitty created at 2007-11-06 03:56:32

On William's advice, I've revised my patch to raise an exception.  The new patch is 1109b.patch, which should be applied instead of 1109.patch.


---

Comment by mabshoff created at 2007-11-06 22:16:20

Resolution: fixed


---

Attachment

applied to 2.8.12.rc0
