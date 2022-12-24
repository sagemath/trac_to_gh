# Issue 683: bug in "latex?" in the notebook

archive/issues_000683.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n     --  The response to `latex?' seems to be out of date.\n\n            %latex\n            The equation y^2 = x^3 + x defines an elliptic curve.\n            We have 2006 = SAGE{factor(2006)}.\n\n    I thought it was a great credit to SAGE that when I edited the sample input\n    in what seemed the obvious way, enclosing the math in $$ and changing SAGE\n    to \\sage, that it worked as expected.\n\n```\n\n\n\n\n\nAh, you've found a bug.  What happens is that all SAGE documentation\nis de-texed before displaying in the notebook (in plain text format).  Unfortunately\nthis detexing makes the documentation for latex appear completely\nwrong!  \n\nThe solution is probably to come up with a notation to tell SAGE not\nto do the detexing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/683\n\n",
    "created_at": "2007-09-17T21:52:21Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "bug in \"latex?\" in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/683",
    "user": "was"
}
```
Assignee: boothby


```
     --  The response to `latex?' seems to be out of date.

            %latex
            The equation y^2 = x^3 + x defines an elliptic curve.
            We have 2006 = SAGE{factor(2006)}.

    I thought it was a great credit to SAGE that when I edited the sample input
    in what seemed the obvious way, enclosing the math in $$ and changing SAGE
    to \sage, that it worked as expected.

```





Ah, you've found a bug.  What happens is that all SAGE documentation
is de-texed before displaying in the notebook (in plain text format).  Unfortunately
this detexing makes the documentation for latex appear completely
wrong!  

The solution is probably to come up with a notation to tell SAGE not
to do the detexing. 

Issue created by migration from https://trac.sagemath.org/ticket/683





---

archive/issue_comments_003543.json:
```json
{
    "body": "Attachment [683-989-ncalexan-1.patch](tarball://root/attachments/some-uuid/ticket683/683-989-ncalexan-1.patch) by ncalexan created at 2007-11-04 07:32:49",
    "created_at": "2007-11-04T07:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/683#issuecomment-3543",
    "user": "ncalexan"
}
```

Attachment [683-989-ncalexan-1.patch](tarball://root/attachments/some-uuid/ticket683/683-989-ncalexan-1.patch) by ncalexan created at 2007-11-04 07:32:49



---

archive/issue_comments_003544.json:
```json
{
    "body": "683,989: add 'nodetex' directive to docstrings: doesn't strip (la)tex code from docstrings.\n\nThe first line of a docstring is parsed as a comma-separated list of\ndirectives (no whitespace in directives!).  For example:\n\n\n```\nr\"\"\"nodetex,notyetimplemented\n...\n\"\"\"\n```\n\n\nIf 'nodetex' is one of the directives, then no (la)tex code is stripped from\nthe docstring.  The model was the 'nodoctest' directive already found at the\ntop of a file.",
    "created_at": "2007-11-04T07:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/683#issuecomment-3544",
    "user": "ncalexan"
}
```

683,989: add 'nodetex' directive to docstrings: doesn't strip (la)tex code from docstrings.

The first line of a docstring is parsed as a comma-separated list of
directives (no whitespace in directives!).  For example:


```
r"""nodetex,notyetimplemented
...
"""
```


If 'nodetex' is one of the directives, then no (la)tex code is stripped from
the docstring.  The model was the 'nodoctest' directive already found at the
top of a file.



---

archive/issue_comments_003545.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/683#issuecomment-3545",
    "user": "mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_comments_003546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/683#issuecomment-3546",
    "user": "mabshoff"
}
```

Resolution: fixed
