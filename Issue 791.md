# Issue 791: ugly absprec parameter in Polynomial constructor

archive/issues_000791.json:
```json
{
    "body": "Assignee: @williamstein\n\nI'm not happy with the profusion of code to deal with the absprec parameter in Polynomial-related code (for example, search for the string \"absprec\" in sage/rings/polynomial/polynomial_element.pyx). Something feels wrong with this design; the code keeps splitting into branches to deal with \"absprec\" or \"no absprec\" cases. I believe the \"absprec\" parameter has something to do with polynomials over p-adics. There has to be a cleaner way to deal with this issue. Please add comments below.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/791\n\n",
    "created_at": "2007-10-02T18:38:47Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "ugly absprec parameter in Polynomial constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/791",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

I'm not happy with the profusion of code to deal with the absprec parameter in Polynomial-related code (for example, search for the string "absprec" in sage/rings/polynomial/polynomial_element.pyx). Something feels wrong with this design; the code keeps splitting into branches to deal with "absprec" or "no absprec" cases. I believe the "absprec" parameter has something to do with polynomials over p-adics. There has to be a cleaner way to deal with this issue. Please add comments below.


Issue created by migration from https://trac.sagemath.org/ticket/791





---

archive/issue_comments_004740.json:
```json
{
    "body": "Changing assignee from @williamstein to somebody.",
    "created_at": "2007-10-04T19:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4740",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to somebody.



---

archive/issue_comments_004741.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-10-04T19:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4741",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_004742.json:
```json
{
    "body": "Attachment [791.patch](tarball://root/attachments/some-uuid/ticket791/791.patch) by @roed314 created at 2009-01-24 08:38:13",
    "created_at": "2009-01-24T08:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4742",
    "user": "https://github.com/roed314"
}
```

Attachment [791.patch](tarball://root/attachments/some-uuid/ticket791/791.patch) by @roed314 created at 2009-01-24 08:38:13



---

archive/issue_comments_004743.json:
```json
{
    "body": "rebase of previous patch against 3.3.alpha2",
    "created_at": "2009-01-27T06:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4743",
    "user": "https://github.com/aghitza"
}
```

rebase of previous patch against 3.3.alpha2



---

archive/issue_comments_004744.json:
```json
{
    "body": "Attachment [791_rebased.patch](tarball://root/attachments/some-uuid/ticket791/791_rebased.patch) by @aghitza created at 2009-01-27 06:04:38\n\nLooks good.  I have rebased the patch against 3.3.alpha2, since it got entangled in the whole Sage Days 12 flurry of activity.",
    "created_at": "2009-01-27T06:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4744",
    "user": "https://github.com/aghitza"
}
```

Attachment [791_rebased.patch](tarball://root/attachments/some-uuid/ticket791/791_rebased.patch) by @aghitza created at 2009-01-27 06:04:38

Looks good.  I have rebased the patch against 3.3.alpha2, since it got entangled in the whole Sage Days 12 flurry of activity.



---

archive/issue_comments_004745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T12:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004746.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-28T12:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3
