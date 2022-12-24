# Issue 8503: broken multiline input in sage notebook

archive/issues_008503.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @fchapoton\n\nMultiline input like\n\n```\n8+\\\n2\n```\n\nwhich works in command line does not work in notebook and returns error.\n\nJason at [sage-notebook](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9ee2472e1857edcb) wrote\n\n```\nDoes it have to do with the preparser?  Note:\n\nsage: preparse(\"1+\\\\n2\")\n'Integer(1)+ * BackslashOperator() * n2'\n\nMaybe on the command line, ipython joins the two lines before the\npreparser gets to it, but that doesn't happen in the notebook? \n```\n\n\nAnd further:\n\n```\nplot(x,\\\n(x,-2,2))\n```\n\ndoes not produce the plot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8503\n\n",
    "created_at": "2010-03-11T23:20:44Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "broken multiline input in sage notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8503",
    "user": "@robert-marik"
}
```
Assignee: @williamstein

CC:  @fchapoton

Multiline input like

```
8+\
2
```

which works in command line does not work in notebook and returns error.

Jason at [sage-notebook](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9ee2472e1857edcb) wrote

```
Does it have to do with the preparser?  Note:

sage: preparse("1+\\n2")
'Integer(1)+ * BackslashOperator() * n2'

Maybe on the command line, ipython joins the two lines before the
preparser gets to it, but that doesn't happen in the notebook? 
```


And further:

```
plot(x,\
(x,-2,2))
```

does not produce the plot.

Issue created by migration from https://trac.sagemath.org/ticket/8503





---

archive/issue_comments_076776.json:
```json
{
    "body": "Not the preparser.  For some reason, about the time this was reported, someone added `sage` and `python` to this list in `sagenb/notebook/worksheet.py`.\n\n```\n #Handle line continuations: join lines that end in a backslash\n#_except_ in LaTeX mode.\nif cell_system not in ['latex', 'sage', 'python']:\nI = I.replace('\\\\\\n','')\n```\n\nNote from Robert's email\n\n```\n\nA=solve(\\\nsin(x),\\\nx)\nA\n```\n\n\n```\nplot(x,\\\n(x,-2,\\\n2)).show()\n```\n\nboth work.\n\nSee https://github.com/sagemath/sagenb/issues/301",
    "created_at": "2014-12-10T21:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8503#issuecomment-76776",
    "user": "@kcrisman"
}
```

Not the preparser.  For some reason, about the time this was reported, someone added `sage` and `python` to this list in `sagenb/notebook/worksheet.py`.

```
 #Handle line continuations: join lines that end in a backslash
#_except_ in LaTeX mode.
if cell_system not in ['latex', 'sage', 'python']:
I = I.replace('\\\n','')
```

Note from Robert's email

```

A=solve(\
sin(x),\
x)
A
```


```
plot(x,\
(x,-2,\
2)).show()
```

both work.

See https://github.com/sagemath/sagenb/issues/301



---

archive/issue_comments_076777.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8503#issuecomment-76777",
    "user": "@mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_076778.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8503#issuecomment-76778",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076779.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-03T08:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8503#issuecomment-76779",
    "user": "@fchapoton"
}
```

Resolution: invalid
