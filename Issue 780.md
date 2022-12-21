# Issue 780: calculus integration failing due to maxima interacting when it shouldn't

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-02 02:10:15

Assignee: was

CC:  jason


```
Hi,

This is a quick and possibly not so useful answer. 
(1) I think you're running into a bug in Maxima (hence Sage) below, since
your assumption should be passed through.  It's pretty hard for us Sage
developers to fix bugs in Maxima, unfortunately.   Nonetheless, we are
very thankful for the bug report.

(2) Possibly doing the following workaround would be OK for you, i.e.,
just compute the definite integral you want by computing an antiderivative
and use the fundamental theorem of calculus:

sage: x,y=var('x,y')
sage: f = log(x^2+y^2)
sage: integrate(f,x)
x*log(y^2 + x^2) - 2*(x - atan(x/y)*y)
sage: g = integrate(f,x)
sage: h = g(x=1.) - g(x=0.0001415); h    # this is what you want.
1.00000000000000*log(y^2 + 1.00000000000000) - 0.0001415000000000000000*log(y^2 + 0.000000020022250000000000000000) - 2*(1.00000000000000 - atan(1.00000000000000/y)*y) + 2*(0.0001415000000000000000 - atan(0.0001415000000000000000/y)*y)
sage: h(y=5)
3.231596665591034

On 10/1/07, Eliz <elyip`@`comcast.net> wrote:
> 
> Attached is the 'edit' view of my worksheet.  When I changed the lower
> bound of the definite integral from 0.0001415 to  0.0001414, we got
> into trouble.
> 
> Elizabeth
> ------------------------------------------------------------------------------------------------------------
> integration_exercise
> system:sage
> 
> {{{id=0|
> x,y=var('x,y')
> f=log(x^2+y^2)
> integrate(f,x)
> ///
> x*log(y^2 + x^2) - 2*(x - atan(x/y)*y)
> }}}
> 
> {{{id=11|
> assume(y^2>1)
> integrate(f,x,0.0001415,1.)
> ///
> 1.00000000000000*log(1.00000000000000*y^2 + 1.00000000000000) -
> 0.0001415000000000000000*log(1.00000000000000*y^2 +
> 0.000000020022250000000000000000) +
> 2.00000000000000*atan(1.00000000000000/y)*y -
> 2.00000000000000*atan(0.0001415000000000000000/y)*y - 1.99971700000000
> }}}
> 
> {{{id=16|
> assume(y^2<1)
> integrate(f,x,0.0001415,1.)
> ///
> 1.00000000000000*log(1.00000000000000*y^2 + 1.00000000000000) -
> 0.0001415000000000000000*log(1.00000000000000*y^2 +
> 0.000000020022250000000000000000) +
> 2.00000000000000*atan(1.00000000000000/y)*y -
> 2.00000000000000*atan(0.0001415000000000000000/y)*y - 1.99971700000000
> }}}
> 
> {{{id=17|
> assume(y^2==1)
> integrate(f,x,0.0001415,1.)
> ///
> 1.00000000000000*log(1.00000000000000*y^2 + 1.00000000000000) -
> 0.0001415000000000000000*log(1.00000000000000*y^2 +
> 0.000000020022250000000000000000) +
> 2.00000000000000*atan(1.00000000000000/y)*y -
> 2.00000000000000*atan(0.0001415000000000000000/y)*y - 1.99971700000000
> }}}
> 
> {{{id=19|
> assume(y^2>1)
> integrate(f,x,0.0001414,1.)
> ///
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/yip/sage_notebook/worksheets/admin/10/code/47.py", line
> 5, in <module>
>     exec
> compile(ur'integrate(f,x,RealNumber(\u00270.0001414\u0027),RealNumber(\u00271.\u0027))'
> + '\n', '', 'single')
>   File "/local/sage-2.8.5.1/data/extcode/sage/", line 1, in <module>
> 
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> calculus/functional.py", line 175, in integral
>     return f.integral(*args, **kwds)
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> calculus/calculus.py", line 1652, in integral
>     return self.parent()(self._maxima_().integrate(v, a, b))
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/maxima.py", line 1391, in integral
>     return I(var, min, max)
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/expect.py", line 884, in __call__
>     return self._obj.parent().function_call(self._name, [self._obj] +
> list(args))
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/expect.py", line 831, in function_call
>     return self.new("%s(%s)"%(function, ",".join([s.name() for s in
> args])))
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/expect.py", line 733, in new
>     return self(code)
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/maxima.py", line 376, in __call__
>     return Expect.__call__(self, x)
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/expect.py", line 678, in __call__
>     return cls(self, x)
>   File "/local/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/
> interfaces/expect.py", line 919, in __init__
>     raise TypeError, x
> TypeError: Computation failed since Maxima requested additional
> constraints (use assume):
> Is  (y-1)*(y+1)  positive, negative, or zero?
> }}}
> 
> {{{id=20|
> 
> }}}
> 
```



