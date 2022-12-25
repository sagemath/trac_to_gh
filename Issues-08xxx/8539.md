# Issue 8539: Matrix(ZZ, sparse=True)._mod_int(p) has the wrong parent

archive/issues_008539.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @williamstein\n\n```\nsage: M = Matrix(ZZ, 300, 300, sparse=True)\nsage: B = M._mod_int(7)\nsage: B\n300 x 300 sparse matrix over Ring of integers modulo 7 (type 'print B.str()' to see all of the entries)\nsage: B.parent()\nFull MatrixSpace of 300 by 300 dense matrices over Ring of integers modulo 7\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8539\n\n",
    "closed_at": "2010-03-29T22:08:01Z",
    "created_at": "2010-03-15T04:01:18Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.5",
    "title": "Matrix(ZZ, sparse=True)._mod_int(p) has the wrong parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8539",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  @robertwb @williamstein

```
sage: M = Matrix(ZZ, 300, 300, sparse=True)
sage: B = M._mod_int(7)
sage: B
300 x 300 sparse matrix over Ring of integers modulo 7 (type 'print B.str()' to see all of the entries)
sage: B.parent()
Full MatrixSpace of 300 by 300 dense matrices over Ring of integers modulo 7
```

Issue created by migration from https://trac.sagemath.org/ticket/8539





---

archive/issue_comments_077062.json:
```json
{
    "body": "Changing component from elliptic curves to linear algebra.",
    "created_at": "2010-03-15T23:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77062",
    "user": "https://github.com/rlmill"
}
```

Changing component from elliptic curves to linear algebra.



---

archive/issue_comments_077063.json:
```json
{
    "body": "Changing assignee from @JohnCremona to @williamstein.",
    "created_at": "2010-03-15T23:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77063",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @JohnCremona to @williamstein.



---

archive/issue_comments_077064.json:
```json
{
    "body": "Attachment [trac_8539.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539.patch) by @rlmill created at 2010-03-15 23:42:25",
    "created_at": "2010-03-15T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77064",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8539.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539.patch) by @rlmill created at 2010-03-15 23:42:25



---

archive/issue_comments_077065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-15T23:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77065",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077066.json:
```json
{
    "body": "I'm not sure if using dense matrices here was an oversight, or if there was a reason for it...\n\nhttp://hg.sagemath.org/sage-main/annotate/8df7435d1864/sage/matrix/matrix_integer_sparse.pyx#241",
    "created_at": "2010-03-16T00:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77066",
    "user": "https://github.com/robertwb"
}
```

I'm not sure if using dense matrices here was an oversight, or if there was a reason for it...

http://hg.sagemath.org/sage-main/annotate/8df7435d1864/sage/matrix/matrix_integer_sparse.pyx#241



---

archive/issue_comments_077067.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-26T21:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77067",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077068.json:
```json
{
    "body": "Enthusiastic positive review!!!!!!!!!! \n\nThis totally rocks, leading to massive speedups in modular symbols (susprisingly).",
    "created_at": "2010-03-26T22:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77068",
    "user": "https://github.com/williamstein"
}
```

Enthusiastic positive review!!!!!!!!!! 

This totally rocks, leading to massive speedups in modular symbols (susprisingly).



---

archive/issue_comments_077069.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-26T22:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77069",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_077070.json:
```json
{
    "body": "this is a referee patch that fixes a doctest (which was wrong).",
    "created_at": "2010-03-27T01:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77070",
    "user": "https://github.com/williamstein"
}
```

this is a referee patch that fixes a doctest (which was wrong).



---

archive/issue_comments_077071.json:
```json
{
    "body": "Attachment [trac_8539-part2.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539-part2.patch) by @williamstein created at 2010-03-29 22:08:01\n\nMerged into sage-4.3.5",
    "created_at": "2010-03-29T22:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77071",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8539-part2.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539-part2.patch) by @williamstein created at 2010-03-29 22:08:01

Merged into sage-4.3.5



---

archive/issue_comments_077072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-29T22:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77072",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_020580.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-03-29T22:08:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8539#event-20580"
}
```



---

archive/issue_events_020581.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-30T12:10:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "milestone": "sage-4.3.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8539#event-20581"
}
```
