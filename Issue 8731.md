# Issue 8731: update maxima to 5.21.0

archive/issues_008731.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @kcrisman @robert-marik @mwhansen\n\nThis update fixes #8729.  It also includes the fixes noted in #8645 (so this spkg supersedes the maxima spkg at #8645).\n\nThe spkg is up at http://sage.math.washington.edu/home/jason/maxima-5.21.0.spkg\n\nA patch needs to be applied to fix some doctests.  In particular, apparently maxima has gotten better at integration.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8731\n\n",
    "created_at": "2010-04-20T19:32:25Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update maxima to 5.21.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8731",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

CC:  @kcrisman @robert-marik @mwhansen

This update fixes #8729.  It also includes the fixes noted in #8645 (so this spkg supersedes the maxima spkg at #8645).

The spkg is up at http://sage.math.washington.edu/home/jason/maxima-5.21.0.spkg

A patch needs to be applied to fix some doctests.  In particular, apparently maxima has gotten better at integration.

Issue created by migration from https://trac.sagemath.org/ticket/8731





---

archive/issue_comments_079635.json:
```json
{
    "body": "Just a comment:\n\n```\n### maxima-5.21.0 (Jason Grout, 20 APR 2009)\n```\n\nis not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?",
    "created_at": "2010-04-20T19:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79635",
    "user": "https://github.com/kcrisman"
}
```

Just a comment:

```
### maxima-5.21.0 (Jason Grout, 20 APR 2009)
```

is not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?



---

archive/issue_comments_079636.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> Just a comment:\n> {{{\n> === maxima-5.21.0 (Jason Grout, 20 APR 2009) ===\n> }}}\n> is not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?\n\nThere are no less than three different styles in the other dates in the changelog, so apparently it's okay to have inconsistent date styles, so I did the dates in a much more standard notation.  However, I'll change it to spell out April since the date is wrong anyway.",
    "created_at": "2010-04-20T19:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79636",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:1 kcrisman]:
> Just a comment:
> {{{
> === maxima-5.21.0 (Jason Grout, 20 APR 2009) ===
> }}}
> is not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?

There are no less than three different styles in the other dates in the changelog, so apparently it's okay to have inconsistent date styles, so I did the dates in a much more standard notation.  However, I'll change it to spell out April since the date is wrong anyway.



---

archive/issue_comments_079637.json:
```json
{
    "body": "Here are the doctests that are broken for me with this spkg:\n\n\n```\n\n        sage -t  -long 4.3.5/devel/sage/sage/misc/functional.py # 2 doctests failed\n        sage -t  -long 4.3.5/devel/sage/sage/symbolic/relation.py # 7 doctests failed\n        sage -t  -long 4.3.5/devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed\n        sage -t  -long 4.3.5/devel/sage/sage/symbolic/expression.pyx # 3 doctests failed\n        sage -t  -long 4.3.5/devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed\n        sage -t  -long 4.3.5/devel/sage/sage/interfaces/maxima.py # 8 doctests failed\n```\n",
    "created_at": "2010-04-20T20:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79637",
    "user": "https://github.com/jasongrout"
}
```

Here are the doctests that are broken for me with this spkg:


```

        sage -t  -long 4.3.5/devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/relation.py # 7 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/expression.pyx # 3 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/interfaces/maxima.py # 8 doctests failed
```




---

archive/issue_comments_079638.json:
```json
{
    "body": "I've uploaded a new spkg with the changelog date now the correct date (and formatted as 20 April 2010)",
    "created_at": "2010-04-20T20:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79638",
    "user": "https://github.com/jasongrout"
}
```

I've uploaded a new spkg with the changelog date now the correct date (and formatted as 20 April 2010)



---

archive/issue_comments_079639.json:
```json
{
    "body": "For the doctests that return binomial(n,n) instead of 1, we just have to put an assumption in: assume(n>0)",
    "created_at": "2010-04-20T20:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79639",
    "user": "https://github.com/jasongrout"
}
```

For the doctests that return binomial(n,n) instead of 1, we just have to put an assumption in: assume(n>0)



---

archive/issue_comments_079640.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-20T20:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79640",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_079641.json:
```json
{
    "body": "I had the following problem while trying to install this on Sage 4.4:\n\n```\n; registering #<SYSTEM :MAXIMA 4321148288> as MAXIMA\nAn error occurred during initialization:\nUnknown keyword :MOVE-HERE.\n\ninstalling Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas\ncp: maxima.fasb: No such file or directory\n***********************************************************\nFailed to install maxima.fasb as a library\n***********************************************************\n```\n\nNonetheless, I get Maxima 5.21.0 in the console, and the various binomial(n,n) errors you mention, so maybe something went right?",
    "created_at": "2010-04-27T19:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79641",
    "user": "https://github.com/kcrisman"
}
```

I had the following problem while trying to install this on Sage 4.4:

```
; registering #<SYSTEM :MAXIMA 4321148288> as MAXIMA
An error occurred during initialization:
Unknown keyword :MOVE-HERE.

