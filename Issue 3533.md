# Issue 3533: [with patch, needs review] better number fields (mostly cyclotomic)

archive/issues_003533.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro @mwhansen\n\nThis attached patch makes several changes to\n`sage/rings/number_field/number_field.py` and\n`sage/rings/number_field/morphism.py` that are mainly concerned with\nimproving performance for cyclotomic fields, but also tidy up various\nother things.  The main changes are summarised below.\n\n\nThere is a serious bug in `roots_of_unity` when applied to relative number \nfields:\n\n```\nsage: K.<a> = NumberField([x^2 + 3, x^2 + 1])\nsage: K.roots_of_unity()\n[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\n```\n\nBut\n\n```\nsage: K.absolute_field('b').roots_of_unity()\n[1/8*b^3 + 1/4*b^2 + 3/4*b + 1,\n 1/8*b^3 + 5/4*b + 1/2,\n...\n```\n\nso it is clear how to deal with the problem.\n\nIn addition, the `roots_of_unity` and `number_of_roots_of_unity` methods can\nrather obviously be made **much** faster for cyclotomic fields.  \n\nSimilarly, I've written a method for listing the embeddings of a cyclotomic field in\na number field which runs much more quickly than at present.\n\nFor the general case of finding embeddings of number fields, at the moment\nSAGE asks PARI to look for roots when a simple degree check indicates that\nthere are none.  It is, of course, very easy to avoid this wasted time.\n\nA method for complex embeddings of cyclotomic fields already exists, but it\nis inadequate in two ways.  First, it handles the default precision in a\ndifferent way from the method for generic complex embeddings.  Second, it\nfails to cache the result.  These faults have been corrected, and the\nchange in respect of precision also applied to `complex_embedding` (in the\nsingular).\n\nThere is also a slight problem with the `embeddings` function (used by\nthe generic `complex_embeddings` and `real_embeddings`).  It caches its\noutput, but the first time it is called it returns something different from\nwhat has been cached (a `list` rather than a `Sequence`).  This has been\nchanged for both the generic field and the relative field methods.  In\naddition the code now avoids the printing of empty lists of field embeddings on\nthree lines.\n\nI've added a method for real embeddings of cyclotomic fields.  Nobody who \nknows what they're doing would use this function, but it might as well be \nefficient.\n\nMany other functions can be speeded up for cyclotomic fields, \nbecause of the vast amount of theory about these fields.  As well as the \nabove, I've implemented `signature`, `discriminant` and `is_isomorphic` \nfor cyclotomic fields.  Probably more could be done.  Galois groups are an \nobvious example, but that had better wait until ticket #133 is sorted out.\n\nSome of the existing doctests have been moved when they apply to \ncyclotomic fields.  Others have been added.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3533\n\n",
    "created_at": "2008-06-29T09:56:15Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] better number fields (mostly cyclotomic)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3533",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: @williamstein

CC:  @craigcitro @mwhansen

This attached patch makes several changes to
`sage/rings/number_field/number_field.py` and
`sage/rings/number_field/morphism.py` that are mainly concerned with
improving performance for cyclotomic fields, but also tidy up various
other things.  The main changes are summarised below.


There is a serious bug in `roots_of_unity` when applied to relative number 
fields:

