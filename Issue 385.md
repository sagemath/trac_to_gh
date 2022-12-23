# Issue 385: implement at for symbolics

Issue created by migration from https://trac.sagemath.org/ticket/385

Original creator: was

Original creation time: 2007-06-07 18:51:34

Assignee: was

CC:  jason burcin was mhansen


```
On 6/7/07, Randy LeVeque <rjl@amath.washington.edu> wrote:
> By the way, I'm just trying to figure out how sage does Taylor series.
> Maybe you can pass this on to whoever the best person is to chat with about
> this...
> 
> In maple I can do things like
> 
> > mtaylor(u(x+h,t+k),[h,k],3);
>                                                                      2
> u(x, t) + D[1](u)(x, t) h + D[2](u)(x, t) k + 1/2 D[1, 1](u)(x, t) h
> 
>                                                      2
>       + h D[1, 2](u)(x, t) k + 1/2 D[2, 2](u)(x, t) k
> 
> 
> which is very convenient for numerical analysis when computing truncation
> errors of finite difference methods (h and k are mesh widths in space and
> time).  In sage a general expansion of this sort doesn't seem possible even
> in a single variable, e.g.,
> 
> sage: taylor(u(x+h),h,0,4)
> x + h
> 
> Apparently an undefined function like u(x) is taken to be the identity map?

To define a formal function, do u = function('u').  Then

sage: u = function('u')
sage: u(x + h)
u(x + h)
sage: diff(u(x+h), x)
diff(u(x + h), x, 1)

To get the Taylor expansion you would do this:

sage: taylor(u(x+h),h,0,4)

-- however -- this currently doesn't work in SAGE since we hadn't considered
doing this yet.   What happens is Maxima does the computation and outputs
the following expression:

'u(x)+(?%at('diff('u(x+h),h,1),h=0))*h+(?%at('diff('u(x+h),h,2),h=0))*h^2/2+(?%at('diff('u(x+h),h,3),h=0))*h^3/6+(?%at('diff('u(x+h),h,4),h=0))*h^4/24

SAGE doesn't know yet how to parse the "at" function, so you get
an error -- it will have to be added.   [Note that I don't necessarily consider
maxima the ultimate underlying engine for SAGE's symbolic computation
capabilities -- but it does provide a very quick way for SAGE to have
a powerful symbolic system for which a lot of subtle bugs have
already been fixed (over the last 40 years of Maxima development). ]

Definitely point out lots of things like this in your talk at SD4!

 -- William
```



---

Comment by gfurnish created at 2008-03-16 20:12:00

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:12:00

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-01-22 18:20:49

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2009-09-28 20:13:59

This would also resolve #3914.


---

Comment by kcrisman created at 2009-10-09 16:08:00

Try this patch.  It should do the trick.  Notice that I do not make it a normal symbolic function like in functions/other.py or something, because it's only for use here for now.  If necessary, I could do that, though - it's a nice second way to do things instead of .subs(), so I could also import it globally if appropriate.  I put in doctests for this, #3914, and a direct call.


---

Comment by kcrisman created at 2009-10-09 16:08:00

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-10-10 23:08:16

Attachment 'trac_385-at-evaluate.patch' not found :(


---

Comment by kcrisman created at 2009-10-12 16:47:39

Based on 4.1.2.alpha4


---

Attachment

Replying to [comment:6 robert.marik]:
> Attachment 'trac_385-at-evaluate.patch' not found :(

It must have gotten lost somewhere during the latest Trac outage.   This should work now.


---

Comment by wdj created at 2009-10-24 20:07:49

Passes sage -testall and does what it claims. Adds some very very useful functionality.


---

Comment by wdj created at 2009-10-24 20:07:49

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 16:41:17

Resolution: fixed
