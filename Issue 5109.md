# Issue 5109: add support for Bell polynomials in Sage

archive/issues_005109.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5109\n\n",
    "created_at": "2009-01-27T00:14:11Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "add support for Bell polynomials in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5109",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/5109





---

archive/issue_comments_039030.json:
```json
{
    "body": "Attachment [trac_5109.patch](tarball://root/attachments/some-uuid/ticket5109/trac_5109.patch) by mhansen created at 2009-01-27 01:18:03",
    "created_at": "2009-01-27T01:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39030",
    "user": "mhansen"
}
```

Attachment [trac_5109.patch](tarball://root/attachments/some-uuid/ticket5109/trac_5109.patch) by mhansen created at 2009-01-27 01:18:03



---

archive/issue_comments_039031.json:
```json
{
    "body": "This applies cleanly to 3.3.alpha2 and passes sage -t. The examples also agree with some examples given on http://en.wikipedia.org/wiki/Bell_polynomials, as well as this agreement: \n\n\n```\nsage: stirling_number2(6,2) == bell_polynomial(6,2)(1,1,1,1,1) \nTrue\nsage: stirling_number2(6,4) == bell_polynomial(6,4)(1,1,1) \nTrue\nsage: stirling_number2(7,4) == bell_polynomial(7,4)(1,1,1,1) \nTrue\n```\n\n\n\nI ran sage -testall and got this failure:\n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/toy_d_basis.py\"  \n**********************************************************************\nFile \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.3.alpha2/devel/sage/sage/rings/polynomial/toy_d_basis.py\", line 91:\n    sage: d_basis(I)\nExpected:\n    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]\nGot:\n    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]\n**********************************************************************\n```\n\nThough I don't know what a d_basis is, I think it is an unrelated failure\nso I'm giving this a positive review.",
    "created_at": "2009-01-27T12:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39031",
    "user": "wdj"
}
```

This applies cleanly to 3.3.alpha2 and passes sage -t. The examples also agree with some examples given on http://en.wikipedia.org/wiki/Bell_polynomials, as well as this agreement: 


```
sage: stirling_number2(6,2) == bell_polynomial(6,2)(1,1,1,1,1) 
True
sage: stirling_number2(6,4) == bell_polynomial(6,4)(1,1,1) 
True
sage: stirling_number2(7,4) == bell_polynomial(7,4)(1,1,1,1) 
True
```



I ran sage -testall and got this failure:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  
**********************************************************************
File "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.3.alpha2/devel/sage/sage/rings/polynomial/toy_d_basis.py", line 91:
    sage: d_basis(I)
Expected:
    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]
Got:
    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]
**********************************************************************
```

Though I don't know what a d_basis is, I think it is an unrelated failure
so I'm giving this a positive review.



---

archive/issue_comments_039032.json:
```json
{
    "body": "One more test (also positive):\n\n\n```\nsage: n=6\nsage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) \nTrue\nsage: n = 7\nsage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) \nTrue\nsage: n = 8\nsage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) \nTrue\nsage: n = 20\nsage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) \nTrue\nsage: bell_number(n)\n51724158235372\n```\n\nReturns these pretty fast too!",
    "created_at": "2009-01-27T12:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39032",
    "user": "wdj"
}
```

One more test (also positive):


```
sage: n=6
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 7
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 8
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 20
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: bell_number(n)
51724158235372
```

Returns these pretty fast too!



---

archive/issue_comments_039033.json:
```json
{
    "body": "Note that partial credit goes to Blair - see \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/4ae02fd827f68eed#\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T12:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39033",
    "user": "mabshoff"
}
```

Note that partial credit goes to Blair - see 

http://groups.google.com/group/sage-devel/browse_thread/thread/4ae02fd827f68eed#

Cheers,

Michael



---

archive/issue_comments_039034.json:
```json
{
    "body": "Yep, I did the patch in his name.",
    "created_at": "2009-01-28T12:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39034",
    "user": "mhansen"
}
```

Yep, I did the patch in his name.



---

archive/issue_comments_039035.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-28T12:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39035",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039036.json:
```json
{
    "body": "I got Blair's \"real name\" from the hg commit message, but I pinged him to see if he wants to be credited with that name or not.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T12:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39036",
    "user": "mabshoff"
}
```

I got Blair's "real name" from the hg commit message, but I pinged him to see if he wants to be credited with that name or not.

Cheers,

Michael



---

archive/issue_comments_039037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39037",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039038.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5109#issuecomment-39038",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
