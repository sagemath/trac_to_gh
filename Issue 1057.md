# Issue 1057: Order elements do not have Z as a (proper) basering

archive/issues_001057.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: sage: K.<a> = NumberField(x^2 - 5)\nsage: sage: B = K.maximal_order().basis();\nsage: B[1].parent().base_ring() # this is bad\nRational Field\nsage: B[1].parent().base()\nInteger Ring\n```\n\n\nAlso, _rmul_, etc needs to be re-implemented. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1057\n\n",
    "created_at": "2007-11-01T21:14:29Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "title": "Order elements do not have Z as a (proper) basering",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1057",
    "user": "robertwb"
}
```
Assignee: was


```
sage: sage: K.<a> = NumberField(x^2 - 5)
sage: sage: B = K.maximal_order().basis();
sage: B[1].parent().base_ring() # this is bad
Rational Field
sage: B[1].parent().base()
Integer Ring
```


Also, _rmul_, etc needs to be re-implemented. 

Issue created by migration from https://trac.sagemath.org/ticket/1057





---

archive/issue_comments_006424.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-11-01T21:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6424",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_006425.json:
```json
{
    "body": "Attachment [1057-fix-order-basering.hg](tarball://root/attachments/some-uuid/ticket1057/1057-fix-order-basering.hg) by robertwb created at 2007-11-01 23:48:48\n\nOrders now have correct baserings. \n\nWhoever implemented the _base attribute might want to look at how it overrides the (cdef) ParentBase._base attribute, and the implications that might have. \n\nThis patch makes patch #1044 obsolete.",
    "created_at": "2007-11-01T23:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6425",
    "user": "robertwb"
}
```

Attachment [1057-fix-order-basering.hg](tarball://root/attachments/some-uuid/ticket1057/1057-fix-order-basering.hg) by robertwb created at 2007-11-01 23:48:48

Orders now have correct baserings. 

Whoever implemented the _base attribute might want to look at how it overrides the (cdef) ParentBase._base attribute, and the implications that might have. 

This patch makes patch #1044 obsolete.



---

archive/issue_comments_006426.json:
```json
{
    "body": "Changing assignee from robertwb to mabshoff.",
    "created_at": "2007-11-02T19:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6426",
    "user": "mabshoff"
}
```

Changing assignee from robertwb to mabshoff.



---

archive/issue_comments_006427.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-02T19:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6427",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006428.json:
```json
{
    "body": "applied to 2.8.11.rc2 after reverting #1044.",
    "created_at": "2007-11-02T19:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6428",
    "user": "mabshoff"
}
```

applied to 2.8.11.rc2 after reverting #1044.



---

archive/issue_comments_006429.json:
```json
{
    "body": "This is already fixed and in sage-2.8.11.",
    "created_at": "2007-11-03T14:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6429",
    "user": "was"
}
```

This is already fixed and in sage-2.8.11.



---

archive/issue_comments_006430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T14:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1057#issuecomment-6430",
    "user": "was"
}
```

Resolution: fixed
