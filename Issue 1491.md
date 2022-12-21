# Issue 1491: [with patch] improve conversion from interface to sage objects (i.e., the dot sage method)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-13 20:22:35

Assignee: was


```


On Dec 13, 2007 11:54 AM, Timothy Clemans <timothy.clemans`@`gmail.com> wrote:
> 
> I'm getting
> 
> {{{id=2|
> def math_bessel_K(nu,x):
>        return mathematica(nu).BesselK(x).N(20).sage()
> math_bessel_K(2,I)
> ///
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/tclemans/.sage/sage_notebook/worksheets/admin/5/code/
> 9.py", line 6, in <module>
>     exec compile(ur'math_bessel_K(Integer(2),I)' + '\n', '', 'single')
>   File "/home/was/s/data/extcode/sage/", line 1, in <module>
> 
>   File "/home/tclemans/.sage/sage_notebook/worksheets/admin/5/code/
> 9.py", line 5, in math_bessel_K
>     return mathematica(nu).BesselK(x).N(Integer(20)).sage()
>   File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/
> expect.py", line 1086, in sage
>     return self._sage_()
>   File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/
> expect.py", line 1079, in _sage_
>     return sage.misc.sage_eval.sage_eval(repr(self))
>   File "/home/was/s/local/lib/python2.5/site-packages/sage/misc/
> sage_eval.py", line 112, in sage_eval
>     raise SyntaxError, "%s\nError using SAGE to evaluate '%s'"%(msg,
> p)
> SyntaxError: invalid syntax (<string>, line 1)
> Error using SAGE to evaluate '-
> RealNumber('2.592886175491196978167651322538251462935637034451900356688')
> +
> 
> RealNumber('0.180489972066962026629620880838378650496225604668529521981')*I'
> }}}

That's coming from a newline, which appears in Mathematica 5 I guess, but not 6.  Anyway,
the patch I justed posted at 

fixes the problem.  Alternatively rewrite the function like this:

sage: def math_bessel_K(nu,x):
  return sage_eval(repr(mathematica(nu).BesselK(x).N(20)).replace('\n',''))

Important note: The conversion from Mathematica to Sage, i.e., mathematica_object.sage()
is very naive still -- all it is is basically sage_eval(repr(...))!   This could/would be improved
if somebody cared a lot.

William
```



---

Attachment


---

Comment by cwitty created at 2007-12-15 05:18:01

Looks good.  (Looks reasonable, and sage/interfaces/mathematica.py doctests pass on sage.math.)


---

Comment by mabshoff created at 2007-12-15 05:40:10

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 05:40:10

Resolution: fixed
