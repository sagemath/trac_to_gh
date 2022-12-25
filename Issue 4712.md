# Issue 4712: Make the doctest timeouts in Sage easily adjustable

archive/issues_004712.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a left over from #717. The fix here is to define some env variables that can be used to overwrite the default doctesting timeouts. Those are defined in sage-doctest right at the top:\n\n```\n# the default timeout for doctests: 6 minutes (in seconds)\nTIMEOUT      = 20\n# the timeout value for long doctests: 30 minutes (in seconds)\nTIMEOUT_LONG = 30 * 60\n# the timeout for doctests running under valgrind tools: unreasonably long\nTIMEOUT_VALGRIND = 1024*1024\n```\n\nCanonical names would be IMHO:\n\n```\nSAGE_TIMEOUT\nSAGE_TIMEOUT_LONG\nSAGE_TIMEOUT_VALGRIND\n```\n\nBonus points for running some performance counter once and then adjusting the timeout by some factor on slower machines.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4712\n\n",
    "created_at": "2008-12-05T06:49:41Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Make the doctest timeouts in Sage easily adjustable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is a left over from #717. The fix here is to define some env variables that can be used to overwrite the default doctesting timeouts. Those are defined in sage-doctest right at the top:

```
# the default timeout for doctests: 6 minutes (in seconds)
TIMEOUT      = 20
# the timeout value for long doctests: 30 minutes (in seconds)
TIMEOUT_LONG = 30 * 60
# the timeout for doctests running under valgrind tools: unreasonably long
TIMEOUT_VALGRIND = 1024*1024
```

Canonical names would be IMHO:

```
SAGE_TIMEOUT
SAGE_TIMEOUT_LONG
SAGE_TIMEOUT_VALGRIND
```

Bonus points for running some performance counter once and then adjusting the timeout by some factor on slower machines.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4712





---

archive/issue_comments_035457.json:
```json
{
    "body": "Here's a patch; apply to the scripts repository.\n\n(This doesn't earn the bonus points Michael referred to.)",
    "created_at": "2009-06-10T23:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4712#issuecomment-35457",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch; apply to the scripts repository.

(This doesn't earn the bonus points Michael referred to.)



---

archive/issue_comments_035458.json:
```json
{
    "body": "Attachment [trac_4712_scripts.patch](tarball://root/attachments/some-uuid/ticket4712/trac_4712_scripts.patch) by @ncalexan created at 2009-06-15 19:09:00\n\nFine by me.",
    "created_at": "2009-06-15T19:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4712#issuecomment-35458",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_4712_scripts.patch](tarball://root/attachments/some-uuid/ticket4712/trac_4712_scripts.patch) by @ncalexan created at 2009-06-15 19:09:00

Fine by me.



---

archive/issue_events_004957.json:
```json
{
    "actor": "boothby",
    "created_at": "2009-06-26T17:46:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4712",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4712#event-4957"
}
```



---

archive/issue_comments_035459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4712#issuecomment-35459",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed
