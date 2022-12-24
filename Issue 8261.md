# Issue 8261: cygwin: mpfr fails 1 test in its test suite on windows

archive/issues_008261.json:
```json
{
    "body": "Assignee: tbd\n\nUpon building mpfr-2.4.1.p1 on cygwin we get one test failure:\n\n```\n...\nPASS: tprintf.exe\nError in mpfr_sprintf (s, \"%'30Re\", x);\nexpected: \"      1,899347461279296875e+07\"\ngot:      \"      1.899347461279296875e+07\"\nFAIL: tsprintf.exe\nPASS: tfprintf.exe\nPASS: trec_sqrt.exe\nPASS: tpow_all.exe\n=====================\n1 of 148 tests failed\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8261\n\n",
    "created_at": "2010-02-14T06:55:25Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "cygwin: mpfr fails 1 test in its test suite on windows",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8261",
    "user": "was"
}
```
Assignee: tbd

Upon building mpfr-2.4.1.p1 on cygwin we get one test failure:

```
...
PASS: tprintf.exe
Error in mpfr_sprintf (s, "%'30Re", x);
expected: "      1,899347461279296875e+07"
got:      "      1.899347461279296875e+07"
FAIL: tsprintf.exe
PASS: tfprintf.exe
PASS: trec_sqrt.exe
PASS: tpow_all.exe
=====================
1 of 148 tests failed
```


Issue created by migration from https://trac.sagemath.org/ticket/8261





---

archive/issue_comments_073110.json:
```json
{
    "body": "This is the same issue here: http://permalink.gmane.org/gmane.comp.lib.mpfr.general/375\n\nThere is a patch posted there, but I have not tried it yet.",
    "created_at": "2010-02-16T21:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73110",
    "user": "mhansen"
}
```

This is the same issue here: http://permalink.gmane.org/gmane.comp.lib.mpfr.general/375

There is a patch posted there, but I have not tried it yet.



---

archive/issue_comments_073111.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T23:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73111",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073112.json:
```json
{
    "body": "MPFR 2.4.2 has the fix posted in that thread.  I've made an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/mpfr-2.4.2.spkg\n\nI'm building it now to test to see if it works.",
    "created_at": "2010-02-16T23:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73112",
    "user": "mhansen"
}
```

MPFR 2.4.2 has the fix posted in that thread.  I've made an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/mpfr-2.4.2.spkg

I'm building it now to test to see if it works.



---

archive/issue_comments_073113.json:
```json
{
    "body": "I just check and all tests pass on Cygwin with MPFR 2.4.2.",
    "created_at": "2010-02-17T00:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73113",
    "user": "mhansen"
}
```

I just check and all tests pass on Cygwin with MPFR 2.4.2.



---

archive/issue_comments_073114.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> I just check and all tests pass on Cygwin with MPFR 2.4.2.\n\nI have verified this on winxp1 on boxen.math. The Sage 4.3.4.alpha0 build failed when trying to compile the gd spkg. That didn't prevent me from manually installing your upgraded MPFR spkg. First, I set these environment variables:\n\n```\nexport SAGE_PORT=yes\nexport SAGE_CHECK=yes\n```\n\nThen I forced an installation with\n\n```\n./sage -f /URL/to/mpfr-2.4.2.spkg\n```\n\nThe build went OK and the test suite of MPFR passed. I'll now test on t2.math and some other machines.",
    "created_at": "2010-03-03T23:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73114",
    "user": "mvngu"
}
```

Replying to [comment:3 mhansen]:
> I just check and all tests pass on Cygwin with MPFR 2.4.2.

I have verified this on winxp1 on boxen.math. The Sage 4.3.4.alpha0 build failed when trying to compile the gd spkg. That didn't prevent me from manually installing your upgraded MPFR spkg. First, I set these environment variables:

```
export SAGE_PORT=yes
export SAGE_CHECK=yes
```

Then I forced an installation with

```
./sage -f /URL/to/mpfr-2.4.2.spkg
```

The build went OK and the test suite of MPFR passed. I'll now test on t2.math and some other machines.



---

archive/issue_comments_073115.json:
```json
{
    "body": "I qrefresh'd Mike's upgraded spkg to include the ticket number in the commit message and changelog. The resulting spkg can be found at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg",
    "created_at": "2010-03-03T23:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73115",
    "user": "mvngu"
}
```

I qrefresh'd Mike's upgraded spkg to include the ticket number in the commit message and changelog. The resulting spkg can be found at

http://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg



---

archive/issue_comments_073116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T08:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73116",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073117.json:
```json
{
    "body": "The upgraded MPFR spkg builds on sage.math, t2.math, bsd.math, rosemary.math, and Cygwin (winxp1 on boxen.math). First, I set the environment variable\n\n```\nexport SAGE_CHECK=yes\n```\n\nand forced a re-installation with\n\n```\n./sage -f /URL/or/path/to/mpfr-2.4.2.spkg\n```\n\nThe build went OK and the test suite of MPFR passed without any reported failures.\n\n**Note to release manager:** Use the package at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg",
    "created_at": "2010-03-06T08:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73117",
    "user": "mvngu"
}
```

The upgraded MPFR spkg builds on sage.math, t2.math, bsd.math, rosemary.math, and Cygwin (winxp1 on boxen.math). First, I set the environment variable

```
export SAGE_CHECK=yes
```

and forced a re-installation with

```
./sage -f /URL/or/path/to/mpfr-2.4.2.spkg
```

The build went OK and the test suite of MPFR passed without any reported failures.

**Note to release manager:** Use the package at

http://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg



---

archive/issue_comments_073118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8261#issuecomment-73118",
    "user": "mhansen"
}
```

Resolution: fixed