```
sage: K.<a> = NumberField([x^2 + 3, x^2 + 1])
sage: K.roots_of_unity()
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

But

```
sage: K.absolute_field('b').roots_of_unity()
[1/8*b^3 + 1/4*b^2 + 3/4*b + 1,
 1/8*b^3 + 5/4*b + 1/2,
...
```

so it is clear how to deal with the problem.

In addition, the `roots_of_unity` and `number_of_roots_of_unity` methods can
rather obviously be made **much** faster for cyclotomic fields.  

Similarly, I've written a method for listing the embeddings of a cyclotomic field in
a number field which runs much more quickly than at present.

For the general case of finding embeddings of number fields, at the moment
SAGE asks PARI to look for roots when a simple degree check indicates that
there are none.  It is, of course, very easy to avoid this wasted time.

A method for complex embeddings of cyclotomic fields already exists, but it
is inadequate in two ways.  First, it handles the default precision in a
different way from the method for generic complex embeddings.  Second, it
fails to cache the result.  These faults have been corrected, and the
change in respect of precision also applied to `complex_embedding` (in the
singular).

There is also a slight problem with the `embeddings` function (used by
the generic `complex_embeddings` and `real_embeddings`).  It caches its
output, but the first time it is called it returns something different from
what has been cached (a `list` rather than a `Sequence`).  This has been
changed for both the generic field and the relative field methods.  In
addition the code now avoids the printing of empty lists of field embeddings on
three lines.

I've added a method for real embeddings of cyclotomic fields.  Nobody who 
knows what they're doing would use this function, but it might as well be 
efficient.

Many other functions can be speeded up for cyclotomic fields, 
because of the vast amount of theory about these fields.  As well as the 
above, I've implemented `signature`, `discriminant` and `is_isomorphic` 
for cyclotomic fields.  Probably more could be done.  Galois groups are an 
obvious example, but that had better wait until ticket #133 is sorted out.

Some of the existing doctests have been moved when they apply to 
cyclotomic fields.  Others have been added.



Issue created by migration from https://trac.sagemath.org/ticket/3533





---

archive/issue_comments_024875.json:
```json
{
    "body": "Attachment [sage-3533.patch](tarball://root/attachments/some-uuid/ticket3533/sage-3533.patch) by fwclarke created at 2008-06-29 09:59:13",
    "created_at": "2008-06-29T09:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24875",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage-3533.patch](tarball://root/attachments/some-uuid/ticket3533/sage-3533.patch) by fwclarke created at 2008-06-29 09:59:13



---

archive/issue_comments_024876.json:
```json
{
    "body": "Review report by John Cremona:\n\n1. The aims of the patch all look good to me.\n2. Reading the patch diffs it looked ok.  It would be better if someone else took a look too.\n3. The patch applied cleanly to 3.0.4.alpha0\n4. I tested all the number_fields directory but found the following failures:\n\n\n```\n\tsage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field_element.pyx\n\tsage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field.py\n```\n\n\nIn detail:\n\n```\nFile \"/home/jec/sage-current/tmp/number_field_element.py\", line 523:\n    sage: abs(z)\nExpected:\n    1.00000000000000\nGot:\n    1.0\n**********************************************************************\nFile \"/home/jec/sage-current/tmp/number_field_element.py\", line 525:\n    sage: abs(z^2 + 17*z - 3)\nExpected:\n    16.0604426799931\nGot:\n    16.06044268\n```\n\n\nand\n\n\n\n```\nFile \"/home/jec/sage-current/tmp/number_field.py\", line 5552:\n    sage: C.complex_embeddings()\nExpected:\n    [\n    Ring morphism:\n      From: Cyclotomic Field of order 4 and degree 2\n      To:   Complex Double Field\n      Defn: zeta4 |--> 2.77555756156e-17 - 1.0*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 4 and degree 2\n      To:   Complex Double Field\n      Defn: zeta4 |--> -1.83690953073e-16 + 1.0*I\n    ]\nGot:\n    [\n    Ring morphism:\n      From: Cyclotomic Field of order 4 and degree 2\n      To:   Complex Double Field\n      Defn: zeta4 |--> 2.77555756156e-17 - 1.0*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 4 and degree 2\n      To:   Complex Double Field\n      Defn: zeta4 |--> -1.83697019872e-16 + 1.0*I\n    ]\n```\n\n\nThese do not look serious, they are to do with outputting floating point numbers, but there must be a way to get the tests to pass (\"#random low order bits\" if desperate).",
    "created_at": "2008-06-29T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24876",
    "user": "https://github.com/JohnCremona"
}
```

Review report by John Cremona:

1. The aims of the patch all look good to me.
2. Reading the patch diffs it looked ok.  It would be better if someone else took a look too.
3. The patch applied cleanly to 3.0.4.alpha0
4. I tested all the number_fields directory but found the following failures:


```
	sage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field_element.pyx
	sage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field.py
```


In detail:

```
File "/home/jec/sage-current/tmp/number_field_element.py", line 523:
    sage: abs(z)
Expected:
    1.00000000000000
Got:
    1.0
**********************************************************************
File "/home/jec/sage-current/tmp/number_field_element.py", line 525:
    sage: abs(z^2 + 17*z - 3)
Expected:
    16.0604426799931
Got:
    16.06044268
```


and



```
File "/home/jec/sage-current/tmp/number_field.py", line 5552:
    sage: C.complex_embeddings()
Expected:
    [
    Ring morphism:
      From: Cyclotomic Field of order 4 and degree 2
      To:   Complex Double Field
      Defn: zeta4 |--> 2.77555756156e-17 - 1.0*I,
    Ring morphism:
      From: Cyclotomic Field of order 4 and degree 2
      To:   Complex Double Field
      Defn: zeta4 |--> -1.83690953073e-16 + 1.0*I
    ]
Got:
    [
    Ring morphism:
      From: Cyclotomic Field of order 4 and degree 2
      To:   Complex Double Field
      Defn: zeta4 |--> 2.77555756156e-17 - 1.0*I,
    Ring morphism:
      From: Cyclotomic Field of order 4 and degree 2
      To:   Complex Double Field
      Defn: zeta4 |--> -1.83697019872e-16 + 1.0*I
    ]
```


These do not look serious, they are to do with outputting floating point numbers, but there must be a way to get the tests to pass ("#random low order bits" if desperate).



---

archive/issue_comments_024877.json:
```json
{
    "body": "Attachment [sage.3533a.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533a.patch) by fwclarke created at 2008-06-29 21:05:36",
    "created_at": "2008-06-29T21:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24877",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage.3533a.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533a.patch) by fwclarke created at 2008-06-29 21:05:36



---

archive/issue_comments_024878.json:
```json
{
    "body": "The varying results for `abs` derive from the changed default precision \nused for cyclotomic fields (so that they're compatible with generic number \nfields).  Using the generic methods, the same answers are obtained (with or without the patch) for \n\n```\nsage: z = NumberField(cyclotomic_polynomial(7), 'a').gen()\nsage: abs(z)\n1.0\nsage: (z^2 + 17*z - 3).abs(i=5)\n16.06044268\n```\n\n(`i=5` is necessary because the ordering of the embeddings is different \nfor the two ways of constructing the same field.)\n\nI have therefore made the appropriate changes to the doctest in `number_field_element.pyx`\nin a new patch.\n\nThe second doctest failure is both more trivial and more worrying.  I \ndon't actually understand the following behaviour:\n\n```\nsage: z = exp(I*pi/2); z\nI\nsage: [CDF(I), CDF(z)]\n[1.0*I, 6.12303176911e-17 + 1.0*I]\n```\n\n\nBut anyway, the issue here is nothing to do with number fields.  The easy\nway out is to change the example to make it less trivial, and this is done\nin the new patch.\n\nHaven't tried it with 3.0.4.alpha0, but with 3.0.3 and both patches all \ntests pass.",
    "created_at": "2008-06-29T21:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24878",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The varying results for `abs` derive from the changed default precision 
used for cyclotomic fields (so that they're compatible with generic number 
fields).  Using the generic methods, the same answers are obtained (with or without the patch) for 

```
sage: z = NumberField(cyclotomic_polynomial(7), 'a').gen()
sage: abs(z)
1.0
sage: (z^2 + 17*z - 3).abs(i=5)
16.06044268
```

(`i=5` is necessary because the ordering of the embeddings is different 
for the two ways of constructing the same field.)

I have therefore made the appropriate changes to the doctest in `number_field_element.pyx`
in a new patch.

The second doctest failure is both more trivial and more worrying.  I 
don't actually understand the following behaviour:

```
sage: z = exp(I*pi/2); z
I
sage: [CDF(I), CDF(z)]
[1.0*I, 6.12303176911e-17 + 1.0*I]
```


But anyway, the issue here is nothing to do with number fields.  The easy
way out is to change the example to make it less trivial, and this is done
in the new patch.

Haven't tried it with 3.0.4.alpha0, but with 3.0.3 and both patches all 
tests pass.



---

archive/issue_comments_024879.json:
```json
{
    "body": "Replying to [comment:3 fwclarke]:\n> The varying results for `abs` derive from the changed default precision \n> used for cyclotomic fields (so that they're compatible with generic number \n> fields).  Using the generic methods, the same answers are obtained (with or without the patch) for \n> {{{\n> sage: z = NumberField(cyclotomic_polynomial(7), 'a').gen()\n> sage: abs(z)\n> 1.0\n> sage: (z^2 + 17*z - 3).abs(i=5)\n> 16.06044268\n> }}}\n> (`i=5` is necessary because the ordering of the embeddings is different \n> for the two ways of constructing the same field.)\n> \n> I have therefore made the appropriate changes to the doctest in `number_field_element.pyx`\n> in a new patch.\n> \n> The second doctest failure is both more trivial and more worrying.  I \n> don't actually understand the following behaviour:\n> {{{\n> sage: z = exp(I*pi/2); z\n> I\n> sage: [CDF(I), CDF(z)]\n> [1.0*I, 6.12303176911e-17 + 1.0*I]\n> }}}\n> \n\nDoes this explain it?\n\n```\nsage: z = exp(I*pi/2); z\nI\nsage: type(z)           \n<class 'sage.calculus.calculus.SymbolicComposition'>\nsage: type(I)           \n<class 'sage.functions.constants.I_class'>\n```\n\nSo z displays as I but it is not I.  Hmmm\n\n```\nsage: z is I\nFalse\nsage: z == I\nI == I\nsage: bool(z == I)\nTrue\n```\n\n\n\n\n> But anyway, the issue here is nothing to do with number fields.  The easy\n> way out is to change the example to make it less trivial, and this is done\n> in the new patch.\n> \n> Haven't tried it with 3.0.4.alpha0, but with 3.0.3 and both patches all \n> tests pass.\n> \n\nI'll check out the second patch now.",
    "created_at": "2008-06-29T21:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24879",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 fwclarke]:
> The varying results for `abs` derive from the changed default precision 
> used for cyclotomic fields (so that they're compatible with generic number 
> fields).  Using the generic methods, the same answers are obtained (with or without the patch) for 
> {{{
> sage: z = NumberField(cyclotomic_polynomial(7), 'a').gen()
> sage: abs(z)
> 1.0
> sage: (z^2 + 17*z - 3).abs(i=5)
> 16.06044268
> }}}
> (`i=5` is necessary because the ordering of the embeddings is different 
> for the two ways of constructing the same field.)
> 
> I have therefore made the appropriate changes to the doctest in `number_field_element.pyx`
> in a new patch.
> 
> The second doctest failure is both more trivial and more worrying.  I 
> don't actually understand the following behaviour:
> {{{
> sage: z = exp(I*pi/2); z
> I
> sage: [CDF(I), CDF(z)]
> [1.0*I, 6.12303176911e-17 + 1.0*I]
> }}}
> 

Does this explain it?

```
sage: z = exp(I*pi/2); z
I
sage: type(z)           
<class 'sage.calculus.calculus.SymbolicComposition'>
sage: type(I)           
<class 'sage.functions.constants.I_class'>
```

So z displays as I but it is not I.  Hmmm

```
sage: z is I
False
sage: z == I
I == I
sage: bool(z == I)
True
```




> But anyway, the issue here is nothing to do with number fields.  The easy
> way out is to change the example to make it less trivial, and this is done
> in the new patch.
> 
> Haven't tried it with 3.0.4.alpha0, but with 3.0.3 and both patches all 
> tests pass.
> 

I'll check out the second patch now.



---

archive/issue_comments_024880.json:
```json
{
    "body": "Nearly there but not quite:\n\n```\nsage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field.py**********************************************************************\nFile \"/home/jec/sage-current/tmp/number_field.py\", line 5551:\n    sage: CyclotomicField(5).complex_embeddings()\nExpected:\n    [\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> 0.309016994375 - 0.951056516295*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> -0.809016994375 - 0.587785252292*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> -0.809016994375 + 0.587785252292*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> 0.309016994375 + 0.951056516295*I\n    ]\nGot:\n    [\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> 0.309016994375 + 0.951056516295*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> -0.809016994375 + 0.587785252292*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> -0.809016994375 - 0.587785252292*I,\n    Ring morphism:\n      From: Cyclotomic Field of order 5 and degree 4\n      To:   Complex Double Field\n      Defn: zeta5 |--> 0.309016994375 - 0.951056516295*I\n    ]\n\n**********************************************************************\n1 items had failures:\n   1 of   2 in __main__.example_165\n***Test Failed*** 1 failures.\n```\n\n\nThe only difference is in the order of the 4 elements in the list.\nI think you need to apply sort() to the list returned by `complex_embeddings()` to ensure consistency.",
    "created_at": "2008-06-29T21:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24880",
    "user": "https://github.com/JohnCremona"
}
```

Nearly there but not quite:

```
sage -t  sage-3.0.4.alpha0/devel/sage-3533/sage/rings/number_field//number_field.py**********************************************************************
File "/home/jec/sage-current/tmp/number_field.py", line 5551:
    sage: CyclotomicField(5).complex_embeddings()
