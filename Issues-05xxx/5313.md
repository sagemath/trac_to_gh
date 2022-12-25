# Issue 5313: patch singular so that when it runs out of memory the error message says "singular" in it

archive/issues_005313.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @nexttime\n\nWhen looking at #3760 it took a long long time to see that this had anything whatever to do with singular.  To speed this up, we should patch two files in Singular so that instead of getting\n\n```\nerror: no more memory\nSystem 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2\n\nhalt 14\n```\nas an error, one gets\n\n```\nSINGULAR error: no more memory\nSystem 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2\n...\nand then an exception is raised!\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5313\n\n",
    "created_at": "2009-02-19T19:18:47Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "patch singular so that when it runs out of memory the error message says \"singular\" in it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5313",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

CC:  @nexttime

When looking at #3760 it took a long long time to see that this had anything whatever to do with singular.  To speed this up, we should patch two files in Singular so that instead of getting

```
error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2

halt 14
```
as an error, one gets

```
SINGULAR error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2
...
and then an exception is raised!
```

Issue created by migration from https://trac.sagemath.org/ticket/5313





---

archive/issue_comments_040838.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-18T01:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40838",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_040839.json:
```json
{
    "body": "This is really an enhancement, not a bug.",
    "created_at": "2010-01-18T01:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40839",
    "user": "https://github.com/williamstein"
}
```

This is really an enhancement, not a bug.



---

archive/issue_comments_040840.json:
```json
{
    "body": "I'm wrong, this is a *BUG*, since Sage should not exit on memory overflow, but should instead raise an exception. \nHere's a new example to illustrate the problem:\n\n```\n\nsage: n=500\nsage: R = PolynomialRing(QQ,n,names='x')\nsage: f = sum(R.gens())\nsage: g = f*f\n\nerror: no more memory\nSystem 212048k:212048k Appl 164440k/2763k Malloc 156k/0k Valloc 167048k/2763k Pages 41762/0 Regions 360:360\n\nhalt 14\nwstein@sage:~/build/sage-4.4.4/spkg/standard$   \n```\n\nI should not be dumped to the command prompt!",
    "created_at": "2010-07-14T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40840",
    "user": "https://github.com/williamstein"
}
```

I'm wrong, this is a *BUG*, since Sage should not exit on memory overflow, but should instead raise an exception. 
Here's a new example to illustrate the problem:

```

sage: n=500
sage: R = PolynomialRing(QQ,n,names='x')
sage: f = sum(R.gens())
sage: g = f*f

error: no more memory
System 212048k:212048k Appl 164440k/2763k Malloc 156k/0k Valloc 167048k/2763k Pages 41762/0 Regions 360:360

halt 14
wstein@sage:~/build/sage-4.4.4/spkg/standard$   
```

I should not be dumped to the command prompt!



---

archive/issue_comments_040841.json:
```json
{
    "body": "More complete log on sage.math:\n\n```\n\nwstein@sage:~/build/sage-4.4.4$ ulimit -v 1000000\nwstein@sage:~/build/sage-4.4.4$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: n = 1000\nsage: R = PolynomialRing(QQ,n,names='x')\nsage: f = sum(R.gens())\nsage: g = f*f\nerror: no more memory\nSystem 212080k:212080k Appl 168836k/2090k Malloc 211k/0k Valloc 170716k/2090k Pages 42679/0 Regions 388:388\nhalt 14\nwstein@sage:~/build/sage-4.4.4$ \n| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |\n| Type notebook() for the GUI, and license() for information.        |\n```",
    "created_at": "2010-07-14T20:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40841",
    "user": "https://github.com/williamstein"
}
```

More complete log on sage.math:

```

wstein@sage:~/build/sage-4.4.4$ ulimit -v 1000000
wstein@sage:~/build/sage-4.4.4$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 1000
sage: R = PolynomialRing(QQ,n,names='x')
sage: f = sum(R.gens())
sage: g = f*f
error: no more memory
System 212080k:212080k Appl 168836k/2090k Malloc 211k/0k Valloc 170716k/2090k Pages 42679/0 Regions 388:388
halt 14
wstein@sage:~/build/sage-4.4.4$ 
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
```



---

archive/issue_comments_040842.json:
```json
{
    "body": "I submitted this upstream to Hans Schoenemann",
    "created_at": "2010-07-14T20:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40842",
    "user": "https://github.com/williamstein"
}
```

I submitted this upstream to Hans Schoenemann



---

archive/issue_comments_040843.json:
```json
{
    "body": "Attachment [Singular_error.patch](tarball://root/attachments/some-uuid/ticket5313/Singular_error.patch) by @williamstein created at 2010-07-14 20:53:05\n\nNOTE to future self:\n\nTo work on singular:\n\n1. sage -f -m singular-x.y.z.spkg\n2. cd spkg/build/singular-x.y.z\n3. Make changes\n4. Type `make install-libsingular`",
    "created_at": "2010-07-14T20:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40843",
    "user": "https://github.com/williamstein"
}
```

