# Issue 9130: Access to beta function

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-06-03 15:06:34

Assignee: burcin

CC:  benjaminfjones

Keywords: special function, pynac

Although Maxima has the beta function, Sage doesn't:

```
sage: a, b, c = var('a b c') 
sage: assume(a > 0) 
sage: assume(b > 0) 
sage: x = var('x') 
sage: beta_dist = x**(a-1) * (1 - x)**(b-1) 
sage: c = integral(beta_dist, x, 0, 1) 
sage: c
beta(a, b)
sage: c(a=.5,b=.5)
beta(0.500000000000000, 0.500000000000000)
sage: c(a=.5,b=.5).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/karl-dietercrisman/<ipython console> in <module>()

/Users/karl-dietercrisman/Desktop/sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17042)()

TypeError: cannot evaluate symbolic expression numerically
```

This *is* is Ginac, though, and there is even room for defining it in symbolic/expression.pyx . It probably is also included in some of our other libraries, as a standard special function.


---

Comment by fredrik.johansson created at 2010-06-03 18:04:54

For numerical evaluation, mpmath has beta and also the generalized incomplete beta function for complex arguments. But it's probably easy to do the complete beta function directly with Ginac.

Simplification for rational arguments (beta(0.5,0.5) = pi) would be nice.

Unless someone else wants to work on this, I might have a stab at it within a couple of days.


---

Comment by kcrisman created at 2010-06-03 20:00:30

I wasn't suggesting which of the several packages in Sage should be used for numerical evaluation, though mpmath did come to mind :-)

I don't think that beta(0.5,0.5) would work, given that

```
sage: gamma(0.5)
1.77245385090552
sage: gamma(1/2)
sqrt(pi)
```

but beta(1/2,1/2) becoming pi should work fine once we have a symbolic wrapper (with or without Ginac):

```
sage: maxima_console()
Maxima 5.21.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) beta(1/2,1/2);
(%o1)                                 %pi
```

Please do try to add this!  We definitely often get email asking for various special functions both symbolically and numerically.  Also, the more examples we have, the easier it is to finish off the rest of them by cut and paste.


---

Comment by burcin created at 2010-06-03 20:10:28

GiNaC has a beta function, so this can probably be solved simply by wrapping that. See #8864 for an example.

Though I don't know why the `beta()` function in `sage/symbolic/expression.pyx` is commented. Maybe there is something I'm missing.

Fredrik, it would be great if you can do this. I'd be happy to answer questions if anything goes wrong.


---

Comment by kcrisman created at 2010-06-03 20:15:39

Replying to [comment:3 burcin]:
> GiNaC has a beta function, so this can probably be solved simply by wrapping that. See #8864 for an example.
> 
> Though I don't know why the `beta()` function in `sage/symbolic/expression.pyx` is commented. Maybe there is something I'm missing.
> 

I think the same reason the psi and psi2 ones are commented - when those were implemented, they didn't notice that they had been commented earlier.  This was probably pretty early in the conversion, maybe when William was dealing with CLN (whatever that is)?


---

Comment by burcin created at 2010-06-03 20:28:48

Replying to [comment:4 kcrisman]:
> Replying to [comment:3 burcin]:
> > GiNaC has a beta function, so this can probably be solved simply by wrapping that. See #8864 for an example.
> > 
> > Though I don't know why the `beta()` function in `sage/symbolic/expression.pyx` is commented. Maybe there is something I'm missing.
> > 
> 
> I think the same reason the psi and psi2 ones are commented - when those were implemented, they didn't notice that they had been commented earlier.  This was probably pretty early in the conversion, maybe when William was dealing with CLN (whatever that is)?

`psi()` and `psi2()` were commented because at the time there was no method defined to numerically evaluate those. This is not the case for `beta()` however. Here is the `evalf` method (from line 227 of `ginac/inifcns_gamma.cpp`):


```
	if (is_exactly_a<numeric>(x) && is_exactly_a<numeric>(y)) {
		try {
			return exp(lgamma(ex_to<numeric>(x))+lgamma(ex_to<numeric>(y))-lgamma(ex_to<numeric>(x+y)));
		} catch (const dunno &e) { }
	}
```


We'll find out when someone tries this out I suppose.


---