installing Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas
cp: maxima.fasb: No such file or directory
***********************************************************
Failed to install maxima.fasb as a library
***********************************************************
```

Nonetheless, I get Maxima 5.21.0 in the console, and the various binomial(n,n) errors you mention, so maybe something went right?



---

archive/issue_comments_079642.json:
```json
{
    "body": "(1) Now the latest maxima is 5.21.1\n\n(2) This should be done in conjunction with upgrading ECL. See #8808.  The maxima in sage-4.4 doesn't build with ecl-10.4.1, but Maxima 5.21.1 *does* build fine on top of ECL-10.4.1.\n\nA new spkg is here (but, again, first install the ECL spkg from #8808 when testing this):\n\n    http://wstein.org/home/wstein/patches/maxima-5.21.1.spkg",
    "created_at": "2010-04-28T18:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79642",
    "user": "https://github.com/williamstein"
}
```

(1) Now the latest maxima is 5.21.1

(2) This should be done in conjunction with upgrading ECL. See #8808.  The maxima in sage-4.4 doesn't build with ecl-10.4.1, but Maxima 5.21.1 *does* build fine on top of ECL-10.4.1.

A new spkg is here (but, again, first install the ECL spkg from #8808 when testing this):

    http://wstein.org/home/wstein/patches/maxima-5.21.1.spkg



---

archive/issue_comments_079643.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T18:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79643",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079644.json:
```json
{
    "body": "Question: Does this still incorporate the fixes mentioned in the Description? I assume it still needs doctest fixes due to improvements.",
    "created_at": "2010-04-28T19:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79644",
    "user": "https://github.com/kcrisman"
}
```

Question: Does this still incorporate the fixes mentioned in the Description? I assume it still needs doctest fixes due to improvements.



---

archive/issue_comments_079645.json:
```json
{
    "body": "I still get \n\n```\ninstalling Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas\ncp: maxima.fasb: No such file or directory\n```\n\nthough I no longer get the unknown keyword error.  maxima_console() does give me 5.21.1.  Testing now.",
    "created_at": "2010-04-28T19:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79645",
    "user": "https://github.com/kcrisman"
}
```

I still get 

```
installing Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas
cp: maxima.fasb: No such file or directory
```

though I no longer get the unknown keyword error.  maxima_console() does give me 5.21.1.  Testing now.



---

archive/issue_comments_079646.json:
```json
{
    "body": "With 5.21.1 Maxima and 10.4.1 ECL, the new failure list is:\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/symbolic/expression.pyx # 3 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py # 0 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed\n        sage -t  devel/sage/sage/calculus/calculus.py # 2 doctests failed\n        sage -t  devel/sage/sage/interfaces/maxima.py # 8 doctests failed\n        sage -t  devel/sage/sage/misc/functional.py # 2 doctests failed\n        sage -t  devel/sage/sage/symbolic/relation.py # 7 doctests failed\n        sage -t  devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed\n        sage -t  devel/sage/sage/tests/startup.py # 1 doctests failed\n        sage -t  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed\n----------------------------------------------------------------------\nTimings have been updated.\nTotal time for all tests: 358.3 seconds\n                                             \n```\n\n\nSee http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run.",
    "created_at": "2010-04-28T19:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79646",
    "user": "https://github.com/williamstein"
}
```

With 5.21.1 Maxima and 10.4.1 ECL, the new failure list is:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/symbolic/expression.pyx # 3 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py # 0 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed
        sage -t  devel/sage/sage/calculus/calculus.py # 2 doctests failed
        sage -t  devel/sage/sage/interfaces/maxima.py # 8 doctests failed
        sage -t  devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t  devel/sage/sage/symbolic/relation.py # 7 doctests failed
        sage -t  devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed
        sage -t  devel/sage/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 358.3 seconds
                                             
```


See http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run.



---

archive/issue_comments_079647.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> \n> See http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run. \n\nOops, seems that solving inequalities is completely broken with this new version of Maxima.",
    "created_at": "2010-04-28T22:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79647",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:12 was]:
> 
> See http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run. 

Oops, seems that solving inequalities is completely broken with this new version of Maxima.



---

archive/issue_comments_079648.json:
```json
{
    "body": "Yes, though I wouldn't say completely broken, since not every doctest fails, correct?  \n\nOther issues:\n\nIn symbolic/integration/integral.py, there is one integral which has been improved, and one which seems to affected by the rational approximation thing, but wasn't before.   There is also an integral (in that file, I think) which Maxima can now do, and we need to replace it with one Maxima can't do.  There is also a slight change in the numeric value because of this, but that wasn't the  point of that doctest.\n\nThe binomial issue seems easy to fix, but apparently now binomial(n,n)=1 for all n in Sage, but not in Maxima.  Should we change Sage, or do what Jason recommends (assume n>0 or something)?\n\nAnd in interfaces/maxima.py there are a lot of erros where Maxima loads like\n\n```\n    ;;; Loading #P\".../local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\".../local/lib/ecl/sysfun.lsp\"\n```\n\nas well as of course the Maxima version being wrong and, oddly, the following:\n\n```\nsage: maxima.eval('sage0: x == x;')\nExpected <Error>\nGot:\n    'x'\n```\n\nwhich is not good at all if real, but maybe just means Maxima changed something minor?\n\nThe plot3d one is not too significant, I think.  I haven't looked at the other ones.\n\nAnyway, obviously 'needs work' until someone posts a fairly comprehensive patch.",
    "created_at": "2010-04-29T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79648",
    "user": "https://github.com/kcrisman"
}
```

Yes, though I wouldn't say completely broken, since not every doctest fails, correct?  

Other issues:

In symbolic/integration/integral.py, there is one integral which has been improved, and one which seems to affected by the rational approximation thing, but wasn't before.   There is also an integral (in that file, I think) which Maxima can now do, and we need to replace it with one Maxima can't do.  There is also a slight change in the numeric value because of this, but that wasn't the  point of that doctest.

The binomial issue seems easy to fix, but apparently now binomial(n,n)=1 for all n in Sage, but not in Maxima.  Should we change Sage, or do what Jason recommends (assume n>0 or something)?

And in interfaces/maxima.py there are a lot of erros where Maxima loads like

```
    ;;; Loading #P".../local/lib/ecl/cmp.fas"
    ;;; Loading #P".../local/lib/ecl/sysfun.lsp"
```

as well as of course the Maxima version being wrong and, oddly, the following:

```
sage: maxima.eval('sage0: x == x;')
Expected <Error>
Got:
    'x'
```

which is not good at all if real, but maybe just means Maxima changed something minor?

The plot3d one is not too significant, I think.  I haven't looked at the other ones.

Anyway, obviously 'needs work' until someone posts a fairly comprehensive patch.



---

archive/issue_comments_079649.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-29T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79649",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079650.json:
```json
{
    "body": "Also, the spkg-install for the most recent spkg does not include the fix from #8645, as opposed to the one Jason posted.  That is crucial to close this ticket.",
    "created_at": "2010-04-29T00:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79650",
    "user": "https://github.com/kcrisman"
}
```

Also, the spkg-install for the most recent spkg does not include the fix from #8645, as opposed to the one Jason posted.  That is crucial to close this ticket.



---

archive/issue_comments_079651.json:
```json
{
    "body": "Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)",
    "created_at": "2010-04-29T19:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79651",
    "user": "https://github.com/robert-marik"
}
```

Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)



---

archive/issue_comments_079652.json:
```json
{
    "body": "Replying to [comment:17 robert.marik]:\n> Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)\n.... and it is already fixed in the CVS version (one-line fix)",
    "created_at": "2010-04-30T04:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79652",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:17 robert.marik]:
> Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)
.... and it is already fixed in the CVS version (one-line fix)



---

archive/issue_comments_079653.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T04:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79653",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079654.json:
```json
{
    "body": "A new spkg is up at: http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg\n\nThis spkg includes the upstream bugfix for the solve_rat_ineq issue noted above.",
    "created_at": "2010-05-13T04:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79654",
    "user": "https://github.com/jasongrout"
}
```

A new spkg is up at: http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg

