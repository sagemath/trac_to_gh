# Issue 6211: typesetting symbolic integrals broken

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-06-04 20:06:11

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



---

Comment by burcin created at 2009-06-10 08:46:20

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

Comment by gmhossain created at 2009-06-13 11:54:48

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

Comment by kcrisman created at 2009-06-13 23:57:25

This was about typesetting integrals, but since a description of exp not typesetting properly was added to this and #5711 is now largely about the typesetting of integrals etc., it seemed wise to change the description and summary.  The commentary above seems pretty useful!


---

Attachment


---

Comment by ncalexan created at 2009-06-14 21:41:01

Resolution: fixed


---

Comment by ncalexan created at 2009-06-14 21:41:01

Fine by me.
