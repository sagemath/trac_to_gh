# Issue 723: Make Sage's LLL faster: Magma seems to totally blow Sage (i.e., NTL) away for large-ish problems.

archive/issues_000723.json:
```json
{
    "body": "Assignee: was\n\nMagma's LLL is... way way way faster than the one in LLL.  E.g., (this requires patch #325)\n\n```\nsage: a = random_matrix(ZZ,200)\nsage: time b=a.lll()\nCPU times: user 8.74 s, sys: 0.08 s, total: 8.83 s\nWall time: 8.85\n\nsage: m = magma(a)\nsage: time c=m.LLL()\nWall time: 1.02\n\nsage: a = random_matrix(ZZ,400)\nsage: time b=a.lll()\nCPU times: user 202.89 s, sys: 1.54 s, total: 204.44 s\nWall time: 206.16\nsage: time c=magma(a)\nCPU times: user 0.24 s, sys: 0.02 s, total: 0.26 s\nWall time: 0.38\nsage: time d=c.LLL()\nWall time: 13.23\n\n\n```\n\n\nIt would also be good to benchmark PARI's LLL and compare.\nMake sure to use the 1 option, so it knows the matrix is integral:\n\n\n```\nsage: a = random_matrix(ZZ,100)\nsage: time b=a.lll()\nCPU times: user 0.53 s, sys: 0.00 s, total: 0.53 s\nWall time: 0.53\nsage: c = pari(a)\nsage: time d=c.qflll(1)\nCPU times: user 0.47 s, sys: 0.00 s, total: 0.47 s\nWall time: 0.47\nsage: a = random_matrix(ZZ,200)\nsage: time b=a.lll()\nCPU times: user 9.02 s, sys: 0.06 s, total: 9.08 s\nWall time: 9.14\nsage: c = pari(a)\nsage: time d=c.qflll(1)\nCPU times: user 9.88 s, sys: 0.05 s, total: 9.93 s\nWall time: 9.95\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/723\n\n",
    "created_at": "2007-09-20T23:28:12Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "Make Sage's LLL faster: Magma seems to totally blow Sage (i.e., NTL) away for large-ish problems.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/723",
    "user": "was"
}
```
Assignee: was

Magma's LLL is... way way way faster than the one in LLL.  E.g., (this requires patch #325)

```
sage: a = random_matrix(ZZ,200)
sage: time b=a.lll()
CPU times: user 8.74 s, sys: 0.08 s, total: 8.83 s
Wall time: 8.85

sage: m = magma(a)
sage: time c=m.LLL()
Wall time: 1.02

sage: a = random_matrix(ZZ,400)
sage: time b=a.lll()
CPU times: user 202.89 s, sys: 1.54 s, total: 204.44 s
Wall time: 206.16
sage: time c=magma(a)
CPU times: user 0.24 s, sys: 0.02 s, total: 0.26 s
Wall time: 0.38
sage: time d=c.LLL()
Wall time: 13.23


```


It would also be good to benchmark PARI's LLL and compare.
Make sure to use the 1 option, so it knows the matrix is integral:


```
sage: a = random_matrix(ZZ,100)
sage: time b=a.lll()
CPU times: user 0.53 s, sys: 0.00 s, total: 0.53 s
Wall time: 0.53
sage: c = pari(a)
sage: time d=c.qflll(1)
CPU times: user 0.47 s, sys: 0.00 s, total: 0.47 s
Wall time: 0.47
sage: a = random_matrix(ZZ,200)
sage: time b=a.lll()
CPU times: user 9.02 s, sys: 0.06 s, total: 9.08 s
Wall time: 9.14
sage: c = pari(a)
sage: time d=c.qflll(1)
CPU times: user 9.88 s, sys: 0.05 s, total: 9.93 s
Wall time: 9.95
```


Issue created by migration from https://trac.sagemath.org/ticket/723





---

archive/issue_comments_004211.json:
```json
{
    "body": "David Kohel had by far the most interesting response on sage-devel to this ticket:\n\n```\nDavid Kohel <drkohel@gmail.com> \t\t hide details\t 6:00 am (6 hours ago) \n\treply-to\t\tsage-devel@googlegroups.com\t \n\tto\t\tsage-devel <sage-devel@googlegroups.com>\t \n\tdate\t\tSep 21, 2007 6:00 AM\t \n\tsubject\t\t[sage-devel] Re: LLL\t \n\tmailed-by\t\tgooglegroups.com\t \n\nSince LLL and LLLGram in Magma V2.13 are written by Damien Stehle,\nusing his asymptotically better algorithm.  The previous version was\nnot\neven mathematically correct (adhoc \"improvements\" or post-processing\ncould destroy the LLL reduction condition).\n\nDamien provides C code under GPL and can be found on his web page:\n\nhttp://perso.ens-lyon.fr/damien.stehle/english.html\n\nIt might take some art to decide on optimal parameters, but linking it\ninto\nSAGE should provide the same asymptotic performance as in Magma.\n\n--David\n- Show quoted text -\n```\n",
    "created_at": "2007-09-21T19:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4211",
    "user": "was"
}
```

David Kohel had by far the most interesting response on sage-devel to this ticket:

```
David Kohel <drkohel@gmail.com> 		 hide details	 6:00 am (6 hours ago) 
	reply-to		sage-devel@googlegroups.com	 
	to		sage-devel <sage-devel@googlegroups.com>	 
	date		Sep 21, 2007 6:00 AM	 
	subject		[sage-devel] Re: LLL	 
	mailed-by		googlegroups.com	 

