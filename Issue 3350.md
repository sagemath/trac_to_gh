# Issue 3350: plot_vector_field error

archive/issues_003350.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: plot_vector_field, plot\n\nSometimes functions in plot_vector_field are evaluated on the wrong argument somehow:\n\nSubject: Re: plot directional field differential equations\nFrom: Georg Muntingh <georg.munti...`@`gmail.com>\nTo: sage-support <sage-support`@`googlegroups.com>\n\nYou can use the plot_vector_field command:\n# Declare your variables:\nvar('x t')\n# Define you function, for instance:\ndef f(t,x):\n    return t*x\nThere seems to be something awry, however, compare\nplot_vector_field((lambda t, x: 1, x), (-1, 1), (-2, 2))\nplot_vector_field((lambda t, x: 1, x + 0.001*t), (-1, 1), (-2, 2))\n(the second one is what one expects for the differential equation x' =\nx)\n\nWhy does the vector field look so different when it depends only on one coordinate?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3350\n\n",
    "created_at": "2008-06-02T12:49:28Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "plot_vector_field error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: plot_vector_field, plot

Sometimes functions in plot_vector_field are evaluated on the wrong argument somehow:

Subject: Re: plot directional field differential equations
From: Georg Muntingh <georg.munti...`@`gmail.com>
To: sage-support <sage-support`@`googlegroups.com>

You can use the plot_vector_field command:
# Declare your variables:
var('x t')
# Define you function, for instance:
def f(t,x):
    return t*x
There seems to be something awry, however, compare
plot_vector_field((lambda t, x: 1, x), (-1, 1), (-2, 2))
plot_vector_field((lambda t, x: 1, x + 0.001*t), (-1, 1), (-2, 2))
(the second one is what one expects for the differential equation x' =
x)

Why does the vector field look so different when it depends only on one coordinate?

Issue created by migration from https://trac.sagemath.org/ticket/3350





---

archive/issue_comments_023239.json:
```json
{
    "body": "Someone else should take a look at this, I've given it some thought and can't figure it out.\n\nThe syntax on the above examples is wrong, I think, but does not account for the problem.  For example, even:\n\n```\nplot_vector_field((lambda x,t: 1, lambda x,t: x), (-1, 1), (-2, 2))\n```\nwhich seems safer, still gives the wrong result, as does\n\n```\nvar('x,t')\nplot_vector_field((1, x), (-1, 1), (-2, 2))\n```",
    "created_at": "2008-10-16T15:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Someone else should take a look at this, I've given it some thought and can't figure it out.

The syntax on the above examples is wrong, I think, but does not account for the problem.  For example, even:

```
plot_vector_field((lambda x,t: 1, lambda x,t: x), (-1, 1), (-2, 2))
```
which seems safer, still gives the wrong result, as does

```
var('x,t')
plot_vector_field((1, x), (-1, 1), (-2, 2))
```



---

archive/issue_comments_023240.json:
```json
{
    "body": "Changing assignee from mhampton to somebody.",
    "created_at": "2008-10-16T15:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to somebody.



---

archive/issue_comments_023241.json:
```json
{
    "body": "In your second example, it is impossible to tell which variable is which (i.e., which is the horizontal axis, which is the vertical).  Specify it by doing:\n\n```\nvar('x,t')\nplot_vector_field((1, x), (x,-1, 1), (t,-2, 2))\n```\n\nWhat is wrong about the result?  I get the correct result on my computer.  Of course, to make the slope actually look like a slope of -1, you need to change the aspect_ratio:\n\n```\nvar('x,t')\nplot_vector_field((1, x), (-1, 1), (-2, 2)).show(aspect_ratio=1)\n```",
    "created_at": "2009-01-22T19:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23241",
    "user": "https://github.com/jasongrout"
}
```

In your second example, it is impossible to tell which variable is which (i.e., which is the horizontal axis, which is the vertical).  Specify it by doing:

```
var('x,t')
plot_vector_field((1, x), (x,-1, 1), (t,-2, 2))
```

What is wrong about the result?  I get the correct result on my computer.  Of course, to make the slope actually look like a slope of -1, you need to change the aspect_ratio:

```
var('x,t')
plot_vector_field((1, x), (-1, 1), (-2, 2)).show(aspect_ratio=1)
```



---

archive/issue_comments_023242.json:
```json
{
    "body": "You have the same problem of specifying variables in the example in the ticket description.\n\n\n\nHowever, currently the convention for choosing the variables is not very good, and the functions ought to be fast_float functions anyway.  I'll do those two things for this ticket.",
    "created_at": "2009-01-22T20:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23242",
    "user": "https://github.com/jasongrout"
}
```

You have the same problem of specifying variables in the example in the ticket description.



However, currently the convention for choosing the variables is not very good, and the functions ought to be fast_float functions anyway.  I'll do those two things for this ticket.



---

archive/issue_comments_023243.json:
```json
{
    "body": "I take that back; everything is fine and dandy for this function as far as variable selection and fast_float goes.  At least, it's consistent with all the other plotting functions.\n\nPlease, please, please, just like in all of the doc examples for plot_vector_field, specify the variables in the ranges, like (t, -3, 3).",
    "created_at": "2009-01-22T22:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23243",
    "user": "https://github.com/jasongrout"
}
```

I take that back; everything is fine and dandy for this function as far as variable selection and fast_float goes.  At least, it's consistent with all the other plotting functions.

Please, please, please, just like in all of the doc examples for plot_vector_field, specify the variables in the ranges, like (t, -3, 3).



---

archive/issue_comments_023244.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-22T22:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3350#issuecomment-23244",
    "user": "https://github.com/jasongrout"
}
```

Resolution: invalid



---

archive/issue_events_007501.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-01-22T22:43:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3350#event-7501"
}
```



---

archive/issue_events_007502.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:55:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3350",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3350#event-7502"
}
```
