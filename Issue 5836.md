# Issue 5836: Make show() immediately show an image in the notebook

archive/issues_005836.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nThe patch makes the cell containing:\n\n```\nshow(plot(x^2, (x, -2,2)))\nprint \"hi\"\n```\n\ndisplay the plot before printing \"hi\".  This makes it much easier to construct nice-looking output.\n\nWilliam should get author credit on this one as well as me, since he showed how it could be done in a demo.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5836\n\n",
    "created_at": "2009-04-20T18:30:27Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Make show() immediately show an image in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5836",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @williamstein

The patch makes the cell containing:

```
show(plot(x^2, (x, -2,2)))
print "hi"
```

display the plot before printing "hi".  This makes it much easier to construct nice-looking output.

William should get author credit on this one as well as me, since he showed how it could be done in a demo.

Issue created by migration from https://trac.sagemath.org/ticket/5836





---

archive/issue_comments_045774.json:
```json
{
    "body": "Well, unless William wants to review it.\n\nIn a sense, I reviewed his demo; I suppose he could review the actual patch.\n\nA note about the patch: sage.misc.misc was imported twice in plot.py.  I changed one of those imports to import the html function.",
    "created_at": "2009-04-20T18:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5836#issuecomment-45774",
    "user": "https://github.com/jasongrout"
}
```

Well, unless William wants to review it.

In a sense, I reviewed his demo; I suppose he could review the actual patch.

A note about the patch: sage.misc.misc was imported twice in plot.py.  I changed one of those imports to import the html function.



---

archive/issue_comments_045775.json:
```json
{
    "body": "Despite rumors to the contrary, there are several hundred doctests in the notebook directory, and your new code breaks two in cell.py, so post a patch that fixes those doctest breaks:\n\n\n```\nsage -t  devel/sage/sage/server/notebook/cell.py\n**********************************************************************\nFile \"/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py\", line 1751:\n    sage: W.check_comp(wait=9999)\nExpected:\n    ('d', Cell 0; in=plot(sin(x),0,5), out=\n    <BLANKLINE>\n    )\nGot:\n    ('d', Cell 0; in=plot(sin(x),0,5), out=\n    <html><font color='black'><img src='cell://sage0.png'></font></html>\n    <BLANKLINE>\n    )\n**********************************************************************\nFile \"/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py\", line 1777:\n    sage: W.check_comp(wait=9999)\nExpected:\n    ('d', Cell 0; in=plot(sin(x),0,5), out=\n    <BLANKLINE>\n    )\nGot:\n    ('d', Cell 0; in=plot(sin(x),0,5), out=\n    <html><font color='black'><img src='cell://sage0.png'></font></html>\n    <BLANKLINE>\n    )\n**********************************************************************\n2 items had failures:\n   1 of  10 in __main__.example_80\n\n```\n",
    "created_at": "2009-04-20T18:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5836#issuecomment-45775",
    "user": "https://github.com/williamstein"
}
```

Despite rumors to the contrary, there are several hundred doctests in the notebook directory, and your new code breaks two in cell.py, so post a patch that fixes those doctest breaks:


```
sage -t  devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py", line 1751:
    sage: W.check_comp(wait=9999)
Expected:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <BLANKLINE>
    )
Got:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <html><font color='black'><img src='cell://sage0.png'></font></html>
    <BLANKLINE>
    )
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/cell.py", line 1777:
    sage: W.check_comp(wait=9999)
Expected:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <BLANKLINE>
    )
Got:
    ('d', Cell 0; in=plot(sin(x),0,5), out=
    <html><font color='black'><img src='cell://sage0.png'></font></html>
    <BLANKLINE>
    )
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_80

```




---

archive/issue_comments_045776.json:
```json
{
    "body": "Attachment [trac-5836-show-html.patch](tarball://root/attachments/some-uuid/ticket5836/trac-5836-show-html.patch) by @jasongrout created at 2009-04-20 18:46:00\n\nPatch redone to correct the doctests.",
    "created_at": "2009-04-20T18:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5836#issuecomment-45776",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5836-show-html.patch](tarball://root/attachments/some-uuid/ticket5836/trac-5836-show-html.patch) by @jasongrout created at 2009-04-20 18:46:00

Patch redone to correct the doctests.



---

archive/issue_comments_045777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T07:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5836#issuecomment-45777",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045778.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T07:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5836#issuecomment-45778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
