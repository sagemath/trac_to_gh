# Issue 4791: [with patch, needs review] purge nodoctest.py from the Sage library tree

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-14 07:22:12

Assignee: mabshoff

We should doctest every possible file and not put up with any nodoctest.py crap. This keeps certain files from getting doctested, i.e.

```
sage -t -long devel/sage/sage/dsage/server/stats.py
         [2.3 s]
sage -t -long devel/sage/sage/dsage/server/tests/test_server.py
         [2.6 s]
sage -t -long devel/sage/sage/dsage/twisted/tests/test_pubkeyauth.py
         [2.4 s]
sage -t -long devel/sage/sage/dsage/twisted/tests/test_remote.py
         [2.5 s]
sage -t -long devel/sage/sage/dsage/twisted/pubkeyauth.py
         [2.6 s]
sage -t -long devel/sage/sage/dsage/twisted/pb.py
         [2.7 s]
sage -t -long devel/sage/sage/server/notebook/sage_email.py
         [2.5 s]
sage -t -long devel/sage/sage/quadratic_forms/genera/genus.py
         [2.7 s]
```

The following files are removed by this patch:

```
sage/dsage/database/tests/nodoctest.py
sage/dsage/database/nodoctest.py
sage/dsage/errors/nodoctest.py
sage/dsage/misc/nodoctest.py
sage/dsage/scripts/nodoctest.py
sage/dsage/server/tests/nodoctest.py
sage/dsage/server/nodoctest.py
sage/dsage/twisted/tests/nodoctest.py
sage/dsage/twisted/nodoctest.py
sage/dsage/nodoctest.py
sage/quadratic_forms/genera/nodoctest.py
sage/server/notebook/compress/nodoctest.py
```

With my current merge tree -t -long passes.

Cheers,

Michael


---

Attachment

This is a git style patch


---

Comment by craigcitro created at 2008-12-14 08:12:31

Yep, I agree that we should remove all these `nodoctest.py` files. Anything that pops up should get turned up by the next alpha/rc ...


---

Comment by mabshoff created at 2008-12-14 08:15:15

Merged in Sage 3.2.2.rc0


---

Comment by mabshoff created at 2008-12-14 08:15:15

Resolution: fixed
