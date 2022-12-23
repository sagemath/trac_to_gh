# Issue 2867: [witch patch, needs review] allow load_files parameter in __call__

Issue created by migration from https://trac.sagemath.org/ticket/2867

Original creator: yi

Original creation time: 2008-04-09 23:09:00

Assignee: yi

This patch allows you to do dsage('f = Foo()', load_files = ['foo.py']) which loads foo.py before executing the job. 


---

Comment by mabshoff created at 2008-04-10 01:29:39

Patch looks good to me. Positive review.

For the record: Please post proper mercurial patches in the future. I.e. use export instead of diff. I cannot tell the difference with patch preview and by the time I import the patch it is too late.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-10 01:59:36

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 01:59:36

Merged in Sage 3.0.alpha4


---

Attachment


---

Comment by mabshoff created at 2008-04-10 03:44:59

Oh, the irony that I didn't catch this doctest failure: Merged load_files.2.patch in Sage 3.0.alpha4.

Cheers,

Michael