This spkg includes the upstream bugfix for the solve_rat_ineq issue noted above.



---

archive/issue_comments_079655.json:
```json
{
    "body": "My 5.21.1 spkg also includes the fixes noted in the description.",
    "created_at": "2010-05-13T04:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79655",
    "user": "https://github.com/jasongrout"
}
```

My 5.21.1 spkg also includes the fixes noted in the description.



---

archive/issue_comments_079656.json:
```json
{
    "body": "This upgrade fixes #8729",
    "created_at": "2010-05-13T04:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79656",
    "user": "https://github.com/jasongrout"
}
```

This upgrade fixes #8729



---

archive/issue_comments_079657.json:
```json
{
    "body": "Attachment [trac-8731-maxima-upgrade.patch](tarball://root/attachments/some-uuid/ticket8731/trac-8731-maxima-upgrade.patch) by @jasongrout created at 2010-05-13 06:07:32\n\nThe doctests that still fail after the patch is applied (under ptestlong) are listed below:\n\n\n\nI couldn't find a way to double-check that the new answer is correct in the following output mismatch\n\n\n```\n\nsage -t -long \"4.4.1/devel/sage/sage/symbolic/integration/integral.py\"\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py\", line 464:\n    sage: integrate(sin(x)*cos(10*x)*log(x), x)\nExpected:\n    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)\nGot:\n    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)\n**********************************************************************\n```\n\n\n\nThe next doctest is testing that #780 is fixed.  Here, it appears that #780 is *not* fixed again.  However, the actual maxima bug that was fixed for #780 is still fixed.  The problem seems to be that we use keepfloat: true, and when we have keepfloat: true, the erroneous question pops up.\n\n\n```\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py\", line 486:\n    sage: res = integral(f,x,0.0001414, 1.); res\nException raised:\n    Traceback (most recent call last):\n      File \"/home/grout/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/grout/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/grout/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[56]>\", line 1, in <module>\n        res = integral(f,x,RealNumber('0.0001414'), RealNumber('1.')); res###line 486:\n    sage: res = integral(f,x,0.0001414, 1.); res\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/misc/functional.py\", line 720, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 7330, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:29048)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py\", line 589, in integrate\n        return definite_integral(expression, v, a, b)\n      File \"function.pyx\", line 425, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py\", line 174, in _eval_\n        return integrator(*args)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/external.py\", line 21, in maxima_integrator\n        result = expression._maxima_().integrate(v, a, b)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/maxima.py\", line 2112, in integral\n        return I(var, min, max)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1408, in __call__\n        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1316, in function_call\n        return self.new(s)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1097, in new\n        return self(code)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1032, in __call__\n        return cls(self, x, name=name)\n      File \"/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1451, in __init__\n        raise TypeError, x\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume((y-1)*(y+1)>0)' before integral or limit evaluation, for example):\n    Is  (y-1)*(y+1)  positive, negative, or zero?\n```\n\n\nHere is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back\n\n\n```\n% sage -maxima\n;;; Loading #P\"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas\"\n;;; Loading #P\"/home/grout/sage/local/lib/ecl/sockets.fas\"\n;;; Loading #P\"/home/grout/sage/local/lib/ecl/defsystem.fas\"\n;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\nMaxima 5.21.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.4.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) assume(y^2>1);\n                                     2\n(%o1)                              [y  > 1]\n(%i2) keepfloat: true;              \n(%o2)                                true\n(%i3) integrate(log(x^2+y^2),x,0,1);\n                               2               1\n                        2 log(y  + 1) + 4 atan(-) y - 4\n                                               y\n(%o3)                   -------------------------------\n                                       2\n(%i4) integrate(log(x^2+y^2),x,0.0001414,1);\nIs  (y - 1) (y + 1)  positive, negative, or zero?\n```\n\n\n\nThere is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?\n\n\n```\nsage -t -long \"4.4.1/devel/sage/sage/plot/plot3d/transform.pyx\"\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx\", line 217:\n    sage: m\nExpected:\n    [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]\n    [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]\n    [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]\nGot:\n    [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z)]\n    [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]\n    [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]\n**********************************************************************\n```\n\n\n\n\nThere are a few errors in the interfaces/maxima.py file.  These seem to all stem from more output, rather than actual errors.\n\n\n```\nsage -t -long \"4.4.1/devel/sage/sage/interfaces/maxima.py\"  \n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 871:\n    sage: maxima._command_runner('describe', 'gcd')\nExpected:\n    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n    ...\nGot:\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n    <BLANKLINE>\n     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n         Returns the greatest common divisor of <p_1> and <p_2>.  The flag\n         `gcd' determines which algorithm is employed.  Setting `gcd' to\n         `ez', `subres', `red', or `spmod' selects the `ezgcd',\n         subresultant `prs', reduced, or modular algorithm, respectively.\n         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1\n         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)\n         cause gcd's to be taken implicitly.  For homogeneous polynomials\n         it is recommended that `gcd' equal to `subres' be used.  To take\n         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -\n         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and\n         `gcd' must not be `ez'.\n    <BLANKLINE>\n         The `gcd' flag, default: `spmod', if `false' will also prevent the\n         greatest common divisor from being taken when expressions are\n         converted to canonical rational expression (CRE) form.  This will\n         sometimes speed the calculation if gcds are not required.\n    <BLANKLINE>\n    <BLANKLINE>\n      There are also some inexact matches for `gcd'.\n      Try `?? gcd' to see them.\n    <BLANKLINE>\n                                         true\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 896:\n    sage: maxima.help('gcd')\nExpected:\n    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n    ...\nGot:\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n    <BLANKLINE>\n     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n         Returns the greatest common divisor of <p_1> and <p_2>.  The flag\n         `gcd' determines which algorithm is employed.  Setting `gcd' to\n         `ez', `subres', `red', or `spmod' selects the `ezgcd',\n         subresultant `prs', reduced, or modular algorithm, respectively.\n         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1\n         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)\n         cause gcd's to be taken implicitly.  For homogeneous polynomials\n         it is recommended that `gcd' equal to `subres' be used.  To take\n         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -\n         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and\n         `gcd' must not be `ez'.\n    <BLANKLINE>\n         The `gcd' flag, default: `spmod', if `false' will also prevent the\n         greatest common divisor from being taken when expressions are\n         converted to canonical rational expression (CRE) form.  This will\n         sometimes speed the calculation if gcds are not required.\n    <BLANKLINE>\n    <BLANKLINE>\n      There are also some inexact matches for `gcd'.\n      Try `?? gcd' to see them.\n    <BLANKLINE>\n                                         true\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 906:\n    sage: maxima.example('arrays')\nExpected:\n    a[n]:=n*a[n-1]\n                                    a  := n a\n                                     n       n - 1\n    a[0]:1\n    a[5]\n                                          120\n    a[n]:=n\n    a[6]\n                                           6\n    a[4]\n                                          24\n                                         done\nGot:\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n    a[n]:=n*a[n-1]\n                                    a  := n a\n                                     n       n - 1\n    a[0]:1\n    a[5]\n                                          120\n    a[n]:=n\n    a[6]\n                                           6\n    a[4]\n                                          24\n                                         done\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 2384:\n    sage: m.gcd._sage_doc_()\nExpected:\n    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n    ...\nGot:\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n    <BLANKLINE>\n     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n         Returns the greatest common divisor of <p_1> and <p_2>.  The flag\n         `gcd' determines which algorithm is employed.  Setting `gcd' to\n         `ez', `subres', `red', or `spmod' selects the `ezgcd',\n         subresultant `prs', reduced, or modular algorithm, respectively.\n         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1\n         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)\n         cause gcd's to be taken implicitly.  For homogeneous polynomials\n         it is recommended that `gcd' equal to `subres' be used.  To take\n         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -\n         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and\n         `gcd' must not be `ez'.\n    <BLANKLINE>\n         The `gcd' flag, default: `spmod', if `false' will also prevent the\n         greatest common divisor from being taken when expressions are\n         converted to canonical rational expression (CRE) form.  This will\n         sometimes speed the calculation if gcds are not required.\n    <BLANKLINE>\n    <BLANKLINE>\n      There are also some inexact matches for `gcd'.\n      Try `?? gcd' to see them.\n    <BLANKLINE>\n                                         true\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 2395:\n    sage: maxima.gcd._sage_doc_()\nExpected:\n    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n    ...\nGot:\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n    ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n    <BLANKLINE>\n     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)\n         Returns the greatest common divisor of <p_1> and <p_2>.  The flag\n         `gcd' determines which algorithm is employed.  Setting `gcd' to\n         `ez', `subres', `red', or `spmod' selects the `ezgcd',\n         subresultant `prs', reduced, or modular algorithm, respectively.\n         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1\n         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)\n         cause gcd's to be taken implicitly.  For homogeneous polynomials\n         it is recommended that `gcd' equal to `subres' be used.  To take\n         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -\n         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and\n         `gcd' must not be `ez'.\n    <BLANKLINE>\n         The `gcd' flag, default: `spmod', if `false' will also prevent the\n         greatest common divisor from being taken when expressions are\n         converted to canonical rational expression (CRE) form.  This will\n         sometimes speed the calculation if gcds are not required.\n    <BLANKLINE>\n    <BLANKLINE>\n      There are also some inexact matches for `gcd'.\n      Try `?? gcd' to see them.\n    <BLANKLINE>\n                                         true\n    <BLANKLINE>\n```\n\n\nFinally, I'm not sure what is happening in this error:\n\n\n```\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py\", line 729:\n    sage: maxima.eval('sage0: x == x;')\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: error evaluating \"sage0: x == x;\":...\nGot:\n    'x'\n**********************************************************************\n```\n",
    "created_at": "2010-05-13T06:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79657",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8731-maxima-upgrade.patch](tarball://root/attachments/some-uuid/ticket8731/trac-8731-maxima-upgrade.patch) by @jasongrout created at 2010-05-13 06:07:32

The doctests that still fail after the patch is applied (under ptestlong) are listed below:



I couldn't find a way to double-check that the new answer is correct in the following output mismatch


```

sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
**********************************************************************
```



The next doctest is testing that #780 is fixed.  Here, it appears that #780 is *not* fixed again.  However, the actual maxima bug that was fixed for #780 is still fixed.  The problem seems to be that we use keepfloat: true, and when we have keepfloat: true, the erroneous question pops up.


```
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 486:
    sage: res = integral(f,x,0.0001414, 1.); res
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[56]>", line 1, in <module>
        res = integral(f,x,RealNumber('0.0001414'), RealNumber('1.')); res###line 486:
    sage: res = integral(f,x,0.0001414, 1.); res
      File "/home/grout/sage/local/lib/python/site-packages/sage/misc/functional.py", line 720, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 7330, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:29048)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 589, in integrate
        return definite_integral(expression, v, a, b)
      File "function.pyx", line 425, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 174, in _eval_
        return integrator(*args)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
        result = expression._maxima_().integrate(v, a, b)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2112, in integral
        return I(var, min, max)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1408, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1316, in function_call
        return self.new(s)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1097, in new
        return self(code)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1032, in __call__
        return cls(self, x, name=name)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1451, in __init__
        raise TypeError, x
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume((y-1)*(y+1)>0)' before integral or limit evaluation, for example):
    Is  (y-1)*(y+1)  positive, negative, or zero?
```


Here is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back


```
% sage -maxima
;;; Loading #P"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/sockets.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.21.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) assume(y^2>1);
                                     2
(%o1)                              [y  > 1]
(%i2) keepfloat: true;              
(%o2)                                true
(%i3) integrate(log(x^2+y^2),x,0,1);
                               2               1
                        2 log(y  + 1) + 4 atan(-) y - 4
                                               y
(%o3)                   -------------------------------
                                       2
(%i4) integrate(log(x^2+y^2),x,0.0001414,1);
Is  (y - 1) (y + 1)  positive, negative, or zero?
```



There is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?


```
sage -t -long "4.4.1/devel/sage/sage/plot/plot3d/transform.pyx"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx", line 217:
    sage: m
Expected:
    [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]
    [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]
    [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]
Got:
    [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z)]
    [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]
    [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]
**********************************************************************
```




There are a few errors in the interfaces/maxima.py file.  These seem to all stem from more output, rather than actual errors.


```
sage -t -long "4.4.1/devel/sage/sage/interfaces/maxima.py"  
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 871:
    sage: maxima._command_runner('describe', 'gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 896:
    sage: maxima.help('gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 906:
    sage: maxima.example('arrays')
Expected:
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 2384:
    sage: m.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 2395:
    sage: maxima.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
```


Finally, I'm not sure what is happening in this error:


```
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 729:
    sage: maxima.eval('sage0: x == x;')
Expected:
    Traceback (most recent call last):
    ...
    TypeError: error evaluating "sage0: x == x;":...
Got:
    'x'
**********************************************************************
```




---

archive/issue_comments_079658.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-13T06:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79658",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079659.json:
```json
{
    "body": "Thanks for the comprehensive report; I had my own private list of these from a few weeks ago, but had not had time to look into all of them yet.\n\nI think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.",
    "created_at": "2010-05-13T12:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79659",
    "user": "https://github.com/kcrisman"
}
```

Thanks for the comprehensive report; I had my own private list of these from a few weeks ago, but had not had time to look into all of them yet.

I think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.



---

archive/issue_comments_079660.json:
```json
{
    "body": "Replying to [comment:23 kcrisman]:\n\n\n> I think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.\n\nWell, I wouldn't be surprised if those extra lines actually came from the updated ECL package, given what the messages are.",
    "created_at": "2010-05-13T12:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79660",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:23 kcrisman]:


> I think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.

Well, I wouldn't be surprised if those extra lines actually came from the updated ECL package, given what the messages are.



---

archive/issue_comments_079661.json:
```json
{
    "body": "Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!",
    "created_at": "2010-05-13T12:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79661",
    "user": "https://github.com/kcrisman"
}
```

Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!



---

archive/issue_comments_079662.json:
```json
{
    "body": "With the new ECL and the new Maxima, I no longer get the error messages about installing a .fas or .fasb file.  That is good.\n\nAnyway, doctest should just be changed for the loading thing, regardless of where it does it.  All documentation requests do that, as does running maxima_console().  Unless... before, maxima_console() gave three loading statements, the last two of which are the ones which show up in your examples.  Now there are five, but the top two are new... are we stripping away three load statements in the output, but not more?  Just a wild idea.\n\nAs for the last error, here it is in the maxima_console() - something's not going right.\n\n```\nMaxima 5.21.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.4.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) sage0: x==x;\n\nstdin:1289935:incorrect syntax: = is not a prefix operator\n(%i1) (%o1)                                  x\n```\n\nYet in the previous one we get\n\n```\nMaxima 5.20.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.2.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) sage0: x==x;\n\nstdin:1373:Incorrect syntax: = is not a prefix operator\n(%i1) (%o1)                                  x\n```\n\nwhich sure looks the same to me, yet Sage catches it correctly before and not now!  What the heck?",
    "created_at": "2010-05-13T13:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79662",
    "user": "https://github.com/kcrisman"
}
```

With the new ECL and the new Maxima, I no longer get the error messages about installing a .fas or .fasb file.  That is good.

Anyway, doctest should just be changed for the loading thing, regardless of where it does it.  All documentation requests do that, as does running maxima_console().  Unless... before, maxima_console() gave three loading statements, the last two of which are the ones which show up in your examples.  Now there are five, but the top two are new... are we stripping away three load statements in the output, but not more?  Just a wild idea.

As for the last error, here it is in the maxima_console() - something's not going right.

```
Maxima 5.21.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) sage0: x==x;

