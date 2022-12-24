# Issue 1215: Sage misparses maxima integration result

archive/issues_001215.json:
```json
{
    "body": "Assignee: was\n\nLordRuslanNightmare reported:\n\n```\n> As far as i know, length of curve, defined as\n> f(x)\n> from a to b (a <= x <= b) is\n> L = integral from a to b of sqrt(1 + df(x)^2)dx\n> where df(x) is diff(f,x)\n> \n> for f(x) = y = x^2 , a=0, b=2 it should be\n> df(x)=2x\n> sqrt(17) + ln|4 + sqrt(17)|/4\n> \n> which is 4.647\n> \n> however, SAGE thinks differently. For this code:\n> \n> y = x^2\n> dy = diff(y,x)\n> z = integral(sqrt(1 + dy^2), x, 0, 2)\n> print(z)\n> print(RR(z))\n> \n> output is\n> \n>                                  4 sqrt(17) + 4\n>                                  --------------\n>                                        4\n> 5.12310562561766\n> \n> Am i doing something wrong?\n\nNo. Maxima gives\n\n(%i2) integrate (sqrt(1+4*x^2), x, 0, 2);\n                             asinh(4) + 4 sqrt(17)\n(%o2)                        ---------------------\n                                       4\n\nso possibly SAGE is not parsing that properly? That's the only thing I can think\nof. The following just confirms your computation:\n\nsage: sqrt(1 + (2*x)^2).nintegrate(x, 0, 2)\n(4.6467837624329427, 1.5663635326179329e-09, 21, 0)\nsage: integral(sqrt(1 + (2*x)^2), x, 0, 2)\n(4 + 4*sqrt(17))/4\nsage: RR(integral(sqrt(1 + (2*x)^2), x, 0, 2))\n5.12310562561766\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1215\n\n",
    "created_at": "2007-11-20T13:45:56Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "Sage misparses maxima integration result",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1215",
    "user": "mabshoff"
}
```
Assignee: was

LordRuslanNightmare reported:

```
> As far as i know, length of curve, defined as
> f(x)
> from a to b (a <= x <= b) is
> L = integral from a to b of sqrt(1 + df(x)^2)dx
> where df(x) is diff(f,x)
> 
> for f(x) = y = x^2 , a=0, b=2 it should be
> df(x)=2x
> sqrt(17) + ln|4 + sqrt(17)|/4
> 
> which is 4.647
> 
> however, SAGE thinks differently. For this code:
> 
> y = x^2
> dy = diff(y,x)
> z = integral(sqrt(1 + dy^2), x, 0, 2)
> print(z)
> print(RR(z))
> 
> output is
> 
>                                  4 sqrt(17) + 4
>                                  --------------
>                                        4
> 5.12310562561766
> 
> Am i doing something wrong?

No. Maxima gives

(%i2) integrate (sqrt(1+4*x^2), x, 0, 2);
                             asinh(4) + 4 sqrt(17)
(%o2)                        ---------------------
                                       4

so possibly SAGE is not parsing that properly? That's the only thing I can think
of. The following just confirms your computation:

sage: sqrt(1 + (2*x)^2).nintegrate(x, 0, 2)
(4.6467837624329427, 1.5663635326179329e-09, 21, 0)
sage: integral(sqrt(1 + (2*x)^2), x, 0, 2)
(4 + 4*sqrt(17))/4
sage: RR(integral(sqrt(1 + (2*x)^2), x, 0, 2))
5.12310562561766
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1215





---

archive/issue_comments_007544.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-11-20T15:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7544",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_007545.json:
```json
{
    "body": "Attachment [trac1215.patch](tarball://root/attachments/some-uuid/ticket1215/trac1215.patch) by was created at 2007-11-20 15:32:08",
    "created_at": "2007-11-20T15:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7545",
    "user": "was"
}
```

Attachment [trac1215.patch](tarball://root/attachments/some-uuid/ticket1215/trac1215.patch) by was created at 2007-11-20 15:32:08



---

archive/issue_comments_007546.json:
```json
{
    "body": "fixed: Merged in 2.8.13.rc1.",
    "created_at": "2007-11-20T15:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7546",
    "user": "mabshoff"
}
```

fixed: Merged in 2.8.13.rc1.



---

archive/issue_comments_007547.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-20T15:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7547",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007548.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-11-20T15:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7548",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_007549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T16:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1215#issuecomment-7549",
    "user": "mabshoff"
}
```

Resolution: fixed
