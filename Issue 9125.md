# Issue 9125: more examples of simplicial complexes: RP^n, CP^2, etc.

archive/issues_009125.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThis patch adds more examples of simplicial complexes: real projective spaces (that is, RP<sup>d</sup> for any positive d), CP<sup>2</sup>, and the Poincare homology sphere.  Some of these are the minimal triangulations, some are not; see the documentation.\n\nThese are important test cases for homology and other computations which I hope will be implemented soon -- see tickets #6102 and #6103, for instance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9125\n\n",
    "created_at": "2010-06-03T04:13:48Z",
    "labels": [
        "algebraic topology",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "more examples of simplicial complexes: RP^n, CP^2, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9125",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

This patch adds more examples of simplicial complexes: real projective spaces (that is, RP<sup>d</sup> for any positive d), CP<sup>2</sup>, and the Poincare homology sphere.  Some of these are the minimal triangulations, some are not; see the documentation.

These are important test cases for homology and other computations which I hope will be implemented soon -- see tickets #6102 and #6103, for instance.

Issue created by migration from https://trac.sagemath.org/ticket/9125





---

archive/issue_comments_084878.json:
```json
{
    "body": "Attachment [trac_9125-projective-space.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-projective-space.patch) by jhpalmieri created at 2010-06-03 04:14:15",
    "created_at": "2010-06-03T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84878",
    "user": "jhpalmieri"
}
```

Attachment [trac_9125-projective-space.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-projective-space.patch) by jhpalmieri created at 2010-06-03 04:14:15



---

archive/issue_comments_084879.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T04:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84879",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-10T22:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84880",
    "user": "robert_goss"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084881.json:
```json
{
    "body": "A very useful patch the documentation is very good.\n\nThe doc tests all run and the functionality seems correct.\n\n\nI have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?\n\nRobert",
    "created_at": "2010-11-10T22:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84881",
    "user": "robert_goss"
}
```

A very useful patch the documentation is very good.

The doc tests all run and the functionality seems correct.


I have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?

Robert



---

archive/issue_comments_084882.json:
```json
{
    "body": "Replying to [comment:2 robert_goss]:\n> I have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?\n\nI think having lens spaces would be very nice, although maybe it could go on another ticket so that the current patch can get merged.  If you post something, I'll almost certainly review it.   A naive approach would be fine, but you might also look at some of the papers referenced in the current patch.  In particular, \n\n- Basudeb Datta, \"Minimal triangulations of manifolds\", J. Indian Inst. Sci. 87 (2007), no. 4, 429-449. \n\n- Frank H. Lutz, \"Triangulated Manifolds with Few Vertices: Combinatorial Manifolds\", preprint (2005), 484\tarXiv:math/0506372. \n\nare both expository papers which might include some discussion of lens spaces, or might give references.  (I think I've seen discussions of triangulations of lens spaces somewhere, but I don't remember where.  You might also try searching the web.)",
    "created_at": "2010-11-10T23:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84882",
    "user": "jhpalmieri"
}
```

Replying to [comment:2 robert_goss]:
> I have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?

I think having lens spaces would be very nice, although maybe it could go on another ticket so that the current patch can get merged.  If you post something, I'll almost certainly review it.   A naive approach would be fine, but you might also look at some of the papers referenced in the current patch.  In particular, 

- Basudeb Datta, "Minimal triangulations of manifolds", J. Indian Inst. Sci. 87 (2007), no. 4, 429-449. 

- Frank H. Lutz, "Triangulated Manifolds with Few Vertices: Combinatorial Manifolds", preprint (2005), 484	arXiv:math/0506372. 

are both expository papers which might include some discussion of lens spaces, or might give references.  (I think I've seen discussions of triangulations of lens spaces somewhere, but I don't remember where.  You might also try searching the web.)



---

archive/issue_comments_084883.json:
```json
{
    "body": "robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.",
    "created_at": "2010-11-14T10:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84883",
    "user": "jdemeyer"
}
```

robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.



---

archive/issue_comments_084884.json:
```json
{
    "body": "Replying to [comment:4 jdemeyer]:\n> robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.\n\n\nHi thank you jdemeyer this is my first time contributing directly to sage and I am not sure of all the procedures.\n\nIs there anything else I should do?",
    "created_at": "2010-11-14T17:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84884",
    "user": "robert_goss"
}
```

Replying to [comment:4 jdemeyer]:
> robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.


Hi thank you jdemeyer this is my first time contributing directly to sage and I am not sure of all the procedures.

Is there anything else I should do?



---

archive/issue_comments_084885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84885",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_084886.json:
```json
{
    "body": "See the notes from  Fran\u00e7ois Bissey\n\nhttps://groups.google.com/group/sage-devel/browse_thread/thread/9e4cef8c8558150?hl=en\n\nthat this may be the cause of some timeouts seen on sage-gentoo. \n\nDave",
    "created_at": "2010-11-18T01:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84886",
    "user": "drkirkby"
}
```

See the notes from  François Bissey

https://groups.google.com/group/sage-devel/browse_thread/thread/9e4cef8c8558150?hl=en

that this may be the cause of some timeouts seen on sage-gentoo. 

Dave



---

archive/issue_comments_084887.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-18T08:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84887",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_084888.json:
```json
{
    "body": "The tests take way too long time.  This is on a 32-bit Linux Pentium 4 system:\n\n```\nsage: P5 = simplicial_complexes.RealProjectiveSpace(Integer(5))\nsage: time P5.homology()\nCPU times: user 4083.68 s, sys: 0.63 s, total: 4084.31 s\nWall time: 4084.50 s\n{0: 0, 1: C2, 2: 0, 3: C2, 4: 0, 5: Z}\n```\n",
    "created_at": "2010-11-18T08:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84888",
    "user": "jdemeyer"
}
```

The tests take way too long time.  This is on a 32-bit Linux Pentium 4 system:

```
sage: P5 = simplicial_complexes.RealProjectiveSpace(Integer(5))
sage: time P5.homology()
CPU times: user 4083.68 s, sys: 0.63 s, total: 4084.31 s
Wall time: 4084.50 s
{0: 0, 1: C2, 2: 0, 3: C2, 4: 0, 5: Z}
```




---

archive/issue_comments_084889.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-18T08:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84889",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_084890.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-18T08:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84890",
    "user": "jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084891.json:
```json
{
    "body": "Apply this patch on top of the other one.  This way the doctest will only run if you give it a command like `sage -t -long -only-optional=chomp`.  Since the test finishes in about a second when using CHomP, as opposed to around half an hour (sometimes causing timeouts, since 1800 seconds is the cutoff for long doctests) without CHomP, this seems like the right solution.",
    "created_at": "2010-11-18T15:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84891",
    "user": "jhpalmieri"
}
```

Apply this patch on top of the other one.  This way the doctest will only run if you give it a command like `sage -t -long -only-optional=chomp`.  Since the test finishes in about a second when using CHomP, as opposed to around half an hour (sometimes causing timeouts, since 1800 seconds is the cutoff for long doctests) without CHomP, this seems like the right solution.



---

archive/issue_comments_084892.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-18T15:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84892",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084893.json:
```json
{
    "body": "On the same Pentium 4 system, the following test\n\n```\nsage:P4 = simplicial_complexes.RealProjectiveSpace(4)\n```\n\ntakes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).",
    "created_at": "2010-11-18T19:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84893",
    "user": "jdemeyer"
}
```

On the same Pentium 4 system, the following test

```
sage:P4 = simplicial_complexes.RealProjectiveSpace(4)
```

takes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).



