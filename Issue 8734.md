# Issue 8734: make sage variables unique in maxima

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-04-21 05:45:14

Assignee: was

CC:  was acleone kcrisman robert.marik burcin saliola

This patch prepends a unique string, "_SAGE_VAR_", to each variable name in maxima, to avoid conflicts with existing variables in maxima.


---

Comment by jason created at 2010-04-21 05:54:17

Changing status from new to needs_work.


---

Attachment

I haven't run doctests on everything, but this patch is a start, if one of you wants to take it from here.


---

Comment by kcrisman created at 2010-04-21 13:03:51

I think there might also be another ticket about this somewhere...


---

Comment by robert.marik created at 2010-04-21 13:23:39

Hi, it is also #8634 and there is a dicussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835/06557a921a582f87)


---

Comment by jason created at 2010-05-03 17:36:09

Changing assignee from was to jason.


---

Comment by jason created at 2010-05-03 17:36:09

This should fix #6882


---

Comment by jason created at 2010-05-03 17:37:15

Replying to [comment:5 jason]:
> This should fix #6882

Well, or at least *help* with the solution, anyway.


---

Comment by mpatel created at 2010-08-12 22:47:31

This ticket may also fix #9538.


---

Comment by zimmerma created at 2013-08-25 13:09:45

patch should be rebased, it fails to apply to Sage 5.11:

```
sage: hg_sage.import_patch("/tmp/trac-8734-maxima-vars.patch")
cd "/home/zimmerma/Downloads/sage-5.11/devel/sage" && sage --hg import   "/tmp/trac-8734-maxima-vars.patch"
applying /tmp/trac-8734-maxima-vars.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 1450
Hunk #2 FAILED at 1461
2 out of 2 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
patching file sage/symbolic/assumptions.py
Hunk #1 FAILED at 100
1 out of 1 hunks FAILED -- saving rejects to file sage/symbolic/assumptions.py.rej
abort: patch failed to apply
```

Paul


---

Comment by rws created at 2014-03-08 08:30:52

Rebased on 6.2.beta3

Patch doesn't seem ready:

```
sage -t --long src/sage/symbolic/integration/integral.py  # 3 doctests failed
sage -t --long src/sage/symbolic/assumptions.py  # 26 doctests failed
sage -t --long src/sage/symbolic/pynac.pyx  # 1 doctest failed
sage -t --long src/sage/symbolic/expression.pyx  # 21 doctests failed
sage -t --long src/sage/calculus/desolvers.py  # 63 doctests failed
sage -t --long src/sage/calculus/calculus.py  # 13 doctests failed
sage -t --long src/sage/calculus/functional.py  # 1 doctest failed
```

----
New commits:


---

Comment by git created at 2014-03-22 15:29:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-03-22 15:31:01

This fixes the errors in symbolic. More to come...


---

Comment by kcrisman created at 2014-03-22 15:59:13

