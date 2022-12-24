# Issue 9176: cygwin: various heegner_index errors involving interval arithmetic on cygwin

archive/issues_009176.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  kcrisman dimpase\n\n\n```\n\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6380:\n    sage: E.heegner_index(-7)\nExpected:\n    1.00000?\nGot:\n    1\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6410:\n    sage: I = E.heegner_index(-8); I\nExpected:\n    1.50000?\nGot:\n    1\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6412:\n    sage: 2*I\nExpected:\n    3.0000?\nGot:\n    2\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6546:\n    sage: E.heegner_index_bound()\nExpected:\n    ([2], -7)\nGot:\n    ([], -7)\n**********************************************************************\n2 items had failures:\n   3 of  15 in __main__.example_229\n   1 of   4 in __main__.example_231\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_heegner.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9176\n\n",
    "created_at": "2010-06-07T05:33:45Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: various heegner_index errors involving interval arithmetic on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9176",
    "user": "was"
}
```
Assignee: tbd

CC:  kcrisman dimpase


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6380:
    sage: E.heegner_index(-7)
Expected:
    1.00000?
Got:
    1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6410:
    sage: I = E.heegner_index(-8); I
Expected:
    1.50000?
Got:
    1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6412:
    sage: 2*I
Expected:
    3.0000?
Got:
    2
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6546:
    sage: E.heegner_index_bound()
Expected:
    ([2], -7)
Got:
    ([], -7)
