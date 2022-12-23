# Issue 7356: fixed latex representation for floats

archive/issues_007356.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nFloats have no LaTeX representation and are formated using str function. Thus output of latex(float(1e25)) is '1e+25' and not '1 \\times 10^{25}'. \n\nThe solution is to define function to handle this like the function below\n\n```\n\ndef float_function(x):\n    r\"\"\"\n    Returns the LaTeX code for a float ``x``.\n\n    INPUT: ``x`` - float number\n\n    EXAMPLES::\n\n        sage: from sage.misc.latex import float_function\n        sage: float_function(float(123.05))\n        '123.05'\n        sage: float_function(float(3e-15))\n        '3 \\\\times 10^{-15}'\n        sage: float_function(float(3.2e25))\n        '3.2 \\\\times 10^{25}'\n        sage: float_function(float(3.2e+15))\n        '3.2 \\\\times 10^{15}'\n\n        The output is in some cases shorter than latex method for real numbers.\n\n        sage: float_function(float(1e+15))\n        '1 \\\\times 10^{15}'\n    \"\"\"\n    s = str(x)\n    parts = s.split('e')\n    if len(parts) > 1:\n        # scientific notation\n        if parts[1][0] == '+':\n            parts[1] = parts[1][1:]\n        s = \"%s \\\\times 10^{%s}\" % (parts[0], parts[1])\n    return s\n```\n\n\nWill post simple patch, provided it passes tests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7356\n\n",
    "created_at": "2009-10-30T09:12:06Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "fixed latex representation for floats",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7356",
    "user": "robert.marik"
}
```
Assignee: AlexGhitza

Floats have no LaTeX representation and are formated using str function. Thus output of latex(float(1e25)) is '1e+25' and not '1 \times 10^{25}'. 

The solution is to define function to handle this like the function below

```

def float_function(x):
    r"""
    Returns the LaTeX code for a float ``x``.

    INPUT: ``x`` - float number

    EXAMPLES::

        sage: from sage.misc.latex import float_function
        sage: float_function(float(123.05))
        '123.05'
        sage: float_function(float(3e-15))
        '3 \\times 10^{-15}'
        sage: float_function(float(3.2e25))
        '3.2 \\times 10^{25}'
        sage: float_function(float(3.2e+15))
        '3.2 \\times 10^{15}'

        The output is in some cases shorter than latex method for real numbers.

        sage: float_function(float(1e+15))
        '1 \\times 10^{15}'
    """
    s = str(x)
    parts = s.split('e')
    if len(parts) > 1:
        # scientific notation
        if parts[1][0] == '+':
            parts[1] = parts[1][1:]
        s = "%s \\times 10^{%s}" % (parts[0], parts[1])
    return s
```


Will post simple patch, provided it passes tests.

Issue created by migration from https://trac.sagemath.org/ticket/7356





---

archive/issue_comments_061634.json:
```json
{
    "body": "Attachment\n\nThe patch for 4.2 is attached. When running tests I got two errors not related to the change in this trac. The first one is solved in #6479.\n\n\n```\nsage -t  \"devel/sage/sage/calculus/desolvers.py\"\nsage -t  \"devel/sage/sage/interfaces/maxima.py\"\n```\n",
    "created_at": "2009-10-30T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61634",
    "user": "robert.marik"
}
```

Attachment

The patch for 4.2 is attached. When running tests I got two errors not related to the change in this trac. The first one is solved in #6479.


```
sage -t  "devel/sage/sage/calculus/desolvers.py"
sage -t  "devel/sage/sage/interfaces/maxima.py"
```




---

archive/issue_comments_061635.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-30T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61635",
    "user": "robert.marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061636.json:
```json
{
    "body": "\n```\nsage -t  \"devel/sage/sage/interfaces/maxima.py\"\n```\n\nThis test passed as well. (Error has been introduced by my custom settings in maxima-init.lisp file)",
    "created_at": "2009-10-30T11:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61636",
    "user": "robert.marik"
}
```


```
sage -t  "devel/sage/sage/interfaces/maxima.py"
```

This test passed as well. (Error has been introduced by my custom settings in maxima-init.lisp file)



---

archive/issue_comments_061637.json:
```json
{
    "body": "According to [this](http://groups.google.cz/group/sage-devel/browse_thread/thread/67657d52cbc5a915) thread, there is another patch for this with slightly different output: #7328",
    "created_at": "2009-10-30T14:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61637",
    "user": "robert.marik"
}
```

According to [this](http://groups.google.cz/group/sage-devel/browse_thread/thread/67657d52cbc5a915) thread, there is another patch for this with slightly different output: #7328



---

archive/issue_comments_061638.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-06T06:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61638",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_061639.json:
```json
{
    "body": "Should this be closed as a duplicate since #7328 has been closed with a positive review?",
    "created_at": "2009-11-06T06:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61639",
    "user": "jhpalmieri"
}
```

Should this be closed as a duplicate since #7328 has been closed with a positive review?



---

archive/issue_comments_061640.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Should this be closed as a duplicate since #7328 has been closed with a positive review?\n\nPerhaps yes, but the patch in this trac produces shorter output, so I think that this is better. The patch #7328 produces sometimes zeros which are not necessary at the end of decimal number.",
    "created_at": "2009-11-07T21:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61640",
    "user": "robert.marik"
}
```

Replying to [comment:4 jhpalmieri]:
> Should this be closed as a duplicate since #7328 has been closed with a positive review?

Perhaps yes, but the patch in this trac produces shorter output, so I think that this is better. The patch #7328 produces sometimes zeros which are not necessary at the end of decimal number.



---

archive/issue_comments_061641.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-11-20T05:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61641",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_061642.json:
```json
{
    "body": "Attachment\n\nUse instead of other, applies on top of #7328",
    "created_at": "2009-11-20T05:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61642",
    "user": "robertwb"
}
```

Attachment

Use instead of other, applies on top of #7328



---

archive/issue_comments_061643.json:
```json
{
    "body": "I agree, less digits should be printed. Floats are more like RDF than RR, so I've posted a patch that applies on top of #7328. The attached patch works fine to (though will conflict with 4.2.1).",
    "created_at": "2009-11-20T05:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61643",
    "user": "robertwb"
}
```

I agree, less digits should be printed. Floats are more like RDF than RR, so I've posted a patch that applies on top of #7328. The attached patch works fine to (though will conflict with 4.2.1).



---

archive/issue_comments_061644.json:
```json
{
    "body": "Attachment\n\napply on top of latex-float-4.2.1.patch",
    "created_at": "2009-11-20T07:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61644",
    "user": "robert.marik"
}
```

Attachment

apply on top of latex-float-4.2.1.patch



---

archive/issue_comments_061645.json:
```json
{
    "body": "Seems good, thanks for fixing. Since one test failed, I fixed it in reviewers patch which should be installed on the top of latex-float-4.2.1.patch  \n\nTests are O.K. now. Positive review.",
    "created_at": "2009-11-20T07:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61645",
    "user": "robert.marik"
}
```

Seems good, thanks for fixing. Since one test failed, I fixed it in reviewers patch which should be installed on the top of latex-float-4.2.1.patch  

Tests are O.K. now. Positive review.



---

archive/issue_comments_061646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-20T07:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61646",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-22T07:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7356#issuecomment-61647",
    "user": "mhansen"
}
```

Resolution: fixed
