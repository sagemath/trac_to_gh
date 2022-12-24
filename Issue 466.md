# Issue 466: -b is actually not an option for hg_sage.merge()

archive/issues_000466.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage: hg_sage.merge?                        \nType:           instancemethod\nBase Class:     <type 'instancemethod'>\nString Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>\nNamespace:      Interactive\nFile:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py\nDefinition:     hg_sage.merge(self, options='')\nDocstring:\n    \n            Merge working directory with another revision\n            \n            Merge the contents of the current working directory and the\n            requested revision. Files that changed between either parent are\n            marked as changed for the next commit and a commit must be\n            performed before any further updates are allowed.\n    \n            INPUT:\n                options -- default: ''\n                    'tip' -- tip\n                     -b --branch  merge with head of a specific branch\n                     -f --force   force a merge with outstanding changes\n            \n\ncontradicted by\n\n\nsage: hg_sage.merge(options=\"--branch main\")\ncd \"/Library/sage/devel/sage\" && hg merge --branch main\nhg merge: option --branch not recognized\nhg merge [-f] [[-r] REV]\n\nmerge working directory with another revision\n\n    Merge the contents of the current working directory and the\n    requested revision. Files that changed between either parent are\n    marked as changed for the next commit and a commit must be\n    performed before any further updates are allowed.\n\n    If no revision is specified, the working directory's parent is a\n    head revision, and the repository contains exactly one other head,\n    the other head is merged with by default.  Otherwise, an explicit\n    revision to merge with must be provided.\n\noptions:\n\n -f --force  force a merge with outstanding changes\n -r --rev    revision to merge\n\nuse \"hg -v help merge\" to show global options\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/466\n\n",
    "created_at": "2007-08-20T09:20:13Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "-b is actually not an option for hg_sage.merge()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/466",
    "user": "pdehaye"
}
```
Assignee: @williamstein

sage: hg_sage.merge?                        
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>
Namespace:      Interactive
File:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py
Definition:     hg_sage.merge(self, options='')
Docstring:
    
            Merge working directory with another revision
            
            Merge the contents of the current working directory and the
            requested revision. Files that changed between either parent are
            marked as changed for the next commit and a commit must be
            performed before any further updates are allowed.
    
            INPUT:
                options -- default: ''
                    'tip' -- tip
                     -b --branch  merge with head of a specific branch
                     -f --force   force a merge with outstanding changes
            

contradicted by


sage: hg_sage.merge(options="--branch main")
cd "/Library/sage/devel/sage" && hg merge --branch main
hg merge: option --branch not recognized
hg merge [-f] [[-r] REV]

merge working directory with another revision

    Merge the contents of the current working directory and the
    requested revision. Files that changed between either parent are
    marked as changed for the next commit and a commit must be
    performed before any further updates are allowed.

    If no revision is specified, the working directory's parent is a
    head revision, and the repository contains exactly one other head,
    the other head is merged with by default.  Otherwise, an explicit
    revision to merge with must be provided.

options:

 -f --force  force a merge with outstanding changes
 -r --rev    revision to merge

use "hg -v help merge" to show global options




Issue created by migration from https://trac.sagemath.org/ticket/466





---

archive/issue_comments_002313.json:
```json
{
    "body": "That would be\n\n```\nsage: hg_sage.merge?\nType:           instancemethod\nBase Class:     <type 'instancemethod'>\nString Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>\nNamespace:      Interactive\nFile:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py\nDefinition:     hg_sage.merge(self, options='')\nDocstring:\n    \n            Merge working directory with another revision\n            \n            Merge the contents of the current working directory and the\n            requested revision. Files that changed between either parent are\n            marked as changed for the next commit and a commit must be\n            performed before any further updates are allowed.\n    \n            INPUT:\n                options -- default: ''\n                    'tip' -- tip\n                     -b --branch  merge with head of a specific branch\n                     -f --force   force a merge with outstanding changes\n            \n\nsage: hg_sage.merge(options=\"--branch main\")\ncd \"/Library/sage/devel/sage\" && hg merge --branch main\nhg merge: option --branch not recognized\nhg merge [-f] [[-r] REV]\n\nmerge working directory with another revision\n\n    Merge the contents of the current working directory and the\n    requested revision. Files that changed between either parent are\n    marked as changed for the next commit and a commit must be\n    performed before any further updates are allowed.\n\n    If no revision is specified, the working directory's parent is a\n    head revision, and the repository contains exactly one other head,\n    the other head is merged with by default.  Otherwise, an explicit\n    revision to merge with must be provided.\n\noptions:\n\n -f --force  force a merge with outstanding changes\n -r --rev    revision to merge\n\nuse \"hg -v help merge\" to show global options\n```\n",
    "created_at": "2007-08-22T13:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2313",
    "user": "pdehaye"
}
```

That would be

```
sage: hg_sage.merge?
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>
Namespace:      Interactive
File:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py
Definition:     hg_sage.merge(self, options='')
Docstring:
    
            Merge working directory with another revision
            
            Merge the contents of the current working directory and the
            requested revision. Files that changed between either parent are
            marked as changed for the next commit and a commit must be
            performed before any further updates are allowed.
    
            INPUT:
                options -- default: ''
                    'tip' -- tip
                     -b --branch  merge with head of a specific branch
                     -f --force   force a merge with outstanding changes
            

sage: hg_sage.merge(options="--branch main")
cd "/Library/sage/devel/sage" && hg merge --branch main
hg merge: option --branch not recognized
hg merge [-f] [[-r] REV]

merge working directory with another revision

    Merge the contents of the current working directory and the
    requested revision. Files that changed between either parent are
    marked as changed for the next commit and a commit must be
    performed before any further updates are allowed.

    If no revision is specified, the working directory's parent is a
    head revision, and the repository contains exactly one other head,
    the other head is merged with by default.  Otherwise, an explicit
    revision to merge with must be provided.

options:

 -f --force  force a merge with outstanding changes
 -r --rev    revision to merge

use "hg -v help merge" to show global options
```




---

archive/issue_comments_002314.json:
```json
{
    "body": "Attachment [5825.patch](tarball://root/attachments/some-uuid/ticket466/5825.patch) by pdehaye created at 2007-08-22 19:28:44",
    "created_at": "2007-08-22T19:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2314",
    "user": "pdehaye"
}
```

Attachment [5825.patch](tarball://root/attachments/some-uuid/ticket466/5825.patch) by pdehaye created at 2007-08-22 19:28:44



---

archive/issue_comments_002315.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2315",
    "user": "pdehaye"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002316.json:
```json
{
    "body": "the file attached should fix the bug",
    "created_at": "2007-08-22T19:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2316",
    "user": "pdehaye"
}
```

the file attached should fix the bug



---

archive/issue_comments_002317.json:
```json
{
    "body": "Changing assignee from @williamstein to pdehaye.",
    "created_at": "2007-08-22T19:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2317",
    "user": "pdehaye"
}
```

Changing assignee from @williamstein to pdehaye.



---

archive/issue_comments_002318.json:
```json
{
    "body": "Applied for sage-2.8.3",
    "created_at": "2007-08-29T02:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2318",
    "user": "@williamstein"
}
```

Applied for sage-2.8.3



---

archive/issue_comments_002319.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T02:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/466#issuecomment-2319",
    "user": "@williamstein"
}
```

Resolution: fixed
