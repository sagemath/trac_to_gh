# Issue 9858: Doctest failures due to hard-coded line numbers in (doctests of) sage/rings/*.pyx

archive/issues_009858.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: DeprecationWarning failure integer.pyx rational.pyx beginner\n\n\n```\n$ ./sage -t  -long devel/sage/sage/rings/integer.pyx\nsage -t -long \"devel/sage/sage/rings/integer.pyx\"           \n**********************************************************************\nFile \"devel/sage/sage/rings/integer.pyx\", line 4618:\n    sage: 5.sqrt_approx(prec=200)\nExpected:\n    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.\n    2.2360679774997896964091736687312762354406183596115257242709\nGot:\n    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.\n    2.2360679774997896964091736687312762354406183596115257242709\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_118\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_integer.py\n\t [16.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/integer.pyx\"\nTotal time for all tests: 16.4 seconds\n$ ./sage -t  -long devel/sage/sage/rings/rational.pyx \nsage -t -long \"devel/sage/sage/rings/rational.pyx\"          \n**********************************************************************\nFile \"devel/sage/sage/rings/rational.pyx\", line 1339:\n    sage: (5/3).sqrt_approx()\nExpected:\n    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.\n    1.29099444873581\nGot:\n    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.\n    1.29099444873581\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_31\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_rational.py\n\t [4.5 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/rational.pyx\"\nTotal time for all tests: 4.6 seconds\n```\n\n\nThese failures occurred just because some line numbers in `$SAGE_LOCAL/bin/ncadoctest.py` changed (when I added some flush statements).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9859\n\n",
    "created_at": "2010-09-06T04:32:10Z",
    "labels": [
        "component: doctest coverage",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Doctest failures due to hard-coded line numbers in (doctests of) sage/rings/*.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9858",
    "user": "https://github.com/nexttime"
}
```
Assignee: mvngu

Keywords: DeprecationWarning failure integer.pyx rational.pyx beginner


```
$ ./sage -t  -long devel/sage/sage/rings/integer.pyx
sage -t -long "devel/sage/sage/rings/integer.pyx"           
**********************************************************************
File "devel/sage/sage/rings/integer.pyx", line 4618:
    sage: 5.sqrt_approx(prec=200)
Expected:
    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    2.2360679774997896964091736687312762354406183596115257242709
Got:
    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    2.2360679774997896964091736687312762354406183596115257242709
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_118
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_integer.py
	 [16.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/integer.pyx"
Total time for all tests: 16.4 seconds
$ ./sage -t  -long devel/sage/sage/rings/rational.pyx 
sage -t -long "devel/sage/sage/rings/rational.pyx"          
**********************************************************************
File "devel/sage/sage/rings/rational.pyx", line 1339:
    sage: (5/3).sqrt_approx()
Expected:
    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    1.29099444873581
Got:
    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    1.29099444873581
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_31
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_rational.py
	 [4.5 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/rational.pyx"
Total time for all tests: 4.6 seconds
```


These failures occurred just because some line numbers in `$SAGE_LOCAL/bin/ncadoctest.py` changed (when I added some flush statements).

Issue created by migration from https://trac.sagemath.org/ticket/9859





---

archive/issue_comments_097171.json:
```json
{
    "body": "Minh, please excuse and change the component in case it's the wrong one. (I'm not sure if \"doctest\" refers to the framework or doctest failures in general.)",
    "created_at": "2010-09-06T04:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97171",
    "user": "https://github.com/nexttime"
}
```

Minh, please excuse and change the component in case it's the wrong one. (I'm not sure if "doctest" refers to the framework or doctest failures in general.)



---

archive/issue_comments_097172.json:
```json
{
    "body": "Based on Sage 4.5.3.rc0. Apply to Sage library.",
    "created_at": "2010-09-06T05:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97172",
    "user": "https://github.com/nexttime"
}
```

Based on Sage 4.5.3.rc0. Apply to Sage library.



---

archive/issue_comments_097173.json:
```json
{
    "body": "Attachment [trac_9859-fix_hard-coded_doctest_line_numbers.patch](tarball://root/attachments/some-uuid/ticket9859/trac_9859-fix_hard-coded_doctest_line_numbers.patch) by @nexttime created at 2010-09-06 05:06:53\n\nOk, I'm a beginner. ;-)\n\n(I've uploaded a patch.)",
    "created_at": "2010-09-06T05:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97173",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9859-fix_hard-coded_doctest_line_numbers.patch](tarball://root/attachments/some-uuid/ticket9859/trac_9859-fix_hard-coded_doctest_line_numbers.patch) by @nexttime created at 2010-09-06 05:06:53

Ok, I'm a beginner. ;-)

(I've uploaded a patch.)



---

archive/issue_comments_097174.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-06T05:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97174",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097175.json:
```json
{
    "body": "Those hard-coded line numbers that leif fixed shouldn't have been there in the first place. The patch applied OK against Sage 4.5.3.rc0, all doctests (including long) passed, and the standard documentation built fine. And I'm OK with the changes in the patch.",
    "created_at": "2010-09-07T18:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Those hard-coded line numbers that leif fixed shouldn't have been there in the first place. The patch applied OK against Sage 4.5.3.rc0, all doctests (including long) passed, and the standard documentation built fine. And I'm OK with the changes in the patch.



---

archive/issue_comments_097176.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T18:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097177.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Those hard-coded line numbers that leif fixed shouldn't have been there in the first place.\n\nYes. According to Mercurial, Michael Abshoff introduced that in Jan 2009(!)... :-)\n(There's no ticket number in the commit message. I'm not sure when it really got merged, but obviously long time ago.)\n\nI wonder why I never ran into this before, since I frequently doctest with modified versions of `ncadoctest` (but perhaps incidentally not the whole Sage library, or `sage/rings`).\n\nThanks for reviewing this.",
    "created_at": "2010-09-07T19:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97177",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 mvngu]:
> Those hard-coded line numbers that leif fixed shouldn't have been there in the first place.

Yes. According to Mercurial, Michael Abshoff introduced that in Jan 2009(!)... :-)
(There's no ticket number in the commit message. I'm not sure when it really got merged, but obviously long time ago.)

I wonder why I never ran into this before, since I frequently doctest with modified versions of `ncadoctest` (but perhaps incidentally not the whole Sage library, or `sage/rings`).

Thanks for reviewing this.



---

archive/issue_comments_097178.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9858#issuecomment-97178",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024820.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:40:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9858#event-24820"
}
```
