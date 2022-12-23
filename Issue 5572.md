# Issue 5572: fast_callable improvements (followup for #5093)

Issue created by migration from https://trac.sagemath.org/ticket/5572

Original creator: robertwb

Original creation time: 2009-03-19 23:55:25

Assignee: somebody

CC:  robertwb timdumol eviatarbach novoselt mjo

The code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. 

Specifically, 

Not fixed:

* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word "fast" in any option names.)

* fast_callable on list,tuple,vector,matrix arguments

* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)

* fast_callable on constant arguments (waiting for a spec from Jason!)

* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments


---

Comment by cwitty created at 2009-03-26 02:02:39

Changing assignee from somebody to cwitty.


---

Comment by cwitty created at 2009-03-26 02:02:39

Changing status from new to assigned.


---

Comment by jason created at 2009-09-24 19:36:51

More fast_callable improvements:

 * domain=float is the same as domain=RDF, but domain=complex is not the same as domain=CDF.  Make domain=complex use the same interpreter as domain=CDF

 * if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.


---

Comment by robertwb created at 2009-09-24 20:27:49

Both good points. At least g.variables() should be a subset of g.args().


---

Comment by jason created at 2010-04-24 06:02:58

Replying to [comment:2 jason]:

>  * if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.

#7512 may take care of this.


---

Attachment

This is a big patch to fast_callable which 

  * makes it work for lists/tuples like fast_float does
  * adds lots of _fast_callable_ methods to make it work on a lot of different constant objects (integers/rationals/RDF/RR/CDF/CC)
  * refactors the code a bit
  * in general replaces calls to fast_float with calls to fast_callable.
 
The patch also breaks some things---it's still a work in progress.


---

Comment by jason created at 2010-04-24 11:36:09

apply on top of previous patch


---

Attachment

The second patch is a broken attempt at streamlining the complex support since Cython now supports C99 complex numbers.


---

Comment by jason created at 2010-04-24 11:36:48

Changing status from new to needs_work.


---

Comment by jason created at 2010-04-26 11:57:23

CCing: robertwb since fast_float was his idea originally

timdumol since he's expressed interest in working on this sort of thing.

The two patches need work at this point.  In particular, the improvements patch needs docs added/changed, and ptestlong needs to be run to check for breakage.

The complex number patch needs an overhaul, as I think it's completely broken at this point.  The complex number patch is not necessary for resolving the issues on this ticket.


---

Comment by jason created at 2010-04-26 12:00:57

#8450 would be a good ticket to (trivially) fix after this ticket moves plotting solely over to fast_callable.


---

Comment by jason created at 2010-05-04 05:22:44

rebase to 4.4.1


---

Attachment

I think it might be best just to fix #7512 in this ticket.


---

Attachment

apply instead of previous patches


---

Comment by jason created at 2010-05-27 07:56:48

Still not done.  A clean design still needs to happen for fast_callable on symbolics without specified variables, and the nvars option seems like a hack to make plotting work with lambda functions (since we now match the argument names of lambda functions by default).


---

Comment by jason created at 2010-05-27 08:09:52

Also, something should be done to put fast_float back (and its file) as a convenience method.


---

Attachment

apply instead of previous patches (now doctests in plot/*.py[x] pass)


---

Comment by jason created at 2010-05-27 19:30:50

apply instead of previous patches (now almost all doctests in plot/plot3d/ pass)


---

Attachment

I had to rework some of the transformation code because the returned function often did not have the same keyword arguments as the original function, which throws off plotting.


---

Attachment

apply instead of previous patches (fixed a bunch of stuff so even more doctests pass)


---

Comment by jason created at 2010-09-05 01:47:23

To delete the fast_eval.so file from the build directory (necessary so that the cython fast_eval is eliminated when testing), do:


```
cd $SAGE_ROOT/devel/sage/build
find . -name fast_eval.so | xargs rm
```



---

Comment by jason created at 2010-09-05 02:59:10

Progress report: my current patch queue has the following failures on `make ptestlong` on Sage 4.5.2:


```
	sage -t  -long 4.5.2/devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t  -long 4.5.2/devel/sage/sage/ext/fast_callable.pyx # Exception from doctest framework
	sage -t  -long 4.5.2/devel/sage/sage/rings/polynomial/polynomial_element.pyx # 9 doctests failed
	sage -t  -long 4.5.2/devel/sage/sage/stats/hmm/distributions.pyx # 1 doctests failed

```



---

Comment by jason created at 2010-09-05 03:19:08

(my patch queue is up at http://sage.math.washington.edu/home/jason/sage-4.5.2-patches and this ticket involves patches up to pickling.patch)


---

Comment by kcrisman created at 2011-06-24 14:04:01

What is the status of switching to `fast_callable`?  There seem to be a number of tickets which would benefit, not to mention the fact that `fast_float` has old-style documentation which looks bad in the command line :)  Plus, if `fast_float` is to be deprecated (even though it seems to use `fast_callable` under the hood) it would be helpful to start that process.  

Anyway, just curious.


---

Comment by jason created at 2011-06-24 16:25:35

A long time ago I worked on the patches you see here; I believe that all of my work is here, anyway.  I probably won't have time to work on this this summer, due to notebook enhancements.  I'd like to make this one of the projects for next summer if someone hasn't beaten me to it by then.


---

Comment by jason created at 2011-06-24 16:27:20

The problem is that I think my patch is too big and needs to be broken down into smaller patches that change less at each step.  It's been a long time, but I think I'm remembering that right.  Anyways, as noted above, my patch queue is up on sage.math and anyone is welcome to work on it.


---

Comment by eviatarbach created at 2013-08-10 00:39:00

Can I just create a new patch to switch plotting to use `fast_callable`? Using `fast_float` causes big problems for plotting, namely that any point at which the function is complex at some value in the call stack fails to plot. For example, the plot of `abs(log(x))` will not show up for negative `x`, despite the output being guaranteed to be real, since `fast_float` will evaluate `log(x)` first and choke on the complex number.


---

Comment by jason created at 2013-08-10 00:44:57

Sounds fine to me.  Especially if all the doctests pass (including the new one or two that you write :).


---

Comment by eviatarbach created at 2013-08-10 10:05:24

Okay, thanks. This is now #15030, with a patch up.


---

Comment by kcrisman created at 2014-04-21 13:38:16

Note that #15030 is now merged.  How that does affect whatever else needs to happen here?


---

Comment by rws created at 2018-01-14 08:34:16

Anyone interested in the deprecation of `fast_float` can find relevant tickets at https://trac.sagemath.org/wiki/symbolics#fast_floatdeprecation


---

Comment by rws created at 2018-01-14 13:46:51

Without looking in detail I'd guess that implementing https://github.com/pynac/pynac/issues/8 will make `ex.subs()` a much faster alternative to `fast_callable`.
