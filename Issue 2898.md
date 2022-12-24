# Issue 2898: Coerce float and RDF to Integers

archive/issues_002898.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n>  That said, William, is there a reason why this doesn't work?  This is\n> >  what is necessitating the two type conversions above.\n> >\n> >  sage: Integer(float(2))\n> >\n> > ---------------------------------------------------------------------------\n> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)\n> >\n> >  /home/grout/<ipython console> in <module>()\n> >\n> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()\n> >\n> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer\n> >\n> >\n> >  sage: Integer(RDF(2))\n> >\n> > ---------------------------------------------------------------------------\n> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)\n> >\n> >  /home/grout/<ipython console> in <module>()\n> >\n> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()\n> >\n> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer\n> >\n> >\n> >  I guess I would think it was a design decision to not convert floating\n> >  points to ints automatically.  However, the following does work:\n> >\n> >  sage: Integer(RR(2))\n> >  2\n> >\n> >\n> >  This seems inconsistent.\n\nYep.  I think it's just a NotImplementedError.  Please implement it\nand post a patch.  Make sure that it only succeeds if\n\n   Integer(k(a)) == a\n\nand otherwise fails.  I.e., Integer(k(a)) should *not* truncate k(a).\n\nWilliam\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2898\n\n",
    "created_at": "2008-04-12T16:08:08Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Coerce float and RDF to Integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2898",
    "user": "jason"
}
```
Assignee: somebody


```
>  That said, William, is there a reason why this doesn't work?  This is
> >  what is necessitating the two type conversions above.
> >
> >  sage: Integer(float(2))
> >
> > ---------------------------------------------------------------------------
> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)
> >
> >  /home/grout/<ipython console> in <module>()
> >
> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()
> >
> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer
> >
> >
> >  sage: Integer(RDF(2))
> >
> > ---------------------------------------------------------------------------
> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)
> >
> >  /home/grout/<ipython console> in <module>()
> >
> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()
> >
> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer
> >
> >
> >  I guess I would think it was a design decision to not convert floating
> >  points to ints automatically.  However, the following does work:
> >
> >  sage: Integer(RR(2))
> >  2
> >
> >
> >  This seems inconsistent.

Yep.  I think it's just a NotImplementedError.  Please implement it
and post a patch.  Make sure that it only succeeds if

   Integer(k(a)) == a

and otherwise fails.  I.e., Integer(k(a)) should *not* truncate k(a).

