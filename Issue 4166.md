# Issue 4166: Separate resource for @interact

archive/issues_004166.json:
```json
{
    "body": "Assignee: itolkov\n\nThere is a new resource for the initial evaluation and later updates.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4166\n\n",
    "created_at": "2008-09-22T02:15:26Z",
    "labels": [
        "interact",
        "major",
        "enhancement"
    ],
    "title": "Separate resource for @interact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4166",
    "user": "itolkov"
}
```
Assignee: itolkov

There is a new resource for the initial evaluation and later updates.

Issue created by migration from https://trac.sagemath.org/ticket/4166





---

archive/issue_comments_030248.json:
```json
{
    "body": "Attachment\n\nGood, works, but has one problem, which is that it creates a serious security vulnerability.  It needs code like this or something like in the Worksheet_eval Resource:\n\n```\n        if owner != '_sage_':\n            if W.owner() != self.username and not (self.username in W.collaborators()):\n               return InvalidPage(msg = \"can't evaluate worksheet cells\", username = self.username\\\n)\n```\n\n\nOnce this is resolved, it will get a positive review. \n\nIt might also be nice if there were a comment that explains why we are creating this new resource.  E.g., \"make code cleaner\"?  \"because it will be needed later for something else\nthat is planned?\"",
    "created_at": "2008-09-24T22:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4166#issuecomment-30248",
    "user": "was"
}
```

Attachment

Good, works, but has one problem, which is that it creates a serious security vulnerability.  It needs code like this or something like in the Worksheet_eval Resource:

```
        if owner != '_sage_':
            if W.owner() != self.username and not (self.username in W.collaborators()):
               return InvalidPage(msg = "can't evaluate worksheet cells", username = self.username\
)
```


Once this is resolved, it will get a positive review. 

It might also be nice if there were a comment that explains why we are creating this new resource.  E.g., "make code cleaner"?  "because it will be needed later for something else
that is planned?"
