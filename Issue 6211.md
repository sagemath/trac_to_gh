# Issue 6211: typesetting symbolic integrals broken

archive/issues_006211.json:
```json
{
    "body": "CC:  mhansen\n\nReported by Ricardo on sage-support:\n\n\n```\nI had installed sage 3.4.1 in my Ubuntu machine, and every time I did\nsomething like:\n\nf=function(\"f\",x)\nintegrate(f,x,0,1)\n\nin a notebook, sage showed me the equation using an integral symbol. I\njust installed sage 4.0, and when I do the same, I get:\n\nintegrate(f(x), x, 0, 1)\n\n\nno matter if I check the Typeset Box. It happens also with\nderivatives.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6211\n\n",
    "created_at": "2009-06-04T20:06:11Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "typesetting symbolic integrals broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6211",
    "user": "burcin"
}
```
CC:  mhansen

Reported by Ricardo on sage-support:


```
I had installed sage 3.4.1 in my Ubuntu machine, and every time I did
something like:

f=function("f",x)
integrate(f,x,0,1)

in a notebook, sage showed me the equation using an integral symbol. I
just installed sage 4.0, and when I do the same, I get:

integrate(f(x), x, 0, 1)


no matter if I check the Typeset Box. It happens also with
derivatives.
```


Issue created by migration from https://trac.sagemath.org/ticket/6211





---

archive/issue_comments_049623.json:
```json
{
    "body": "Latex typesetting of sub expressions also seem to be broken. This is probably caused by pynac not passing on the printing context when it calls the print function on the subexpression, though I haven't looked at any code yet.\n\nHere is an example:\n\n\n```\nsage: var('kappa')\nkappa\nsage: x = sqrt(kappa)\nsage: latex(x)\n\\sqrt{\\kappa}\nsage: F = exp(x)\nsage: F\ne^sqrt(kappa)\nsage: latex(F)\ne^{sqrt(kappa)}\n```\n",
    "created_at": "2009-06-10T08:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49623",
    "user": "burcin"
}
```

Latex typesetting of sub expressions also seem to be broken. This is probably caused by pynac not passing on the printing context when it calls the print function on the subexpression, though I haven't looked at any code yet.

Here is an example:


```
sage: var('kappa')
kappa
sage: x = sqrt(kappa)
sage: latex(x)
\sqrt{\kappa}
sage: F = exp(x)
sage: F
e^sqrt(kappa)
sage: latex(F)
e^{sqrt(kappa)}
```




---

archive/issue_comments_049624.json:
```json
{
    "body": "Burcin: It seems the problem of sub-expression not getting typeset properly\nis specific to exp function. I could get it working by adding the\n_latex_composition method to class Function_exp (sage.functions.log) as\n\n\n```\n    def _latex_composition(self, x):\n        from sage.misc.latex import latex\n        return \"e^{%s}\"%(latex(x))\n```\n\n\nNote: My sage copy has patch #5711 applied on it.",
    "created_at": "2009-06-13T11:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49624",
    "user": "gmhossain"
}
```

Burcin: It seems the problem of sub-expression not getting typeset properly
is specific to exp function. I could get it working by adding the
_latex_composition method to class Function_exp (sage.functions.log) as


```
    def _latex_composition(self, x):
        from sage.misc.latex import latex
        return "e^{%s}"%(latex(x))
```


Note: My sage copy has patch #5711 applied on it.



---

archive/issue_comments_049625.json:
```json
{
    "body": "This was about typesetting integrals, but since a description of exp not typesetting properly was added to this and #5711 is now largely about the typesetting of integrals etc., it seemed wise to change the description and summary.  The commentary above seems pretty useful!",
    "created_at": "2009-06-13T23:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49625",
    "user": "kcrisman"
}
```

This was about typesetting integrals, but since a description of exp not typesetting properly was added to this and #5711 is now largely about the typesetting of integrals etc., it seemed wise to change the description and summary.  The commentary above seems pretty useful!



---

archive/issue_comments_049626.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-14T21:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49626",
    "user": "burcin"
}
```

Attachment



---

archive/issue_comments_049627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T21:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49627",
    "user": "ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_049628.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-06-14T21:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6211#issuecomment-49628",
    "user": "ncalexan"
}
```

Fine by me.
