# Issue 5027: doctest failure for rings/polynomial/toy_d_basis.py

archive/issues_005027.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: groebner, toy, toy_d_basis\n\nI get this failure on an intel mac:\n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/toy_d_basis.py\"\n**********************************************************************\nFile \".../devel/sage/sage/rings/polynomial/toy_d_basis.py\", line 91:\n    sage: d_basis(I)\nExpected:\n    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]\nGot:\n    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]\n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5027\n\n",
    "created_at": "2009-01-19T16:13:02Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "doctest failure for rings/polynomial/toy_d_basis.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5027",
    "user": "mhampton"
}
```
Assignee: tbd

Keywords: groebner, toy, toy_d_basis

I get this failure on an intel mac:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"
**********************************************************************
File ".../devel/sage/sage/rings/polynomial/toy_d_basis.py", line 91:
    sage: d_basis(I)
Expected:
    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]
Got:
    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/5027





---

archive/issue_comments_038294.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38294",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038295.json:
```json
{
    "body": "After chatting with malb we decided to dot out the constant since it is the same GBasis.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38295",
    "user": "mabshoff"
}
```

After chatting with malb we decided to dot out the constant since it is the same GBasis.

Cheers,

Michael



---

archive/issue_comments_038296.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38296",
    "user": "mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_038297.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-05T13:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38297",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_038298.json:
```json
{
    "body": "After applying the patch:\n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/toy_d_basis.py\"  \n\t [9.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 9.5 seconds\n[jaap@paix sage-3.3.alpha4]$ \n\n```\n\n\nOn fedora 9, 32 bits.\n\nJaap",
    "created_at": "2009-02-05T15:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38298",
    "user": "jsp"
}
```

After applying the patch:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  
	 [9.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.5 seconds
[jaap@paix sage-3.3.alpha4]$ 

```


On fedora 9, 32 bits.

Jaap



---

archive/issue_comments_038299.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T23:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38299",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_038300.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T23:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38300",
    "user": "mabshoff"
}
```

Resolution: fixed
