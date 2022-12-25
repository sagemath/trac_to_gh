# Issue 3574: [with patch; needs review] optimize startup time by not importing mwrank library until needed

archive/issues_003574.json:
```json
{
    "body": "Assignee: cwitty\n\nBEFORE, with caching, on OS X:\n\n```\nteragon-2:mwrank was$ sage -startuptime|grep mwrank\n           mwrank: 0.000 (sage.interfaces.all)\n     sage.libs.mwrank.all: 0.013 (sage.libs.all)\n      interface: 0.001 (sage.libs.mwrank.all)\nteragon-2:mwrank was$ \n```\n\n\nAFTER:\n\n```\nteragon-2:mwrank was$ sage -startuptime|grep mwrank\n           mwrank: 0.000 (sage.interfaces.all)\n     sage.libs.mwrank.all: 0.001 (sage.libs.all)\n      interface: 0.001 (sage.libs.mwrank.all)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3574\n\n",
    "created_at": "2008-07-06T22:00:40Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch; needs review] optimize startup time by not importing mwrank library until needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3574",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

BEFORE, with caching, on OS X:

```
teragon-2:mwrank was$ sage -startuptime|grep mwrank
           mwrank: 0.000 (sage.interfaces.all)
     sage.libs.mwrank.all: 0.013 (sage.libs.all)
      interface: 0.001 (sage.libs.mwrank.all)
teragon-2:mwrank was$ 
```


AFTER:

```
teragon-2:mwrank was$ sage -startuptime|grep mwrank
           mwrank: 0.000 (sage.interfaces.all)
     sage.libs.mwrank.all: 0.001 (sage.libs.all)
      interface: 0.001 (sage.libs.mwrank.all)
```


Issue created by migration from https://trac.sagemath.org/ticket/3574





---

archive/issue_comments_025199.json:
```json
{
    "body": "Attachment [sage-3574.patch](tarball://root/attachments/some-uuid/ticket3574/sage-3574.patch) by @mwhansen created at 2008-07-06 22:44:20\n\nThis applies and passes tests in sage/libs/mwrank/ for me.",
    "created_at": "2008-07-06T22:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3574#issuecomment-25199",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-3574.patch](tarball://root/attachments/some-uuid/ticket3574/sage-3574.patch) by @mwhansen created at 2008-07-06 22:44:20

This applies and passes tests in sage/libs/mwrank/ for me.



---

archive/issue_comments_025200.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T02:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3574#issuecomment-25200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_025201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T02:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3574#issuecomment-25201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