Thanks for working on this!  This could also then eventually lead to a way to deal with the extra variables that come from e.g. differential equation solvers in Maxima - if we picked up a non-existent (in Sage) variable, we could perhaps do something with it.  (There are tickets about this out there, so I won't repeat that discussion.)


---

Comment by git created at 2014-03-24 15:10:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-03-24 15:13:17

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-03-24 15:13:17

This fixes the last doctests, mainly by handling the desolver entry points.


---

Comment by vbraun created at 2014-04-14 22:49:09

Merge conflict, please merge in the latest beta


---

Comment by rws created at 2014-04-15 06:17:25

New commits:


---

Comment by vbraun created at 2014-04-15 11:02:22


```
sage -t --long src/sage/functions/bessel.py  # 3 doctests failed
sage -t --long src/sage/interfaces/maxima_abstract.py  # 16 doctests failed
sage -t --long src/sage/tests/french_book/recequadiff.py  # 1 doctest failed
sage -t --long src/sage/interfaces/maxima.py  # 2 doctests failed
sage -t --long src/doc/en/constructions/calculus.rst  # 2 doctests failed
sage -t --long src/sage/interfaces/maxima_lib.py  # 11 doctests failed
sage -t --long src/sage/functions/other.py  # 4 doctests failed
sage -t --long src/sage/functions/orthogonal_polys.py  # 5 doctests failed
sage -t --long src/sage/symbolic/expression_conversions.py  # 2 doctests failed
sage -t --long src/sage/interfaces/interface.py  # 10 doctests failed
```



---

Comment by vbraun created at 2014-04-15 11:02:28

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-04-15 16:44:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-17 08:50:59

Concerning the remaining doctests in `interfaces/maxima_abstract.py` I am at a loss at what to do. For example this

```
sage: x,y = var('x,y'); f = maxima.function('x','sin(x)')
sage: type(f)
<class 'sage.interfaces.maxima.MaximaElementFunction'>
sage: g=maxima.cos(x)
sage: type(g)
<class 'sage.interfaces.maxima.MaximaElement'>
sage: f+g
cos(_SAGE_VAR_x)+sin(x)
sage: (f+g)(2)
cos(_SAGE_VAR_x)+sin(2)
```

shows that while the `MaximaElementFunction f` has the variable `x` which is associated with `_SAGE_VAR_x` in Maxima (and calling the function works as expected), the `MaximaElement g` shows `_SAGE_VAR_x` which has of course no Maxima pendant (and calling the function bombs). Naively both should behave identically.


```
sage: h=SR(maxima.cos(x))
sage: h
cos(x)
sage: h(2)
cos(2)
sage: f+h
cos(_SAGE_VAR_x)+sin(x)
sage: (f+h)(2)
cos(_SAGE_VAR_x)+sin(2)
```

Moreover, if `g` gets converted to `SR` it behaves fine but when converted to `type(f)` by using it as rhs it gets `_SAGE_VAR_x` as parameter. What is the next step?


---

Comment by rws created at 2014-04-18 14:33:49

As far as I understand now, a `MaximaElementFunction` is a function defined within the Maxima process, and so `x` is the parameter name, not a registered variable. Thus the output `sin(x)` makes sense. OTOH any `_SAGE_VAR_x` that appears in a `MaximaElement` repr refers to a registered variable within Maxima that is associated with a registered Sage var named `x`. Let's interpret the above output in the light of this.
> {{{
> sage: f+g
> cos(_SAGE_VAR_x)+sin(x)
> }}}
Correct but can the user make sense of it?
> {{{
> sage: (f+g)(2)
> cos(_SAGE_VAR_x)+sin(2)
> }}}
That is not less correct than

```
sage: (sin(x)+cos(y))(2)
cos(y) + sin(2)
```

and it just seems to be another case of `SR._call_element_()` where is stated: "Note that you make get unexpected results when calling symbolic expressions and not explicitly giving the variables."

Moreover, it was a hack that this worked at all in the `MaximaAbstractElementFunction._add_()` doctests because

```
sage: f = maxima.function('z','sin(z)')
sage: f
sin(z)
sage: f(2)
sin(2)
sage: (sin(z))(2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
NameError: name 'z' is not defined
```



---

Comment by git created at 2014-04-18 14:57:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-18 14:58:21

Changing status from needs_work to needs_review.


---

Comment by git created at 2014-05-26 09:29:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-26 13:57:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-06-06 13:23:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-06-06 13:50:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-06-06 14:40:48

Hi!  Thanks for keeping at this.  I'll try to look at it one final time soon - waiting for the latest beta to compile.  In the meantime:

I like the renaming and doctesting of the missing assumption function, and I agree with your analysis of the Maxima 'parameters', as you call them - yes, those are completely separate from Sage.  I would encourage you to be even more explicit than

```
The parameter ``x`` is different from the symbolic variable::
```

by saying something about it being a _Maxima_ parameter versus _Sage_ symbolic variable.  Does that make sense?

Also, don't worry too much about the 'todo' in `doc/en/constructions/calculus.rst`.  That is truly ancient, from the days where legendary heroes of yore managed to bring calculus functionality, despite awkward syntax, into an algebraic geometry program... meaning eventually that should be just rewritten to use "native syntax" or just folded into the calculus documentation.


---

Comment by git created at 2014-06-07 05:32:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-06-17 15:11:17

Okay, here are a few questions.  I am pretty sure the answers are very straightforward, but I want to make sure it's clear - in case we might want to add a doctest, for instance.
* Commit 	be9367 (where you add a try/except clause in `_create`) - what sort of situation is that catching?  (Also, did you change all of the doctests with assumptions, or leave a few just so people see what the full form looks like?)
* Commit 	ced268 (where you generalized the missing assumptions) - what situation is that additionally catching?  Was that a case of Maxima asking questions which we didn't catch (and hence doctest) before?
* I assume you are more than happy with Jason's original patch doing the basic functionality, right?

The only part I haven't had a chance to really dig into is the differential equations changes (Commit a74ec0).  I assume there isn't an obvious more modular way to deal with those :( but I don't have time currently to go through this in detail.  My main issue (not really a concern, just my lack of being convinced yet) is just seeing that we really aren't over-replacing or under-replacing in that.

So these are pretty minor things and hopefully I'll be able to find some time for the DE part (or someone else will!) and we'll be on our way!  It certainly looks like you were VERY thorough in finding places that might cause trouble.  The difficulty is that one might miss some places it is needed because in the absence of adding `_SAGE_VAR_` things should still work, so one might not know if we missed one.  Thanks!


---

Comment by rws created at 2014-06-17 15:45:47

Replying to [comment:37 kcrisman]:
> Okay, here are a few questions.  I am pretty sure the answers are very straightforward, but I want to make sure it's clear - in case we might want to add a doctest, for instance.
Sure, as long as you remember "The perfect is the enemy of the good." 
> * Commit 	be9367 (where you add a try/except clause in `_create`) - what sort of situation is that catching?
There are several places where maxima.eval() is called and where exceptions are thrown. This one was simply overlooked, so that change fixes an unreported bug.
>(Also, did you change all of the doctests with assumptions, or leave a few just so people see what the full form looks like?)
Yes.
> * Commit 	ced268 (where you generalized the missing assumptions) - what situation is that additionally catching?  Was that a case of Maxima asking questions which we didn't catch (and hence doctest) before?
No, it reduces code duplication. Recommended reading: https://en.wikipedia.org/wiki/Code_refactoring
> * I assume you are more than happy with Jason's original patch doing the basic functionality, right?
Yes and no. A lot was missing.
> ...
> So these are pretty minor things and hopefully I'll be able to find some time for the DE part (or someone else will!) and we'll be on our way!  It certainly looks like you were VERY thorough in finding places that might cause trouble.  The difficulty is that one might miss some places it is needed because in the absence of adding `_SAGE_VAR_` things should still work, so one might not know if we missed one.  Thanks!
I would assume this is caught by all those doctests using maxima.


---

Comment by git created at 2014-06-17 15:47:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-06-17 15:48:17

The output changed recently and I forgot to fix one doctest.


---

Comment by kcrisman created at 2014-06-17 16:04:10

> > Okay, here are a few questions.  I am pretty sure the answers are very straightforward, but I want to make sure it's clear - in case we might want to add a doctest, for instance.
> Sure, as long as you remember "The perfect is the enemy of the good." 
Of course!
> > * Commit 	be9367 (where you add a try/except clause in `_create`) - what sort of situation is that catching?
> There are several places where maxima.eval() is called and where exceptions are thrown. This one was simply overlooked, so that change fixes an unreported bug.
Hmm, okay.  I don't see how `_create` could have asked for an evaluation of this type, but I suppose.
> > * Commit 	ced268 (where you generalized the missing assumptions) - what situation is that additionally catching?  Was that a case of Maxima asking questions which we didn't catch (and hence doctest) before?
> No, it reduces code duplication. Recommended reading: https://en.wikipedia.org/wiki/Code_refactoring
I'm not referring to that; in fact, I fully agreed with that strategy in earlier comments.  My question is specifically about `jj=2` - since usually `jj=3` seems to be the old case.  We should test a new branch, which this appears to be (though it may just be something obvious I'm not seeing).
> > * I assume you are more than happy with Jason's original patch doing the basic functionality, right?
> Yes and no. A lot was missing.
I mean in terms of reviewing that for the _basic_ functionality for proper conversion.  Naturally you provided a huge amount of missing stuff!
> > So these are pretty minor things and hopefully I'll be able to find some time for the DE part (or someone else will!) and we'll be on our way!  It certainly looks like you were VERY thorough in finding places that might cause trouble.  The difficulty is that one might miss some places it is needed because in the absence of adding `_SAGE_VAR_` things should still work, so one might not know if we missed one.  Thanks!
> I would assume this is caught by all those doctests using maxima.
That's my point - they may NOT catch a missing one, since we only remove things via search-and-replace-with-empty-string, and everything worked before.


---

Comment by rws created at 2014-06-18 08:39:13

Replying to [comment:41 kcrisman]:
> > > * Commit 	be9367 (where you add a try/except clause in `_create`) - what sort of situation is that catching?
> > There are several places where maxima.eval() is called and where exceptions are thrown. This one was simply overlooked, so that change fixes an unreported bug.
> Hmm, okay.  I don't see how `_create` could have asked for an evaluation of this type, but I suppose.
It is really easy to find it out yourself: just change `RuntimeError` to something different like `NotImplementedError`, doctest, and you'll get:

```
sage -t src/sage/tests/french_book/recequadiff.py
**********************************************************************
File "src/sage/tests/french_book/recequadiff.py", line 247, in sage.tests.french_book.recequadiff
Failed example:
    desolve(eq1,[f,x])
Expected:
    Traceback (most recent call last):
      ...
    TypeError: Computation failed ...
    Is k positive, negative or zero?
Got:
    <BLANKLINE>
    Traceback (most recent call last):
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 480, in _run
        self.execute(example, compiled, test.globs)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 839, in execute
        exec compiled in globs
      File "<doctest sage.tests.french_book.recequadiff[64]>", line 1, in <module>
        desolve(eq1,[f,x])
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/calculus/desolvers.py", line 436, in desolve
        soln = P(cmd)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/interfaces/interface.py", line 199, in __call__
        return cls(self, x, name=name)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/interfaces/interface.py", line 626, in __init__
        raise TypeError(x)
    TypeError: ECL says: Maxima asks: Is _SAGE_VAR_k positive, negative or zero?
```

> > > * Commit 	ced268 (where you generalized the missing assumptions) - what situation is that additionally catching?  Was that a case of Maxima asking questions which we didn't catch (and hence doctest) before?
> > No, it reduces code duplication. Recommended reading: https://en.wikipedia.org/wiki/Code_refactoring
> I'm not referring to that; in fact, I fully agreed with that strategy in earlier comments.  My question is specifically about `jj=2` - since usually `jj=3` seems to be the old case.  We should test a new branch, which this appears to be (though it may just be something obvious I'm not seeing).
There were cases where there were two spaces in the output after 'Is '.
> > > * I assume you are more than happy with Jason's original patch doing the basic functionality, right?
> > Yes and no. A lot was missing.
> I mean in terms of reviewing that for the _basic_ functionality for proper conversion.  Naturally you provided a huge amount of missing stuff!
I think his ansatz was what I would have done, too.
> > > So these are pretty minor things and hopefully I'll be able to find some time for the DE part (or someone else will!) and we'll be on our way!  It certainly looks like you were VERY thorough in finding places that might cause trouble.  The difficulty is that one might miss some places it is needed because in the absence of adding `_SAGE_VAR_` things should still work, so one might not know if we missed one.  Thanks!
> > I would assume this is caught by all those doctests using maxima.
> That's my point - they may NOT catch a missing one, since we only remove things via search-and-replace-with-empty-string, and everything worked before.
Can you please clarify: "one might miss some places it is needed"---what's the it here?