stdin:1289935:incorrect syntax: = is not a prefix operator
(%i1) (%o1)                                  x
```

Yet in the previous one we get

```
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) sage0: x==x;

stdin:1373:Incorrect syntax: = is not a prefix operator
(%i1) (%o1)                                  x
```

which sure looks the same to me, yet Sage catches it correctly before and not now!  What the heck?



---

archive/issue_comments_079663.json:
```json
{
    "body": "Before, there was a lowercase \"i\", now it is upper-case in \"Incorrect\".  Maybe that's the problem.",
    "created_at": "2010-05-14T00:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79663",
    "user": "https://github.com/jasongrout"
}
```

Before, there was a lowercase "i", now it is upper-case in "Incorrect".  Maybe that's the problem.



---

archive/issue_comments_079664.json:
```json
{
    "body": "Oh yes, I should have seen that.  A quick search_src doesn't reveal anything useful, though.",
    "created_at": "2010-05-14T00:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79664",
    "user": "https://github.com/kcrisman"
}
```

Oh yes, I should have seen that.  A quick search_src doesn't reveal anything useful, though.



---

archive/issue_comments_079665.json:
```json
{
    "body": "Regarding the other errors:\n\nReplying to [comment:22 jason]:\n> The doctests that still fail after the patch is applied (under ptestlong) are listed below:\n> \n> \n> \n> I couldn't find a way to double-check that the new answer is correct in the following output mismatch\n> \n\n```\n\nsage -t -long \"4.4.1/devel/sage/sage/symbolic/integration/integral.py\"\n**********************************************************************\nFile \"/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py\", line 464:\n    sage: integrate(sin(x)*cos(10*x)*log(x), x)\nExpected:\n    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)\nGot:\n    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)\n**********************************************************************\n```\n\nThis is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.\n\n\n> Here is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back\n> \n> {{{\n> % sage -maxima\n> ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas\"\n> ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sockets.fas\"\n> ;;; Loading #P\"/home/grout/sage/local/lib/ecl/defsystem.fas\"\n> ;;; Loading #P\"/home/grout/sage/local/lib/ecl/cmp.fas\"\n> ;;; Loading #P\"/home/grout/sage/local/lib/ecl/sysfun.lsp\"\n> Maxima 5.21.1 http://maxima.sourceforge.net\n> using Lisp ECL 10.4.1\n> Distributed under the GNU Public License. See the file COPYING.\n> Dedicated to the memory of William Schelter.\n> The function bug_report() provides bug reporting information.\n> (%i1) assume(y^2>1);\n>                                      2\n> (%o1)                              [y  > 1]\n> (%i2) keepfloat: true;              \n> (%o2)                                true\n> (%i3) integrate(log(x<sup>2+y</sup>2),x,0,1);\n>                                2               1\n>                         2 log(y  + 1) + 4 atan(-) y - 4\n>                                                y\n> (%o3)                   -------------------------------\n>                                        2\n> (%i4) integrate(log(x<sup>2+y</sup>2),x,0.0001414,1);\n> Is  (y - 1) (y + 1)  positive, negative, or zero?\n> }}}\n> \n\nI'm not sure what to do with this.  keepfloat is so annoying.\n\n> \n> There is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?\n> \n> {{{\n> sage -t -long \"4.4.1/devel/sage/sage/plot/plot3d/transform.pyx\"\n> **********************************************************************\n> File \"/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx\", line 217:\n>     sage: m\n> Expected:\n>     [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]\n>     [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]\n>     [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]\n> Got:\n>     [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z)]\n>     [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]\n>     [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]\n> **********************************************************************\n> }}}\n> \n\nI believe this is all related to a change made in how sqrt behaves with respect to factors (sqrt(ab) and sqrt(a), sqrt(b)) and whether an I gets factored out or not. They all come down to the same essential things:\n\n```\n-(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x\n-((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) \n```\n\n\n```\n- sqrt(z^2)*sin(theta)\n- I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)\n```\n\nThe latter seems ok immediately (or at least no worse than other decision made for us about which root of -1 to choose), but even given that $x<sup>2+y</sup>2+z^2=1$, which is asserted earlier in the file, I can't quite make out the former. I'll look into this a little more.",
    "created_at": "2010-05-25T15:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79665",
    "user": "https://github.com/kcrisman"
}
```

Regarding the other errors:

Replying to [comment:22 jason]:
> The doctests that still fail after the patch is applied (under ptestlong) are listed below:
> 
> 
> 
> I couldn't find a way to double-check that the new answer is correct in the following output mismatch
> 

```

sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
**********************************************************************
```

This is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.


> Here is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back
> 
> {{{
> % sage -maxima
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sockets.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/defsystem.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
> Maxima 5.21.1 http://maxima.sourceforge.net
> using Lisp ECL 10.4.1
> Distributed under the GNU Public License. See the file COPYING.
> Dedicated to the memory of William Schelter.
> The function bug_report() provides bug reporting information.
> (%i1) assume(y^2>1);
>                                      2
> (%o1)                              [y  > 1]
> (%i2) keepfloat: true;              
> (%o2)                                true
> (%i3) integrate(log(x<sup>2+y</sup>2),x,0,1);
>                                2               1
>                         2 log(y  + 1) + 4 atan(-) y - 4
>                                                y
> (%o3)                   -------------------------------
>                                        2
> (%i4) integrate(log(x<sup>2+y</sup>2),x,0.0001414,1);
> Is  (y - 1) (y + 1)  positive, negative, or zero?
> }}}
> 

I'm not sure what to do with this.  keepfloat is so annoying.

> 
> There is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?
> 
> {{{
> sage -t -long "4.4.1/devel/sage/sage/plot/plot3d/transform.pyx"
> **********************************************************************
> File "/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx", line 217:
>     sage: m
> Expected:
>     [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]
>     [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]
>     [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]
> Got:
>     [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z)]
>     [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]
>     [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]
> **********************************************************************
> }}}
> 

I believe this is all related to a change made in how sqrt behaves with respect to factors (sqrt(ab) and sqrt(a), sqrt(b)) and whether an I gets factored out or not. They all come down to the same essential things:

```
-(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x
-((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) 
```


```
- sqrt(z^2)*sin(theta)
- I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)
```

The latter seems ok immediately (or at least no worse than other decision made for us about which root of -1 to choose), but even given that $x<sup>2+y</sup>2+z^2=1$, which is asserted earlier in the file, I can't quite make out the former. I'll look into this a little more.



---

archive/issue_comments_079666.json:
```json
{
    "body": "Replying to [comment:25 kcrisman]:\n> Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!\nNow remember to use #8951 first.",
    "created_at": "2010-05-25T15:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79666",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:25 kcrisman]:
> Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!
Now remember to use #8951 first.



---

archive/issue_comments_079667.json:
```json
{
    "body": "> sage -t -long \"4.4.1/devel/sage/sage/symbolic/integration/integral.py\"\n> **********************************************************************\n> File \"/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py\", line 464:\n>     sage: integrate(sin(x)*cos(10*x)*log(x), x)\n> Expected:\n>     1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)\n> Got:\n>     1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)\n> **********************************************************************\n> }}}\n> This is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.\n \nBurcin has also already pointed this out at #8624.",
    "created_at": "2010-05-25T16:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79667",
    "user": "https://github.com/kcrisman"
}
```

> sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
> **********************************************************************
> File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
>     sage: integrate(sin(x)*cos(10*x)*log(x), x)
> Expected:
>     1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
> Got:
>     1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
> **********************************************************************
> }}}
> This is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.
 