Comment by burcin created at 2010-08-28 16:15:05

Changing keywords from "special function, pynac" to "special function, pynac, beginner".


---

Attachment


---

Comment by ktkohl created at 2010-12-10 06:17:24

Added ginac wrapper for beta function.
There is a problem when one argument is a float.

--Karen



```
sage: beta(3,2.0)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

```



---

Comment by ktkohl created at 2010-12-10 06:17:24

Changing status from new to needs_work.


---

Attachment

fix segfault in py_float


---

Comment by burcin created at 2011-05-25 18:02:24

Changing keywords from "special function, pynac, beginner" to "special function, pynac".


---

Comment by burcin created at 2011-05-25 18:02:24

Hi Karen,

sorry for taking so long to look at this. It seems that I forgot to check for a NULL pointer in `py_float()`. attachment:trac_9130-py_float_segfault.patch fixes the segfault.


```
sage: from sage.functions.other import beta
sage: beta(3,2.0)
0.0833333333333333
```


Will you have time to finish the patch?

You need to add an import statement to `sage/functions/all.py` so `beta` is available at the command line.  The documentation also needs some care. IIRC there should be an empty line after `INPUT`, `OUTPUT` and `EXAMPLES`. The statement


```
        It is computed by various libraries within Sage, depending on
        the input type.
```


