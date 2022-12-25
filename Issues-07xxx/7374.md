# Issue 7374: wrong docstring for is_isomorphic() in permgroup.py

archive/issues_007374.json:
```json
{
    "body": "Assignee: joyner\n\nThe docstring for `is_isomorphic()` for permutation groups claims \"If mode=\"verbose\" then an isomorphism is printed.\"\n\nHowever, that's not the case.  This is probably just left over from a previous version of the method.  In any case, the attached trivial patch removes this from the docstring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7374\n\n",
    "closed_at": "2009-11-04T14:46:33Z",
    "created_at": "2009-11-02T06:18:33Z",
    "labels": [
        "component: group theory",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "wrong docstring for is_isomorphic() in permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7374",
    "user": "https://github.com/aghitza"
}
```
Assignee: joyner

The docstring for `is_isomorphic()` for permutation groups claims "If mode="verbose" then an isomorphism is printed."

However, that's not the case.  This is probably just left over from a previous version of the method.  In any case, the attached trivial patch removes this from the docstring.

Issue created by migration from https://trac.sagemath.org/ticket/7374





---

archive/issue_comments_061661.json:
```json
{
    "body": "Attachment [trac_7374.patch](tarball://root/attachments/some-uuid/ticket7374/trac_7374.patch) by @aghitza created at 2009-11-02 06:20:31",
    "created_at": "2009-11-02T06:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61661",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7374.patch](tarball://root/attachments/some-uuid/ticket7374/trac_7374.patch) by @aghitza created at 2009-11-02 06:20:31



---

archive/issue_comments_061662.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-02T06:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61662",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061663.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-03T15:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61663",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_061664.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-03T15:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61664",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017436.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-04T14:46:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7374#event-17436"
}
```



---

archive/issue_comments_061665.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-04T14:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61665",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
