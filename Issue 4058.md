# Issue 4058: [with patch, needs review] move integer ring to the new coercion model

archive/issues_004058.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  alexghitza @malb\n\nA couple of bugfixes are included as well. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4058\n\n",
    "created_at": "2008-09-04T04:27:58Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] move integer ring to the new coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4058",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

CC:  alexghitza @malb

A couple of bugfixes are included as well. 

Issue created by migration from https://trac.sagemath.org/ticket/4058





---

archive/issue_comments_029193.json:
```json
{
    "body": "Attachment [4058-integer-coerce.patch](tarball://root/attachments/some-uuid/ticket4058/4058-integer-coerce.patch) by @robertwb created at 2008-09-04 04:28:33",
    "created_at": "2008-09-04T04:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29193",
    "user": "https://github.com/robertwb"
}
```

Attachment [4058-integer-coerce.patch](tarball://root/attachments/some-uuid/ticket4058/4058-integer-coerce.patch) by @robertwb created at 2008-09-04 04:28:33



---

archive/issue_comments_029194.json:
```json
{
    "body": "I'm getting an error trying to apply this patch to a fresh 3.1.2:\n\n\n```\npatching file sage/interfaces/expect.py\nHunk #1 FAILED at 1385\n1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/expect.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\n```\n",
    "created_at": "2008-09-20T04:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29194",
    "user": "https://github.com/aghitza"
}
```

I'm getting an error trying to apply this patch to a fresh 3.1.2:


```
patching file sage/interfaces/expect.py
Hunk #1 FAILED at 1385
1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/expect.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
```




---

archive/issue_comments_029195.json:
```json
{
    "body": "I'll rebase this as soon as I get 3.1.2.",
    "created_at": "2008-09-20T06:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29195",
    "user": "https://github.com/robertwb"
}
```

I'll rebase this as soon as I get 3.1.2.



---

archive/issue_comments_029196.json:
```json
{
    "body": "Attachment [4058-integer-coerce.2.patch](tarball://root/attachments/some-uuid/ticket4058/4058-integer-coerce.2.patch) by @robertwb created at 2008-09-23 19:00:07",
    "created_at": "2008-09-23T19:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29196",
    "user": "https://github.com/robertwb"
}
```

Attachment [4058-integer-coerce.2.patch](tarball://root/attachments/some-uuid/ticket4058/4058-integer-coerce.2.patch) by @robertwb created at 2008-09-23 19:00:07



---

archive/issue_comments_029197.json:
```json
{
    "body": "Refreshed the patch so it applies cleanly to 3.1.2.",
    "created_at": "2008-09-23T19:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29197",
    "user": "https://github.com/robertwb"
}
```

Refreshed the patch so it applies cleanly to 3.1.2.



---

archive/issue_comments_029198.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-24T02:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29198",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_029199.json:
```json
{
    "body": "One thing I notice with this patch is that sr.py now takes around 650 seconds instead of 450 or so:\n\n```\nsage -t -long devel/sage/sage/crypto/mq/sr.py\n         [655.1 s]\n```\n\nI am still merging the patch, but can we get this issue fixed next?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T04:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29199",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One thing I notice with this patch is that sr.py now takes around 650 seconds instead of 450 or so:

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
         [655.1 s]
```

I am still merging the patch, but can we get this issue fixed next?

Cheers,

Michael



---

archive/issue_events_009268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T04:22:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4058#event-9268"
}
```



---

archive/issue_comments_029200.json:
```json
{
    "body": "Merged 4058-integer-coerce.2.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T04:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4058-integer-coerce.2.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_029201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T04:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029202.json:
```json
{
    "body": "I will certainly look into that.",
    "created_at": "2008-09-24T05:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29202",
    "user": "https://github.com/robertwb"
}
```

I will certainly look into that.



---

archive/issue_comments_029203.json:
```json
{
    "body": "Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown.",
    "created_at": "2008-09-24T05:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29203",
    "user": "https://github.com/robertwb"
}
```

Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown.



---

archive/issue_comments_029204.json:
```json
{
    "body": "See #4186 for a fix.",
    "created_at": "2008-09-24T08:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29204",
    "user": "https://github.com/robertwb"
}
```

See #4186 for a fix.



---

archive/issue_comments_029205.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown. \n\nYeah, in that doctest we do some wacky coercion into some mv polynomial ring with a couple thousand variables, so this is really an interesting test case. This was first discussed at SD6 in Bristol, so it just shows how much the coercion re-re-write has been an interesting road :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T08:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4058#issuecomment-29205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:9 robertwb]:
> Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown. 

Yeah, in that doctest we do some wacky coercion into some mv polynomial ring with a couple thousand variables, so this is really an interesting test case. This was first discussed at SD6 in Bristol, so it just shows how much the coercion re-re-write has been an interesting road :)

Cheers,

Michael
