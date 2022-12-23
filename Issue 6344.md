# Issue 6344: Typesetting partial derivatives in new Symbolics

archive/issues_006344.json:
```json
{
    "body": "CC:  jason mvngu robertwb eviatarbach schymans pbruin nbruin\n\nNew symbolics uses \"D\" format for derivatives instead of old \"diff\" format. \n\nSee the threads below for discussion on various related issues\n\n**[1]**  http://groups.google.com/group/sage-devel/browse_thread/thread/7479c3eeb96348a2\n\n**[2]**  http://groups.google.com/group/sage-devel/browse_thread/thread/2c8068f27c1fb642\n\nThe purpose of this patch to decide the strategy: how to tackle the various issues while typesetting D derivative.\n\nSome part of the code from the patch #5711 should be taken out.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6344\n\n",
    "created_at": "2009-06-16T23:47:36Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "Typesetting partial derivatives in new Symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6344",
    "user": "gmhossain"
}
```
CC:  jason mvngu robertwb eviatarbach schymans pbruin nbruin

New symbolics uses "D" format for derivatives instead of old "diff" format. 

See the threads below for discussion on various related issues

**[1]**  http://groups.google.com/group/sage-devel/browse_thread/thread/7479c3eeb96348a2

**[2]**  http://groups.google.com/group/sage-devel/browse_thread/thread/2c8068f27c1fb642

The purpose of this patch to decide the strategy: how to tackle the various issues while typesetting D derivative.

Some part of the code from the patch #5711 should be taken out.

Issue created by migration from https://trac.sagemath.org/ticket/6344





---

archive/issue_comments_050702.json:
```json
{
    "body": "an attempt at implementing the MMA style, for testing only",
    "created_at": "2009-06-24T21:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50702",
    "user": "burcin"
}
```

an attempt at implementing the MMA style, for testing only



---

archive/issue_comments_050703.json:
```json
{
    "body": "Attachment\n\nattachment:trac_6344-mma_style_attempt.patch implements an approximation to MMA style. It is just for testing, needs much more work for inclusion.\n\nIt doesn't look good in text only mode:\n\n\n```\nsage: f = function('f')\nsage: f(x).derivative(x,3)\nf^{(3)}(x)\n```\n",
    "created_at": "2009-06-24T21:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50703",
    "user": "burcin"
}
```

Attachment

attachment:trac_6344-mma_style_attempt.patch implements an approximation to MMA style. It is just for testing, needs much more work for inclusion.

It doesn't look good in text only mode:


```
sage: f = function('f')
sage: f(x).derivative(x,3)
f^{(3)}(x)
```




---

