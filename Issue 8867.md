# Issue 8867: speed up the riemann mapping functionality

Issue created by migration from https://trac.sagemath.org/ticket/8867

Original creator: jason

Original creation time: 2010-05-04 04:55:56

Assignee: burcin

CC:  evanandel kcrisman

This patch speeds up the riemann mapping functionality by automatically trying to call fast_callable on the functions passed in.  This depends on #5572 (patch "improve_fast_callable.patch")


---

Attachment


---

Comment by jason created at 2010-05-04 05:24:06

Changing status from new to needs_work.


---

Comment by jason created at 2010-05-04 05:25:04

The doctests are *much* faster now; I hope I didn't introduce any bugs!  The patch isn't finished yet, I don't think.


---

Comment by jason created at 2010-05-04 05:26:49

(I don't think I can work on this a lot more, but at least this is a start to making this faster)

This is very timely---another faculty member was just asking me a few weeks ago about how to use Sage to visualize Riemann mappings.  That's why I thought I'd work on it for a few minutes to speed it up.


---

Comment by evanandel created at 2010-05-04 15:13:00

Excellent Jason, thanks. Let me know if there's anything else that would help you guys.


---

Comment by evanandel created at 2010-11-30 17:18:12

What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch


---

Comment by evanandel created at 2010-11-30 17:20:49

Whoops, changed description on accident, comment should have read:

 What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch, do you have any idea when that is expected to finish? 
 
Not at all trying to rush you, just curious for my own purposes if this is coming through soon.


---

Comment by jason created at 2010-11-30 17:41:31

No guarantees, but I'd like to finish the fast_callable patch over Christmas break (so before the middle of January).


---

Comment by jason created at 2010-12-01 04:18:09

Actually, I just tried applying this patch without #5572 and things seem to work just fine.  You might try testing this patch anyway and reviewing it.


---

Comment by jason created at 2010-12-01 04:19:05

So I don't think this depends on #5572 anymore.


---

Comment by evanandel created at 2010-12-17 19:18:53

Did all of the tests work for you? The riemann tests go fine, but the interpolators do this:


```
File "/home/ethan/sage-4.5.3/devel/sage/sage/calculus/interpolators.pyx", line 52:

  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)

Exception raised:

  Traceback (most recent call last):
    File "/home/ethan/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
      self.run_one_example(test, example, filename, compileflags)
    File "/home/ethan/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
      OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
    File "/home/ethan/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
      compileflags, 1) in test.globs
    File "<doctest __main__.example_1[7]>", line 1, in <module>
      m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],Integer(0))###line 52:
  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)
    File "riemann.pyx", line 164, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1443) File "fast_callable.pyx", line 399, in sage.ext.fast_callable.fast_callable (sage/ext/fast_callable.c:2668)
  AttributeError: 'function' object has no attribute 'variables'
```


I can solve this by wrapping the fast-callable casts in a try except block, but of course that means that it isn't using them for unusual functions like the interpolators.


---

Comment by jason created at 2010-12-17 19:34:40

fast_callable won't do anything to speed up a lambda function anyway.  It just blindly wraps them in a python call.  So I don't think there's any loss in having a try-except block.


---

Comment by jason created at 2010-12-17 19:38:36

My big patch to fast_callable should also be able to handle the error, but it probably won't be finished or ready for testing for at least another couple of weeks, so if you have time now, don't wait for it.


---

Comment by evanandel created at 2011-03-22 03:34:49

Updated to dodge lambdas and work with new doctests


---

Attachment

I've uploaded a new version of the fast_callable patch. It now properly avoids failing with lambda functions, although it doesn't work optimally for them. I'll add some notes on that in #10945. It also is updated to work properly with the numpy 1.5.1 version. Therefore tickets #10792 and #10821 should be applied first. I don't think the current patch is dependent on #5572, although I'm sure that faster fast_callables would help.


---

Comment by evanandel created at 2011-03-22 03:39:51

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2011-04-27 22:14:01

This seems to be faster and less buggy than before, although I still have a pretty easy time tripping it up.  For example, the following crescent region causes problems if its not translated as I do below, but even when its translated so that 0 is in the interior the spiderweb plot looks wrong:


```
npi = N(pi)
crescent = [(cos(t)+.9,sin(t)) for t in srange(npi/2,3*npi/2,npi/12)]
crescent = crescent + [(5.0*cos(t)/6+.9,sin(t)) for t in srange(3*npi/2,npi/2,-npi/12)]
ps = polygon_spline(crescent) 
f = lambda t: ps.value(real(t)) 
fprime = lambda t: ps.derivative(real(t)) 
m = Riemann_Map([f], [fprime], 0.25, ncorners=24) 
show(m.plot_colored() + m.plot_spiderweb(pts=100),figsize=[6,6])
}}} 

But maybe that sort of problem should be in a seperate ticket.


---

Comment by mhampton created at 2011-04-27 22:14:01

Remove assignee burcin.


---

Comment by kcrisman created at 2011-04-28 02:00:29

Yeah, if you think this is good to go (i.e., correct and doesn't make functionality worse), you can give it positive review.  If you can open a ticket with things like this plot and the untranslated one, that would be great.  It sounds like Ethan is working on it a fair amount right now (?), so it would be good to have it on the burner.


---

Comment by evanandel created at 2011-04-28 03:34:08

The example given is naturally a problematic one. With the center located outside (a = .25) of the region, it is mathematically nonsensical, thus any output that you get will be bizarre. For the a = 0 case, the spiderweb plot is indeed slightly erratic (caused by the natural inaccuracy of the numerical integration near the boundary). This can be solved by decreasing the linescale parameter. This is documented, but I can see now that it isn't quite clear enough. I'll elaborate as part of the major documentation changes described in #10945.

I'm curious, what were you trying to accomplish by setting ncorners to 24 when this region only has 2? Is this poorly documented?

To elaborate, none of the behavior seen in this example is incorrect. Let me know if there are any other doc changes I can make to make this easier (I'm working on that already).


---

Comment by mhampton created at 2011-04-28 14:18:06

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2011-04-28 14:18:06

The crescent is a polygon with 24 vertices, so I thought using ncorners=24 would make sense.

To be honest, I didn't read the documentation very carefully.  This is a good simulation of general users :)  Now that I have, I am happy with the behavior of this function.


---

Comment by evanandel created at 2011-04-28 14:41:51

Ah, good point. I'll clarify that in the docs.


---

Comment by evanandel created at 2011-04-28 14:42:22

Specifically in the major revision I'm working on, not here.


---

Comment by jdemeyer created at 2011-05-31 17:06:54

Resolution: fixed