Since LLL and LLLGram in Magma V2.13 are written by Damien Stehle,
using his asymptotically better algorithm.  The previous version was
not
even mathematically correct (adhoc "improvements" or post-processing
could destroy the LLL reduction condition).

Damien provides C code under GPL and can be found on his web page:

http://perso.ens-lyon.fr/damien.stehle/english.html

It might take some art to decide on optimal parameters, but linking it
into
SAGE should provide the same asymptotic performance as in Magma.

--David
- Show quoted text -
```




---

archive/issue_comments_004212.json:
```json
{
    "body": "The attached patch exposes NTL's floating point LLL implementations which are significantly faster than the exact one. However, these are approximates only.",
    "created_at": "2007-09-21T23:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4212",
    "user": "malb"
}
```

The attached patch exposes NTL's floating point LLL implementations which are significantly faster than the exact one. However, these are approximates only.



---

archive/issue_comments_004213.json:
```json
{
    "body": "Attachment [ntls-fp-lll.patch](tarball://root/attachments/some-uuid/ticket723/ntls-fp-lll.patch) by malb created at 2007-09-21 23:33:59",
    "created_at": "2007-09-21T23:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4213",
    "user": "malb"
}
```

Attachment [ntls-fp-lll.patch](tarball://root/attachments/some-uuid/ticket723/ntls-fp-lll.patch) by malb created at 2007-09-21 23:33:59



---

archive/issue_comments_004214.json:
```json
{
    "body": "after patch:\n\ndouble precision vs. MAGMA:\n\n\n```\nsage: a = random_matrix(ZZ,200)\nsage: time b=a.LLL(algorithm=\"NTL:LLL_FP\")\nTime: CPU 0.91 s, Wall: 0.93 s\n\nsage: m = magma(a)\nsage: time c=m.LLL()\nWall: 1.33 s\n\nsage: a = random_matrix(ZZ,400)\nsage: time b=a.LLL(algorithm=\"NTL:LLL_FP\")\nTime: CPU 6.75 s, Wall: 6.94 s\n\nsage: c=magma(a)\nsage: time d=c.LLL()\nWall: 20.41 s\n```\n\n\nquad float precision vs. MAGMA:\n\n\n```\nsage: a = random_matrix(ZZ,200)\nsage: time b=a.LLL(algorithm=\"NTL:LLL_QP\")\nTime: CPU 2.56 s, Wall: 2.60 s\n\nsage: m = magma(a)\nsage: time c=m.LLL()\nWall: 1.34 s\n\nsage: a = random_matrix(ZZ,400)\nsage: time b=a.LLL(algorithm=\"NTL:LLL_QP\")\nTime: CPU 31.36 s, Wall: 32.00 s\n\nsage: c=magma(a)\nsage: time d=c.LLL()\nWall: 20.13 s\n```\n\n\nHowever:\n\n\n```\nsage: B = MatrixSpace(IntegerRing(), 50, 51)(0\nsage: for i in range(50): B[i,0] = ZZ.random_element(2**10000)\nsage: for i in range(50): B[i,i+1] = 1;  \n\nsage: B.LLL(algorithm=\"NTL:LLL_FP\")\nLLL_FP: numbers too big...use LLL_XD\n...\n<type 'exceptions.RuntimeError'>\n\nsage: time B.LLL(algorithm=\"NTL:LLL_XD\")\n50 x 51 dense matrix over Integer Ring\nCPU time: 43.55 s,  Wall time: 44.73 s\n\nsage: M = magma(B)\nsage: time C = M.LLL()\nWall: 15.53 s\n```\n",
    "created_at": "2007-09-21T23:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4214",
    "user": "malb"
}
```

after patch:

double precision vs. MAGMA:


```
sage: a = random_matrix(ZZ,200)
sage: time b=a.LLL(algorithm="NTL:LLL_FP")
Time: CPU 0.91 s, Wall: 0.93 s

