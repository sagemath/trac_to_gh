# Issue 4972: matrix setitem should deal with slicing

archive/issues_004972.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following should work:\n\n\n```\na=matrix(QQ,3,[1,3,4,3,2,3,6,4,5])\na[1,:]=a[0,:]\n```\n\n\nInstead, I get an error:\n\n\n```\n          \t\n\nTraceback (click to the left for traceback)\n...\nTypeError: 'slice' object cannot be interpreted as an index\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/grout/.sage/sage_notebook/worksheets/admin/143/code/10.py\", line 7, in <module>\n    a[_sage_const_1 ,:]=a[_sage_const_0 ,:]\n  File \"/home/grout/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"matrix0.pyx\", line 798, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:4517)\nTypeError: 'slice' object cannot be interpreted as an index\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4972\n\n",
    "created_at": "2009-01-14T08:33:23Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "matrix setitem should deal with slicing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4972",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The following should work:


```
a=matrix(QQ,3,[1,3,4,3,2,3,6,4,5])
a[1,:]=a[0,:]
```


Instead, I get an error:


```
          	

Traceback (click to the left for traceback)
...
TypeError: 'slice' object cannot be interpreted as an index

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grout/.sage/sage_notebook/worksheets/admin/143/code/10.py", line 7, in <module>
    a[_sage_const_1 ,:]=a[_sage_const_0 ,:]
  File "/home/grout/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "matrix0.pyx", line 798, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:4517)
TypeError: 'slice' object cannot be interpreted as an index

