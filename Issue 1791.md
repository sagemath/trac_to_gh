# Issue 1791: Sage 2.10.alpha3: numerical noise doctest failure with gcc 4.2.2/x86

archive/issues_001791.json:
```json
{
    "body": "Assignee: failure\n\nAs reported by Kate in https://groups.google.com/group/sage-devel/t/1cd682b8f3e49748\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/\npolynomial_element.pyx\n**********************************************************************\nFile \"polynomial_element.pyx\", line 2549:\n    sage: f.roots(multiplicities=False)\nExpected:\n    [...1.00000000000000...*I, 1.00000000000000...*I]\nGot:\n    [1.00000000000000 + 1.11022302462516e-16*I, 1.12045416424138e-16 +\n1.00000000000000*I] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1791\n\n",
    "created_at": "2008-01-16T01:42:28Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "Sage 2.10.alpha3: numerical noise doctest failure with gcc 4.2.2/x86",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

As reported by Kate in https://groups.google.com/group/sage-devel/t/1cd682b8f3e49748

```
sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx
**********************************************************************
File "polynomial_element.pyx", line 2549:
    sage: f.roots(multiplicities=False)
Expected:
    [...1.00000000000000...*I, 1.00000000000000...*I]
Got:
    [1.00000000000000 + 1.11022302462516e-16*I, 1.12045416424138e-16 +
1.00000000000000*I] 
```


Issue created by migration from https://trac.sagemath.org/ticket/1791





---

archive/issue_comments_011307.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T03:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1791#issuecomment-11307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha4



---

archive/issue_comments_011308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T03:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1791#issuecomment-11308",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
