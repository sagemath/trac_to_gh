# Issue 1784: number field doctest failure

archive/issues_001784.json:
```json
{
    "body": "Assignee: @williamstein\n\nA doctest failure in sage-2.9.3\n\n./sage -t ./devel/sage-main/sage/rings/number_field/number_field.py\nsage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************\nFile \"number_field.py\", line 2042:\n    sage: Z(-1)\nExpected:\n    0.0333333333333333\nGot:\n    0\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_58\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field.py\n         [90.3 s]\nexit code: 256\n\n---\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/rings/number_field/number_field.py\nTotal time for all tests: 90.3 seconds\n\nThe failed test is the following:\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1784\n\n",
    "created_at": "2008-01-15T19:10:16Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "number field doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1784",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein

A doctest failure in sage-2.9.3

./sage -t ./devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************
File "number_field.py", line 2042:
    sage: Z(-1)
Expected:
    0.0333333333333333
Got:
    0
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_58
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [90.3 s]
exit code: 256

---
The following tests failed:


        sage -t  devel/sage-main/sage/rings/number_field/number_field.py
Total time for all tests: 90.3 seconds

The failed test is the following:



Issue created by migration from https://trac.sagemath.org/ticket/1784





---

archive/issue_comments_011265.json:
```json
{
    "body": "Changing component from algebraic geometry to number theory.",
    "created_at": "2008-01-15T19:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11265",
    "user": "https://github.com/pdenapo"
}
```

Changing component from algebraic geometry to number theory.



---

archive/issue_comments_011266.json:
```json
{
    "body": "I cannot reproduce this. So could you supply more information, i.e. compiler used, operating system and so on. What seems strange is that it took 90 seconds to get to a failure. on sage.math the whole doctest takes 20 second.\n\nPlease also assign a milestone to all your tickets. In case of doctest failures it should be always the next release.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T19:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I cannot reproduce this. So could you supply more information, i.e. compiler used, operating system and so on. What seems strange is that it took 90 seconds to get to a failure. on sage.math the whole doctest takes 20 second.

Please also assign a milestone to all your tickets. In case of doctest failures it should be always the next release.

Cheers,

Michael



---

archive/issue_events_004359.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-15T19:18:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1784#event-4359"
}
```



---

archive/issue_comments_011267.json:
```json
{
    "body": "This is very very suspicious.  I can't replicate it anywhere either.\n\nThe doctest in question is running a stand-alone PARI program to compute the special value of a zeta function at -1.  I think the answer should be 0.03333... as claimed.  Hmmm...   As you say, we need to know if the problem is reproducible from the command line, what computer, etc.,",
    "created_at": "2008-01-15T19:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11267",
    "user": "https://github.com/williamstein"
}
```

This is very very suspicious.  I can't replicate it anywhere either.

The doctest in question is running a stand-alone PARI program to compute the special value of a zeta function at -1.  I think the answer should be 0.03333... as claimed.  Hmmm...   As you say, we need to know if the problem is reproducible from the command line, what computer, etc.,



---

archive/issue_comments_011268.json:
```json
{
    "body": "Hmm, any chance your improved pari.spkg from #258 is involved here?\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T19:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, any chance your improved pari.spkg from #258 is involved here?

Cheers,

Michael



---

archive/issue_comments_011269.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-01-19T22:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11269",
    "user": "https://github.com/pdenapo"
}
```

Resolution: invalid



---

archive/issue_events_004360.json:
```json
{
    "actor": "https://github.com/pdenapo",
    "created_at": "2008-01-19T22:12:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1784#event-4360"
}
```



---

archive/issue_comments_011270.json:
```json
{
    "body": "May be you are right about some problem with my own version of\npari in #258, I could not reproduce the bug in a fresh install\nof sage-2.9.3\n\nI'll check further...",
    "created_at": "2008-01-19T22:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1784#issuecomment-11270",
    "user": "https://github.com/pdenapo"
}
```

May be you are right about some problem with my own version of
pari in #258, I could not reproduce the bug in a fresh install
of sage-2.9.3

I'll check further...



---

archive/issue_events_004361.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-19T22:18:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1784",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1784#event-4361"
}
```
