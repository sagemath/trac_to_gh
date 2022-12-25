# Issue 4494: conjugate method returns error on ZZ matrix

archive/issues_004494.json:
```json
{
    "body": "Assignee: tbd\n\nThis should be easy to fix:\n\n\n```\n\n\nsage:  a=random_matrix(ZZ,2)\nsage: a.conjugate()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/grout/jason/byu/papers/minrank-f2r3-laa/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.conjugate (sage/matrix/matrix2.c:24447)()\n\nAttributeError: 'sage.rings.integer.Integer' object has no attribute 'conjugate'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4494\n\n",
    "created_at": "2008-11-11T18:47:01Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "conjugate method returns error on ZZ matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4494",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

This should be easy to fix:


```


sage:  a=random_matrix(ZZ,2)
sage: a.conjugate()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/grout/jason/byu/papers/minrank-f2r3-laa/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.conjugate (sage/matrix/matrix2.c:24447)()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'conjugate'
```



Issue created by migration from https://trac.sagemath.org/ticket/4494





---

archive/issue_comments_033164.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2008-11-11T18:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33164",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_033165.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2008-11-11T18:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33165",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_comments_033166.json:
```json
{
    "body": "This is a problem with the Integer class, not with the matrix class.  The matrix code is:\n\nreturn self.new_matrix(self.nrows(), self.ncols(), [z.conjugate() for z in self.list()])\n\nThe problem is that the Integer class doesn't have a conjugate method.  Should it, or should the integer matrices override this definition?",
    "created_at": "2008-11-14T05:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33166",
    "user": "https://github.com/jasongrout"
}
```

This is a problem with the Integer class, not with the matrix class.  The matrix code is:

return self.new_matrix(self.nrows(), self.ncols(), [z.conjugate() for z in self.list()])

The problem is that the Integer class doesn't have a conjugate method.  Should it, or should the integer matrices override this definition?



---

archive/issue_comments_033167.json:
```json
{
    "body": "Changing component from linear algebra to algebra.",
    "created_at": "2008-11-14T05:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33167",
    "user": "https://github.com/jasongrout"
}
```

Changing component from linear algebra to algebra.



---

archive/issue_comments_033168.json:
```json
{
    "body": "Gee, apparently *I* was the one to change it to linear algebra.  Oops!",
    "created_at": "2008-11-14T05:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33168",
    "user": "https://github.com/jasongrout"
}
```

Gee, apparently *I* was the one to change it to linear algebra.  Oops!



---

archive/issue_comments_033169.json:
```json
{
    "body": "Changing assignee from @williamstein to tbd.",
    "created_at": "2008-11-14T05:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33169",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to tbd.



---

archive/issue_comments_033170.json:
```json
{
    "body": "I'm attaching a patch that implements trivial conjugate() methods for ZZ, QQ, and RR, and adds some doctests to the matrix conjugate method in matrix2.pyx.",
    "created_at": "2008-12-20T15:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33170",
    "user": "https://github.com/aghitza"
}
```

I'm attaching a patch that implements trivial conjugate() methods for ZZ, QQ, and RR, and adds some doctests to the matrix conjugate method in matrix2.pyx.



---

archive/issue_comments_033171.json:
```json
{
    "body": "Attachment [trac_4494.patch](tarball://root/attachments/some-uuid/ticket4494/trac_4494.patch) by @aghitza created at 2008-12-20 15:51:34",
    "created_at": "2008-12-20T15:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33171",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4494.patch](tarball://root/attachments/some-uuid/ticket4494/trac_4494.patch) by @aghitza created at 2008-12-20 15:51:34



---

archive/issue_comments_033172.json:
```json
{
    "body": "Great; I updated http://wiki.sagemath.org/LinearAlgebraSEP to reference this ticket.",
    "created_at": "2008-12-20T21:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33172",
    "user": "https://github.com/jasongrout"
}
```

Great; I updated http://wiki.sagemath.org/LinearAlgebraSEP to reference this ticket.



---

archive/issue_comments_033173.json:
```json
{
    "body": "Positive review.  The patch simply supplies the correct solution.  It applies cleanly to 3.2.2.  Tests in sage/matrix and sage/rings all pass.",
    "created_at": "2008-12-21T17:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33173",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  The patch simply supplies the correct solution.  It applies cleanly to 3.2.2.  Tests in sage/matrix and sage/rings all pass.



---

archive/issue_comments_033174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T22:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033175.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T22:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4494#issuecomment-33175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_events_004740.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T22:26:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4494",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4494#event-4740"
}
```