William
```



Issue created by migration from https://trac.sagemath.org/ticket/2898





---

archive/issue_comments_019942.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2008-04-12T16:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19942",
    "user": "jason"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_019943.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2008-04-12T16:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19943",
    "user": "jason"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_019944.json:
```json
{
    "body": "I've put up a preliminary patch at:\n\nhttp://sage.math.washington.edu/home/jason/trac-2898-coerce-to-Int.patch\n\nThis is undergoing doctesting in alpha3 right now.",
    "created_at": "2008-04-13T04:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19944",
    "user": "jason"
}
```

I've put up a preliminary patch at:

http://sage.math.washington.edu/home/jason/trac-2898-coerce-to-Int.patch

This is undergoing doctesting in alpha3 right now.



---

archive/issue_comments_019945.json:
```json
{
    "body": "Jason, \n\nany update on this patch? I corrected the subject to be a little clearer.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T07:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19945",
    "user": "mabshoff"
}
```

Jason, 

any update on this patch? I corrected the subject to be a little clearer.

Cheers,

Michael



---

archive/issue_comments_019946.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-20T04:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19946",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_019947.json:
```json
{
    "body": "I believe the patch is ready to be doctested (which is where my time gave out before).",
    "created_at": "2008-06-24T00:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19947",
    "user": "jason"
}
```

I believe the patch is ready to be doctested (which is where my time gave out before).



---

archive/issue_comments_019948.json:
```json
{
    "body": "This is supposed to fix #2899, so it would be good to check if the other issue is resolved as well.",
    "created_at": "2008-06-24T00:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19948",
    "user": "jason"
}
```

This is supposed to fix #2899, so it would be good to check if the other issue is resolved as well.



---

archive/issue_comments_019949.json:
```json
{
    "body": "Attachment [2898-jgrout-coerce-to-integer-1.patch](tarball://root/attachments/some-uuid/ticket2898/2898-jgrout-coerce-to-integer-1.patch) by ncalexan created at 2008-08-14 00:33:50",
    "created_at": "2008-08-14T00:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19949",
    "user": "ncalexan"
}
```

Attachment [2898-jgrout-coerce-to-integer-1.patch](tarball://root/attachments/some-uuid/ticket2898/2898-jgrout-coerce-to-integer-1.patch) by ncalexan created at 2008-08-14 00:33:50



---

archive/issue_comments_019950.json:
```json
{
    "body": "The patch I posted is basically the same as jgrout's; it sat in my tree for a long time without any problems.\n\nIt looks good to me, but let's get a second opinion.",
    "created_at": "2008-08-14T00:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19950",
    "user": "ncalexan"
}
```

The patch I posted is basically the same as jgrout's; it sat in my tree for a long time without any problems.

It looks good to me, but let's get a second opinion.



---

archive/issue_comments_019951.json:
```json
{
    "body": "Unfortunately, this patch gives:\n\n```\nsage: 1.0r/8\n1/8\n```\n\nwhich is IMHO unacceptable.\n\nI think that the bug is actually in the coercion framework, rather than in this patch; so I've opened a new issue for that bug at #3938.  Once it is fixed, then we can revisit this patch.",
    "created_at": "2008-08-23T21:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19951",
    "user": "cwitty"
}
```

Unfortunately, this patch gives:

```
sage: 1.0r/8
1/8
```

which is IMHO unacceptable.

I think that the bug is actually in the coercion framework, rather than in this patch; so I've opened a new issue for that bug at #3938.  Once it is fixed, then we can revisit this patch.



---

archive/issue_comments_019952.json:
```json
{
    "body": "I agree with cwitty, I'll be taking a look at #3938.",
    "created_at": "2008-08-23T22:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19952",
    "user": "robertwb"
}
```

I agree with cwitty, I'll be taking a look at #3938.



---

archive/issue_comments_019953.json:
```json
{
    "body": "#3938 has been resolved.",
    "created_at": "2008-08-30T19:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19953",
    "user": "robertwb"
}
```

#3938 has been resolved.



---

archive/issue_comments_019954.json:
```json
{
    "body": "Replying to [comment:11 robertwb]:\n> #3938 has been resolved. \n\nHi Robert,\n\nso if I understand you correctly this patch here should not be merged since it fixes a symptom and not the root cause.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T23:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19954",
    "user": "mabshoff"
}
```

Replying to [comment:11 robertwb]:
> #3938 has been resolved. 

Hi Robert,

so if I understand you correctly this patch here should not be merged since it fixes a symptom and not the root cause.

Cheers,

Michael



---

archive/issue_comments_019955.json:
```json
{
    "body": "This patch should be applied. The problem is that it exposed a bug that was worse than what it fixed. Now the bug has been resolved, they both should be applied.",
    "created_at": "2008-08-31T03:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19955",
    "user": "robertwb"
}
```

This patch should be applied. The problem is that it exposed a bug that was worse than what it fixed. Now the bug has been resolved, they both should be applied.



---

archive/issue_comments_019956.json:
```json
{
    "body": "Looks good to me.  This depends on #3938.",
    "created_at": "2008-09-19T00:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19956",
    "user": "mhansen"
}
```

Looks good to me.  This depends on #3938.



---

archive/issue_comments_019957.json:
```json
{
    "body": "The patch no longer applies cleanly and also causes a doctest failure (sorry, forgot the details and no longer have the logs ;)). The rebase should be easy since hunk 2 of integer.pyx is affected and it is only a doctest issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T02:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19957",
    "user": "mabshoff"
}
```

The patch no longer applies cleanly and also causes a doctest failure (sorry, forgot the details and no longer have the logs ;)). The rebase should be easy since hunk 2 of integer.pyx is affected and it is only a doctest issue.

Cheers,

Michael



---

archive/issue_comments_019958.json:
```json
{
    "body": "Attachment [2898-jgrout-coerce-to-integer-3.3.alpha2.patch](tarball://root/attachments/some-uuid/ticket2898/2898-jgrout-coerce-to-integer-3.3.alpha2.patch) by cwitty created at 2009-01-25 20:16:57",
    "created_at": "2009-01-25T20:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19958",
    "user": "cwitty"
}
```

Attachment [2898-jgrout-coerce-to-integer-3.3.alpha2.patch](tarball://root/attachments/some-uuid/ticket2898/2898-jgrout-coerce-to-integer-3.3.alpha2.patch) by cwitty created at 2009-01-25 20:16:57



---

archive/issue_comments_019959.json:
```json
{
    "body": "I've attached two patches, 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch.  With #3938 plus these two patches over 3.3.alpha2, all doctests pass (except those that were broken in base 3.3.alpha2).\n\nI'm giving a positive review for 2898-jgrout-coerce-to-integer-3.3.alpha2.patch; somebody else should review trac2898-fixups.patch.",
    "created_at": "2009-01-25T20:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19959",
    "user": "cwitty"
}
```

I've attached two patches, 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch.  With #3938 plus these two patches over 3.3.alpha2, all doctests pass (except those that were broken in base 3.3.alpha2).

I'm giving a positive review for 2898-jgrout-coerce-to-integer-3.3.alpha2.patch; somebody else should review trac2898-fixups.patch.



---

archive/issue_comments_019960.json:
```json
{
    "body": "I get an error applying the fixups patch:\n\n\n```\napplying trac2898-fixups.patch?format=raw\npatching file sage/rings/real_mpfr.pyx\nHunk #1 FAILED at 396\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/real_mpfr.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac2898-fixups.patch?format=raw\n```\n",
    "created_at": "2009-01-28T18:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19960",
    "user": "jason"
}
```

I get an error applying the fixups patch:


```
applying trac2898-fixups.patch?format=raw
patching file sage/rings/real_mpfr.pyx
Hunk #1 FAILED at 396
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/real_mpfr.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac2898-fixups.patch?format=raw
```




---

archive/issue_comments_019961.json:
```json
{
    "body": "I'm confused by the real_mpfr.pyx part of the fixups patch.  I can't find the misspelling \"cannonical\" anywhere in that directory in sage-3.3alpha2.",
    "created_at": "2009-01-28T18:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19961",
    "user": "jason"
}
```

I'm confused by the real_mpfr.pyx part of the fixups patch.  I can't find the misspelling "cannonical" anywhere in that directory in sage-3.3alpha2.



---

archive/issue_comments_019962.json:
```json
{
    "body": "The real_mpfr.pyx part of the fixups patch should be deleted-mabshoff corrected the typo when merging #3938.\n\nDoctests pass in all files touched by the fixups patch.  I'd like someone else to look at the code it touches in free_modules.pyx and verify the changes there.  Other than that, this looks good to me.",
    "created_at": "2009-01-28T19:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19962",
    "user": "jason"
}
```

The real_mpfr.pyx part of the fixups patch should be deleted-mabshoff corrected the typo when merging #3938.

Doctests pass in all files touched by the fixups patch.  I'd like someone else to look at the code it touches in free_modules.pyx and verify the changes there.  Other than that, this looks good to me.



---

archive/issue_comments_019963.json:
```json
{
    "body": "Attachment [trac2898-fixups.patch](tarball://root/attachments/some-uuid/ticket2898/trac2898-fixups.patch) by cwitty created at 2009-02-06 07:42:31\n\nWe didn't get this in quite soon enough; in alpha5, this gives failing doctests in symbolic/expression.pyx.  (The following is hand-edited to remove boring bits of the backtraces.)\n\n```\nsage -t  \"devel/sage-mqtmp/sage/symbolic/expression.pyx\"    \n**********************************************************************\nFile \"/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx\", line 2169:\n    sage: S(10.0r).gamma()\nExpected:\n    362880.000000000\nGot:\n    362880\n**********************************************************************\nFile \"/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx\", line 2180:\n    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)\nException raised:\n    Traceback (most recent call last):\n...\n      File \"<doctest __main__.example_73[9]>\", line 1, in <module>\n        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:\n    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)\n      File \"/home/cwitty/sage-3.3.alpha5/local/lib/python2.5/site-packages/sage/plot/misc.py\", line 428, in wrapper\n        return func(*args, **kwds)\n...\n      File \"<doctest __main__.example_73[9]>\", line 1, in <lambda>\n        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:\n    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)\n      File \"expression.pyx\", line 2183, in sage.symbolic.expression.Expression.gamma (sage/symbolic/expression.cpp:8410)\n    RuntimeError: tgamma_eval(): simple pole\n**********************************************************************\nFile \"/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx\", line 2204:\n    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()\nException raised:\n    Traceback (most recent call last):\n...\n      File \"<doctest __main__.example_74[7]>\", line 1, in <module>\n        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:\n    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()\n...\n      File \"<doctest __main__.example_74[7]>\", line 1, in <lambda>\n        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:\n    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()\n      File \"expression.pyx\", line 2210, in sage.symbolic.expression.Expression.lgamma (sage/symbolic/expression.cpp:8476)\n    RuntimeError: lgamma_eval(): logarithmic pole\n**********************************************************************\n2 items had failures:\n   2 of  10 in __main__.example_73\n   1 of  10 in __main__.example_74\n***Test Failed*** 3 failures.\n```\n",
    "created_at": "2009-02-06T07:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19963",
    "user": "cwitty"
}
```

Attachment [trac2898-fixups.patch](tarball://root/attachments/some-uuid/ticket2898/trac2898-fixups.patch) by cwitty created at 2009-02-06 07:42:31

We didn't get this in quite soon enough; in alpha5, this gives failing doctests in symbolic/expression.pyx.  (The following is hand-edited to remove boring bits of the backtraces.)

```
sage -t  "devel/sage-mqtmp/sage/symbolic/expression.pyx"    
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2169:
    sage: S(10.0r).gamma()
