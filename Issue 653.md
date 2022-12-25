# Issue 653: Need LLL-optimize from pari

archive/issues_000653.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt would be good to port polredabs() from pari--this runs LLL to find a \"small\" generator of a field.\n\nFrom gp:\n\n? ?polredabs\npolredabs(x,{flag=0}): a smallest generating polynomial of the number field for \nthe T2 norm on the roots, with smallest index for the minimal T2 norm. flag is \noptional, whose binary digit mean 1: give the element whose characteristic \npolynomial is the given polynomial. 4: give all polynomials of minimal T2 norm \n(give only one of P(x) and P(-x)). 16: partial reduction.\n\n(Of course, this is part of the larger project of bringing the number fields up to speed...)\n\nIssue created by migration from https://trac.sagemath.org/ticket/653\n\n",
    "created_at": "2007-09-14T04:28:55Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "Need LLL-optimize from pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/653",
    "user": "https://github.com/jvoight"
}
```
Assignee: @williamstein

It would be good to port polredabs() from pari--this runs LLL to find a "small" generator of a field.

From gp:

? ?polredabs
polredabs(x,{flag=0}): a smallest generating polynomial of the number field for 
the T2 norm on the roots, with smallest index for the minimal T2 norm. flag is 
optional, whose binary digit mean 1: give the element whose characteristic 
polynomial is the given polynomial. 4: give all polynomials of minimal T2 norm 
(give only one of P(x) and P(-x)). 16: partial reduction.

(Of course, this is part of the larger project of bringing the number fields up to speed...)

Issue created by migration from https://trac.sagemath.org/ticket/653





---

archive/issue_comments_003386.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-14T04:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/653#issuecomment-3386",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003387.json:
```json
{
    "body": "I believe this issue has been fixed, but there is also malb's new LLL wrapper code.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T14:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/653#issuecomment-3387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I believe this issue has been fixed, but there is also malb's new LLL wrapper code.

Cheers,

Michael



---

archive/issue_comments_003388.json:
```json
{
    "body": "polredabs() is in.\n\nHopefully we don't have to re-implement every computer algebra algorithm that uses LLL, just because we have a fast LLL now.  If so, that should be a separate ticket. :)",
    "created_at": "2007-10-26T05:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/653#issuecomment-3388",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

polredabs() is in.

Hopefully we don't have to re-implement every computer algebra algorithm that uses LLL, just because we have a fast LLL now.  If so, that should be a separate ticket. :)



---

archive/issue_comments_003389.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-26T05:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/653#issuecomment-3389",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
