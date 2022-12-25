# Issue 7598: NumberField embedding slightly off

archive/issues_007598.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @burcin\n\n```\nsage: Q.<i> = NumberField(x^2+1)\nsage: complex(i)\n0.99999999999999967j\n```\n\nIt should give `1j` instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7598\n\n",
    "created_at": "2009-12-04T05:35:08Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "NumberField embedding slightly off",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7598",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @loefflerd

CC:  @burcin

```
sage: Q.<i> = NumberField(x^2+1)
sage: complex(i)
0.99999999999999967j
```

It should give `1j` instead.

Issue created by migration from https://trac.sagemath.org/ticket/7598





---

archive/issue_events_018051.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-04T05:35:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7598#event-18051"
}
```



---

archive/issue_comments_064692.json:
```json
{
    "body": "This is probably caused by the roots method using NumPy which uses Fortran which is a little off.  If you specify algorithm='pari' to the roots command when computing them, things should be fine.\n\n```\nsage: Q.<i> = NumberField(x^2+1)\nsage: Q.defining_polynomial().change_ring(CC).roots()[1][0].imag().exact_rational()\n9007199254740989/9007199254740992\nsage: Q.defining_polynomial().change_ring(ComplexField(100)).roots()[1][0].imag().exact_rational()\n1\n```\n\nNote that NumPy is not used for the second example.",
    "created_at": "2009-12-14T06:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64692",
    "user": "https://github.com/mwhansen"
}
```

This is probably caused by the roots method using NumPy which uses Fortran which is a little off.  If you specify algorithm='pari' to the roots command when computing them, things should be fine.

```
sage: Q.<i> = NumberField(x^2+1)
sage: Q.defining_polynomial().change_ring(CC).roots()[1][0].imag().exact_rational()
9007199254740989/9007199254740992
sage: Q.defining_polynomial().change_ring(ComplexField(100)).roots()[1][0].imag().exact_rational()
1
```

Note that NumPy is not used for the second example.



---

archive/issue_comments_064693.json:
```json
{
    "body": "Attachment [trac_7598-more_serious_version.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-more_serious_version.patch) by @williamstein created at 2009-12-14 10:33:39\n\ntrac_7598-more_serious_version.patch  -- this deals with the problems more at the root.  Unfortunately, there are doctests in this file that fail:\n\n```\n\tsage -t  devel/sage-main/sage/modular/dirichlet.py # 4 doctests failed\n```\nand I haven't had time to figure out what is wrong.  It probably has to do with a complex embedding not being defined automatically, whereas before it was...\n\nThe design of embeddings was really bad before and relied on numerical errors to mess up the order of roots in case of 53 bit precision.  This was potentially *very* buggy and was I think the result of some absolutely terrible design decisions.    This absolutely must be fixed before releasing sage-4.3.  This patch basically fixes it, modulo some small remaining issue.\n\nHere is an example from sage-4.2.1 that illustrates just how horrendously bad the previous design was (with using CDF when prec=53 but ComplexField(prec) otherwise):\n\n```\nsage: K.<i> = QuadraticField(-1)\nsage: i.complex_em\ni.complex_embedding   i.complex_embeddings  \nsage: i.complex_embedding()\n1.0*I\nsage: i.complex_embedding(100)\n-1.0000000000000000000000000000*I\n```",
    "created_at": "2009-12-14T10:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64693",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7598-more_serious_version.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-more_serious_version.patch) by @williamstein created at 2009-12-14 10:33:39

trac_7598-more_serious_version.patch  -- this deals with the problems more at the root.  Unfortunately, there are doctests in this file that fail:

```
	sage -t  devel/sage-main/sage/modular/dirichlet.py # 4 doctests failed
```
and I haven't had time to figure out what is wrong.  It probably has to do with a complex embedding not being defined automatically, whereas before it was...

The design of embeddings was really bad before and relied on numerical errors to mess up the order of roots in case of 53 bit precision.  This was potentially *very* buggy and was I think the result of some absolutely terrible design decisions.    This absolutely must be fixed before releasing sage-4.3.  This patch basically fixes it, modulo some small remaining issue.

