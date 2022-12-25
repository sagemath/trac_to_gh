# Issue 9171: cygwin: some test failures in sagedoc.py

archive/issues_009171.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\n\n```\n\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"                  \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py\", line 891:\n    sage: len(search_doc('tree', interact=False).splitlines()) > 2000\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py\", line 496:\n    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\nExpected:\n    True\nGot:\n    False\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9171\n\n",
    "created_at": "2010-06-07T04:36:13Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: some test failures in sagedoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9171",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori


```

sage -t  "devel/sage/sage/misc/sagedoc.py"                  
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py", line 891:
    sage: len(search_doc('tree', interact=False).splitlines()) > 2000
Expected:
    True
Got:
    False
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py", line 496:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    False

```


Issue created by migration from https://trac.sagemath.org/ticket/9171





---

archive/issue_comments_085631.json:
```json
{
    "body": "I usually get these errors if the documentation isn't built.  Is that's what's going on here?",
    "created_at": "2010-08-02T13:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85631",
    "user": "https://github.com/kcrisman"
}
```

I usually get these errors if the documentation isn't built.  Is that's what's going on here?



---

archive/issue_comments_085632.json:
```json
{
    "body": "I get the second failure, but not the first one, on a recent build on XP.",
    "created_at": "2011-08-02T02:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85632",
    "user": "https://github.com/kcrisman"
}
```

I get the second failure, but not the first one, on a recent build on XP.



---

archive/issue_comments_085633.json:
```json
{
    "body": "I'm getting these failures by hand, though.   And I checked - the documentation is not automatically built.  So let's change this title.",
    "created_at": "2011-08-19T14:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85633",
    "user": "https://github.com/kcrisman"
}
```

I'm getting these failures by hand, though.   And I checked - the documentation is not automatically built.  So let's change this title.



---

archive/issue_comments_085634.json:
```json
{
    "body": "JP says that the doc does now build (since Maxima now works with #9167).",
    "created_at": "2013-01-15T15:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85634",
    "user": "https://github.com/kcrisman"
}
```

JP says that the doc does now build (since Maxima now works with #9167).



---

archive/issue_comments_085635.json:
```json
{
    "body": "Yup the doc built fine for me and the test passes.\nIf you can reproduce that, let's close this ticket.",
    "created_at": "2013-01-15T18:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85635",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Yup the doc built fine for me and the test passes.
If you can reproduce that, let's close this ticket.



---

archive/issue_comments_085636.json:
```json
{
    "body": "This is really frustrating for me - I simply cannot build the doc, or (once again) even start Sage, even though it **just was working a few days ago**.  All the usual can't map foo.dll to the same address stuff.  I've rebased several times, no luck, though sometimes different files that can't map...\n\nI'd like to try this again, though - yet another build from scratch, hopefully.  There is no rush to close this, after all, as there is no patch or spkg required.",
    "created_at": "2013-01-17T03:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85636",
    "user": "https://github.com/kcrisman"
}
```

This is really frustrating for me - I simply cannot build the doc, or (once again) even start Sage, even though it **just was working a few days ago**.  All the usual can't map foo.dll to the same address stuff.  I've rebased several times, no luck, though sometimes different files that can't map...

I'd like to try this again, though - yet another build from scratch, hopefully.  There is no rush to close this, after all, as there is no patch or spkg required.



---

archive/issue_comments_085637.json:
```json
{
    "body": "I once again built the doc succesfully, so let's close this one.\nI doubt XP/7 32bits/64bits will make any difference.",
    "created_at": "2013-01-30T10:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85637",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I once again built the doc succesfully, so let's close this one.
I doubt XP/7 32bits/64bits will make any difference.



---

archive/issue_comments_085638.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-30T10:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85638",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085639.json:
```json
{
    "body": "No, I think you are right.  Assuming one can get Sage to start reliably, this should now be okay.",
    "created_at": "2013-01-30T13:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85639",
    "user": "https://github.com/kcrisman"
}
```

No, I think you are right.  Assuming one can get Sage to start reliably, this should now be okay.



---

archive/issue_comments_085640.json:
```json
{
    "body": "Ok, so I'm putting this as positive_review/wontfix",
    "created_at": "2013-01-30T13:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85640",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Ok, so I'm putting this as positive_review/wontfix



---

archive/issue_events_022559.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jpflori",
    "created_at": "2013-01-30T13:10:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9171#event-22559"
}
```



---

archive/issue_comments_085641.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-30T13:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85641",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085642.json:
```json
{
    "body": "I guess it would be worth confirming this doctest passes :) though I'm sure it will now.",
    "created_at": "2013-01-30T13:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85642",
    "user": "https://github.com/kcrisman"
}
```

I guess it would be worth confirming this doctest passes :) though I'm sure it will now.



---

archive/issue_comments_085643.json:
```json
{
    "body": "It passed on my 5.5.rc0 and 5.6.rc0 'make ptest' and just did so on my 5.7.beta1.",
    "created_at": "2013-01-30T13:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85643",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

It passed on my 5.5.rc0 and 5.6.rc0 'make ptest' and just did so on my 5.7.beta1.



---

archive/issue_events_022560.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-31T20:35:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9171#event-22560"
}
```



---

archive/issue_comments_085644.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-31T20:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85644",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
