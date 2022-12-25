# Issue 4733: matrix exponential for general matrices

archive/issues_004733.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis adds a generic matrix exponential (convert to SR matrix; use maxima, or use scipy if RDF/CDF matrix)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4733\n\n",
    "created_at": "2008-12-06T23:35:17Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "matrix exponential for general matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4733",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

This adds a generic matrix exponential (convert to SR matrix; use maxima, or use scipy if RDF/CDF matrix)



Issue created by migration from https://trac.sagemath.org/ticket/4733





---

archive/issue_comments_035651.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-12-06T23:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35651",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035652.json:
```json
{
    "body": "Attachment [matrix-exp.patch](tarball://root/attachments/some-uuid/ticket4733/matrix-exp.patch) by @jasongrout created at 2008-12-06 23:36:03",
    "created_at": "2008-12-06T23:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35652",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matrix-exp.patch](tarball://root/attachments/some-uuid/ticket4733/matrix-exp.patch) by @jasongrout created at 2008-12-06 23:36:03



---

archive/issue_comments_035653.json:
```json
{
    "body": "depends on #4493",
    "created_at": "2008-12-06T23:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35653",
    "user": "https://github.com/jasongrout"
}
```

depends on #4493



---

archive/issue_comments_035654.json:
```json
{
    "body": "This takes care of #2273 (sorry, I didn't find that one before opening this one).",
    "created_at": "2008-12-07T04:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35654",
    "user": "https://github.com/jasongrout"
}
```

This takes care of #2273 (sorry, I didn't find that one before opening this one).



---

archive/issue_comments_035655.json:
```json
{
    "body": "For my teaching, this is a very useful addition. However, the following behavior seems odd. Maybe it is a quirk and not a bug. Still, I'd like someone to comment on it before reviewing this further. \n\n(It is based on the facts that exp(A) commutes with A\nand the derivative of exp(At) equals Aexp(At)=exp(At)A.)\n\n```\nsage: t = var('t')                 \nsage: A = matrix([[1,2],[3,4]])\nsage: B = (t*A).exp()\nsage: Bprime = matrix(map(diff,B.list()))\nsage: B(1)*A == Bprime(1)\nFalse                    \nsage: B(1)*A == A*B(1)\nFalse                 \nsage: B*A == A*B\nFalse           \nsage: MS = MatrixSpace(RR,2,2)\nsage: MS(A*B(1)) == MS(Bprime(1))\nFalse\nsage: MS(A*B(1)); MS(Bprime(1))\n\n[276.178649899715 402.884170665423]\n[604.326255998134 880.504905897849]\n\n[276.178649899715 402.884170665423]\n[604.326255998134 880.504905897849]\nsage: MS(A*B(-1)); MS(Bprime(-1))\n\n[-0.405192443954626  0.196757133983140]\n[ 0.295135700974710 -0.110056742979916]\n\n[-0.405192443954626  0.196757133983140]\n[ 0.295135700974710 -0.110056742979916]\nsage: MS(A*B(-1)); MS(B(-1)*A)\n\n[-0.405192443954626  0.196757133983140]\n[ 0.295135700974710 -0.110056742979916]\n\n[-0.405192443954626  0.196757133983140]\n[ 0.295135700974711 -0.110056742979916]\nsage:\n```",
    "created_at": "2008-12-07T13:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35655",
    "user": "https://github.com/wdjoyner"
}
```

For my teaching, this is a very useful addition. However, the following behavior seems odd. Maybe it is a quirk and not a bug. Still, I'd like someone to comment on it before reviewing this further. 

(It is based on the facts that exp(A) commutes with A
and the derivative of exp(At) equals Aexp(At)=exp(At)A.)

```
sage: t = var('t')                 
sage: A = matrix([[1,2],[3,4]])
sage: B = (t*A).exp()
sage: Bprime = matrix(map(diff,B.list()))
sage: B(1)*A == Bprime(1)
False                    
sage: B(1)*A == A*B(1)
False                 
sage: B*A == A*B
False           
sage: MS = MatrixSpace(RR,2,2)
sage: MS(A*B(1)) == MS(Bprime(1))
False
sage: MS(A*B(1)); MS(Bprime(1))

[276.178649899715 402.884170665423]
[604.326255998134 880.504905897849]

[276.178649899715 402.884170665423]
[604.326255998134 880.504905897849]
sage: MS(A*B(-1)); MS(Bprime(-1))

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]
sage: MS(A*B(-1)); MS(B(-1)*A)

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]

