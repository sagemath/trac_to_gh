# Issue 5618: Cyclotomic field elements are not convert to Gap correctly.

archive/issues_005618.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  joyner\n\nAlthough this works:\n\n```\nsage: K = CyclotomicField(3)\nsage: z = K.an_element(); z\nzeta3\nsage: gap(z)\nzeta3\n```\n\nthe resulting gap element doesn't have the correct properties:\n\n```\nsage: K(gap.E(3)) == z  # Good!\nTrue\nsage: gap(K(gap.E(3))) == gap.E(3)  # Bad!\nFalse\n```\n\n\nThis causes the following problem with group characters.\n\n```\nsage: H = AlternatingGroup(4)\nsage: g = H.list()[1]\nsage: K = H.subgroup([g])\nsage: z = CyclotomicField(3).an_element(); z\nsage: c = K.character([1,z,z**2])\n...\nRuntimeError: Gap produced error output\nError, no 1st choice method found for `CONDUCTOR' on 1 arguments\n```\n\nNote: the above works if one takes z = gap.E(3).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5618\n\n",
    "created_at": "2009-03-26T19:40:53Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Cyclotomic field elements are not convert to Gap correctly.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5618",
    "user": "https://github.com/saliola"
}
```
Assignee: tbd

CC:  joyner

Although this works:

```
sage: K = CyclotomicField(3)
sage: z = K.an_element(); z
zeta3
sage: gap(z)
zeta3
```

the resulting gap element doesn't have the correct properties:

```
sage: K(gap.E(3)) == z  # Good!
True
sage: gap(K(gap.E(3))) == gap.E(3)  # Bad!
False
```


This causes the following problem with group characters.

```
sage: H = AlternatingGroup(4)
sage: g = H.list()[1]
sage: K = H.subgroup([g])
sage: z = CyclotomicField(3).an_element(); z
sage: c = K.character([1,z,z**2])
...
RuntimeError: Gap produced error output
Error, no 1st choice method found for `CONDUCTOR' on 1 arguments
```

Note: the above works if one takes z = gap.E(3).

Issue created by migration from https://trac.sagemath.org/ticket/5618





---

archive/issue_comments_043780.json:
```json
{
    "body": "Here is some problem analysis:\n\n```\nsage: K = CyclotomicField(3)\nsage: z = K.an_element(); z\nzeta3\nsage: gap(z)\nzeta3\nsage: K(gap(z))\nzeta3\nsage: gap.E(3)\nE(3)\nsage: gap.E(3) == gap(z)\nFalse\nsage: K(gap.E(3)) == K(gap(z)) == z\nTrue\n```\n\n\nSo, apparently GAP treats \"the same\" elements of a cyclotomic field differently if they have different names. But this isn't particularly surprising, since the two cyclotomic fields seem to have a totaly different representation in GAP:\n\n```\nsage: ZFgap = gap('CyclotomicField(3)')\nsage: Kgap = gap(K)\nsage: Kgap\n<algebraic extension over the Rationals of degree 2>\nsage: ZFgap\nCF(3)\nsage: ZFgap.GeneratorsOfField()\n[ E(3) ]\nsage: Kgap.GeneratorsOfField()\n[ zeta3 ]\n```\n\n\nNote that comparison of the two field in the GAP interface results in an error:\n\n\n```\nsage: Kgap == ZFgap\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (47, 0))\n\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/king/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7061)()\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6943)()\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)\n   1527                                  other.name())) == P._true_symbol():\n   1528             return 0\n-> 1529         elif P.eval(\"%s %s %s\"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():\n   1530             return -1\n   1531         elif P.eval(\"%s %s %s\"%(self.name(), P._greaterthan_symbol(), other.name())) == P._true_symbol():\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in eval(self, x, newlines, strip, **kwds)\n    478             input_line += ';'\n    479\n--> 480         result = Expect.eval(self, input_line, **kwds)\n    481\n    482         if not newlines:\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)\n    981         try:\n    982             with gc_disabled():\n--> 983                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    984         except KeyboardInterrupt:\n    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    720                         return ''\n    721                 else:\n--> 722                     raise RuntimeError, message\n    723\n    724         except KeyboardInterrupt:\n\nRuntimeError: Gap produced error output\nError, no 1st choice method found for `LT' on 2 arguments\n\n   executing $sage2 < $sage8;\n```\n\n\nBut GAP indeed considers the two fields to be different:\n\n```\nsage: gap.eval(Kgap.name() + ' = ' + ZFgap.name())\n'false'\n```\n\n\nSo, what does all this mean?\n\n1. The `__cmp__` method of the GAP interface has a bug. An error raised by GAP when attempting \"<\" or \">\" should be caught and then \"=\" should be tried.\n2. A GAP cyclotomic field is different from the GAP version of a Sage cyclotomic field. This is since the GAP version of a Sage cyclotomic field is a number field. It could be solved by providing a genuine `_gap_init_` method for Sage cyclotomic fields (currently, it is inherited from number fields).\n\nIt seems likely to me that after implementing 2., things will already work. But 1. should be fixed as well.",
    "created_at": "2010-07-03T11:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43780",
    "user": "https://github.com/simon-king-jena"
}
```

Here is some problem analysis:

```
sage: K = CyclotomicField(3)
sage: z = K.an_element(); z
zeta3
sage: gap(z)
zeta3
sage: K(gap(z))
zeta3
sage: gap.E(3)
E(3)
sage: gap.E(3) == gap(z)
False
sage: K(gap.E(3)) == K(gap(z)) == z
True
```


So, apparently GAP treats "the same" elements of a cyclotomic field differently if they have different names. But this isn't particularly surprising, since the two cyclotomic fields seem to have a totaly different representation in GAP:

```
sage: ZFgap = gap('CyclotomicField(3)')
sage: Kgap = gap(K)
sage: Kgap
<algebraic extension over the Rationals of degree 2>
sage: ZFgap
CF(3)
sage: ZFgap.GeneratorsOfField()
[ E(3) ]
sage: Kgap.GeneratorsOfField()
[ zeta3 ]
```


Note that comparison of the two field in the GAP interface results in an error:


```
sage: Kgap == ZFgap
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (47, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7061)()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6943)()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)
   1527                                  other.name())) == P._true_symbol():
   1528             return 0