Attachment [Singular_error.patch](tarball://root/attachments/some-uuid/ticket5313/Singular_error.patch) by @williamstein created at 2010-07-14 20:53:05

NOTE to future self:

To work on singular:

1. sage -f -m singular-x.y.z.spkg
2. cd spkg/build/singular-x.y.z
3. Make changes
4. Type `make install-libsingular`



---

archive/issue_comments_040844.json:
```json
{
    "body": "To get rid of the \"exit of out sage\" issue hackishly:\n\n1. Modify src/kernel/mminit.cc and put abort() right after the first fprintf in the function void omSingOutOfMemoryFunc().\n\n2. Edit the file devel/sage/sage/libs/singular/polynomial.pyx  by adding _sig_on/_sig_off around `ret[0] = pp_Mult_qq(p, q, r)` in the function singular_polynomial_mul. \n\nThen we have:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: n = 1000\nsage: sage: R = PolynomialRing(QQ,n,names='x')\nsage: sage: f = sum(R.gens())\nsage: sage: g = f*f\n| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |\n| Type notebook() for the GUI, and license() for information.        |\n2 - Singular error: no more memory\ncalling abort\nsage: \n```\n\nNote that strangely there is no traceback.  But at least one gets the sage prompt back.\n\nRegarding speed:\n\nWITH the _sig_on/_sig_off stuff:\n\n```\n\nsage: R.<x,y,z> = PolynomialRing(QQ)\nsage: f = (x+y+z)^2\nsage: timeit('f*(f+1)')\n625 loops, best of 3: 12.6 \u00b5s per loop\nsage: f = (x+y+z)\nsage: timeit('f*(f+1)')\n625 loops, best of 3: 11.4 \u00b5s per loop\nsage: f = (x+y+z)^10+1\nsage: timeit('f*(f+1)')\n625 loops, best of 3: 168 \u00b5s per loop\nsage: timeit('x*x')\n625 loops, best of 3: 410 ns per loop\n```\nand without it:\n\n```\nsage: sage: R.<x,y,z> = PolynomialRing(QQ)\nsage: sage: f = (x+y+z)^2\nsage:  timeit('f*(f+1)')\n625 loops, best of 3: 12.4 \u00b5s per loop\nsage: sage: f = (x+y+z)\nsage: sage: timeit('f*(f+1)')\n625 loops, best of 3: 11.2 \u00b5s per loop\nsage: sage: f = (x+y+z)^10+1\nsage: sage: timeit('f*(f+1)')\n625 loops, best of 3: 167 \u00b5s per loop\nsage: timeit('x*x')\n625 loops, best of 3: 290 ns per loop\n```\n\nThis is all on sage.math.",
    "created_at": "2010-07-14T21:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40844",
    "user": "https://github.com/williamstein"
}
```

To get rid of the "exit of out sage" issue hackishly:

1. Modify src/kernel/mminit.cc and put abort() right after the first fprintf in the function void omSingOutOfMemoryFunc().

2. Edit the file devel/sage/sage/libs/singular/polynomial.pyx  by adding _sig_on/_sig_off around `ret[0] = pp_Mult_qq(p, q, r)` in the function singular_polynomial_mul. 

Then we have:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: n = 1000
sage: sage: R = PolynomialRing(QQ,n,names='x')
sage: sage: f = sum(R.gens())
sage: sage: g = f*f
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
2 - Singular error: no more memory
calling abort
sage: 
```

Note that strangely there is no traceback.  But at least one gets the sage prompt back.

Regarding speed:

WITH the _sig_on/_sig_off stuff:

```

sage: R.<x,y,z> = PolynomialRing(QQ)
sage: f = (x+y+z)^2
sage: timeit('f*(f+1)')
625 loops, best of 3: 12.6 µs per loop
sage: f = (x+y+z)
sage: timeit('f*(f+1)')
625 loops, best of 3: 11.4 µs per loop
sage: f = (x+y+z)^10+1
sage: timeit('f*(f+1)')
625 loops, best of 3: 168 µs per loop
sage: timeit('x*x')
625 loops, best of 3: 410 ns per loop
```
and without it:

```
sage: sage: R.<x,y,z> = PolynomialRing(QQ)
sage: sage: f = (x+y+z)^2
sage:  timeit('f*(f+1)')
625 loops, best of 3: 12.4 µs per loop
sage: sage: f = (x+y+z)
sage: sage: timeit('f*(f+1)')
625 loops, best of 3: 11.2 µs per loop
sage: sage: f = (x+y+z)^10+1
sage: sage: timeit('f*(f+1)')
625 loops, best of 3: 167 µs per loop
sage: timeit('x*x')
625 loops, best of 3: 290 ns per loop
```

This is all on sage.math.



---

