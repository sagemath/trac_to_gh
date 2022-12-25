# Issue 8549: Add a cycle enumerator for Permutation Group

archive/issues_008549.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat\n\nKeywords: permutation, cycle, enumeration\n\nLet G a permutation group. Each permutation of G has a cycle type. The goal of this ticket is to add a method for permutation group which return a dictionary associating for each cycle pattern, the number of permutation in G having this pattern.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8549\n\n",
    "created_at": "2010-03-16T20:07:53Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Add a cycle enumerator for Permutation Group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8549",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: nborie

CC:  sage-combinat

Keywords: permutation, cycle, enumeration

Let G a permutation group. Each permutation of G has a cycle type. The goal of this ticket is to add a method for permutation group which return a dictionary associating for each cycle pattern, the number of permutation in G having this pattern.

Issue created by migration from https://trac.sagemath.org/ticket/8549





---

archive/issue_comments_077175.json:
```json
{
    "body": "This should allow to do some plethysm very easily.\n\nSuggestion welcome to improve the latex math line and make it more nice and understandable.",
    "created_at": "2010-03-16T23:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77175",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

This should allow to do some plethysm very easily.

Suggestion welcome to improve the latex math line and make it more nice and understandable.



---

archive/issue_comments_077176.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-16T23:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77176",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077177.json:
```json
{
    "body": "After face to face discussion, this patch is ready for review!",
    "created_at": "2010-04-21T13:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77177",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

After face to face discussion, this patch is ready for review!



---

archive/issue_comments_077178.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T13:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77178",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077179.json:
```json
{
    "body": "Changing keywords from \"permutation, cycle, enumeration\" to \"permutation groups, cycle index, Polya enumeration\".",
    "created_at": "2010-04-21T13:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77179",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "permutation, cycle, enumeration" to "permutation groups, cycle index, Polya enumeration".



---

archive/issue_comments_077180.json:
```json
{
    "body": "If I apply \"trac_8549_cycle_enumerator-nb.patch\" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8500, all tests pass.  If I apply *both* patches, though, then I get a doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\"\n**********************************************************************\nFile \"/Applications/sage_builds/sage-4.4.alpha1/devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 315:\n    sage: len(C.points())\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[7]>\", line 1, in <module>\n        len(C.points())###line 315:\n    sage: len(C.points())\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 327, in points\n        self.__points = self._points_fast_sqrt() # this is fast using Zech logarithms\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 239, in _points_fast_sqrt\n        points.append(self.point([x, v+sqrtD, one], check=True))\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/scheme.py\", line 256, in point\n        return self._point_class(self, v, check=check)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py\", line 196, in _point_class\n        return self.__A._point_class(*args, **kwds)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/projective_space.py\", line 535, in _point_class\n        return morphism.SchemeMorphism_projective_coordinates_field(*args, **kwds)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/morphism.py\", line 608, in __init__\n        X.codomain()._check_satisfies_equations(v)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py\", line 465, in _check_satisfies_equations\n        raise TypeError, \"Coordinates %s do not define a point on %s\"%(list(v),self)\n    TypeError: Coordinates [7*a + 9, 2*a + 2, 1] do not define a point on Hyperelliptic Curve over Finite Field in a of size 11^2 defined by y^2 + (x^2 + 2)*y = x^5 + x + 10\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_hyperelliptic_finite_field.py\n\t [8.2 s]\n```",
    "created_at": "2010-04-22T02:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77180",
    "user": "https://github.com/jhpalmieri"
}
```

If I apply "trac_8549_cycle_enumerator-nb.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8500, all tests pass.  If I apply *both* patches, though, then I get a doctest failure:

```
sage -t -long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
**********************************************************************
File "/Applications/sage_builds/sage-4.4.alpha1/devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 315:
    sage: len(C.points())
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        len(C.points())###line 315:
    sage: len(C.points())
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 327, in points
        self.__points = self._points_fast_sqrt() # this is fast using Zech logarithms
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 239, in _points_fast_sqrt
        points.append(self.point([x, v+sqrtD, one], check=True))
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/scheme.py", line 256, in point
        return self._point_class(self, v, check=check)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 196, in _point_class
        return self.__A._point_class(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/projective_space.py", line 535, in _point_class
        return morphism.SchemeMorphism_projective_coordinates_field(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/morphism.py", line 608, in __init__
        X.codomain()._check_satisfies_equations(v)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 465, in _check_satisfies_equations
        raise TypeError, "Coordinates %s do not define a point on %s"%(list(v),self)
    TypeError: Coordinates [7*a + 9, 2*a + 2, 1] do not define a point on Hyperelliptic Curve over Finite Field in a of size 11^2 defined by y^2 + (x^2 + 2)*y = x^5 + x + 10
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_hyperelliptic_finite_field.py
	 [8.2 s]
```



---

archive/issue_comments_077181.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-22T02:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77181",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077182.json:
```json
{
    "body": "I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.",
    "created_at": "2010-04-22T02:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77182",
    "user": "https://github.com/jhpalmieri"
}
```

I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.



---

archive/issue_comments_077183.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.\n\n\n#8500 and #8549 together pass all long tests on 64-bit Ubuntu 9.04.  I also saw Mike Hansen at Sage Days 21 test just the file `sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py` with both patches and it passed all tests as well.  I'll be working on a review at some point today.",
    "created_at": "2010-05-28T15:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77183",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:7 jhpalmieri]:
> I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.


#8500 and #8549 together pass all long tests on 64-bit Ubuntu 9.04.  I also saw Mike Hansen at Sage Days 21 test just the file `sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py` with both patches and it passed all tests as well.  I'll be working on a review at some point today.



---

archive/issue_comments_077184.json:
```json
{
    "body": "Nicolas(s),\n\nThis is a nice addition, and I can already think of a use for it in a classroom example.\n\nSome small comments/suggestions:\n\n1.  One small bit of language, in\n\n```\nHere are the cycle index of some permutation groups\n```\n\nI would write the plural as \"cycle indices.\"  Nicely written otherwise.\n\n\n2.  Would there be some way to qualify a value for the parent keyword as being legitimate?  For example, with `D=DihedralGroup(7)`, `14*D.cycle_index(parent=QQ)` goes boom.  It doesn't seem that there is a simple type to test on (but maybe I'm wrong on this), but it does look like parent need only implement  term() and sum().  Would it work to put something like  `parent.term(Partition([1]), 1)` in a try/except block?\n\n\n3.  Documentation.\n\n(a)  Do you want to add this into the reference manual?\n\n(b)  Last doctest block needs a preceding \"::\" to make it render as verbatim.\n\n(c)  Two instances of \"cycle_type\" near the top print weird due to the underscore.\n\n\nImportant stuff:  builds and passes long tests, works as advertised.  So I'm ready to give this a positive review subject to the above minor items.\n\nRob",
    "created_at": "2010-05-29T04:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77184",
    "user": "https://github.com/rbeezer"
}
```

Nicolas(s),

This is a nice addition, and I can already think of a use for it in a classroom example.

Some small comments/suggestions:

1.  One small bit of language, in

```
Here are the cycle index of some permutation groups
```

I would write the plural as "cycle indices."  Nicely written otherwise.


2.  Would there be some way to qualify a value for the parent keyword as being legitimate?  For example, with `D=DihedralGroup(7)`, `14*D.cycle_index(parent=QQ)` goes boom.  It doesn't seem that there is a simple type to test on (but maybe I'm wrong on this), but it does look like parent need only implement  term() and sum().  Would it work to put something like  `parent.term(Partition([1]), 1)` in a try/except block?


3.  Documentation.

(a)  Do you want to add this into the reference manual?

(b)  Last doctest block needs a preceding "::" to make it render as verbatim.

(c)  Two instances of "cycle_type" near the top print weird due to the underscore.


Important stuff:  builds and passes long tests, works as advertised.  So I'm ready to give this a positive review subject to the above minor items.

Rob



---

archive/issue_comments_077185.json:
```json
{
    "body": "See #8500 for the results of further OSX testing on this combination.",
    "created_at": "2010-05-29T04:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77185",
    "user": "https://github.com/rbeezer"
}
```

See #8500 for the results of further OSX testing on this combination.



---

archive/issue_comments_077186.json:
```json
{
    "body": "Hi,\n\nI just wrote a quick patch in the queue implementing the requested changes, and adding FinitePermutationGroups to the ref manual where it was missing. Nicolas, please double check, fold, and reupload.",
    "created_at": "2010-06-01T09:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77186",
    "user": "https://github.com/nthiery"
}
```

Hi,

I just wrote a quick patch in the queue implementing the requested changes, and adding FinitePermutationGroups to the ref manual where it was missing. Nicolas, please double check, fold, and reupload.



---

archive/issue_comments_077187.json:
```json
{
    "body": "Attachment [trac_8549_cycle_enumerator-nb.patch](tarball://root/attachments/some-uuid/ticket8549/trac_8549_cycle_enumerator-nb.patch) by nborie created at 2010-06-01 11:30:39\n\nThanks very much for these fix.\n\nAll tests pass for sage, all tests long and optionnal pass for the finite_permutation_groups, the doc is well built... New comments for parent argument make also more clear the doc.\n\nPositive Review from me. Thanks you Rob for pointing improvements and fix.",
    "created_at": "2010-06-01T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77187",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_8549_cycle_enumerator-nb.patch](tarball://root/attachments/some-uuid/ticket8549/trac_8549_cycle_enumerator-nb.patch) by nborie created at 2010-06-01 11:30:39

Thanks very much for these fix.

All tests pass for sage, all tests long and optionnal pass for the finite_permutation_groups, the doc is well built... New comments for parent argument make also more clear the doc.

Positive Review from me. Thanks you Rob for pointing improvements and fix.



---

archive/issue_comments_077188.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-01T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77188",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077189.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-01T11:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77189",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077190.json:
```json
{
    "body": "I change two times the status of this patch but I precise the last change come from Nicolas Thi\u00e9ry.\n\nThis positive review is also modulo the comment \n\n> If I apply \"trac_8549_cycle_enumerator-nb.patch\" on top of 4.4.alpha1, all tests pass. If I instead apply the patch from #8500, all tests pass. If I apply both patches, though, then I get a doctest failure\n\n\nI currently have no possible access to any OS X machine. All my tests was computing from Ubuntu machines.",
    "created_at": "2010-06-01T11:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77190",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I change two times the status of this patch but I precise the last change come from Nicolas Thiéry.

This positive review is also modulo the comment 

> If I apply "trac_8549_cycle_enumerator-nb.patch" on top of 4.4.alpha1, all tests pass. If I instead apply the patch from #8500, all tests pass. If I apply both patches, though, then I get a doctest failure


I currently have no possible access to any OS X machine. All my tests was computing from Ubuntu machines.



---

archive/issue_events_020597.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:29:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8549#event-20597"
}
```



---

archive/issue_comments_077191.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8549#issuecomment-77191",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
