# Issue 3448: Preparser handles (ellipses in) triple quotes incorrectly

archive/issues_003448.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\n\n```\nsage: s = \"\"\"G0 [14..26,6][:6242]\n....: G1 [14..26,6][6242:12484]\n....: G2 [14..26,6][12484:18726]\n....: G3 [14..26,6][18726:24968]\n....: G4 [14..26,6][24968:31210]\n....: G5 [14..26,6][31210:]\n....: \"\"\"\nsage: s.split('\\n')\n\n['G0 (ellipsis_range(14,Ellipsis,26,6))[:6242]',\n 'G1 (ellipsis_range(14,Ellipsis,26,6))[6242:12484]',\n 'G2 (ellipsis_range(14,Ellipsis,26,6))[12484:18726]',\n 'G3 (ellipsis_range(14,Ellipsis,26,6))[18726:24968]',\n 'G4 (ellipsis_range(14,Ellipsis,26,6))[24968:31210]',\n 'G5 (ellipsis_range(14,Ellipsis,26,6))[31210:]',\n '']  \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3448\n\n",
    "created_at": "2008-06-17T15:39:08Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Preparser handles (ellipses in) triple quotes incorrectly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3448",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  @robertwb


```
sage: s = """G0 [14..26,6][:6242]
....: G1 [14..26,6][6242:12484]
....: G2 [14..26,6][12484:18726]
....: G3 [14..26,6][18726:24968]
....: G4 [14..26,6][24968:31210]
....: G5 [14..26,6][31210:]
....: """
sage: s.split('\n')

['G0 (ellipsis_range(14,Ellipsis,26,6))[:6242]',
 'G1 (ellipsis_range(14,Ellipsis,26,6))[6242:12484]',
 'G2 (ellipsis_range(14,Ellipsis,26,6))[12484:18726]',
 'G3 (ellipsis_range(14,Ellipsis,26,6))[18726:24968]',
 'G4 (ellipsis_range(14,Ellipsis,26,6))[24968:31210]',
 'G5 (ellipsis_range(14,Ellipsis,26,6))[31210:]',
 '']  
```


Issue created by migration from https://trac.sagemath.org/ticket/3448





---

archive/issue_comments_024272.json:
```json
{
    "body": "I don't think RobertWB is aware of the problem, so let's CC him.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T17:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3448#issuecomment-24272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I don't think RobertWB is aware of the problem, so let's CC him.

Cheers,

Michael



---

archive/issue_comments_024273.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-02T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3448#issuecomment-24273",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_003667.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-02-02T22:57:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3448",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3448#event-3667"
}
```



---

archive/issue_comments_024274.json:
```json
{
    "body": "I'm going to mark this as invalid now since the code for the preparser has been reworked:\n\n\n```\nsage: s = \"\"\"G0 [14..26,6][:6242]\n....: G1 [14..26,6][6242:12484]\n....: G2 [14..26,6][12484:18726]\n....: G3 [14..26,6][18726:24968]\n....: G4 [14..26,6][24968:31210]\n....: G5 [14..26,6][31210:]\n....: \"\"\"\nsage: s.split('\\n')\n['G0 [14..26,6][:6242]', 'G1 [14..26,6][6242:12484]', 'G2 [14..26,6][12484:18726]', 'G3 [14..26,6][18726:24968]', 'G4 [14..26,6][24968:31210]', 'G5 [14..26,6][31210:]', '']\n```\n",
    "created_at": "2010-02-02T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3448#issuecomment-24274",
    "user": "https://github.com/mwhansen"
}
```

I'm going to mark this as invalid now since the code for the preparser has been reworked:


```
sage: s = """G0 [14..26,6][:6242]
....: G1 [14..26,6][6242:12484]
....: G2 [14..26,6][12484:18726]
....: G3 [14..26,6][18726:24968]
....: G4 [14..26,6][24968:31210]
....: G5 [14..26,6][31210:]
....: """
sage: s.split('\n')
['G0 [14..26,6][:6242]', 'G1 [14..26,6][6242:12484]', 'G2 [14..26,6][12484:18726]', 'G3 [14..26,6][18726:24968]', 'G4 [14..26,6][24968:31210]', 'G5 [14..26,6][31210:]', '']
```

