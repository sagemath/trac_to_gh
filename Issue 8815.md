# Issue 8815: Misc elliptic curve typo fixes (easy review)

archive/issues_008815.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThis code was clearly never actually tried out.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8815\n\n",
    "created_at": "2010-04-29T04:24:30Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Misc elliptic curve typo fixes (easy review)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8815",
    "user": "https://github.com/robertwb"
}
```
Assignee: @JohnCremona

This code was clearly never actually tried out.

Issue created by migration from https://trac.sagemath.org/ticket/8815





---

archive/issue_comments_080772.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T04:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80772",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080773.json:
```json
{
    "body": "Attachment [8815-ec-fixes.patch](tarball://root/attachments/some-uuid/ticket8815/8815-ec-fixes.patch) by @robertwb created at 2010-04-29 04:30:31\n\nNote, `AttributeError` was the wrong thing to raise here, and got caught in odd places. The other logic was overly complicated, just let the TypeError get raised.",
    "created_at": "2010-04-29T04:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80773",
    "user": "https://github.com/robertwb"
}
```

Attachment [8815-ec-fixes.patch](tarball://root/attachments/some-uuid/ticket8815/8815-ec-fixes.patch) by @robertwb created at 2010-04-29 04:30:31

Note, `AttributeError` was the wrong thing to raise here, and got caught in odd places. The other logic was overly complicated, just let the TypeError get raised.



---

archive/issue_comments_080774.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-29T08:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80774",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080775.json:
```json
{
    "body": "Patch applies to 4.4;  tests pass (I checked all sage/schemes/elliptic_curves).\n\nIn the first file patched, was there a reason for not changing the TypeError in lines 1093/4 to another ValueError?\n\nIn the second:  there are essentially identical blocks of code in lines 1052-1068 and 1360-1376.  But the typo (s to z) was only fixed in one place.  So the other needs fixing too.\n\nIn the \"logic simplification\" bit of the patch -- this is not correct now!  If z's parent is (say) QQ then after the patch, z will have been coerced into CC but C will be set to QQ.  So this now fails:\n\n```\nsage: E = EllipticCurve('14a1')\nsage: L = E.period_lattice()\nsage: L.coordinates(1)\n```\n\n\nFinally, your description is a little unkind!  I spent a long time trying this out -- though I do admit, of course, that I clearly did not test every line.  Perhaps we need to add some more doctests?",
    "created_at": "2010-04-29T08:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80775",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies to 4.4;  tests pass (I checked all sage/schemes/elliptic_curves).

In the first file patched, was there a reason for not changing the TypeError in lines 1093/4 to another ValueError?

In the second:  there are essentially identical blocks of code in lines 1052-1068 and 1360-1376.  But the typo (s to z) was only fixed in one place.  So the other needs fixing too.

In the "logic simplification" bit of the patch -- this is not correct now!  If z's parent is (say) QQ then after the patch, z will have been coerced into CC but C will be set to QQ.  So this now fails:

```
sage: E = EllipticCurve('14a1')
sage: L = E.period_lattice()
sage: L.coordinates(1)
```


Finally, your description is a little unkind!  I spent a long time trying this out -- though I do admit, of course, that I clearly did not test every line.  Perhaps we need to add some more doctests?



---

archive/issue_comments_080776.json:
```json
{
    "body": "Sorry, my comment was not supposed to be derogatory about the code, it was supposed to be encouragement that the bug wasn't anything deep (but I can see how it was taken the wrong way). You're right about C--we need to set it if it's being used later. \n\nI typically raise a `TypeError` when I get something that's the wrong type (e.g. I expected a list, but got an integer, or something like that), and a `ValueError`when it's something about the value (e.g. it was supposed to be positive, or a prime). \n\nI'll fix the patch, including more doctests.",
    "created_at": "2010-04-29T09:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80776",
    "user": "https://github.com/robertwb"
}
```

Sorry, my comment was not supposed to be derogatory about the code, it was supposed to be encouragement that the bug wasn't anything deep (but I can see how it was taken the wrong way). You're right about C--we need to set it if it's being used later. 

I typically raise a `TypeError` when I get something that's the wrong type (e.g. I expected a list, but got an integer, or something like that), and a `ValueError`when it's something about the value (e.g. it was supposed to be positive, or a prime). 

I'll fix the patch, including more doctests.



---

archive/issue_comments_080777.json:
```json
{
    "body": "Attachment [8815-ec-fixes.2.patch](tarball://root/attachments/some-uuid/ticket8815/8815-ec-fixes.2.patch) by @JohnCremona created at 2010-04-29 09:38:31\n\nNo offence taken!  I'll review this again when ready.  #8820 wil take more work, so probably not today...",
    "created_at": "2010-04-29T09:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80777",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8815-ec-fixes.2.patch](tarball://root/attachments/some-uuid/ticket8815/8815-ec-fixes.2.patch) by @JohnCremona created at 2010-04-29 09:38:31

No offence taken!  I'll review this again when ready.  #8820 wil take more work, so probably not today...



---

archive/issue_comments_080778.json:
```json
{
    "body": "The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. \n\nThanks for looking at this barrage of tickets I've just posted!",
    "created_at": "2010-04-29T09:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80778",
    "user": "https://github.com/robertwb"
}
```

The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. 

Thanks for looking at this barrage of tickets I've just posted!



---

archive/issue_comments_080779.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-29T10:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80779",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080780.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. \n\nI used to be one of the tab culprits but I have now properly configured emacs on all the machines I use not to use them!\n\n> \n> Thanks for looking at this barrage of tickets I've just posted!\n\nWell, I feel it's my duty to do so...\n\nI am looking at the new patch now.",
    "created_at": "2010-04-29T10:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80780",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 robertwb]:
> The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. 

I used to be one of the tab culprits but I have now properly configured emacs on all the machines I use not to use them!

> 
> Thanks for looking at this barrage of tickets I've just posted!

Well, I feel it's my duty to do so...

I am looking at the new patch now.



---

archive/issue_comments_080781.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T10:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80781",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080782.json:
```json
{
    "body": "New patch fixes the issues I had with the first patch, applies fine to 4.4 and all tests in sage/schemes/elliptic_curves pass.\n\nPositive review:  apply second patch only.",
    "created_at": "2010-04-29T10:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80782",
    "user": "https://github.com/JohnCremona"
}
```

New patch fixes the issues I had with the first patch, applies fine to 4.4 and all tests in sage/schemes/elliptic_curves pass.

Positive review:  apply second patch only.



---

archive/issue_events_021501.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T21:53:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8815#event-21501"
}
```



---

archive/issue_comments_080783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80783",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_080784.json:
```json
{
    "body": "Merged [8815-ec-fixes.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8815/8815-ec-fixes.2.patch).",
    "created_at": "2010-05-08T21:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8815#issuecomment-80784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [8815-ec-fixes.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8815/8815-ec-fixes.2.patch).
