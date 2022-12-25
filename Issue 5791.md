# Issue 5791: Allow custom packages to be injected or %latex and the Sage latex mode

archive/issues_005791.json:
```json
{
    "body": "Assignee: cwitty\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/39f1d0e71eae2453 for the discussion: It would be great of one could add packages that are automatically included when running LaTeX, i.e. for commutative diagrams.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5791\n\n",
    "created_at": "2009-04-15T06:55:56Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Allow custom packages to be injected or %latex and the Sage latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

See http://groups.google.com/group/sage-devel/browse_thread/thread/39f1d0e71eae2453 for the discussion: It would be great of one could add packages that are automatically included when running LaTeX, i.e. for commutative diagrams.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5791





---

archive/issue_comments_045265.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45265",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045266.json:
```json
{
    "body": "Here's an attempt at this.  To use it:\n\n```\nsage: latex.add_macro('\\\\newcommand{\\\\foo}{bar}')\n```\n\nand then a %latex cell with \\\\foo in it will be processed correctly, as will %jsmath and %html cells.  Also,\n\n```\nsage: latex.add_to_preamble('\\\\usepackage{blah}')\n```\n\nwill do what it says; it should only have an effect on %latex cells.\n\n(In this patch, \"macros\" are things which are processed by latex and jsmath, while the \"preamble\" is only passed to latex.  For both categories, you can add to the current string with latex.add_macro or latex.add_preamble, or you can replace it with latex.extra_macros or latex.extra_preamble.)\n\nSome pictures are [here](http://sage.math.washington.edu/home/palmieri/misc/foobar.png) and [here](http://sage.math.washington.edu/home/palmieri/misc/ext.png).\n\nAnyway, please test it out; the patch is against 3.4.2.alpha0.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45266",
    "user": "https://github.com/jhpalmieri"
}
```

Here's an attempt at this.  To use it:

```
sage: latex.add_macro('\\newcommand{\\foo}{bar}')
```

and then a %latex cell with \\foo in it will be processed correctly, as will %jsmath and %html cells.  Also,

```
sage: latex.add_to_preamble('\\usepackage{blah}')
```

will do what it says; it should only have an effect on %latex cells.

(In this patch, "macros" are things which are processed by latex and jsmath, while the "preamble" is only passed to latex.  For both categories, you can add to the current string with latex.add_macro or latex.add_preamble, or you can replace it with latex.extra_macros or latex.extra_preamble.)

Some pictures are [here](http://sage.math.washington.edu/home/palmieri/misc/foobar.png) and [here](http://sage.math.washington.edu/home/palmieri/misc/ext.png).

Anyway, please test it out; the patch is against 3.4.2.alpha0.



---

archive/issue_comments_045267.json:
```json
{
    "body": "Changing assignee from cwitty to @jhpalmieri.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45267",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from cwitty to @jhpalmieri.



---

archive/issue_comments_045268.json:
```json
{
    "body": "Attachment [latex-5791.patch](tarball://root/attachments/some-uuid/ticket5791/latex-5791.patch) by @rbeezer created at 2009-04-25 04:47:11\n\nPasses tests on misc/latex.py and misc/latex_macros.py in 3.4.2.alpha0, and works as advertised at command-line and in notebook.\n\nPDF version of documentation builds fine also.  Another great addition to Sage-LaTeX integration.\n\nSo this is ready to go - positive review.",
    "created_at": "2009-04-25T04:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45268",
    "user": "https://github.com/rbeezer"
}
```

Attachment [latex-5791.patch](tarball://root/attachments/some-uuid/ticket5791/latex-5791.patch) by @rbeezer created at 2009-04-25 04:47:11

Passes tests on misc/latex.py and misc/latex_macros.py in 3.4.2.alpha0, and works as advertised at command-line and in notebook.

PDF version of documentation builds fine also.  Another great addition to Sage-LaTeX integration.

So this is ready to go - positive review.



---

archive/issue_events_013588.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T04:09:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5791#event-13588"
}
```



---

archive/issue_events_013589.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T04:09:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5791#event-13589"
}
```



---

archive/issue_comments_045269.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45269",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45270",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