Expected:
    362880.000000000
Got:
    362880
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
Exception raised:
    Traceback (most recent call last):
...
      File "<doctest __main__.example_73[9]>", line 1, in <module>
        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
      File "/home/cwitty/sage-3.3.alpha5/local/lib/python2.5/site-packages/sage/plot/misc.py", line 428, in wrapper
        return func(*args, **kwds)
...
      File "<doctest __main__.example_73[9]>", line 1, in <lambda>
        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
      File "expression.pyx", line 2183, in sage.symbolic.expression.Expression.gamma (sage/symbolic/expression.cpp:8410)
    RuntimeError: tgamma_eval(): simple pole
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
Exception raised:
    Traceback (most recent call last):
...
      File "<doctest __main__.example_74[7]>", line 1, in <module>
        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
...
      File "<doctest __main__.example_74[7]>", line 1, in <lambda>
        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
      File "expression.pyx", line 2210, in sage.symbolic.expression.Expression.lgamma (sage/symbolic/expression.cpp:8476)
    RuntimeError: lgamma_eval(): logarithmic pole
**********************************************************************
2 items had failures:
   2 of  10 in __main__.example_73
   1 of  10 in __main__.example_74
***Test Failed*** 3 failures.
```




---

archive/issue_comments_019964.json:
```json
{
    "body": "I've placed a proposed patch for the above doctest failure at #5199.  So I'm now saying that this is \"ready for review\" again; but the patch now depends on #5199 (and #3938, if the reviewer is using a version of Sage older than 3.3.alpha3).",
    "created_at": "2009-02-07T05:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19964",
    "user": "cwitty"
}
```

I've placed a proposed patch for the above doctest failure at #5199.  So I'm now saying that this is "ready for review" again; but the patch now depends on #5199 (and #3938, if the reviewer is using a version of Sage older than 3.3.alpha3).



---

archive/issue_comments_019965.json:
```json
{
    "body": "The fixups patch looks good to me except for the following two failures:\n\n\n```\n**********************************************************************\nFile \"/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx\", line 74:\n    sage: hermite_constant(1) # trivial one-dimensional lattice\nExpected:\n    1.0\nGot:\n    1\n**********************************************************************\nFile \"/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx\", line 80:\n    sage: hermite_constant(8) # E_8\nExpected:\n    2.0\nGot:\n    2\n**********************************************************************\n```\n",
    "created_at": "2009-02-09T08:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19965",
    "user": "mhansen"
}
```

The fixups patch looks good to me except for the following two failures:


```
**********************************************************************
File "/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx", line 74:
    sage: hermite_constant(1) # trivial one-dimensional lattice
Expected:
    1.0
Got:
    1
**********************************************************************
File "/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx", line 80:
    sage: hermite_constant(8) # E_8
Expected:
    2.0
Got:
    2
**********************************************************************
```




---

archive/issue_comments_019966.json:
```json
{
    "body": "I cannot reproduce the failures Mike saw and I assume #5199 fixed that.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19966",
    "user": "mabshoff"
}
```

I cannot reproduce the failures Mike saw and I assume #5199 fixed that.

Cheers,

Michael



---

archive/issue_comments_019967.json:
```json
{
    "body": "Merged 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19967",
    "user": "mabshoff"
}
```

Merged 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_019968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T08:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2898#issuecomment-19968",
    "user": "mabshoff"
}
```

Resolution: fixed
