# Issue 812: add Pollack/Stevens overconvergent modular symbols code

archive/issues_000812.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @loefflerd @roed314 @craigcitro @categorie\n\nKeywords: p-adic L-functions\n\nI'm just starting to work on implementing Pollack & Stevens' methods for using overconvergent modular symbols for p-adic L-functions, Stark-Heegner points, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/812\n\n",
    "created_at": "2007-10-03T18:12:33Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "add Pollack/Stevens overconvergent modular symbols code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/812",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @loefflerd @roed314 @craigcitro @categorie

Keywords: p-adic L-functions

I'm just starting to work on implementing Pollack & Stevens' methods for using overconvergent modular symbols for p-adic L-functions, Stark-Heegner points, etc.

Issue created by migration from https://trac.sagemath.org/ticket/812





---

archive/issue_comments_004897.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-03T18:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4897",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004898.json:
```json
{
    "body": "Craig,\n\nI know I must be bothering you by now, but what is the status here?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T04:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig,

I know I must be bothering you by now, but what is the status here?

Cheers,

Michael



---

archive/issue_comments_004899.json:
```json
{
    "body": "Could somebody post a link to the Magma code here?",
    "created_at": "2009-06-25T09:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4899",
    "user": "https://github.com/williamstein"
}
```

Could somebody post a link to the Magma code here?



---

archive/issue_comments_004900.json:
```json
{
    "body": "Sure,\nit's part of the \"shp package\" at:\n\nhttp://www.math.mcgill.ca/darmon/programs/shp/shp.html",
    "created_at": "2009-11-20T21:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4900",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Sure,
it's part of the "shp package" at:

http://www.math.mcgill.ca/darmon/programs/shp/shp.html



---

archive/issue_comments_004901.json:
```json
{
    "body": "From Jennifer Balakrishnan:\n\nRob Pollack just ported over some of his p-adic L-series via\noverconvergent modular symbols code to Sage, which could be very\nuseful for our p-adic BSD paper.\n\nThe code he sent me originally didn't quite produce results matching\nour data, but I've worked on it over the last few days, fixed a few\nbugs, noticed a few more, and thought this might be a good coding\nsprint project for us this week.\n\nHere's where the code currently stands:\n-- it can compute the p-adic L-series in the split p case (with data\nmatching what we've already computed naively)\n-- Rob says inert p is straightforward, just a matter of knowing how\nto call the right objects in Sage, which I think I can do\n-- I've tested it against the regulators I computed in my thesis, and\nwe can easily produce 10+ digits of precision in the L-value!!\n-- for some primes, it results in memory errors (I've put examples,\nworking and not, in the docstring in the test file). I'm not sure how\nto fix these.\n\nAs an enhancement, maybe we could also use some of your very fast code\nfor modular symbols?\n\nPerhaps most mathematically interesting, the special values computed\nby his program also result in the same +/-1 \"sign\" in the BSD formula\nthat our previous methods produced!\n\nThe code is available here:\n\nhttp://sage.math.washington.edu/home/jen/OMS\n\nTo run it, attach master.sage and Jen/test_run_generic.sage. The\nsecond file (http://sage.math.washington.edu/home/jen/OMS/Jen/test_run_generic.sage)\nhas some examples in the docstring.\n\nJen",
    "created_at": "2012-02-20T18:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4901",
    "user": "https://github.com/williamstein"
}
```

From Jennifer Balakrishnan:

Rob Pollack just ported over some of his p-adic L-series via
overconvergent modular symbols code to Sage, which could be very
useful for our p-adic BSD paper.

The code he sent me originally didn't quite produce results matching
our data, but I've worked on it over the last few days, fixed a few
bugs, noticed a few more, and thought this might be a good coding
sprint project for us this week.

Here's where the code currently stands:
-- it can compute the p-adic L-series in the split p case (with data
matching what we've already computed naively)
-- Rob says inert p is straightforward, just a matter of knowing how
to call the right objects in Sage, which I think I can do
-- I've tested it against the regulators I computed in my thesis, and
we can easily produce 10+ digits of precision in the L-value!!
-- for some primes, it results in memory errors (I've put examples,
working and not, in the docstring in the test file). I'm not sure how
to fix these.

As an enhancement, maybe we could also use some of your very fast code
for modular symbols?

Perhaps most mathematically interesting, the special values computed
by his program also result in the same +/-1 "sign" in the BSD formula
that our previous methods produced!

The code is available here:

http://sage.math.washington.edu/home/jen/OMS

To run it, attach master.sage and Jen/test_run_generic.sage. The
second file (http://sage.math.washington.edu/home/jen/OMS/Jen/test_run_generic.sage)
has some examples in the docstring.

Jen



---

archive/issue_comments_004902.json:
```json
{
    "body": "Changing assignee from @craigcitro to @mmasdeu.",
    "created_at": "2014-03-14T14:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4902",
    "user": "https://github.com/mmasdeu"
}
```

Changing assignee from @craigcitro to @mmasdeu.



---

archive/issue_comments_004903.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-03-14T14:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4903",
    "user": "https://github.com/mmasdeu"
}
```

New commits:



---

archive/issue_comments_004904.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T14:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4904",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_004905.json:
```json
{
    "body": "I think the code is usable enough that it should made into Sage. It includes the btquotients code, which is in a quite stable state as well. Several parts of the code are in need for more debugging, though. Especially the dist.pyx and distributions.py, which are not very robust.",
    "created_at": "2014-03-14T14:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4905",
    "user": "https://github.com/mmasdeu"
}
```

I think the code is usable enough that it should made into Sage. It includes the btquotients code, which is in a quite stable state as well. Several parts of the code are in need for more debugging, though. Especially the dist.pyx and distributions.py, which are not very robust.



---

archive/issue_comments_004906.json:
```json
{
    "body": "There are some failing doctests, see patchbot's report",
    "created_at": "2014-03-21T21:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4906",
    "user": "https://github.com/fchapoton"
}
```

There are some failing doctests, see patchbot's report



---

archive/issue_comments_004907.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-03-21T21:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4907",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004908.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-23T18:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4908",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004909.json:
```json
{
    "body": "OK, I just learned that:\n# long time optional - magma\ndoes not work. One has to do:\n# long time, optional - magma\n\nSo hopefully now it works!",
    "created_at": "2014-03-23T18:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4909",
    "user": "https://github.com/mmasdeu"
}
```

OK, I just learned that:
# long time optional - magma
does not work. One has to do:
# long time, optional - magma

So hopefully now it works!



---

archive/issue_comments_004910.json:
```json
{
    "body": "I just (very) quickly skimmed the patches -- this is some beautiful code!",
    "created_at": "2014-03-23T18:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4910",
    "user": "https://github.com/williamstein"
}
```

I just (very) quickly skimmed the patches -- this is some beautiful code!



---

archive/issue_comments_004911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-03-25T17:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4911",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004912.json:
```json
{
    "body": "Just some general \"top-level\" remarks, without really looking at the code yet:\n- In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.\n- It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.",
    "created_at": "2014-05-06T01:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4912",
    "user": "https://github.com/pjbruin"
}
```

Just some general "top-level" remarks, without really looking at the code yet:
- In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.
- It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.



---

archive/issue_comments_004913.json:
```json
{
    "body": "Hi Marc,\nJen and I worked on reviewing this last weekend, but I'm getting married on Saturday and haven't had time to upload our progress, etc.  I'll try to have some comments and changes next week.",
    "created_at": "2014-05-06T01:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4913",
    "user": "https://github.com/roed314"
}
```

Hi Marc,
Jen and I worked on reviewing this last weekend, but I'm getting married on Saturday and haven't had time to upload our progress, etc.  I'll try to have some comments and changes next week.



---

archive/issue_comments_004914.json:
```json
{
    "body": "patchbot:\n\n```\nsage -t --long src/sage/doctest/sources.py  # 1 doctest failed\nsage -t --long src/sage/modular/pollack_stevens/distributions.py  # 1 doctest failed\nsage -t --long src/sage/modular/btquotients/pautomorphicform.py  # 2 doctests failed\n```\n",
    "created_at": "2014-05-07T12:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4914",
    "user": "https://github.com/rwst"
}
```

patchbot:

```
sage -t --long src/sage/doctest/sources.py  # 1 doctest failed
sage -t --long src/sage/modular/pollack_stevens/distributions.py  # 1 doctest failed
sage -t --long src/sage/modular/btquotients/pautomorphicform.py  # 2 doctests failed
```




---

archive/issue_comments_004915.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-07T12:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4915",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004916.json:
```json
{
    "body": "I have made some large scale cleanup of the file btquotient (pyflakes and pep8 compliance). And also taken care of the \"doctest continuation\" plugin failure.\n----\nNew commits:",
    "created_at": "2014-05-09T19:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4916",
    "user": "https://github.com/fchapoton"
}
```

I have made some large scale cleanup of the file btquotient (pyflakes and pep8 compliance). And also taken care of the "doctest continuation" plugin failure.
----
New commits:



---

archive/issue_comments_004917.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T07:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4917",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004918.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T11:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4918",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004919.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T12:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4919",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004920.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T16:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4920",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004921.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T19:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4921",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004922.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T20:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4922",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004923.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-06-04T10:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4923",
    "user": "https://github.com/mmasdeu"
}
```

New commits:



---

archive/issue_comments_004924.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-04T10:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4924",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004925.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-08-23T06:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4925",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004926.json:
```json
{
    "body": "one doctest is failing, and needs more doc, see patchbot report",
    "created_at": "2014-08-23T06:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4926",
    "user": "https://github.com/fchapoton"
}
```

one doctest is failing, and needs more doc, see patchbot report



---

archive/issue_comments_004927.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-24T23:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4927",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004928.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-24T23:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4928",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004929.json:
```json
{
    "body": "is this needs review now ?",
    "created_at": "2016-01-25T20:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4929",
    "user": "https://github.com/fchapoton"
}
```

is this needs review now ?



---

archive/issue_comments_004930.json:
```json
{
    "body": "Thanks for asking.  It's not yet: there are still doctest failures.  I was setting up an SMC project with this code and updated it to 7.0, so I figured I would push the changes here.  But there's more work to be done before Needs Review, which I don't have time to do this week.",
    "created_at": "2016-01-25T21:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4930",
    "user": "https://github.com/roed314"
}
```

Thanks for asking.  It's not yet: there are still doctest failures.  I was setting up an SMC project with this code and updated it to 7.0, so I figured I would push the changes here.  But there's more work to be done before Needs Review, which I don't have time to do this week.



---

archive/issue_comments_004931.json:
```json
{
    "body": "It would be nice to get this in at long last. It's been an open Sage ticket since the dawn of time. Working on this at SD44 in Madison must have absorbed hundreds of person-hours and thousands of dollars of grant money, and we all flew home thinking the job was 95% done; that was three years ago. \n\nCan you say what would be the absolute minimum amount of work needed for this to get merged? Is it just a case of identifying the doctest failures and fixing them?",
    "created_at": "2016-01-26T09:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4931",
    "user": "https://github.com/loefflerd"
}
```

It would be nice to get this in at long last. It's been an open Sage ticket since the dawn of time. Working on this at SD44 in Madison must have absorbed hundreds of person-hours and thousands of dollars of grant money, and we all flew home thinking the job was 95% done; that was three years ago. 

Can you say what would be the absolute minimum amount of work needed for this to get merged? Is it just a case of identifying the doctest failures and fixing them?



---

archive/issue_comments_004932.json:
```json
{
    "body": "Agreed.  I think mostly it's a matter of fixing the doctest problems, and then splitting off further problems into followup tickets.  I will try to work on it soon....",
    "created_at": "2016-01-26T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4932",
    "user": "https://github.com/roed314"
}
```

Agreed.  I think mostly it's a matter of fixing the doctest problems, and then splitting off further problems into followup tickets.  I will try to work on it soon....



---

archive/issue_comments_004933.json:
```json
{
    "body": "I have added the authors (please check), so that patchbots can run on this ticket once it is put in needs_review.",
    "created_at": "2016-01-27T14:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4933",
    "user": "https://github.com/fchapoton"
}
```

I have added the authors (please check), so that patchbots can run on this ticket once it is put in needs_review.



---

archive/issue_comments_004934.json:
```json
{
    "body": "I put this into needs_review, so that the patchbots can work on it.",
    "created_at": "2016-03-06T17:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4934",
    "user": "https://github.com/fchapoton"
}
```

I put this into needs_review, so that the patchbots can work on it.



---

archive/issue_comments_004935.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-03-06T17:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4935",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004936.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-27T13:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4936",
    "user": "https://github.com/categorie"
}
```

New commits:



---

archive/issue_comments_004937.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2016-04-04T16:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4937",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:



---

archive/issue_comments_004938.json:
```json
{
    "body": "All doctests pass now, finally! I have also checked for whitespace. There are still things that one can work on, but my feeling is that they should be relegated to other tickets depending on this one. Here is a list of these:\n\n1. The distributions code is embarrassingly slow. It would be drastically improved by having an implementation that uses Sage's integers (no need to use longs here) instead of Qp and Zp.\n\n2. More functions/methods to interact with other implementations of modular symbols could be added. For example, it is straightforward to have a method to construct a Pollack-Stevens modular symbol from a one-dimensional modular symbols space. Such a method exists if one starts from an elliptic curve already.\n\n3. The p-adic L-function returned by this implementation is quite different to what is returned by the current (not overconvergent) implementation. Fixing this involves deciding where the overconvergent lift is done: one needs to know a target precision for this, whereas the non-overconvergent implementation only requires the precision parameter when evaluating a particular term of the series.\n\n4. The normalization of the p-adic L-series is different than the one used in the current implementation. This is noted in the examples, and it can be easy to fix (once this ticket is accepted).\n\nI am sure that there are many other improvements that other people will suggest, but let's first ensure that this ticket doesn't see its 10th birthday.",
    "created_at": "2016-04-04T17:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4938",
    "user": "https://github.com/mmasdeu"
}
```

All doctests pass now, finally! I have also checked for whitespace. There are still things that one can work on, but my feeling is that they should be relegated to other tickets depending on this one. Here is a list of these:

1. The distributions code is embarrassingly slow. It would be drastically improved by having an implementation that uses Sage's integers (no need to use longs here) instead of Qp and Zp.

2. More functions/methods to interact with other implementations of modular symbols could be added. For example, it is straightforward to have a method to construct a Pollack-Stevens modular symbol from a one-dimensional modular symbols space. Such a method exists if one starts from an elliptic curve already.

3. The p-adic L-function returned by this implementation is quite different to what is returned by the current (not overconvergent) implementation. Fixing this involves deciding where the overconvergent lift is done: one needs to know a target precision for this, whereas the non-overconvergent implementation only requires the precision parameter when evaluating a particular term of the series.

4. The normalization of the p-adic L-series is different than the one used in the current implementation. This is noted in the examples, and it can be easy to fix (once this ticket is accepted).

I am sure that there are many other improvements that other people will suggest, but let's first ensure that this ticket doesn't see its 10th birthday.



---

archive/issue_comments_004939.json:
```json
{
    "body": "See the latest patchbot report for several failing plugins, that needs to be corrected. And doc does not build.",
    "created_at": "2016-04-06T19:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4939",
    "user": "https://github.com/fchapoton"
}
```

See the latest patchbot report for several failing plugins, that needs to be corrected. And doc does not build.



---

archive/issue_comments_004940.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-07T11:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4940",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004941.json:
```json
{
    "body": "Thanks. But doc still does not build.\nThe problem is probably here:\n\n```\n+        -  ``sign`` - None (default), 0, +1 or -1. If None, choose the default\n+        according to the implementation, which currently is 0 for pollack-stevens,\n+        and 1 otherwise.\n```\n\nwhere the last two lines should be indented by 2.\n\nYou can check that the doc build using something like that\n\n```\nsage -docbuild reference/plane_curves html\n```\n\n\n\nYou also used a wrong newstyle doctest continuation, the correct one is `....:`\nPlease correct.",
    "created_at": "2016-04-07T12:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4941",
    "user": "https://github.com/fchapoton"
}
```

Thanks. But doc still does not build.
The problem is probably here:

```
+        -  ``sign`` - None (default), 0, +1 or -1. If None, choose the default
+        according to the implementation, which currently is 0 for pollack-stevens,
+        and 1 otherwise.
```

where the last two lines should be indented by 2.

You can check that the doc build using something like that

```
sage -docbuild reference/plane_curves html
```



You also used a wrong newstyle doctest continuation, the correct one is `....:`
Please correct.



---

archive/issue_comments_004942.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-07T15:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4942",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004943.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-07T16:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4943",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004944.json:
```json
{
    "body": "<rant>Am I the only one that thinks that this is becoming ridiculous?</rant>",
    "created_at": "2016-04-07T16:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4944",
    "user": "https://github.com/mmasdeu"
}
```

<rant>Am I the only one that thinks that this is becoming ridiculous?</rant>



---

archive/issue_comments_004945.json:
```json
{
    "body": "I'm looking at it now Marc.  It is really annoying how many little things come up.",
    "created_at": "2016-04-07T17:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4945",
    "user": "https://github.com/roed314"
}
```

I'm looking at it now Marc.  It is really annoying how many little things come up.



---

archive/issue_comments_004946.json:
```json
{
    "body": "I think the following points from comment:16 are still valid:\n> - In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.\n> - It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.",
    "created_at": "2016-04-12T19:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4946",
    "user": "https://github.com/pjbruin"
}
```

I think the following points from comment:16 are still valid:
> - In `sage/modular/all.py`, the `import *` commands may not be what you want; this will all end up in the global namespace.
> - It would be nice to add the new modules to the relevant `src/doc/en/reference/*/index.rst` files, probably with `*` = `modfrm`, `modmisc` and/or `modsym`.



---

archive/issue_comments_004947.json:
```json
{
    "body": "Peter,\n\n- The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.\n\n- I am working on the docs now.",
    "created_at": "2016-04-13T21:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4947",
    "user": "https://github.com/mmasdeu"
}
```

Peter,

- The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.

- I am working on the docs now.



---

archive/issue_comments_004948.json:
```json
{
    "body": "Hi Marc,\n> The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.\nIt is actually less bad than I thought, but if I understand the import statements correctly, all of the following will end up in the global namespace:\n- `BTQuotient`\n- `DoubleCosetReduction`\n- `HarmonicCocycleElement`\n- `HarmonicCocycles`\n- `pAutomorphicFormElement`\n- `pAutomorphicForms`\n- `PSModularSymbols`\n- `Distributions`\n- `Symk`\n- `ManinRelations`\n- `pAdicLseries`\nI think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...",
    "created_at": "2016-04-13T22:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4948",
    "user": "https://github.com/pjbruin"
}
```

Hi Marc,
> The import * commands are not added by this ticket, which only concerns .../pollack_stevens and .../btquotients. In sage/modular/all.py we do import everything in btquotients/all.py (and same for pollack_stevens) but this should be fine, since that file contains only the modules that need to be put in the global namespace.
It is actually less bad than I thought, but if I understand the import statements correctly, all of the following will end up in the global namespace:
- `BTQuotient`
- `DoubleCosetReduction`
- `HarmonicCocycleElement`
- `HarmonicCocycles`
- `pAutomorphicFormElement`
- `pAutomorphicForms`
- `PSModularSymbols`
- `Distributions`
- `Symk`
- `ManinRelations`
- `pAdicLseries`
I think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...



---

archive/issue_comments_004949.json:
```json
{
    "body": "Replying to [comment:51 pbruin]:\n> - `BTQuotient`\n> - `DoubleCosetReduction` - removed\n> - `HarmonicCocycleElement` - removed\n> - `HarmonicCocycles`\n> - `pAutomorphicFormElement` - removed\n> - `pAutomorphicForms`\n> - `PSModularSymbols`\n> - `Distributions`\n> - `Symk`\n> - `ManinRelations` - removed\n> - `pAdicLseries` - removed\n> I think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...\nSo the new proposed list would be:\n- `BTQuotient`\n- `HarmonicCocycles`\n- `pAutomorphicForms`\n- `PSModularSymbols\n- `Distributions`\n- `Symk`\nWould this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean. Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).",
    "created_at": "2016-04-13T22:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4949",
    "user": "https://github.com/mmasdeu"
}
```

Replying to [comment:51 pbruin]:
> - `BTQuotient`
> - `DoubleCosetReduction` - removed
> - `HarmonicCocycleElement` - removed
> - `HarmonicCocycles`
> - `pAutomorphicFormElement` - removed
> - `pAutomorphicForms`
> - `PSModularSymbols`
> - `Distributions`
> - `Symk`
> - `ManinRelations` - removed
> - `pAdicLseries` - removed
> I think most mathematicians who are not specialists in automorphic forms couldn't guess what any of these means, let alone the average Sage user...
So the new proposed list would be:
- `BTQuotient`
- `HarmonicCocycles`
- `pAutomorphicForms`
- `PSModularSymbols
- `Distributions`
- `Symk`
Would this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean. Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).



---

archive/issue_comments_004950.json:
```json
{
    "body": "Replying to [comment:52 mmasdeu]:\n> So the new proposed list would be:\n> - `BTQuotient`\n> - `HarmonicCocycles`\n> - `pAutomorphicForms`\n> - `PSModularSymbols\n> - `Distributions`\n> - `Symk`\n> Would this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean.\nThis does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are *p*-adic objects (all of them would make sense in the complex world or in even greater generality).\n\nBy the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...\n> Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).\nWell, many things are functions in Magma that are methods in Sage, so in principle the global namespace should be cleaner in Sage...\n\n**Edit:** And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.",
    "created_at": "2016-04-13T22:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4950",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:52 mmasdeu]:
> So the new proposed list would be:
> - `BTQuotient`
> - `HarmonicCocycles`
> - `pAutomorphicForms`
> - `PSModularSymbols
> - `Distributions`
> - `Symk`
> Would this be more reasonable? Considering that objects like `CrystalOfProjectedLevelZeroLSPaths` is also in the global namespace, I mean.
This does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are *p*-adic objects (all of them would make sense in the complex world or in even greater generality).

By the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...
> Also, have you seen Magma's global namespace? It doesn't prevent people from using it :-).
Well, many things are functions in Magma that are methods in Sage, so in principle the global namespace should be cleaner in Sage...

**Edit:** And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.



---

archive/issue_comments_004951.json:
```json
{
    "body": "> This does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are *p*-adic objects (all of them would make sense in the complex world or in even greater generality).\n\nI am renaming HarmonicCocycles to BTHarmonicCocycles, and Distributions to OverconvergentDistributions. The Symk does not need to be p-adic, it's pretty general.\n\n> By the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...\n\nI do agree, but it's quite low in my list of priorities. I'd rather have Sage create an Eichler order in a quaternion algebra...\n\n> **Edit:** And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.\n\nI agree, too.",
    "created_at": "2016-04-13T22:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4951",
    "user": "https://github.com/mmasdeu"
}
```

> This does sound more reasonable, although `Distributions`, `HarmonicCocycles` and `Symk` should definitely get a more descriptive name that makes it clear that they are *p*-adic objects (all of them would make sense in the complex world or in even greater generality).

I am renaming HarmonicCocycles to BTHarmonicCocycles, and Distributions to OverconvergentDistributions. The Symk does not need to be p-adic, it's pretty general.

> By the way, I do hope you agree that having something called `CrystalOfProjectedLevelZeroLSPaths` in the global namespace is pretty ridiculous and should be deprecated...

I do agree, but it's quite low in my list of priorities. I'd rather have Sage create an Eichler order in a quaternion algebra...

> **Edit:** And maybe `pAutomorphicForms` should be called `pAdicAutomorphicForms`?  Also, I guess it would be less cryptic to expand `BT` to `BruhatTits` and `PS` to `PollackStevens`.

I agree, too.



---

archive/issue_comments_004952.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-13T22:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4952",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004953.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-13T23:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4953",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004954.json:
```json
{
    "body": "I think it looks good now.",
    "created_at": "2016-04-13T23:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4954",
    "user": "https://github.com/mmasdeu"
}
```

I think it looks good now.



---

archive/issue_comments_004955.json:
```json
{
    "body": "OK, thanks!  I still haven't got the time for a real review, unfortunately...",
    "created_at": "2016-04-14T09:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4955",
    "user": "https://github.com/pjbruin"
}
```

OK, thanks!  I still haven't got the time for a real review, unfortunately...



---

archive/issue_comments_004956.json:
```json
{
    "body": "needs rebase on latest develop",
    "created_at": "2016-05-22T20:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4956",
    "user": "https://github.com/fchapoton"
}
```

needs rebase on latest develop



---

archive/issue_comments_004957.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-06-14T08:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4957",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004958.json:
```json
{
    "body": "I started to work on this a bit.\n\nI will try to merge it. But I also found a lot of things that I am not totally happy with, before that ticket goes in. See below. There is a real danger that this patch-bomb ticket never makes it into sage at this rate. I would be really sorry about this. Here are the possibilities:\n\n1. One option  would be to split it up: Put the basic code (i.e. the new files) in then in further tickets starts incorporating it into sage step by step.\n\n2. Another option is to accept it in an incomplete version as soon as it is rebased and doc-test are corrected and then open new tickets. But that means that certain functions will change and deprecation will be all over the place.\n\n3. We try to fix all issues here slowly and hope this converges in finite time.\n\nRight, option 1 would have been the correct decision at the start but I fear it is too late for this. Marc probably favours 2 and I would prefer 3, I must admit, although I am not sure I can put in the effort needed.",
    "created_at": "2016-06-14T12:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4958",
    "user": "https://github.com/categorie"
}
```

I started to work on this a bit.

I will try to merge it. But I also found a lot of things that I am not totally happy with, before that ticket goes in. See below. There is a real danger that this patch-bomb ticket never makes it into sage at this rate. I would be really sorry about this. Here are the possibilities:

1. One option  would be to split it up: Put the basic code (i.e. the new files) in then in further tickets starts incorporating it into sage step by step.

2. Another option is to accept it in an incomplete version as soon as it is rebased and doc-test are corrected and then open new tickets. But that means that certain functions will change and deprecation will be all over the place.

3. We try to fix all issues here slowly and hope this converges in finite time.

Right, option 1 would have been the correct decision at the start but I fear it is too late for this. Marc probably favours 2 and I would prefer 3, I must admit, although I am not sure I can put in the effort needed.



---

archive/issue_comments_004959.json:
```json
{
    "body": "(I am having issues posting. So I will do it in small portions, sorry)\n\nNow here to a list of issues that I spotted this morning.\n\n* I don't think it is a good idea that `m = E.modular_symbol(implementation=\"pollack-stevens\")` gives a completely different type of thing back. It is not even callable. Is it even desirable to have them in the same function. I would have left `modular_symbols` as before and added a `overconvergent_modular_symbols` as a separate method. (Personally, I would revert this function to before and think about it in a next ticket.)",
    "created_at": "2016-06-14T12:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4959",
    "user": "https://github.com/categorie"
}
```

(I am having issues posting. So I will do it in small portions, sorry)

Now here to a list of issues that I spotted this morning.

* I don't think it is a good idea that `m = E.modular_symbol(implementation="pollack-stevens")` gives a completely different type of thing back. It is not even callable. Is it even desirable to have them in the same function. I would have left `modular_symbols` as before and added a `overconvergent_modular_symbols` as a separate method. (Personally, I would revert this function to before and think about it in a next ticket.)



---

archive/issue_comments_004960.json:
```json
{
    "body": "* The normalisation of the p-adic L-function is wrong. One has to divide by the number of real connected components of the elliptic curve. This matters for p=2, otherwise it is a choice of normalisation. But it is better to be consistent with sage.\n\n* If we leave `E.modular_symbol()` as modified here, then it should take eclib as default (as stated in the new docstring). Without having resolved #10256, `ps_modsym_from_elliptic_curve` should take eclib for positive and sage for negative. Or is sage for both a better choice? Certainly much slower. (Again I opt, for keeping as before and use slow sage for overconvergent ms by now)",
    "created_at": "2016-06-14T12:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4960",
    "user": "https://github.com/categorie"
}
```

* The normalisation of the p-adic L-function is wrong. One has to divide by the number of real connected components of the elliptic curve. This matters for p=2, otherwise it is a choice of normalisation. But it is better to be consistent with sage.

* If we leave `E.modular_symbol()` as modified here, then it should take eclib as default (as stated in the new docstring). Without having resolved #10256, `ps_modsym_from_elliptic_curve` should take eclib for positive and sage for negative. Or is sage for both a better choice? Certainly much slower. (Again I opt, for keeping as before and use slow sage for overconvergent ms by now)



---

archive/issue_comments_004961.json:
```json
{
    "body": "* The arguments `n` and `prec` in series of the overconvergent p-adic L-functions are not clear to me. They are probably the wrong way around. The new precision should have a default value, also it should have another name, not to confuse it with the precision in T.\n\n* Many functions have incomplete documentations. E.g. no description of what the input arguments mean and what the output means.\n\nIf there is anyone else working on this, please let me know. I might not update my changes too often, but I will try to work on these issues over the next two weeks.",
    "created_at": "2016-06-14T12:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4961",
    "user": "https://github.com/categorie"
}
```

* The arguments `n` and `prec` in series of the overconvergent p-adic L-functions are not clear to me. They are probably the wrong way around. The new precision should have a default value, also it should have another name, not to confuse it with the precision in T.

* Many functions have incomplete documentations. E.g. no description of what the input arguments mean and what the output means.

If there is anyone else working on this, please let me know. I might not update my changes too often, but I will try to work on these issues over the next two weeks.



---

archive/issue_comments_004962.json:
```json
{
    "body": "Last 10 new commits:",
    "created_at": "2016-06-22T19:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4962",
    "user": "https://github.com/categorie"
}
```

Last 10 new commits:



---

archive/issue_comments_004963.json:
```json
{
    "body": "Last 10 new commits:",
    "created_at": "2016-06-22T21:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4963",
    "user": "https://github.com/categorie"
}
```

Last 10 new commits:



---

archive/issue_comments_004964.json:
```json
{
    "body": "Thanks Marc, for fixing the last problems and improving the docstrings. A spotted a few last things. Now there is one very last thing that should be changed before this goes in: Please change the title line of pollack_stevens/modsym.py.\nI will be running the tests.\n\nI opend a few follow up tickets:\n\n* #20863 : Improve documentation. There are some # mm TODO left. \n* #20864 : The caching of modular_symbols should be modernised and the keyword use_eclib should be dropped\n* #20865 : General ticket to ask for improving the code so that the p-adic L-functions are as fast as we could hope for.",
    "created_at": "2016-06-22T21:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4964",
    "user": "https://github.com/categorie"
}
```

Thanks Marc, for fixing the last problems and improving the docstrings. A spotted a few last things. Now there is one very last thing that should be changed before this goes in: Please change the title line of pollack_stevens/modsym.py.
I will be running the tests.

I opend a few follow up tickets:

* #20863 : Improve documentation. There are some # mm TODO left. 
* #20864 : The caching of modular_symbols should be modernised and the keyword use_eclib should be dropped
* #20865 : General ticket to ask for improving the code so that the p-adic L-functions are as fast as we could hope for.



---

archive/issue_comments_004965.json:
```json
{
    "body": "please take care of using python2/3 compatible print. See patchbot report\n(plugin oldstyle_print)\n\nand\n\nhttps://wiki.sagemath.org/PrintFunction",
    "created_at": "2016-06-23T11:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4965",
    "user": "https://github.com/fchapoton"
}
```

please take care of using python2/3 compatible print. See patchbot report
(plugin oldstyle_print)

and

https://wiki.sagemath.org/PrintFunction



---

archive/issue_comments_004966.json:
```json
{
    "body": "It only screamed about commented lines. I changed them too.\n\n(I am not sure the bot should tell us it failed when print is wrongly used on comment lines and I am very certain it should say nothing about the \"print\" apprearing in the middle of a docstring as in \"Return the print representation\" in `_repr_` )\n----\nNew commits:",
    "created_at": "2016-06-23T12:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4966",
    "user": "https://github.com/categorie"
}
```

It only screamed about commented lines. I changed them too.

(I am not sure the bot should tell us it failed when print is wrongly used on comment lines and I am very certain it should say nothing about the "print" apprearing in the middle of a docstring as in "Return the print representation" in `_repr_` )
----
New commits:



---

archive/issue_comments_004967.json:
```json
{
    "body": "Indeed, the plugin is not very smart, and should not care about commented lines. Sorry for the noise.",
    "created_at": "2016-06-23T12:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4967",
    "user": "https://github.com/fchapoton"
}
```

Indeed, the plugin is not very smart, and should not care about commented lines. Sorry for the noise.



---

archive/issue_comments_004968.json:
```json
{
    "body": "It all compiles fine now and tests all pass. So if that one title line is changed this can be set to positive review.",
    "created_at": "2016-06-23T14:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4968",
    "user": "https://github.com/categorie"
}
```

It all compiles fine now and tests all pass. So if that one title line is changed this can be set to positive review.



---

archive/issue_comments_004969.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-06-23T15:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4969",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004970.json:
```json
{
    "body": "Done. I have also changed the title in space.py, since the modular symbols in it are not necessarily overconvergent.\n----\nNew commits:",
    "created_at": "2016-06-23T15:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4970",
    "user": "https://github.com/mmasdeu"
}
```

Done. I have also changed the title in space.py, since the modular symbols in it are not necessarily overconvergent.
----
New commits:



---

archive/issue_comments_004971.json:
```json
{
    "body": "Thanks Marc.\n\nThis 9 year old ticket is now done ! Yeah.",
    "created_at": "2016-06-23T15:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4971",
    "user": "https://github.com/categorie"
}
```

Thanks Marc.

This 9 year old ticket is now done ! Yeah.



---

archive/issue_comments_004972.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-06-23T15:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4972",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004973.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-06-23T17:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4973",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_004974.json:
```json
{
    "body": "\n```\n[sagelib-7.3.beta4] [2/7] Cythonizing sage/modular/pollack_stevens/dist.pyx\n[sagelib-7.3.beta4] [3/7] Cythonizing sage/numerical/backends/cplex_backend.pyx\n[sagelib-7.3.beta4] \n[sagelib-7.3.beta4] Error compiling Cython file:\n[sagelib-7.3.beta4] ------------------------------------------------------------\n[sagelib-7.3.beta4] ...\n[sagelib-7.3.beta4]         if negate:\n[sagelib-7.3.beta4]             rmoments = -rmoments\n[sagelib-7.3.beta4]         ans._moments = smoments + rmoments\n[sagelib-7.3.beta4]         return ans\n[sagelib-7.3.beta4] \n[sagelib-7.3.beta4]     cpdef ModuleElement _add_(self, ModuleElement _right):\n[sagelib-7.3.beta4]          ^\n[sagelib-7.3.beta4] ------------------------------------------------------------\n[sagelib-7.3.beta4] \n[sagelib-7.3.beta4] sage/modular/pollack_stevens/dist.pyx:957:10: Signature not compatible with previous declaration\n```\n",
    "created_at": "2016-06-23T17:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4974",
    "user": "https://github.com/vbraun"
}
```


```
[sagelib-7.3.beta4] [2/7] Cythonizing sage/modular/pollack_stevens/dist.pyx
[sagelib-7.3.beta4] [3/7] Cythonizing sage/numerical/backends/cplex_backend.pyx
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4] Error compiling Cython file:
[sagelib-7.3.beta4] ------------------------------------------------------------
[sagelib-7.3.beta4] ...
[sagelib-7.3.beta4]         if negate:
[sagelib-7.3.beta4]             rmoments = -rmoments
[sagelib-7.3.beta4]         ans._moments = smoments + rmoments
[sagelib-7.3.beta4]         return ans
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4]     cpdef ModuleElement _add_(self, ModuleElement _right):
[sagelib-7.3.beta4]          ^
[sagelib-7.3.beta4] ------------------------------------------------------------
[sagelib-7.3.beta4] 
[sagelib-7.3.beta4] sage/modular/pollack_stevens/dist.pyx:957:10: Signature not compatible with previous declaration
```




---

archive/issue_comments_004975.json:
```json
{
    "body": "I don't know how to reproduce the above error in my machine. I removed a superfluous import (in dist.pyx and dist.pxd), which I think is unrelated but was giving out warnings while cythonizing. Also, to make the patchbot happy I changed \"print\" into \"string\" in some of the docstrings.\n----\nNew commits:",
    "created_at": "2016-06-24T08:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4975",
    "user": "https://github.com/mmasdeu"
}
```

I don't know how to reproduce the above error in my machine. I removed a superfluous import (in dist.pyx and dist.pxd), which I think is unrelated but was giving out warnings while cythonizing. Also, to make the patchbot happy I changed "print" into "string" in some of the docstrings.
----
New commits:



---

archive/issue_comments_004976.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-06-24T08:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4976",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004977.json:
```json
{
    "body": "Hello. You should not care about stupid patchbot remarks. Having the patchbot complete\napproval is not a requirement, as long as **you** understand why.",
    "created_at": "2016-06-24T08:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4977",
    "user": "https://github.com/fchapoton"
}
```

Hello. You should not care about stupid patchbot remarks. Having the patchbot complete
approval is not a requirement, as long as **you** understand why.



---

archive/issue_comments_004978.json:
```json
{
    "body": "I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...",
    "created_at": "2016-06-24T14:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4978",
    "user": "https://github.com/mmasdeu"
}
```

I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...



---

archive/issue_comments_004979.json:
```json
{
    "body": "Replying to [comment:78 mmasdeu]:\n> I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...\nIt must be because of #20740, which is apparently merged in Volker's branch, but is not in the latest beta.",
    "created_at": "2016-06-24T16:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4979",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:78 mmasdeu]:
> I'm just worried about Volker's remarks, not the patchbot's. Can someone see how to fix the issue (or at least how to reproduce it?). I have looked at the signature in sage/structure/element.pxd and it looks the same as the one used in dist.pyx...
It must be because of #20740, which is apparently merged in Volker's branch, but is not in the latest beta.



---

archive/issue_comments_004980.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-06-26T21:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4980",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004981.json:
```json
{
    "body": "I think that is right. Even with the updated branch here, when merged into the current develop, there are Error compiling Cython file: dist.pyx.",
    "created_at": "2016-06-26T21:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4981",
    "user": "https://github.com/categorie"
}
```

I think that is right. Even with the updated branch here, when merged into the current develop, there are Error compiling Cython file: dist.pyx.



---

archive/issue_comments_004982.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-27T14:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4982",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004983.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-06-27T14:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4983",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004984.json:
```json
{
    "body": "I believe that it works now.",
    "created_at": "2016-06-27T14:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4984",
    "user": "https://github.com/mmasdeu"
}
```

I believe that it works now.



---

archive/issue_comments_004985.json:
```json
{
    "body": "It compiles fine for me. Running the tests now.",
    "created_at": "2016-06-27T14:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4985",
    "user": "https://github.com/categorie"
}
```

It compiles fine for me. Running the tests now.



---

archive/issue_comments_004986.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-06-27T15:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4986",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004987.json:
```json
{
    "body": "they passed",
    "created_at": "2016-06-27T15:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4987",
    "user": "https://github.com/categorie"
}
```

they passed



---

archive/issue_comments_004988.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-06-27T22:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4988",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_004989.json:
```json
{
    "body": "Failures on 32-bit:\n\n```\nsage -t --long src/sage/modular/btquotients/btquotient.py\n**********************************************************************\nFile \"src/sage/modular/btquotients/btquotient.py\", line 1502, in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key\nFailed example:\n    X._cache_key()\nExpected:\n    1375458358400022881\nGot:\n    -406423199\n**********************************************************************\nFile \"src/sage/modular/btquotients/btquotient.py\", line 2478, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion\nFailed example:\n    l[3]\nExpected:\n    [-1]\n    [ 0]\n    [ 1]\n    [ 1]\nGot:\n    [-1]\n    [ 1]\n    [ 0]\n    [ 1]\n**********************************************************************\nFile \"src/sage/modular/btquotients/btquotient.py\", line 2483, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion\nFailed example:\n    X.embed_quaternion(l[3])\nExpected:\n    [    O(7) 3 + O(7)]\n    [2 + O(7) 6 + O(7)]\nGot:\n    [4 + O(7)     O(7)]\n    [1 + O(7) 2 + O(7)]\n**********************************************************************\nFile \"src/sage/modular/btquotients/btquotient.py\", line 2487, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion\nFailed example:\n    X.embed_quaternion(l[3])\nExpected:\n    [                7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             3 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]\n    [            2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6) 6 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)]\nGot:\n    [4 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)                 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]\n    [            1 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]\n**********************************************************************\n2 items had failures:\n   1 of   3 in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key\n   3 of   8 in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion\n    [375 tests, 4 failures, 8.18 s]\n```\n",
    "created_at": "2016-06-27T22:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4989",
    "user": "https://github.com/vbraun"
}
```

Failures on 32-bit:

```
sage -t --long src/sage/modular/btquotients/btquotient.py
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 1502, in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key
Failed example:
    X._cache_key()
Expected:
    1375458358400022881
Got:
    -406423199
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2478, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    l[3]
Expected:
    [-1]
    [ 0]
    [ 1]
    [ 1]
Got:
    [-1]
    [ 1]
    [ 0]
    [ 1]
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2483, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    X.embed_quaternion(l[3])
Expected:
    [    O(7) 3 + O(7)]
    [2 + O(7) 6 + O(7)]
Got:
    [4 + O(7)     O(7)]
    [1 + O(7) 2 + O(7)]
**********************************************************************
File "src/sage/modular/btquotients/btquotient.py", line 2487, in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
Failed example:
    X.embed_quaternion(l[3])
Expected:
    [                7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             3 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
    [            2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6) 6 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)]
Got:
    [4 + 5*7 + 3*7^2 + 5*7^3 + 2*7^4 + 6*7^5 + O(7^6)                 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
    [            1 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)             2 + 7 + 3*7^2 + 7^3 + 4*7^4 + O(7^6)]
**********************************************************************
2 items had failures:
   1 of   3 in sage.modular.btquotients.btquotient.BruhatTitsQuotient._cache_key
   3 of   8 in sage.modular.btquotients.btquotient.BruhatTitsQuotient.embed_quaternion
    [375 tests, 4 failures, 8.18 s]
```




---

archive/issue_comments_004990.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-28T12:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4990",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004991.json:
```json
{
    "body": "That is fine by me. Is the first output really random ? Otherwise you can use `# 32-bit` and `# 64-bit` in the doctest.\n\nIn any case, I have no means of checking as I don't have access to magma or 32-bit. If someone listening has, they should run the test for us, otherwise we have to bother the release manager again with a \"positive review\"....",
    "created_at": "2016-06-28T12:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4991",
    "user": "https://github.com/categorie"
}
```

That is fine by me. Is the first output really random ? Otherwise you can use `# 32-bit` and `# 64-bit` in the doctest.

In any case, I have no means of checking as I don't have access to magma or 32-bit. If someone listening has, they should run the test for us, otherwise we have to bother the release manager again with a "positive review"....



---

archive/issue_comments_004992.json:
```json
{
    "body": "I fixed the problem with the doctests, plus another bug that arised when using Magma. Tests in btquotients and in pollackstevens pass in my machine.",
    "created_at": "2016-06-28T12:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4992",
    "user": "https://github.com/mmasdeu"
}
```

I fixed the problem with the doctests, plus another bug that arised when using Magma. Tests in btquotients and in pollackstevens pass in my machine.



---

archive/issue_comments_004993.json:
```json
{
    "body": "The `__cache_key` is not random, but I have put it as it were since it is not of much use. The test done after is more relevant. The embedding functions depend on a call to `pMatrixRing` in Magma, so it would be random, or at least fairly unpredictable.",
    "created_at": "2016-06-28T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4993",
    "user": "https://github.com/mmasdeu"
}
```

The `__cache_key` is not random, but I have put it as it were since it is not of much use. The test done after is more relevant. The embedding functions depend on a call to `pMatrixRing` in Magma, so it would be random, or at least fairly unpredictable.



---

archive/issue_comments_004994.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-06-28T12:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4994",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004995.json:
```json
{
    "body": "You can use this:\n\n```\n            sage: hash(SR(19.23))\n            -1458111714  # 32-bit\n            2836855582   # 64-bit\n```\n",
    "created_at": "2016-06-28T13:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4995",
    "user": "https://github.com/vbraun"
}
```

You can use this:

```
            sage: hash(SR(19.23))
            -1458111714  # 32-bit
            2836855582   # 64-bit
```




---

archive/issue_comments_004996.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-28T13:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4996",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004997.json:
```json
{
    "body": "I have followed Volker's suggestion. I leave it as needs_review...",
    "created_at": "2016-06-28T13:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4997",
    "user": "https://github.com/mmasdeu"
}
```

I have followed Volker's suggestion. I leave it as needs_review...



---

archive/issue_comments_004998.json:
```json
{
    "body": "To me all tests still pass and I can't check 32-bit or optional magma. So I set this to positive review, fearing of course that a bot or vbraun will find yet another issue.\n\nThe patchbot complains about something, but I don't understand it.",
    "created_at": "2016-06-28T17:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4998",
    "user": "https://github.com/categorie"
}
```

To me all tests still pass and I can't check 32-bit or optional magma. So I set this to positive review, fearing of course that a bot or vbraun will find yet another issue.

The patchbot complains about something, but I don't understand it.



---

archive/issue_comments_004999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-06-28T17:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-4999",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005000.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2016-06-29T11:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5000",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_005001.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2016-06-29T11:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5001",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_005002.json:
```json
{
    "body": "I realized that there was one doctest missing in `btquotient.py`. This is fixed now. I'm keeping it as \"needs review\" and hope that the patchbot is happier now.",
    "created_at": "2016-06-29T11:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5002",
    "user": "https://github.com/mmasdeu"
}
```

I realized that there was one doctest missing in `btquotient.py`. This is fixed now. I'm keeping it as "needs review" and hope that the patchbot is happier now.



---

archive/issue_comments_005003.json:
```json
{
    "body": "Well, you deleted lots of commented code and moved an undocumented function to a place where coverage won't complain about it. I guess this is not the optimal solutions, but one can deal with this in #20863.\n\nCoverage also complains about another missing docstring:\n\n\n```\nSCORE src/sage/schemes/elliptic_curves/padics.py: 92.3% (12 of 13)\n\nMissing doctests:\n     * line 72: def _normalize_padic_lseries(self, p, normalize, use_eclib, implementation, precision)\n```\n",
    "created_at": "2016-06-29T11:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5003",
    "user": "https://github.com/categorie"
}
```

Well, you deleted lots of commented code and moved an undocumented function to a place where coverage won't complain about it. I guess this is not the optimal solutions, but one can deal with this in #20863.

Coverage also complains about another missing docstring:


```
SCORE src/sage/schemes/elliptic_curves/padics.py: 92.3% (12 of 13)

Missing doctests:
     * line 72: def _normalize_padic_lseries(self, p, normalize, use_eclib, implementation, precision)
```




---

archive/issue_comments_005004.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-29T13:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5004",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_005005.json:
```json
{
    "body": "I fixed the missing doctest in `padics.py` as well.\n----\nNew commits:",
    "created_at": "2016-06-29T13:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5005",
    "user": "https://github.com/mmasdeu"
}
```

I fixed the missing doctest in `padics.py` as well.
----
New commits:



---

archive/issue_comments_005006.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-06-29T14:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5006",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005007.json:
```json
{
    "body": "tests pass.",
    "created_at": "2016-06-29T14:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5007",
    "user": "https://github.com/categorie"
}
```

tests pass.



---

archive/issue_comments_005008.json:
```json
{
    "body": "Building the pdf docs fails\n\n```\n[docpdf] LaTeX Warning: Hyper reference `sage/modular/pollack_stevens/modsym:sage.modula\n[docpdf] r.pollack_stevens.modsym.PSModularSymbolElement' on page 162 undefined on input\n[docpdf]  line 13297.\n[docpdf] \n[docpdf] [162] [163] [164] [165] [166]\n[docpdf] Underfull \\hbox (badness 10000) in paragraph at lines 13628--13628\n[docpdf] \\T1/ptm/m/it/10 char-ac-ter=None\\T1/ptm/m/n/10 ,\n[docpdf] \n[docpdf] Underfull \\hbox (badness 10000) in paragraph at lines 13628--13628\n[docpdf] \\T1/ptm/m/it/10 use_magma=False\\T1/ptm/m/n/10 ,\n[docpdf] \n[docpdf] Overfull \\hbox (152.67451pt too wide) in paragraph at lines 13629--13630\n[docpdf] \\T1/ptm/m/n/10 Bases: \\T1/pcr/m/n/10 sage.structure.sage_object.SageObject\\T1/p\n[docpdf] tm/m/n/10 , \\T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent\n[docpdf] ation \n[docpdf] [167] [168] [169] [170] [171] [172] [173] [174] [175] [176] [177] [178]\n[docpdf] Overfull \\hbox (152.67451pt too wide) in paragraph at lines 14890--14891\n[docpdf] \\T1/ptm/m/n/10 Bases: \\T1/pcr/m/n/10 sage.structure.sage_object.SageObject\\T1/p\n[docpdf] tm/m/n/10 , \\T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent\n[docpdf] ation \n[docpdf] [179] [180] [181]\n[docpdf] ! Undefined control sequence.\n[docpdf] l.15130 modulo \\(p\\) is not in \\(\\FF\n[docpdf]                                     _p\\):\n[docpdf] ? \n[docpdf] ! Emergency stop.\n[docpdf] l.15130 modulo \\(p\\) is not in \\(\\FF\n[docpdf]                                     _p\\):\n[docpdf] !  ==> Fatal error occurred, no output PDF file produced!\n[docpdf] Transcript written on modsym.log.\n[docpdf] Makefile:68: recipe for target 'modsym.pdf' failed\n```\n",
    "created_at": "2016-06-29T23:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5008",
    "user": "https://github.com/vbraun"
}
```

Building the pdf docs fails

```
[docpdf] LaTeX Warning: Hyper reference `sage/modular/pollack_stevens/modsym:sage.modula
[docpdf] r.pollack_stevens.modsym.PSModularSymbolElement' on page 162 undefined on input
[docpdf]  line 13297.
[docpdf] 
[docpdf] [162] [163] [164] [165] [166]
[docpdf] Underfull \hbox (badness 10000) in paragraph at lines 13628--13628
[docpdf] \T1/ptm/m/it/10 char-ac-ter=None\T1/ptm/m/n/10 ,
[docpdf] 
[docpdf] Underfull \hbox (badness 10000) in paragraph at lines 13628--13628
[docpdf] \T1/ptm/m/it/10 use_magma=False\T1/ptm/m/n/10 ,
[docpdf] 
[docpdf] Overfull \hbox (152.67451pt too wide) in paragraph at lines 13629--13630
[docpdf] \T1/ptm/m/n/10 Bases: \T1/pcr/m/n/10 sage.structure.sage_object.SageObject\T1/p
[docpdf] tm/m/n/10 , \T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent
[docpdf] ation 
[docpdf] [167] [168] [169] [170] [171] [172] [173] [174] [175] [176] [177] [178]
[docpdf] Overfull \hbox (152.67451pt too wide) in paragraph at lines 14890--14891
[docpdf] \T1/ptm/m/n/10 Bases: \T1/pcr/m/n/10 sage.structure.sage_object.SageObject\T1/p
[docpdf] tm/m/n/10 , \T1/pcr/m/n/10 sage.structure.unique_representation.UniqueRepresent
[docpdf] ation 
[docpdf] [179] [180] [181]
[docpdf] ! Undefined control sequence.
[docpdf] l.15130 modulo \(p\) is not in \(\FF
[docpdf]                                     _p\):
[docpdf] ? 
[docpdf] ! Emergency stop.
[docpdf] l.15130 modulo \(p\) is not in \(\FF
[docpdf]                                     _p\):
[docpdf] !  ==> Fatal error occurred, no output PDF file produced!
[docpdf] Transcript written on modsym.log.
[docpdf] Makefile:68: recipe for target 'modsym.pdf' failed
```




---

archive/issue_comments_005009.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-06-29T23:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5009",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_005010.json:
```json
{
    "body": "pdf documentation now build for me.\n----\nLast 10 new commits:",
    "created_at": "2016-06-30T12:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5010",
    "user": "https://github.com/categorie"
}
```

pdf documentation now build for me.
----
Last 10 new commits:



---

archive/issue_comments_005011.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2016-06-30T16:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5011",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_005012.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-07-01T16:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/812#issuecomment-5012",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
