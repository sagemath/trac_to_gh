# Issue 7798: Text in Plots at any given Function

archive/issues_007798.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot, label\n\nThe purpose of the ticket is to locate where the function text should be applied to the function plot to be able to have lables for plots like: var('x'); f = x**2; p = plot(f,x); p.text(\"hello\") for one function.\n\n------ not sure about this -------------\nTwo functions: g = x; p2 = plot(g,x); (g + f).text(\"eggs fro g\", g) where the string prints the label for g, while \"g\" prints label only for f.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7798\n\n",
    "created_at": "2009-12-31T00:56:07Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "Text in Plots at any given Function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7798",
    "user": "slosoi"
}
```
Assignee: was

Keywords: plot, label

The purpose of the ticket is to locate where the function text should be applied to the function plot to be able to have lables for plots like: var('x'); f = x**2; p = plot(f,x); p.text("hello") for one function.

------ not sure about this -------------
Two functions: g = x; p2 = plot(g,x); (g + f).text("eggs fro g", g) where the string prints the label for g, while "g" prints label only for f.

Issue created by migration from https://trac.sagemath.org/ticket/7798





---

archive/issue_comments_067474.json:
```json
{
    "body": "Attachment\n\nNot working attempt: trying to get some text initially to the plot",
    "created_at": "2009-12-31T01:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67474",
    "user": "slosoi"
}
```

Attachment

Not working attempt: trying to get some text initially to the plot



---

archive/issue_comments_067475.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-31T01:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67475",
    "user": "slosoi"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_067476.json:
```json
{
    "body": "To recompute line first to get coordinates right",
    "created_at": "2009-12-31T23:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67476",
    "user": "slosoi"
}
```

To recompute line first to get coordinates right



---

archive/issue_comments_067477.json:
```json
{
    "body": "Attachment\n\nI get the error in running the patch. There is somewhere a bug which prevents the loading of the module.",
    "created_at": "2009-12-31T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67477",
    "user": "slosoi"
}
```

Attachment

I get the error in running the patch. There is somewhere a bug which prevents the loading of the module.



---

archive/issue_comments_067478.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-31T23:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67478",
    "user": "slosoi"
}
```

Attachment



---

archive/issue_comments_067479.json:
```json
{
    "body": "Changing keywords from \"plot, label\" to \"axes, range\".",
    "created_at": "2010-01-02T04:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67479",
    "user": "slosoi"
}
```

Changing keywords from "plot, label" to "axes, range".



---

archive/issue_comments_067480.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67480",
    "user": "jason"
}
```

Changing type from defect to enhancement.