sage: m = magma(a)
sage: time c=m.LLL()
Wall: 1.33 s

sage: a = random_matrix(ZZ,400)
sage: time b=a.LLL(algorithm="NTL:LLL_FP")
Time: CPU 6.75 s, Wall: 6.94 s

sage: c=magma(a)
sage: time d=c.LLL()
Wall: 20.41 s
```


quad float precision vs. MAGMA:


```
sage: a = random_matrix(ZZ,200)
sage: time b=a.LLL(algorithm="NTL:LLL_QP")
Time: CPU 2.56 s, Wall: 2.60 s

sage: m = magma(a)
sage: time c=m.LLL()
Wall: 1.34 s

sage: a = random_matrix(ZZ,400)
sage: time b=a.LLL(algorithm="NTL:LLL_QP")
Time: CPU 31.36 s, Wall: 32.00 s

sage: c=magma(a)
sage: time d=c.LLL()
Wall: 20.13 s
```


However:


```
sage: B = MatrixSpace(IntegerRing(), 50, 51)(0
sage: for i in range(50): B[i,0] = ZZ.random_element(2**10000)
sage: for i in range(50): B[i,i+1] = 1;  

sage: B.LLL(algorithm="NTL:LLL_FP")
LLL_FP: numbers too big...use LLL_XD
...
<type 'exceptions.RuntimeError'>

sage: time B.LLL(algorithm="NTL:LLL_XD")
50 x 51 dense matrix over Integer Ring
CPU time: 43.55 s,  Wall time: 44.73 s

sage: M = magma(B)
sage: time C = M.LLL()
Wall: 15.53 s
```




---

archive/issue_comments_004215.json:
```json
{
    "body": "fpLLL as mentioned above is patched into SAGE by the patch found at\n\n  http://sage.math.washington.edu/home/malb/fplll.patch\n\n. Using this code, we can achieve a quite good performance.\n\n\n```\nsage:  = MatrixSpace(IntegerRing(), 50, 51)(0)\nsage: for i in range(50): B[i,0] = ZZ.random_element(2**10000)\n....:\nsage: for i in range(50): B[i,i+1] = 1\n....:\nsage: time C = B.LLL('fpLLL:fast')\nCPU times: user 9.54 s, sys: 0.00 s, total: 9.54 s\nWall time: 9.56\n\nsage: C.is_LLL_reduced()\nTrue\n\nsage: BM = B._magma_()\nsage: time CM = BM.LLL()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 15.20\n\nsage: time magma.eval(\"CM := LLL(%s:Fast:=1)\"%BM.name())\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 11.68\n```\n",
    "created_at": "2007-10-02T02:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4215",
    "user": "malb"
}
```

fpLLL as mentioned above is patched into SAGE by the patch found at

  http://sage.math.washington.edu/home/malb/fplll.patch

. Using this code, we can achieve a quite good performance.


```
sage:  = MatrixSpace(IntegerRing(), 50, 51)(0)
sage: for i in range(50): B[i,0] = ZZ.random_element(2**10000)
....:
sage: for i in range(50): B[i,i+1] = 1
....:
sage: time C = B.LLL('fpLLL:fast')
CPU times: user 9.54 s, sys: 0.00 s, total: 9.54 s
Wall time: 9.56

sage: C.is_LLL_reduced()
True

sage: BM = B._magma_()
sage: time CM = BM.LLL()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 15.20

sage: time magma.eval("CM := LLL(%s:Fast:=1)"%BM.name())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 11.68
```




---

archive/issue_comments_004216.json:
```json
{
    "body": "This patch has fplll.c, which is Cython autogenerated code.  Please make a clean new patch that doesn't\nhave fplll.c or any other autogenerated code in it.",
    "created_at": "2007-10-19T01:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4216",
    "user": "was"
}
```

This patch has fplll.c, which is Cython autogenerated code.  Please make a clean new patch that doesn't
have fplll.c or any other autogenerated code in it.



---

archive/issue_comments_004217.json:
```json
{
    "body": "I *have* applied ntls-fp-lll.patch.  The patch that isn't clean is \n   http://sage.math.washington.edu/home/malb/fplll.patch",
    "created_at": "2007-10-19T01:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4217",
    "user": "was"
}
```

I *have* applied ntls-fp-lll.patch.  The patch that isn't clean is 
   http://sage.math.washington.edu/home/malb/fplll.patch



---

archive/issue_comments_004218.json:
```json
{
    "body": "The Damien part has been moved to ticket 929.",
    "created_at": "2007-10-19T17:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4218",
    "user": "was"
}
```

The Damien part has been moved to ticket 929.



---

archive/issue_comments_004219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T17:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/723#issuecomment-4219",
    "user": "was"
}
```

Resolution: fixed
