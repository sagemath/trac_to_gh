# Issue 9171: cygwin: some test failures in sagedoc.py

archive/issues_009171.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\n\n```\n\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"                  \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py\", line 891:\n    sage: len(search_doc('tree', interact=False).splitlines()) > 2000\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py\", line 496:\n    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\nExpected:\n    True\nGot:\n    False\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9171\n\n",
    "created_at": "2010-06-07T04:36:13Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "cygwin: some test failures in sagedoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9171",
    "user": "was"
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

archive/issue_comments_085769.json:
```json
{
    "body": "I usually get these errors if the documentation isn't built.  Is that's what's going on here?",
    "created_at": "2010-08-02T13:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85769",
    "user": "kcrisman"
}
```

I usually get these errors if the documentation isn't built.  Is that's what's going on here?



---

archive/issue_comments_085770.json:
```json
{
    "body": "I get the second failure, but not the first one, on a recent build on XP.",
    "created_at": "2011-08-02T02:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85770",
    "user": "kcrisman"
}
```

I get the second failure, but not the first one, on a recent build on XP.



---

archive/issue_comments_085771.json:
```json
{
    "body": "I'm getting these failures by hand, though.   And I checked - the documentation is not automatically built.  So let's change this title.",
    "created_at": "2011-08-19T14:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85771",
    "user": "kcrisman"
}
```

I'm getting these failures by hand, though.   And I checked - the documentation is not automatically built.  So let's change this title.



---

archive/issue_comments_085772.json:
```json
{
    "body": "JP says that the doc does now build (since Maxima now works with #9167).",
    "created_at": "2013-01-15T15:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85772",
    "user": "kcrisman"
}
```

JP says that the doc does now build (since Maxima now works with #9167).



---

archive/issue_comments_085773.json:
```json
{
    "body": "Yup the doc built fine for me and the test passes.\nIf you can reproduce that, let's close this ticket.",
    "created_at": "2013-01-15T18:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85773",
    "user": "jpflori"
}
```

Yup the doc built fine for me and the test passes.
If you can reproduce that, let's close this ticket.



---

archive/issue_comments_085774.json:
```json
{
    "body": "This is really frustrating for me - I simply cannot build the doc, or (once again) even start Sage, even though it **just was working a few days ago**.  All the usual can't map foo.dll to the same address stuff.  I've rebased several times, no luck, though sometimes different files that can't map...\n\nI'd like to try this again, though - yet another build from scratch, hopefully.  There is no rush to close this, after all, as there is no patch or spkg required.",
    "created_at": "2013-01-17T03:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85774",
    "user": "kcrisman"
}
```

This is really frustrating for me - I simply cannot build the doc, or (once again) even start Sage, even though it **just was working a few days ago**.  All the usual can't map foo.dll to the same address stuff.  I've rebased several times, no luck, though sometimes different files that can't map...

I'd like to try this again, though - yet another build from scratch, hopefully.  There is no rush to close this, after all, as there is no patch or spkg required.



---

archive/issue_comments_085775.json:
```json
{
    "body": "I once again built the doc succesfully, so let's close this one.\nI doubt XP/7 32bits/64bits will make any difference.",
    "created_at": "2013-01-30T10:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85775",
    "user": "jpflori"
}
```

I once again built the doc succesfully, so let's close this one.
I doubt XP/7 32bits/64bits will make any difference.



---

archive/issue_comments_085776.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-30T10:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85776",
    "user": "jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085777.json:
```json
{
    "body": "No, I think you are right.  Assuming one can get Sage to start reliably, this should now be okay.",
    "created_at": "2013-01-30T13:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85777",
    "user": "kcrisman"
}
```

No, I think you are right.  Assuming one can get Sage to start reliably, this should now be okay.



---

archive/issue_comments_085778.json:
```json
{
    "body": "Ok, so I'm putting this as positive_review/wontfix",
    "created_at": "2013-01-30T13:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85778",
    "user": "jpflori"
}
```

Ok, so I'm putting this as positive_review/wontfix



---

archive/issue_comments_085779.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-30T13:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85779",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085780.json:
```json
{
    "body": "I guess it would be worth confirming this doctest passes :) though I'm sure it will now.",
    "created_at": "2013-01-30T13:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85780",
    "user": "kcrisman"
}
```

I guess it would be worth confirming this doctest passes :) though I'm sure it will now.



---

archive/issue_comments_085781.json:
```json
{
    "body": "It passed on my 5.5.rc0 and 5.6.rc0 'make ptest' and just did so on my 5.7.beta1.",
    "created_at": "2013-01-30T13:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85781",
    "user": "jpflori"
}
```

It passed on my 5.5.rc0 and 5.6.rc0 'make ptest' and just did so on my 5.7.beta1.



---

archive/issue_comments_085782.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-31T20:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9171#issuecomment-85782",
    "user": "jdemeyer"
}
```

Resolution: worksforme