Expected:
    [
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> 0.309016994375 - 0.951056516295*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> -0.809016994375 - 0.587785252292*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> -0.809016994375 + 0.587785252292*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> 0.309016994375 + 0.951056516295*I
    ]
Got:
    [
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> 0.309016994375 + 0.951056516295*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> -0.809016994375 + 0.587785252292*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> -0.809016994375 - 0.587785252292*I,
    Ring morphism:
      From: Cyclotomic Field of order 5 and degree 4
      To:   Complex Double Field
      Defn: zeta5 |--> 0.309016994375 - 0.951056516295*I
    ]

**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_165
***Test Failed*** 1 failures.
```


The only difference is in the order of the 4 elements in the list.
I think you need to apply sort() to the list returned by `complex_embeddings()` to ensure consistency.



---

archive/issue_comments_024881.json:
```json
{
    "body": "I would like to note that there have been significant changes to the number field files in the coercion branch. I think most of the changes in this ticket are orthogonal to the coercion ones, but this is something we should be aware of and I'm not so sure how clean the merge will be.",
    "created_at": "2008-06-30T15:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24881",
    "user": "https://github.com/robertwb"
}
```

I would like to note that there have been significant changes to the number field files in the coercion branch. I think most of the changes in this ticket are orthogonal to the coercion ones, but this is something we should be aware of and I'm not so sure how clean the merge will be.



---

archive/issue_comments_024882.json:
```json
{
    "body": "I think the order of embeddings is reasonable: in terms of the powers of a\nprimitive n-th root.  But what this failure has exposed is that\n`CDF.zeta(n)` uses the generic method in `ring.pyx`.  This certainly needs\nchanging.  At the moment we have\n\n```\nsage: version()\n'SAGE Version 3.0.3, Release Date: 2008-06-17'\nsage: timeit('CDF.zeta(117)')\n5 loops, best of 3: 42.3 ms per loop\nsage: timeit('ComplexField(64).zeta(117)')\n625 loops, best of 3: 77 \u00b5s per loop\n```\n\n`CDF` is supposed to be *faster* than `ComplexField`!\n\nI've written a patch to include a new `zeta` method for `CDF` and modify\ntwo doctests so that they comply.  All tests pass with 3.0.3.\n\nAfter the patch:\n\n```\nsage: timeit('CDF.zeta(117)')\n625 loops, best of 3: 22.9 \u00b5s per loop\n```\n\n\nI don't think there are likely to be any coercion problems, since all the\ncode in these patches is just a minor adaptation of code used elsewhere.",
    "created_at": "2008-07-04T12:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24882",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

I think the order of embeddings is reasonable: in terms of the powers of a
primitive n-th root.  But what this failure has exposed is that
`CDF.zeta(n)` uses the generic method in `ring.pyx`.  This certainly needs
changing.  At the moment we have

```
sage: version()
'SAGE Version 3.0.3, Release Date: 2008-06-17'
sage: timeit('CDF.zeta(117)')
5 loops, best of 3: 42.3 ms per loop
sage: timeit('ComplexField(64).zeta(117)')
625 loops, best of 3: 77 µs per loop
```

`CDF` is supposed to be *faster* than `ComplexField`!

I've written a patch to include a new `zeta` method for `CDF` and modify
two doctests so that they comply.  All tests pass with 3.0.3.

After the patch:

```
sage: timeit('CDF.zeta(117)')
625 loops, best of 3: 22.9 µs per loop
```


I don't think there are likely to be any coercion problems, since all the
code in these patches is just a minor adaptation of code used elsewhere.



---

archive/issue_comments_024883.json:
```json
{
    "body": "Attachment [sage.3533b.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533b.patch) by fwclarke created at 2008-07-04 12:15:09",
    "created_at": "2008-07-04T12:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24883",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage.3533b.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533b.patch) by fwclarke created at 2008-07-04 12:15:09



---

archive/issue_comments_024884.json:
```json
{
    "body": "The patches (all three in succession) apply cleanly to 3.0.4.alpha0, and all tests (in sage/rings/number_field) pass.\n\nTo be really picky,  the new CDF.zeta(n) returns None if n<=0.  This could conceivably trip someone up -- and I haven't checked to see what the other .zeta() functions do for arguments which are not positive.  I think one might argue for CDF.zeta(-n)=CDF.zeta(n) and CDF.zeta(0)=1, but it might be better to throw a ValueError if n<1.\n \nIn the 4th patch sage.3533c.patch I added tests to this effect and corresponding doctests.  I also deleted some weird stuff at the end of complex_double.pyx which I assume is garbage.",
    "created_at": "2008-07-04T15:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24884",
    "user": "https://github.com/JohnCremona"
}
```

The patches (all three in succession) apply cleanly to 3.0.4.alpha0, and all tests (in sage/rings/number_field) pass.

To be really picky,  the new CDF.zeta(n) returns None if n<=0.  This could conceivably trip someone up -- and I haven't checked to see what the other .zeta() functions do for arguments which are not positive.  I think one might argue for CDF.zeta(-n)=CDF.zeta(n) and CDF.zeta(0)=1, but it might be better to throw a ValueError if n<1.
 
In the 4th patch sage.3533c.patch I added tests to this effect and corresponding doctests.  I also deleted some weird stuff at the end of complex_double.pyx which I assume is garbage.



---

archive/issue_comments_024885.json:
```json
{
    "body": "Attachment [sage.3533c.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533c.patch) by @JohnCremona created at 2008-07-04 15:08:50",
    "created_at": "2008-07-04T15:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24885",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage.3533c.patch](tarball://root/attachments/some-uuid/ticket3533/sage.3533c.patch) by @JohnCremona created at 2008-07-04 15:08:50



---

archive/issue_comments_024886.json:
```json
{
    "body": "My concerns about coercion were not that things would become incompatible, it was just that there have been so many changes to the number field file (especially cyclotomic fields) that the resulting merge could be painful. It would just be a question of timing, the code (what I've looked at) looks good. Mike Hansen has volunteered to do the merge with 3.0.4, so perhaps he should comment on whether or not it would cause any problems (if not, I don't want to hold it up).",
    "created_at": "2008-07-04T17:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24886",
    "user": "https://github.com/robertwb"
}
```

My concerns about coercion were not that things would become incompatible, it was just that there have been so many changes to the number field file (especially cyclotomic fields) that the resulting merge could be painful. It would just be a question of timing, the code (what I've looked at) looks good. Mike Hansen has volunteered to do the merge with 3.0.4, so perhaps he should comment on whether or not it would cause any problems (if not, I don't want to hold it up).



---

archive/issue_comments_024887.json:
```json
{
    "body": "Mike said in IRC minutes ago:\n\n```\nmhansen: mabshoff: I looked at #3533 and it's good to go.  I can handle the merge issues.\n```\n\nso I am merging those patches ASAP.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-05T23:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike said in IRC minutes ago:

```
mhansen: mabshoff: I looked at #3533 and it's good to go.  I can handle the merge issues.
```

so I am merging those patches ASAP.

Cheers,

Michael



---

archive/issue_comments_024888.json:
```json
{
    "body": "I am seeing some trivial to fix numerical noise doctest failures:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t -long devel/sage/sage/modular/dirichlet.py # 5 doctests failed\nsage -t -long devel/sage/sage/modular/dirichlet.py          **********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py\", line 674:\n    sage: e.gauss_sum_numerical()\nExpected:\n    5.55111512312578e-16 + 1.73205080756888*I\nGot:\n    9.43689570931e-16 + 1.73205080757*I\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py\", line 676:\n    sage: abs(e.gauss_sum_numerical())\nExpected:\n    1.73205080756888\nGot:\n    1.73205080757\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py\", line 680:\n    sage: e.gauss_sum_numerical(a=2)\nExpected:\n    -1.11022302462516e-15 - 1.73205080756888*I\nGot:\n    -1.33226762955e-15 - 1.73205080757*I\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py\", line 686:\n    sage: e.gauss_sum_numerical()\nExpected:\n    -3.07497205899524 + 1.88269669261902*I\nGot:\n    -3.074972059 + 1.88269669262*I\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py\", line 688:\n    sage: abs(e.gauss_sum_numerical())\nExpected:\n    3.60555127546399\nGot:\n    3.60555127546\n**********************************************************************\n1 items had failures:\n   5 of  13 in __main__.example_23\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_dirichlet.py\n\t [3.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long devel/sage/sage/modular/dirichlet.py\nTotal time for all tests: 3.4 seconds\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t -long devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 3 doctests failed\nsage -t -long devel/sage/sage/matrix/matrix_cyclo_dense.pyx \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py\", line 664:\n    sage: (A[1,0]).abs()\nExpected:\n    12.9975436637560\nGot:\n    12.9975436638\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py\", line 697:\n    sage: A.height()\nExpected:\n    12.9975436637560\nGot:\n    12.9975436638\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py\", line 699:\n    sage: (A[1,0]).abs()\nExpected:\n    12.9975436637560\nGot:\n    12.9975436638\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_20\n   2 of   5 in __main__.example_21\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_matrix_cyclo_dense.py\n\t [9.8 s]\nexit code: 1024\n```\n\n\nPatch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T00:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing some trivial to fix numerical noise doctest failures:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t -long devel/sage/sage/modular/dirichlet.py # 5 doctests failed
sage -t -long devel/sage/sage/modular/dirichlet.py          **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py", line 674:
    sage: e.gauss_sum_numerical()
Expected:
    5.55111512312578e-16 + 1.73205080756888*I
Got:
    9.43689570931e-16 + 1.73205080757*I
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py", line 676:
    sage: abs(e.gauss_sum_numerical())
Expected:
    1.73205080756888
Got:
    1.73205080757
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py", line 680:
    sage: e.gauss_sum_numerical(a=2)
Expected:
    -1.11022302462516e-15 - 1.73205080756888*I
Got:
    -1.33226762955e-15 - 1.73205080757*I
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py", line 686:
    sage: e.gauss_sum_numerical()
Expected:
    -3.07497205899524 + 1.88269669261902*I
Got:
    -3.074972059 + 1.88269669262*I
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/dirichlet.py", line 688:
    sage: abs(e.gauss_sum_numerical())
Expected:
    3.60555127546399
Got:
    3.60555127546
**********************************************************************
1 items had failures:
   5 of  13 in __main__.example_23
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_dirichlet.py
	 [3.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/sage/sage/modular/dirichlet.py
Total time for all tests: 3.4 seconds
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t -long devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 3 doctests failed
sage -t -long devel/sage/sage/matrix/matrix_cyclo_dense.pyx 
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py", line 664:
    sage: (A[1,0]).abs()
Expected:
    12.9975436637560
Got:
    12.9975436638
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py", line 697:
    sage: A.height()
Expected:
    12.9975436637560
Got:
    12.9975436638
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_cyclo_dense.py", line 699:
    sage: (A[1,0]).abs()
Expected:
    12.9975436637560
Got:
    12.9975436638
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_20
   2 of   5 in __main__.example_21
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_matrix_cyclo_dense.py
	 [9.8 s]
exit code: 1024
```


Patch coming up.

Cheers,

Michael



---

archive/issue_comments_024889.json:
```json
{
    "body": "For the record (and so that I do not forget): I already have applied \n\n* sage-3533.patch\n* sage.3533a.patch\n* sage.3533b.patch\n* sage.3533c.patch\n\nto my Sage 3.0.4.alpha2 repo and am waiting for #3557 to be fixed and a review before applying the doctest fix patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T02:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record (and so that I do not forget): I already have applied 

* sage-3533.patch
* sage.3533a.patch
* sage.3533b.patch
* sage.3533c.patch

to my Sage 3.0.4.alpha2 repo and am waiting for #3557 to be fixed and a review before applying the doctest fix patch.

Cheers,

Michael



---

archive/issue_comments_024890.json:
```json
{
    "body": "cleaned up version of the previous diff.",
    "created_at": "2008-07-06T17:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

cleaned up version of the previous diff.



---

archive/issue_comments_024891.json:
```json
{
    "body": "Attachment [trac_3533_doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket3533/trac_3533_doctest_fixes.patch) by mabshoff created at 2008-07-06 17:49:29\n\nNote that in the last doctest fix patch I am removing\n\n```\ne.gauss_sum_numerical() \n```\n\nfrom dirichlet.py since it is numerically unstable and would require an ellipsis at the start of a line which is not allowed. We still test the absolute, so I think we are covered.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24891",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3533_doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket3533/trac_3533_doctest_fixes.patch) by mabshoff created at 2008-07-06 17:49:29

Note that in the last doctest fix patch I am removing

```
e.gauss_sum_numerical() 
```

from dirichlet.py since it is numerically unstable and would require an ellipsis at the start of a line which is not allowed. We still test the absolute, so I think we are covered.

Cheers,

Michael



---

archive/issue_comments_024892.json:
```json
{
    "body": "REVIEW:\n\n+1 to the numerical noise doctest fixes",
    "created_at": "2008-07-06T18:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24892",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

+1 to the numerical noise doctest fixes



---

archive/issue_events_008065.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-06T18:08:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3533#event-8065"
}
```



---

archive/issue_comments_024893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T18:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24893",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024894.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T18:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3533#issuecomment-24894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
