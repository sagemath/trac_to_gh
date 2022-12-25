# Issue 150: if foo is a pyrex function then foo?? should give the source code

archive/issues_000150.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/150\n\n",
    "created_at": "2006-10-25T09:09:22Z",
    "labels": [
        "component: user interface"
    ],
    "title": "if foo is a pyrex function then foo?? should give the source code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/150",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/150





---

archive/issue_comments_000682.json:
```json
{
    "body": "OK, I created this just to mark it off. \n\nI solved this by adding a new option to Pyrex that embeds the source location\nin the generated Pyrex code.  I think modified IPython slightly, and finally\nwrote a new display of source hook that uses the embeded Pyrex info.\n\nIt works!\n\nFor SAGE-1.4.2",
    "created_at": "2006-10-25T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/150#issuecomment-682",
    "user": "https://github.com/williamstein"
}
```

OK, I created this just to mark it off. 

I solved this by adding a new option to Pyrex that embeds the source location
in the generated Pyrex code.  I think modified IPython slightly, and finally
wrote a new display of source hook that uses the embeded Pyrex info.

It works!

For SAGE-1.4.2



---

archive/issue_comments_000683.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-25T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/150#issuecomment-683",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