**********************************************************************
2 items had failures:
   3 of  15 in __main__.example_229
   1 of   4 in __main__.example_231
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_heegner.py
```


Issue created by migration from https://trac.sagemath.org/ticket/9176





---

archive/issue_comments_085827.json:
```json
{
    "body": "This file passed doctests in a build of mine on XP.",
    "created_at": "2011-08-02T02:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85827",
    "user": "kcrisman"
}
```

This file passed doctests in a build of mine on XP.



---

archive/issue_comments_085828.json:
```json
{
    "body": "But trying the first example by hand leads to a segfault (presumably related to the segfault currently bedeveling Cygwin startup, see #11551).\n\nThat is weird.  Is it possible that a *silent* segfault makes a doctest think it passed?",
    "created_at": "2011-08-19T14:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85828",
    "user": "kcrisman"
}
```

But trying the first example by hand leads to a segfault (presumably related to the segfault currently bedeveling Cygwin startup, see #11551).

That is weird.  Is it possible that a *silent* segfault makes a doctest think it passed?



---

archive/issue_comments_085829.json:
```json
{
    "body": "Got lots of failures, apparently because of forking issues, I'll try a rebase.",
    "created_at": "2013-01-15T18:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85829",
    "user": "jpflori"
}
```

Got lots of failures, apparently because of forking issues, I'll try a rebase.



---

archive/issue_comments_085830.json:
```json
{
    "body": "Also lots of MemoryError for PARI trying to allocate memory.",
    "created_at": "2013-01-15T18:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85830",
    "user": "jpflori"
}
```

Also lots of MemoryError for PARI trying to allocate memory.



---

archive/issue_comments_085831.json:
```json
{
    "body": "> Got lots of failures, apparently because of forking issues, I'll try a rebase.\nGlad at least *one* of the forking issues I had cropped up for you :-) Even if it does work on a rebase, don't forget to try by hand as well.",
    "created_at": "2013-01-15T18:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85831",
    "user": "kcrisman"
}
```

> Got lots of failures, apparently because of forking issues, I'll try a rebase.
Glad at least *one* of the forking issues I had cropped up for you :-) Even if it does work on a rebase, don't forget to try by hand as well.



---

archive/issue_comments_085832.json:
```json
{
    "body": "And indeed inside \"./sage -gp\" I cannot allocatemem(512000000), but only 256000000, not sure why though.",
    "created_at": "2013-01-15T18:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85832",
    "user": "jpflori"
}
```

And indeed inside "./sage -gp" I cannot allocatemem(512000000), but only 256000000, not sure why though.



---

archive/issue_comments_085833.json:
```json
{
    "body": "I think I only have one forking issue (among 202 failing tests) caused by ecl which I rebuilt in the end (and potentially did not rebase after that).",
    "created_at": "2013-01-15T18:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85833",
    "user": "jpflori"
}
```

I think I only have one forking issue (among 202 failing tests) caused by ecl which I rebuilt in the end (and potentially did not rebase after that).



---

archive/issue_comments_085834.json:
```json
{
    "body": "And I guess it is http://cygwin.com/cygwin-ug-net/setup-maxmem.html so was expected.\n\nSo I'm left with the one forking issue :)",
    "created_at": "2013-01-15T18:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85834",
    "user": "jpflori"
}
```

And I guess it is http://cygwin.com/cygwin-ug-net/setup-maxmem.html so was expected.

So I'm left with the one forking issue :)



---

archive/issue_comments_085835.json:
```json
{
    "body": "Ok I still get the forking issue after rebasing :( the only solution might be to get a clean install at once (I rebuilt ECL p1 spkg and dependencies after having installed all Sage with the p0).\n\nNot sure how to let Cygwin increase the mx mem used, using peflags on python tells me it could not open the file...",
    "created_at": "2013-01-15T21:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85835",
    "user": "jpflori"
}
```

Ok I still get the forking issue after rebasing :( the only solution might be to get a clean install at once (I rebuilt ECL p1 spkg and dependencies after having installed all Sage with the p0).

Not sure how to let Cygwin increase the mx mem used, using peflags on python tells me it could not open the file...



---

archive/issue_comments_085836.json:
```json
{
    "body": "The max mem I can allocate is 502333407 and all the hacks I tried in the registry seem to have no (good or bad) effect.",
    "created_at": "2013-01-16T10:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85836",
    "user": "jpflori"
}
```

The max mem I can allocate is 502333407 and all the hacks I tried in the registry seem to have no (good or bad) effect.



---

archive/issue_comments_085837.json:
```json
{
    "body": "Ok, I manage to use peflags to modify --cygwin-heap but if I set it to 1024MB then I get forking errors...",
    "created_at": "2013-01-16T10:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85837",
    "user": "jpflori"
}
```

Ok, I manage to use peflags to modify --cygwin-heap but if I set it to 1024MB then I get forking errors...



---

archive/issue_comments_085838.json:
```json
{
    "body": "I can set it to 600MB without forking errors and that is enough to let the tests pass.\n(And indeed the global variable heap_chunk_in_mb support has been removed in Cygwin 1.7.10, see http://cygwin.com/cygwin-ug-net/ov-new1.7.html.)",
    "created_at": "2013-01-16T10:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85838",
    "user": "jpflori"
}
```

I can set it to 600MB without forking errors and that is enough to let the tests pass.
(And indeed the global variable heap_chunk_in_mb support has been removed in Cygwin 1.7.10, see http://cygwin.com/cygwin-ug-net/ov-new1.7.html.)



---

archive/issue_comments_085839.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-27T09:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85839",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085840.json:
```json
{
    "body": "I propose to close it (as won't fix/worksforme), as it works now.",
    "created_at": "2013-01-27T09:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85840",
    "user": "dimpase"
}
```

I propose to close it (as won't fix/worksforme), as it works now.



---

archive/issue_comments_085841.json:
```json
{
    "body": "Replying to [comment:13 dimpase]:\n> I propose to close it (as won't fix/worksforme), as it works now.\nDid you actually manage to run the test without hacking around with --cygwin-heap?\nI think we should at least add some doc somewhere to state that the tests are expected to fail with default max heap memory and how to modify that (e.g. use peflags and the global var is not supported anymore).",
    "created_at": "2013-01-30T10:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85841",
    "user": "jpflori"
}
```

Replying to [comment:13 dimpase]:
> I propose to close it (as won't fix/worksforme), as it works now.
Did you actually manage to run the test without hacking around with --cygwin-heap?
I think we should at least add some doc somewhere to state that the tests are expected to fail with default max heap memory and how to modify that (e.g. use peflags and the global var is not supported anymore).



---

archive/issue_comments_085842.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-01-30T17:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85842",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_085843.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-03-01T10:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85843",
    "user": "jpflori"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_085844.json:
```json
{
    "body": "Anyway, I don't think we should deal with the peflags usage in another ticket as this was not the point of this ticket originally.\n\nSo lets close this one.\nIll open a ticket for documenting usage of peflags shortly.",
    "created_at": "2013-03-01T10:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85844",
    "user": "jpflori"
}
```

Anyway, I don't think we should deal with the peflags usage in another ticket as this was not the point of this ticket originally.

So lets close this one.
Ill open a ticket for documenting usage of peflags shortly.



---

archive/issue_comments_085845.json:
```json
{
    "body": "This is #14207.",
    "created_at": "2013-03-01T10:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85845",
    "user": "jpflori"
}
```

This is #14207.



---

archive/issue_comments_085846.json:
```json
{
    "body": "Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures\n\n```\nExpected:\n    0\nGot:\n    32\n```\n\nwhich seems to be exactly one per example.  Of course, there *is* no such doctest listed in the file, so this must be something in the framework.",
    "created_at": "2013-03-08T12:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85846",
    "user": "kcrisman"
}
```

Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures

```
Expected:
    0