```


Issue created by migration from https://trac.sagemath.org/ticket/4972





---

archive/issue_comments_037790.json:
```json
{
    "body": "To clarify, I think we should support setting a submatrix (and not just getting a submatrix) using slicing.  This will be consistent with numpy, matlab, octave, etc.",
    "created_at": "2009-01-14T08:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37790",
    "user": "https://github.com/jasongrout"
}
```

To clarify, I think we should support setting a submatrix (and not just getting a submatrix) using slicing.  This will be consistent with numpy, matlab, octave, etc.



---

archive/issue_comments_037791.json:
```json
{
    "body": "Now that #4973 is pretty much done, what we really should do is factor out the bulk of the setup code in getitem and use it for both setitem and getitem.",
    "created_at": "2009-01-16T02:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37791",
    "user": "https://github.com/jasongrout"
}
```

Now that #4973 is pretty much done, what we really should do is factor out the bulk of the setup code in getitem and use it for both setitem and getitem.



---

archive/issue_comments_037792.json:
```json
{
    "body": "See #2396, which should probably be closed when this is fixed.",
    "created_at": "2009-02-03T21:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37792",
    "user": "https://github.com/jasongrout"
}
```

See #2396, which should probably be closed when this is fixed.



---

archive/issue_comments_037793.json:
```json
{
    "body": "I'm making some changes.  I'll post an updated patch soon.",
    "created_at": "2009-02-04T21:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37793",
    "user": "https://github.com/jasongrout"
}
```

I'm making some changes.  I'll post an updated patch soon.



---

archive/issue_comments_037794.json:
```json
{
    "body": "ignore the .2.patch file.  I've refreshed the original .patch file.",
    "created_at": "2009-02-05T06:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37794",
    "user": "https://github.com/jasongrout"
}
```

ignore the .2.patch file.  I've refreshed the original .patch file.



---

archive/issue_comments_037795.json:
```json
{
    "body": "Attachment [trac_4972-matrix-setitem.patch](tarball://root/attachments/some-uuid/ticket4972/trac_4972-matrix-setitem.patch) by @jasongrout created at 2009-02-05 08:08:23\n\nRefreshed patch to fix some doctests.",
    "created_at": "2009-02-05T08:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37795",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4972-matrix-setitem.patch](tarball://root/attachments/some-uuid/ticket4972/trac_4972-matrix-setitem.patch) by @jasongrout created at 2009-02-05 08:08:23

Refreshed patch to fix some doctests.



---

archive/issue_comments_037796.json:
```json
{
    "body": "That's a lot of doctests; cool!  (Maybe some of them should be marked\nas TESTS:, in case we ever get around to having that mean something...)\n\n\n```\n            key -- any legal indexing (i.e., self[key] works)\n```\n\nfeels a little awkward... I had to read it twice to figure out what it\nmeant.  Maybe\n\n```\n            key -- any legal indexing (i.e., such that self[key] works)\n```\n\nwould be better?\n\nI think it's wrong that this works:\n\n```\nsage: M = matrix(3, 2, srange(6)); M[1] = 15; M\n```\n\nbut this raises an exception:\n\n```\nsage: M = matrix(3, 1, srange(3)); M[1] = 15; M\n```\n\n\nA lot of your variables should have type Py_ssize_t rather than int;\nyour current code will give very wrong results on matrices with more\nthan 2<sup>31</sup> rows or columns (which could happen on a 64-bit machine).\n\nOther than that, looks very nice!",
    "created_at": "2009-02-06T02:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37796",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

That's a lot of doctests; cool!  (Maybe some of them should be marked
as TESTS:, in case we ever get around to having that mean something...)


```
            key -- any legal indexing (i.e., self[key] works)
```

feels a little awkward... I had to read it twice to figure out what it
meant.  Maybe

```
            key -- any legal indexing (i.e., such that self[key] works)
```

would be better?

I think it's wrong that this works:

```
sage: M = matrix(3, 2, srange(6)); M[1] = 15; M
```

but this raises an exception:

```
sage: M = matrix(3, 1, srange(3)); M[1] = 15; M
```


A lot of your variables should have type Py_ssize_t rather than int;
your current code will give very wrong results on matrices with more
than 2<sup>31</sup> rows or columns (which could happen on a 64-bit machine).

Other than that, looks very nice!



---

archive/issue_comments_037797.json:
```json
{
    "body": "the fixups.patch addresses cwitty's concerns.  It should be applied on top of trac_4972-matrix-setitem.patch",
    "created_at": "2009-02-06T06:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37797",
    "user": "https://github.com/jasongrout"
}
```

the fixups.patch addresses cwitty's concerns.  It should be applied on top of trac_4972-matrix-setitem.patch



---

archive/issue_comments_037798.json:
```json
{
    "body": "Attachment [trac_4972-matrix-setitem-fixups.patch](tarball://root/attachments/some-uuid/ticket4972/trac_4972-matrix-setitem-fixups.patch) by @jasongrout created at 2009-02-06 06:28:43\n\ngrr, forgot to check the \"replace\" checkbox again.\n\nSo apply the following:\n\ntrac_4972-matrix-setitem.patch, then trac_4972-matrix-setitem-fixups.patch\n\nIgnore both .2.patch files.\n\nThis second refresh corrects some \"int\" cdefs in misc_c.pyx",
    "created_at": "2009-02-06T06:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37798",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4972-matrix-setitem-fixups.patch](tarball://root/attachments/some-uuid/ticket4972/trac_4972-matrix-setitem-fixups.patch) by @jasongrout created at 2009-02-06 06:28:43

grr, forgot to check the "replace" checkbox again.

So apply the following:

trac_4972-matrix-setitem.patch, then trac_4972-matrix-setitem-fixups.patch

Ignore both .2.patch files.

This second refresh corrects some "int" cdefs in misc_c.pyx



---

archive/issue_comments_037799.json:
```json
{
    "body": "Code looks good, all doctests pass.\n\nThanks for making the requested changes!\n\nPositive review; apply both patches.",
    "created_at": "2009-02-06T06:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37799",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, all doctests pass.

Thanks for making the requested changes!

Positive review; apply both patches.



---

archive/issue_events_005214.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-06T22:27:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4972#event-5214"
}
```



---

archive/issue_comments_037800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T22:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37800",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037801.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4972#issuecomment-37801",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha6.

Cheers,

Michael
