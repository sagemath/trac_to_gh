# Issue 4506: [with patch, positive review] planarity ignores error code when adding edge

archive/issues_004506.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  ekirkman bober\n\nThe planarity code ignores errors when adding edges.  This patch also shortcuts the planarity checking when adding an edge returns the NONPLANAR code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4506\n\n",
    "closed_at": "2008-11-14T03:30:53Z",
    "created_at": "2008-11-13T01:21:30Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] planarity ignores error code when adding edge",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4506",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  ekirkman bober

The planarity code ignores errors when adding edges.  This patch also shortcuts the planarity checking when adding an edge returns the NONPLANAR code.

Issue created by migration from https://trac.sagemath.org/ticket/4506





---

archive/issue_comments_033345.json:
```json
{
    "body": "Attachment [planarity-add-edge.patch](tarball://root/attachments/some-uuid/ticket4506/planarity-add-edge.patch) by @jasongrout created at 2008-11-13 01:22:43",
    "created_at": "2008-11-13T01:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33345",
    "user": "https://github.com/jasongrout"
}
```

Attachment [planarity-add-edge.patch](tarball://root/attachments/some-uuid/ticket4506/planarity-add-edge.patch) by @jasongrout created at 2008-11-13 01:22:43



---

archive/issue_comments_033346.json:
```json
{
    "body": "The patch here ought to add a doctest :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T03:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33346",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch here ought to add a doctest :)

Cheers,

Michael



---

archive/issue_comments_033347.json:
```json
{
    "body": "I don't see what to doctest.  I personally didn't come across any errors, I'm just adding the checking as good programming practice.  As for the shortcut in the nonplanar case, I'm just doing exactly what Boyer does in his C program.  The program gave the correct answers before, now it just doesn't worry about finding a kuratowski subgraph if it is not needed.\n\nAgain, I didn't see any errors before, so I can't put in a doctest that didn't work before, but does after the patch.  This is pro-active bugfixing, not reactive bugfixing :).",
    "created_at": "2008-11-13T03:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33347",
    "user": "https://github.com/jasongrout"
}
```

I don't see what to doctest.  I personally didn't come across any errors, I'm just adding the checking as good programming practice.  As for the shortcut in the nonplanar case, I'm just doing exactly what Boyer does in his C program.  The program gave the correct answers before, now it just doesn't worry about finding a kuratowski subgraph if it is not needed.

Again, I didn't see any errors before, so I can't put in a doctest that didn't work before, but does after the patch.  This is pro-active bugfixing, not reactive bugfixing :).



---

archive/issue_comments_033348.json:
```json
{
    "body": "It looks good to me. \n\nUnless one knows how to make the C program fail (out of memory?) I don't see what doctest to add. The result is the same, so I think the existing doctests cover it.",
    "created_at": "2008-11-13T23:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33348",
    "user": "https://github.com/robertwb"
}
```

It looks good to me. 

Unless one knows how to make the C program fail (out of memory?) I don't see what doctest to add. The result is the same, so I think the existing doctests cover it.



---

archive/issue_comments_033349.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-14T03:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_events_010208.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-14T03:30:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4506#event-10208"
}
```



---

archive/issue_comments_033350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T03:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4506#issuecomment-33350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
