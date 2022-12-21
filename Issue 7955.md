# Issue 7955: printing unevaluated integrals, limits, etc. broken

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-16 18:26:41

Assignee: burcin

From the sage-devel thread here:

http://groups.google.com/group/sage-devel/t/592ce36b210c2fbe


```
On Mon, 11 Jan 2010 23:58:54 -0800 (PST)
"marik`@`mendelu.cz" <marik`@`mendelu.cz> wrote:

> Dear sage-devel
> 
> the following (definite) integral is not evaluated by maxima and show
> () command should return the same unevaluated integral in TeX
> notation. I think this was the case in previous versions. On Sage 4.3.
> I get th following
> 
> input: integrate(1/(1+sqrt(x)),x,0,1).show()
> 
> output: \int integrate\,{d \frac{1}{\sqrt{x} + 1}}
> 
> expected output: \int_0^1 \frac{..}{...} dx
> 
> What has changed?
```


After #7490, we give the function object as the first argument to
custom methods of symbolic functions. The function that prints integrals
is _integrate_latex_() on line 1556 of sage/calculus/calculus.py. It
gets the function integrate as a first argument, and prints the
nonsense reported above.



---

Attachment

fix typesetting of unevaluated integrals


---

Comment by burcin created at 2010-01-17 09:11:43

Changing status from new to needs_review.


---

Comment by burcin created at 2010-01-17 09:11:43

attachment:trac_7955-integrate_latex.patch should fix this.


---

Comment by ddrake created at 2010-01-27 06:21:20

Replying to [comment:1 burcin]:
> attachment:trac_7955-integrate_latex.patch should fix this.

...and it does, on 4.3.1. The code looks good, all doctests pass, and the problem is fixed.


---

Comment by ddrake created at 2010-01-27 06:21:20

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:03:07

Resolution: fixed