Here is an example from sage-4.2.1 that illustrates just how horrendously bad the previous design was (with using CDF when prec=53 but ComplexField(prec) otherwise):

```
sage: K.<i> = QuadraticField(-1)
sage: i.complex_em
i.complex_embedding   i.complex_embeddings  
sage: i.complex_embedding()
1.0*I
sage: i.complex_embedding(100)
-1.0000000000000000000000000000*I
```



---

archive/issue_comments_064694.json:
```json
{
    "body": "I think the errors in dirichlet.py comes from the following:\n\n```\nsage: a = mod(1,3)\nsage: CDF.zeta(3)^a\n-0.5 + 0.866025403784*I\nsage: CC.zeta(3)^a\n---------------------------------------------------------------------------\nTraceback (most recent call last)\n...\nTypeError: unable to coerce <type 'sage.rings.complex_number.ComplexNumber'> to an integer\n```\n\nIt'd be nice if the {{{__pow__}} methods were standardized.",
    "created_at": "2009-12-14T13:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64694",
    "user": "https://github.com/mwhansen"
}
```

I think the errors in dirichlet.py comes from the following:

```
sage: a = mod(1,3)
sage: CDF.zeta(3)^a
-0.5 + 0.866025403784*I
sage: CC.zeta(3)^a
---------------------------------------------------------------------------
Traceback (most recent call last)
...
TypeError: unable to coerce <type 'sage.rings.complex_number.ComplexNumber'> to an integer
```

It'd be nice if the {{{__pow__}} methods were standardized.



---

archive/issue_comments_064695.json:
```json
{
    "body": "Attachment [trac_7598-dirichlet.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-dirichlet.patch) by @mwhansen created at 2009-12-15 03:16:42",
    "created_at": "2009-12-15T03:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64695",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7598-dirichlet.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-dirichlet.patch) by @mwhansen created at 2009-12-15 03:16:42



---

archive/issue_comments_064696.json:
```json
{
    "body": "I've added a patch which fixes the errors in dirichlet.py by just forcing the exponent to be an int.\n\nWilliam's changes look good to me so the only thing that needs review is trac_7598-dirichlet.patch.\n\nWe should open another ticket for the `__pow__` discrepencies.",
    "created_at": "2009-12-15T03:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64696",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch which fixes the errors in dirichlet.py by just forcing the exponent to be an int.

William's changes look good to me so the only thing that needs review is trac_7598-dirichlet.patch.

We should open another ticket for the `__pow__` discrepencies.



---

archive/issue_comments_064697.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-15T03:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64697",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064698.json:
```json
{
    "body": "Do we need to apply both patches?  Or is it that Mike has given a positive review to the first and only needs a review of the second?  I was hoping to test this (being someone who experienced the problems) but as it will take a long time to rebuild, I want to make sure that the time is not wasted.",
    "created_at": "2009-12-15T09:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64698",
    "user": "https://github.com/JohnCremona"
}
```

Do we need to apply both patches?  Or is it that Mike has given a positive review to the first and only needs a review of the second?  I was hoping to test this (being someone who experienced the problems) but as it will take a long time to rebuild, I want to make sure that the time is not wasted.



---

archive/issue_comments_064699.json:
```json
{
    "body": "You need to apply both patches.  I've given a positive review to the first.  The second is pretty easy since it makes the exponent an integer instead of an integermod.",
    "created_at": "2009-12-15T09:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64699",
    "user": "https://github.com/mwhansen"
}
```

You need to apply both patches.  I've given a positive review to the first.  The second is pretty easy since it makes the exponent an integer instead of an integermod.



---

archive/issue_comments_064700.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T11:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64700",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064701.json:
```json
{
    "body": "Running long doctests on a 32-bit Arch Linux machine gives one doctest failure related to this ticket:\n\n```\nsage -t -long \"devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst\"\n**********************************************************************\nFile \"/opt/sage-4.3.rc0/devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst\", line 109:\n    sage: K.complex_embeddings()\nExpected:\n    [\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Double Field\n      Defn: a |--> -0.629960524947 - 1.09112363597*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Double Field\n      Defn: a |--> -0.629960524947 + 1.09112363597*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Double Field\n      Defn: a |--> 1.25992104989\n    ]\nGot:\n    [\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Field with 53 bits of precision\n      Defn: a |--> -0.629960524947437 - 1.09112363597172*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Field with 53 bits of precision\n      Defn: a |--> -0.629960524947437 + 1.09112363597172*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Field with 53 bits of precision\n      Defn: a |--> 1.25992104989487\n    ]\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_nf_galois_groups.py\n\t [5.9 s]\nexit code: 1024\n``` \n\nApart from this small issue, everything looks good.",
    "created_at": "2009-12-15T11:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64701",
    "user": "https://github.com/aghitza"
}
```

Running long doctests on a 32-bit Arch Linux machine gives one doctest failure related to this ticket:

```
sage -t -long "devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst"
**********************************************************************
File "/opt/sage-4.3.rc0/devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst", line 109:
    sage: K.complex_embeddings()
