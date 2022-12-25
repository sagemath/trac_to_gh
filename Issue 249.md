# Issue 249: possible optimization opportunity

archive/issues_000249.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nprint preparse(\"\"\"\ndef m(n):\n  return [[j%n*n+(j+j-i)%n+1\n    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]\n\"\"\")\n///\ndef m(n):\n  return [[j%n*n+(j+j-i)%n+Integer(1)\n    for j in range(i+(Integer(1)-n)/Integer(2),i+(n+Integer(1))/Integer(2))] for i in range(n)]\n```\n\n\n\n```\ndef m(n):\n  return [[j%n*n+(j+j-i)%n+1\n    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]\n```\n\n\n\n```\ntime a=m(201)\n///\nCPU time: 0.63 s,  Wall time: 0.65 s\n```\n\n\n\n```\ndef m(n):\n  one = 1; two=2\n  return [[j%n*n+(j+j-i)%n+one\n    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]\n```\n\n\n\n```\ntime a=m(201)\n///\nCPU time: 0.60 s,  Wall time: 0.61 s\n```\n\n\n\n```\ndef m(n):\n  one = 1r; two=2r\n  return [[j%n*n+(j+j-i)%n+one\n    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]\n```\n\n\n\n```\ntime a=m(201)\n///\nCPU time: 0.75 s,  Wall time: 0.79 s\n```\n\n\n\n```\n%python\n\ndef m(n):\n  one = 1; two=2\n  return [[j%n*n+(j+j-i)%n+one\n    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]\n```\n\n\n\n```\ntime a=m(201r)\n///\nCPU time: 0.03 s,  Wall time: 0.03 s\n```\n\n\n\n```\ndef m(n):\n  one = 1r; two=2r; n=int(n)\n  return [[j%n*n+(j+j-i)%n+one\n    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]\n```\n\n\n\n```\ntime a=m(201)\n///\nCPU time: 0.02 s,  Wall time: 0.02 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/249\n\n",
    "created_at": "2007-02-07T06:39:19Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "possible optimization opportunity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/249",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
print preparse("""
def m(n):
  return [[j%n*n+(j+j-i)%n+1
    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]
""")
///
def m(n):
  return [[j%n*n+(j+j-i)%n+Integer(1)
    for j in range(i+(Integer(1)-n)/Integer(2),i+(n+Integer(1))/Integer(2))] for i in range(n)]
```



```
def m(n):
  return [[j%n*n+(j+j-i)%n+1
    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.63 s,  Wall time: 0.65 s
```



```
def m(n):
  one = 1; two=2
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.60 s,  Wall time: 0.61 s
```



```
def m(n):
  one = 1r; two=2r
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.75 s,  Wall time: 0.79 s
```



```
%python

def m(n):
  one = 1; two=2
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201r)
///
CPU time: 0.03 s,  Wall time: 0.03 s
```



```
def m(n):
  one = 1r; two=2r; n=int(n)
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.02 s,  Wall time: 0.02 s
```


Issue created by migration from https://trac.sagemath.org/ticket/249





---

archive/issue_events_000516.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T05:26:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/249#event-516"
}
```



---

archive/issue_comments_001090.json:
```json
{
    "body": "It is unclear to me what the objective of this ticket is besides the fact that python types are potentially faster than certain Sage types like Integers. So: please elaborate or invalidate this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T19:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1090",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It is unclear to me what the objective of this ticket is besides the fact that python types are potentially faster than certain Sage types like Integers. So: please elaborate or invalidate this ticket.

Cheers,

Michael



---

archive/issue_comments_001091.json:
```json
{
    "body": "The examples above very clearly indicate that by factoring preparsed constants out when preparsing chunks of code results in potentially vast speedups.   We should have been doing this since day 1, but just haven't got around to it.  This ticket should definitely *not* be invalidated.  I've reworded it to be much more precise with one clear example.",
    "created_at": "2008-03-22T19:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1091",
    "user": "https://github.com/williamstein"
}
```

The examples above very clearly indicate that by factoring preparsed constants out when preparsing chunks of code results in potentially vast speedups.   We should have been doing this since day 1, but just haven't got around to it.  This ticket should definitely *not* be invalidated.  I've reworded it to be much more precise with one clear example.



---

archive/issue_events_000517.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-22T19:42:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/249#event-517"
}
```



---

archive/issue_events_000518.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-22T19:42:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/249#event-518"
}
```



---

archive/issue_comments_001092.json:
```json
{
    "body": "I have strong concerns about this messing up things with side effects.  It is far from clear for me that this is the correct course of action, and if it is, it must have a flag to disable it for doctests.",
    "created_at": "2008-04-07T08:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1092",
    "user": "https://github.com/garyfurnish"
}
```

I have strong concerns about this messing up things with side effects.  It is far from clear for me that this is the correct course of action, and if it is, it must have a flag to disable it for doctests.



---

archive/issue_comments_001093.json:
```json
{
    "body": "It makes even more of a difference for real numbers. \n\nBefore \n\n\n```\n%time\nx = 0\nwhile x < 1e5:\n    x += 1.5\nCPU time: 0.71 s,  Wall time: 0.73 s\n```\n\n\nAfter\n\n\n```\n%time\nx = 0\nwhile x < 1e5:\n    x += 1.5\nCPU time: 0.06 s,  Wall time: 0.06 s\n```\n",
    "created_at": "2008-09-23T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1093",
    "user": "https://github.com/robertwb"
}
```

It makes even more of a difference for real numbers. 

Before 


```
%time
x = 0
while x < 1e5:
    x += 1.5
CPU time: 0.71 s,  Wall time: 0.73 s
```


After


```
%time
x = 0
while x < 1e5:
    x += 1.5
CPU time: 0.06 s,  Wall time: 0.06 s
```




---

archive/issue_comments_001094.json:
```json
{
    "body": "Attachment [249-preparse-constants.patch](tarball://root/attachments/some-uuid/ticket249/249-preparse-constants.patch) by @robertwb created at 2008-09-23 21:43:57",
    "created_at": "2008-09-23T21:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1094",
    "user": "https://github.com/robertwb"
}
```

Attachment [249-preparse-constants.patch](tarball://root/attachments/some-uuid/ticket249/249-preparse-constants.patch) by @robertwb created at 2008-09-23 21:43:57



---

archive/issue_comments_001095.json:
```json
{
    "body": "Looks good.  I have tried it with a bunch of different types of constants (reals, complexes, rationals) and I'm satisfied that it works.",
    "created_at": "2008-09-24T00:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1095",
    "user": "https://github.com/aghitza"
}
```

Looks good.  I have tried it with a bunch of different types of constants (reals, complexes, rationals) and I'm satisfied that it works.



---

archive/issue_events_000519.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T02:09:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/249#event-519"
}
```



---

archive/issue_comments_001096.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T02:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_001097.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T02:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/249#issuecomment-1097",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