archive/issue_comments_050704.json:
```json
{
    "body": "I uploaded a new patch at attachment:trac_6344-symbolic_derivative_print.patch.\n\nThe new patch keeps the text mode printing similar to the old one, but changes the printed parameters to indicate how many times each argument is differentiated. E.g., old output:\n\n\n```\nsage: var('x,y')\nsage: f = function('f')\nsage: f(x).derivative(x)\nD[0](f)(x)\nsage: f(x,x).derivative(x,2)\nD[0, 0](f)(x, x) + 2*D[0, 1](f)(x, x) + D[1, 1](f)(x, x)\n```\n\n\nNew output:\n\n\n```\nsage: f(x).derivative(x)\nD[1](f)(x)\nsage: f(x,x).derivative(x,2)\nD[2, 0](f)(x, x) + 2*D[1, 1](f)(x, x) + D[0, 2](f)(x, x)\n```\n\n\nNew latex output:\n\n\n```\nsage: latex(f(x).derivative(x))\nf'\\left(x\\right)\nsage: latex(f(x,x).derivative(x,2))\nf^{(2,0)}\\left(x, x\\right) + 2 \\, f^{(1,1)}\\left(x, x\\right) + f^{(0,2)}\\left(x, x\\right)\n```\n\n\nIt would be better to add more documentation to explain the output, provide conversions to \"textbook style\" and fix other problems that pop up when printing derivatives:\n\n\n```\nsage: binomial(x,y).derivative(x)\n<boom>\nsage: latex(floor(x).derivative(x))\nD[0]\\left \\lfloor x \\right \\rfloor\nsage: latex(ceil(x).derivative(x))\nD[0]\\left \\lceil x \\right \\rceil\n```\n\n\nHowever, I think we should settle on an output style ASAP, without letting too many releases go by.\n\nJason, Minh, can one (or both) of you review this?",
    "created_at": "2009-07-14T21:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50704",
    "user": "burcin"
}
```

I uploaded a new patch at attachment:trac_6344-symbolic_derivative_print.patch.

The new patch keeps the text mode printing similar to the old one, but changes the printed parameters to indicate how many times each argument is differentiated. E.g., old output:


```
sage: var('x,y')
sage: f = function('f')
sage: f(x).derivative(x)
D[0](f)(x)
sage: f(x,x).derivative(x,2)
D[0, 0](f)(x, x) + 2*D[0, 1](f)(x, x) + D[1, 1](f)(x, x)
```


New output:


```
sage: f(x).derivative(x)
D[1](f)(x)
sage: f(x,x).derivative(x,2)
D[2, 0](f)(x, x) + 2*D[1, 1](f)(x, x) + D[0, 2](f)(x, x)
```


New latex output:


```
sage: latex(f(x).derivative(x))
f'\left(x\right)
sage: latex(f(x,x).derivative(x,2))
f^{(2,0)}\left(x, x\right) + 2 \, f^{(1,1)}\left(x, x\right) + f^{(0,2)}\left(x, x\right)
```


It would be better to add more documentation to explain the output, provide conversions to "textbook style" and fix other problems that pop up when printing derivatives:


```
sage: binomial(x,y).derivative(x)
<boom>
sage: latex(floor(x).derivative(x))
D[0]\left \lfloor x \right \rfloor
sage: latex(ceil(x).derivative(x))
D[0]\left \lceil x \right \rceil
```


However, I think we should settle on an output style ASAP, without letting too many releases go by.

Jason, Minh, can one (or both) of you review this?



---

archive/issue_comments_050705.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-14T21:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50705",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050706.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2009-07-14T21:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50706",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_050707.json:
```json
{
    "body": "Attachment\n\nchange printing of symbolic derivatives",
    "created_at": "2009-07-14T21:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50707",
    "user": "burcin"
}
```

Attachment

change printing of symbolic derivatives



---

archive/issue_comments_050708.json:
```json
{
    "body": "This needs a slight rebasing to be applied and tested to Sage 4.2, in calculus/tests.py and symbolic/pynac.pyx.",
    "created_at": "2009-10-29T18:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50708",
    "user": "kcrisman"
}
```

This needs a slight rebasing to be applied and tested to Sage 4.2, in calculus/tests.py and symbolic/pynac.pyx.



---

archive/issue_comments_050709.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T18:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50709",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050710.json:
```json
{
    "body": "#14517 has a similar complaint.",
    "created_at": "2014-03-12T08:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50710",
    "user": "burcin"
}
```

#14517 has a similar complaint.



---

archive/issue_comments_050711.json:
```json
{
    "body": "I tried to apply the most recent patch, but did not succeed. It is just too old and when looking at the diff I couldn't make any sense of it. I tried to implement differential notation myself, but got stuck, perhaps someone can help?\n\nAll I wanted to do is to change the _latex_ representation of the FDerivativeOperator and added the following lines to src/sage/symbolic/operators.py:\n\n\n\n```\ndef _latex_(self):\n        \"\"\"\n            Return the LaTeX representation of X.\n\n            EXAMPLES::\n\n            sage: from sage.symbolic.operators import FDerivativeOperator\n            sage: var('x z')\n            sage: f = function('f', x, z)\n            sage: op = FDerivativeOperator(f, [0,1]); latex(op)\n            \\frac{\\partial \\frac{\\partial f }{\\partial x } }{\\partial z }\n        \"\"\"\n        fname = self._f.operator()\n        vars = self._f.operands()\n        difvars = self._parameter_set\n        str1 = str(fname)\n        for difvar in difvars:\n            str1 = '\\\\frac{\\partial '+str1+'}{\\partial '+str(vars[difvar])+'}'\n        return str1\n```\n\nUnfortunately, this does not have any effect on the latex representation of f.diff:\n\n\n```\nsage: f = function('f', x, z)\nsage: g = diff(f, x,z)\nsage: latex(g)\nD[0, 1]\\left(f\\right)\\left(x, z\\right)\n```\n\n\nDoes anyone have an idea what else I need to modify? Thanks in advance!",
    "created_at": "2014-12-03T21:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50711",
    "user": "schymans"
}
```

I tried to apply the most recent patch, but did not succeed. It is just too old and when looking at the diff I couldn't make any sense of it. I tried to implement differential notation myself, but got stuck, perhaps someone can help?

All I wanted to do is to change the _latex_ representation of the FDerivativeOperator and added the following lines to src/sage/symbolic/operators.py:



```
def _latex_(self):
        """
            Return the LaTeX representation of X.

            EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: var('x z')
            sage: f = function('f', x, z)
            sage: op = FDerivativeOperator(f, [0,1]); latex(op)
            \frac{\partial \frac{\partial f }{\partial x } }{\partial z }
        """
        fname = self._f.operator()
        vars = self._f.operands()
        difvars = self._parameter_set
        str1 = str(fname)
        for difvar in difvars:
            str1 = '\\frac{\partial '+str1+'}{\partial '+str(vars[difvar])+'}'
        return str1
