# Issue 1326: 2.8.14/Solaris: combinat/combinat.py doctest failure

archive/issues_001326.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t  devel/sage-main/sage/combinat/combinat.py          ****************************************************************\n******\nFile \"combinat.py\", line 1869:\n    sage: number_of_partitions(100000)\nExpected:\n    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489\n4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140\n4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519\nGot:\n    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489\n4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140\n4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600582558780007\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1326\n\n",
    "created_at": "2007-11-28T21:56:40Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "2.8.14/Solaris: combinat/combinat.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1326",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure


```
sage -t  devel/sage-main/sage/combinat/combinat.py          ****************************************************************
******
File "combinat.py", line 1869:
    sage: number_of_partitions(100000)
Expected:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489
4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140
4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519
Got:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489
4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140
4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600582558780007
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/1326





---

archive/issue_comments_008471.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-15T23:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1326#issuecomment-8471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_001466.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-15T23:08:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1326#event-1466"
}
```



---

archive/issue_comments_008472.json:
```json
{
    "body": "This is a dupe of #1339. So I am closing this one as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1326#issuecomment-8472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #1339. So I am closing this one as a dupe.

Cheers,

Michael