-> 1529         elif P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():
   1530             return -1
   1531         elif P.eval("%s %s %s"%(self.name(), P._greaterthan_symbol(), other.name())) == P._true_symbol():

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in eval(self, x, newlines, strip, **kwds)
    478             input_line += ';'
    479
--> 480         result = Expect.eval(self, input_line, **kwds)
    481
    482         if not newlines:

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)
    981         try:
    982             with gc_disabled():
--> 983                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    984         except KeyboardInterrupt:
    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    720                         return ''
    721                 else:
--> 722                     raise RuntimeError, message
    723
    724         except KeyboardInterrupt:

RuntimeError: Gap produced error output
Error, no 1st choice method found for `LT' on 2 arguments

   executing $sage2 < $sage8;
```


But GAP indeed considers the two fields to be different:

```
sage: gap.eval(Kgap.name() + ' = ' + ZFgap.name())
'false'
```


So, what does all this mean?

1. The `__cmp__` method of the GAP interface has a bug. An error raised by GAP when attempting "<" or ">" should be caught and then "=" should be tried.
2. A GAP cyclotomic field is different from the GAP version of a Sage cyclotomic field. This is since the GAP version of a Sage cyclotomic field is a number field. It could be solved by providing a genuine `_gap_init_` method for Sage cyclotomic fields (currently, it is inherited from number fields).

It seems likely to me that after implementing 2., things will already work. But 1. should be fixed as well.



---

archive/issue_comments_043781.json:
```json
{
    "body": "Gap-representation of Cyclotomic Fields should be a Cyclotomic Field in Gap",
    "created_at": "2010-07-04T18:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43781",
    "user": "https://github.com/simon-king-jena"
}
```

Gap-representation of Cyclotomic Fields should be a Cyclotomic Field in Gap



---

archive/issue_comments_043782.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-04T18:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43782",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043783.json:
```json
{
    "body": "Changing keywords from \"\" to \"gap interface cyclotomic field\".",
    "created_at": "2010-07-04T18:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43783",
    "user": "https://github.com/simon-king-jena"
}
```

Changing keywords from "" to "gap interface cyclotomic field".



---