```

Unfortunately, this does not have any effect on the latex representation of f.diff:


```
sage: f = function('f', x, z)
sage: g = diff(f, x,z)
sage: latex(g)
D[0, 1]\left(f\right)\left(x, z\right)
```


Does anyone have an idea what else I need to modify? Thanks in advance!



---

archive/issue_comments_050712.json:
```json
{
    "body": "Replying to [comment:13 schymans]:\n> All I wanted to do is to change the _latex_ representation of the FDerivativeOperator and added the following lines to src/sage/symbolic/operators.py:\n\nLooks like the wrong place to hook into this. For symbolic expressions. `self._latex_` invokes `SR._latex_element_` which calls straight into Pynac via ` GEx_to_str_latex(&x._gobj)`. Your experiment shows that this doesn't dispatch to `_latex_` methods on operators. Perhaps there's another hook?\n\nIncidentally, your code wouldn't work, because that's not how FDerivateOperators occur in code:\n\n\n```\nsage: var(\"x,y\")\n(x, y)\nsage: function('f',x,y)\nf(x, y)\nsage: g=diff(f(x,y),x,y)\nsage: g\nD[0, 1](f)(x, y)\nsage: g.operator()\nD[0, 1](f)\nsage: type(g.operator())\n<class 'sage.symbolic.operators.FDerivativeOperator'>\nsage: g.operator()._f\nf\n```\n\nAs you can see, there are no variable names to refer to. That's why this ticket has stalled: if you want to do this, you need to recognize on the level of `g` that the operator is an `FDerivativeOperator` and hence that, if the operands of `g` are distinct, simple symbolic variables, that the derivative could be written in Leibnitz notation.\n\nClearly, people haven't found the effort required worth the payoff.",
    "created_at": "2014-12-03T22:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50712",
    "user": "nbruin"
}
```

Replying to [comment:13 schymans]:
> All I wanted to do is to change the _latex_ representation of the FDerivativeOperator and added the following lines to src/sage/symbolic/operators.py:

Looks like the wrong place to hook into this. For symbolic expressions. `self._latex_` invokes `SR._latex_element_` which calls straight into Pynac via ` GEx_to_str_latex(&x._gobj)`. Your experiment shows that this doesn't dispatch to `_latex_` methods on operators. Perhaps there's another hook?

Incidentally, your code wouldn't work, because that's not how FDerivateOperators occur in code:


```
sage: var("x,y")
(x, y)
sage: function('f',x,y)
f(x, y)
sage: g=diff(f(x,y),x,y)
sage: g
D[0, 1](f)(x, y)
sage: g.operator()
D[0, 1](f)
sage: type(g.operator())
<class 'sage.symbolic.operators.FDerivativeOperator'>
sage: g.operator()._f
f
```

As you can see, there are no variable names to refer to. That's why this ticket has stalled: if you want to do this, you need to recognize on the level of `g` that the operator is an `FDerivativeOperator` and hence that, if the operands of `g` are distinct, simple symbolic variables, that the derivative could be written in Leibnitz notation.

Clearly, people haven't found the effort required worth the payoff.



---

archive/issue_comments_050713.json:
```json
{
    "body": "Thanks for the quick answer! From the user's perspective, the best way would be to have an option similar to derivative_func in the function definition, allowing to define the notation for derivatives. The efforts required seems indeed amazingly high. \n\nWouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040",
    "created_at": "2014-12-04T00:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50713",
    "user": "schymans"
}
```

Thanks for the quick answer! From the user's perspective, the best way would be to have an option similar to derivative_func in the function definition, allowing to define the notation for derivatives. The efforts required seems indeed amazingly high. 

Wouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040



---

archive/issue_comments_050714.json:
```json
{
    "body": "Replying to [comment:16 schymans]:\n> Wouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040\n\nIt's really much easier to do on the expression tree than on a string. We do it for conversions already. See e.g. [https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564](https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564). The approach is straightforward. The hard work is that you need to reach into Pynac to make the change. So it takes someone conversant with Pynac who cares enough to do it. Doing it on strings afterwards is going to be horrible.\n\nIncidentally, watch out that an expression like\n\n```\nD[0,1](f)(x,x+1)\n```\n\nis almost impossible to write in Leibnitz notation unless you introduce auxiliary variables (which is what happens in the maxima_lib code). So you should probably just stick with operator notation for those cases (maple does).",
    "created_at": "2014-12-04T01:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50714",
    "user": "nbruin"
}
```

Replying to [comment:16 schymans]:
> Wouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040

It's really much easier to do on the expression tree than on a string. We do it for conversions already. See e.g. [https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564](https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564). The approach is straightforward. The hard work is that you need to reach into Pynac to make the change. So it takes someone conversant with Pynac who cares enough to do it. Doing it on strings afterwards is going to be horrible.

Incidentally, watch out that an expression like

```
D[0,1](f)(x,x+1)
```

is almost impossible to write in Leibnitz notation unless you introduce auxiliary variables (which is what happens in the maxima_lib code). So you should probably just stick with operator notation for those cases (maple does).



---

archive/issue_comments_050715.json:
```json
{
    "body": "I see. Would it be easier to allow the user to define custom latex representations for just some standard differentials one anticipates when defining a function? For all others, the system could fall back to the D[0,1] (f)(x,z) notation. A simple replacement rule when latexing an expression could do it. \n\nBy the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?",
    "created_at": "2014-12-04T08:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50715",
    "user": "schymans"
}
```

I see. Would it be easier to allow the user to define custom latex representations for just some standard differentials one anticipates when defining a function? For all others, the system could fall back to the D[0,1] (f)(x,z) notation. A simple replacement rule when latexing an expression could do it. 

By the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?



---

archive/issue_comments_050716.json:
```json
{
    "body": "> By the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?\n\nIf anyone should know, I should, but I don't.  It would be *wonderful* to have some better documentation of that where it belongs - want to take a stab?  If so, open a ticket and cc: me.",
    "created_at": "2014-12-04T14:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50716",
    "user": "kcrisman"
}
```

> By the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?

If anyone should know, I should, but I don't.  It would be *wonderful* to have some better documentation of that where it belongs - want to take a stab?  If so, open a ticket and cc: me.



---

archive/issue_comments_050717.json:
```json
{
    "body": "Thanks, this is now http://trac.sagemath.org/ticket/17445\nThere, I mentioned some other, related tickets, which made me realise that I do not fully understand the meaning of the D-notation, so it wouldn't make much sense for me to write a documentation for it. Sorry!",
    "created_at": "2014-12-04T22:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50717",
    "user": "schymans"
}
```

Thanks, this is now http://trac.sagemath.org/ticket/17445
There, I mentioned some other, related tickets, which made me realise that I do not fully understand the meaning of the D-notation, so it wouldn't make much sense for me to write a documentation for it. Sorry!



---

archive/issue_comments_050718.json:
```json
{
    "body": "Wow, after reading the threads in question I see that at this point Sage has existed about as long with this new format as it did with the previous one.  I'm reluctant to make this wontfix, at least the *option* as indicated there\n\n```\npsi(x) = function('psi',x)\ng = diff(psi(x),x)\nlatex(g)\n\\frac{d \\psi\\left(x\\right)}{d x}\n\n# Switch to D format\nsage.symbolic.pynac.typeset_d_as_diff=False\n\nlatex(g)\nD[0]\\psi\\left(x\\right)\n```\n\nshould exist, except of course the other way around for the default nowadays, I guess.  Maybe that piece of attachment:enhanced-symbolic-typesetting-rebased_to_4.0.1.patch:ticket:5711 should be implemented here instead?",
    "created_at": "2014-12-05T04:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50718",
    "user": "kcrisman"
}
```

Wow, after reading the threads in question I see that at this point Sage has existed about as long with this new format as it did with the previous one.  I'm reluctant to make this wontfix, at least the *option* as indicated there

```
psi(x) = function('psi',x)
g = diff(psi(x),x)
latex(g)
\frac{d \psi\left(x\right)}{d x}

