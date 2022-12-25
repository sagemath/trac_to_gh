# Issue 1060: fix flintqs compile on OSX 10.5

archive/issues_001060.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe fix for flintqs is the same as for givaro, basically. To the file\n\n```\n    src/lanczos.c\n```\n\nadd the following as the first line:\n\n```\n#include \"sys/types.h\"\n```\n\nThen it builds fine. \n\n-- William\n\nIssue created by migration from https://trac.sagemath.org/ticket/1060\n\n",
    "created_at": "2007-11-02T00:25:17Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "fix flintqs compile on OSX 10.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The fix for flintqs is the same as for givaro, basically. To the file

```
    src/lanczos.c
```

add the following as the first line:

```
#include "sys/types.h"
```

Then it builds fine. 

-- William

Issue created by migration from https://trac.sagemath.org/ticket/1060





---

archive/issue_events_002870.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-02T01:08:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1060",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1060#event-2870"
}
```



---

archive/issue_comments_006425.json:
```json
{
    "body": "applied to 2.8.11.rc1 - via new flintqs-20070817.p0",
    "created_at": "2007-11-02T01:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1060#issuecomment-6425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.rc1 - via new flintqs-20070817.p0



---

archive/issue_comments_006426.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T01:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1060#issuecomment-6426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
