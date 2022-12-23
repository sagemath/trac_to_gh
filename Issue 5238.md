# Issue 5238: remove qsieve.spkg and replace it by mpQS (part of FLINT)

archive/issues_005238.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis ought to be doable in the 3.4 release once the ReST patches are in:\n\n```\nFLINT ships with a much improved version of qsieve. It is now called mpQS.\n\nIf you do make mpQS in the main directory of  FLINT (make all also\nbuilds it) it will build a program which replaces the old qsieve.\nHowever this program will deal with much smaller integers, and is much\nfaster overall.\n\nIt should have far fewer issues than the old code.\n\nIt also handles numbers with small factors, but still won't handle\nintegers which are perfect powers or primes. These should be scanned\nfor before running mpQS.\n\nThe new program actually uses FLINT for some parts of the computation,\nso it cannot be built standalone (it doesn't link against libflint, it\njust includes the files it needs). I have just verified this program\nstill builds (and works) on sage.math.\n\nBill.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5238\n\n",
    "created_at": "2009-02-11T23:20:59Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "remove qsieve.spkg and replace it by mpQS (part of FLINT)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5238",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This ought to be doable in the 3.4 release once the ReST patches are in:

```
FLINT ships with a much improved version of qsieve. It is now called mpQS.

If you do make mpQS in the main directory of  FLINT (make all also
builds it) it will build a program which replaces the old qsieve.
However this program will deal with much smaller integers, and is much
faster overall.

It should have far fewer issues than the old code.

It also handles numbers with small factors, but still won't handle
integers which are perfect powers or primes. These should be scanned
for before running mpQS.

The new program actually uses FLINT for some parts of the computation,
so it cannot be built standalone (it doesn't link against libflint, it
just includes the files it needs). I have just verified this program
still builds (and works) on sage.math.

Bill.
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5238





---

archive/issue_comments_040135.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5238#issuecomment-40135",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040136.json:
```json
{
    "body": "Close as fixed:\n\n\n```\n[mvngu@sage flint-1.5.0.p4]$ pwd\n/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/flint-1.5.0.p4\n[mvngu@sage flint-1.5.0.p4]$ find src/ | grep 'mpQS'\nsrc/QS/mpQS.h\nsrc/QS/mpQS.c\n[mvngu@sage flint-1.5.0.p4]$ find src/ | grep 'qsieve'\n<no-output>\n```\n",
    "created_at": "2010-06-16T02:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5238#issuecomment-40136",
    "user": "mvngu"
}
```

Close as fixed:


```
[mvngu@sage flint-1.5.0.p4]$ pwd
/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/flint-1.5.0.p4
[mvngu@sage flint-1.5.0.p4]$ find src/ | grep 'mpQS'
src/QS/mpQS.h
src/QS/mpQS.c
[mvngu@sage flint-1.5.0.p4]$ find src/ | grep 'qsieve'
<no-output>
```




---

archive/issue_comments_040137.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-16T02:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5238#issuecomment-40137",
    "user": "mvngu"
}
```

Resolution: fixed