Got:
    32
```

which seems to be exactly one per example.  Of course, there *is* no such doctest listed in the file, so this must be something in the framework.



---

archive/issue_comments_085847.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures\n> {{{\n> Expected:\n>     0\n> Got:\n>     32\n> }}}\nI guess these extra failures are mostly due to the fact a previous doctest needing too much memory for PARI failed.\n> which seems to be exactly one per example.  Of course, there *is* no such doctest listed in the file, so this must be something in the framework.",
    "created_at": "2013-03-14T00:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85847",
    "user": "jpflori"
}
```

Replying to [comment:18 kcrisman]:
> Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures
> {{{
> Expected:
>     0
> Got:
>     32
> }}}
I guess these extra failures are mostly due to the fact a previous doctest needing too much memory for PARI failed.
> which seems to be exactly one per example.  Of course, there *is* no such doctest listed in the file, so this must be something in the framework.



---

archive/issue_comments_085848.json:
```json
{
    "body": "Sorry for not following up - so you agree with Dima that this is a pure memory issue, and so should be closed?  Should we at least put a mention in the doc for this file that \"if you are on a system with not much memory allocated (such as default Cygwin, but perhaps others like tablets or something) then there is this trick, see the verbiage added by #14207\"?",
    "created_at": "2013-03-15T18:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85848",
    "user": "kcrisman"
}
```

Sorry for not following up - so you agree with Dima that this is a pure memory issue, and so should be closed?  Should we at least put a mention in the doc for this file that "if you are on a system with not much memory allocated (such as default Cygwin, but perhaps others like tablets or something) then there is this trick, see the verbiage added by #14207"?



---

archive/issue_comments_085849.json:
```json
{
    "body": "I do, lets close this one.",
    "created_at": "2013-03-30T13:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85849",
    "user": "jpflori"
}
```

I do, lets close this one.



---

archive/issue_comments_085850.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-30T13:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85850",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085851.json:
```json
{
    "body": "Changing keywords from \"\" to \"cygwin\".",
    "created_at": "2013-03-30T13:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85851",
    "user": "jpflori"
}
```

Changing keywords from "" to "cygwin".



---

archive/issue_comments_085852.json:
```json
{
    "body": "Please fill in Author/Reviewer.",
    "created_at": "2013-04-01T13:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85852",
    "user": "jdemeyer"
}
```

Please fill in Author/Reviewer.



---

archive/issue_comments_085853.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-04-03T15:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9176#issuecomment-85853",
    "user": "jdemeyer"
}
```

Resolution: invalid
