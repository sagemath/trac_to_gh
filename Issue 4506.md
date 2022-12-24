# Issue 4506: planarity ignores error code when adding edge

archive/issues_004506.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ekirkman bober\n\nThe planarity code ignores errors when adding edges.  This patch also shortcuts the planarity checking when adding an edge returns the NONPLANAR code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4506\n\n",
    "created_at": "2008-11-13T01:21:30Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "planarity ignores error code when adding edge",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4506",
    "user": "jason"
}
```
Assignee: rlm

CC:  ekirkman bober

The planarity code ignores errors when adding edges.  This patch also shortcuts the planarity checking when adding an edge returns the NONPLANAR code.

Issue created by migration from https://trac.sagemath.org/ticket/4506





---

archive/issue_comments_033410.json:
```json
{
    "body": "Attachment [planarity-add-edge.patch](tarball://root/attachments/some-uuid/ticket4506/planarity-add-edge.patch) by jason created at 2008-11-13 01:22:43",
    "created_at": "2008-11-13T01:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33410",
    "user": "jason"
}
```

Attachment [planarity-add-edge.patch](tarball://root/attachments/some-uuid/ticket4506/planarity-add-edge.patch) by jason created at 2008-11-13 01:22:43



---

archive/issue_comments_033411.json:
```json
{
    "body": "The patch here ought to add a doctest :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T03:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33411",
    "user": "mabshoff"
}
```

The patch here ought to add a doctest :)

Cheers,

Michael



---

archive/issue_comments_033412.json:
```json
{
    "body": "I don't see what to doctest.  I personally didn't come across any errors, I'm just adding the checking as good programming practice.  As for the shortcut in the nonplanar case, I'm just doing exactly what Boyer does in his C program.  The program gave the correct answers before, now it just doesn't worry about finding a kuratowski subgraph if it is not needed.\n\nAgain, I didn't see any errors before, so I can't put in a doctest that didn't work before, but does after the patch.  This is pro-active bugfixing, not reactive bugfixing :).",
    "created_at": "2008-11-13T03:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33412",
    "user": "jason"
}
```

I don't see what to doctest.  I personally didn't come across any errors, I'm just adding the checking as good programming practice.  As for the shortcut in the nonplanar case, I'm just doing exactly what Boyer does in his C program.  The program gave the correct answers before, now it just doesn't worry about finding a kuratowski subgraph if it is not needed.

Again, I didn't see any errors before, so I can't put in a doctest that didn't work before, but does after the patch.  This is pro-active bugfixing, not reactive bugfixing :).



---

archive/issue_comments_033413.json:
```json
{
    "body": "It looks good to me. \n\nUnless one knows how to make the C program fail (out of memory?) I don't see what doctest to add. The result is the same, so I think the existing doctests cover it.",
    "created_at": "2008-11-13T23:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33413",
    "user": "robertwb"
}
```

It looks good to me. 

Unless one knows how to make the C program fail (out of memory?) I don't see what doctest to add. The result is the same, so I think the existing doctests cover it.



---

archive/issue_comments_033414.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-14T03:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33414",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_comments_033415.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T03:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33415",
    "user": "mabshoff"
}
```

Resolution: fixed
