# Issue 9452: strip_automount_prefix() is useless

archive/issues_009452.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\n> We wrote the strip_automount_prefix() function for\n> sage-test to get around problems with automounted\n> file system having wierd mount points.\n> Unfotunately the strip_automount_prefix() does not\n> work at all!\n>\n> Here is a patch:\n>\n> % diff sage-test.old sage-test.new\n> 20c20\n> <     return strip_automount_prefix(os.path.abspath(x))\n> ---\n>>     return os.path.abspath(x)\n> 57c57\n> <         f = g[len(SAGE_ROOT)+1:]\n> ---\n>>         f = g[g.find(SAGE_ROOT)+len(SAGE_ROOT)+1:]\n> %\n>\n> You can remove - or deprecate - the function strip_automount_prefix().\n\nIssue created by migration from https://trac.sagemath.org/ticket/9452\n\n",
    "created_at": "2010-07-08T08:00:49Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "strip_automount_prefix() is useless",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9452",
    "user": "https://github.com/rlmill"
}
```
Assignee: tbd

CC:  @williamstein

> We wrote the strip_automount_prefix() function for
> sage-test to get around problems with automounted
> file system having wierd mount points.
> Unfotunately the strip_automount_prefix() does not
> work at all!
>
> Here is a patch:
>
> % diff sage-test.old sage-test.new
> 20c20
> <     return strip_automount_prefix(os.path.abspath(x))
> ---
>>     return os.path.abspath(x)
> 57c57
> <         f = g[len(SAGE_ROOT)+1:]
> ---
>>         f = g[g.find(SAGE_ROOT)+len(SAGE_ROOT)+1:]
> %
>
> You can remove - or deprecate - the function strip_automount_prefix().

Issue created by migration from https://trac.sagemath.org/ticket/9452





---

archive/issue_comments_090428.json:
```json
{
    "body": "Attachment [trac-9452-strip_automount_prefix.patch](tarball://root/attachments/some-uuid/ticket9452/trac-9452-strip_automount_prefix.patch) by @jasongrout created at 2011-02-23 23:28:03",
    "created_at": "2011-02-23T23:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90428",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9452-strip_automount_prefix.patch](tarball://root/attachments/some-uuid/ticket9452/trac-9452-strip_automount_prefix.patch) by @jasongrout created at 2011-02-23 23:28:03



---

archive/issue_comments_090429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-23T23:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90429",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090430.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-24T00:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90430",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023374.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-02-24T10:00:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9452#event-23374"
}
```



---

archive/issue_comments_090431.json:
```json
{
    "body": "What exactly is the problem that this patch is supposed to fix?  The description is very unclear...",
    "created_at": "2011-02-24T10:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90431",
    "user": "https://github.com/jdemeyer"
}
```

What exactly is the problem that this patch is supposed to fix?  The description is very unclear...



---

archive/issue_comments_090432.json:
```json
{
    "body": "This patch is undoing a mysterious \"fix\" from a long time ago, which was required on some obscure filesystem somewhere.",
    "created_at": "2011-02-24T17:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90432",
    "user": "https://github.com/williamstein"
}
```

This patch is undoing a mysterious "fix" from a long time ago, which was required on some obscure filesystem somewhere.



---

archive/issue_events_023375.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-08T09:16:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9452#event-23375"
}
```



---

archive/issue_events_023376.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-08T09:16:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "milestone": "sage-4.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9452#event-23376"
}
```



---

archive/issue_events_023377.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-08T21:45:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9452#event-23377"
}
```



---

archive/issue_comments_090433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-08T21:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90433",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