# Switch to D format
sage.symbolic.pynac.typeset_d_as_diff=False

latex(g)
D[0]\psi\left(x\right)
```

should exist, except of course the other way around for the default nowadays, I guess.  Maybe that piece of attachment:enhanced-symbolic-typesetting-rebased_to_4.0.1.patch:ticket:5711 should be implemented here instead?



---

archive/issue_comments_050719.json:
```json
{
    "body": "+1 from me! I was very sad to find out that this had not been implemented.",
    "created_at": "2014-12-05T09:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50719",
    "user": "schymans"
}
```

+1 from me! I was very sad to find out that this had not been implemented.



---

archive/issue_comments_050720.json:
```json
{
    "body": "Nils and/or Peter, would you have objections to the following, based on code from #5711 (if possible)?\n\n```\npsi(x) = function('psi',x)\ng = diff(psi(x),x)\nlatex(g)\nD[0]\\psi\\left(x\\right)\n\n# Switch to D format\nsage.symbolic.pynac.typeset_d_as_diff=True\n\nlatex(g)\n\\frac{d \\psi\\left(x\\right)}{d x}\n```\n",
    "created_at": "2014-12-05T14:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50720",
    "user": "kcrisman"
}
```

Nils and/or Peter, would you have objections to the following, based on code from #5711 (if possible)?

```
psi(x) = function('psi',x)
g = diff(psi(x),x)
latex(g)
D[0]\psi\left(x\right)

