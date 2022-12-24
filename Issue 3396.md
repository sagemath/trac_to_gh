# Issue 3396: [with patch, needs review] new function in misc/latex.py: print_or_typeset

archive/issues_003396.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: latex, view, print\n\nThis patch defines a function in sage.misc.latex, print_or_typeset, which runs 'view' if in notebook mode with the typeset box, and runs 'print' otherwise.  See the discussion toward the end of this thread:\n\n[http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac](http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3396\n\n",
    "created_at": "2008-06-11T04:31:55Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] new function in misc/latex.py: print_or_typeset",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3396",
    "user": "jhpalmieri"
}
```
Assignee: somebody

Keywords: latex, view, print

This patch defines a function in sage.misc.latex, print_or_typeset, which runs 'view' if in notebook mode with the typeset box, and runs 'print' otherwise.  See the discussion toward the end of this thread:

[http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac](http://groups.google.com/group/sage-support/browse_frm/thread/9698e83a1d1b22ac)



Issue created by migration from https://trac.sagemath.org/ticket/3396





---

archive/issue_comments_023781.json:
```json
{
    "body": "new function, print_or_typeset",
    "created_at": "2008-06-11T04:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3396#issuecomment-23781",
    "user": "jhpalmieri"
}
```

new function, print_or_typeset



---

archive/issue_comments_023782.json:
```json
{
    "body": "Attachment [sage-3396-doctests.patch](tarball://root/attachments/some-uuid/ticket3396/sage-3396-doctests.patch) by was created at 2008-06-11 15:05:15\n\napply this after the other patch",
    "created_at": "2008-06-11T15:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3396#issuecomment-23782",
    "user": "was"
}
```

Attachment [sage-3396-doctests.patch](tarball://root/attachments/some-uuid/ticket3396/sage-3396-doctests.patch) by was created at 2008-06-11 15:05:15

apply this after the other patch



---

archive/issue_comments_023783.json:
```json
{
    "body": "Merged both patch in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3396#issuecomment-23783",
    "user": "mabshoff"
}
```

Merged both patch in Sage 3.0.3.rc0



---

archive/issue_comments_023784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3396#issuecomment-23784",
    "user": "mabshoff"
}
```

Resolution: fixed
