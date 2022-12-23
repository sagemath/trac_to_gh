# Issue 8842: sage notebook interacts: format exceptions nicely

archive/issues_008842.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  chapoton\n\n\n```\nIf I write a function in a cell of a notebook like:\n\n@interact\ndef foo(a = input_box(default=0, type=Integer)):\n    # do something here\n    pass\n\nAnd the user enters something that cannot be coerced to Integer, then\nI get a verbose (and rather unhelpful) exception, which, as far as I\ncan see, can't be caught inside of foo.  So, I would suggest that if a\ntype is specified in input_box, and the coercion fails that a nicer\nlooking message be given (perhaps next to the box that a specifies).\n\nVictor\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8842\n\n",
    "created_at": "2010-05-02T20:20:35Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "sage notebook interacts: format exceptions nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8842",
    "user": "was"
}
```
Assignee: jason, was

CC:  chapoton


```
If I write a function in a cell of a notebook like:

@interact
def foo(a = input_box(default=0, type=Integer)):
    # do something here
    pass

And the user enters something that cannot be coerced to Integer, then
I get a verbose (and rather unhelpful) exception, which, as far as I
can see, can't be caught inside of foo.  So, I would suggest that if a
type is specified in input_box, and the coercion fails that a nicer
looking message be given (perhaps next to the box that a specifies).

Victor
```


Issue created by migration from https://trac.sagemath.org/ticket/8842





---

archive/issue_comments_081289.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8842#issuecomment-81289",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_081290.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8842#issuecomment-81290",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081291.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-09T09:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8842#issuecomment-81291",
    "user": "chapoton"
}
```

Resolution: invalid
