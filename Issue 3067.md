# Issue 3067: matrices:  numeric_array() is missing an import

archive/issues_003067.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis happens for all matrices:\n\n\n```\nsage: m = matrix([])\nsage: m.numeric_array()\n<type 'exceptions.ImportError'>: No module named Numeric\nsage: q= random_matrix(ZZ,2)\nsage: q.numeric_array()\n<type 'exceptions.ImportError'>: No module named Numeric\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3067\n\n",
    "created_at": "2008-04-30T15:23:45Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "matrices:  numeric_array() is missing an import",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3067",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

This happens for all matrices:


```
sage: m = matrix([])
sage: m.numeric_array()
<type 'exceptions.ImportError'>: No module named Numeric
sage: q= random_matrix(ZZ,2)
sage: q.numeric_array()
<type 'exceptions.ImportError'>: No module named Numeric
```


Issue created by migration from https://trac.sagemath.org/ticket/3067





---

archive/issue_comments_021124.json:
```json
{
    "body": "Attachment [3067.patch](tarball://root/attachments/some-uuid/ticket3067/3067.patch) by @dfdeshom created at 2008-04-30 18:54:00\n\nI deleted this function since it looks like sage doesn't use Numeric anymore. Or I could do a conditional import. Thoughts?",
    "created_at": "2008-04-30T18:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3067#issuecomment-21124",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [3067.patch](tarball://root/attachments/some-uuid/ticket3067/3067.patch) by @dfdeshom created at 2008-04-30 18:54:00

I deleted this function since it looks like sage doesn't use Numeric anymore. Or I could do a conditional import. Thoughts?



---

archive/issue_comments_021125.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3067#issuecomment-21125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003277.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-01T05:50:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3067",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3067#event-3277"
}
```



---

archive/issue_comments_021126.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3067#issuecomment-21126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
