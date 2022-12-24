# Issue 162: Integer.exact_log causes segfault

archive/issues_000162.json:
```json
{
    "body": "Assignee: somebody\n\nThis code (which I noticed in `Integer.exact_log`) causes a segfault:\n\n\n```\nsage: x = 3**10000000\nsage: bits = 31699256\nsage: R = RealField(bits)\nsage: y = x._mpfr_(R)\nsage: z = y.log()\n```\n\n\nI haven't investigated the underlying cause.\n\nIssue created by migration from https://trac.sagemath.org/ticket/162\n\n",
    "created_at": "2006-10-29T21:56:58Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Integer.exact_log causes segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/162",
    "user": "dmharvey"
}
```
Assignee: somebody

This code (which I noticed in `Integer.exact_log`) causes a segfault:


```
sage: x = 3**10000000
sage: bits = 31699256
sage: R = RealField(bits)
sage: y = x._mpfr_(R)
sage: z = y.log()
```


I haven't investigated the underlying cause.

Issue created by migration from https://trac.sagemath.org/ticket/162





---

archive/issue_comments_000721.json:
```json
{
    "body": "It's mpfr (=gmp) running out of memory.   I don't know how or if it is\npossible to resolve this -- they might make assumptions in those libraries\nthat preclude us dealing with the problem.  These things were much worse\nwith GMP-4.0, by the way...",
    "created_at": "2006-11-06T07:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/162#issuecomment-721",
    "user": "@williamstein"
}
```

It's mpfr (=gmp) running out of memory.   I don't know how or if it is
possible to resolve this -- they might make assumptions in those libraries
that preclude us dealing with the problem.  These things were much worse
with GMP-4.0, by the way...



---

archive/issue_comments_000722.json:
```json
{
    "body": "Looking again, it's basically just that GMP doesn't work with ridiculously\nlarge precisions -- it just dies. \n\nInteresting, MAGMA seg faults on exactly the same sort of computation, and of course MAGMA uses GMP/MPFR behind the scenes:\n\n\n```\nwas@sage:~$ magma\nMagma V2.13-5     Fri Jan 12 2007 17:05:25 on sage     [Seed = 853493552]\nType ? for help.  Type <Ctrl>-D to quit.\n> x := 3**10000000;\n\n>> x := 3**10000000;\n         ^\nUser error: bad syntax\n> x := 3^10000000; \n> R := RealField(31699256);\n> y := R!x;\n> time z=Log(y);\n\n>> time z=Log(y);\n        ^\nUser error: Identifier 'z' has not been declared or assigned\n> time z:=Log(y);\nSegmentation fault\n```\n",
    "created_at": "2007-01-13T01:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/162#issuecomment-722",
    "user": "@williamstein"
}
```

Looking again, it's basically just that GMP doesn't work with ridiculously
large precisions -- it just dies. 

Interesting, MAGMA seg faults on exactly the same sort of computation, and of course MAGMA uses GMP/MPFR behind the scenes:


```
was@sage:~$ magma
Magma V2.13-5     Fri Jan 12 2007 17:05:25 on sage     [Seed = 853493552]
Type ? for help.  Type <Ctrl>-D to quit.
> x := 3**10000000;

>> x := 3**10000000;
         ^
User error: bad syntax
> x := 3^10000000; 
> R := RealField(31699256);
> y := R!x;
> time z=Log(y);

>> time z=Log(y);
        ^
User error: Identifier 'z' has not been declared or assigned
> time z:=Log(y);
Segmentation fault
```




---

archive/issue_comments_000723.json:
```json
{
    "body": "This is a basic mpfr problem.  Any super-high precision arithmetic breaks with SAGE or Magma:\n\n```\nwas@ubuntu:~$ magma\nMagma V2.13-10    Thu Aug 16 2007 02:54:37 on ubuntu   [Seed = 3360329821]\nType ? for help.  Type <Ctrl>-D to quit.\n> R := RealField(31699256);\n> y := R!3;\n> z := y*y;\nSegmentation fault\nwas@ubuntu:~$    \n\nSame on 64-bit:\n\nwas@sage:~$ magma\nMagma V2.13-5     Thu Aug 16 2007 02:56:05 on sage     [Seed = 4101418455]\nType ? for help.  Type <Ctrl>-D to quit.\n> R := RealField(31699256);\n> y := R!3;\n> z := y*y;\nSegmentation fault\nwas@sage:~$   \n```\n\n\nProposed solution -- in SAGE, don't allow construction of RealField(n) for\nn > 2^23.",
    "created_at": "2007-08-16T10:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/162#issuecomment-723",
    "user": "@williamstein"
}
```

This is a basic mpfr problem.  Any super-high precision arithmetic breaks with SAGE or Magma:

```
was@ubuntu:~$ magma
Magma V2.13-10    Thu Aug 16 2007 02:54:37 on ubuntu   [Seed = 3360329821]
Type ? for help.  Type <Ctrl>-D to quit.
> R := RealField(31699256);
> y := R!3;
> z := y*y;
Segmentation fault
was@ubuntu:~$    

Same on 64-bit:

was@sage:~$ magma
Magma V2.13-5     Thu Aug 16 2007 02:56:05 on sage     [Seed = 4101418455]
Type ? for help.  Type <Ctrl>-D to quit.
> R := RealField(31699256);
> y := R!3;
> z := y*y;
Segmentation fault
was@sage:~$   
```


Proposed solution -- in SAGE, don't allow construction of RealField(n) for
n > 2^23.



---

archive/issue_comments_000724.json:
```json
{
    "body": "Attachment [5762.patch](tarball://root/attachments/some-uuid/ticket162/5762.patch) by @williamstein created at 2007-08-16 10:23:27\n\nfix",
    "created_at": "2007-08-16T10:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/162#issuecomment-724",
    "user": "@williamstein"
}
```

Attachment [5762.patch](tarball://root/attachments/some-uuid/ticket162/5762.patch) by @williamstein created at 2007-08-16 10:23:27

fix



---

archive/issue_comments_000725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-16T10:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/162#issuecomment-725",
    "user": "@williamstein"
}
```

Resolution: fixed
