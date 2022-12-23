# Issue 4394: Sage 3.1.4: magma related optional doctest failure in sage/rings/polynomial/polynomial_element.pyx

archive/issues_004394.json:
```json
{
    "body": "Assignee: was\n\n\n```\nmabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\nsage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/polynomial_element.py\", line 2833:\n    sage: g = magma(f); g              # optional -- requires Magma\nExpected:\n    y^3 - 17*y + 5\nGot:\n    $.1^3 - 17*$.1 + 5\n**********************************************************************\n1 items had failures:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4394\n\n",
    "created_at": "2008-10-30T16:51:51Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/rings/polynomial/polynomial_element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4394",
    "user": "mabshoff"
}
```
Assignee: was


```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/polynomial_element.py", line 2833:
    sage: g = magma(f); g              # optional -- requires Magma
Expected:
    y^3 - 17*y + 5
Got:
    $.1^3 - 17*$.1 + 5
**********************************************************************
1 items had failures:
```


Issue created by migration from https://trac.sagemath.org/ticket/4394





---

archive/issue_comments_032340.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-30T20:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32340",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_032341.json:
```json
{
    "body": "Positive review. The patch makes the doctests pass:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ \n./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\nsage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx\n\t [11.4 s]\n \n----------------------------------------------------------------------\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T20:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32341",
    "user": "mabshoff"
}
```

Positive review. The patch makes the doctests pass:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ 
./sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
sage -t -long -optional devel/sage/sage/rings/polynomial/polynomial_element.pyx
	 [11.4 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael



---

archive/issue_comments_032342.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T20:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32342",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T20:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4394#issuecomment-32343",
    "user": "mabshoff"
}
```

Resolution: fixed
