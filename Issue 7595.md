# Issue 7595: Chinese Remainder Theorem for polynomials over a field

archive/issues_007595.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis wasn't hard to implement, since all the hard work was already done.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7595\n\n",
    "created_at": "2009-12-03T17:27:53Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Chinese Remainder Theorem for polynomials over a field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7595",
    "user": "@rlmill"
}
```
Assignee: @aghitza

This wasn't hard to implement, since all the hard work was already done.

Issue created by migration from https://trac.sagemath.org/ticket/7595





---

archive/issue_comments_064762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-03T19:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64762",
    "user": "@rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064763.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-04T06:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64763",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_064764.json:
```json
{
    "body": "Hello !! This is clearly not my field but I dare intrude : I see you are using functions \"crt\" and \"CRT_list\", and I wondered if you would find it sensible to rename them to chinese_remainer_theorem and chinese_remainder_theorem_list ? If this is too long, it may be possible to drop the \"theorem\" from the name, but the fact remains that if I had to use this function sometime ( which is not excluded, as it is a very famous result ), there is no way on earth I would have thought of trying the \"crt\" function if I had not seen it related to this ticket :-)\n\nI am under the impression the english speakers would end this message with :\n\n\"Well, just my two cents\" :-)\n\nNathann",
    "created_at": "2009-12-04T06:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64764",
    "user": "@nathanncohen"
}
```

Hello !! This is clearly not my field but I dare intrude : I see you are using functions "crt" and "CRT_list", and I wondered if you would find it sensible to rename them to chinese_remainer_theorem and chinese_remainder_theorem_list ? If this is too long, it may be possible to drop the "theorem" from the name, but the fact remains that if I had to use this function sometime ( which is not excluded, as it is a very famous result ), there is no way on earth I would have thought of trying the "crt" function if I had not seen it related to this ticket :-)

I am under the impression the english speakers would end this message with :

"Well, just my two cents" :-)

Nathann



---

archive/issue_comments_064765.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-04T17:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64765",
    "user": "@rlmill"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064766.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> ... I wondered if you would find it sensible to rename them to chinese_remainer_theorem ...\n\nThis is irrelevant to this ticket. You should bring it up on sage-devel instead.",
    "created_at": "2009-12-04T17:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64766",
    "user": "@rlmill"
}
```

Replying to [comment:2 ncohen]:
> ... I wondered if you would find it sensible to rename them to chinese_remainer_theorem ...

This is irrelevant to this ticket. You should bring it up on sage-devel instead.



---

archive/issue_comments_064767.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T07:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64767",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064768.json:
```json
{
    "body": "Nice.",
    "created_at": "2009-12-08T07:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64768",
    "user": "@robertwb"
}
```

Nice.



---

archive/issue_comments_064769.json:
```json
{
    "body": "This patch wasn't applying, so I've rebased it. No real changes though.",
    "created_at": "2009-12-15T22:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64769",
    "user": "@rlmill"
}
```

This patch wasn't applying, so I've rebased it. No real changes though.



---

archive/issue_comments_064770.json:
```json
{
    "body": "rebased on 4.3.rc0",
    "created_at": "2009-12-15T23:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64770",
    "user": "@rlmill"
}
```

rebased on 4.3.rc0



---

archive/issue_comments_064771.json:
```json
{
    "body": "Attachment [trac_7595.patch](tarball://root/attachments/some-uuid/ticket7595/trac_7595.patch) by @rlmill created at 2009-12-15 23:16:31\n\nJust caught a doctest failure in sage/rings/arith.py. Oops!",
    "created_at": "2009-12-15T23:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64771",
    "user": "@rlmill"
}
```

