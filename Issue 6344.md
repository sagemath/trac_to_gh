# Issue 6344: Typesetting partial derivatives in new Symbolics

Issue created by migration from https://trac.sagemath.org/ticket/6344

Original creator: gmhossain

Original creation time: 2009-06-16 23:47:36

CC:  jason mvngu robertwb eviatarbach schymans pbruin nbruin

New symbolics uses "D" format for derivatives instead of old "diff" format. 

See the threads below for discussion on various related issues

*[1]*  http://groups.google.com/group/sage-devel/browse_thread/thread/7479c3eeb96348a2

*[2]*  http://groups.google.com/group/sage-devel/browse_thread/thread/2c8068f27c1fb642

The purpose of this patch to decide the strategy: how to tackle the various issues while typesetting D derivative.

Some part of the code from the patch #5711 should be taken out.


---

Comment by burcin created at 2009-06-24 21:43:19

an attempt at implementing the MMA style, for testing only


---

Attachment

attachment:trac_6344-mma_style_attempt.patch implements an approximation to MMA style. It is just for testing, needs much more work for inclusion.

It doesn't look good in text only mode:


```
sage: f = function('f')
sage: f(x).derivative(x,3)
f^{(3)}(x)
```



---

Comment by burcin created at 2009-07-14 21:39:10

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

Comment by burcin created at 2009-07-14 21:39:10

Changing status from new to assigned.


---

Comment by burcin created at 2009-07-14 21:39:10

Set assignee to burcin.


---

Attachment

change printing of symbolic derivatives


---

Comment by kcrisman created at 2009-10-29 18:19:26

This needs a slight rebasing to be applied and tested to Sage 4.2, in calculus/tests.py and symbolic/pynac.pyx.


---

Comment by kcrisman created at 2009-10-29 18:19:26

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2014-03-12 08:50:15

#14517 has a similar complaint.


---

Comment by schymans created at 2014-12-03 21:41:12

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

Comment by nbruin created at 2014-12-03 22:48:26

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

Comment by schymans created at 2014-12-04 00:40:08

Thanks for the quick answer! From the user's perspective, the best way would be to have an option similar to derivative_func in the function definition, allowing to define the notation for derivatives. The efforts required seems indeed amazingly high. 

Wouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040


---

Comment by nbruin created at 2014-12-04 01:26:06

Replying to [comment:16 schymans]:
> Wouldn't it be possible to write some parsing code to convert something like D[0,1](f)(x,y) to any kind of notation? It should even be possible to convert it back to diff(f(x,y),x,y), as requested here: http://comments.gmane.org/gmane.comp.mathematics.sage.devel/58040

It's really much easier to do on the expression tree than on a string. We do it for conversions already. See e.g. [https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564](https://github.com/sagemath/sage/blob/master/src/sage/interfaces/maxima_lib.py#L1564). The approach is straightforward. The hard work is that you need to reach into Pynac to make the change. So it takes someone conversant with Pynac who cares enough to do it. Doing it on strings afterwards is going to be horrible.

Incidentally, watch out that an expression like

```
D[0,1](f)(x,x+1)
```

is almost impossible to write in Leibnitz notation unless you introduce auxiliary variables (which is what happens in the maxima_lib code). So you should probably just stick with operator notation for those cases (maple does).


---

Comment by schymans created at 2014-12-04 08:34:10

I see. Would it be easier to allow the user to define custom latex representations for just some standard differentials one anticipates when defining a function? For all others, the system could fall back to the D[0,1] (f)(x,z) notation. A simple replacement rule when latexing an expression could do it. 

By the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?


---

Comment by kcrisman created at 2014-12-04 14:19:29

> By the way, it took me a quite some time of digging in the code to understand the meaning of e.g. D[0,1](f)(x,z). Now that I have understood it, I see its use. I was expecting a description in the documentation of the diff() or differential() command, but I didn't find it there. Where is the right place to look?

If anyone should know, I should, but I don't.  It would be _wonderful_ to have some better documentation of that where it belongs - want to take a stab?  If so, open a ticket and cc: me.


---

Comment by schymans created at 2014-12-04 22:16:55

Thanks, this is now http://trac.sagemath.org/ticket/17445
There, I mentioned some other, related tickets, which made me realise that I do not fully understand the meaning of the D-notation, so it wouldn't make much sense for me to write a documentation for it. Sorry!


---

Comment by kcrisman created at 2014-12-05 04:11:42

Wow, after reading the threads in question I see that at this point Sage has existed about as long with this new format as it did with the previous one.  I'm reluctant to make this wontfix, at least the _option_ as indicated there

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

Comment by schymans created at 2014-12-05 09:27:35

+1 from me! I was very sad to find out that this had not been implemented.


---

Comment by kcrisman created at 2014-12-05 14:08:23

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

Comment by nbruin created at 2014-12-05 17:39:38

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

Comment by kcrisman created at 2014-12-05 17:52:15

Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?  <ducks />


---

Comment by nbruin created at 2014-12-05 17:58:51

Replying to [comment:25 kcrisman]:
> Oh, so that's where the `t0` and friends come from.  Funny thing... what if those variables are already taken?
Thought about that, no problem. They get substituted right away.


---

Comment by nbruin created at 2018-03-22 01:28:35

#21286 has dealt with with this. Close as duplicate/invalid ?


---

Comment by nbruin created at 2018-03-22 01:28:35

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2018-04-15 11:46:09

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
