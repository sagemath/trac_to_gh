# Issue 5791: Allow custom packages to be injected or %latex and the Sage latex mode

archive/issues_005791.json:
```json
{
    "body": "Assignee: cwitty\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/39f1d0e71eae2453 for the discussion: It would be great of one could add packages that are automatically included when running LaTeX, i.e. for commutative diagrams.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5791\n\n",
    "created_at": "2009-04-15T06:55:56Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "Allow custom packages to be injected or %latex and the Sage latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5791",
    "user": "mabshoff"
}
```
Assignee: cwitty

See http://groups.google.com/group/sage-devel/browse_thread/thread/39f1d0e71eae2453 for the discussion: It would be great of one could add packages that are automatically included when running LaTeX, i.e. for commutative diagrams.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5791





---

archive/issue_comments_045351.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45351",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045352.json:
```json
{
    "body": "Here's an attempt at this.  To use it:\n\n```\nsage: latex.add_macro('\\\\newcommand{\\\\foo}{bar}')\n```\n\nand then a %latex cell with \\\\foo in it will be processed correctly, as will %jsmath and %html cells.  Also,\n\n```\nsage: latex.add_to_preamble('\\\\usepackage{blah}')\n```\n\nwill do what it says; it should only have an effect on %latex cells.\n\n(In this patch, \"macros\" are things which are processed by latex and jsmath, while the \"preamble\" is only passed to latex.  For both categories, you can add to the current string with latex.add_macro or latex.add_preamble, or you can replace it with latex.extra_macros or latex.extra_preamble.)\n\nSome pictures are [here](http://sage.math.washington.edu/home/palmieri/misc/foobar.png) and [here](http://sage.math.washington.edu/home/palmieri/misc/ext.png).\n\nAnyway, please test it out; the patch is against 3.4.2.alpha0.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45352",
    "user": "jhpalmieri"
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

archive/issue_comments_045353.json:
```json
{
    "body": "Changing assignee from cwitty to jhpalmieri.",
    "created_at": "2009-04-24T20:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45353",
    "user": "jhpalmieri"
}
```

Changing assignee from cwitty to jhpalmieri.



---

archive/issue_comments_045354.json:
```json
{
    "body": "Attachment [latex-5791.patch](tarball://root/attachments/some-uuid/ticket5791/latex-5791.patch) by rbeezer created at 2009-04-25 04:47:11\n\nPasses tests on misc/latex.py and misc/latex_macros.py in 3.4.2.alpha0, and works as advertised at command-line and in notebook.\n\nPDF version of documentation builds fine also.  Another great addition to Sage-LaTeX integration.\n\nSo this is ready to go - positive review.",
    "created_at": "2009-04-25T04:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45354",
    "user": "rbeezer"
}
```

Attachment [latex-5791.patch](tarball://root/attachments/some-uuid/ticket5791/latex-5791.patch) by rbeezer created at 2009-04-25 04:47:11

Passes tests on misc/latex.py and misc/latex_macros.py in 3.4.2.alpha0, and works as advertised at command-line and in notebook.

PDF version of documentation builds fine also.  Another great addition to Sage-LaTeX integration.

So this is ready to go - positive review.



---

archive/issue_comments_045355.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45355",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5791#issuecomment-45356",
    "user": "mabshoff"
}
```

Resolution: fixed
