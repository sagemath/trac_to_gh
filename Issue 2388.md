# Issue 2388: linbox charpoly crashes on OS X 10.5-intel

archive/issues_002388.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations.\nThe bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.\n\n[http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html](http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html), may help.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2388\n\n",
    "created_at": "2008-03-04T21:55:42Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "linbox charpoly crashes on OS X 10.5-intel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2388",
    "user": "cpernet"
}
```
Assignee: mabshoff

The proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations.
The bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.

[http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html](http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html), may help.

Issue created by migration from https://trac.sagemath.org/ticket/2388





---

archive/issue_comments_016116.json:
```json
{
    "body": "Attachment [ticket-staticinit.txt](tarball://root/attachments/some-uuid/ticket2388/ticket-staticinit.txt) by cpernet created at 2008-03-04 21:56:02",
    "created_at": "2008-03-04T21:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16116",
    "user": "cpernet"
}
```

Attachment [ticket-staticinit.txt](tarball://root/attachments/some-uuid/ticket2388/ticket-staticinit.txt) by cpernet created at 2008-03-04 21:56:02



---

archive/issue_comments_016117.json:
```json
{
    "body": "I fixed the bug by changing the algorithm for charpoly, that I had to change anyway (faster).\nThis fixes the bug, since the buggy code is no longer used.\n\nThe fixed spkg is available at\n[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg)\n\nThe clean fix will be in ticket 2389.",
    "created_at": "2008-03-04T22:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16117",
    "user": "cpernet"
}
```

I fixed the bug by changing the algorithm for charpoly, that I had to change anyway (faster).
This fixes the bug, since the buggy code is no longer used.

The fixed spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg)

The clean fix will be in ticket 2389.



---

archive/issue_comments_016118.json:
```json
{
    "body": "Changing assignee from mabshoff to cpernet.",
    "created_at": "2008-03-04T22:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16118",
    "user": "cpernet"
}
```

Changing assignee from mabshoff to cpernet.



---

archive/issue_comments_016119.json:
```json
{
    "body": "Positive review after fixing various issues in the repo, i.e. \n\n```\nM SPKG.txt\n! linbox_wrap/src/linbox_wrap.cpp~\n! linbox_wrap/src/linbox_wrap.h~\n? linbox_wrap/src/linbox_wrap.cpp.ori\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-05T05:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16119",
    "user": "mabshoff"
}
```

Positive review after fixing various issues in the repo, i.e. 

```
M SPKG.txt
! linbox_wrap/src/linbox_wrap.cpp~
! linbox_wrap/src/linbox_wrap.h~
? linbox_wrap/src/linbox_wrap.cpp.ori
```


Cheers,

Michael



---

archive/issue_comments_016120.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T05:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16120",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_comments_016121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T05:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2388#issuecomment-16121",
    "user": "mabshoff"
}
```

Resolution: fixed
