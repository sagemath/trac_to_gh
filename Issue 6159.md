# Issue 6159: Implement real_part for CDF and CC

archive/issues_006159.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: CC(I).real_part()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()\n\nAttributeError: 'sage.rings.complex_number.ComplexNumber' object has no attribute 'real_part'\n\n\nsage: CDF(I).real_part()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()\n\nAttributeError: 'sage.rings.complex_double.ComplexDoubleElement' object has no attribute 'real_part'\n```\n\n\nbut \n\n\n```\nsage: (3+I).real_part()\n3\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6159\n\n",
    "created_at": "2009-05-30T15:46:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Implement real_part for CDF and CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6159",
    "user": "jason"
}
```
Assignee: somebody


```
sage: CC(I).real_part()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.complex_number.ComplexNumber' object has no attribute 'real_part'


sage: CDF(I).real_part()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jason/.sage/temp/littleone/9440/_home_jason__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.complex_double.ComplexDoubleElement' object has no attribute 'real_part'
```


but 


```
sage: (3+I).real_part()
3

```


Issue created by migration from https://trac.sagemath.org/ticket/6159





---

archive/issue_comments_049132.json:
```json
{
    "body": "Done in the attached patch.  I even threw in imag_part() for free.",
    "created_at": "2009-07-13T14:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49132",
    "user": "AlexGhitza"
}
```

Done in the attached patch.  I even threw in imag_part() for free.



---

archive/issue_comments_049133.json:
```json
{
    "body": "Attachment [trac_6159.patch](tarball://root/attachments/some-uuid/ticket6159/trac_6159.patch) by AlexGhitza created at 2009-07-13 14:03:15",
    "created_at": "2009-07-13T14:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49133",
    "user": "AlexGhitza"
}
```

Attachment [trac_6159.patch](tarball://root/attachments/some-uuid/ticket6159/trac_6159.patch) by AlexGhitza created at 2009-07-13 14:03:15



---

archive/issue_comments_049134.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-13T14:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49134",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049135.json:
```json
{
    "body": "Changing assignee from somebody to AlexGhitza.",
    "created_at": "2009-07-13T14:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49135",
    "user": "AlexGhitza"
}
```

Changing assignee from somebody to AlexGhitza.



---

archive/issue_comments_049136.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-07-17T14:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49136",
    "user": "burcin"
}
```

Looks good.



---

archive/issue_comments_049137.json:
```json
{
    "body": "After a first merge of the patch `trac_6159.patch` and running full doctests on the Sage library, I got this failure:\n\n```\nsage -t -long devel/sage-exp/sage/modules/vector_double_dense.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/modules/vector_double_dense.pyx\", line 656:\n    sage: v.stats_kurtosis()\nExpected:\n    -1.23\nGot:\n    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?\n    -1.23\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_29\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_vector_double_dense.py\n\t [2.6 s]\n```\n\nI then unmerged that patch, and all doctests passed. As another attempt, I merged `trac_6159.patch` a second time, ran all doctests in the Sage library, and they passed.",
    "created_at": "2009-07-18T13:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49137",
    "user": "mvngu"
}
```

After a first merge of the patch `trac_6159.patch` and running full doctests on the Sage library, I got this failure:

```
sage -t -long devel/sage-exp/sage/modules/vector_double_dense.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/modules/vector_double_dense.pyx", line 656:
    sage: v.stats_kurtosis()
Expected:
    -1.23
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    -1.23
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_29
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_vector_double_dense.py
	 [2.6 s]
```

I then unmerged that patch, and all doctests passed. As another attempt, I merged `trac_6159.patch` a second time, ran all doctests in the Sage library, and they passed.



---

archive/issue_comments_049138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T13:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6159#issuecomment-49138",
    "user": "mvngu"
}
```

Resolution: fixed
