# Issue 6305: preparser issue with recurssive loading of .sage files

archive/issues_006305.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nHi,\nI'm not sure if it's a bug or it's me doing something wrong.\n\nI have two files:\n\ntest1.sage containing nothing but\n  print numpy.random.normal(0,(2*0.0061*0.33)^(1/2),1)\n\nand\n\ntest2.sage containing\n  load \"test1.sage\"\n\n\nI import numpy\nsage: import numpy\n\nNow\nsage: load \"test1.sage\"\nreturns values always smaller than 1\nthats the right distribution, the same i get when using the notebook-\ninterface\n\nbut\nsage: load \"test2.sage\"\nvery often returns values bigger than 1,\nthats a whole different distribution\n\nMy system is ubuntu-9.04-amd64 on Pentium Dual Core\nsage-4.0.1 from 2009-06-06\n```\n\n\nto which Marshall responds:\n\n```\nI'm not sure what is happening but I would guess that at some point\nthe ^(1/2) gets turned into ^(0), and then your standard deviation\ngoes from .06... to 1.  I.e., it seems like maybe the preparser\ndoesn't catch these nested loadings.\n\n-M. Hampton\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6305\n\n",
    "created_at": "2009-06-15T23:53:40Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "preparser issue with recurssive loading of .sage files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6305",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```
Hi,
I'm not sure if it's a bug or it's me doing something wrong.

I have two files:

test1.sage containing nothing but
  print numpy.random.normal(0,(2*0.0061*0.33)^(1/2),1)

and

test2.sage containing
  load "test1.sage"


I import numpy
sage: import numpy

Now
sage: load "test1.sage"
returns values always smaller than 1
thats the right distribution, the same i get when using the notebook-
interface

but
sage: load "test2.sage"
very often returns values bigger than 1,
thats a whole different distribution

My system is ubuntu-9.04-amd64 on Pentium Dual Core
sage-4.0.1 from 2009-06-06
```


to which Marshall responds:

```
I'm not sure what is happening but I would guess that at some point
the ^(1/2) gets turned into ^(0), and then your standard deviation
goes from .06... to 1.  I.e., it seems like maybe the preparser
doesn't catch these nested loadings.

-M. Hampton

```


Issue created by migration from https://trac.sagemath.org/ticket/6305





---

archive/issue_comments_050228.json:
```json
{
    "body": "Attachment [12063.patch](tarball://root/attachments/some-uuid/ticket6305/12063.patch) by rkirov created at 2009-06-16 02:49:07\n\nA simple fix by moving out the code that does the literals (changes 1/2 -> Integer(1)/Integer(2)) into a separate function and made sure its called at each load.\n\nall tests in devel/sage/misc passed.",
    "created_at": "2009-06-16T02:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6305#issuecomment-50228",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Attachment [12063.patch](tarball://root/attachments/some-uuid/ticket6305/12063.patch) by rkirov created at 2009-06-16 02:49:07

A simple fix by moving out the code that does the literals (changes 1/2 -> Integer(1)/Integer(2)) into a separate function and made sure its called at each load.

all tests in devel/sage/misc passed.



---

archive/issue_comments_050229.json:
```json
{
    "body": "This seems to be fixed now. I'll close this.",
    "created_at": "2010-01-19T07:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6305#issuecomment-50229",
    "user": "https://github.com/TimDumol"
}
```

This seems to be fixed now. I'll close this.



---

archive/issue_comments_050230.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-01-19T07:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6305#issuecomment-50230",
    "user": "https://github.com/TimDumol"
}
```

Resolution: worksforme



---

archive/issue_events_006551.json:
```json
{
    "actor": "@TimDumol",
    "created_at": "2010-01-19T07:19:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6305",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6305#event-6551"
}
```
