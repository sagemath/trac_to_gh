# Issue 6034: [with spkg, needs review] update Singular to newest upstream release

archive/issues_006034.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @craigcitro\n\nKeywords: singular\n\nSingular 3.1 has many new features which are pretty exciting for Sage (computation over base *rings*, yay!). So we should upgrade.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6034\n\n",
    "created_at": "2009-05-13T03:00:37Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with spkg, needs review] update Singular to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6034",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @craigcitro

Keywords: singular

Singular 3.1 has many new features which are pretty exciting for Sage (computation over base *rings*, yay!). So we should upgrade.

Issue created by migration from https://trac.sagemath.org/ticket/6034





---

archive/issue_comments_047953.json:
```json
{
    "body": "fixes doctest fallout",
    "created_at": "2009-05-13T03:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47953",
    "user": "https://github.com/malb"
}
```

fixes doctest fallout



---

archive/issue_comments_047954.json:
```json
{
    "body": "Attachment [singular_3_1_0.patch](tarball://root/attachments/some-uuid/ticket6034/singular_3_1_0.patch) by @malb created at 2009-05-13 03:02:20\n\nThe SPKG can be found here:\n\n   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg\n\nIt does not contain the changed LIB location. It basically is a drop-in replacement for the current Singular spkg.",
    "created_at": "2009-05-13T03:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47954",
    "user": "https://github.com/malb"
}
```

