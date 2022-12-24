# Issue 1441: latex(x1) -> x_1 might cause problems

archive/issues_001441.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider the following:\n\n```\nsage: var('x_1,x1');\nsage: x_1 - x1\nx_1 - x1\nsage: latex(x_1 - x1)\nx_{1} - x_{1}\n```\n\nThe automatic rule latex(x1) -> x_1 might thus cause ambiguities if both x1 and x_1 exist as\nvariables.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1441\n\n",
    "created_at": "2007-12-09T21:32:14Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "latex(x1) -> x_1 might cause problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1441",
    "user": "@zimmermann6"
}
```
Assignee: @williamstein

Consider the following:

```
sage: var('x_1,x1');
sage: x_1 - x1
x_1 - x1
sage: latex(x_1 - x1)
x_{1} - x_{1}
```

The automatic rule latex(x1) -> x_1 might thus cause ambiguities if both x1 and x_1 exist as
variables.

Issue created by migration from https://trac.sagemath.org/ticket/1441





---

archive/issue_comments_009299.json:
```json
{
    "body": "I can see no possible fix for this.  Suggest something.\nI mean, the only option I can think of would be for latex(x1) to be x1, which\nisn't even latex for a variable (since that's \"x times 1\").\n\nInvalid?",
    "created_at": "2007-12-15T23:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1441#issuecomment-9299",
    "user": "@williamstein"
}
```

I can see no possible fix for this.  Suggest something.
I mean, the only option I can think of would be for latex(x1) to be x1, which
isn't even latex for a variable (since that's "x times 1").

Invalid?



---

archive/issue_comments_009300.json:
```json
{
    "body": "Here is what Maple does:\n\n```\n> latex(x1);\n{\\it x1}\n> latex(x_1);\n{\\it x\\_1}\n```\n\nThis seems a reasonable alternative to me.",
    "created_at": "2007-12-17T12:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1441#issuecomment-9300",
    "user": "@zimmermann6"
}
```

Here is what Maple does:

```
> latex(x1);
{\it x1}
> latex(x_1);
{\it x\_1}
```

This seems a reasonable alternative to me.



---

archive/issue_comments_009301.json:
```json
{
    "body": "Joel Mohler also votes invalid.",
    "created_at": "2007-12-18T18:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1441#issuecomment-9301",
    "user": "@rlmill"
}
```

Joel Mohler also votes invalid.



---

archive/issue_comments_009302.json:
```json
{
    "body": "The translation x1 -> x_1 far outweight the potential ambiguity in my mind. However, perhaps a variable named \"x_1\" should actually be latexed as \"x\\_1\"",
    "created_at": "2007-12-19T03:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1441#issuecomment-9302",
    "user": "@robertwb"
}
```

The translation x1 -> x_1 far outweight the potential ambiguity in my mind. However, perhaps a variable named "x_1" should actually be latexed as "x\_1"



---

archive/issue_comments_009303.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-12-19T19:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1441#issuecomment-9303",
    "user": "@rlmill"
}
```

Resolution: invalid
