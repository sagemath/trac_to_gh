# Issue 1795: [with-patch] Adds support for cdef'd and cpdef'd functions to sage-coverage

archive/issues_001795.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @jasongrout\n\nThe previous version of sage-coverage did not check cdef'd functions, and it incorrectly claimed that cpdef'd functions did not have doctests.  This patch fixes that problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1795\n\n",
    "created_at": "2008-01-16T18:06:01Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with-patch] Adds support for cdef'd and cpdef'd functions to sage-coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1795",
    "user": "@roed314"
}
```
Assignee: @roed314

CC:  @jasongrout

The previous version of sage-coverage did not check cdef'd functions, and it incorrectly claimed that cpdef'd functions did not have doctests.  This patch fixes that problem.

Issue created by migration from https://trac.sagemath.org/ticket/1795





---

archive/issue_comments_011362.json:
```json
{
    "body": "Attachment [cdef-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/cdef-coverage.patch) by @roed314 created at 2008-01-16 18:06:42\n\nAdds cdef, cpdef support to sage-coverage",
    "created_at": "2008-01-16T18:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11362",
    "user": "@roed314"
}
```

Attachment [cdef-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/cdef-coverage.patch) by @roed314 created at 2008-01-16 18:06:42

Adds cdef, cpdef support to sage-coverage



---

archive/issue_comments_011363.json:
```json
{
    "body": "At a quick glance it looks good.  Also I agree with the design decisions.  Does it work when run on all our codebase?",
    "created_at": "2008-01-16T18:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11363",
    "user": "@williamstein"
}
```

At a quick glance it looks good.  Also I agree with the design decisions.  Does it work when run on all our codebase?



---

archive/issue_comments_011364.json:
```json
{
    "body": "A minor fix to how Python classes are printed",
    "created_at": "2008-01-16T19:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11364",
    "user": "@roed314"
}
```

A minor fix to how Python classes are printed



---

archive/issue_comments_011365.json:
```json
{
    "body": "Attachment [class-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/class-coverage.patch) by @roed314 created at 2008-01-16 19:31:14\n\nIt gives reasonable output on sage -coverageall and gives reasonable output on a few selected files (integer.pyx, padic_capped_relative_element.pyx, graph.py).",
    "created_at": "2008-01-16T19:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11365",
    "user": "@roed314"
}
```

Attachment [class-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/class-coverage.patch) by @roed314 created at 2008-01-16 19:31:14

It gives reasonable output on sage -coverageall and gives reasonable output on a few selected files (integer.pyx, padic_capped_relative_element.pyx, graph.py).



---

archive/issue_comments_011366.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-19T07:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11366",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011367.json:
```json
{
    "body": "Changing assignee from @roed314 to @mwhansen.",
    "created_at": "2008-09-19T07:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11367",
    "user": "@mwhansen"
}
```

Changing assignee from @roed314 to @mwhansen.



---

archive/issue_comments_011368.json:
```json
{
    "body": "This no longer applies cleanly (against, e.g. 3.1.3)",
    "created_at": "2008-10-19T05:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11368",
    "user": "@robertwb"
}
```

This no longer applies cleanly (against, e.g. 3.1.3)



---

archive/issue_comments_011369.json:
```json
{
    "body": "Ok, we should get this rebased. I think that since we do not test cdef-ed functions those should not be accounted for.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T04:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11369",
    "user": "mabshoff"
}
```

Ok, we should get this rebased. I think that since we do not test cdef-ed functions those should not be accounted for.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_011370.json:
```json
{
    "body": "Fix the summary so it is picked up by the right reports.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T04:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11370",
    "user": "mabshoff"
}
```

Fix the summary so it is picked up by the right reports.

Cheers,

Michael



---

archive/issue_comments_011371.json:
```json
{
    "body": "The question I would like to see answered is: *should* we check `cdef` functions? We already check `cpdef` functions.",
    "created_at": "2013-03-07T08:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11371",
    "user": "@jdemeyer"
}
```

The question I would like to see answered is: *should* we check `cdef` functions? We already check `cpdef` functions.
