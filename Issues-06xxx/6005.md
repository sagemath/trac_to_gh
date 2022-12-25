# Issue 6005: real and imaginary parts for quadratic number fields

archive/issues_006005.json:
```json
{
    "body": "Assignee: @loefflerd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6005\n\n",
    "closed_at": "2010-07-29T06:12:14Z",
    "created_at": "2009-05-07T21:22:29Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "real and imaginary parts for quadratic number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6005",
    "user": "https://github.com/robertwb"
}
```
Assignee: @loefflerd



Issue created by migration from https://trac.sagemath.org/ticket/6005





---

archive/issue_comments_047682.json:
```json
{
    "body": "Attachment [6005-qnf-real-imag.patch](tarball://root/attachments/some-uuid/ticket6005/6005-qnf-real-imag.patch) by @williamstein created at 2009-05-07 23:33:25\n\n```\nsage: K.<i> = QuadraticField(-1) \nsage: i.imag()\n1\n```\n\nThe above is hundreds of times slower than i.real().  That needs to be fixed.\n\nit's because of this line\n\n```",
    "created_at": "2009-05-07T23:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47682",
    "user": "https://github.com/williamstein"
}
```

Attachment [6005-qnf-real-imag.patch](tarball://root/attachments/some-uuid/ticket6005/6005-qnf-real-imag.patch) by @williamstein created at 2009-05-07 23:33:25

```
sage: K.<i> = QuadraticField(-1) 
sage: i.imag()
1
```

The above is hundreds of times slower than i.real().  That needs to be fixed.

it's because of this line

```



---

archive/issue_comments_047683.json:
```json
{
    "body": "Attachment [6005-qnf-real-imag-fix.patch](tarball://root/attachments/some-uuid/ticket6005/6005-qnf-real-imag-fix.patch) by @robertwb created at 2009-05-07 23:55:01",
    "created_at": "2009-05-07T23:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47683",
    "user": "https://github.com/robertwb"
}
```

Attachment [6005-qnf-real-imag-fix.patch](tarball://root/attachments/some-uuid/ticket6005/6005-qnf-real-imag-fix.patch) by @robertwb created at 2009-05-07 23:55:01



---

archive/issue_comments_047684.json:
```json
{
    "body": "Now \n\n```\nsage: K.<i> = QuadraticField(-1)\nsage: timeit(\"i.imag()\")\n625 loops, best of 3: 9.73 \u00b5s per loop\n```",
    "created_at": "2009-05-07T23:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47684",
    "user": "https://github.com/robertwb"
}
```

Now 

```
sage: K.<i> = QuadraticField(-1)
sage: timeit("i.imag()")
625 loops, best of 3: 9.73 µs per loop
```



---

archive/issue_comments_047685.json:
```json
{
    "body": "The two patches cause doctest failures in one file:\n\n```\nsage -t -long \"devel/sage/sage/rings/number_field/number_field.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/number_field/number_field.py\", line 5512:\n    sage: F, F_into_L, _ = L.subfields(2)[0]; F  \nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_124[42]>\", line 1, in <module>\n        F, F_into_L, _ = L.subfields(Integer(2))[Integer(0)]; F###line 5512:\n    sage: F, F_into_L, _ = L.subfields(2)[0]; F  \n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4676, in subfields\n        both_maps=True, optimize=False)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4733, in _subfields_helper\n        K = NumberField(f, names=name + str(i), embedding=embedding)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 423, in NumberField\n        K = NumberField_quadratic(polynomial, name, check, embedding)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 6852, in __init__\n        self._standard_embedding = RDF(rootD) > 0\n      File \"parent.pyx\", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4121)\n      File \"coerce_maps.pyx\", line 81, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3064)\n      File \"coerce_maps.pyx\", line 76, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2955)\n      File \"real_double.pyx\", line 525, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5668)\n    TypeError: float() argument must be a string or a number\n**********************************************************************\n<SNIP>\n```\n\nCheers,\n\nMichaep",
    "created_at": "2009-05-12T16:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The two patches cause doctest failures in one file:

```
sage -t -long "devel/sage/sage/rings/number_field/number_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 5512:
    sage: F, F_into_L, _ = L.subfields(2)[0]; F  
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_124[42]>", line 1, in <module>
        F, F_into_L, _ = L.subfields(Integer(2))[Integer(0)]; F###line 5512:
    sage: F, F_into_L, _ = L.subfields(2)[0]; F  
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4676, in subfields
        both_maps=True, optimize=False)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4733, in _subfields_helper
        K = NumberField(f, names=name + str(i), embedding=embedding)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 423, in NumberField
        K = NumberField_quadratic(polynomial, name, check, embedding)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 6852, in __init__
        self._standard_embedding = RDF(rootD) > 0
      File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4121)
      File "coerce_maps.pyx", line 81, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3064)
      File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2955)
      File "real_double.pyx", line 525, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5668)
    TypeError: float() argument must be a string or a number
**********************************************************************
<SNIP>
```

Cheers,

Michaep



---

archive/issue_comments_047686.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47686",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_047687.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47687",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_events_014107.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-07-29T06:12:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6005#event-14107"
}
```



---

archive/issue_comments_047688.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-29T06:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47688",
    "user": "https://github.com/robertwb"
}
```

Resolution: duplicate



---

archive/issue_comments_047689.json:
```json
{
    "body": "This was merged in as part of #5930. \n\nIt was folded into one of those patches: http://hg.sagemath.org/sage-main/diff/d7533ae4895e/sage/rings/number_field/number_field_element_quadratic.pyx",
    "created_at": "2010-07-29T06:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6005#issuecomment-47689",
    "user": "https://github.com/robertwb"
}
```

This was merged in as part of #5930. 

It was folded into one of those patches: http://hg.sagemath.org/sage-main/diff/d7533ae4895e/sage/rings/number_field/number_field_element_quadratic.pyx



---

archive/issue_events_014108.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-07-29T06:12:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6005",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6005#event-14108"
}
```