[-0.405192443954626  0.196757133983140]
[ 0.295135700974711 -0.110056742979916]
sage:
```



---

archive/issue_comments_035656.json:
```json
{
    "body": "Sorry, I only had a minute to look at your code...What exactly is odd?",
    "created_at": "2008-12-12T21:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35656",
    "user": "https://github.com/jasongrout"
}
```

Sorry, I only had a minute to look at your code...What exactly is odd?



---

archive/issue_comments_035657.json:
```json
{
    "body": "I think I see what you were saying:\n\n```\nsage: t = var('t')     \nsage: A = matrix([[1,2],[3,4]])\nsage: B = (t*A).exp()\nsage: Bprime = matrix(map(diff,B.list())) # This is wrong...\nsage: Bprime.nrows()\n1\nsage: Bprime = B.apply_map(diff) # This is right (and with 3.2.2, we could just do diff(B,x) :).\nsage: Bprime.nrows()\n2\nsage: B(1)*A == Bprime(1)\nFalse\nsage: B(1)*A == A*B(1)\nFalse\nsage: n(B(1)*A - A*B(1)) # Close to zero, should be equal to zero\n[   0.000000000000000 1.42108547152020e-14]\n[5.68434188608080e-14    0.000000000000000]\nsage: n(B(1)*A - Bprime(1)) # Close to zero, should be equal to zero\n\n[ 2.13162820728030e-14 -1.27897692436818e-13]\n[-4.26325641456060e-14  2.84217094304040e-14]\n```\n\nEverything is all right, though.  \"==\" returning false just means that Sage can't prove that they are equal.  Let's simplify instead:\n\n```\nsage: (B(1)*A - A*B(1)).apply_map(lambda e: e.full_simplify())\n\n[0 0]\n[0 0]\nsage: (B(1)*A - Bprime(1)).apply_map(lambda e: e.full_simplify())\n\n[0 0]\n[0 0]\n```\n\nDoes that ease your mind?  Can you review this patch now?",
    "created_at": "2008-12-12T21:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35657",
    "user": "https://github.com/jasongrout"
}
```

I think I see what you were saying:

```
sage: t = var('t')     
sage: A = matrix([[1,2],[3,4]])
sage: B = (t*A).exp()
sage: Bprime = matrix(map(diff,B.list())) # This is wrong...
sage: Bprime.nrows()
1
sage: Bprime = B.apply_map(diff) # This is right (and with 3.2.2, we could just do diff(B,x) :).
sage: Bprime.nrows()
2
sage: B(1)*A == Bprime(1)
False
sage: B(1)*A == A*B(1)
False
sage: n(B(1)*A - A*B(1)) # Close to zero, should be equal to zero
[   0.000000000000000 1.42108547152020e-14]
[5.68434188608080e-14    0.000000000000000]
sage: n(B(1)*A - Bprime(1)) # Close to zero, should be equal to zero

[ 2.13162820728030e-14 -1.27897692436818e-13]
[-4.26325641456060e-14  2.84217094304040e-14]
```

Everything is all right, though.  "==" returning false just means that Sage can't prove that they are equal.  Let's simplify instead:

```
sage: (B(1)*A - A*B(1)).apply_map(lambda e: e.full_simplify())

[0 0]
[0 0]
sage: (B(1)*A - Bprime(1)).apply_map(lambda e: e.full_simplify())

[0 0]
[0 0]
```

Does that ease your mind?  Can you review this patch now?



---

archive/issue_comments_035658.json:
```json
{
    "body": "Yes, thanks. I just wanted to make sure that wasn't a problem.\n\nApplies cleanly and passes sage -t on both modules it modifies. Looks good to me.",
    "created_at": "2008-12-12T23:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35658",
    "user": "https://github.com/wdjoyner"
}
```

Yes, thanks. I just wanted to make sure that wasn't a problem.

Applies cleanly and passes sage -t on both modules it modifies. Looks good to me.



---

archive/issue_comments_035659.json:
```json
{
    "body": "This patch does not compile for me:\n\n```\npython2.5 `which cython` --embed-positions --incref-local-binop \n-I/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main \n-o sage/matrix/matrix_mod2_dense.c sage/matrix/matrix_mod2_dense.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        a = t.transpose()\n        right_mat = right_mat* s.transpose()\n\n    return left_mat, a, right_mat\n    \n    def exp(self):\n   ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main/\nsage/matrix/matrix2.pyx:4914:4: def statement not allowed here\nParallel build failed with status 256.\nsage: There was an error installing modified sage library code.\n```\nNote that it applied with huge, i.e. 337 line, offset. This patch probably needs a rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T02:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch does not compile for me:

```
python2.5 `which cython` --embed-positions --incref-local-binop 
-I/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main 
-o sage/matrix/matrix_mod2_dense.c sage/matrix/matrix_mod2_dense.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        a = t.transpose()
        right_mat = right_mat* s.transpose()

    return left_mat, a, right_mat
    
    def exp(self):
   ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main/
sage/matrix/matrix2.pyx:4914:4: def statement not allowed here
Parallel build failed with status 256.
sage: There was an error installing modified sage library code.
```
Note that it applied with huge, i.e. 337 line, offset. This patch probably needs a rebase.

Cheers,

Michael



---

archive/issue_comments_035660.json:
```json
{
    "body": "trivial rebase to 3.3.alpha0",
    "created_at": "2009-01-22T01:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35660",
    "user": "https://github.com/aghitza"
}
```

trivial rebase to 3.3.alpha0



---

archive/issue_comments_035661.json:
```json
{
    "body": "Attachment [trac_4733.patch](tarball://root/attachments/some-uuid/ticket4733/trac_4733.patch) by @aghitza created at 2009-01-22 06:18:04",
    "created_at": "2009-01-22T06:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35661",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4733.patch](tarball://root/attachments/some-uuid/ticket4733/trac_4733.patch) by @aghitza created at 2009-01-22 06:18:04



---

archive/issue_events_010813.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T07:30:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4733#event-10813"
}
```



---

archive/issue_events_010814.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T07:30:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4733#event-10814"
}
```



---

archive/issue_comments_035662.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T07:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_035663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T07:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4733#issuecomment-35663",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
