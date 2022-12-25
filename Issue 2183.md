# Issue 2183: scipy and special functions

archive/issues_002183.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nIn the thread \"[sage-support] Bessel argument order\"\nhttp://blog.gmane.org/gmane.comp.mathematics.sage.support/page=20\nMicheal suggested replacing all \"#random's\" by \"...\" and\nWilliam seconded this. Then William suggested adding the scip option to\nthe functions implemented. This has been done as well.\nThe patch passes \"sage -t\" has some examples added and some\ndocstring typos fixed. The patch is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2183\n\n",
    "created_at": "2008-02-16T23:14:55Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "scipy and special functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2183",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

CC:  @ncalexan

In the thread "[sage-support] Bessel argument order"
http://blog.gmane.org/gmane.comp.mathematics.sage.support/page=20
Micheal suggested replacing all "#random's" by "..." and
William seconded this. Then William suggested adding the scip option to
the functions implemented. This has been done as well.
The patch passes "sage -t" has some examples added and some
docstring typos fixed. The patch is attached.

Issue created by migration from https://trac.sagemath.org/ticket/2183





---

archive/issue_comments_014308.json:
```json
{
    "body": "Attachment [special_16-02-2008.hg](tarball://root/attachments/some-uuid/ticket2183/special_16-02-2008.hg) by @wdjoyner created at 2008-02-16 23:16:00",
    "created_at": "2008-02-16T23:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14308",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [special_16-02-2008.hg](tarball://root/attachments/some-uuid/ticket2183/special_16-02-2008.hg) by @wdjoyner created at 2008-02-16 23:16:00



---

archive/issue_comments_014309.json:
```json
{
    "body": "David,\n\nplease export a single patch next time since this is a single commit only. It makes review on the command line easier and in case of rejects makes it possible to edit the patch by hand.\n\nYou should also add an indicator like \"[with patch|bundle, needs review]\" so that people are aware that there is a patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T23:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David,

please export a single patch next time since this is a single commit only. It makes review on the command line easier and in case of rejects makes it possible to edit the patch by hand.

You should also add an indicator like "[with patch|bundle, needs review]" so that people are aware that there is a patch.

Cheers,

Michael



---

archive/issue_comments_014310.json:
```json
{
    "body": "There is also no reason not to still try to get this into 2.10.2, so for something as simple as this it is always recommended to assign against the current milestone.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T23:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14310",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is also no reason not to still try to get this into 2.10.2, so for something as simple as this it is always recommended to assign against the current milestone.

Cheers,

Michael



---

archive/issue_comments_014311.json:
```json
{
    "body": "There are some typos in the opening docstring.\n\nThe tests don't always make it clear that scipy agrees with the previous implementations, which is what I was looking for.\n\nI say apply.",
    "created_at": "2008-02-18T19:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14311",
    "user": "https://github.com/ncalexan"
}
```

There are some typos in the opening docstring.

The tests don't always make it clear that scipy agrees with the previous implementations, which is what I was looking for.

I say apply.



---

archive/issue_comments_014312.json:
```json
{
    "body": "I see two typos in the initial docstring and will fix those after I apply the bundle.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T20:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14312",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I see two typos in the initial docstring and will fix those after I apply the bundle.

Cheers,

Michael



---

archive/issue_comments_014313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002350.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-18T20:46:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2183#event-2350"
}
```



---

archive/issue_comments_014314.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
