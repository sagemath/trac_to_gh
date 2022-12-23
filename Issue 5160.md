# Issue 5160: Change name of misc/sagex_ds.pyx

archive/issues_005160.json:
```json
{
    "body": "Assignee: tba\n\nSince #5094 is merged, I'll open this ticket.  It seems to be a worthwhile idea.  \n\nIt appears to only be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory to pull this off.  I'm putting this under \"documentation\" component because it's really just a nomenclature holdover.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5160\n\n",
    "created_at": "2009-02-02T18:58:33Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Change name of misc/sagex_ds.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5160",
    "user": "kcrisman"
}
```
Assignee: tba

Since #5094 is merged, I'll open this ticket.  It seems to be a worthwhile idea.  

It appears to only be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory to pull this off.  I'm putting this under "documentation" component because it's really just a nomenclature holdover.

Issue created by migration from https://trac.sagemath.org/ticket/5160





---

archive/issue_comments_039550.json:
```json
{
    "body": "The deprecation policy might apply here.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T19:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39550",
    "user": "mabshoff"
}
```

The deprecation policy might apply here.

Cheers,

Michael



---

archive/issue_comments_039551.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-09-25T20:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39551",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_039552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-25T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39552",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039553.json:
```json
{
    "body": "Changing type from task to enhancement.",
    "created_at": "2012-09-25T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39553",
    "user": "jdemeyer"
}
```

Changing type from task to enhancement.



---

archive/issue_comments_039554.json:
```json
{
    "body": "Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?  Who could we ask?",
    "created_at": "2012-09-25T20:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39554",
    "user": "kcrisman"
}
```

Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?  Who could we ask?



---

archive/issue_comments_039555.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?\nI think it's unlikely, since it's barely used in Sage itself.  Besides, Sage code shouldn't be affected:\n\n```\nsage: BinaryTree()\n```\n\nshould work just as before.\n\nI don't even know how to deprecate a *module name* (as opposed to a function).",
    "created_at": "2012-09-25T20:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39555",
    "user": "jdemeyer"
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

archive/issue_comments_039556.json:
```json
{
    "body": "> I don't even know how to deprecate a *module name* (as opposed to a function).\nGood point, which is why I didn't do it before.\n\nThis looks good.  I guess at some point this was supposed to have a lot more than binary trees :)  Running irrelevant tests now, but the relevant ones were fine.  I'm getting some errors, but they seem unrelated - I'll look into it.",
    "created_at": "2012-09-26T01:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39556",
    "user": "kcrisman"
}
```

> I don't even know how to deprecate a *module name* (as opposed to a function).
Good point, which is why I didn't do it before.

This looks good.  I guess at some point this was supposed to have a lot more than binary trees :)  Running irrelevant tests now, but the relevant ones were fine.  I'm getting some errors, but they seem unrelated - I'll look into it.



---

archive/issue_comments_039557.json:
```json
{
    "body": "Yeah, they seem to be unrelated - weird, but I must have done something wrong.  They occurred with and without the patch.",
    "created_at": "2012-09-26T02:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39557",
    "user": "kcrisman"
}
```

Yeah, they seem to be unrelated - weird, but I must have done something wrong.  They occurred with and without the patch.



---

archive/issue_comments_039558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-26T02:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39558",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039559.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-28T07:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5160#issuecomment-39559",
    "user": "jdemeyer"
}
```

Resolution: fixed