archive/issue_comments_043784.json:
```json
{
    "body": "Attachment [trac_5618_gap_for_cyclotomic_fields.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields.patch) by @simon-king-jena created at 2010-07-04 18:46:22\n\nI created the patch after the patches from #8909 and #9423 -- so, it is possible that the new patch actually depends on the two other tickets (but one of them already has a positive review).\n\nWith the patch, a cyclotomic field in Sage is represented as a cyclotomic field (and not as a number field) in GAP:\n\n```\nsage: Z = CyclotomicField(8)\nsage: gap(Z)\nCF(8)\nsage: Z(gap(Z.0^2))\nzeta8^2\n```\n\n\nThe advantage is that the motivating example from the ticket description now works (and is used as a doctest):\n\n```\nsage: H = AlternatingGroup(4)\nsage: g = H.list()[1]\nsage: K = H.subgroup([g])\nsage: z = CyclotomicField(3).an_element(); z\nsage: c = K.character([1,z,z**2]); c\nCharacter of Subgroup of AlternatingGroup(4) generated by [(2,3,4)]\nsage: c(g^2); z^2\n-zeta3 - 1\n-zeta3 - 1\n```\n\n\nThe disadvantage: While it is still possible to chose the name of a number field generator in GAP as in Sage\n\n```\nsage: K.<tau> = NumberField(x^2+x+1)\nsage: gap(K)\n<algebraic extension over the Rationals of degree 3>\nsage: K.0\ntau\nsage: gap(K.0)\ntau\n```\n\nit is now impossible to do the same for cyclotomic fields:\n\n```\nsage: L.<zeta> = CyclotomicField(3)\nsage: L.0\nzeta\nsage: gap(L.0)\nE(3)\n```\n\n\nBy consequence, I had to fix a couple of doctests. All doctests pass, but I can not vouch for external code.",
    "created_at": "2010-07-04T18:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43784",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_5618_gap_for_cyclotomic_fields.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields.patch) by @simon-king-jena created at 2010-07-04 18:46:22

I created the patch after the patches from #8909 and #9423 -- so, it is possible that the new patch actually depends on the two other tickets (but one of them already has a positive review).

With the patch, a cyclotomic field in Sage is represented as a cyclotomic field (and not as a number field) in GAP:

```
sage: Z = CyclotomicField(8)
sage: gap(Z)
CF(8)
sage: Z(gap(Z.0^2))
zeta8^2
```


The advantage is that the motivating example from the ticket description now works (and is used as a doctest):

```
sage: H = AlternatingGroup(4)
sage: g = H.list()[1]
sage: K = H.subgroup([g])
sage: z = CyclotomicField(3).an_element(); z
sage: c = K.character([1,z,z**2]); c
Character of Subgroup of AlternatingGroup(4) generated by [(2,3,4)]
sage: c(g^2); z^2
-zeta3 - 1
-zeta3 - 1
```


The disadvantage: While it is still possible to chose the name of a number field generator in GAP as in Sage

```
sage: K.<tau> = NumberField(x^2+x+1)
sage: gap(K)
<algebraic extension over the Rationals of degree 3>
sage: K.0
tau
sage: gap(K.0)
tau
```

it is now impossible to do the same for cyclotomic fields:

```
sage: L.<zeta> = CyclotomicField(3)
sage: L.0
zeta
sage: gap(L.0)
E(3)
```


By consequence, I had to fix a couple of doctests. All doctests pass, but I can not vouch for external code.



---

archive/issue_comments_043785.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-04T16:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43785",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043786.json:
```json
{
    "body": "The patch simply converts sage Cyclotomic fields to gap cyclotomic fields instead of generic number fields. The disadvantage presented is just a limitation of gap, not sage.\n\nThe semantics of gap(CyclotomicField(n)) have changed!\nDeprecationWarning would be too pedantic here. Current behaviour of sage is considered a bug and I cannot see any functionality loss. So the code is ok.\n\nThe doctests are relevant. However, this patch depends on #9423 and one doctest has disappeared in that patch. That doctest is relevant, because it shows the change in the code. So, I would add the output of:\n\n\n```\nsage: F=CyclotomicField(8)\nsage: F.gen()\nsage: F._gap_init_() # the following variable name $sage1 represents the F.base_ring() in gap and is somehow random\nsage: f=gap(F)\nsage: f.GeneratorsOfDivisionRing() \n```\n\n\nin NumberField_cyclotomic._gap_init_()",
    "created_at": "2010-12-04T16:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43786",
    "user": "https://github.com/lftabera"
}
```

The patch simply converts sage Cyclotomic fields to gap cyclotomic fields instead of generic number fields. The disadvantage presented is just a limitation of gap, not sage.

The semantics of gap(CyclotomicField(n)) have changed!
DeprecationWarning would be too pedantic here. Current behaviour of sage is considered a bug and I cannot see any functionality loss. So the code is ok.

The doctests are relevant. However, this patch depends on #9423 and one doctest has disappeared in that patch. That doctest is relevant, because it shows the change in the code. So, I would add the output of:


```
sage: F=CyclotomicField(8)
sage: F.gen()
sage: F._gap_init_() # the following variable name $sage1 represents the F.base_ring() in gap and is somehow random
sage: f=gap(F)
sage: f.GeneratorsOfDivisionRing() 
```


in NumberField_cyclotomic._gap_init_()



---

archive/issue_comments_043787.json:
```json
{
    "body": "Attachment [trac_5618_gap_for_cyclotomic_fields.2.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields.2.patch) by @lftabera created at 2010-12-29 14:30:08\n\nupdated headers",
    "created_at": "2010-12-29T14:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43787",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac_5618_gap_for_cyclotomic_fields.2.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields.2.patch) by @lftabera created at 2010-12-29 14:30:08