---

Comment by kcrisman created at 2014-06-18 15:26:35

> There were cases where there were two spaces in the output after 'Is '.
Annoying.
> > That's my point - they may NOT catch a missing one, since we only remove things via search-and-replace-with-empty-string, and everything worked before.
> Can you please clarify: "one might miss some places it is needed"---what's the it here? 
What I mean is that if one had missed a place where we should have added `SAGE_VAR` but didn't, we might not know because the result would not need `SAGE_VAR` stripped from it, so it would perhaps still work.  But I'm not overly concerned about this ... because it would still work.

----

Anyway, if someone reviews the diffeq part before me (I won't have time before next week), that is all I think still needs review.  This will be great to finally have in!


---

Comment by nbruin created at 2014-06-18 20:47:28

For the

```
try:
 ....
except ... as error:
 ...
    raise error
```

in maxima_lib.py (and possibly elsewhere):
It's *much* better to reraise an error with a bare `raise` rather than `raise error`, since the bare raise will leave the original traceback intact, whereas the `raise error` will create a new traceback, obscuring the actual source of the error.


---

Comment by rws created at 2014-06-19 09:20:53

Replying to [comment:44 nbruin]:
> For the
> {{{
> try:
>  ....
> except ... as error:
>  ...
>     raise error
> }}}
> in maxima_lib.py (and possibly elsewhere):
> It's *much* better to reraise an error with a bare `raise` rather than `raise error`, since the bare raise will leave the original traceback intact, whereas the `raise error` will create a new traceback, obscuring the actual source of the error.
In this case, yes. Else, are you requesting to rethrow the `RuntimeError` from Maxima in all cases as `RuntimeError`? I'm asking because it appears that preserving the stacktrace and throwing the more specific `ValueError` appears possible:
http://www.gossamer-threads.com/lists/python/python/947257

```
In Python 3 you could chain the exceptions with: 

except Exception as e: 
raise CustomException() from e 

There is no such syntax in Python 2, but you could manually store and 
retrieve the __cause__ and __traceback__ attributes similarly to the 
way Python 3 does it. See PEP 3134 for full details. 
```

http://legacy.python.org/dev/peps/pep-3134/

```
Sometimes it can be useful for an exception handler to intentionally
    re-raise an exception, either to provide extra information or to
    translate an exception to another type. ...
```



---

Comment by git created at 2014-06-19 09:22:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nbruin created at 2014-06-19 13:19:29

Replying to [comment:45 rws]:
> In this case, yes. Else, are you requesting to rethrow the `RuntimeError` from Maxima in all cases as `RuntimeError`? I'm asking because it appears that preserving the stacktrace and throwing the more specific `ValueError` appears possible:

Good to know! I don't have a strong opinion what type of error to return. However, without further inspection, I don't think you would know if the error is more appropriately a `ValueError`. You could get `RuntimeError("ECL says: I'm tired")`for as far as you know at this point. So my guess is that it's not worth trying to do something with the error type.


---

Comment by rws created at 2014-06-20 07:28:18

All the following is modulo my Python newbieness.

What I wrote about legal tricks to preserve the traceback would work IF Sage was purely Python-2 or Python-3. With the momentary transition to Py-3, the form `raise Error, message, traceback` of the raise command is considered a bug. OTOH there is no way to supply two arguments in parentheses. Finally, the form `raise Error from previous_error` is only possible with Py-3.

Secondly, to ask interactively for a missing assumption a message has to be given in the terminal different from the error message tied to the original `RuntimeError`. So, simply re-raising is not an option if you do not like `RuntimeError: ECL says: Maxima asks: Is _SAGE_VAR_a an integer?`.

So, in my opinion, unless someone comes up with a better solution, this ticket will have to wait until Sage is Py-3.


---

Comment by nbruin created at 2014-06-20 12:54:30

Replying to [comment:48 rws]:
> Secondly, to ask interactively for a missing assumption a message has to be given in the terminal different from the error message tied to the original `RuntimeError`. So, simply re-raising is not an option if you do not like `RuntimeError: ECL says: Maxima asks: Is _SAGE_VAR_a an integer?`.

In that case we know exactly what happened and the original traceback doesn't have to be kept. Raising a a fresh exception with a fresh traceback should be fine. It's when you find that the `RuntimeError` you've just caught is *not* the one you expected that the original traceback is valuable. And in that case you probably don't want to mess with the exception object itself either, so a bare `raise` should do the trick. The scenario of changing the error object but keeping the original traceback should be quite rare.

> So, in my opinion, unless someone comes up with a better solution, this ticket will have to wait until Sage is Py-3.

which may be a very long time. It nice to do things in a Py2/Py3 compatible way if possible (which can be done here, I think), but if not we'll just have to fix it if/when sage transitions from Py2 to Py3.


---

Comment by kcrisman created at 2014-06-20 13:08:40

> > So, in my opinion, unless someone comes up with a better solution, this ticket will have to wait until Sage is Py-3.
> 
> which may be a very long time. 
Indeed.
> It nice to do things in a Py2/Py3 compatible way if possible (which can be done here, I think), but if not we'll just have to fix it if/when sage transitions from Py2 to Py3.
I'm not quite clear on why this is the case.  I thought you said above to not let the perfect be the enemy of the good ;-)  It seems like just raising the original exception is a good compromise here; at the very least it should give _some_ information, right?


---

Comment by rws created at 2014-06-20 13:46:25

I agree I was the perfectionist this time so, with the bare raise patch already uploaded, it remains for me to thank you and ask for positive review.


---

Comment by kcrisman created at 2014-06-20 17:20:36

Again, for me, all is positive review except the diffeq commit, and that only because I haven't had time to look carefully at it, not because I suspect any problems - it looks quite thorough.


---

Comment by kcrisman created at 2014-06-26 14:06:59

Okay, I have a few questions about [the ode changes](http://git.sagemath.org/sage.git/diff/src/sage/calculus/desolvers.py?id=610fb79bfc9fde84dea1200fdfcd4bceb25bd77f).   I assume the answer to all of them is "it would have been even messier any other way", but I just wanted to check.
 * In some of the sanitizing functions, you replace things like `'_SAGE_VAR_f` with `f`, but in others you only replace the independent variable that way.  Is that because of specific examples that didn't work, or was the context different, or... ? 
 * I'm wondering whether the Sage translation would have just taken care of this in `soln.sage()`, but I guess it didn't.   Was there any possible change to the translation that could have done this, rather than getting into the ode wrapper code directly (which makes it harder to read)?  For instance, in `desolve_laplace` we convert the `de` to Maxima (presumably adding `SAGE_VAR`, add another `SAGE_VAR` from `f(x)` to `f(_SAGE_VAR_x)` (I think), and then proceed to remove only the `SAGE_VAR` from the _de_pendent variable.  So... that part isn't taken care of by the translation, but the independent variable still somehow is translated back correctly, but not forward within `de0=de._maxima_()`?  Yet in the `rk4` types this isn't a problem, apparently.
 * We should probably just remove `desolve_system_strings`, see #8132 where it was first said to be obsolete, and it hasn't been in the global namespace since before 2010.  That is pretty much equivalent to a deprecation to me.  However, we should keep any non-overlapping examples - so maybe removal should be another ticket...
But it seems good, assuming I didn't miss any tests that fail...


---

Comment by kcrisman created at 2014-06-26 14:54:36

> But it seems good, assuming I didn't miss any tests that fail...
I didn't.  So as long as you give the answers I expect, we are all set here.


---

Comment by rws created at 2014-06-27 14:28:48

Working from the bottom up ...

Replying to [comment:54 kcrisman]:
>  * We should probably just remove `desolve_system_strings`, see #8132 where it was first said to be obsolete, and it hasn't been in the global namespace since before 2010.  That is pretty much equivalent to a deprecation to me.  However, we should keep any non-overlapping examples - so maybe removal should be another ticket...

This is now #16568.


---

Comment by git created at 2014-06-29 08:29:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-06-29 08:50:14

Replying to [comment:54 kcrisman]:
>  * In some of the sanitizing functions, you replace things like `'_SAGE_VAR_f` with `f`, but in others you only replace the independent variable that way.  Is that because of specific examples that didn't work, or was the context different, or... ? 
It certainly was then because of specific examples. The removal of the code I think you mean makes no difference now, however.
>  * I'm wondering whether the Sage translation would have just taken care of this in `soln.sage()`, but I guess it didn't.   Was there any possible change to the translation that could have done this, rather than getting into the ode wrapper code directly (which makes it harder to read)?  For instance, in `desolve_laplace` we convert the `de` to Maxima (presumably adding `SAGE_VAR`, add another `SAGE_VAR` from `f(x)` to `f(_SAGE_VAR_x)` (I think), and then proceed to remove only the `SAGE_VAR` from the _de_pendent variable.  So... that part isn't taken care of by the translation, but the independent variable still somehow is translated back correctly, but not forward within `de0=de._maxima_()`?  Yet in the `rk4` types this isn't a problem, apparently.
With the above removal of superfluous code I don't see any different behaviour in the three functions `laplace/system/rk4`. There is always the marking of the dependent var to prepare for the call to solve. You cannot remove this because `maxima(cmd)` does no translation, it's the low-level call. The translation has to be done here, as far as I understand.


---

Comment by kcrisman created at 2014-07-02 02:55:46

> With the above removal of superfluous code I don't see any different behaviour in the three functions `laplace/system/rk4`. There is always the marking of the dependent var to prepare for the call to solve. You cannot remove this because `maxima(cmd)` does no translation, it's the low-level call. The translation has to be done here, as far as I understand.
Again, I'm just confused because in `laplace/rk4` the dependent variable gets `_SAGE_VAR_` but in `desolve` it doesn't.  Maybe this isn't important, though.  And is the last change in `desolve` ok because putting things into Maxima takes care of the `_SAGE_VAR_` already?


---

Comment by kcrisman created at 2014-07-02 12:52:21

Passes all tests.


---

Comment by rws created at 2014-07-02 15:13:04

After studying this in detail, the reason why the last change makes no difference is the following: in `desolve` and `desolve_laplace` the translation to Maxima is applied several times using `maxima()` and `P()` (which is the parent of the first translation result, i.e. of a Maxima expression). `P()` is also applied to `dvar.operator()` resulting in `dvar_str` which already has `_SAGE_VAR_` and is template for sanitization. Appending `_SAGE_VAR_` to `dvar_str` and replacing it thus was useless.

In `desolve_rk4` the `cmd` is constructed from two parts: the `de0` that gets translated via `._maxima()_` and the construction via string concatenation. So, there is no difference between `desolve` and `desolve_rk4` because `desolve` gets `_SAGE_VAR_` everywhere and `desolve_rk4` too.


---

Comment by kcrisman created at 2014-07-02 15:45:37

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-07-02 15:45:37

Let's make it so, then.  I was kind of suspecting there were extra `_SAGE_VAR_`s.


---

Comment by vbraun created at 2014-07-03 02:07:16

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2014-07-03 02:07:16

conflicts with #6882


---

Comment by git created at 2014-07-03 06:12:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-07-03 06:17:25

Changing status from needs_work to positive_review.


---

Comment by rws created at 2014-07-03 06:17:25

Since the reviewed #6882 is orthogonal I set positive again. Thanks Karl-Dieter for this review! I would be happy if you could have a look at #2516 too.


---

Comment by kcrisman created at 2014-07-03 13:17:23

> I would be happy if you could have a look at #2516 too.
Sorry, that one I definitely like the idea of and have reviewed many similar ones in the past, but just don't have the time currently to review much new functionality carefully. :(


---

Comment by vbraun created at 2014-07-06 17:55:56

Resolution: fixed
