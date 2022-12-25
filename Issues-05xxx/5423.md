# Issue 5423: [with patch, needs work] Move calculus to new coercion model

archive/issues_005423.json:
```json
{
    "body": "Assignee: @robertwb\n\nI went through and included all of the changes that Robert made in the symbolics branch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5423\n\n",
    "closed_at": "2009-05-18T22:01:44Z",
    "created_at": "2009-03-03T09:23:07Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] Move calculus to new coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5423",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

I went through and included all of the changes that Robert made in the symbolics branch.

Issue created by migration from https://trac.sagemath.org/ticket/5423





---

archive/issue_comments_041888.json:
```json
{
    "body": "Attachment [5423-coerce-calc.patch](tarball://root/attachments/some-uuid/ticket5423/5423-coerce-calc.patch) by @robertwb created at 2009-03-03 22:10:43",
    "created_at": "2009-03-03T22:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41888",
    "user": "https://github.com/robertwb"
}
```

Attachment [5423-coerce-calc.patch](tarball://root/attachments/some-uuid/ticket5423/5423-coerce-calc.patch) by @robertwb created at 2009-03-03 22:10:43



---

archive/issue_comments_041889.json:
```json
{
    "body": "Attachment [trac_5423.patch](tarball://root/attachments/some-uuid/ticket5423/trac_5423.patch) by @mwhansen created at 2009-03-07 22:01:31",
    "created_at": "2009-03-07T22:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41889",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5423.patch](tarball://root/attachments/some-uuid/ticket5423/trac_5423.patch) by @mwhansen created at 2009-03-07 22:01:31



---

archive/issue_comments_041890.json:
```json
{
    "body": "I've uploaded trac_5423.patch which is the original patch rebased against 3.4.rc1.",
    "created_at": "2009-03-07T22:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41890",
    "user": "https://github.com/mwhansen"
}
```

I've uploaded trac_5423.patch which is the original patch rebased against 3.4.rc1.



---

archive/issue_comments_041891.json:
```json
{
    "body": "mhansen: did you review trac_5423.patch while you did the rebase?",
    "created_at": "2009-03-24T21:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41891",
    "user": "https://github.com/jasongrout"
}
```

mhansen: did you review trac_5423.patch while you did the rebase?



---

archive/issue_comments_041892.json:
```json
{
    "body": "The following doctests fail after applying the rebased patch:\n\n```\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/misc/citation.pyx\", line 56:\n    sage: get_systems('integrate(x^2, x)')\nExpected:\n    ['Maxima']\nGot:\n    ['MPFI', 'MPFR', 'Maxima']\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_0\n***Test Failed*** 1 failures.\n```\n\nand\n\n```\nsage -t  devel/sage/sage/rings/complex_interval.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/rings/complex_interval.pyx\", line 456:\n    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[3]>\", line 1, in <module>\n        sage_input(ComplexIntervalField(Integer(64))(Integer(2))**I, preparse=False, verify=True)###line 456:\n    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)\n      File \"complex_interval.pyx\", line 432, in sage.rings.complex_interval.ComplexIntervalFieldElement.__pow__ (sage/rings/complex_interval.c:6298)\n        return (self.log() * right).exp()\n      File \"element.pyx\", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)\n      File \"coerce.pyx\", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7168)\n    TypeError: unsupported operand parent(s) for '*': 'Complex Interval Field with 64 bits of precision' and 'Symbolic Ring'\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_14\n```\n\nOtherwise, this looks very good. \n\nThe above is against sage-3.4.1.rc2.",
    "created_at": "2009-04-12T05:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41892",
    "user": "https://github.com/williamstein"
}
```

The following doctests fail after applying the rebased patch:

```
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/misc/citation.pyx", line 56:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['Maxima']
Got:
    ['MPFI', 'MPFR', 'Maxima']
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0
***Test Failed*** 1 failures.
```

and

```
sage -t  devel/sage/sage/rings/complex_interval.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/rings/complex_interval.pyx", line 456:
    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[3]>", line 1, in <module>
        sage_input(ComplexIntervalField(Integer(64))(Integer(2))**I, preparse=False, verify=True)###line 456:
    sage: sage_input(ComplexIntervalField(64)(2)^I, preparse=False, verify=True)
      File "complex_interval.pyx", line 432, in sage.rings.complex_interval.ComplexIntervalFieldElement.__pow__ (sage/rings/complex_interval.c:6298)
        return (self.log() * right).exp()
      File "element.pyx", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)
      File "coerce.pyx", line 740, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7168)
    TypeError: unsupported operand parent(s) for '*': 'Complex Interval Field with 64 bits of precision' and 'Symbolic Ring'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_14
```

Otherwise, this looks very good. 

The above is against sage-3.4.1.rc2.



---

archive/issue_comments_041893.json:
```json
{
    "body": "Made obsolete by the Pynac switch.",
    "created_at": "2009-05-18T21:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41893",
    "user": "https://github.com/robertwb"
}
```

Made obsolete by the Pynac switch.



---

archive/issue_events_012638.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-18T22:01:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5423#event-12638"
}
```



---

archive/issue_comments_041894.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-05-18T22:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5423#issuecomment-41894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_012639.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-18T22:01:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5423",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5423#event-12639"
}
```
