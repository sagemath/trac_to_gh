# Issue 5021: [with patch, needs review] add some jsMath extensions

archive/issues_005021.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: jsMath\n\nIn the spirit of the patch for #4945, this patch adds several jsMath extensions so that some new LaTeX commands will be available: it adds `moreArrows` which implements \\xrightarrow among other things, and it adds `AMSmath`, which implements a handful of commands from the amsmath LaTeX package.\n\nThis patch also adds a few lines of documentation which give links to the jsMath pages for these extensions.  See those web pages for complete lists of all of the LaTeX commands made available by these packages.\n\n(I'm adding this because I want to contribute some Sage code which uses \\xrightarrow, but other people might find these useful as well.)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5021\n\n",
    "created_at": "2009-01-19T06:02:31Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] add some jsMath extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5021",
    "user": "@jhpalmieri"
}
```
Assignee: boothby

Keywords: jsMath

In the spirit of the patch for #4945, this patch adds several jsMath extensions so that some new LaTeX commands will be available: it adds `moreArrows` which implements \xrightarrow among other things, and it adds `AMSmath`, which implements a handful of commands from the amsmath LaTeX package.

This patch also adds a few lines of documentation which give links to the jsMath pages for these extensions.  See those web pages for complete lists of all of the LaTeX commands made available by these packages.

(I'm adding this because I want to contribute some Sage code which uses \xrightarrow, but other people might find these useful as well.)



Issue created by migration from https://trac.sagemath.org/ticket/5021





---

archive/issue_comments_038247.json:
```json
{
    "body": "Attachment [5021.patch](tarball://root/attachments/some-uuid/ticket5021/5021.patch) by @jasongrout created at 2009-01-28 17:39:05\n\nLooks good.  I tested a command from each package and it seemed to work great.  Positive review.",
    "created_at": "2009-01-28T17:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5021#issuecomment-38247",
    "user": "@jasongrout"
}
```

Attachment [5021.patch](tarball://root/attachments/some-uuid/ticket5021/5021.patch) by @jasongrout created at 2009-01-28 17:39:05

Looks good.  I tested a command from each package and it seemed to work great.  Positive review.



---

archive/issue_comments_038248.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T18:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5021#issuecomment-38248",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038249.json:
```json
{
    "body": "Moved in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T18:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5021#issuecomment-38249",
    "user": "mabshoff"
}
```

Moved in Sage 3.3.alpha3.

Cheers,

Michael
