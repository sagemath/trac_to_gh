# Issue 60: notebook cuts output of latex view

archive/issues_000060.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: notebook, latex\n\nThis may be related to ticket #38.\n\nEnter\n\nf = maxima(\"%e<sup>(k*x)+sin(b*x)+x</sup>3\")\n\ng = f.diff(\"x\")\n\nview(f)\n\nview(g)\n\ninto a cell and hit \"shift-enter\". Only the latexed\ndisplay of g is shown.\n\nIssue created by migration from https://trac.sagemath.org/ticket/60\n\n",
    "created_at": "2006-09-14T15:15:34Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "notebook cuts output of latex view",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/60",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: somebody

Keywords: notebook, latex

This may be related to ticket #38.

Enter

f = maxima("%e<sup>(k*x)+sin(b*x)+x</sup>3")

g = f.diff("x")

view(f)

view(g)

into a cell and hit "shift-enter". Only the latexed
display of g is shown.

Issue created by migration from https://trac.sagemath.org/ticket/60





---

archive/issue_comments_000315.json:
```json
{
    "body": "Currently, view() calls typeset() if EMBEDDED_MODE is True.  typeset() merely returns a string -- so if you want to see both f and g, \n\n\n```\n    f = maxima(\"%e(k*x)+sin(b*x)+x3\")\n    g = f.diff(\"x\")\n    print view(f)\n    print view(g)\n```\n\n\nPerhaps view() should print?",
    "created_at": "2006-09-14T18:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-315",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Currently, view() calls typeset() if EMBEDDED_MODE is True.  typeset() merely returns a string -- so if you want to see both f and g, 


```
    f = maxima("%e(k*x)+sin(b*x)+x3")
    g = f.diff("x")
    print view(f)
    print view(g)
```


Perhaps view() should print?



---

archive/issue_comments_000316.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2006-09-14T18:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-316",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000317.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2006-09-14T18:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-317",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_000318.json:
```json
{
    "body": "I definitely consider this a bug.",
    "created_at": "2006-09-15T18:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-318",
    "user": "https://github.com/williamstein"
}
```

I definitely consider this a bug.



---

archive/issue_comments_000319.json:
```json
{
    "body": "Fixed.  Changed start of view function in sage/misc/latex.py to the following:\n\n```\n    if EMBEDDED_MODE:\n        print typeset(objects)\n        return \n```\n",
    "created_at": "2006-10-15T17:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-319",
    "user": "https://github.com/williamstein"
}
```

Fixed.  Changed start of view function in sage/misc/latex.py to the following:

```
    if EMBEDDED_MODE:
        print typeset(objects)
        return 
```




---

archive/issue_comments_000320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T17:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/60",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/60#issuecomment-320",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
