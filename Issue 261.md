# Issue 261: a new matrix constructor

archive/issues_000261.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nKyle Schalm suggests:\n\n```\n \n \nhere is a matrix constructor i would like to see:\n \nMatrix(M, N, f):\n   for i in range(1,M+1):\n     for j in range(1,N+1):\n       self[i][j] = f(i,j)   # or whatever the syntax is\n \n \ni might use it like this:\n \nA = Matrix(3, 3, lambda i,j: i+j)\n \ni'd do it myself, but i don't have a development environment set up,\nand don't wanna do that right now.\n \ncheers,\nkyle\n \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/261\n\n",
    "created_at": "2007-02-14T06:49:52Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "a new matrix constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/261",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @jasongrout

Kyle Schalm suggests:

```
 
 
here is a matrix constructor i would like to see:
 
Matrix(M, N, f):
   for i in range(1,M+1):
     for j in range(1,N+1):
       self[i][j] = f(i,j)   # or whatever the syntax is
 
 
i might use it like this:
 
A = Matrix(3, 3, lambda i,j: i+j)
 
i'd do it myself, but i don't have a development environment set up,
and don't wanna do that right now.
 
cheers,
kyle
 
```


Issue created by migration from https://trac.sagemath.org/ticket/261





---

archive/issue_comments_001228.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-08-31T06:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_001229.json:
```json
{
    "body": "Changing assignee from @mwhansen to @jasongrout.",
    "created_at": "2008-11-14T06:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1229",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @mwhansen to @jasongrout.



---

archive/issue_comments_001230.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-14T06:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1230",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001231.json:
```json
{
    "body": "Remove assignee @jasongrout.",
    "created_at": "2009-11-19T22:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1231",
    "user": "https://github.com/jasongrout"
}
```

Remove assignee @jasongrout.



---

archive/issue_comments_001232.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-16T06:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1232",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001233.json:
```json
{
    "body": "Attachment [trac_261.patch](tarball://root/attachments/some-uuid/ticket261/trac_261.patch) by AlecMihailovs created at 2010-03-20 20:47:35\n\nOn my system seems to be working fine. A light cosmetic suggestion for the patch - I would use 'import numpy' only once, at the very beginning. \n\nA desirable thing is to adjust 'vector' correspondingly - both vorking as 'vector(3,f)' and 'vector(v)' for a 1-dimensional numpy array v with dtype=int, dtype=object or any other dtype, which possible currently to do as 'vector(list(v))'. I'll try to add this as a ticket later (when I'll have more time) if it won't be created earlier.\n\nAlec Mihailovs",
    "created_at": "2010-03-20T20:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1233",
    "user": "https://trac.sagemath.org/admin/accounts/users/AlecMihailovs"
}
```

Attachment [trac_261.patch](tarball://root/attachments/some-uuid/ticket261/trac_261.patch) by AlecMihailovs created at 2010-03-20 20:47:35

On my system seems to be working fine. A light cosmetic suggestion for the patch - I would use 'import numpy' only once, at the very beginning. 

A desirable thing is to adjust 'vector' correspondingly - both vorking as 'vector(3,f)' and 'vector(v)' for a 1-dimensional numpy array v with dtype=int, dtype=object or any other dtype, which possible currently to do as 'vector(list(v))'. I'll try to add this as a ticket later (when I'll have more time) if it won't be created earlier.

Alec Mihailovs



---

archive/issue_comments_001234.json:
```json
{
    "body": "This patch includes not only this enhancement, but also fixes a bug for matrix(v) with v being a 1x1 numpy array, which currently produces a n x n zero matrix for v being a 1x1 numpy array with one element n. So it should be, perhaps, marked not only as an enhancement, but also as a defect. \n\nAlec Mihailovs",
    "created_at": "2010-03-20T21:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1234",
    "user": "https://trac.sagemath.org/admin/accounts/users/AlecMihailovs"
}
```

This patch includes not only this enhancement, but also fixes a bug for matrix(v) with v being a 1x1 numpy array, which currently produces a n x n zero matrix for v being a 1x1 numpy array with one element n. So it should be, perhaps, marked not only as an enhancement, but also as a defect. 

Alec Mihailovs



---

archive/issue_comments_001235.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-20T22:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1235",
    "user": "https://trac.sagemath.org/admin/accounts/users/AlecMihailovs"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001236.json:
```json
{
    "body": "I get a doctest failure with this.  I'm attaching a trivial patch to fix it.",
    "created_at": "2010-04-14T20:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1236",
    "user": "https://github.com/jhpalmieri"
}
```

I get a doctest failure with this.  I'm attaching a trivial patch to fix it.



---

archive/issue_comments_001237.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2010-04-14T20:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1237",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_001238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1238",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_001239.json:
```json
{
    "body": "Attachment [trac_261-trivial.patch](tarball://root/attachments/some-uuid/ticket261/trac_261-trivial.patch) by @jhpalmieri created at 2010-04-15 05:18:48\n\nMerged both patches in 4.4.alpha0.",
    "created_at": "2010-04-15T05:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/261#issuecomment-1239",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_261-trivial.patch](tarball://root/attachments/some-uuid/ticket261/trac_261-trivial.patch) by @jhpalmieri created at 2010-04-15 05:18:48

Merged both patches in 4.4.alpha0.