Burcin has also already pointed this out at #8624.



---

archive/issue_comments_079668.json:
```json
{
    "body": "I get the following on Mac OSX 10.6 on Intel (see the patch for the which test):\n\n```\n    sage: h.n()\nExpected:\n    0.075715991017028972\nGot:\n    0.075715991017028958\n```\n",
    "created_at": "2010-05-25T17:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79668",
    "user": "https://github.com/kcrisman"
}
```

I get the following on Mac OSX 10.6 on Intel (see the patch for the which test):

```
    sage: h.n()
Expected:
    0.075715991017028972
Got:
    0.075715991017028958
```




---

archive/issue_comments_079669.json:
```json
{
    "body": "That h.n() doctest is interesting.  (From what I recall when I investigated it) the old maxima agreed with both mathematica and mpmath, but the new maxima is off in the last few digits---it might be worth checking into, though it may just be numerical error.",
    "created_at": "2010-05-28T03:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79669",
    "user": "https://github.com/jasongrout"
}
```

That h.n() doctest is interesting.  (From what I recall when I investigated it) the old maxima agreed with both mathematica and mpmath, but the new maxima is off in the last few digits---it might be worth checking into, though it may just be numerical error.



---

archive/issue_comments_079670.json:
```json
{
    "body": "(but those h.n() errors I talked about were for the old sin function, not the new tan function, IIRC)",
    "created_at": "2010-05-28T03:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79670",
    "user": "https://github.com/jasongrout"
}
```

(but those h.n() errors I talked about were for the old sin function, not the new tan function, IIRC)



---

