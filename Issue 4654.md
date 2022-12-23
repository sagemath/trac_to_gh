# Issue 4654: [with patch, needs review] for 'sage -testall': put sage version in test log

Issue created by migration from https://trac.sagemath.org/ticket/4654

Original creator: jhpalmieri

Original creation time: 2008-11-29 16:42:31

Assignee: somebody

Keywords: doctest

Especially with the improved ability to upgrade sage versions in place (from #4638), when running `sage -testall` it seems helpful to record the sage version in the file SAGE_ROOT/tmp/test.log.  The attached patch does this.




---

Attachment

Yep, I agree that this is an excellent thing to do.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 16:57:53

Arrg, typo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 17:16:18

Sigh, I need to be awake when working :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 21:53:35

Resolution: fixed


---

Comment by mabshoff created at 2008-11-29 21:53:35

Merged in Sage 3.2.1.rc1
