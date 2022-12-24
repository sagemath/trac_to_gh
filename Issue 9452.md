# Issue 9452: strip_automount_prefix() is useless

archive/issues_009452.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\n> We wrote the strip_automount_prefix() function for\n> sage-test to get around problems with automounted\n> file system having wierd mount points.\n> Unfotunately the strip_automount_prefix() does not\n> work at all!\n>\n> Here is a patch:\n>\n> % diff sage-test.old sage-test.new\n> 20c20\n> <     return strip_automount_prefix(os.path.abspath(x))\n> ---\n>>     return os.path.abspath(x)\n> 57c57\n> <         f = g[len(SAGE_ROOT)+1:]\n> ---\n>>         f = g[g.find(SAGE_ROOT)+len(SAGE_ROOT)+1:]\n> %\n>\n> You can remove - or deprecate - the function strip_automount_prefix().\n\nIssue created by migration from https://trac.sagemath.org/ticket/9452\n\n",
    "created_at": "2010-07-08T08:00:49Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "strip_automount_prefix() is useless",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9452",
    "user": "rlm"
}
```
Assignee: tbd

CC:  was

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

archive/issue_comments_090577.json:
```json
{
    "body": "Attachment [trac-9452-strip_automount_prefix.patch](tarball://root/attachments/some-uuid/ticket9452/trac-9452-strip_automount_prefix.patch) by jason created at 2011-02-23 23:28:03",
    "created_at": "2011-02-23T23:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90577",
    "user": "jason"
}
```

Attachment [trac-9452-strip_automount_prefix.patch](tarball://root/attachments/some-uuid/ticket9452/trac-9452-strip_automount_prefix.patch) by jason created at 2011-02-23 23:28:03



---

archive/issue_comments_090578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-23T23:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90578",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090579.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-24T00:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90579",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090580.json:
```json
{
    "body": "What exactly is the problem that this patch is supposed to fix?  The description is very unclear...",
    "created_at": "2011-02-24T10:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90580",
    "user": "jdemeyer"
}
```

What exactly is the problem that this patch is supposed to fix?  The description is very unclear...



---

archive/issue_comments_090581.json:
```json
{
    "body": "This patch is undoing a mysterious \"fix\" from a long time ago, which was required on some obscure filesystem somewhere.",
    "created_at": "2011-02-24T17:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90581",
    "user": "was"
}
```

This patch is undoing a mysterious "fix" from a long time ago, which was required on some obscure filesystem somewhere.



---

archive/issue_comments_090582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-08T21:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9452#issuecomment-90582",
    "user": "jdemeyer"
}
```

Resolution: fixed