updated headers



---

archive/issue_comments_043788.json:
```json
{
    "body": "additional doctest",
    "created_at": "2010-12-29T14:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43788",
    "user": "https://github.com/lftabera"
}
```

additional doctest



---

archive/issue_comments_043789.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-29T14:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43789",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043790.json:
```json
{
    "body": "Attachment [trac_5618_gap_for_cyclotomic_fields_doctest.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields_doctest.patch) by @lftabera created at 2010-12-29 14:34:16\n\nI give a positive review to Simon's patch. However, I have added some doctest in trac_5618_gap_for_cyclotomic_fields_doctest.patch that needs review. The doctest are in the unpatched code, but they have disappeared in the process. This patch put them back.\n\nApply:\n\ntrac_5618_gap_for_cyclotomic_fields.2.patch\n\ntrac_5618_gap_for_cyclotomic_fields_doctest.patch\n\nDepends on: #9423",
    "created_at": "2010-12-29T14:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43790",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac_5618_gap_for_cyclotomic_fields_doctest.patch](tarball://root/attachments/some-uuid/ticket5618/trac_5618_gap_for_cyclotomic_fields_doctest.patch) by @lftabera created at 2010-12-29 14:34:16

I give a positive review to Simon's patch. However, I have added some doctest in trac_5618_gap_for_cyclotomic_fields_doctest.patch that needs review. The doctest are in the unpatched code, but they have disappeared in the process. This patch put them back.

Apply:

trac_5618_gap_for_cyclotomic_fields.2.patch

trac_5618_gap_for_cyclotomic_fields_doctest.patch

Depends on: #9423



---

archive/issue_comments_043791.json:
```json
{
    "body": "Should this be marked positive review then?",
    "created_at": "2011-01-11T06:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Should this be marked positive review then?



---

archive/issue_comments_043792.json:
```json
{
    "body": "If you agreee with the doctest I wrote back in http://trac.sagemath.org/sage_trac/ticket/5618 yes, it should have a positive review.",
    "created_at": "2011-01-11T08:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43792",
    "user": "https://github.com/lftabera"
}
```

If you agreee with the doctest I wrote back in http://trac.sagemath.org/sage_trac/ticket/5618 yes, it should have a positive review.



---

archive/issue_comments_043793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T16:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43793",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043794.json:
```json
{
    "body": "The doctest looks fine to me. Let's get this in. (I'm not going to claim reviewer credit for this one -- I just verified that the doctest was the same as the one removed from #9423.)",
    "created_at": "2011-01-19T16:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43794",
    "user": "https://github.com/loefflerd"
}
```

The doctest looks fine to me. Let's get this in. (I'm not going to claim reviewer credit for this one -- I just verified that the doctest was the same as the one removed from #9423.)



---

archive/issue_comments_043795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5618#issuecomment-43795",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
