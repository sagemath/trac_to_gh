# Issue 4083: [with patch, needs work] sage.finance - Options pricing implementation

archive/issues_004083.json:
```json
{
    "body": "Assignee: psinis\n\nCC:  @cswiercz software@pacificafog.com @slel\n\nKeywords: finance, options, black-scholes\n\nIncludes capabilities for options pricing using the Black-Scholes model. The primary class of this ticket is finance.Option, which uses finance.Stock.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4083\n\n",
    "closed_at": "2021-10-25T15:39:21Z",
    "created_at": "2008-09-09T02:16:17Z",
    "labels": [
        "component: finance"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] sage.finance - Options pricing implementation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4083",
    "user": "https://github.com/cswiercz"
}
```
Assignee: psinis

CC:  @cswiercz software@pacificafog.com @slel

Keywords: finance, options, black-scholes

Includes capabilities for options pricing using the Black-Scholes model. The primary class of this ticket is finance.Option, which uses finance.Stock.

Issue created by migration from https://trac.sagemath.org/ticket/4083





---

archive/issue_comments_029395.json:
```json
{
    "body": "Attachment [sage-4083-part1.patch](tarball://root/attachments/some-uuid/ticket4083/sage-4083-part1.patch) by @cswiercz created at 2008-09-09 02:17:33\n\nInitial implementation of the Option class.",
    "created_at": "2008-09-09T02:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29395",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-4083-part1.patch](tarball://root/attachments/some-uuid/ticket4083/sage-4083-part1.patch) by @cswiercz created at 2008-09-09 02:17:33

Initial implementation of the Option class.



---

archive/issue_comments_029396.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-16T22:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29396",
    "user": "https://github.com/cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029397.json:
```json
{
    "body": "Changing assignee from @williamstein to @cswiercz.",
    "created_at": "2008-09-16T22:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29397",
    "user": "https://github.com/cswiercz"
}
```

Changing assignee from @williamstein to @cswiercz.



---

archive/issue_comments_029398.json:
```json
{
    "body": "REFEREE:\n\nThis code is *really* good, and I definitely want it in Sage.  There are a bunch of minor issues that need to be fixed. \n\n1. A bunch of doctests fail when run on OSX 10.5 32-bit, which is maybe numerical noise:\n\n```\nteragon-2:finance wstein$ sage -t black_scholes.py \nsage -t  devel/sage-main/sage/finance/black_scholes.py      **********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 43:\n    sage: tenyr_swap.Black(5, 1.2, 0.25, 'n')\nExpected:\n    0.0679829347644\nGot:\n    0.067982934764359987\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 333:\n    sage: opt.Black(5, 1.2, 0.25, 'ln')\nExpected:\n    1.38685477149\nGot:\n    1.3868547714858503\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 335:\n    sage: opt._bs_ln()\nExpected:\n    1.38685477149\nGot:\n    1.3868547714858503\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 272:\n    sage: aapl_200c.Black(175, 0.4, 0.5, 'ln')\nExpected:\n    10.8744664878\nGot:\n    10.874466487776381\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 318:\n    sage: opt.Black(5, 1.2, 0.25, 'n')\nExpected:\n    0.567982934764\nGot:\n    0.5679829347643599\n**********************************************************************\nFile \"/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py\", line 320:\n    sage: opt._bs_n()\nExpected:\n    0.567982934764\nGot:\n    0.5679829347643599\n**********************************************************************\n4 items had failures:\n   1 of   7 in __main__.example_1\n   2 of   5 in __main__.example_10\n   1 of   4 in __main__.example_8\n   2 of   5 in __main__.example_9\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /Users/wstein/sage/tmp/.doctest_black_scholes.py\n\t [13.8 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  devel/sage-main/sage/finance/black_scholes.py\nTotal time for all tests: 13.8 seconds\nteragon-2:finance wstein$ \n```\n\n2. There are three convenience functions with no doctests, which breaks the 100% coverage rule:\n\n```\ndef n(x):       return scipy.stats.norm.pdf(float(x))\ndef N(x):       return scipy.stats.norm.cdf(float(x))\ndef invNorm(x): return scipy.stats.norm.ppf(float(x), loc=0, scale=1)\n```\nIn fact the coverage score isn't very good:\n\n```\nteragon-2:finance wstein$ sage -coverage black_scholes.py \n----------------------------------------------------------------------\nblack_scholes.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE black_scholes.py: 50% (9 of 18)\n\nMissing documentation:\n\t * n(x):\n\t * N(x):\n\t * invNorm(x):\n\t * _fullalpha(self, cps):\n\t * _alpha(self):\n\t * _beta(self):\n\t * _ratio(self):\n\t * _d1(self):\n\t * _d2(self):\n```\n\n3. There is an empty TESTS: block at the top of the file.  (Just delete it.)\n\n4. There are several instances of % in docstrings, which will confuse latex.  I'm not sure if this matters, since we're switching to Sphinx. \n\n5. I see the text \"Funciton call is inherent:\" in the __init__ method.  It has typos and makes no sense.\n\n6. Change things like this in docstrings\n\n```\n# optional -- requires internet and random\n```\nto\n\n```\n# random; optional -- internet\n```\nThis will work using the new -only_optional doctesting framework, which allows us to test only particular components (e.g., those that require the internet).",
    "created_at": "2008-11-28T03:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29398",
    "user": "https://github.com/williamstein"
}
```

REFEREE:

This code is *really* good, and I definitely want it in Sage.  There are a bunch of minor issues that need to be fixed. 

1. A bunch of doctests fail when run on OSX 10.5 32-bit, which is maybe numerical noise:

```
teragon-2:finance wstein$ sage -t black_scholes.py 
sage -t  devel/sage-main/sage/finance/black_scholes.py      **********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 43:
    sage: tenyr_swap.Black(5, 1.2, 0.25, 'n')
