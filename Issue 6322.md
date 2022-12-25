# Issue 6322: optional doctest failure -- another mistake in bordeaux lectures

archive/issues_006322.json:
```json
{
    "body": "Assignee: tbd\n\n```\nsage -t -long --optional devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/nf_galois_groups.rst\", line 92:\n    sage: K.galois_group(type=\"gap\", algorithm='magma')    # optional\nExpected:\n    verbose...\n    Galois group Transitive group number 2 of degree 3 of\n    the Number Field in a with defining polynomial x^3 - 2\nGot:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_nf_galois_groups.py\n\t [12.4 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6322\n\n",
    "created_at": "2009-06-16T14:52:53Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.10",
    "title": "optional doctest failure -- another mistake in bordeaux lectures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6322",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
sage -t -long --optional devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/nf_galois_groups.rst", line 92:
    sage: K.galois_group(type="gap", algorithm='magma')    # optional
Expected:
    verbose...
    Galois group Transitive group number 2 of degree 3 of
    the Number Field in a with defining polynomial x^3 - 2
Got:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_nf_galois_groups.py
	 [12.4 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/6322





---

archive/issue_events_014833.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14833"
}
```



---

archive/issue_events_014834.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14834"
}
```



---

archive/issue_events_014835.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14835"
}
```



---

archive/issue_events_014836.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14836"
}
```



---

archive/issue_events_014837.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14837"
}
```



---

archive/issue_events_014838.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14838"
}
```



---

archive/issue_events_014839.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14839"
}
```



---

archive/issue_comments_050354.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50354",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050355.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50355",
    "user": "https://github.com/fchapoton"
}
```

Changing priority from major to minor.



---

archive/issue_events_014840.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-10-10T18:48:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14840"
}
```



---

archive/issue_events_014841.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-10-10T18:48:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "milestone": "sage-6.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14841"
}
```



---

archive/issue_comments_050356.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50356",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_050357.json:
```json
{
    "body": "Did you actually test it? I don't have magma, but if you tell me that the doctest passes, I believe you.",
    "created_at": "2015-10-10T20:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50357",
    "user": "https://github.com/jdemeyer"
}
```

Did you actually test it? I don't have magma, but if you tell me that the doctest passes, I believe you.



---

archive/issue_comments_050358.json:
```json
{
    "body": "I do not have magma either. Do we know somebody that has magma ?",
    "created_at": "2015-10-10T20:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50358",
    "user": "https://github.com/fchapoton"
}
```

I do not have magma either. Do we know somebody that has magma ?



---

archive/issue_comments_050359.json:
```json
{
    "body": "Replying to [comment:8 chapoton]:\n> I do not have magma either.\n\n\nThen why do you care about this ticket???",
    "created_at": "2015-10-10T21:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50359",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 chapoton]:
> I do not have magma either.


Then why do you care about this ticket???



---

archive/issue_comments_050360.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-12T17:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50360",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050361.json:
```json
{
    "body": "It appears that:\n\n1) I do have `magma` now\n2) The test requires `database_gap`\n\nThis has been tested, and needs review again.",
    "created_at": "2015-10-12T17:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50361",
    "user": "https://github.com/fchapoton"
}
```

It appears that:

1) I do have `magma` now
2) The test requires `database_gap`

This has been tested, and needs review again.



---

archive/issue_comments_050362.json:
```json
{
    "body": "ok, the tests do pass with magma and database_gap and also without both\n\ni am not quite sure of the way to put 2 optional conditions on the same line\n\nJeroen, could you please set a positive review if this is correct ?",
    "created_at": "2015-10-17T20:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50362",
    "user": "https://github.com/fchapoton"
}
```

ok, the tests do pass with magma and database_gap and also without both

i am not quite sure of the way to put 2 optional conditions on the same line

Jeroen, could you please set a positive review if this is correct ?



---

archive/issue_comments_050363.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-10-17T20:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50363",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050364.json:
```json
{
    "body": "The usual syntax is\n\n```\n# optional - magma database_gap\n```\nI don't know if what you did works or not, but it's better to change it.",
    "created_at": "2015-10-17T20:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50364",
    "user": "https://github.com/jdemeyer"
}
```

The usual syntax is

```
# optional - magma database_gap
```
I don't know if what you did works or not, but it's better to change it.



---

archive/issue_comments_050365.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-17T20:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50365",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050366.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-10-17T20:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50366",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050367.json:
```json
{
    "body": "done",
    "created_at": "2015-10-17T20:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50367",
    "user": "https://github.com/fchapoton"
}
```

done



---

archive/issue_comments_050368.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-10-17T20:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50368",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-10-18T19:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50369",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_014842.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-10-18T19:11:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6322#event-14842"
}
```