Attachment [singular_3_1_0.patch](tarball://root/attachments/some-uuid/ticket6034/singular_3_1_0.patch) by @malb created at 2009-05-13 03:02:20

The SPKG can be found here:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg

It does not contain the changed LIB location. It basically is a drop-in replacement for the current Singular spkg.



---

archive/issue_comments_047955.json:
```json
{
    "body": "Attachment [singular_env.patch](tarball://root/attachments/some-uuid/ticket6034/singular_env.patch) by @malb created at 2009-05-13 03:42:36\n\nI've updated sage-env and the spkg to move the `*.lib` files out of the way to `$SAGE_LOCAL/share/singular`.",
    "created_at": "2009-05-13T03:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47955",
    "user": "https://github.com/malb"
}
```

Attachment [singular_env.patch](tarball://root/attachments/some-uuid/ticket6034/singular_env.patch) by @malb created at 2009-05-13 03:42:36

I've updated sage-env and the spkg to move the `*.lib` files out of the way to `$SAGE_LOCAL/share/singular`.



---

archive/issue_comments_047956.json:
```json
{
    "body": "Note that I updated the SPKG at \n\n    http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg\n\nto include the fixes for enabling the coefficient rings which are not fields.",
    "created_at": "2009-05-17T01:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47956",
    "user": "https://github.com/malb"
}
```

Note that I updated the SPKG at 

    http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg

to include the fixes for enabling the coefficient rings which are not fields.



---

archive/issue_comments_047957.json:
```json
{
    "body": "The attached patch enables the Singular coefficient rings natively. It passes doctests except:\n\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1049.8 seconds\n```\n\n\nwhich I reported upstream at \n\n  http://www.singular.uni-kl.de:8002/trac/ticket/137",
    "created_at": "2009-05-17T01:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47957",
    "user": "https://github.com/malb"
}
```

The attached patch enables the Singular coefficient rings natively. It passes doctests except:


```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1049.8 seconds
```


which I reported upstream at 

  http://www.singular.uni-kl.de:8002/trac/ticket/137



---

archive/issue_comments_047958.json:
```json
{
    "body": "Ignore that comment, wrong ticket.",
    "created_at": "2009-05-17T01:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47958",
    "user": "https://github.com/malb"
}
```

Ignore that comment, wrong ticket.



---

archive/issue_comments_047959.json:
```json
{
    "body": "This will be a perfect addition for sage-4.0.1.",
    "created_at": "2009-05-28T07:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47959",
    "user": "https://github.com/williamstein"
}
```

This will be a perfect addition for sage-4.0.1.



---

archive/issue_events_014172.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-05-28T07:11:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6034#event-14172"
}
```



---

archive/issue_comments_047960.json:
```json
{
    "body": "Could you change singular_env.patch so that it knows where to find sage-env (i.e., in (sage directory)/local/bin)?\n\nThanks,\nKiran",
    "created_at": "2009-05-30T22:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47960",
    "user": "https://github.com/kedlaya"
}
```

Could you change singular_env.patch so that it knows where to find sage-env (i.e., in (sage directory)/local/bin)?

Thanks,
Kiran



---

archive/issue_comments_047961.json:
```json
{
    "body": "I am not quite sure what you're asking since singular_env.patch is a HG patch which should be applied via \n\n\n```\ncd $SAGE_LOCAL/bin\nhg import ~/singular_env.patch \n```\n",
    "created_at": "2009-05-31T13:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47961",
    "user": "https://github.com/malb"
}
```

I am not quite sure what you're asking since singular_env.patch is a HG patch which should be applied via 


```
cd $SAGE_LOCAL/bin
hg import ~/singular_env.patch 
```




---

archive/issue_comments_047962.json:
```json
{
    "body": "That works, yes. I had been trying to run hg from within sage.\n\nWith that, the patches apply against 4.0, the spkg builds, and the patch on #6051 applies and does what is expected (with the one known doctest failure caused by upstream). I didn't find any collateral doctest failures either. Positive review; however, in order to get #6051 to pass doctests, we'll need a new version from upstream and hence a new spkg.",
    "created_at": "2009-06-02T16:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47962",
    "user": "https://github.com/kedlaya"
}
```

That works, yes. I had been trying to run hg from within sage.

With that, the patches apply against 4.0, the spkg builds, and the patch on #6051 applies and does what is expected (with the one known doctest failure caused by upstream). I didn't find any collateral doctest failures either. Positive review; however, in order to get #6051 to pass doctests, we'll need a new version from upstream and hence a new spkg.



---

archive/issue_comments_047963.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-07T12:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47963",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_047964.json:
```json
{
    "body": "Sorry, but something is wrong.\n\nI get\n\n```\nsage: import os\nsage: os.environ['SINGULARPATH']\n'/home/king/SAGE/devel/sage-4.0/local/share/singular'\nsage: singular.eval('system(\"SingularLib\")')\n'/home/king/SAGE/devel/sage-4.0/local/share/singular:/home/king/SAGE/devel/sage-4.0/local/LIB'\n```\n\n\nBut the last line is Singular's way of telling where the libs are.",
    "created_at": "2009-06-08T14:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47964",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry, but something is wrong.

I get

```
sage: import os
sage: os.environ['SINGULARPATH']
'/home/king/SAGE/devel/sage-4.0/local/share/singular'
sage: singular.eval('system("SingularLib")')
'/home/king/SAGE/devel/sage-4.0/local/share/singular:/home/king/SAGE/devel/sage-4.0/local/LIB'
```


But the last line is Singular's way of telling where the libs are.



---

archive/issue_comments_047965.json:
```json
{
    "body": "Hi Simon,\n\nwhy is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?",
    "created_at": "2009-06-08T14:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47965",
    "user": "https://github.com/malb"
}
```

Hi Simon,

why is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?



---

archive/issue_comments_047966.json:
```json
{
    "body": "Replying to [comment:13 malb]:\n> Hi Simon,\n> \n> why is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?\n\nDouble sorry. I was missing something. Ithought that ``system(\"SingularLib\")`` gives precisely one location in which Singular is looking for libraries. But, as you point out, it may provide multiple search paths.\n\nOK, then back to Kiran's positive review.",
    "created_at": "2009-06-08T14:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47966",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:13 malb]:
> Hi Simon,
> 
> why is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?

Double sorry. I was missing something. Ithought that ``system("SingularLib")`` gives precisely one location in which Singular is looking for libraries. But, as you point out, it may provide multiple search paths.

OK, then back to Kiran's positive review.



---

archive/issue_comments_047967.json:
```json
{
    "body": "This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.",
    "created_at": "2009-06-10T05:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47967",
    "user": "https://github.com/ncalexan"
}
```

This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.



---

archive/issue_comments_047968.json:
```json
{
    "body": "Replying to [comment:15 ncalexan]:\n> This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.\n\nWhat did you do in order to install the spkg?\n\nYou should do:\n1. Either replace the singular-3-0-4 spkg by the new spkg and re-build Sage *from scratch*\n2. Or do the following:\n     i. ``sage -i singular-3-1-0...`` (so, install it into an existing sage)\n     iii. ``sage -f ntl...`` (so, force a re-installation of the ntl-spkg)\n     iiiii. \n       * Do ``sage -ba``, or \n       * touch all Cython extensions depending on Singular (these are sage.libs.singular.singular, sage.matrix.matrix_mpolynomial_dense, sage.rings.polynomial.multi_polynomial_ideal_libsingular and sage.rings.polynomial.multi_polynomial_libsingular) and do ``sage -b``\n\nThis is how I installed the new spkg.\n\nCheers,\n    Simon",
    "created_at": "2009-06-10T06:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47968",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:15 ncalexan]:
> This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.

What did you do in order to install the spkg?

You should do:
1. Either replace the singular-3-0-4 spkg by the new spkg and re-build Sage *from scratch*
2. Or do the following:
     i. ``sage -i singular-3-1-0...`` (so, install it into an existing sage)
     iii. ``sage -f ntl...`` (so, force a re-installation of the ntl-spkg)
     iiiii. 
       * Do ``sage -ba``, or 
       * touch all Cython extensions depending on Singular (these are sage.libs.singular.singular, sage.matrix.matrix_mpolynomial_dense, sage.rings.polynomial.multi_polynomial_ideal_libsingular and sage.rings.polynomial.multi_polynomial_libsingular) and do ``sage -b``

This is how I installed the new spkg.

Cheers,
    Simon



---

archive/issue_comments_047969.json:
```json
{
    "body": "> This is how I installed the new spkg.\n\nThanks Simon, it now builds and runs and I'll get to testing it tomorrow.",
    "created_at": "2009-06-10T07:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47969",
    "user": "https://github.com/ncalexan"
}
```

> This is how I installed the new spkg.

Thanks Simon, it now builds and runs and I'll get to testing it tomorrow.



---

archive/issue_comments_047970.json:
```json
{
    "body": "Replying to [comment:17 ncalexan]:\n> > This is how I installed the new spkg.\n> \n> Thanks Simon, it now builds and runs and I'll get to testing it tomorrow.\n\nJust for my own reference:\n\n\n```\ntouch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*\n```\n",
    "created_at": "2009-06-10T17:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47970",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:17 ncalexan]:
> > This is how I installed the new spkg.
> 
> Thanks Simon, it now builds and runs and I'll get to testing it tomorrow.

Just for my own reference:


```
touch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*
```




---

archive/issue_comments_047971.json:
```json
{
    "body": "Replying to [comment:18 ncalexan]:\n> Just for my own reference:\n> \n> {{{\n> touch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*\n> }}}\n\nShould we add something involving these dependencies to `module_list.py`?",
    "created_at": "2009-06-10T17:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47971",
    "user": "https://github.com/craigcitro"
}
```

Replying to [comment:18 ncalexan]:
> Just for my own reference:
> 
> {{{
> touch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*
> }}}

Should we add something involving these dependencies to `module_list.py`?



---

archive/issue_comments_047972.json:
```json
{
    "body": "Replying to [comment:19 craigcitro]:\n> Should we add something involving these dependencies to `module_list.py`?\n\nYes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.",
    "created_at": "2009-06-10T17:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47972",
    "user": "https://github.com/malb"
}
```

Replying to [comment:19 craigcitro]:
> Should we add something involving these dependencies to `module_list.py`?

Yes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.



---

archive/issue_comments_047973.json:
```json
{
    "body": "Replying to [comment:20 malb]:\n> Replying to [comment:19 craigcitro]:\n> > Should we add something involving these dependencies to `module_list.py`?\n> \n> Yes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.\n\nAren't these dependencies already in `module_list.py`? Actually this is where I was looking what I had to touch. Or perhaps touching `libsingular.h` would have been enough, who knows...",
    "created_at": "2009-06-11T06:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47973",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:20 malb]:
> Replying to [comment:19 craigcitro]:
> > Should we add something involving these dependencies to `module_list.py`?
> 
> Yes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.

Aren't these dependencies already in `module_list.py`? Actually this is where I was looking what I had to touch. Or perhaps touching `libsingular.h` would have been enough, who knows...



---

archive/issue_comments_047974.json:
```json
{
    "body": "Indeed the dependencies are already in, Nick must have forgotten to `sage -b` ?",
    "created_at": "2009-06-11T11:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47974",
    "user": "https://github.com/malb"
}
```

Indeed the dependencies are already in, Nick must have forgotten to `sage -b` ?



---

archive/issue_events_014173.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-12T07:43:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6034#event-14173"
}
```



---

archive/issue_comments_047975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T07:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6034#issuecomment-47975",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
