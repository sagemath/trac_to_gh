# Issue 403: polymake deadlocks from popen3 call

archive/issues_000403.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: polymake, polytope\n\nWhen doing large enough calculations, popen3 deadlocks in the cmd method of the Polytope class.  The attached patch fixes this by using the subprocess module instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/403\n\n",
    "created_at": "2007-07-12T11:43:48Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "polymake deadlocks from popen3 call",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

Keywords: polymake, polytope

When doing large enough calculations, popen3 deadlocks in the cmd method of the Polytope class.  The attached patch fixes this by using the subprocess module instead.

Issue created by migration from https://trac.sagemath.org/ticket/403





---

archive/issue_comments_001969.json:
```json
{
    "body": "Attachment [polytope.patch](tarball://root/attachments/some-uuid/ticket403/polytope.patch) by mabshoff created at 2007-08-20 07:36:15",
    "created_at": "2007-08-20T07:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1969",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [polytope.patch](tarball://root/attachments/some-uuid/ticket403/polytope.patch) by mabshoff created at 2007-08-20 07:36:15



---

archive/issue_comments_001970.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-08-23T01:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1970",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_001971.json:
```json
{
    "body": "I changed the priority to minor because polymake is an optional package.",
    "created_at": "2007-08-23T01:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1971",
    "user": "https://github.com/williamstein"
}
```

I changed the priority to minor because polymake is an optional package.



---

archive/issue_events_000429.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T01:55:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/403#event-429"
}
```



---

archive/issue_comments_001972.json:
```json
{
    "body": "This is applied now for sage-2.8.3.",
    "created_at": "2007-08-29T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1972",
    "user": "https://github.com/williamstein"
}
```

This is applied now for sage-2.8.3.



---

archive/issue_comments_001973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1973",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