Attachment [trac_7595.patch](tarball://root/attachments/some-uuid/ticket7595/trac_7595.patch) by @rlmill created at 2009-12-15 23:16:31

Just caught a doctest failure in sage/rings/arith.py. Oops!



---

archive/issue_comments_064772.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-16T02:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64772",
    "user": "@mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064773.json:
```json
{
    "body": "Which ticket is the patch conflicting with?",
    "created_at": "2009-12-16T02:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64773",
    "user": "@rlmill"
}
```

Which ticket is the patch conflicting with?



---

archive/issue_comments_064774.json:
```json
{
    "body": "I've checked, and this merges with the current rc1.",
    "created_at": "2009-12-18T22:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64774",
    "user": "@rlmill"
}
```

I've checked, and this merges with the current rc1.



---

archive/issue_comments_064775.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-18T22:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64775",
    "user": "@rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064776.json:
```json
{
    "body": "The patch is fine, applies to 4.3.rc0 and all tests pass in sage/rings.\n\nI have some problems with the CRT* functions though.\n\n1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.\n\n2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).\n\nOf course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.",
    "created_at": "2009-12-22T15:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64776",
    "user": "@JohnCremona"
}
```

The patch is fine, applies to 4.3.rc0 and all tests pass in sage/rings.

I have some problems with the CRT* functions though.

1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.

2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).

Of course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.



---

archive/issue_comments_064777.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-22T15:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64777",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064778.json:
```json
{
    "body": "I've made #7836 for this.",
    "created_at": "2010-01-03T21:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64778",
    "user": "@mwhansen"
}
```

I've made #7836 for this.



---

archive/issue_comments_064779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64779",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_064780.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-01-04T01:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64780",
    "user": "@mwhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_064781.json:
```json
{
    "body": "This causes failures in the following file `sage/quadratic_forms/quadratic_form__ternary_Tornaria.py`:\n\n\n```\n**********************************************************************\nFile \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 476:\n    sage: map(Q1.xi_rec, [-1,2,3,5])\nException raised:\n    Traceback (most recent call last):\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[8]>\", line 1, in <module>\n        map(Q1.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 476:\n    sage: map(Q1.xi_rec, [-1,2,3,5])\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 481, in xi_rec\n        return self.reciprocal().xi(p)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 456, in xi\n        return kronecker_symbol(p, self.basiclemma(2))\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 385, in basiclemma\n        a=self(self.basiclemmavec(M))\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 416, in basiclemmavec\n        return CRT_list(vec,mod)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py\", line 2522, in CRT_list\n        return moduli[0].parent()(v[0])\n      File \"parent.pyx\", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)\n      File \"integer.pyx\", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)\n    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer\n**********************************************************************\nFile \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 478:\n    sage: map(Q2.xi_rec, [-1,2,3,5])\nException raised:\n    Traceback (most recent call last):\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[9]>\", line 1, in <module>\n        map(Q2.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 478:\n    sage: map(Q2.xi_rec, [-1,2,3,5])\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 481, in xi_rec\n        return self.reciprocal().xi(p)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 456, in xi\n        return kronecker_symbol(p, self.basiclemma(2))\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 385, in basiclemma\n        a=self(self.basiclemmavec(M))\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\", line 416, in basiclemmavec\n        return CRT_list(vec,mod)\n      File \"/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py\", line 2522, in CRT_list\n        return moduli[0].parent()(v[0])\n      File \"parent.pyx\", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)\n      File \"integer.pyx\", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)\n    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer\n```\n",
    "created_at": "2010-01-04T01:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64781",
    "user": "@mwhansen"
}
```

This causes failures in the following file `sage/quadratic_forms/quadratic_form__ternary_Tornaria.py`:


```
**********************************************************************
File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 476:
    sage: map(Q1.xi_rec, [-1,2,3,5])
Exception raised:
    Traceback (most recent call last):
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[8]>", line 1, in <module>
        map(Q1.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 476:
    sage: map(Q1.xi_rec, [-1,2,3,5])
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 481, in xi_rec
        return self.reciprocal().xi(p)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 456, in xi
        return kronecker_symbol(p, self.basiclemma(2))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 385, in basiclemma
        a=self(self.basiclemmavec(M))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 416, in basiclemmavec
        return CRT_list(vec,mod)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py", line 2522, in CRT_list
        return moduli[0].parent()(v[0])
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "integer.pyx", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)
    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer
**********************************************************************
File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 478:
    sage: map(Q2.xi_rec, [-1,2,3,5])
