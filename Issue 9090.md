# Issue 9090: Interactive matrix_viewer(...)

archive/issues_009090.json:
```json
{
    "body": "Assignee: acleone\n\nCC:  acleone\n\nAdds an interactive matrix viewer to the notebook.\n\nRequires: #8758\n\nIssue created by migration from https://trac.sagemath.org/ticket/9090\n\n",
    "created_at": "2010-05-29T22:52:27Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Interactive matrix_viewer(...)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9090",
    "user": "acleone"
}
```
Assignee: acleone

CC:  acleone

Adds an interactive matrix viewer to the notebook.

Requires: #8758

Issue created by migration from https://trac.sagemath.org/ticket/9090





---

archive/issue_comments_084434.json:
```json
{
    "body": "What is an \"interactive matrix viewer\"?",
    "created_at": "2017-07-04T13:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9090#issuecomment-84434",
    "user": "jdemeyer"
}
```

What is an "interactive matrix viewer"?



---

archive/issue_comments_084435.json:
```json
{
    "body": "My guess is that this might be something that allows easy input of a matrix, as with the `graph_editor`?  That would certainly be useful (in TeXShop I use something analogous all the time to relieve the tedium of typing in LaTeX matrices).  Don't know for sure, though.",
    "created_at": "2017-07-05T15:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9090#issuecomment-84435",
    "user": "kcrisman"
}
```

My guess is that this might be something that allows easy input of a matrix, as with the `graph_editor`?  That would certainly be useful (in TeXShop I use something analogous all the time to relieve the tedium of typing in LaTeX matrices).  Don't know for sure, though.



---

archive/issue_comments_084436.json:
```json
{
    "body": "Well, we have `input_grid` (both in SageNB and Jupyter) which can do this. The only potential caveat is that the size is fixed: you need to specify the number of rows and columns in advance.",
    "created_at": "2017-07-05T15:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9090#issuecomment-84436",
    "user": "jdemeyer"
}
```

Well, we have `input_grid` (both in SageNB and Jupyter) which can do this. The only potential caveat is that the size is fixed: you need to specify the number of rows and columns in advance.



---

archive/issue_comments_084437.json:
```json
{
    "body": "In interacts, yes? Maybe this was originally opened to allow this outside of interacts ... honestly I don't know, but your caveat sounds like a reasonable goal for this ticket.",
    "created_at": "2017-07-05T16:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9090#issuecomment-84437",
    "user": "kcrisman"
}
```

In interacts, yes? Maybe this was originally opened to allow this outside of interacts ... honestly I don't know, but your caveat sounds like a reasonable goal for this ticket.



---

archive/issue_comments_084438.json:
```json
{
    "body": "Right... the thing with Jupyter widgets is that one can use the widgets without interacts. Essentially ``@`interact` is built up from widgets, for example setting up the auto-evaluation when a widget changes.\n\nWith SageNB on the other hand, controls (the SageNB term for widgets) cannot live by themselves. They require ``@`interact` to be used.",
    "created_at": "2017-07-06T09:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9090#issuecomment-84438",
    "user": "jdemeyer"
}
```

Right... the thing with Jupyter widgets is that one can use the widgets without interacts. Essentially ``@`interact` is built up from widgets, for example setting up the auto-evaluation when a widget changes.

With SageNB on the other hand, controls (the SageNB term for widgets) cannot live by themselves. They require ``@`interact` to be used.
