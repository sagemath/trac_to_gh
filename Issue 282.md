# Issue 282: [with patch] add matrix() class to FiniteFields and FiniteField extensions

archive/issues_000282.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: finitefield extension matrix polynomial\n\nNumberFields support a matrix() class, very handy.  FiniteFields and FiniteField extensions should also support such a beast.  In fact, all algebraic extensions should provide such functionality, but at this time there is no generic AlgebraicExtension class in which to put such functionality.  Damn you, Pyrex and multiple inheritance!\n\nIssue created by migration from https://trac.sagemath.org/ticket/282\n\n",
    "closed_at": "2007-10-23T19:51:22Z",
    "created_at": "2007-02-23T20:02:37Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] add matrix() class to FiniteFields and FiniteField extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/282",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

Keywords: finitefield extension matrix polynomial

NumberFields support a matrix() class, very handy.  FiniteFields and FiniteField extensions should also support such a beast.  In fact, all algebraic extensions should provide such functionality, but at this time there is no generic AlgebraicExtension class in which to put such functionality.  Damn you, Pyrex and multiple inheritance!

Issue created by migration from https://trac.sagemath.org/ticket/282





---

archive/issue_comments_001336.json:
```json
{
    "body": "I don't understand what you're talking about, what you want, or why this is a defect and not\nan enhancement.  Please clarify this trac issue.",
    "created_at": "2007-02-24T02:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1336",
    "user": "https://github.com/williamstein"
}
```

I don't understand what you're talking about, what you want, or why this is a defect and not
an enhancement.  Please clarify this trac issue.



---

archive/issue_comments_001337.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-18T12:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1337",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001338.json:
```json
{
    "body": "Changing assignee from somebody to @malb.",
    "created_at": "2007-09-18T12:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1338",
    "user": "https://github.com/malb"
}
```

Changing assignee from somebody to @malb.



---

archive/issue_comments_001339.json:
```json
{
    "body": "This ticket means that the method matrix() which is described as: \"The matrix of right multiplication by the element on the power basis $1, x, x^2, \\ldots, x^{d-1}$ for the number field.  Thus the {\\em rows} of this matrix give the images of each of the $x^i$.\" should be added to finite extension fields. Also, (my addition) the method vector() of GFq should proably be added to number field elements.",
    "created_at": "2007-09-18T12:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1339",
    "user": "https://github.com/malb"
}
```

This ticket means that the method matrix() which is described as: "The matrix of right multiplication by the element on the power basis $1, x, x^2, \ldots, x^{d-1}$ for the number field.  Thus the {\em rows} of this matrix give the images of each of the $x^i$." should be added to finite extension fields. Also, (my addition) the method vector() of GFq should proably be added to number field elements.



---

archive/issue_events_000634.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-09-18T12:43:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/282#event-634"
}
```



---

archive/issue_comments_001340.json:
```json
{
    "body": "Attachment [K_matrix.patch](tarball://root/attachments/some-uuid/ticket282/K_matrix.patch) by @malb created at 2007-10-20 22:46:32",
    "created_at": "2007-10-20T22:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1340",
    "user": "https://github.com/malb"
}
```

Attachment [K_matrix.patch](tarball://root/attachments/some-uuid/ticket282/K_matrix.patch) by @malb created at 2007-10-20 22:46:32



---

archive/issue_comments_001341.json:
```json
{
    "body": "The attached patch implements this.",
    "created_at": "2007-10-20T22:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1341",
    "user": "https://github.com/malb"
}
```

The attached patch implements this.



---

archive/issue_comments_001342.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-10-20T22:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1342",
    "user": "https://github.com/malb"
}
```

Changing status from assigned to new.



---

archive/issue_events_000635.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-21T22:40:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/282#event-635"
}
```



---

archive/issue_events_000636.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-21T22:40:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/282#event-636"
}
```



---

archive/issue_comments_001343.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1343",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_events_000637.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T19:51:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/282#event-637"
}
```



---

archive/issue_comments_001344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T19:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1344",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_001345.json:
```json
{
    "body": "applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T19:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/282#issuecomment-1345",
    "user": "https://github.com/malb"
}
```

applied to 2.8.9.alpha0
