# Issue 9048: different behaviour of var in notebook and text version

archive/issues_009048.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  eocansey@risc.jku.at\n\nIn the text version of Sage, `var('x');` does not print anything.\nHowever, in the notebook, it prints `x`, even with the `;`\nthat should prevent output. This is quite annoying. Is there a reason for that?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9048\n\n",
    "created_at": "2010-05-25T19:59:01Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "different behaviour of var in notebook and text version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9048",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: jason, was

CC:  eocansey@risc.jku.at

In the text version of Sage, `var('x');` does not print anything.
However, in the notebook, it prints `x`, even with the `;`
that should prevent output. This is quite annoying. Is there a reason for that?

Issue created by migration from https://trac.sagemath.org/ticket/9048





---

archive/issue_comments_083634.json:
```json
{
    "body": "Changed the title to identify the underlying issue.  Note that 1+2; also prints out something in the notebook, but not in the command line.\n\nMy guess is that it is a convention in ipython, since a semicolon does nothing in just plain python:\n\n\n```\n% sage -python\nPython 2.6.4 (r264:75706, May  6 2010, 23:38:46) \n[GCC 4.2.1 (Apple Inc. build 5659)] on darwin\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> 1+2;\n3\n\n\n```\n",
    "created_at": "2010-05-26T03:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83634",
    "user": "https://github.com/jasongrout"
}
```

Changed the title to identify the underlying issue.  Note that 1+2; also prints out something in the notebook, but not in the command line.

My guess is that it is a convention in ipython, since a semicolon does nothing in just plain python:


```
% sage -python
Python 2.6.4 (r264:75706, May  6 2010, 23:38:46) 
[GCC 4.2.1 (Apple Inc. build 5659)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+2;
3


```




---

archive/issue_events_022159.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22159"
}
```



---

archive/issue_comments_083635.json:
```json
{
    "body": "note sure what to do with this ticket. At least we can try to list all inconsistencies between the terminal version and the notebook:\n\n* `1+2;` does not print anything in the terminal version, but does print something in the notebook\n\n* `__` and `____` do not work in the notebook\n\n* `automatic_names` does not work in the terminal version\n\nAre there any other differences?\n\nPaul",
    "created_at": "2013-08-24T12:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83635",
    "user": "https://github.com/zimmermann6"
}
```

note sure what to do with this ticket. At least we can try to list all inconsistencies between the terminal version and the notebook:

* `1+2;` does not print anything in the terminal version, but does print something in the notebook

* `__` and `____` do not work in the notebook

* `automatic_names` does not work in the terminal version

Are there any other differences?

Paul



---

archive/issue_comments_083636.json:
```json
{
    "body": "Replying to [comment:3 zimmerma]:\n> * `1+2;` does not print anything in the terminal version, but does print something in the notebook\nThe printing in the notebook is a little more different than just that:\n\n```\n1;2;\n```\n\nprints\n\n```\n1\n2\n```\n\nwhereas\n\n```\n1\n2\n```\n\nprints\n\n```\n2\n```\n\nand\n\n```\n(1\n)\n```\n\nprints nothing, whereas\n\n```\n(1)\n```\n\nprints\n\n```\n1\n```\n\ni.e., it seems that all results from statements contained entirely on the last line of the cell are printed, regardless of semicolons, and no other results are. To me this seems a little arbitrary, but resolving this is probably something for the notebook.",
    "created_at": "2013-08-24T17:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83636",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:3 zimmerma]:
> * `1+2;` does not print anything in the terminal version, but does print something in the notebook
The printing in the notebook is a little more different than just that:

```
1;2;
```

prints

```
1
2
```

whereas

```
1
2
```

prints

```
2
```

and

```
(1
)
```

prints nothing, whereas

```
(1)
```

prints

```
1
```

i.e., it seems that all results from statements contained entirely on the last line of the cell are printed, regardless of semicolons, and no other results are. To me this seems a little arbitrary, but resolving this is probably something for the notebook.



---

archive/issue_events_022160.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22160"
}
```



---

archive/issue_events_022161.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22161"
}
```



---

archive/issue_events_022162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22162"
}
```



---

archive/issue_events_022163.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22163"
}
```



---

archive/issue_events_022164.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22164"
}
```



---

archive/issue_events_022165.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22165"
}
```



---

archive/issue_comments_083637.json:
```json
{
    "body": "I've added `automatic_names` in the description as a reminder, since we write in our book about Sage (which is currently being translated to english) that `automatic_names` does not work in the terminal version.",
    "created_at": "2017-03-06T20:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83637",
    "user": "https://github.com/zimmermann6"
}
```

I've added `automatic_names` in the description as a reminder, since we write in our book about Sage (which is currently being translated to english) that `automatic_names` does not work in the terminal version.



---

archive/issue_events_022166.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-07-14T09:20:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22166"
}
```



---

archive/issue_events_022167.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-07-14T09:20:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9048#event-22167"
}
```



---

archive/issue_comments_083638.json:
```json
{
    "body": "automatic_names also doesn't work in the Jupyter Notebook. This was also discussed in #25837. I looked into this a bit \u00e0 year ago, and it turns out the `automatic_names` implementation lives in sagenb. It needs to be moved into the main sage package, and will take some adjusting to integrate into the IPython terminal and Jupyter kernel interfaces.",
    "created_at": "2019-07-14T09:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83638",
    "user": "https://github.com/embray"
}
```

automatic_names also doesn't work in the Jupyter Notebook. This was also discussed in #25837. I looked into this a bit à year ago, and it turns out the `automatic_names` implementation lives in sagenb. It needs to be moved into the main sage package, and will take some adjusting to integrate into the IPython terminal and Jupyter kernel interfaces.



---

archive/issue_comments_083639.json:
```json
{
    "body": "I thought I also made a ticket specifically for this issue but I can't find it now, so maybe this is just the one.",
    "created_at": "2019-07-14T09:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83639",
    "user": "https://github.com/embray"
}
```

I thought I also made a ticket specifically for this issue but I can't find it now, so maybe this is just the one.



---

archive/issue_comments_083640.json:
```json
{
    "body": "I've created #29888 for automatic_names in Jupyter.\n\nThis ticket can still be about differences between the terminal and Jupyter notebook, but probably should be updated for differences between that one and the terminal, not the sagenb and terminal.",
    "created_at": "2020-06-17T18:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9048#issuecomment-83640",
    "user": "https://github.com/kcrisman"
}
```

I've created #29888 for automatic_names in Jupyter.

This ticket can still be about differences between the terminal and Jupyter notebook, but probably should be updated for differences between that one and the terminal, not the sagenb and terminal.