archive/issue_comments_040845.json:
```json
{
    "body": "Attachment [trac_5313-sigon_sigoff.patch](tarball://root/attachments/some-uuid/ticket5313/trac_5313-sigon_sigoff.patch) by @williamstein created at 2010-07-14 21:28:49\n\nThis makes it so errors during arithmetic can be handled.   This won't do anything though unless the singular library is patched to call abort() before exit, as explained in a comment on this ticket.",
    "created_at": "2010-07-14T21:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40845",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5313-sigon_sigoff.patch](tarball://root/attachments/some-uuid/ticket5313/trac_5313-sigon_sigoff.patch) by @williamstein created at 2010-07-14 21:28:49

This makes it so errors during arithmetic can be handled.   This won't do anything though unless the singular library is patched to call abort() before exit, as explained in a comment on this ticket.



---

archive/issue_comments_040846.json:
```json
{
    "body": "Attachment [singular-spkg_add_abort.patch](tarball://root/attachments/some-uuid/ticket5313/singular-spkg_add_abort.patch) by @williamstein created at 2010-07-14 21:36:57\n\nthis is a patch to the singular spkg.  It patches a patch file.",
    "created_at": "2010-07-14T21:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40846",
    "user": "https://github.com/williamstein"
}
```

Attachment [singular-spkg_add_abort.patch](tarball://root/attachments/some-uuid/ticket5313/singular-spkg_add_abort.patch) by @williamstein created at 2010-07-14 21:36:57

this is a patch to the singular spkg.  It patches a patch file.



---

archive/issue_comments_040847.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-14T21:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40847",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040848.json:
```json
{
    "body": "This patch http://trac.sagemath.org/sage_trac/attachment/ticket/5313/Singular_error.patch is already included in #8059.",
    "created_at": "2010-08-12T13:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40848",
    "user": "https://github.com/malb"
}
```

This patch http://trac.sagemath.org/sage_trac/attachment/ticket/5313/Singular_error.patch is already included in #8059.



---

archive/issue_comments_040849.json:
```json
{
    "body": "These examples all work for me, no memory issue reported, even.\n\nAnyway, Martin or someone, can you confirm this, put your name as reviewer, and set to positive review (possibly cc:ing jdemeyer)?  Then this can be closed, assuming the previous comment is true.",
    "created_at": "2011-06-23T03:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40849",
    "user": "https://github.com/kcrisman"
}
```

These examples all work for me, no memory issue reported, even.

Anyway, Martin or someone, can you confirm this, put your name as reviewer, and set to positive review (possibly cc:ing jdemeyer)?  Then this can be closed, assuming the previous comment is true.



---

archive/issue_comments_040850.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-05T14:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40850",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_040851.json:
```json
{
    "body": "Okay, I can confirm that the equivalent of [attachment:Singular_error.patch] is in the Singular in Sage, but that nothing like [attachment:singular-spkg_add_abort.patch] is in the current Singular - `abort()` is not called, and can confirm that William's example with the ulimit still fails to raise an exception, although it does now say Singular in the error.  Sorry for not reading more carefully before.\n\nFurther, the patch [attachment:trac_5313-sigon_sigoff.patch] to Sage no longer applies.\n\n```\npatching file sage/libs/singular/polynomial.pyx\nHunk #4 FAILED at 266\nHunk #5 FAILED at 336\n2 out of 5 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej\nabort: patch failed to apply\n```\n\nFinally, should we submit a pull request or issue [upstream](https://github.com/Singular/Sources) for the abort issue, or is that truly too hackish to ask them to do?  Putting none of the above for upstream since one thing was completely incorporated while the other they apparently don't even know about.",
    "created_at": "2012-07-05T14:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5313#issuecomment-40851",
    "user": "https://github.com/kcrisman"
}
```

Okay, I can confirm that the equivalent of [attachment:Singular_error.patch] is in the Singular in Sage, but that nothing like [attachment:singular-spkg_add_abort.patch] is in the current Singular - `abort()` is not called, and can confirm that William's example with the ulimit still fails to raise an exception, although it does now say Singular in the error.  Sorry for not reading more carefully before.

Further, the patch [attachment:trac_5313-sigon_sigoff.patch] to Sage no longer applies.

```
patching file sage/libs/singular/polynomial.pyx
Hunk #4 FAILED at 266
Hunk #5 FAILED at 336
2 out of 5 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej
abort: patch failed to apply
```

Finally, should we submit a pull request or issue [upstream](https://github.com/Singular/Sources) for the abort issue, or is that truly too hackish to ask them to do?  Putting none of the above for upstream since one thing was completely incorporated while the other they apparently don't even know about.



---

archive/issue_events_012370.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12370"
}
```



---

archive/issue_events_012371.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12371"
}
```



---

archive/issue_events_012372.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12372"
}
```



---

archive/issue_events_012373.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12373"
}
```



---

archive/issue_events_012374.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12374"
}
```



---

archive/issue_events_012375.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12375"
}
```



---

archive/issue_events_012376.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5313",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5313#event-12376"
}
```
