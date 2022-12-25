# Issue 4699: should be even more easier to change how many threads used for "make ptest" and friends

archive/issues_004699.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @garyfurnish\n\nFrom http://trac.sagemath.org/sage_trac/ticket/4684#comment:5 :\n\n> This is already closed, but I want to comment that I would vastly prefer if \"make ptest\" were to by default just parse the MAKE environment variable, and if it is \"make -j6\", say, then use 6 threads. This is what \"sage -t\" does now. This way, I just set MAKE in my .bash_profile, and everything works right.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4699\n\n",
    "created_at": "2008-12-04T23:53:04Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "should be even more easier to change how many threads used for \"make ptest\" and friends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4699",
    "user": "https://github.com/dandrake"
}
```
Assignee: mabshoff

CC:  @garyfurnish

From http://trac.sagemath.org/sage_trac/ticket/4684#comment:5 :

> This is already closed, but I want to comment that I would vastly prefer if "make ptest" were to by default just parse the MAKE environment variable, and if it is "make -j6", say, then use 6 threads. This is what "sage -t" does now. This way, I just set MAKE in my .bash_profile, and everything works right.

Issue created by migration from https://trac.sagemath.org/ticket/4699





---

archive/issue_comments_035325.json:
```json
{
    "body": "...and, from http://trac.sagemath.org/sage_trac/ticket/4684#comment:6:\n> I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.",
    "created_at": "2008-12-04T23:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35325",
    "user": "https://github.com/dandrake"
}
```

...and, from http://trac.sagemath.org/sage_trac/ticket/4684#comment:6:
> I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.



---

archive/issue_comments_035326.json:
```json
{
    "body": "I renamed and changed the ticket description.\n\nCheers,\n\nMicheal",
    "created_at": "2008-12-05T00:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35326",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I renamed and changed the ticket description.

Cheers,

Micheal



---

archive/issue_comments_035327.json:
```json
{
    "body": "Also see #838 for something closely related that could be solved using pyprocessing by using an initialized sage session and then forking.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T04:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35327",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Also see #838 for something closely related that could be solved using pyprocessing by using an initialized sage session and then forking.

Cheers,

Michael



---

archive/issue_comments_035328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35328",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035329.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35329",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_035330.json:
```json
{
    "body": "This also fixes #4711",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35330",
    "user": "https://github.com/garyfurnish"
}
```

This also fixes #4711



---

archive/issue_comments_035331.json:
```json
{
    "body": "Oops:\n\n```\n(Stripping trailing CRs from patch.)\npatching file sage-ptest\nHunk #2 FAILED at 279.\nHunk #3 FAILED at 291.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T13:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops:

```
(Stripping trailing CRs from patch.)
patching file sage-ptest
Hunk #2 FAILED at 279.
Hunk #3 FAILED at 291.
```


Cheers,

Michael



---

archive/issue_comments_035332.json:
```json
{
    "body": "apply instead of other patches",
    "created_at": "2008-12-11T13:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35332",
    "user": "https://github.com/garyfurnish"
}
```

apply instead of other patches



---

archive/issue_comments_035333.json:
```json
{
    "body": "Attachment [trac_4699_new_bin.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_new_bin.patch) by @garyfurnish created at 2008-12-11 13:14:20",
    "created_at": "2008-12-11T13:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35333",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4699_new_bin.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_new_bin.patch) by @garyfurnish created at 2008-12-11 13:14:20



---

archive/issue_comments_035334.json:
```json
{
    "body": "Attachment [trac_4699_fix.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_fix.patch) by @garyfurnish created at 2008-12-11 14:07:34",
    "created_at": "2008-12-11T14:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35334",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4699_fix.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_fix.patch) by @garyfurnish created at 2008-12-11 14:07:34



---

archive/issue_comments_035335.json:
```json
{
    "body": "Nice work, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice work, positive review.

Cheers,

Michael



---

archive/issue_comments_035336.json:
```json
{
    "body": "Merged trac_4699_fix.patch and trac_4699_new_bin.patch in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4699_fix.patch and trac_4699_new_bin.patch in Sage 3.2.2.alpha2



---

archive/issue_events_004944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-11T15:07:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4699#event-4944"
}
```



---

archive/issue_comments_035337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
