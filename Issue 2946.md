# Issue 2946: bug in jordan_form

archive/issues_002946.json:
```json
{
    "body": "Assignee: was\n\nKeywords: jordan_form, matrix\n\nMatrices with 0 eigenvalues crash jordan_form.  1x1 matrices do not seem affected, so the simplest example is:\n\n\n```\nj1 = matrix(ZZ,2,2,[[0,0],[0,0]])\nj1.jordan_form()\n```\n\n\nThe following code might be of some use in testing this; the function tough_nut(n) produces a highly degenerate nilpotent n by n matrix:\n\n\n```\ndef uprand(i,j, max_i = 1):\n    if i > j: return 0\n    if i == j: return 1\n    return Integer(randint(0,max_i))\ndef superd(i,j, odds = .75):\n    if j - i == 1: \n        temp = random()\n        if temp < odds: return 1\n        else: return 0\n    return 0\ndef tough_nut(m_size, odds = .75):\n    t1 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])\n    t2 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])\n    t2 = t2.transpose()\n    pre_j = matrix(ZZ,m_size,m_size,[[superd(i,j, odds = odds) for j in range(m_size)] for i in range(m_size)])\n    mystery_mat = t1*t2*pre_j*t2.inverse()*t1.inverse()\n    return mystery_mat\n```\n\n\nAt first I thought this was only caused by nilpotents, but it affects many matrices with a zero eigenvalue.  Maybe it is more pervasive than that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2946\n\n",
    "created_at": "2008-04-17T21:27:33Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "title": "bug in jordan_form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2946",
    "user": "mhampton"
}
```
Assignee: was

Keywords: jordan_form, matrix

Matrices with 0 eigenvalues crash jordan_form.  1x1 matrices do not seem affected, so the simplest example is:


```
j1 = matrix(ZZ,2,2,[[0,0],[0,0]])
j1.jordan_form()
```


The following code might be of some use in testing this; the function tough_nut(n) produces a highly degenerate nilpotent n by n matrix:


```
def uprand(i,j, max_i = 1):
    if i > j: return 0
    if i == j: return 1
    return Integer(randint(0,max_i))
def superd(i,j, odds = .75):
    if j - i == 1: 
        temp = random()
        if temp < odds: return 1
        else: return 0
    return 0
def tough_nut(m_size, odds = .75):
    t1 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])
    t2 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])
    t2 = t2.transpose()
    pre_j = matrix(ZZ,m_size,m_size,[[superd(i,j, odds = odds) for j in range(m_size)] for i in range(m_size)])
    mystery_mat = t1*t2*pre_j*t2.inverse()*t1.inverse()
    return mystery_mat
```


At first I thought this was only caused by nilpotents, but it affects many matrices with a zero eigenvalue.  Maybe it is more pervasive than that.

Issue created by migration from https://trac.sagemath.org/ticket/2946





---

archive/issue_comments_020312.json:
```json
{
    "body": "The current `jordan_form` computes the number of Jordan blocks of size 1 at eigenvalue x of a matrix A as `rank(A) - rank(A - x)`. This should be `dim(ker(A-x)) = size(A) - rank(A - x)`.\n\nThe attached patch fixes this.",
    "created_at": "2008-04-17T21:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20312",
    "user": "wjp"
}
```

The current `jordan_form` computes the number of Jordan blocks of size 1 at eigenvalue x of a matrix A as `rank(A) - rank(A - x)`. This should be `dim(ker(A-x)) = size(A) - rank(A - x)`.

The attached patch fixes this.



---

archive/issue_comments_020313.json:
```json
{
    "body": "Attachment [noninvertible_jordan_form.patch](tarball://root/attachments/some-uuid/ticket2946/noninvertible_jordan_form.patch) by wjp created at 2008-04-17 21:51:31",
    "created_at": "2008-04-17T21:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20313",
    "user": "wjp"
}
```

Attachment [noninvertible_jordan_form.patch](tarball://root/attachments/some-uuid/ticket2946/noninvertible_jordan_form.patch) by wjp created at 2008-04-17 21:51:31



---

archive/issue_comments_020314.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-18T00:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20314",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_020315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T06:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20315",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020316.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-18T06:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20316",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020317.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-18T06:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20317",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020318.json:
```json
{
    "body": "There are rejection problems [with or without #2947 applied]:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch\npatching file sage/matrix/constructor.py\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch\npatching file sage/matrix/matrix2.pyx\nHunk #1 succeeded at 3591 (offset 59 lines).\nHunk #2 FAILED at 3601.\nHunk #3 FAILED at 3630.\n2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T06:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20318",
    "user": "mabshoff"
}
```

There are rejection problems [with or without #2947 applied]:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch
patching file sage/matrix/constructor.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 succeeded at 3591 (offset 59 lines).
Hunk #2 FAILED at 3601.
Hunk #3 FAILED at 3630.
2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
```

Cheers,

Michael



---

archive/issue_comments_020319.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-18T06:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20319",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_020320.json:
```json
{
    "body": "Attachment [2946.patch](tarball://root/attachments/some-uuid/ticket2946/2946.patch) by mhansen created at 2008-04-18 06:29:39",
    "created_at": "2008-04-18T06:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20320",
    "user": "mhansen"
}
```

Attachment [2946.patch](tarball://root/attachments/some-uuid/ticket2946/2946.patch) by mhansen created at 2008-04-18 06:29:39



---

archive/issue_comments_020321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T06:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20321",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020322.json:
```json
{
    "body": "Merged 2946.patch in Sage 3.0.alpha6",
    "created_at": "2008-04-18T06:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20322",
    "user": "mabshoff"
}
```

Merged 2946.patch in Sage 3.0.alpha6



---

archive/issue_comments_020323.json:
```json
{
    "body": "Thanks for catching and fixing this!  Sorry I forgot about poor ol' zero as an eigenvalue when I wrote the original code and doctests; my bad.",
    "created_at": "2008-04-18T11:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2946#issuecomment-20323",
    "user": "jason"
}
```

Thanks for catching and fixing this!  Sorry I forgot about poor ol' zero as an eigenvalue when I wrote the original code and doctests; my bad.
