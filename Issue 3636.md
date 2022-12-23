# Issue 3636: Text control, no label

archive/issues_003636.json:
```json
{
    "body": "Assignee: itolkov\n\nAllows adding text among the controls:\n\n\n```\n@interact\ndef _(t1=text_control(\"Factors an integer.\"), n=\"1\"):\n    print factor(Integer(n))\n```\n\n\nAdditionally, the way labels are displayed is changed. If an empty label ('') is specified, the input block is aligned with the left edge of the table, rather than the rest of the controls. This is useful for controls that should not have a label, such as text. However, if label=' ' (space) is set, the input is aligned with the rest of the inputs with no label showing.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3636\n\n",
    "created_at": "2008-07-10T21:07:58Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Text control, no label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3636",
    "user": "itolkov"
}
```
Assignee: itolkov

Allows adding text among the controls:


```
@interact
def _(t1=text_control("Factors an integer."), n="1"):
    print factor(Integer(n))
```


Additionally, the way labels are displayed is changed. If an empty label ('') is specified, the input block is aligned with the left edge of the table, rather than the rest of the controls. This is useful for controls that should not have a label, such as text. However, if label=' ' (space) is set, the input is aligned with the rest of the inputs with no label showing.


Issue created by migration from https://trac.sagemath.org/ticket/3636





---

archive/issue_comments_025717.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-10T21:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25717",
    "user": "itolkov"
}
```

Attachment



---

archive/issue_comments_025718.json:
```json
{
    "body": "Can you please put an example of using the control in the documentation for interact()?  The above example would work great.",
    "created_at": "2008-07-21T22:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25718",
    "user": "jason"
}
```

Can you please put an example of using the control in the documentation for interact()?  The above example would work great.



---

archive/issue_comments_025719.json:
```json
{
    "body": "Please remember to assign a milestone.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T22:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25719",
    "user": "mabshoff"
}
```

Please remember to assign a milestone.

Cheers,

Michael



---

archive/issue_comments_025720.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-22T20:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25720",
    "user": "itolkov"
}
```

Attachment



---

archive/issue_comments_025721.json:
```json
{
    "body": "Done.",
    "created_at": "2008-07-22T20:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25721",
    "user": "itolkov"
}
```

Done.



---

archive/issue_comments_025722.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha0",
    "created_at": "2008-07-30T23:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25722",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.alpha0



---

archive/issue_comments_025723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T23:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3636#issuecomment-25723",
    "user": "mabshoff"
}
```

Resolution: fixed