Expected:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> -0.629960524947 - 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> -0.629960524947 + 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> 1.25992104989
    ]
Got:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 - 1.09112363597172*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 + 1.09112363597172*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> 1.25992104989487
    ]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_nf_galois_groups.py
	 [5.9 s]
exit code: 1024
``` 

Apart from this small issue, everything looks good.



---

archive/issue_comments_064702.json:
```json
{
    "body": "OK, I've added a trivial patch that fixes the last doctest failure.",
    "created_at": "2009-12-15T11:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64702",
    "user": "https://github.com/aghitza"
}
```

OK, I've added a trivial patch that fixes the last doctest failure.



---

archive/issue_comments_064703.json:
```json
{
    "body": "Attachment [trac_7598-nf_galois_groups.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-nf_galois_groups.patch) by @aghitza created at 2009-12-15 11:43:01\n\napply after the previous two patches",
    "created_at": "2009-12-15T11:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64703",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7598-nf_galois_groups.patch](tarball://root/attachments/some-uuid/ticket7598/trac_7598-nf_galois_groups.patch) by @aghitza created at 2009-12-15 11:43:01

apply after the previous two patches



---

archive/issue_comments_064704.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-15T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64704",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T14:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64705",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064706.json:
```json
{
    "body": "Applied all 3 patches to 4.3.rc0 on both 32-bit Suse (built using system gfortran) and 64-bit ubuntu (using Sage's gfortran).  No problems.  All tests in the files touched pass.  I still get a failure in doc/en/bordeaux_2008/nf_introduction.rst but that has a different cause.\n\nSo, positive review.",
    "created_at": "2009-12-15T14:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64706",
    "user": "https://github.com/JohnCremona"
}
```

Applied all 3 patches to 4.3.rc0 on both 32-bit Suse (built using system gfortran) and 64-bit ubuntu (using Sage's gfortran).  No problems.  All tests in the files touched pass.  I still get a failure in doc/en/bordeaux_2008/nf_introduction.rst but that has a different cause.

So, positive review.



---

archive/issue_comments_064707.json:
```json
{
    "body": "Excellent.  I'm glad we (you guys) tracked that down.  I'm not sure why I didn't think that the number field was just using the alternate embedding.",
    "created_at": "2009-12-15T14:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64707",
    "user": "https://github.com/mwhansen"
}
```

Excellent.  I'm glad we (you guys) tracked that down.  I'm not sure why I didn't think that the number field was just using the alternate embedding.



---

archive/issue_comments_064708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T15:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7598#issuecomment-64708",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018052.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T15:16:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7598#event-18052"
}
```



---

archive/issue_events_018053.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T17:15:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7598#event-18053"
}
```



---

archive/issue_events_018054.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T17:15:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7598",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7598#event-18054"
}
```