is too vague. We should either remove it or explain how GiNaC evaluates this (see `beta_eval()` and `beta_evalf()` in [inifcns_gamma.cpp](https://bitbucket.org/burcin/pynac/src/51619d2eb90f/ginac/inifcns_gamma.cpp#cl-249)).


---

Comment by ktkohl created at 2012-01-09 15:48:33

Changing keywords from "special function, pynac" to "special function, pynac, sd35.5".


---

Attachment


---

Comment by ktkohl created at 2012-01-10 04:15:53

Changing status from needs_work to needs_review.


---

Comment by ktkohl created at 2012-01-10 15:44:41

include beta in random_tests


---

Attachment

Apply all patches in the order they were added:

* trac_9130_beta_function.patch 

* trac_9130-py_float_segfault.patch

* trac_9130_beta_function.2.patch

* trac_9130_beta_function.3.patch


---

Comment by benjaminfjones created at 2012-01-10 17:27:40

I think we discovered that the only complex inputs that the code accepts are ones where one of the parameters is equal to 1. In that case `beta(1,x) = 1/x` is used to compute the result. Looks like GiNaC can't handle complex inputs at all (or perhaps complex numbers aren't being passed to GiNaC in a way it understands).

On the other hand, [mpmath](http://mpmath.googlecode.com/svn/tags/0.17/doc/build/functions/gamma.html#beta-function) does support evaluation at arbitrary precision complex numbers so that could be a useful enhancement that could take place in a new ticket. 

I would change the docstrings to clearly indicate that
 1. only real inputs are accepted (for now)
 1. beta(1,x) = beta(x,1) = 1/x simplification is automatically applied


---

Comment by benjaminfjones created at 2012-01-10 17:27:40

Changing status from needs_review to needs_work.


---

Comment by ktkohl created at 2012-01-10 20:56:53

updated comments/examples/error message text.


---

Comment by ktkohl created at 2012-01-10 21:09:43

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

combined reviewer patch folding up previously uploaded 5 patches


---

Comment by benjaminfjones created at 2012-01-11 05:30:41

I uploaded a combined *single* patch that folds together the previously uploaded 5 patches applied in order. The patch looks great to me. I have one question about what happens when `GinacFunction`'s `__call__` returns a TypeError whose message doesn't contain "cannot coerce". What gets returned in that case? (the comments in the `gamma` implementation that the try / except block was borrowed from say that TypeErrors are raised when a fast float is passed. These are then ignored in the current implementation? I haven't tested this.

I'm running `make ptestlong` on Sage-4.8.alpha6 with the combined patch applied overnight; will update in the morning.


---

Attachment


---

Comment by burcin created at 2012-01-12 17:06:49

I uploaded a new patch attachment:trac_9130-py_float_segfault.take2.patch which checks for `TypeError` instead of `ValueError` in `sage.symbolic.pynac.py_float()`. Now we can evaluate `beta()` on complex values, so the `__call__()` method in Karen's patches can be removed.


---

Comment by burcin created at 2012-01-12 17:06:49

Changing status from needs_review to needs_work.


---

Attachment

new combined file replacement by trac_9130-py_float_segfault.take2.patch and removal of `__call__()` method


---

Comment by ktkohl created at 2012-01-12 20:52:57

New patch attachment:trac_9130_combined.2.patch replaces burcin's old patch with the newer one and also removes the `__call__()` method in beta.

Apply only this one.


---

Comment by ktkohl created at 2012-01-12 20:52:57

Changing status from needs_work to needs_review.


---

Comment by ktkohl created at 2012-01-12 21:02:51

I added #12303 as a separate ticket to leave beta symbolic for exact complex inputs such as `beta(2,1+5*I)`


---

Comment by burcin created at 2012-01-12 22:51:32

The patch looks great, I have a couple of minor comments. We can switch this to positive review when these are fixed:

 * This paragraph in the docstring is not needed any more:


```
GiNaC is used to compute `B(p,q)`.  However, complex inputs 
are not yet handled in general.  When GiNaC raises an error on 
such inputs, we raise a NotImplementedError. 
```

 Perhaps the first sentence can be merged with the paragraph following that.
 * The commit message for the combined patch is not very helpful. I'd like my patch to stay separate if possible.


---

Comment by burcin created at 2012-01-12 22:51:32

Changing status from needs_review to needs_work.


---

Comment by benjaminfjones created at 2012-01-12 23:22:15

I forgot to update -- with attachment:trac_9130_combined.patch applied to 4.8.alpha6, `make ptestlong` succeeds with no failures! I'll test the updated patch now. 

It should be easy to edit the newest combined patch file to remove the changes from Burcin's patches and just have those applied separately, right?


---

Attachment

combined Karen's patches


---

Comment by burcin created at 2012-02-06 14:45:04

Changing status from needs_work to positive_review.


---

Comment by burcin created at 2012-02-06 14:45:04

I uploaded a new patch which combines Karen's previous patches. This is ready to go now.


---

Comment by burcin created at 2012-02-06 14:46:34

Changing keywords from "special function, pynac, sd35.5" to "special function, pynac, sd35.5 Cernay2012".


---

Comment by kcrisman created at 2012-02-06 18:08:35

Hooray!


---

Comment by jdemeyer created at 2012-02-09 12:52:14

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-09 12:52:14

There are problems building the documentation:

```
/mnt/usb1/scratch/jdemeyer/merger/sage-5.0.beta4/local/lib/python2.7/site-packages/sage/functions/other.py:docstring of sage.functions.other.psi:6: WARNING: Inline literal start-string without end-string.
```



---

Comment by kcrisman created at 2012-02-10 03:36:35

This is because of the addition to the reference manual of stuff that wasn't up to snuff, though almost.  There was an extra colon as well, and a few other similar things.

I've fixed these things, and actually tried adding loads(dumpg()) tests as well, but it doesn't matter, because it's not testing right.  It's not the computer, since other files are passing fine.  It seems to be the symbolic version of beta.

Getting rid of all stuff with `x` and keeping

```
            sage: beta(1,2.0+I)
            0.400000000000000 - 0.200000000000000*I
```

causes

```

$ ../../sage -t sage/functions/other.py 
sage -t  "devel/sage-main/sage/functions/other.py"          
The doctested process was killed by signal 11
	 [6.8 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/functions/other.py" # Killed/crashed
Total time for all tests: 6.9 seconds
```

but removing that as well yields passing tests.

This seems unexpected to me.


---

Comment by kcrisman created at 2012-02-10 03:38:20

Sorry, ignore all that.  I didn't see Burcin's other patch because I read the comments, not the description.


---

Comment by kcrisman created at 2012-02-10 03:57:27

This requires *only* that someone do 

```
./sage -docbuild reference html
```

and look at 

```
devel/sage-main/doc/output/html/en/reference/other.html
```

as well as run tests.


---

Comment by kcrisman created at 2012-02-10 03:57:27

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by kcrisman created at 2012-02-10 03:58:01

Apply last


---

Attachment

To finish:
 * Apply 
   * [attachment:trac_9130-beta_function.patch]
   * [attachment:trac_9130-py_float_segfault.take2.patch]
   * [attachment:trac_9130-reviewer.patch]
 * Check docbuild as above
 * Run tests on other.py, the only file that changed since the last positive review.


---

Comment by benjaminfjones created at 2012-02-10 05:28:18

Changing status from needs_review to positive_review.


---

Comment by benjaminfjones created at 2012-02-10 05:28:18

Finished! The patches apply cleanly to 5.0.beta3, I checked the docs and they look good. All tests pass (I tested sage/functions/other.py and also did `make ptest` for good measure).


---

Comment by jdemeyer created at 2012-02-12 12:47:26

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-12 12:47:26

This patch conflicts with #4498.  Either this one or #4498 should be rebased.


---

Attachment


---

Attachment

fixes random tests after rebasing against #4498


---

Comment by benjaminfjones created at 2012-02-12 20:38:28

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2012-02-12 20:38:28

I rebased the patches against #4498. This meant moving the changes to `sage/symbolic/random_tests.py` out of [attachment:trac_9130_beta_function.patch] and into a new patch [attachment:trac_9130-random-tests.patch] that reflects the differences in the random tests after #4498 was applied and `beta` was added.

The tests in `random_test.py` are getting annoying. Now #9130 must depend on #4498 and in turn my #11888 must depend on #9130, etc. To finish #11143, I need to rebase the changes to `random_tests.py` to all 3 of these other symbolics patches.

Would it make sense to open a new ticket for changes needed to `random_tests.py` after all the new symbolic functions are added that will go into sage-5.0? This new ticket would depend on all the other tickets adding new functions. This way we wouldn't have to fix the random tests like this in every ticket that adds a new function, just *once* per release.


---

Comment by jdemeyer created at 2012-02-13 08:34:16

Replying to [comment:37 benjaminfjones]:
> Would it make sense to open a new ticket for changes needed to `random_tests.py` after all the new symbolic functions are added that will go into sage-5.0? This new ticket would depend on all the other tickets adding new functions. This way we wouldn't have to fix the random tests like this in every ticket that adds a new function, just *once* per release. 

I think that would be making it more complicated for yourself and for reviewers.  It also means that, if just one of those tickets has a problem, none of them can be merged.  But I'm not against your suggestion.


---

Comment by burcin created at 2012-02-13 09:48:23

Replying to [comment:37 benjaminfjones]:
> I rebased the patches against #4498. This meant moving the changes to `sage/symbolic/random_tests.py` out of [attachment:trac_9130_beta_function.patch] and into a new patch [attachment:trac_9130-random-tests.patch] that reflects the differences in the random tests after #4498 was applied and `beta` was added.

Thank you for taking care of this.

> The tests in `random_test.py` are getting annoying. Now #9130 must depend on #4498 and in turn my #11888 must depend on #9130, etc. To finish #11143, I need to rebase the changes to `random_tests.py` to all 3 of these other symbolics patches.
> 
> Would it make sense to open a new ticket for changes needed to `random_tests.py` after all the new symbolic functions are added that will go into sage-5.0? This new ticket would depend on all the other tickets adding new functions. This way we wouldn't have to fix the random tests like this in every ticket that adds a new function, just *once* per release. 

At this stage I'd be happy to mark that test in `random_tests.py` with a `#random` tag so the doctesting framework ignores the output. If you open a new ticket for this and provide a patch, I promise a quick positive review. :)


---

Comment by benjaminfjones created at 2012-02-14 05:39:52

Replying to [comment:39 burcin]:
Thanks, marking the three "offending" doctests with a `random` tag is #12507.


---

Comment by kcrisman created at 2012-02-16 04:45:57

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-02-16 04:45:57

Just checked one _last_ time - yes, everything is fine!  A very minor quibble is that the (why here?) added prime pi file could use a few double backticks and one or two other things, but that is immaterial in this saga.


---

Attachment


---

Attachment

Rebased again.


---

Comment by kcrisman created at 2012-02-21 13:43:27

I think if you would have merged this first, then #12507, there wouldn't have needed to be a rebase.   Maybe the authors of #12507 should have put this as a dependency?  I think we were all lax with it because it `# random`ized a doctest...


---

Comment by jdemeyer created at 2012-02-27 11:19:47

Resolution: fixed