---

Comment by was created at 2007-10-02 02:12:48

The solution might be to make the pexpect interface interaction with maxima even more sophisticated or -- even better -- replicate the whole bug directly in maxima and report it to the maxima list (I'm too lazy to do so
right now).


---

Comment by AlexGhitza created at 2008-02-22 05:54:41

Submitted bug report to the maxima list, see

https://sourceforge.net/tracker/?func=detail&atid=104933&aid=1899352&group_id=4933


---

Comment by gfurnish created at 2008-03-16 20:11:42

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-16 20:11:42

Changing assignee from was to gfurnish.


---

Comment by was created at 2008-03-16 21:04:35

Somebody on the maxima list responded:

```
Date: 2008-02-22 06:16
Sender: rtoy
Logged In: YES 
user_id=28849
Originator: NO

Note that is((y-1)*(y+1)>0) returns unknown.  If you say assume(y>1),
integrate doesn't ask about that anymore. But it still asks about
y^2+x^2+2*x+1.  It should know that x > 0 and y > 0 here.
```



---

Comment by tjlahey created at 2008-11-27 08:33:40

I've noticed this many times when running my integration tests. Axiom handles these kinds of integrals by returning multiple solutions. Maxima could do the same and that's what I think is the best solution.

One possible solution on the Sage side would be to add optional parameters to answer the questions. So, the first time one tries the integral, you get the trackback so you re-run the integration with an added parameter to answer the question (or series of questions for problems with several branches). 

Since the questions are yes/no based, another option arises, that is more difficult to implement but better for the user. This would be to have an option for Sage to build up the branches by re-running the integration answering the questions automatically and noting the solution and the question+answer.

Both of these Sage solutions require improvements to the pexpect interface which are likely non-trivial.


---

Comment by kcrisman created at 2009-01-29 16:43:28

It should be pointed out that:

1. Changing the left endpoint from 0.0001415 to 0.0001414 caused the error in this case. Mysteriously, doing the endpoint 0.0001415 in maxima_console() still has two questions for you, but Sage nonetheless answers it!

2. assume((y-1)*(y+1)>0) or whatever doesn't work -  and even if it did, Maxima does have an actual bug in not recognizing that x is positive from the integral we wanted to calculate.  So a question-and-answer framework, while definitely helpful, wouldn't solve this particular issue.


---

Comment by AlexGhitza created at 2009-06-13 03:29:57

Note that the Maxima bug seems to have been fixed, see

https://sourceforge.net/tracker/?func=detail&atid=104933&aid=1899352&group_id=4933


---

Comment by AlexGhitza created at 2009-08-24 09:08:31

Changing assignee from gfurnish to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-24 09:08:31

This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest verifying this when #6699 gets merged.


---

Comment by AlexGhitza created at 2009-08-24 09:08:31

Changing status from assigned to new.


---

Attachment

attachment:trac_780-maxima_integral.patch adds doctests to show that this is fixed.

Alex, many thanks for your work on updating maxima. I'm trying to get as many symbolics/calculus tickets closed as possible for this release now.


---

Comment by kcrisman created at 2009-09-22 20:43:34

All tests passed!

Yes, also thanks!  Incidentally, I would be happy to help with updating Maxima as needed, now that I've read the spkg documentation in the developer's guide, because there are always new improvements.


---

Comment by mvngu created at 2009-09-22 23:05:58

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:39:09

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