archive/issue_comments_079671.json:
```json
{
    "body": "Replying to [comment:12 was]:\n\nIt may be useful to note that all the doctests that fail with maxima.5.21.1 and ecl.10.4.1, pass with maxima.5.20.1.p1 from #8645. So, ecl.10.4.1 is not of influence. All changes in doctest responses are due to changes in maxima.",
    "created_at": "2010-06-21T05:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79671",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:12 was]:

It may be useful to note that all the doctests that fail with maxima.5.21.1 and ecl.10.4.1, pass with maxima.5.20.1.p1 from #8645. So, ecl.10.4.1 is not of influence. All changes in doctest responses are due to changes in maxima.



---

archive/issue_comments_079672.json:
```json
{
    "body": "> And in interfaces/maxima.py there are a lot of erros where Maxima loads like\n> {{{\n>     ;;; Loading #P\".../local/lib/ecl/cmp.fas\"\n>     ;;; Loading #P\".../local/lib/ecl/sysfun.lsp\"\n> }}}\n\nIt's actually possible to turn messages like this off. If you're driving maxima via a pexpect interface, that might be the proper thing to do. The key is the \"Common Lisp HyperSpec\", the de facto official CL documentation. Looking at `load` leads to the global variable `*load-verbose*`:\n\nhttp://www.lispworks.com/documentation/HyperSpec/Body/v_ld_prs.htm#STload-verboseST\n\nIt's on by default in ECL, but can be turned off:\n\n\n```\nECL (Embeddable Common-Lisp) 10.4.1\nCopyright (C) 1984 Taiichi Yuasa and Masami Hagiya\nCopyright (C) 1993 Giuseppe Attardi\nCopyright (C) 2000 Juan J. Garcia-Ripoll\nECL is free software, and you are welcome to redistribute it\nunder certain conditions; see file 'Copyright' for details.\nType :h for Help.  \nTop level.\n> (require 'maxima)\n\n;;; Loading #P\"/mnt/usb1/scratch/nbruin/sage-4.4.3/local/lib/ecl/maxima.fas\"\n(\"MAXIMA\")\n```\n\n\n\n```\nECL (Embeddable Common-Lisp) 10.4.1\nCopyright (C) 1984 Taiichi Yuasa and Masami Hagiya\nCopyright (C) 1993 Giuseppe Attardi\nCopyright (C) 2000 Juan J. Garcia-Ripoll\nECL is free software, and you are welcome to redistribute it\nunder certain conditions; see file 'Copyright' for details.\nType :h for Help.  \nTop level.\n> *load-verbose*\n\nT\n> (setf *load-verbose* NIL)\n\nNIL\n> (require 'maxima)\n\n(\"MAXIMA\")\n```\n",
    "created_at": "2010-06-21T18:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79672",
    "user": "https://github.com/nbruin"
}
```

> And in interfaces/maxima.py there are a lot of erros where Maxima loads like
> {{{
>     ;;; Loading #P".../local/lib/ecl/cmp.fas"
>     ;;; Loading #P".../local/lib/ecl/sysfun.lsp"
> }}}

It's actually possible to turn messages like this off. If you're driving maxima via a pexpect interface, that might be the proper thing to do. The key is the "Common Lisp HyperSpec", the de facto official CL documentation. Looking at `load` leads to the global variable `*load-verbose*`:

http://www.lispworks.com/documentation/HyperSpec/Body/v_ld_prs.htm#STload-verboseST

It's on by default in ECL, but can be turned off:


```
ECL (Embeddable Common-Lisp) 10.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  
Top level.
> (require 'maxima)

;;; Loading #P"/mnt/usb1/scratch/nbruin/sage-4.4.3/local/lib/ecl/maxima.fas"
("MAXIMA")
```



```
ECL (Embeddable Common-Lisp) 10.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  
Top level.
> *load-verbose*

T
> (setf *load-verbose* NIL)

NIL
> (require 'maxima)

("MAXIMA")
```




---

archive/issue_comments_079673.json:
```json
{
    "body": "Note to eventual author of patch - please confirm here that #8729 is fixed when writing doctests.",
    "created_at": "2010-06-25T13:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79673",
    "user": "https://github.com/kcrisman"
}
```

Note to eventual author of patch - please confirm here that #8729 is fixed when writing doctests.



---

archive/issue_comments_079674.json:
```json
{
    "body": "With 4.5.alpha4 + http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg + [attachment:trac-8731-maxima-upgrade.patch], the long tests on sage.math give reproducible failures in\n\n```\n        sage -t -long  devel/sage/sage/calculus/calculus.py # 1 doctests failed\n        sage -t -long  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed\n        sage -t -long  devel/sage/sage/interfaces/maxima.py # 6 doctests failed\n        sage -t -long  devel/sage/sage/symbolic/integration/integral.py # 4 doctests failed\n```\n\nThe full raw test log is [here](http://sage.math.washington.edu/home/mpatel/trac/8731/ptestlong_4.5.alpha4.log).",
    "created_at": "2010-07-11T08:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79674",
    "user": "https://github.com/qed777"
}
```

With 4.5.alpha4 + http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg + [attachment:trac-8731-maxima-upgrade.patch], the long tests on sage.math give reproducible failures in

```
        sage -t -long  devel/sage/sage/calculus/calculus.py # 1 doctests failed
        sage -t -long  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
        sage -t -long  devel/sage/sage/interfaces/maxima.py # 6 doctests failed
        sage -t -long  devel/sage/sage/symbolic/integration/integral.py # 4 doctests failed
```

The full raw test log is [here](http://sage.math.washington.edu/home/mpatel/trac/8731/ptestlong_4.5.alpha4.log).



---

archive/issue_comments_079675.json:
```json
{
    "body": "Just FYI:\n\n```\n\nMessage: 4\nDate: Sun, 1 Aug 2010 15:39:28 -0600\nFrom: Robert Dodier <robert.dodier@gmail.com>\nTo: Maxima Mailing List <maxima@math.utexas.edu>\nSubject: [Maxima] Maxima 5.22.0\nMessage-ID:\n       <AANLkTimGPxt1uLWDmFEVUgDU8nxByJ=V00Fxk4o2_3yc@mail.gmail.com>\nContent-Type: text/plain; charset=ISO-8859-1\n\nHi, I;ve tagged version-5_22_0 in CVS and built rpms\nand tar.gz and upload them all to SF.\nShould be available real soon now at:\nhttp://sourceforge.net/projects/maxima/files/\n(looks like the list hasn't been refreshed yet, I don't\nknow what the refresh schedule is)\n\nIf someone can build & upload a Windows installer that\nwould be great.\n\nAs ever please give the new version a try and if/when\nthere aren't too many complaints I'll make a general announcement.\n\nbest\n\nRobert Dodier\n```\n\nSo maybe we should change this ticket to 5.22.0 if they don't get too many problems with it?",
    "created_at": "2010-08-02T14:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79675",
    "user": "https://github.com/kcrisman"
}
```

Just FYI:

```

Message: 4
Date: Sun, 1 Aug 2010 15:39:28 -0600
From: Robert Dodier <robert.dodier@gmail.com>
To: Maxima Mailing List <maxima@math.utexas.edu>
Subject: [Maxima] Maxima 5.22.0
Message-ID:
       <AANLkTimGPxt1uLWDmFEVUgDU8nxByJ=V00Fxk4o2_3yc@mail.gmail.com>
Content-Type: text/plain; charset=ISO-8859-1

Hi, I;ve tagged version-5_22_0 in CVS and built rpms
and tar.gz and upload them all to SF.
Should be available real soon now at:
http://sourceforge.net/projects/maxima/files/
(looks like the list hasn't been refreshed yet, I don't
know what the refresh schedule is)

If someone can build & upload a Windows installer that
would be great.

As ever please give the new version a try and if/when
there aren't too many complaints I'll make a general announcement.

best

Robert Dodier
```

So maybe we should change this ticket to 5.22.0 if they don't get too many problems with it?



---

archive/issue_comments_079676.json:
```json
{
    "body": "And now the latest is 5.22.1.",
    "created_at": "2010-08-12T16:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79676",
    "user": "https://github.com/kcrisman"
}
```

And now the latest is 5.22.1.



---

archive/issue_comments_079677.json:
```json
{
    "body": "This will probably also fix #8582.",
    "created_at": "2010-09-22T14:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79677",
    "user": "https://github.com/kcrisman"
}
```

This will probably also fix #8582.



---

archive/issue_comments_079678.json:
```json
{
    "body": "Just FYI on this ticket - from an email on the Maxima list by Robert Dodier:\n\n```\nThe next release is planned for December, with the release branch\n(5.23) on Dec 1 or soon thereafter, with a stable release to follow\naround Christmas.\n```\n",
    "created_at": "2010-10-15T17:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79678",
    "user": "https://github.com/kcrisman"
}
```

Just FYI on this ticket - from an email on the Maxima list by Robert Dodier:

```
The next release is planned for December, with the release branch
(5.23) on Dec 1 or soon thereafter, with a stable release to follow
around Christmas.
```




---

archive/issue_comments_079679.json:
```json
{
    "body": "As sooner or later maxima would have to be updated to 5.22 or newer I decided to share my experiences of first approach to update to it. I wanted to try 5.22 because it's first version that supports inversion of error function, and first to support integrals of form abs(x) from 0 to a without assumptions. I based on patch by Jason for 5.21 and wanted to reach at least same level of failures as with 5.21. Unfortunately, I got stuck at one place - maxima hangs in some situations. I tracked that to this difference:\n\nbefore it was\n\n```\nsage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp\n;;; Loading #P\"/opt/sage/local/lib/ecl/defsystem.fas\"\n;;; Loading #P\"/opt/sage/local/lib/ecl/cmp.fas\"\n;;; Loading #P\"/opt/sage/local/lib/ecl/sysfun.lsp\"\nMaxima 5.20.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.2.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) 0;\n<sage-display>(%o1)                                  0\n(%i2) sage0: x==x;\nIncorrect syntax: = is not a prefix operator\n(%i2) <sage-display>(%o2)                                  x\n```\n\nand now it is\n\n```\n./sage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp\n;;; Loading #P\"/home/giniu/dev/sage/local/lib/ecl/sb-bsd-sockets.fas\"\n;;; Loading #P\"/home/giniu/dev/sage/local/lib/ecl/sockets.fas\"\n;;; Loading #P\"/home/giniu/dev/sage/local/lib/ecl/defsystem.fas\"\n;;; Loading #P\"/home/giniu/dev/sage/local/lib/ecl/cmp.fas\"\n;;; Loading #P\"/home/giniu/dev/sage/local/lib/ecl/sysfun.lsp\"\nMaxima 5.22.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.4.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) 0;\n<sage-display>(%o1)                                  0\n(%i2) sage0: x==x;\nincorrect syntax: = is not a prefix operator\nsage0: x==\n        ^\n```\n\n\nwhich makes Sage wait for \"<sage-display>\" forever.\n\nI made spkg: http://lab15.im.pwr.wroc.pl/~giniew/maxima-5.22.1.spkg and patch - http://lab15.im.pwr.wroc.pl/~giniew/trac-8731-maxima-upgrade-to-5.22.1.patch - those are not working but I'm attaching them in case someone wants to pick up from here - as I said I gave up for now.\n\n(btw, the doctest that was failing in devel/sage/sage/calculus/calculus.py is just different grouping, checked it and added new version to doctest, and there is one new doctest failure in devel/sage/sage/calculus/calculus.py that fails because maxima can integrate abs(x) in x from 0 to any a and returns correct 1/2*a*abs(a). There was also change to how logcontract works, they don't make full rational simplification now. I added one more step of rational simplification to simplify_full to simplify it more, though it might change some results.)",
    "created_at": "2010-10-29T16:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79679",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

As sooner or later maxima would have to be updated to 5.22 or newer I decided to share my experiences of first approach to update to it. I wanted to try 5.22 because it's first version that supports inversion of error function, and first to support integrals of form abs(x) from 0 to a without assumptions. I based on patch by Jason for 5.21 and wanted to reach at least same level of failures as with 5.21. Unfortunately, I got stuck at one place - maxima hangs in some situations. I tracked that to this difference:

before it was

```
sage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp
;;; Loading #P"/opt/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/opt/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/opt/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 0;
<sage-display>(%o1)                                  0
(%i2) sage0: x==x;
Incorrect syntax: = is not a prefix operator
(%i2) <sage-display>(%o2)                                  x
```

and now it is

```
./sage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sockets.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.22.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 0;
<sage-display>(%o1)                                  0
(%i2) sage0: x==x;
incorrect syntax: = is not a prefix operator
sage0: x==
        ^
```


which makes Sage wait for "<sage-display>" forever.

I made spkg: http://lab15.im.pwr.wroc.pl/~giniew/maxima-5.22.1.spkg and patch - http://lab15.im.pwr.wroc.pl/~giniew/trac-8731-maxima-upgrade-to-5.22.1.patch - those are not working but I'm attaching them in case someone wants to pick up from here - as I said I gave up for now.

(btw, the doctest that was failing in devel/sage/sage/calculus/calculus.py is just different grouping, checked it and added new version to doctest, and there is one new doctest failure in devel/sage/sage/calculus/calculus.py that fails because maxima can integrate abs(x) in x from 0 to any a and returns correct 1/2*a*abs(a). There was also change to how logcontract works, they don't make full rational simplification now. I added one more step of rational simplification to simplify_full to simplify it more, though it might change some results.)



---

archive/issue_comments_079680.json:
```json
{
    "body": "See #10187 for up-to-date ecl/maxima spkgs and a workaround to the `sage-display` issue.",
    "created_at": "2010-10-29T23:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79680",
    "user": "https://github.com/vbraun"
}
```

See #10187 for up-to-date ecl/maxima spkgs and a workaround to the `sage-display` issue.



---

archive/issue_comments_079681.json:
```json
{
    "body": "Close as a duplicate of #10187. The latter ticket upgrades Maxima to version 5.22.1.",
    "created_at": "2010-12-06T11:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as a duplicate of #10187. The latter ticket upgrades Maxima to version 5.22.1.



---

archive/issue_comments_079682.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-12-06T11:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8731#issuecomment-79682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