---

archive/issue_comments_084894.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> On the same Pentium 4 system, the following test takes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).\n\nI'll do that, but are you using specific guidelines about what constitutes \"long\"?  On a 2-year-old iMac, it takes about 10 seconds to doctest the whole file (\"sage -t examples.py\", not \"sage -t -long\").  That doesn't seem excessively long to me, especially since the machine isn't new, and it wasn't a top-of-the line machine even when it was new.",
    "created_at": "2010-11-18T22:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84894",
    "user": "jhpalmieri"
}
```

Replying to [comment:11 jdemeyer]:
> On the same Pentium 4 system, the following test takes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).

I'll do that, but are you using specific guidelines about what constitutes "long"?  On a 2-year-old iMac, it takes about 10 seconds to doctest the whole file ("sage -t examples.py", not "sage -t -long").  That doesn't seem excessively long to me, especially since the machine isn't new, and it wasn't a top-of-the line machine even when it was new.



---

archive/issue_comments_084895.json:
```json
{
    "body": "The guideline is that 1 second is the bound for # long time.  In the Sage developer manual, there is the following example:\n\n```\nsage: E = EllipticCurve([0, 0, 1, -1, 0])\nsage: E.regulator()              # long time (1 second)\n0.0511114082399688\n```\n",
    "created_at": "2010-11-19T07:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84895",
    "user": "jdemeyer"
}
```

The guideline is that 1 second is the bound for # long time.  In the Sage developer manual, there is the following example:

```
sage: E = EllipticCurve([0, 0, 1, -1, 0])
sage: E.regulator()              # long time (1 second)
0.0511114082399688
```




---

archive/issue_comments_084896.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2010-12-15T19:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84896",
    "user": "jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_084897.json:
```json
{
    "body": "Attachment [trac_9125-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-doctest-fix.patch) by jhpalmieri created at 2010-12-15 19:04:53\n\nCan this get reviewed soon?  The original patch was reviewed positively already, so I think only \"trac_9125-doctest-fix.patch\" needs to be reviewed.  That one just marks some doctests as being \"long time\" or \"optional - CHomP\", so I think it should be easy to review.",
    "created_at": "2010-12-15T19:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84897",
    "user": "jhpalmieri"
}
```

Attachment [trac_9125-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-doctest-fix.patch) by jhpalmieri created at 2010-12-15 19:04:53

Can this get reviewed soon?  The original patch was reviewed positively already, so I think only "trac_9125-doctest-fix.patch" needs to be reviewed.  That one just marks some doctests as being "long time" or "optional - CHomP", so I think it should be easy to review.



---

archive/issue_comments_084898.json:
```json
{
    "body": "Looks like you missed one \"long time\" addition, so there is a doctest failure.  \n\n\n\n```\n**********************************************************************\nFile \"/Users/mh/sagestuff/sage-4.7.alpha2/devel/sage-t1/sage/homology/examples.py\", line 518:\n    sage: P4.dimension()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[7]>\", line 1, in <module>\n        P4.dimension()###line 518:\n    sage: P4.dimension()\n    NameError: name 'P4' is not defined\n**********************************************************************\n\n```\n\n\nI am attaching a cumulative patch that fixes that.",
    "created_at": "2011-03-28T11:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84898",
    "user": "mhampton"
}
```

Looks like you missed one "long time" addition, so there is a doctest failure.  



```
**********************************************************************
File "/Users/mh/sagestuff/sage-4.7.alpha2/devel/sage-t1/sage/homology/examples.py", line 518:
    sage: P4.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[7]>", line 1, in <module>
        P4.dimension()###line 518:
    sage: P4.dimension()
    NameError: name 'P4' is not defined
