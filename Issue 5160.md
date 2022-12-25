# Issue 5160: Change name of misc/sagex_ds.pyx

archive/issues_005160.json:
```json
{
    "body": "Assignee: tba\n\nSince #5094 is merged, I'll open this ticket.  It seems to be a worthwhile idea.  \n\nIt appears to only be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory to pull this off.  I'm putting this under \"documentation\" component because it's really just a nomenclature holdover.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5160\n\n",
    "created_at": "2009-02-02T18:58:33Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Change name of misc/sagex_ds.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5160",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tba

Since #5094 is merged, I'll open this ticket.  It seems to be a worthwhile idea.  

It appears to only be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory to pull this off.  I'm putting this under "documentation" component because it's really just a nomenclature holdover.

Issue created by migration from https://trac.sagemath.org/ticket/5160





---

archive/issue_comments_039474.json:
```json
{
    "body": "The deprecation policy might apply here.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T19:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The deprecation policy might apply here.

Cheers,

Michael



---

archive/issue_comments_039475.json:
```json
{
    "body": "Attachment [5160_rename_sagex_ds.patch](tarball://root/attachments/some-uuid/ticket5160/5160_rename_sagex_ds.patch) by @jdemeyer created at 2012-09-25 20:44:30",
    "created_at": "2012-09-25T20:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39475",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [5160_rename_sagex_ds.patch](tarball://root/attachments/some-uuid/ticket5160/5160_rename_sagex_ds.patch) by @jdemeyer created at 2012-09-25 20:44:30



---

archive/issue_comments_039476.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-25T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39476",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039477.json:
```json
{
    "body": "Changing type from task to enhancement.",
    "created_at": "2012-09-25T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39477",
    "user": "https://github.com/jdemeyer"
}
```

Changing type from task to enhancement.



---

archive/issue_comments_039478.json:
```json
{
    "body": "Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?  Who could we ask?",
    "created_at": "2012-09-25T20:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39478",
    "user": "https://github.com/kcrisman"
}
```

Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?  Who could we ask?



---

archive/issue_comments_039479.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?\n  \nI think it's unlikely, since it's barely used in Sage itself.  Besides, Sage code shouldn't be affected:\n\n```\nsage: BinaryTree()\n```\nshould work just as before.\n\nI don't even know how to deprecate a *module name* (as opposed to a function).",
    "created_at": "2012-09-25T20:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39479",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:3 kcrisman]:
> Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?
  
I think it's unlikely, since it's barely used in Sage itself.  Besides, Sage code shouldn't be affected:

```
sage: BinaryTree()
```
should work just as before.

I don't even know how to deprecate a *module name* (as opposed to a function).



---

archive/issue_comments_039480.json:
```json
{
    "body": "> I don't even know how to deprecate a *module name* (as opposed to a function).\n\nGood point, which is why I didn't do it before.\n\nThis looks good.  I guess at some point this was supposed to have a lot more than binary trees :)  Running irrelevant tests now, but the relevant ones were fine.  I'm getting some errors, but they seem unrelated - I'll look into it.",
    "created_at": "2012-09-26T01:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39480",
    "user": "https://github.com/kcrisman"
}
```

> I don't even know how to deprecate a *module name* (as opposed to a function).

Good point, which is why I didn't do it before.

This looks good.  I guess at some point this was supposed to have a lot more than binary trees :)  Running irrelevant tests now, but the relevant ones were fine.  I'm getting some errors, but they seem unrelated - I'll look into it.



---

archive/issue_comments_039481.json:
```json
{
    "body": "Yeah, they seem to be unrelated - weird, but I must have done something wrong.  They occurred with and without the patch.",
    "created_at": "2012-09-26T02:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39481",
    "user": "https://github.com/kcrisman"
}
```

Yeah, they seem to be unrelated - weird, but I must have done something wrong.  They occurred with and without the patch.



---

archive/issue_comments_039482.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-26T02:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39482",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-28T07:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39483",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_011955.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-28T07:46:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5160#event-11955"
}
```
