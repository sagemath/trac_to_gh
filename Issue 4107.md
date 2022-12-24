# Issue 4107: [with patch, needs review] trivial typos in tut.tex

archive/issues_004107.json:
```json
{
    "body": "Assignee: somebody\n\n(see the thread of the same name in sage-devel)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4107\n\n",
    "created_at": "2008-09-12T20:17:24Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] trivial typos in tut.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4107",
    "user": "GeorgSWeber"
}
```
Assignee: somebody

(see the thread of the same name in sage-devel)

Issue created by migration from https://trac.sagemath.org/ticket/4107





---

archive/issue_comments_029741.json:
```json
{
    "body": "Where is the patch? :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-12T23:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29741",
    "user": "mabshoff"
}
```

Where is the patch? :)

Cheers,

Michael



---

archive/issue_comments_029742.json:
```json
{
    "body": "I have attached a diff (not a patch) against 3.1.2.rc2 since not all fixes do apply any more due to the rewrite of the manual by John Palmieri. I left out the fix \n\n```\n There is one subtlety in defining complex numbers: as mentioned above, \n-the symbol \\code{i} represents a square root of \\minusone, but it is a \n+the symbol \\code{i} represents the square root of \\minusone, but it is a \n \\emph{formal} square root of \\minusone; it is not in the complex numbers. \n Calling \\code{CC(i)} returns the complex square root of \\minusone.\n```\n\nsince there are multiple roots.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-13T00:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29742",
    "user": "mabshoff"
}
```

I have attached a diff (not a patch) against 3.1.2.rc2 since not all fixes do apply any more due to the rewrite of the manual by John Palmieri. I left out the fix 

```
 There is one subtlety in defining complex numbers: as mentioned above, 
-the symbol \code{i} represents a square root of \minusone, but it is a 
+the symbol \code{i} represents the square root of \minusone, but it is a 
 \emph{formal} square root of \minusone; it is not in the complex numbers. 
 Calling \code{CC(i)} returns the complex square root of \minusone.
```

since there are multiple roots.

Cheers,

Michael



---

archive/issue_comments_029743.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-13T00:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29743",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_029744.json:
```json
{
    "body": "Attachment [trac_4107.patch](tarball://root/attachments/some-uuid/ticket4107/trac_4107.patch) by mabshoff created at 2008-09-13 00:42:50\n\nUpdated patch with changes commited in Minh Nguyen's name",
    "created_at": "2008-09-13T00:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29744",
    "user": "mabshoff"
}
```

Attachment [trac_4107.patch](tarball://root/attachments/some-uuid/ticket4107/trac_4107.patch) by mabshoff created at 2008-09-13 00:42:50

Updated patch with changes commited in Minh Nguyen's name



---

archive/issue_comments_029745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-13T00:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29745",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029746.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-13T00:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4107#issuecomment-29746",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc2
