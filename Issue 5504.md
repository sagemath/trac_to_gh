# Issue 5504: fix shell script "sage"

Issue created by migration from https://trac.sagemath.org/ticket/5504

Original creator: dangrayson

Original creation time: 2009-03-12 21:03:27

Assignee: was

It would be great if the line

"$SAGE_ROOT/local/bin/sage-sage" $*

in the top level script 'sage' would be changed to

"$SAGE_ROOT/local/bin/sage-sage" "$`@`"

so it doesn't split up command line arguments that happen to have spaces in them.


---

Comment by GeorgSWeber created at 2009-03-27 20:18:13

The intended change already has happened and was part of trac #4354 : "loading a file with spaces in the filename doesn't work"


---

Comment by GeorgSWeber created at 2009-03-27 20:19:56

Am I allowed to close this?


---

Comment by mabshoff created at 2009-03-27 20:37:41

Replying to [comment:3 GeorgSWeber]:

This is indeed a dupe of  #4354.

> Am I allowed to close this?

Nope, the release manager does that after verifying that it is a dupe. And I have to state that you are right, so closed as a dupe :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-27 20:37:41

Resolution: duplicate
