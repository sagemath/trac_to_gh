# Issue 1795: [with patch, needs work] Adds support for cdef'd functions to sage-coverage

archive/issues_001795.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jasongrout\n\nsage-coverage does not check cdef'd functions.  This patch fixes that problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1795\n\n",
    "created_at": "2008-01-16T18:06:01Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs work] Adds support for cdef'd functions to sage-coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1795",
    "user": "https://github.com/roed314"
}
```
Assignee: @mwhansen

CC:  @jasongrout

sage-coverage does not check cdef'd functions.  This patch fixes that problem.

Issue created by migration from https://trac.sagemath.org/ticket/1795





---

archive/issue_comments_011334.json:
```json
{
    "body": "Attachment [cdef-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/cdef-coverage.patch) by @roed314 created at 2008-01-16 18:06:42\n\nAdds cdef, cpdef support to sage-coverage",
    "created_at": "2008-01-16T18:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11334",
    "user": "https://github.com/roed314"
}
```

Attachment [cdef-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/cdef-coverage.patch) by @roed314 created at 2008-01-16 18:06:42

Adds cdef, cpdef support to sage-coverage



---

archive/issue_comments_011335.json:
```json
{
    "body": "At a quick glance it looks good.  Also I agree with the design decisions.  Does it work when run on all our codebase?",
    "created_at": "2008-01-16T18:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11335",
    "user": "https://github.com/williamstein"
}
```

At a quick glance it looks good.  Also I agree with the design decisions.  Does it work when run on all our codebase?



---

archive/issue_comments_011336.json:
```json
{
    "body": "A minor fix to how Python classes are printed",
    "created_at": "2008-01-16T19:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11336",
    "user": "https://github.com/roed314"
}
```

A minor fix to how Python classes are printed



---

archive/issue_comments_011337.json:
```json
{
    "body": "Attachment [class-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/class-coverage.patch) by @roed314 created at 2008-01-16 19:31:14\n\nIt gives reasonable output on sage -coverageall and gives reasonable output on a few selected files (integer.pyx, padic_capped_relative_element.pyx, graph.py).",
    "created_at": "2008-01-16T19:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11337",
    "user": "https://github.com/roed314"
}
```

Attachment [class-coverage.patch](tarball://root/attachments/some-uuid/ticket1795/class-coverage.patch) by @roed314 created at 2008-01-16 19:31:14

It gives reasonable output on sage -coverageall and gives reasonable output on a few selected files (integer.pyx, padic_capped_relative_element.pyx, graph.py).



---

archive/issue_events_004385.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:08:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4385"
}
```



---

archive/issue_comments_011338.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-19T07:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11338",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011339.json:
```json
{
    "body": "Changing assignee from @roed314 to @mwhansen.",
    "created_at": "2008-09-19T07:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11339",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @roed314 to @mwhansen.



---

archive/issue_comments_011340.json:
```json
{
    "body": "This no longer applies cleanly (against, e.g. 3.1.3)",
    "created_at": "2008-10-19T05:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11340",
    "user": "https://github.com/robertwb"
}
```

This no longer applies cleanly (against, e.g. 3.1.3)



---

archive/issue_comments_011341.json:
```json
{
    "body": "Ok, we should get this rebased. I think that since we do not test cdef-ed functions those should not be accounted for.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T04:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11341",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, we should get this rebased. I think that since we do not test cdef-ed functions those should not be accounted for.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_011342.json:
```json
{
    "body": "Fix the summary so it is picked up by the right reports.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T04:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fix the summary so it is picked up by the right reports.

Cheers,

Michael



---

archive/issue_comments_011343.json:
```json
{
    "body": "The question I would like to see answered is: *should* we check `cdef` functions? We already check `cpdef` functions.",
    "created_at": "2013-03-07T08:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1795#issuecomment-11343",
    "user": "https://github.com/jdemeyer"
}
```

The question I would like to see answered is: *should* we check `cdef` functions? We already check `cpdef` functions.



---

archive/issue_events_004386.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4386"
}
```



---

archive/issue_events_004387.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4387"
}
```



---

archive/issue_events_004388.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4388"
}
```



---

archive/issue_events_004389.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4389"
}
```



---

archive/issue_events_004390.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4390"
}
```



---

archive/issue_events_004391.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4391"
}
```



---

archive/issue_events_004392.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4392"
}
```



---

archive/issue_events_004393.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1795",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1795#event-4393"
}
```
