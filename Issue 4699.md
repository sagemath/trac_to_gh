# Issue 4699: should be even more easier to change how many threads used for "make ptest" and friends

archive/issues_004699.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  gfurnish\n\nFrom http://trac.sagemath.org/sage_trac/ticket/4684#comment:5 :\n\n> This is already closed, but I want to comment that I would vastly prefer if \"make ptest\" were to by default just parse the MAKE environment variable, and if it is \"make -j6\", say, then use 6 threads. This is what \"sage -t\" does now. This way, I just set MAKE in my .bash_profile, and everything works right.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4699\n\n",
    "created_at": "2008-12-04T23:53:04Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "should be even more easier to change how many threads used for \"make ptest\" and friends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4699",
    "user": "ddrake"
}
```
Assignee: mabshoff

CC:  gfurnish

From http://trac.sagemath.org/sage_trac/ticket/4684#comment:5 :

> This is already closed, but I want to comment that I would vastly prefer if "make ptest" were to by default just parse the MAKE environment variable, and if it is "make -j6", say, then use 6 threads. This is what "sage -t" does now. This way, I just set MAKE in my .bash_profile, and everything works right.

Issue created by migration from https://trac.sagemath.org/ticket/4699





---

archive/issue_comments_035394.json:
```json
{
    "body": "...and, from http://trac.sagemath.org/sage_trac/ticket/4684#comment:6:\n> I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.",
    "created_at": "2008-12-04T23:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35394",
    "user": "ddrake"
}
```

...and, from http://trac.sagemath.org/sage_trac/ticket/4684#comment:6:
> I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.



---

archive/issue_comments_035395.json:
```json
{
    "body": "I renamed and changed the ticket description.\n\nCheers,\n\nMicheal",
    "created_at": "2008-12-05T00:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35395",
    "user": "mabshoff"
}
```

I renamed and changed the ticket description.

Cheers,

Micheal



---

archive/issue_comments_035396.json:
```json
{
    "body": "Also see #838 for something closely related that could be solved using pyprocessing by using an initialized sage session and then forking.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T04:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35396",
    "user": "mabshoff"
}
```

Also see #838 for something closely related that could be solved using pyprocessing by using an initialized sage session and then forking.

Cheers,

Michael



---

archive/issue_comments_035397.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35397",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035398.json:
```json
{
    "body": "Changing assignee from mabshoff to gfurnish.",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35398",
    "user": "gfurnish"
}
```

Changing assignee from mabshoff to gfurnish.



---

archive/issue_comments_035399.json:
```json
{
    "body": "This also fixes #4711",
    "created_at": "2008-12-10T19:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35399",
    "user": "gfurnish"
}
```

This also fixes #4711



---

archive/issue_comments_035400.json:
```json
{
    "body": "Oops:\n\n```\n(Stripping trailing CRs from patch.)\npatching file sage-ptest\nHunk #2 FAILED at 279.\nHunk #3 FAILED at 291.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T13:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35400",
    "user": "mabshoff"
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

archive/issue_comments_035401.json:
```json
{
    "body": "apply instead of other patches",
    "created_at": "2008-12-11T13:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35401",
    "user": "gfurnish"
}
```

apply instead of other patches



---

archive/issue_comments_035402.json:
```json
{
    "body": "Attachment [trac_4699_new_bin.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_new_bin.patch) by gfurnish created at 2008-12-11 13:14:20",
    "created_at": "2008-12-11T13:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35402",
    "user": "gfurnish"
}
```

Attachment [trac_4699_new_bin.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_new_bin.patch) by gfurnish created at 2008-12-11 13:14:20



---

archive/issue_comments_035403.json:
```json
{
    "body": "Attachment [trac_4699_fix.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_fix.patch) by gfurnish created at 2008-12-11 14:07:34",
    "created_at": "2008-12-11T14:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35403",
    "user": "gfurnish"
}
```

Attachment [trac_4699_fix.patch](tarball://root/attachments/some-uuid/ticket4699/trac_4699_fix.patch) by gfurnish created at 2008-12-11 14:07:34



---

archive/issue_comments_035404.json:
```json
{
    "body": "Nice work, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35404",
    "user": "mabshoff"
}
```

Nice work, positive review.

Cheers,

Michael



---

archive/issue_comments_035405.json:
```json
{
    "body": "Merged trac_4699_fix.patch and trac_4699_new_bin.patch in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35405",
    "user": "mabshoff"
}
```

Merged trac_4699_fix.patch and trac_4699_new_bin.patch in Sage 3.2.2.alpha2



---

archive/issue_comments_035406.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4699#issuecomment-35406",
    "user": "mabshoff"
}
```

Resolution: fixed