Expected:
    0.0679829347644
Got:
    0.067982934764359987
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 333:
    sage: opt.Black(5, 1.2, 0.25, 'ln')
Expected:
    1.38685477149
Got:
    1.3868547714858503
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 335:
    sage: opt._bs_ln()
Expected:
    1.38685477149
Got:
    1.3868547714858503
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 272:
    sage: aapl_200c.Black(175, 0.4, 0.5, 'ln')
Expected:
    10.8744664878
Got:
    10.874466487776381
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 318:
    sage: opt.Black(5, 1.2, 0.25, 'n')
Expected:
    0.567982934764
Got:
    0.5679829347643599
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 320:
    sage: opt._bs_n()
Expected:
    0.567982934764
Got:
    0.5679829347643599
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_1
   2 of   5 in __main__.example_10
   1 of   4 in __main__.example_8
   2 of   5 in __main__.example_9
***Test Failed*** 6 failures.
For whitespace errors, see the file /Users/wstein/sage/tmp/.doctest_black_scholes.py
	 [13.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage-main/sage/finance/black_scholes.py
Total time for all tests: 13.8 seconds
teragon-2:finance wstein$ 
```

2. There are three convenience functions with no doctests, which breaks the 100% coverage rule:

```
def n(x):       return scipy.stats.norm.pdf(float(x))
def N(x):       return scipy.stats.norm.cdf(float(x))
def invNorm(x): return scipy.stats.norm.ppf(float(x), loc=0, scale=1)
```
In fact the coverage score isn't very good:

```
teragon-2:finance wstein$ sage -coverage black_scholes.py 
----------------------------------------------------------------------
black_scholes.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE black_scholes.py: 50% (9 of 18)

Missing documentation:
	 * n(x):
	 * N(x):
	 * invNorm(x):
	 * _fullalpha(self, cps):
	 * _alpha(self):
	 * _beta(self):
	 * _ratio(self):
	 * _d1(self):
	 * _d2(self):
```

3. There is an empty TESTS: block at the top of the file.  (Just delete it.)

4. There are several instances of % in docstrings, which will confuse latex.  I'm not sure if this matters, since we're switching to Sphinx. 

5. I see the text "Funciton call is inherent:" in the __init__ method.  It has typos and makes no sense.

6. Change things like this in docstrings

```
# optional -- requires internet and random
```
to

```
# random; optional -- internet
```
This will work using the new -only_optional doctesting framework, which allows us to test only particular components (e.g., those that require the internet).



---

archive/issue_comments_029399.json:
```json
{
    "body": "Changing assignee from @cswiercz to psinis.",
    "created_at": "2009-02-23T22:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29399",
    "user": "https://trac.sagemath.org/admin/accounts/users/psinis"
}
```

Changing assignee from @cswiercz to psinis.



---

archive/issue_comments_029400.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-02-23T22:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29400",
    "user": "https://trac.sagemath.org/admin/accounts/users/psinis"
}
```

Changing status from assigned to new.



---

archive/issue_events_009307.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9307"
}
```



---

archive/issue_comments_029401.json:
```json
{
    "body": "See #14671",
    "created_at": "2013-09-08T08:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29401",
    "user": "https://github.com/fchapoton"
}
```

See #14671



---

archive/issue_events_009308.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9308"
}
```



---

archive/issue_events_009309.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9309"
}
```



---

archive/issue_events_009310.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9310"
}
```



---

archive/issue_events_009311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9311"
}
```



---

archive/issue_events_009312.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9312"
}
```



---

archive/issue_events_009313.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9313"
}
```



---

archive/issue_events_009314.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-05-13T05:54:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9314"
}
```



---

archive/issue_events_009315.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-05-13T05:54:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9315"
}
```



---

archive/issue_comments_029402.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-10-10T20:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29402",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029403.json:
```json
{
    "body": "outdated after sage.finance deprecation in #32427",
    "created_at": "2021-10-10T20:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29403",
    "user": "https://github.com/mkoeppe"
}
```

outdated after sage.finance deprecation in #32427



---

archive/issue_events_009316.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-10T20:30:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9316"
}
```



---

archive/issue_events_009317.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-10T20:30:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9317"
}
```



---

archive/issue_comments_029404.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-25T10:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29404",
    "user": "https://github.com/slel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_029405.json:
```json
{
    "body": "Ok.",
    "created_at": "2021-10-25T10:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29405",
    "user": "https://github.com/slel"
}
```

Ok.



---

archive/issue_comments_029406.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-25T15:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4083#issuecomment-29406",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_009318.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-25T15:39:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4083#event-9318"
}
```
