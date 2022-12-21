# Issue 2866: [with patch, needs review] use tempfile.NamedTemporaryFile for unit tests

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-04-09 23:05:27

Assignee: yi

Switch from using hard coded 'test.db' to use the tempfile module's NamedTemporaryFile().


---

Comment by yi created at 2008-04-09 23:54:36

William reviewed it looking over my shoulder =)


---

Comment by mabshoff created at 2008-04-10 00:34:00

I like this patch, but it doesn't pass doctests:

```
sage -t -long devel/sage/sage/dsage/tests/testdoc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/tmp/testdoc.py", line 6:
    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=Integer(3))###line 6:
    sage: dsage.server(blocking=False, port=port, verbose=False, ssl=False, log_level=3)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/dsage/dsage.py", line 228, in server
        db_file = test_db.name
    NameError: global name 'test_db' is not defined
```

Repeat after me: *No positive review without at least minimal doctesting* ;)

Cheers,

Michael


---

Attachment

Thanks for catching this, I updated the patch, it was a one liner blunder! Could you please reapply, should pass doctests now on sage.math at least :-)


---

Comment by mabshoff created at 2008-04-10 03:14:03

The updated patch fixes the issue and is also a proper Mercurial patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-10 03:14:16

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 03:14:16

Merged in Sage 3.0.alpha4
