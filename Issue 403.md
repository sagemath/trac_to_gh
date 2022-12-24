# Issue 403: polymake deadlocks from popen3 call

archive/issues_000403.json:
```json
{
    "body": "Assignee: was\n\nKeywords: polymake, polytope\n\nWhen doing large enough calculations, popen3 deadlocks in the cmd method of the Polytope class.  The attached patch fixes this by using the subprocess module instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/403\n\n",
    "created_at": "2007-07-12T11:43:48Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "polymake deadlocks from popen3 call",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/403",
    "user": "mhampton"
}
```
Assignee: was

Keywords: polymake, polytope

When doing large enough calculations, popen3 deadlocks in the cmd method of the Polytope class.  The attached patch fixes this by using the subprocess module instead.

Issue created by migration from https://trac.sagemath.org/ticket/403





---

archive/issue_comments_001978.json:
```json
{
    "body": "Attachment [polytope.patch](tarball://root/attachments/some-uuid/ticket403/polytope.patch) by mabshoff created at 2007-08-20 07:36:15",
    "created_at": "2007-08-20T07:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1978",
    "user": "mabshoff"
}
```

Attachment [polytope.patch](tarball://root/attachments/some-uuid/ticket403/polytope.patch) by mabshoff created at 2007-08-20 07:36:15



---

archive/issue_comments_001979.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-08-23T01:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1979",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_001980.json:
```json
{
    "body": "I changed the priority to minor because polymake is an optional package.",
    "created_at": "2007-08-23T01:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1980",
    "user": "was"
}
```

I changed the priority to minor because polymake is an optional package.



---

archive/issue_comments_001981.json:
```json
{
    "body": "This is applied now for sage-2.8.3.",
    "created_at": "2007-08-29T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1981",
    "user": "was"
}
```

This is applied now for sage-2.8.3.



---

archive/issue_comments_001982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/403#issuecomment-1982",
    "user": "was"
}
```

Resolution: fixed
