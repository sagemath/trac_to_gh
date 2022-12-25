# Issue 4541: kschur functions don't properly convert to schur's

archive/issues_004541.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: symmetric functions, kschur\n\nExample:\n\n\n```\nsage: ks3 = kSchurFunctions(QQ,3)\nsage: s = SFASchur(ks3.base_ring())\nsage: s(ks3(s([1,1,1,1])))\ns[1, 1, 1, 1] + t^3*s[4]\n```\n\n\nIn general, s(ks3(foo)) returns the_right_thing + bad_stuff  where bad_stuff is a sum of Schur functions with first part larger than 3.  Possibly, this is because the ks3->s conversion doesn't understand that the kschur's do not form a basis for all symmetric functions; only for the span of schur functions with first part <= k.  I will look more at this and see if I can't put up a patch, but assistance is very welcome!\n\nIssue created by migration from https://trac.sagemath.org/ticket/4541\n\n",
    "created_at": "2008-11-17T20:01:47Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "kschur functions don't properly convert to schur's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4541",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: symmetric functions, kschur

Example:


```
sage: ks3 = kSchurFunctions(QQ,3)
sage: s = SFASchur(ks3.base_ring())
sage: s(ks3(s([1,1,1,1])))
s[1, 1, 1, 1] + t^3*s[4]
```


In general, s(ks3(foo)) returns the_right_thing + bad_stuff  where bad_stuff is a sum of Schur functions with first part larger than 3.  Possibly, this is because the ks3->s conversion doesn't understand that the kschur's do not form a basis for all symmetric functions; only for the span of schur functions with first part <= k.  I will look more at this and see if I can't put up a patch, but assistance is very welcome!

Issue created by migration from https://trac.sagemath.org/ticket/4541





---

archive/issue_comments_033951.json:
```json
{
    "body": "Ignore my comments above.  This is maybe still a problem, but for a different reason.  The problem is that s([1,1,1,1]) doesn't live in the space spanned by the the ks3's.  So in cases like this, there are three choices for what ks3(f) should do (f symmetric, but not in the span of the ks3's):\n\n1) Throw an error\n\n2) Project f to the ks3's and return that answer.  This is the current behavior.\n\n3) Do (2) but warn the user about it.\n\nI'd vote for (1), but I'll see what sage-combinat-devel has to say first.",
    "created_at": "2008-11-19T01:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33951",
    "user": "https://github.com/jbandlow"
}
```

Ignore my comments above.  This is maybe still a problem, but for a different reason.  The problem is that s([1,1,1,1]) doesn't live in the space spanned by the the ks3's.  So in cases like this, there are three choices for what ks3(f) should do (f symmetric, but not in the span of the ks3's):

1) Throw an error

2) Project f to the ks3's and return that answer.  This is the current behavior.

3) Do (2) but warn the user about it.

I'd vote for (1), but I'll see what sage-combinat-devel has to say first.



---

archive/issue_comments_033952.json:
```json
{
    "body": "Changing assignee from @mwhansen to @jbandlow.",
    "created_at": "2008-11-19T01:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33952",
    "user": "https://github.com/jbandlow"
}
```

Changing assignee from @mwhansen to @jbandlow.



---

archive/issue_comments_033953.json:
```json
{
    "body": "Attachment [4541.patch](tarball://root/attachments/some-uuid/ticket4541/4541.patch) by @jbandlow created at 2008-11-25 03:50:36\n\nFixed.  And lots of doctests added.",
    "created_at": "2008-11-25T03:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33953",
    "user": "https://github.com/jbandlow"
}
```

Attachment [4541.patch](tarball://root/attachments/some-uuid/ticket4541/4541.patch) by @jbandlow created at 2008-11-25 03:50:36

Fixed.  And lots of doctests added.



---

archive/issue_comments_033954.json:
```json
{
    "body": "oh, i forgot to mention, this patch applies on top of the patch at 4540.  is that ok, mabshoff?",
    "created_at": "2008-11-25T03:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33954",
    "user": "https://github.com/jbandlow"
}
```

oh, i forgot to mention, this patch applies on top of the patch at 4540.  is that ok, mabshoff?



---

archive/issue_comments_033955.json:
```json
{
    "body": "Yes, dependencies on other patches is fine, especially if they have been already merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T03:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, dependencies on other patches is fine, especially if they have been already merged.

Cheers,

Michael



---

archive/issue_comments_033956.json:
```json
{
    "body": "Ok, thanks.  I'm changing the milestone since this is done.  I'll solicit reviews on sage-combinat-devel right now.",
    "created_at": "2008-11-25T03:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33956",
    "user": "https://github.com/jbandlow"
}
```

Ok, thanks.  I'm changing the milestone since this is done.  I'll solicit reviews on sage-combinat-devel right now.



---

archive/issue_comments_033957.json:
```json
{
    "body": "Hi Jason,\n\nThis looks good to me.  I'll make a new ticket for adding a method which does the projection.  This should be pretty easy as we can just add a flag to the change by triangularity method.\n\n--Mike",
    "created_at": "2008-11-25T19:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33957",
    "user": "https://github.com/mwhansen"
}
```

Hi Jason,

This looks good to me.  I'll make a new ticket for adding a method which does the projection.  This should be pretty easy as we can just add a flag to the change by triangularity method.

--Mike



---

archive/issue_comments_033958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-25T20:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004786.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-25T20:11:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4541#event-4786"
}
```



---

archive/issue_comments_033959.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1. \n\nJason: This was a diff, please make sure to post hg patches, i.e. \"hg export\" vs. hg \"diff\". The code was committed in your name, so the changelog properly reflects the credit situation.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T20:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33959",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha1. 

Jason: This was a diff, please make sure to post hg patches, i.e. "hg export" vs. hg "diff". The code was committed in your name, so the changelog properly reflects the credit situation.

Cheers,

Michael



---

archive/issue_comments_033960.json:
```json
{
    "body": "Michael,\nwhoops, sorry.  Thanks for fixing.\n\n\nMike,\nSounds good.  You can assign such a ticket to me, if you'd like, so I can keep my changes to kschur.py organized (adding dual kschurs is probably next...)  Anyway, I agree that projection should be pretty easy.",
    "created_at": "2008-11-25T20:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4541#issuecomment-33960",
    "user": "https://github.com/jbandlow"
}
```

Michael,
whoops, sorry.  Thanks for fixing.


Mike,
Sounds good.  You can assign such a ticket to me, if you'd like, so I can keep my changes to kschur.py organized (adding dual kschurs is probably next...)  Anyway, I agree that projection should be pretty easy.
