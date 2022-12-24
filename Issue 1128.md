# Issue 1128: Coercion of complex numbers

archive/issues_001128.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: ComplexField(200)(1) + RealField(100)(1)\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '+': 'Complex Field with 200 bits of precision' and 'Real Field with 100 bits of precision'\n```\n\nShould return an element of ComplexField(100)\n\nThis should be an easy fix, see \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/5bc6c9190a3da63e/597d0eb7a45dae11?lnk=gst&q=complexfield#597d0eb7a45dae11\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1128\n\n",
    "created_at": "2007-11-08T05:44:47Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "Coercion of complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1128",
    "user": "robertwb"
}
```
Assignee: somebody


```
sage: ComplexField(200)(1) + RealField(100)(1)
<type 'exceptions.TypeError'>: unsupported operand parent(s) for '+': 'Complex Field with 200 bits of precision' and 'Real Field with 100 bits of precision'
```

Should return an element of ComplexField(100)

This should be an easy fix, see 

http://groups.google.com/group/sage-devel/browse_thread/thread/5bc6c9190a3da63e/597d0eb7a45dae11?lnk=gst&q=complexfield#597d0eb7a45dae11



Issue created by migration from https://trac.sagemath.org/ticket/1128





---

archive/issue_comments_006819.json:
```json
{
    "body": "Changing assignee from somebody to roed.",
    "created_at": "2007-12-02T06:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6819",
    "user": "roed"
}
```

Changing assignee from somebody to roed.



---

archive/issue_comments_006820.json:
```json
{
    "body": "Attachment [trac1128.patch](tarball://root/attachments/some-uuid/ticket1128/trac1128.patch) by roed created at 2007-12-02 06:14:11\n\nAdds algebraic completion functor",
    "created_at": "2007-12-02T06:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6820",
    "user": "roed"
}
```

Attachment [trac1128.patch](tarball://root/attachments/some-uuid/ticket1128/trac1128.patch) by roed created at 2007-12-02 06:14:11

Adds algebraic completion functor



---

archive/issue_comments_006821.json:
```json
{
    "body": "cleaner patch",
    "created_at": "2007-12-02T07:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6821",
    "user": "robertwb"
}
```

cleaner patch



---

archive/issue_comments_006822.json:
```json
{
    "body": "Attachment [trac1128.2.patch](tarball://root/attachments/some-uuid/ticket1128/trac1128.2.patch) by robertwb created at 2007-12-02 07:31:01\n\nYep, works great.",
    "created_at": "2007-12-02T07:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6822",
    "user": "robertwb"
}
```

Attachment [trac1128.2.patch](tarball://root/attachments/some-uuid/ticket1128/trac1128.2.patch) by robertwb created at 2007-12-02 07:31:01

Yep, works great.



---

archive/issue_comments_006823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T08:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6823",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006824.json:
```json
{
    "body": "Merged in 2.8.15.alpha2. I did merge trac1128.2.patch.",
    "created_at": "2007-12-02T08:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1128#issuecomment-6824",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2. I did merge trac1128.2.patch.