**********************************************************************

```


I am attaching a cumulative patch that fixes that.



---

archive/issue_comments_084899.json:
```json
{
    "body": "Use instead of previous doctest patch",
    "created_at": "2011-03-28T11:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84899",
    "user": "mhampton"
}
```

Use instead of previous doctest patch



---

archive/issue_comments_084900.json:
```json
{
    "body": "Attachment [trac_9125-cumulative-doctest.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-cumulative-doctest.patch) by mhampton created at 2011-03-28 11:50:21\n\nOops, I forgot to fold so my patch is only cumulative with respect to trac_9125-doctest-fix.patch.",
    "created_at": "2011-03-28T11:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84900",
    "user": "mhampton"
}
```

Attachment [trac_9125-cumulative-doctest.patch](tarball://root/attachments/some-uuid/ticket9125/trac_9125-cumulative-doctest.patch) by mhampton created at 2011-03-28 11:50:21

Oops, I forgot to fold so my patch is only cumulative with respect to trac_9125-doctest-fix.patch.



---

archive/issue_comments_084901.json:
```json
{
    "body": "Looks good, passes all tests in sage/homology without chomp and everything passes -long -optional with chomp installed.\n\nJohn, I think this can have a positive review but you should just double-check my patch.  (Its a tiny change.)  If its OK then you can change to positive review.",
    "created_at": "2011-03-28T11:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84901",
    "user": "mhampton"
}
```

Looks good, passes all tests in sage/homology without chomp and everything passes -long -optional with chomp installed.

John, I think this can have a positive review but you should just double-check my patch.  (Its a tiny change.)  If its OK then you can change to positive review.



---

archive/issue_comments_084902.json:
```json
{
    "body": "Thanks, Marshall, looks good.  Tests failed with just my two patches, but they pass with yours.",
    "created_at": "2011-03-28T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84902",
    "user": "jhpalmieri"
}
```

Thanks, Marshall, looks good.  Tests failed with just my two patches, but they pass with yours.



---

archive/issue_comments_084903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-28T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84903",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T19:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9125#issuecomment-84904",
    "user": "jdemeyer"
}
```

Resolution: fixed