# Switch to D format
sage.symbolic.pynac.typeset_d_as_diff=True

latex(g)
\frac{d \psi\left(x\right)}{d x}
```




---

archive/issue_comments_050721.json:
```json
{
    "body": "Replying to [comment:23 kcrisman]:\n> Nils and/or Peter, would you have objections to the following, based on code from #5711 (if possible)?\n> {{{\n> ...\n> sage.symbolic.pynac.typeset_d_as_diff=True\n> \n> latex(g)\n> \\frac{d \\psi\\left(x\\right)}{d x}\n> }}}\nOnly do that when the argument list consists only of distinct symbolic variables. Then you can even print \"diff\" for the normal rep. See links above for code that makes this distinction already. This is what Maple does too, by the way.",
    "created_at": "2014-12-05T17:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50721",
    "user": "nbruin"
}
```

Replying to [comment:23 kcrisman]:
> Nils and/or Peter, would you have objections to the following, based on code from #5711 (if possible)?
> {{{
> ...
> sage.symbolic.pynac.typeset_d_as_diff=True
> 
> latex(g)
> \frac{d \psi\left(x\right)}{d x}
> }}}
Only do that when the argument list consists only of distinct symbolic variables. Then you can even print "diff" for the normal rep. See links above for code that makes this distinction already. This is what Maple does too, by the way.



---

archive/issue_comments_050722.json:
```json
{
    "body": "Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?  <ducks />",
    "created_at": "2014-12-05T17:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50722",
    "user": "kcrisman"
}
```

Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?  <ducks />



---

archive/issue_comments_050723.json:
```json
{
    "body": "Replying to [comment:25 kcrisman]:\n> Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?\nThought about that, no problem. They get substituted right away.",
    "created_at": "2014-12-05T17:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50723",
    "user": "nbruin"
}
```

Replying to [comment:25 kcrisman]:
> Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?
Thought about that, no problem. They get substituted right away.



---

archive/issue_comments_050724.json:
```json
{
    "body": "#21286 has dealt with with this. Close as duplicate/invalid ?",
    "created_at": "2018-03-22T01:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50724",
    "user": "nbruin"
}
```

#21286 has dealt with with this. Close as duplicate/invalid ?



---

archive/issue_comments_050725.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-03-22T01:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50725",
    "user": "nbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050726.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-04-15T11:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50726",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050727.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50727",
    "user": "vdelecroix"
}
```

Resolution: wontfix



---

archive/issue_comments_050728.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6344#issuecomment-50728",
    "user": "vdelecroix"
}
```

closing positively reviewed duplicates
