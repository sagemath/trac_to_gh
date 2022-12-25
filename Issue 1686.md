# Issue 1686: arpack -- illegal instruction when built on Pentium 4 using gfortran

archive/issues_001686.json:
```json
{
    "body": "Assignee: jkantor\n\nThe file\n\n```\nSAGE_ROOT/devel/sage/sage/numerical/tests.py\n```\n\n\ncontains this doctest:\n\n\n```\nsage: from scipy import sparse\nsage: import arpack\n\n#Test arpack\n#This matrix is the finite difference approximation to\n# the eigenvalue problem\n#d^2f/dx^2=\\lambda f, on [0,\\pi], which boundary values 0\n# The lowest eigenvalue calulated should be close to 1\nsage: import scipy\nsage: n=scipy.zeros((3,500))\nsage: n[0,:]=-1\nsage: n[1,:]=2\nsage: n[2,:]=-1\nsage: A=sparse.spdiags(n,[-1,0,1],int(500),int(500))\nsage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')\nsage: e[0]*float(501/pi)**2\n0.999............\n```\n\n\nThe line \n\n```\nsage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')\n```\n\ncrashes on at least one Pentium 4 machine with Sage built using gfortran.\n\nIf any sage developers replicate this on their personal hardware, please\nemail sage-devel.  We have removed the above doctest until this gets fixed. \n(See attached patch.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1686\n\n",
    "created_at": "2008-01-04T23:54:22Z",
    "labels": [
        "component: numerical",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "arpack -- illegal instruction when built on Pentium 4 using gfortran",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1686",
    "user": "https://github.com/williamstein"
}
```
Assignee: jkantor

The file

```
SAGE_ROOT/devel/sage/sage/numerical/tests.py
```


contains this doctest:


```
sage: from scipy import sparse
sage: import arpack

#Test arpack
#This matrix is the finite difference approximation to
# the eigenvalue problem
#d^2f/dx^2=\lambda f, on [0,\pi], which boundary values 0
# The lowest eigenvalue calulated should be close to 1
sage: import scipy
sage: n=scipy.zeros((3,500))
sage: n[0,:]=-1
sage: n[1,:]=2
sage: n[2,:]=-1
sage: A=sparse.spdiags(n,[-1,0,1],int(500),int(500))
sage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')
sage: e[0]*float(501/pi)**2
0.999............
```


The line 

```
sage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')
```

crashes on at least one Pentium 4 machine with Sage built using gfortran.

If any sage developers replicate this on their personal hardware, please
email sage-devel.  We have removed the above doctest until this gets fixed. 
(See attached patch.)

Issue created by migration from https://trac.sagemath.org/ticket/1686





---

archive/issue_comments_010685.json:
```json
{
    "body": "Attachment [trac-1686-disable.patch](tarball://root/attachments/some-uuid/ticket1686/trac-1686-disable.patch) by mabshoff created at 2008-01-05 00:13:47\n\npatch by William to disable the doctest for now",
    "created_at": "2008-01-05T00:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-1686-disable.patch](tarball://root/attachments/some-uuid/ticket1686/trac-1686-disable.patch) by mabshoff created at 2008-01-05 00:13:47

patch by William to disable the doctest for now



---

archive/issue_comments_010686.json:
```json
{
    "body": "I merged trac-1686-disable.patch into Sage 2.9.2.rc1 - but this ticket will remain open for now until we find a real solution.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-05T00:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10686",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I merged trac-1686-disable.patch into Sage 2.9.2.rc1 - but this ticket will remain open for now until we find a real solution.

Cheers,

Michael



---

archive/issue_comments_010687.json:
```json
{
    "body": "Changing assignee from jkantor to mabshoff.",
    "created_at": "2008-07-16T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from jkantor to mabshoff.



---

archive/issue_comments_010688.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-16T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010689.json:
```json
{
    "body": "My assumption is that #2303 fixed this issue, too. So we should apply the reverse of the doctest patch and close this ticket.\n\nThere is no actual patch to review yet, just consider the reversing of the above doctest patch.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10689",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

My assumption is that #2303 fixed this issue, too. So we should apply the reverse of the doctest patch and close this ticket.

There is no actual patch to review yet, just consider the reversing of the above doctest patch.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_010690.json:
```json
{
    "body": "Verbal positive review by William. I applied the reverse of the above patch and committed.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T05:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Verbal positive review by William. I applied the reverse of the above patch and committed.

Cheers,

Michael



---

archive/issue_comments_010691.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T05:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_010692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T05:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1686#issuecomment-10692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
