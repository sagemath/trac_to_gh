# Issue 1206: doc testing support for numerical computations with randomish output is insufficient

archive/issues_001206.json:
```json
{
    "body": "Assignee: failure\n\nThe current way in which doc tests of numerical computations that produce randomish output are performed is not sufficient to actually detect regressions. \n\nCurrently if the word #random follows the test, it is run but the output is not compared, this only tests that there was no failure doing something but not that what was computed was in any way correct or what was expected.\n\nFor computations with randomish output, what should be checked is that the difference between all the floating values in what is computed and in the doc string are less than some bound 1e-8 or something, or maybe the bound should be specified, so that\n\n#random 1e-8 would check that the the computation differs from the output in the doc string by 1e-8.\n\n  \n\nIssue created by migration from https://trac.sagemath.org/ticket/1206\n\n",
    "created_at": "2007-11-19T06:42:59Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doc testing support for numerical computations with randomish output is insufficient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1206",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: failure

The current way in which doc tests of numerical computations that produce randomish output are performed is not sufficient to actually detect regressions. 

Currently if the word #random follows the test, it is run but the output is not compared, this only tests that there was no failure doing something but not that what was computed was in any way correct or what was expected.

For computations with randomish output, what should be checked is that the difference between all the floating values in what is computed and in the doc string are less than some bound 1e-8 or something, or maybe the bound should be specified, so that

#random 1e-8 would check that the the computation differs from the output in the doc string by 1e-8.

  

Issue created by migration from https://trac.sagemath.org/ticket/1206





---

archive/issue_comments_007440.json:
```json
{
    "body": "We have the \"12.123..\" notation to indicate that the last n, in this case 2 decimals are affected by numerical precision issues. Shouldn't that work for you, too?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-19T08:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We have the "12.123.." notation to indicate that the last n, in this case 2 decimals are affected by numerical precision issues. Shouldn't that work for you, too?

Cheers,

Michael



---

archive/issue_comments_007441.json:
```json
{
    "body": "That should be sufficient, it doesn't seem to be documented in the programming guide, though I may have just missed it.",
    "created_at": "2007-11-21T21:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7441",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

That should be sufficient, it doesn't seem to be documented in the programming guide, though I may have just missed it.



---

archive/issue_comments_007442.json:
```json
{
    "body": "Ok, since was doubted that the following case could happen:\n\n```\nExpected:\n    1.0000000000000000\nGot:\n    0.9999999999999999\n```\n\nhere a real world example from 2.8.14 on Solaris:\n\n```\nFile \"complex_double.pyx\", line 1496:\n    sage: z^2 - z + 1\nExpected:\n    2.22044604925e-16 + 1.11022302463e-16*I\nGot:\n    2.22044604925e-16 + 2.22044604925e-16*I\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-11-28T22:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7442",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, since was doubted that the following case could happen:

```
Expected:
    1.0000000000000000
Got:
    0.9999999999999999
```

here a real world example from 2.8.14 on Solaris:

```
File "complex_double.pyx", line 1496:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
```

Cheers,

Michael



---

archive/issue_comments_007443.json:
```json
{
    "body": "Actually, the case\n\n```\nExpected:\n    1.0000000000000000\nGot:\n    0.9999999999999999\n```\n\nDid happen a couple times in the 2.8.15 release cycle. The usual approach was to change the doctest to avoid results where such small rounding issues would cause `\"...\"` the doctest to be useless.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Actually, the case

```
Expected:
    1.0000000000000000
Got:
    0.9999999999999999
```

Did happen a couple times in the 2.8.15 release cycle. The usual approach was to change the doctest to avoid results where such small rounding issues would cause `"..."` the doctest to be useless.

Cheers,

Michael



---

archive/issue_events_003207.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T14:39:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1206#event-3207"
}
```



---

archive/issue_comments_007444.json:
```json
{
    "body": "I believe implementing this would require a major restructuring of how doctesting is carried out.",
    "created_at": "2007-12-06T04:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7444",
    "user": "https://github.com/mwhansen"
}
```

I believe implementing this would require a major restructuring of how doctesting is carried out.



---

archive/issue_comments_007445.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7445",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_003208.json:
```json
{
    "actor": "https://github.com/koffie",
    "created_at": "2011-08-24T01:44:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1206#event-3208"
}
```



---

archive/issue_events_003209.json:
```json
{
    "actor": "https://github.com/koffie",
    "created_at": "2011-08-24T01:44:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1206#event-3209"
}
```



---

archive/issue_comments_007446.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-24T01:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7446",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_007447.json:
```json
{
    "body": "There is a patch up for the same problem at #10952",
    "created_at": "2011-08-24T01:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7447",
    "user": "https://github.com/koffie"
}
```

There is a patch up for the same problem at #10952



---

archive/issue_comments_007448.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-16T14:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7448",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007449.json:
```json
{
    "body": "Setting this to positive_review so the release manager will see it.",
    "created_at": "2012-05-16T14:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7449",
    "user": "https://github.com/kini"
}
```

Setting this to positive_review so the release manager will see it.



---

archive/issue_events_003210.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:03:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1206#event-3210"
}
```



---

archive/issue_comments_007450.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-05-21T08:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1206#issuecomment-7450",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
