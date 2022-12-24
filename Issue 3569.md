# Issue 3569: optimize import of sage.dsage.interface.dsage_interface

archive/issues_003569.json:
```json
{
    "body": "Assignee: cwitty\n\nBEFORE\n\n```\nteragon-2:misc was$ sage -startuptime|grep dsage_interface\n        sage.dsage.interface.dsage_interface: 0.092 (dist_function)\n         twisted.cred.credentials: 0.009 (sage.dsage.interface.dsage_interface)\n         twisted.internet.threads: 0.011 (sage.dsage.interface.dsage_interface)\n         twisted.internet.interfaces: 0.040 (sage.dsage.interface.dsage_interface)\n0.092 sage.dsage.interface.dsage_interface (dist_function)\n0.040 twisted.internet.interfaces (sage.dsage.interface.dsage_interface)\n```\n\n\nThis is after using it multiple times (so caching).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3569\n\n",
    "created_at": "2008-07-06T20:13:04Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "optimize import of sage.dsage.interface.dsage_interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3569",
    "user": "was"
}
```
Assignee: cwitty

BEFORE

```
teragon-2:misc was$ sage -startuptime|grep dsage_interface
        sage.dsage.interface.dsage_interface: 0.092 (dist_function)
         twisted.cred.credentials: 0.009 (sage.dsage.interface.dsage_interface)
         twisted.internet.threads: 0.011 (sage.dsage.interface.dsage_interface)
         twisted.internet.interfaces: 0.040 (sage.dsage.interface.dsage_interface)
0.092 sage.dsage.interface.dsage_interface (dist_function)
0.040 twisted.internet.interfaces (sage.dsage.interface.dsage_interface)
```


This is after using it multiple times (so caching).

Issue created by migration from https://trac.sagemath.org/ticket/3569





---

archive/issue_comments_025216.json:
```json
{
    "body": "Attachment [sage-3569.patch](tarball://root/attachments/some-uuid/ticket3569/sage-3569.patch) by was created at 2008-07-06 20:26:06\n\nAFTER\n\n```\nteragon-2:dsage was$ sage -startuptime|grep twisted\n```\n\n\n\n```\nteragon-2:dsage was$ sage -startuptime|grep dsage_interface\n        sage.dsage.interface.dsage_interface: 0.007 (dist_function)\n         sage.dsage.misc.misc: 0.005 (sage.dsage.interface.dsage_interface)\n```\n",
    "created_at": "2008-07-06T20:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3569#issuecomment-25216",
    "user": "was"
}
```

Attachment [sage-3569.patch](tarball://root/attachments/some-uuid/ticket3569/sage-3569.patch) by was created at 2008-07-06 20:26:06

AFTER

```
teragon-2:dsage was$ sage -startuptime|grep twisted
```



```
teragon-2:dsage was$ sage -startuptime|grep dsage_interface
        sage.dsage.interface.dsage_interface: 0.007 (dist_function)
         sage.dsage.misc.misc: 0.005 (sage.dsage.interface.dsage_interface)
```




---

archive/issue_comments_025217.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-06T20:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3569#issuecomment-25217",
    "user": "mhansen"
}
```

+1



---

archive/issue_comments_025218.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T02:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3569#issuecomment-25218",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025219.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T02:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3569#issuecomment-25219",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