Exception raised:
    Traceback (most recent call last):
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[9]>", line 1, in <module>
        map(Q2.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 478:
    sage: map(Q2.xi_rec, [-1,2,3,5])
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 481, in xi_rec
        return self.reciprocal().xi(p)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 456, in xi
        return kronecker_symbol(p, self.basiclemma(2))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 385, in basiclemma
        a=self(self.basiclemmavec(M))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 416, in basiclemmavec
        return CRT_list(vec,mod)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py", line 2522, in CRT_list
        return moduli[0].parent()(v[0])
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "integer.pyx", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)
    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer
```




---

archive/issue_comments_064782.json:
```json
{
    "body": "Attachment [trac_7595-failures.patch](tarball://root/attachments/some-uuid/ticket7595/trac_7595-failures.patch) by @rlmill created at 2010-01-04 15:37:39\n\nShould fix the issues in quadratic_form__ternary_Tornaria.py",
    "created_at": "2010-01-04T15:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64782",
    "user": "@rlmill"
}
```

Attachment [trac_7595-failures.patch](tarball://root/attachments/some-uuid/ticket7595/trac_7595-failures.patch) by @rlmill created at 2010-01-04 15:37:39

Should fix the issues in quadratic_form__ternary_Tornaria.py



---

archive/issue_comments_064783.json:
```json
{
    "body": "This patch should fix the issues mentioned above. I wasn't sure whether to make a new ticket, or just post it here (never seen a \"needs_work\" closed ticket...)",
    "created_at": "2010-01-04T15:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64783",
    "user": "@rlmill"
}
```

This patch should fix the issues mentioned above. I wasn't sure whether to make a new ticket, or just post it here (never seen a "needs_work" closed ticket...)



---

archive/issue_comments_064784.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-04T16:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64784",
    "user": "@JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064785.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-04T16:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64785",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064786.json:
```json
{
    "body": "I changed the ticket to \"needs review\" and then gave it a positive review -- it works for me.",
    "created_at": "2010-01-04T16:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64786",
    "user": "@JohnCremona"
}
```

I changed the ticket to "needs review" and then gave it a positive review -- it works for me.



---

archive/issue_comments_064787.json:
```json
{
    "body": "This ticket is rather messy. The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 and it was then closed as being fixed in that version. Later on, the value in the field \"Merged in:\" was deleted. Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1. And yet the ticket is declared as \"fixed\", but without a value for the field \"Merged in:\". I think the ticket's status should now be \"open\" not \"fixed\", until `trac_7595-failures.patch` is merged.",
    "created_at": "2010-01-07T00:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64787",
    "user": "mvngu"
}
```

This ticket is rather messy. The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 and it was then closed as being fixed in that version. Later on, the value in the field "Merged in:" was deleted. Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1. And yet the ticket is declared as "fixed", but without a value for the field "Merged in:". I think the ticket's status should now be "open" not "fixed", until `trac_7595-failures.patch` is merged.



---

archive/issue_comments_064788.json:
```json
{
    "body": "Replying to [comment:16 mvngu]:\n> The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 ... Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1.\n\nThe patch was rolled back-- neither is in Sage-4.3.1.alpha1\n\n> And yet the ticket is declared as \"fixed\"...\n\nApparently when the ticket was reopened, this did not revert. I don't know how to fix this, but the ticket is definitely open.\n\n> ... until `trac_7595-failures.patch` is merged.\n\nRepeat: as of sage-4.3.1.alpha1, *both* patches need to be merged.",
    "created_at": "2010-01-07T04:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7595#issuecomment-64788",
    "user": "@rlmill"
}
```

Replying to [comment:16 mvngu]:
> The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 ... Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1.

The patch was rolled back-- neither is in Sage-4.3.1.alpha1

> And yet the ticket is declared as "fixed"...

Apparently when the ticket was reopened, this did not revert. I don't know how to fix this, but the ticket is definitely open.

> ... until `trac_7595-failures.patch` is merged.

Repeat: as of sage-4.3.1.alpha1, *both* patches need to be merged.
