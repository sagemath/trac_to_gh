# Issue 9975: Decorated functions/methods have generic signature in documentation

Issue created by migration from https://trac.sagemath.org/ticket/9976

Original creator: jsrn

Original creation time: 2010-09-23 12:07:21

Assignee: mvngu

CC:  jason kcrisman jhpalmieri novoselt

Keywords: sphinx, documentation

Functions or methods that have been decorated by generic decorators such as sage.misc.decorators.options (moved from sage.misc.plot.options with Trac #9907) degrade documentation by reducing the signature for these callables to the generic "(*args, **kwargs)".

See also the following sage.devel discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/cbd888f0e60130ff/f533792113c45c2f


---

Comment by jsrn created at 2010-09-23 12:15:01

Fixes the issue by patching Sage's version of Sphinx to look for a custom attribute in functions and methods.


---

Attachment

Note that the attached patch assumes Trac #9907 (which in turn assumes #9919). Sorry for the chain of Tracs, but I believe the others are just about finished, so it seems like wasted extra work to first make a version without the dependency and then patch this.


---

Comment by jsrn created at 2010-09-23 12:16:35

Changing status from new to needs_review.


---

Comment by jsrn created at 2010-10-07 12:52:29

Now I've finished, cleaned up and tested an alternative patch. It is a slightly more invasive change to the Sphinx autodoc algorithm, and it is a little less intuitive than the other, but it makes it easier for decorators to change the signature of the wrapped function (currently, only `@`option and `@`suboption uses this).

In the other patch we used the attribute _sage_decorating which returns the wrapped function to tell Sphinx that it should behave specially, but in the new patch, the decorating callable should now instead define an attribute _sage_getargspec. This should be a function returning an argspec (an argspec is an python.inspect.ArgSpec tuple as returned by python.inspect.getargspec -- basically describing the elements of a function's signature) with the help of an "argspec-retrieving function" taken as argument. This recursive way of doing things is for avoiding the logic within Sphinx of getting the argspec for various types of functions (e.g. Python, Cython or built-in). When Sphinx is asked to format the signature of a function, and that function defines _sage_getargspec, it formats in a standard way whatever _sage_getargspec(getter) returns, where getter is basically itself (that is, the Sphinx function currently being asked to find the argspec of some function).

So for example, `@`option defines an _sage_getargspec which takes Sphinx's own argspec-finding function -- let's call that getter. _sage_getargspec(getter) then uses getter on the wrapped function, getting the function's original argspec. To this, it adds the options given as arguments to the decorator. This is then returned to Sphinx which formats it and outputs that as the signature for the decorated function.


---

Comment by jsrn created at 2010-12-09 10:30:45

I personally prefer the advanced and intrusive patch as it allows more flexibility for the usual developer. I hope that decorators could be more widely used after this patch is introduced, as they are really handy for many things.
So for the everyone -- and in particular the patch buildbot:
Apply trac_9976_decorated_generic_sigs_alternative.patch


---

Comment by SimonKing created at 2011-04-04 13:39:50

I am currently working on a related problem, namely a Cython version of the cached_method decorators - see #11115.

Why is that related?

What one would like to do in this case is to preserve the documentation (and also the source code, file and argspec) of the wrapped function. But if it is Cython, one can not simply override `__doc__`: Even if `__doc__` is defined cdef public, the doc builder would still pick up the the documentation of the decorator, not of the wrapped function.

The obvious solution is to consequently use `sage.misc.sageinspect.sage_getdoc` and related methods. Like `sage_getargspec`, it allows for more flexibility.

So, what I would like to do is to edit `doc/common/builder.py` and replace the calls to `inspect` by the corresponding calls to `sageinspect`, and also replace `__doc__`.

But shall I post that here, since it is related? Or shall I open a new ticket, since, after all, the patch here does not touch `builder.py`?

Best regards,

Simon


---

Comment by SimonKing created at 2011-04-04 13:41:41

Replying to [comment:9 SimonKing]:
> 
> So, what I would like to do is to edit `doc/common/builder.py` and replace the calls to `inspect` by the corresponding calls to `sageinspect`, and also replace `__doc__`.

Oops, me stupid!

I just realised that I was not editing `builder.py` but `sage_autodoc.py`. So, we _do_ work on the same file.

I guess that means that I should post my patch here, right?

Best regards,
Simon


---

Comment by jsrn created at 2011-04-04 14:30:07

The part about decorators shadowing Cython callable's doc, source code, file, etc. definitely sounds like the same. I guessed that something similar would be wrong with Cython, but I don't write Cython so it was tedious to try and dig up. Good that you came across it. I don't see why this ticket shouldn't encompass both patches for completeness.

I guess that your sage_autodoc patch is not about the cache functionality of your `@`cached_method decorator -- that is obviously not related to this ticket ;-)

Cheers,
Johan


---

Comment by SimonKing created at 2011-04-04 16:39:37

Replying to [comment:11 jsrn]:
> I guess that your sage_autodoc patch is not about the cache functionality of your `@`cached_method decorator -- that is obviously not related to this ticket ;-)

Of course! This ticket will eventually become a dependency for #11115.

What I intend to do: Modify the `sage_get...` functions from `sage.misc.sageinspect` such that they also work on classes: If you have a class with an attribute `_sage_doc_` then this attribute would be called - resulting in a type error that is not caught:

```
sage: class MyClass:
....:     def _sage_doc_(self):
....:         return "my doc"
....:
sage: O = MyClass()
sage: sage.misc.sageinspect.sage_getdoc(O)
'my doc\n'
sage: sage.misc.sageinspect.sage_getdoc(MyClass)
Traceback (most recent call last):
...
TypeError: unbound method _sage_doc_() must be called with MyClass instance as first argument (got nothing instead)
```


If that is fixed (similarly in the other `sage_get...`) then I suggest to replace all calls to `inspect.get...` and to `...__doc__` by the corresponding function from `sage.misc.sageinspect`.

Best regards,

Simon


---

Comment by SimonKing created at 2011-04-04 17:26:38

What I would like to have is:

```
sage: class MyClass:
....:     "Class documentation"
....:     def _sage_doc_(self):
....:         return "Instance documentation"
....:
sage: sage.misc.sageinspect.sage_getdoc(MyClass())
'Instance documention\n'
sage: sage.misc.sageinspect.sage_getdoc(MyClass)
'Class documentation\n'
```


Then, using `sage_getdoc` in `sage_autodoc.py` would mean that "usual" methods of a class would be documented according to their doc string. But if it is a decorated method (at least, the following holds true for ``@`cached_method`) then the attribute of the class is in fact a class instance:

```
sage: class MyClass:
....:     @cached_method
....:     def f(x):
....:         return -x
....:     def g(x):
....:         return -x
....:
sage: MyClass.g.__class__
<type 'instancemethod'>
sage: MyClass.f.__class__
<type 'sage.misc.cachefunc.CachedMethodCaller'>
```


So, if the decorator has `_sage_doc_` and `_sage_argspec_` then it can be used when building the reference.


---

Comment by SimonKing created at 2011-04-05 05:58:05

I see this error when building the documentation:

```
/mnt/local/king/SAGE/broken/devel/sage/doc/en/reference/sage/plot/complex_plot.rst:7: (WARNING/2) error while formatting signature for sage.plot.complex_plot.complex_plot: 'tuple' object has no attribute 'args'
```


Admittedly this is after I edited sage_autodoc to use more from sageinspect. However, it concerns a part that I did not touch, namely apparently the method `format_args(self)` in sage_autodoc.


---

Comment by SimonKing created at 2011-04-05 07:10:21

How is the documentation of a class, method etc. actually obtained? There is a method  `get_doc` in sage_autodoc.py, but it was not called when I expected it.

Could it by the the work is done by the method `find_attr_docs()` of `sphinx.pycode.ModuleAnalyzer`? That would be bad, because certainly it is ignorant to methods such as `_sage_doc_()`!

By consequence, if one has a method that is decorated by a cython class (something that I plan for the cached_method decorator) then the documentation will be that of the cython class, not that of the decorated method.

So, could it be that we have to replace `sphinx.pycode.ModuleAnalyzer`?


---

Comment by jsrn created at 2011-04-05 09:55:53

Replying to [comment:14 SimonKing]:
> I see this error when building the documentation:
> {{{
> /mnt/local/king/SAGE/broken/devel/sage/doc/en/reference/sage/plot/complex_plot.rst:7: (WARNING/2) error while formatting signature for sage.plot.complex_plot.complex_plot: 'tuple' object has no attribute 'args'
> }}}
> 
> Admittedly this is after I edited sage_autodoc to use more from sageinspect. However, it concerns a part that I did not touch, namely apparently the method `format_args(self)` in sage_autodoc.

I don't know about that error. On my current version of sage 4.6.2 it applies and compiles with no problems; I am currently updating to 4.7.alpha3 to test it there...


---

Comment by jsrn created at 2011-04-05 10:08:29

Changing status from needs_review to needs_work.


---

Comment by jsrn created at 2011-04-05 10:08:29

Replying to [comment:15 SimonKing]:
> How is the documentation of a class, method etc. actually obtained? There is a method  `get_doc` in sage_autodoc.py, but it was not called when I expected it.

That is indeed surprising; I would have thought that was constructing the documentation. You are aware that there are two get_doc functions: one in the Documenter class (which is the father of all documenters), and the overwritten in the ClassLevelDocumenter subclass? So if you were monitoring Documenter's get_doc but were for the documentation of a method or attribute, you would not see the call (I'm compiling, so I can't test myself just now).

> 
> Could it by the the work is done by the method `find_attr_docs()` of `sphinx.pycode.ModuleAnalyzer`? That would be bad, because certainly it is ignorant to methods such as `_sage_doc_()`!
> 
> By consequence, if one has a method that is decorated by a cython class (something that I plan for the cached_method decorator) then the documentation will be that of the cython class, not that of the decorated method.
> 
> So, could it be that we have to replace `sphinx.pycode.ModuleAnalyzer`?

I hope not. For this ticket, I originally only looked at where the argument string was formatted and that is in sage_autodoc.py. ModuleAnalyzer is (only?) called on line 624 (unpatched) with the following comment: "try to also get a source code analyzer for attribute docs". If what you are suggesting above is true, we should be able to wrap these lines with some exceptions in the cases where a _sage_doc attribute has been set on the object.


---

Comment by SimonKing created at 2011-04-05 15:14:04

Replying to [comment:17 jsrn]:
> Replying to [comment:15 SimonKing]:
> > How is the documentation of a class, method etc. actually obtained? There is a method  `get_doc` in sage_autodoc.py, but it was not called when I expected it.
> 
> That is indeed surprising; I would have thought that was constructing the documentation. You are aware that there are two get_doc functions: one in the Documenter class (which is the father of all documenters), and the overwritten in the ClassLevelDocumenter subclass?

I inserted commands into both `get_doc` methods that I found in `sage_autodoc.py that should write some status reports into a file called "simon_logfile" somewhere in my home directory. After deleting one file in doc/output/html/en/reference and doing `sage -docbuild reference html`, no file called "simon_logfile" can be found anywhere on the disk (even outside my home directory).

Then, I bumped it up, and inserted a `raise RuntimeError` into the first line of both methods. Nevertheless, the documentation builds as it did before.

So, I must conclude that neither version of `get_doc` is used to get documentation.


---

Comment by SimonKing created at 2011-04-05 15:58:25

Replying to [comment:18 SimonKing]:
> Then, I bumped it up, and inserted a `raise RuntimeError` into the first line of both methods. Nevertheless, the documentation builds as it did before.
> 
> So, I must conclude that neither version of `get_doc` is used to get documentation.

No, the reason for that behaviour is that apparently the documentation is cached on disk. In other words, I had to delete the html file *and* to touch the code from which the documentation was taken, *and* to do "sage -b".

After that preparation, things worked.

My question to you: How can I completely wipe the cache?

I have to leave office now. But I guess a bit later today, or tomorrow, I will be able to provide a patch on top of yours. Its purpose is to allow for Cython objects to provide a documentation that is different from the documentation of their class, and it also provides the possibility to inspect Cython code that is defined during an interactive session.


---

Comment by SimonKing created at 2011-04-05 16:37:01

I added a patch that ought to be applied on top of the previous patch. In `sage_autodoc.py`, it replaces calls to the `inspect` module by the corresponding calls to the `sage.misc.sageinspect` module, and in particular it uses `_sage_getdoct_unformatted` rather than asking for the `__doc__` attribute. 

Moreover, it makes `sage_getdoc` and friends a little more stable. Namely, it catches the type error that resulted when calling `sage_getdoc` on a class:

```
sage: class MyClass:
....:     def _sage_doc_(self):
....:         return "some doc"
....:     
sage: sage.misc.sageinspect.sage_getdoc(MyClass())
'some doc\n'
sage: sage.misc.sageinspect.sage_getdoc(MyClass)
''    # This used to give a TypeError
```


Then, it also allows inspection of Cython code that is defined in an interactive session. Its code is defined in a temporary file, thus, not in the sage library tree. But the old algorithm would only try to find files in the library tree.

```
   sage: cython('''cpdef test_funct(x,y): return''') 
   sage: sage_getsourcelines(test_funct) 
   (['cpdef test_funct(x,y): return\n'], 6) 
```


I am building the documentation from scratch. If it works then I can give your patch a positive review. And I hope there will be a reviewer for my patch as well... But careful, my patch modifies something in the sage library, so, doc tests are needed.

For the patchbot:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch


---

Comment by SimonKing created at 2011-04-05 16:37:01

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-05 16:37:01

Changing keywords from "sphinx, documentation" to "sphinx, documentation, cython inspection".


---

Comment by jsrn created at 2011-04-05 18:13:49

Replying to [comment:19 SimonKing]:
> Replying to [comment:18 SimonKing]:
> > Then, I bumped it up, and inserted a `raise RuntimeError` into the first line of both methods. Nevertheless, the documentation builds as it did before.
> > 
> > So, I must conclude that neither version of `get_doc` is used to get documentation.
> 
> No, the reason for that behaviour is that apparently the documentation is cached on disk. In other words, I had to delete the html file *and* to touch the code from which the documentation was taken, *and* to do "sage -b".
> 
> After that preparation, things worked.
> 
> My question to you: How can I completely wipe the cache?

Yeah, that's true. I guess it works as a lot of other build-stuff does by only rebuilding something when the source files have changed; and I guess in this case, the source files are the *py[x] files resulting from running ./sage -b. At least, I found no quicker way for rebuilding the documentation of some file after changing sage_autodoc than what you did: edit sage_autodoc, touch some file, sage -b, build documentation.


---

Comment by jsrn created at 2011-04-06 06:27:42

After upgrade to 4.7.alpha3 from 4.6.2, applying both patches, rebuilding and then building documentation, it fails with the following error:


```
Running Sphinx v1.0.4
loading pickled environment... not yet created
building [html]: targets for 902 source files that are out of date
updating environment: 902 added, 0 changed, 0 removed
reading sources... [ 69%] sage/plot/colors                                                     
Exception occurred:
  File "/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/plot/colors.py", line 1358, in __getitem__
    raise KeyError("no colormap with name '%s'" % name)
KeyError: "no colormap with name '_sage_doc_'"
The full traceback has been saved in /tmp/sphinx-err-0GNrXK.log, if you want to report the issue to the developers.
```


It seems to be from a call to _sage_getdoc_unformatted in sageinspect.py on an object which does not support it.


---

Comment by jsrn created at 2011-04-06 06:27:42

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-06 06:37:23

Replying to [comment:22 jsrn]:
> 
> It seems to be from a call to _sage_getdoc_unformatted in sageinspect.py on an object which does not support it.

Snap diagnose: That class raises a `KeyError` when it should raise an `AttributeError`.

Two ways of fixing:

 1. Replace the `raise KeyError("no colormap with name '%s'"%name)` by an `AttributeError`.
 2. In `_sage_getdoc_unformatted`, catch not only `AttributeError`s but also `KeyError`s.

Can you find out whether raising the `KeyError` is new in sage-4.7.alpha3, and what ticket is to blame?

Cheers,
Simon


---

Comment by jsrn created at 2011-04-06 06:42:10

I have some other thoughts about our patches. The line numbers below are after patching with both patches:

- In sage_autodoc.py:820, we catch a TypeError which might be thrown by sage_getargspec. However, as the comment on the following lines indicates, this is because the old method inspect.getargspec(obj) throws TypeErrors whenever obj is a class (as you demonstrated above). Is the nested try-catch-clauses on those lines still sensible?

- You import _sage_getdoc_unformatted into sage_autodoc but isn't it bad Python practice to import a method indicated to be private? Should we just ignore this anyway?

- Shouldn't the entire sage_autodoc.py be changed to use the sageinspect module instead of the python.inspect module? It seems a bit haphazard to use one some places and the other elsewhere. If this was never the intention of sageinspect, or if it would require a huge amount of effort, then I'm perfectly ok with not doing this ;-)

- In sageinspect.py: 677, you call an object's _sage_argspec_ method. Is this an object attribute that you have invented or did I miss something? In my original patch, I invented the "_sage_getargspec" attribute for callables, which is not a method but a tuple property of the object, following the same format that inspec.getargspec would return. Shouldn't these two be merged to the same attribute, and wouldn't that imply a simplification in your patch of sage_autodoc's format_args functions? If they should indeed be different but it is something that you invented, it should be documented in some comments somewhere.

Cheers,
Johan


---

Comment by SimonKing created at 2011-04-06 06:44:07

Replying to [comment:22 jsrn]:
> It seems to be from a call to _sage_getdoc_unformatted in sageinspect.py on an object which does not support it.

I just looked at `sage/plot/colors.py`, and found that the two `__getattr__` methods defined there simply call `__getitem__` -- and this raises a `KeyError`, even before sage-4.7.

So, I suggested to replace the two `__getattr__` methods in this file by

```
try:
    return self.__getitem__(name)
except KeyError:
    raise AttributeError, "'%s' has no attribute %s"%(type(self),name)
```



---

Comment by jsrn created at 2011-04-06 07:01:37

Replying to [comment:23 SimonKing]:
> Replying to [comment:22 jsrn]:
> > 
> > It seems to be from a call to _sage_getdoc_unformatted in sageinspect.py on an object which does not support it.
> 
> Snap diagnose: That class raises a `KeyError` when it should raise an `AttributeError`.
> 
> Two ways of fixing:
> 
>  1. Replace the `raise KeyError("no colormap with name '%s'"%name)` by an `AttributeError`.
>  2. In `_sage_getdoc_unformatted`, catch not only `AttributeError`s but also `KeyError`s.
> 
> Can you find out whether raising the `KeyError` is new in sage-4.7.alpha3, and what ticket is to blame?
> 
> Cheers,
> Simon

The ticket is #5601 and more than a year old, but the KeyError might have been introduced even before. However, KeyError is clearly the wrong exception: according to Python documentation, it should be used for dictionaries (and derivatives) when asking for a non-present key. As you point out, it should be AttributeError. So I see two possibilities:

1) Open a new ticket for fixing this and let this ticket depend on it, not changing this patch. 
2) Change this patch to allow KeyError but open a new ticket changing KeyError to AttributeError and adding a note that the catch for KeyError we just added should be removed in the new ticket's patch.

The second possibility is in case it for some reason becomes a problem changing the KeyError; a lot of code might (for sick reasons) depend on color throwing a KeyError :-S


---

Comment by SimonKing created at 2011-04-06 07:03:04

Hi Johan,

Replying to [comment:24 jsrn]:
> - In sage_autodoc.py:820, we catch a TypeError which might be thrown by sage_getargspec. However, as the comment on the following lines indicates, this is because the old method inspect.getargspec(obj) throws TypeErrors whenever obj is a class (as you demonstrated above). Is the nested try-catch-clauses on those lines still sensible?

Probably it isn't needed, but I think it doesn't hurt, does it?
 
> - You import _sage_getdoc_unformatted into sage_autodoc but isn't it bad Python practice to import a method indicated to be private? Should we just ignore this anyway?

I don't know much about Python conventions. And actually it could be that "sage_getdoc" is more appropriate for "sage_autodoc.py" anyway. So, I'll try to change it.

> - Shouldn't the entire sage_autodoc.py be changed to use the sageinspect module instead of the python.inspect module? It seems a bit haphazard to use one some places and the other elsewhere. If this was never the intention of sageinspect, or if it would require a huge amount of effort, then I'm perfectly ok with not doing this ;-)

If I am not mistaken, the sageinspect module is intended to replace only a part of the Python inspect module. And if you look into the patched sage_autodoc.py, you will find that we only use the following auxiliary methods from the inspect module

```
inspect.isbuiltin
inspect.ismethoddescriptor
inspect.isfunction
inspect.isroutine
inspect.ismethod
inspect.formatargspec
```


The only "is*"-function in sageinspect is "sage.misc.sageinspect.isclassinstance", and there is also no alternate version of "formatargspec". So, I think it is just fine to use these bits from the Python inspect module.

> - In sageinspect.py: 677, you call an object's _sage_argspec_ method. Is this an object attribute that you have invented or did I miss something? In my original patch, I invented the "_sage_getargspec" attribute for callables, which is not a method but a tuple property of the object, following the same format that inspec.getargspec would return. Shouldn't these two be merged to the same attribute, and wouldn't that imply a simplification in your patch of sage_autodoc's format_args functions? If they should indeed be different but it is something that you invented, it should be documented in some comments somewhere.

As I mentioned above, I don't know much about Python conventions. But I thought it is considered bad practice to provide that type of data by arguments?

Anyway, _sage_argspec_ is a _method_, and it is not my invention, but was used in sageinspect before. Other methods used are _sage_doc_, _sage_src_ and _sage_src_lines_.

So, actually it might be a good idea to change your patch so that it uses the existing _sage_argspec_ method, rather than introducing a _sage_getargspec attribute.


---

Comment by jsrn created at 2011-04-06 07:04:30

Replying to [comment:25 SimonKing]:
> Replying to [comment:22 jsrn]:
> > It seems to be from a call to _sage_getdoc_unformatted in sageinspect.py on an object which does not support it.
> 
> I just looked at `sage/plot/colors.py`, and found that the two `__getattr__` methods defined there simply call `__getitem__` -- and this raises a `KeyError`, even before sage-4.7.
> 
> So, I suggested to replace the two `__getattr__` methods in this file by
> {{{
> try:
>     return self.__getitem__(name)
> except KeyError:
>     raise AttributeError, "'%s' has no attribute %s"%(type(self),name)
> }}}

That's a good fix! New ticket (on which this depends) or just go dirty and fix it here?


---

Comment by jsrn created at 2011-04-06 07:08:30

Replying to [comment:27 SimonKing]:
> Hi Johan,
> 
> Replying to [comment:24 jsrn]:
> > - In sage_autodoc.py:820, we catch a TypeError which might be thrown by sage_getargspec. However, as the comment on the following lines indicates, this is because the old method inspect.getargspec(obj) throws TypeErrors whenever obj is a class (as you demonstrated above). Is the nested try-catch-clauses on those lines still sensible?
> 
> Probably it isn't needed, but I think it doesn't hurt, does it?

I'll try to do some testing without it; if it causes problems, then we'll leave it. Otherwise, I don't care much for confusing and rotting code ;-)

>  
> > - You import _sage_getdoc_unformatted into sage_autodoc but isn't it bad Python practice to import a method indicated to be private? Should we just ignore this anyway?
> 
> I don't know much about Python conventions. And actually it could be that "sage_getdoc" is more appropriate for "sage_autodoc.py" anyway. So, I'll try to change it.
> 
> > - Shouldn't the entire sage_autodoc.py be changed to use the sageinspect module instead of the python.inspect module? It seems a bit haphazard to use one some places and the other elsewhere. If this was never the intention of sageinspect, or if it would require a huge amount of effort, then I'm perfectly ok with not doing this ;-)
> 
> If I am not mistaken, the sageinspect module is intended to replace only a part of the Python inspect module. And if you look into the patched sage_autodoc.py, you will find that we only use the following auxiliary methods from the inspect module
> {{{
> inspect.isbuiltin
> inspect.ismethoddescriptor
> inspect.isfunction
> inspect.isroutine
> inspect.ismethod
> inspect.formatargspec
> }}}
> 
> The only "is*"-function in sageinspect is "sage.misc.sageinspect.isclassinstance", and there is also no alternate version of "formatargspec". So, I think it is just fine to use these bits from the Python inspect module.

Sounds fine.

> 
> > - In sageinspect.py: 677, you call an object's _sage_argspec_ method. Is this an object attribute that you have invented or did I miss something? In my original patch, I invented the "_sage_getargspec" attribute for callables, which is not a method but a tuple property of the object, following the same format that inspec.getargspec would return. Shouldn't these two be merged to the same attribute, and wouldn't that imply a simplification in your patch of sage_autodoc's format_args functions? If they should indeed be different but it is something that you invented, it should be documented in some comments somewhere.
> 
> As I mentioned above, I don't know much about Python conventions. But I thought it is considered bad practice to provide that type of data by arguments?

Huh, why oh why? Ok, I never really read those conventions, but if you say so ;-)
> 
> Anyway, _sage_argspec_ is a _method_, and it is not my invention, but was used in sageinspect before. Other methods used are _sage_doc_, _sage_src_ and _sage_src_lines_.
> 
> So, actually it might be a good idea to change your patch so that it uses the existing _sage_argspec_ method, rather than introducing a _sage_getargspec attribute.

Definitely, if that is the way Sage does it elsewhere; I weren't aware of that. I'll look into changing my patch; what kind of stuff does _sage_argspec_ usually return?


---

Comment by SimonKing created at 2011-04-06 07:09:23

Replying to [comment:26 jsrn]:
> 1) Open a new ticket for fixing this and let this ticket depend on it, not changing this patch. 

> 2) Change this patch to allow KeyError but open a new ticket changing KeyError to AttributeError and adding a note that the catch for KeyError we just added should be removed in the new ticket's patch.
> 
> The second possibility is in case it for some reason becomes a problem changing the KeyError; a lot of code might (for sick reasons) depend on color throwing a KeyError :-S

Both solutions involve opening a new ticket. So, that should be done anyway. Can you do it?

I already sketched a patch for the new ticket. If doc tests pass after changing the `KeyError` into an `AttributeError` (and of course if there is an additional doc test verifying the correct error type) then it can certainly be given a positive review and made a dependency for this ticket (hence, solution 1). Otherwise, we go for solution 2).


---

Comment by SimonKing created at 2011-04-06 07:10:53

Replying to [comment:28 jsrn]:
> That's a good fix! New ticket (on which this depends) or just go dirty and fix it here?

Hm. We can try. If it breaks any old test (except trivial ones that test the wrong exception type) then it should be a new ticket. Otherwise, I think it is ok to include it here.


---

Comment by SimonKing created at 2011-04-06 07:19:20

Replying to [comment:29 jsrn]:
> > As I mentioned above, I don't know much about Python conventions. But I thought it is considered bad practice to provide that type of data by arguments?
> 
> Huh, why oh why? Ok, I never really read those conventions, but if you say so ;-)

Well, I am no expert for Python conventions. It is just something that I think to remember to have heard...

> Definitely, if that is the way Sage does it elsewhere; I weren't aware of that. I'll look into changing my patch; what kind of stuff does _sage_argspec_ usually return?

It is similar to the format that is returned by inspect.getargspec:

```
sage: def f(x,y, k=1,l=2, *args, **kwds): pass....: 
sage: inspect.getargspec(f)
ArgSpec(args=['x', 'y', 'k', 'l'], varargs='args', keywords='kwds', defaults=(1, 2))
sage: sage.misc.sageinspect.sage_getargspec(f)
(['x', 'y', 'k', 'l'], 'args', 'kwds', (1, 2))
```


So, `self._sage_argspec_()` should return a tuple of the kind that is returned by `sage_getargspec(self)`.


---

Comment by jsrn created at 2011-04-06 07:25:10

Replying to [comment:31 SimonKing]:
> Replying to [comment:28 jsrn]:
> > That's a good fix! New ticket (on which this depends) or just go dirty and fix it here?
> 
> Hm. We can try. If it breaks any old test (except trivial ones that test the wrong exception type) then it should be a new ticket. Otherwise, I think it is ok to include it here.

It has been coded and I'm running doctests :-)


---

Comment by SimonKing created at 2011-04-06 07:29:59

Let me try to condense the discussion above in a TODO list:

 * I'll try to replace `_sage_getdoc_unformatted` by `sage_getdoc`.
 * You already tried to let `__getattr__` in sage.plot raise the correct error, and see if doctests still pass. If they don't (except for trivial cases), you'll open a new ticket.
 * I'll remove the "except TypeError" from sage_autodoc.py, since it is caught in sageinspect.py anyway.
 * You'll try to replace the `_sage_getargspec` attribute by a `_sage_argspec_` method.


---

Comment by SimonKing created at 2011-04-06 07:47:34

Replying to [comment:34 SimonKing]:
>  * I'll remove the "except TypeError" from sage_autodoc.py, since it is caught in sageinspect.py anyway.

Probably better not. According to the comments in sage_autodoc.py, the reason for catching `TypeError` is something that is not taken care of in `sage_getargspec`, and it handles these cases using `self.env.config.autodoc_builtin_argspec`, which is something `sageinspect.py` doesn't know of.


---

Comment by jsrn created at 2011-04-06 07:57:01

I already hit the first snag as I misremembered my patch (because I originally had two possible solutions): the _sage_getargspec I defined is a function taking a "getter" function, which is a function able to construct the argspec of an object. When called by sage_autodoc.format_args, the getter will be a local function in there, resulting in a recursive interplay between whatever is in _sage_getargspec and format_args. This is to avoid copying all the logic in sage_autodoc for how to produce argspecs for different "basic" objects.
I see two possibilities for how to proceed:
1) Change _sage_getargspec to be like _sage_argspec_: a no-argument function just returning a tuple. This would entail copying a lot of code from sage_autodoc to somewhere in the Sage library for easy reuse by sage_wraps or something.
2) Change _sage_argspec_ to be like _sage_getargspec and take a getter-function, which is possibly ignored. I'm actually a bit confused about _sage_argspec_ as it seems to never be used anywhere; it is defined on two Cython classes (I forget where), but is never called by any code except your new patch. Therefore, this change would only change these two Cython classes' _sage_argspec_ functions to accept but ignore a getter argument.


---

Comment by jsrn created at 2011-04-06 08:13:26

Replying to [comment:35 SimonKing]:
> Replying to [comment:34 SimonKing]:
> >  * I'll remove the "except TypeError" from sage_autodoc.py, since it is caught in sageinspect.py anyway.
> 
> Probably better not. According to the comments in sage_autodoc.py, the reason for catching `TypeError` is something that is not taken care of in `sage_getargspec`, and it handles these cases using `self.env.config.autodoc_builtin_argspec`, which is something `sageinspect.py` doesn't know of.

No, the TypeError is around the try which is after the logic possibly calling the builtin_argspec-thing: It first checks for a _sage_getarspec-attribute, then it checks if it is a builtin (in which case it uses the builtin_argspec), and if both fail, it tries to use inspect.getargspec (after your patch, sageinspect.sage_getargspec). Now, inspect.getargspec may throw a TypeError if the argument is class and this is then handled separately. But you already do than in sageinspec.sage_getarspec, right?


---

Comment by SimonKing created at 2011-04-06 08:24:45

Replying to [comment:36 jsrn]:
> I already hit the first snag as I misremembered my patch (because I originally had two possible solutions): the _sage_getargspec I defined is a function taking a "getter" function, which is a function able to construct the argspec of an object. When called by sage_autodoc.format_args, the getter will be a local function in there, resulting in a recursive interplay between whatever is in _sage_getargspec and format_args. This is to avoid copying all the logic in sage_autodoc for how to produce argspecs for different "basic" objects.

In other words, the purpose of `_sage_getargspec` and `_sage_argspec_` is different: If an object knows its arguments, then it can simply return them with `_sage_argspec_`. Otherwise, the interplay between sage_autodoc and the getter method of `_sage_getargspec` will find out.

I try to imagine what objects do not know their own arguments. Is it like this? If the object is in fact not a class instance but a class, then calling a method like `_sage_argspec_` would result in a type error. So, _sage_argspec_ would not be able to tell the arguments of a class.

However, the arguments of a class are the arguments of its `__new__` or `__init__` method -- and both are actually considered in sage.misc.sageinspect.sage_getargspec.

So, is the purpose of `_sage_getargspec` and its getter method to deal with the case of a class, or what situation did you have in mind when you invented it?

What would `_sage_getargspec` and its getter method be able to do that `sage_getargspec` (after my patch) can not do?


---

Comment by SimonKing created at 2011-04-06 08:30:14

Replying to [comment:37 jsrn]:
> No, the TypeError is around the try which is after the logic possibly calling the builtin_argspec-thing: It first checks for a _sage_getarspec-attribute, then it checks if it is a builtin (in which case it uses the builtin_argspec), and if both fail, it tries to use inspect.getargspec (after your patch, sageinspect.sage_getargspec). Now, inspect.getargspec may throw a TypeError if the argument is class and this is then handled separately. But you already do than in sageinspec.sage_getarspec, right?

Sounds correct.

Well, I'll try.


---

Comment by SimonKing created at 2011-04-06 08:38:02

Replying to [comment:39 SimonKing]:
> Replying to [comment:37 jsrn]:
> > No, the TypeError is around the try which is after the logic possibly calling the builtin_argspec-thing: It first checks for a _sage_getarspec-attribute, then it checks if it is a builtin (in which case it uses the builtin_argspec), and if both fail, it tries to use inspect.getargspec (after your patch, sageinspect.sage_getargspec). Now, inspect.getargspec may throw a TypeError if the argument is class and this is then handled separately. But you already do than in sageinspec.sage_getarspec, right?
> 
> Sounds correct.
> 
> Well, I'll try.

On the other hand, if you see what is done after the "`except TypeError`", you'll find that something remains to do: Remove the argument "self" that sage_getargspec would return when being called on a class or class instance:

```
sage: from sage.misc.sageinspect import sage_getargspec
sage: sage_getargspec(QQ)
(['self', 'x', '*args', '**kwds'], None, None, (0,))
sage: sage_getargspec(QQ.__class__)
(['self', 'x', '*args', '**kwds'], None, None, (0,))
```


So, I guess a better plan is to explicitly test (using `inspect.isclass` and whether we want the first argument to be stripped:

```
sage: import inspect
sage: inspect.isclass(QQ.__class__)
True
sage: sage.misc.sageinspect.isclassinstance(QQ)
True
```


This is what I will replace the "`except TypeError`" with.


---

Comment by jsrn created at 2011-04-06 09:41:52

> 
> So, I guess a better plan is to explicitly test (using `inspect.isclass` and whether we want the first argument to be stripped:
> {{{
> sage: import inspect
> sage: inspect.isclass(QQ.__class__)
> True
> sage: sage.misc.sageinspect.isclassinstance(QQ)
> True
> }}}
> 
> This is what I will replace the "`except TypeError`" with.

That sounds good. I guess we do not want this stripping down in sage_getargspec.

I'll look into whether sage_getargspec already implements the logic in sage_autodoc that I was trying to avoid duplicating when inventing _sage_getargspec.


---

Comment by SimonKing created at 2011-04-06 10:23:18

Currently (i.e., after replacing the "except TypeError"), I get the  following error when building the references:

```
reading sources... [  7%] sage/algebras/free_algebra_element                    
Exception occurred:
  File "/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/Sphinx-1.0.4-py2.6.egg/sphinx/config.py", line 207, in __getattr__
    raise AttributeError('No such config value: %s' % name)
AttributeError: No such config value: autodoc_default_flags
The full traceback has been saved in /tmp/sphinx-err-5rJIPQ.log, if you want to report the issue to the developers.
```


Do you have an idea where "autodoc_default_flags" is requested? According to `grep autodoc_default -R .`, it occurs _nowhere_ in the sage repository!


---

Comment by SimonKing created at 2011-04-06 10:42:03

It turned out the the error resulted from using `sage_getdoc` -- one _should_ actually use `_sage_getdoc_unformatted`, as I did in my original patch!


---

Comment by jsrn created at 2011-04-06 11:03:53

Another bug: Since Python 2.6, inspect.getargspec should return a _named_ tuple ArgSpec(args, varargs, keywords, defaults) (see e.g. http://docs.python.org/library/inspect.html#inspect.getargspec). My patch expects such a tuple and returns such a tuple. However, sage_getargspec does not return a named argspec, and, apparently, inspect.formatargspec still accepts the unnamed one (so we don't see the error from here). 
We have two possibilities:
1) Change my patch so it doesn't rely on the tuple being named
2) Change sageinspect to return named tuples for all returned argspecs.
I vote for 2) as that seems to be the direction Python is going; I would expect inspect.formatargspec to change in later versions and no longer accept unnamed tuples.


---

Comment by SimonKing created at 2011-04-06 11:25:52

Replying to [comment:44 jsrn]:
> We have two possibilities:
> 1) Change my patch so it doesn't rely on the tuple being named
> 2) Change sageinspect to return named tuples for all returned argspecs.
> I vote for 2) as that seems to be the direction Python is going; I would expect inspect.formatargspec to change in later versions and no longer accept unnamed tuples.

How does one create a named tuple?


---

Comment by SimonKing created at 2011-04-06 11:50:31

Replying to [comment:45 SimonKing]:
> How does one create a named tuple?

I think I got it: One import `ArgSpec` from `inspect`, does not change the expected output of `_sage_argspec_` (it should still be a tuple, for backwards compatibility), and `sage_argspec` returns `ArgSpec(*obj._sage_argspec_())`.


---

Comment by jsrn created at 2011-04-06 12:30:24

> I think I got it: One import `ArgSpec` from `inspect`, does not change the expected output of `_sage_argspec_` (it should still be a tuple, for backwards compatibility), and `sage_argspec` returns `ArgSpec(*obj._sage_argspec_())`.

Do you mean sageinspect.sage_getargspec should return an ArgSpec, while _sage_argspec_ on objects should always return an unnamed tuple? I'm trying to use _sage_argspec_ instead of the _sage_getargspec I invented, but then in order to use sage_getargspec (as an alternative to the recursive getter-thingie I have now), I would have to unwrap the ArgSpec into a normal tuple? That would be clumsy and tedious.

Alternatively, we could let both _sage_argspec_ and sageinspect.sage_getargspec use ArgSpec named tuples everywhere; named tuples exhibit the exact (I think) same behaviour as tuples, whenever one is ignorant that they are named tuples (for example, it returns true on isinstance(*, tuple)). Therefore, I would think no code would break by changing this, and it would be nicer and less clumsy. 

Btw, is there a chat-room or IRC channel recommended for this kind of communication? This is getting a bit old :-)


---

Comment by jsrn created at 2011-04-06 13:00:07

Ok, this seems to work (for me at least). I've made a patch for changing sageinspect into returning ArgSpec, and I've redone my original patch into using _sage_argspec as the place for decorators to put the ArgSpec of the wrapped callable. These patches might cause your later patches to not apply anymore, but the changes should be trivial.


---

Attachment

Changes sageinspect.sage_getargspec to return a named tuple ArgSpec


---

Comment by SimonKing created at 2011-04-06 13:04:21

Replying to [comment:48 jsrn]:
> Ok, this seems to work (for me at least). I've made a patch for changing sageinspect into returning ArgSpec, and I've redone my original patch into using _sage_argspec as the place for decorators to put the ArgSpec of the wrapped callable. These patches might cause your later patches to not apply anymore, but the changes should be trivial.

That's not nice. I was working on replacing tuple by named tuple as well. So, now we have to merge patches.


---

Comment by SimonKing created at 2011-04-06 13:06:45

Replying to [comment:50 SimonKing]:
> Replying to [comment:48 jsrn]:
> > Ok, this seems to work (for me at least). I've made a patch for changing sageinspect into returning ArgSpec, and I've redone my original patch into using _sage_argspec as the place for decorators to put the ArgSpec of the wrapped callable. These patches might cause your later patches to not apply anymore, but the changes should be trivial.
> 
> That's not nice. I was working on replacing tuple by named tuple as well. So, now we have to merge patches.

PS: Your patch does not suffice, as one will need to change a doctest in element.pyx.


---

Comment by SimonKing created at 2011-04-06 13:32:48

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-06 13:32:48

Since [attachment:9976_change_to_argspec.patch] does not do the necessary changes in sage/structure/element.pyx and in sage/misc/lazy_import.pyx, it is hopefully OK that I suggest to replace it with the patch that I just updated.

That patch also contains the fix for plots: An `AttributeError` is raised, not a `KeyError` (and it is tested, of course).

Since your patches changed, I am afraid I need to run long tests again. But I am fairly confident, and so I change the status into "needs review".

For the patchbot:

Apply trac_9976_decorated_generic_sigs_alternative.patch inspection_of_cython.patch


---

Comment by jsrn created at 2011-04-06 13:45:02

Replying to [comment:52 SimonKing]:
> Since [attachment:9976_change_to_argspec.patch] does not do the necessary changes in sage/structure/element.pyx and in sage/misc/lazy_import.pyx, it is hopefully OK that I suggest to replace it with the patch that I just updated.

Sure. The double work was unfortunate -- would have been nice with a more direct communication channel to avoid this.

> 
> That patch also contains the fix for plots: An `AttributeError` is raised, not a `KeyError` (and it is tested, of course).

I also did that, so more double work. My patch was slightly different: I added doc-tests demonstrating the different exception class with different access methods (maps.punk vs maps['punk']). I also used self.__class__.__name__ instead of type(self) for the output string. I don't particularly feel strongly for either, though.

> 
> Since your patches changed, I am afraid I need to run long tests again. But I am fairly confident, and so I change the status into "needs review".

Yup, me too; and compile all documentation again :-S But at long last we seem to be right about there...


---

Comment by SimonKing created at 2011-04-06 14:00:45

Replying to [comment:53 jsrn]:
> > That patch also contains the fix for plots: An `AttributeError` is raised, not a `KeyError` (and it is tested, of course).
> 
> I also did that, so more double work. My patch was slightly different: I added doc-tests demonstrating the different exception class with different access methods (maps.punk vs maps['punk']). I also used self.__class__.__name__ instead of type(self) for the output string. I don't particularly feel strongly for either, though.

That might actually be a good idea. It would coincide with what 
sage.structure.parent.raise_attribute_error does. Moreover, I just saw that I actually forgot to add a new doctest (although there is a modified old doctest showing the error).

So, perhaps one of us (hopefully not both...) could add it. Perhaps you? I plan to move on to ticket #11115.


---

Comment by jsrn created at 2011-04-06 14:09:39

> That might actually be a good idea. It would coincide with what 
> sage.structure.parent.raise_attribute_error does. Moreover, I just saw that I actually forgot to add a new doctest (although there is a modified old doctest showing the error).
> 
> So, perhaps one of us (hopefully not both...) could add it. Perhaps you? I plan to move on to ticket #11115. 
> 

I'll do the change. But a new doc-test showing which error? In plot.colors? That would be superfluous, right? Or in sageinspect?


---

Comment by SimonKing created at 2011-04-06 14:48:48

Replying to [comment:55 jsrn]:
> I'll do the change. But a new doc-test showing which error? In plot.colors? That would be superfluous, right?

Thank you!

I thought that the `__getattr__` method in plot.colors should get a test, demonstrating that the correct error is raised. Of course, getting the correct error is also tested somewhere else, but in general I believe that a bug fix should be tested in the method that was fixed.

Good and bad news: 

The good news is that the long tests all pass.

The bad new is that I get 80 warnings when building the documentation.

Typically, it is

```
.../doc/en/reference/sage/rings/polynomial/real_roots.rst:7: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ratlist.coeffs_bitsize: arg is not a code object
```

and I also obtain 

```
WARNING: display latex u'\\R': latex exited with error:                         
[stderr]
...
! Undefined control sequence.
<recently read> \R 
                   
l.29 $\R
        $
[1] (./math.aux) )
(see the transcript file for additional information)
Output written on math.dvi (1 page, 152 bytes).
Transcript written on math.log.

WARNING: display latex u'\\R^+': latex exited with error:
[stderr]

[stdout]
```


Do you have an idea what happened there?


---

Comment by SimonKing created at 2011-04-06 14:51:53

Concerning "is not a code object", it can be reproduced as follows:

```
sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist
sage: sage.misc.sageinspect.sage_getargspec(bernstein_polynomial_factory_ratlist.coeffs_bitsize)
Traceback (most recent call last):
...
TypeError: arg is not a code object
```


So, it seems like it should be fixed in sage.misc.sageinspect.


---

Comment by SimonKing created at 2011-04-06 14:51:53

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-06 14:57:43

Replying to [comment:57 SimonKing]:
> So, it seems like it should be fixed in sage.misc.sageinspect.

And here is how it can be solved:

```
sage: from sage.misc.sageinspect import _sage_getargspec_from_ast, sage_getsource
sage: _sage_getargspec_from_ast(sage_getsource(bernstein_polynomial_factory_ratlist.coeffs_bitsize))
ArgSpec(args=['self'], varargs=None, keywords=None, defaults=None)
```


Doing it now.


---

Comment by SimonKing created at 2011-04-06 15:04:20

Fixed and doctested! The new doctest is:

```
sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist
sage: sage.misc.sageinspect.sage_getargspec(bernstein_polynomial_factory_ratlist.coeffs_bitsize)
ArgSpec(args=['self'], varargs=None, keywords=None, defaults=None)
```


Back to needs review, and also back to building the docs.


---

Comment by SimonKing created at 2011-04-06 15:04:20

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-06 15:28:15

Not good. The documentation does not build. I keep getting errors such as

```
/mnt/local/king/SAGE/broken/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:7: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gen: ('invalid syntax', ('<unknown>', 1, 19, 'def gen(self, int i=0):\n'))
/mnt/local/king/SAGE/broken/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:7: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gens: ('invalid syntax', ('<unknown>', 13, 45, '        return tuple([new_BM_from_DD(self, (<BooleanPolynomialRing>self._ring),\n'))
```



---

Comment by SimonKing created at 2011-04-06 15:28:15

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-06 15:38:38

It turns out that in that case, another method does the job: `_sage_getargspec_cython`. I guess the solution is to ask `sage_getfile(obj)` whether the source is Python or Cython, and then choose the appropriate solution.


---

Comment by SimonKing created at 2011-04-06 16:34:57

Building the docs, I get some warnings:


```
docstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement:6: (ERROR/3) Unexpected indentation.
docstring of sage.rings.padics.padic_capped_relative_element:5: (ERROR/3) Unexpected indentation.
docstring of sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic:18: (WARNING/2) Literal block expected; none found.
```


But worse is that the arguments of the `groebner_basis` method of multivariate ideals are not correctly provided: It is `(*args,**kwds)` again!!! Can you check whether this used to be fine with your original patch?

Anyway, the reason for the failure is that the `cached_method` decorator does not provide `_sage_argspec_` yet (it will be, by #11115). I assume that one can inspect the source code, though.

So, it still needs work, but not today.

My plan for tomorrow:

 * Fix the warnings above (I already succeeded with two of them)
 * Fix the argument extraction in sageinspect.


---

Comment by SimonKing created at 2011-04-06 18:59:33

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-06 18:59:33

I was able to submit new patches earlier than expected. 

First, there is another fix in sage_getargspec. It is now tested:

```
sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist 
sage: sage_getargspec(bernstein_polynomial_factory_ratlist.coeffs_bitsize) 
ArgSpec(args=['self'], varargs=None, keywords=None, defaults=None) 
sage: from sage.rings.polynomial.pbori import BooleanMonomialMonoid 
sage: sage_getargspec(BooleanMonomialMonoid.gen) 
ArgSpec(args=['self', 'i'], varargs=None, keywords=None, defaults=(0,)) 
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: sage_getargspec(I.groebner_basis)
ArgSpec(args=['self', 'algorithm', 'deg_bound', 'mult_bound', 'prot', '*args', '**kwds'], varargs=None, keywords=None, defaults=('', None, None, False)) 
```


When building the documentation, I got a couple of warnings. I fixed them in the other patch.

I will only be able to look at the resulting reference manual tomorrow. However, if someone in a different time zone wants to look at it now, it shall be "needs review"...

For the patchbot:

Apply trac_9976_decorated_generic_sigs_alternative.patch inspection_of_cython.patch 9976_doc_fixes.patch


---

Comment by jsrn created at 2011-04-07 06:32:40

Replying to [comment:62 SimonKing]:
> Building the docs, I get some warnings:
> 
> {{{
> docstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement:6: (ERROR/3) Unexpected indentation.
> docstring of sage.rings.padics.padic_capped_relative_element:5: (ERROR/3) Unexpected indentation.
> docstring of sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic:18: (WARNING/2) Literal block expected; none found.
> }}}
> 
> But worse is that the arguments of the `groebner_basis` method of multivariate ideals are not correctly provided: It is `(*args,**kwds)` again!!! Can you check whether this used to be fine with your original patch?
> 
> Anyway, the reason for the failure is that the `cached_method` decorator does not provide `_sage_argspec_` yet (it will be, by #11115). I assume that one can inspect the source code, though.
> 
> So, it still needs work, but not today.
> 
> My plan for tomorrow:
> 
>  * Fix the warnings above (I already succeeded with two of them)
>  * Fix the argument extraction in sageinspect.

Back again :-)

No, groebner_basis has never worked with my patch; for my patch to work, it requires that the decorator use `@`sage_wraps on the wrapping function which is returned. cached_method doesn't do this. As far as I can see, however, it should be possible to make (the non-Cython version of) cached_method use sage_wraps; this would remove some lines in _common_init and replace it with a `@`sage_wraps somewhere. You have been working on this so what do you say?


---

Attachment

Improve inspection on Cython objects; let sage_getargspec return an _ArgSpec_; let a plot raise an _AttributeError_ if an attribute is missing


---

Comment by SimonKing created at 2011-04-07 06:44:57

Replying to [comment:64 jsrn]:
> No, groebner_basis has never worked with my patch; for my patch to work, it requires that the decorator use `@`sage_wraps on the wrapping function which is returned. 

Did you check whether it works with my latest patches? With them, `sage_getargspec` works on `groebner_basis()`.

In fact, I just checked that the documentation looks ok if I apply both our patches.

By the way, I asked at [sage-devel http://groups.google.com/group/sage-devel/browse_thread/thread/dd7de9c504c13164] whether it is ok if I review your patch and you review mine.

> cached_method doesn't do this. As far as I can see, however, it should be possible to make (the non-Cython version of) cached_method use sage_wraps; this would remove some lines in _common_init and replace it with a `@`sage_wraps somewhere. You have been working on this so what do you say?

I think that would be a waste of time. The to-be-submitted Cython version of `@`cached_method will be _vastly_ superior to the old Python version, but you can't use a decorator such as `@`sage_wraps in Cython code. Moreover, if I am not mistaken, the problem is already solved with our patches.


---

Comment by jsrn created at 2011-04-07 06:45:54

Ridiculous: I can't overwrite your 9976 as I don't have DELETE-privileges. So I've made a v2; it's like your latest version but with the doctest-changes we discussed in colors.py.

Patchbot: Apply trac_9976_decorated_generic_sigs_alternative.patch inspection_of_cython_v2.patch 9976_doc_fixes.patch


---

Comment by jsrn created at 2011-04-07 06:54:24

Replying to [comment:65 SimonKing]:
> Replying to [comment:64 jsrn]:
> > No, groebner_basis has never worked with my patch; for my patch to work, it requires that the decorator use `@`sage_wraps on the wrapping function which is returned. 
> 
> Did you check whether it works with my latest patches? With them, `sage_getargspec` works on `groebner_basis()`.

I was being unclear before; what I meant to say was that a decorator should usually just use sage_wraps and then not worry any more about all this inheriting of __doc__, etc. However, another route is to do it manually as cached_method does. 

However, it doesn't seem to work for me. I still get some warnings (in sage.rings.padics.padic_ZZ_pX_CA_element, sage.rings.padics.padic_capped_relative_element, sage.rings.polynomial.multi_polynomial_ring_generic), and then a latex error like the ones you described earlier. I wasn't supposed to apply your 11115 patch, was I?

> 
> In fact, I just checked that the documentation looks ok if I apply both our patches.
> 
> By the way, I asked at [sage-devel http://groups.google.com/group/sage-devel/browse_thread/thread/dd7de9c504c13164] whether it is ok if I review your patch and you review mine.
Sounds good; I was thinking the same thing.

> I think that would be a waste of time. The to-be-submitted Cython version of `@`cached_method will be _vastly_ superior to the old Python version, but you can't use a decorator such as `@`sage_wraps in Cython code. Moreover, if I am not mistaken, the problem is already solved with our patches.

Convinced; I hadn't really looked into the extend of your changes in cached_method. Good job.


---

Comment by SimonKing created at 2011-04-07 07:02:40

Replying to [comment:67 jsrn]:
> > Did you check whether it works with my latest patches? With them, `sage_getargspec` works on `groebner_basis()`.
> 
> I was being unclear before; what I meant to say was that a decorator should usually just use sage_wraps and then not worry any more about all this inheriting of __doc__, etc. However, another route is to do it manually as cached_method does. 
> 
> However, it doesn't seem to work for me. I still get some warnings (in sage.rings.padics.padic_ZZ_pX_CA_element, sage.rings.padics.padic_capped_relative_element, sage.rings.polynomial.multi_polynomial_ring_generic), and then a latex error like the ones you described earlier. I wasn't supposed to apply your 11115 patch, was I?

There is no patch posted at #11115, yet.

Concerning the warnings: Did you also apply [attachment 9976_doc_fixes.patch]? That should fix it. Or at least, it did so for me.

And does the argument list for groebner_basis look fine now?


---

Comment by SimonKing created at 2011-04-07 07:08:43

Your changes to my patch look OK.

For some reason, the patchbot did not pick up the correct patches (it only considers two of them). So, again:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython_v2.patch 9976_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-07 07:50:58

After emptying my patch queue, applying our three patches, removing any reference to `cachefunc` in the `build` directories, touching `sage/rings/polynomial/multi_polynomial_ideal.py`, `sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx`, `sage/plot/contour_plot.py` and `sage/misc/cachefunc.py`, I did `sage -b` and then `sage -docbuild html`.

So, I can be sufficiently sure that there is no leftover from previous work, and that I am really only testing the effects of this ticket.

I obtain:

```
sphinx-build -b html -d /mnt/local/king/SAGE/broken/devel/sage/doc/output/doctrees/en/reference    /mnt/local/king/SAGE/broken/devel/sage/doc/en/reference /mnt/local/king/SAGE/broken/devel/sage/doc/output/html/en/reference
Running Sphinx v1.0.4
loading pickled environment... done
building [html]: targets for 98 source files that are out of date
updating environment: 0 added, 98 changed, 0 removed
reading sources... [ 72%] sage/rings/polynomial/multi_polynomial_ideal_libsingulreading sources... [100%] sage/symbolic/ring                                    
<autodoc>:0: (ERROR/3) Unexpected indentation.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [ 78%] sage/rings/polynomial/multi_polynomial_ideal_libsingulawriting output... [100%] structure                                              
writing additional files... genindex py-modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 1 warning.
Build finished.  The built documents can be found in /mnt/local/king/SAGE/broken/devel/sage/doc/output/html/en/reference
```


I don't understand the warning about `autodoc`: It doesn't say which sage file it is from.

The arguments in the documentation of groebner_basis are given by:

```
groebner_basis(algorithm, deg_bound, mult_bound='', prot=None, *args=None, **kwds=False)
```

and of sage.plot.contour_plot.contour_plot:

```
sage.plot.contour_plot.contour_plot(f, xrange, yrange, axes=False, linestyles=None, frame=True, labels=False, plot_points=100, linewidths=None, colorbar=False, contours=None, legend_label=None, fill=True, label_inline=None, label_fmt='%1.2f', label_fontsize=9, label_colors='blue', label_inline_spacing=3, colorbar_spacing=None, colorbar_orientation='vertical', colorbar_format=None, **options)
```


From my perspective, the problem is solved. I have already done the long tests yesterday, and to be on the safe side, I repeat them now.

If we are allowed to do cross reviewing, I would give your patch a positive review. Let's see what the fellow developers on sage-devel will tell us...


---

Comment by SimonKing created at 2011-04-07 08:01:35

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-07 08:01:35

Replying to [comment:70 SimonKing]:
> The arguments in the documentation of groebner_basis are given by:
> groebner_basis(algorithm, deg_bound, mult_bound='', prot=None, *args=None, **kwds=False)

NO! That's wrong again. It should be "algorithm='', degbound=None, mult_bound=None, *args, **kwds"!!

What does that come from?? I see:

```
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: sage.misc.sageinspect.sage_getargspec(I.groebner_basis)
ArgSpec(args=['self', 'algorithm', 'deg_bound', 'mult_bound', 'prot', '*args', '**kwds'], varargs=None, keywords=None, defaults=('', None, None, False))
```

and that's wrong.

It seems that the problem lies here:

```
sage: source = sage.misc.sageinspect.sage_getsource(I.groebner_basis)
sage: sage.misc.sageinspect._sage_getargspec_cython(source)
(['self', 'algorithm', 'deg_bound', 'mult_bound', 'prot', '*args', '**kwds'], None, None, ('', None, None, False))
```

Hence, the bug is in _sage_getargspec_cython.

Too bad.

I guess the problem is that _sage_getargspec_cython does not consider `*args` and `**kwds`, since it is not supported by Cython. But `_sage_getargspec_from_ast` can not deal with the problem either.

Potential approach: extend `_sage_getargspec_cython` so that it allows for `*args` and `**kwds` -- who knows, perhaps Cython will supported such arguments anyway, in future?


---

Comment by SimonKing created at 2011-04-07 08:38:14

I went for a different solution:

In sage_getargspec, if the object is no method or class but a class instance (which is the case for decorated methods), then the source code is taken, the definition is extracted, and then analyzed with `_sage_getargspec_from_ast`. That approach will both work on Cython and Python code, but to be on the safe side, I use `_sage_getargspec_cython` if an error occurs.

With that, we have (doctested)

```
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: sage_getargspec(I.groebner_basis)
ArgSpec(args=['self', 'algorithm', 'deg_bound', 'mult_bound', 'prot'],
varargs='args', keywords='kwds', defaults=('', None, None, False))
sage: cython("cpdef int foo(x,y) except -1: return 1")
sage: sage.misc.sageinspect.sage_getargspec(foo)
ArgSpec(args=['x', 'y'], varargs=None, keywords=None, defaults=None)
```


And the documentation of groebner_basis looks fine.

Of course, due to missing rights, I can not replace your patch version 2, but I have replaced my patch version 1. It contains your additions, though. Hence:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-07 08:38:14

Changing status from needs_work to needs_review.


---

Comment by jsrn created at 2011-04-07 08:58:20

hmm, ok, now I don't get the warnings anymore (I had indeed forgotten the doc-patch). But even with your new patch, I still get the wrong argument-string for groebner_basis:


```
groebner_basis(algorithm, deg_bound, mult_bound='', prot=None, *args=None, **kwds=False)
```


I'm getting a headache :-S


---

Comment by jsrn created at 2011-04-07 09:01:15

Sorry! Skip that; I must have messed up with the patches. After starting over and trying again it worked with groebner_basis.


---

Comment by SimonKing created at 2011-04-07 09:07:54

FWIW, all tests pass for me.

The opinion on sage-devel seems to be that I can review your patch and you can review my patches, if we don't feel biased by the long discussion that we had yesterday.


---

Comment by SimonKing created at 2011-04-07 09:15:31

Can you please add doctests for your changes in sage/misc/decorators.py?


---

Comment by jsrn created at 2011-04-07 09:36:00

Ok, sounds fine. I'm trying to review your patch right now.

Question: On line 1064 of sage_autodoc.py after your patch, you remove self and cls if they are there. Why do you use that check:


```
if argspec is not None and argspec[0] and argspec[0][0] in ('cls', 'self'): 
```


instead of


```
if isclassinstance(obj) or inspect.isclass(obj): 
```


which you have included, commented out, on the line above, and which you used on line 819 for something similar?

I'll look into some doctests...


---

Comment by SimonKing created at 2011-04-07 10:12:13

Replying to [comment:77 jsrn]:
> Question: On line 1064 of sage_autodoc.py after your patch, you remove self and cls if they are there. Why do you use that check:
> 
> {{{
> if argspec is not None and argspec[0] and argspec[0][0] in ('cls', 'self'): 
> }}}
> 
> instead of
> 
> {{{
> if isclassinstance(obj) or inspect.isclass(obj): 
> }}}
> 
> which you have included, commented out, on the line above, and which you used on line 819 for something similar?

Good question. I don't know if there was a concrete reason.

I guess I did this because it is in `sage_autodoc.MethodDocumenter.format_args`, hence, we already know that we are dealing with a method. So, I was inclined to simply delete `argspec[0][0]`, but then I thought "better safe than sorry".

The commented-out line could be removed, if you wish.

> I'll look into some doctests...

Looking forward!


---

Comment by jsrn created at 2011-04-07 10:47:08

Ok, added some doctests and a bit better documentation in sage_wraps. Unfortunately, there was also a bug in suboptions, which I have fixed (I had forgotten to update it like I did options back when _sage_getargspec became _sage_argspec_. I'm not quite sure, but perhaps suboptions never really worked in the documentation; it does now (and plot.contour_plot looks pretty crazy)).

Phew, I'm getting dizzy from pushing and popping patches everytime I need to change something in the bottom patch :-S


---

Comment by jsrn created at 2011-04-07 10:47:08

Changing assignee from mvngu to jsrn.


---

Comment by jsrn created at 2011-04-07 10:56:57

inspect.getargspec is used two places that we haven't touched: plot.plot3d.plot3d and server.notebook.interact. I am wondering whether they should use sageinspect.sage_getargspec instead.

plot3d uses it for getting information on the constructor of child classes of Coordinate; can these ever be Cython classes e.g.? I guess they could be decorated classes, which means that the inspection code in plot3d will fail, as it would see the decorator's constructor.

interact uses it for the `@`interact decorator to get information on what widgets to present to the user. I guess we have the same again: it might be an already decorated function we `@`interact with, meaning that code will fail. Can one write Cython code interactively in the notebook (I guess not; it would need to be compiled)?

Continuing my review...


---

Comment by jsrn created at 2011-04-07 11:01:54

The comment on line 515 of sage.misc.sageinspect._sage_getargspec_cython is out of date as the output of the function is now the named tuple ArgSpec. It should probably contain a reference to the inspect.getargspec of the Python  standard library.


---

Comment by jsrn created at 2011-04-07 11:03:25

Replying to [comment:81 jsrn]:
> The comment on line 515 of sage.misc.sageinspect._sage_getargspec_cython is out of date as the output of the function is now the named tuple ArgSpec. It should probably contain a reference to the inspect.getargspec of the Python  standard library.
Argh! Sorry -- you've changed it so that one still just returns a tuple :-S


---

Comment by jsrn created at 2011-04-07 11:07:54

In sageinspect.sage_getargspec, you read the contents of _sage_argspec_() (if present) and transform it to a named tuple. But shouldn't it _always_ be a named tuple? I certainly assume so in the options decorators...


---

Comment by jsrn created at 2011-04-07 11:19:36

I'm worried about lines 722-725 of sage_getarcspec: that TypeError which you silently catch, is that only raised in case obj._sage_argspec_() does not fit inside an ArgSpec? In that case, as my above comment indicates, I think that should not be caught, but instead go to the user so we can see the bug and fix it. In that case, the try-catch block should be changed back into an hasattr-block so as not to confuse the reader into thinking that we expect the object to have the _sage_argspec_ attribute.


---

Comment by jsrn created at 2011-04-07 11:44:26

Ok, this might be nitpicking, but I'm not completely happy with your hack in lines 731-740: first off, the following function definition, I think, would cause the code to fail:


```
def monkey2(a={(1+2) : 'wee'}):
   return a[3]
```


and in general, there's no way to avoid that with your approach, as you can't match nested parentheses with regular expressions.

Ok, moving back to realism, is this then really what we want? I mean, if a decorator is so insightful so as to save the wrapped function's src in its own _sage_src_, but does not save its argspec in _sage_argspec_, aren't we asking for errors? (I'm talking in the future and not right now where of course _sage_argspec_ has just been introduced.) And wouldn't it be nice that this "error" is quite visible in the documentation so authors and reviewers can find the error? I would be perfectly happy and glad with groebner_basis and similar functions having documentation slightly off until cached_method is changed to write to _sage_argspec_ (which I guess will probably end up being in the same release as this ticket).

Of course, we could also retain this fix until such time as the cached_method is fixed, and ticket #11115 could have the removal of this code in its ticket. Was this what you had in mind all along?


---

Comment by SimonKing created at 2011-04-07 12:03:58

Replying to [comment:80 jsrn]:
> inspect.getargspec is used two places that we haven't touched: plot.plot3d.plot3d and server.notebook.interact. I am wondering whether they should use sageinspect.sage_getargspec instead.

But I think that would better be on a new ticket.


---

Comment by jsrn created at 2011-04-07 12:05:23

> Can one write Cython code interactively in the notebook (I guess not; it would need to be compiled)?

Ok, duh! I just finished reading your patch and that pretty much answers my question ;-) Pretty cool.

It's a peculiar thing and a bit too bad that now one can introspect interactive cython objects but not interactive python objects :-)

I'm through reading the code, and apart from my above comments, it looks good. I've also experimented a bit and that all worked. If the doctests all work and the documentation builds, then I'm close to a green light :-)

Oh, one more thing: I don't understand the "except TypeError" on line 763. When will the exception be thrown and why do you revert to Cython parsing in those cases?


---

Comment by SimonKing created at 2011-04-07 12:06:40

Replying to [comment:83 jsrn]:
> In sageinspect.sage_getargspec, you read the contents of _sage_argspec_() (if present) and transform it to a named tuple. But shouldn't it _always_ be a named tuple? I certainly assume so in the options decorators...

I wouldn't rely on the assumption that it is a named tuple.


---

Comment by SimonKing created at 2011-04-07 12:10:22

Replying to [comment:84 jsrn]:
> I'm worried about lines 722-725 of sage_getarcspec: that TypeError which you silently catch, is that only raised in case obj._sage_argspec_() does not fit inside an ArgSpec?

No, the type error silently tests whether the object is a class - in which case `obj._sage_argspec_()` would be called without an argument (which gives rise to a type error).

`inspect.ArgSpec(*obj._sage_argspec_())` works regardless whether _sage_getargspec_ returns a tuple, a named tuple or a list.


---

Comment by SimonKing created at 2011-04-07 12:13:51

Replying to [comment:85 jsrn]:
> Ok, this might be nitpicking, but I'm not completely happy with your hack in lines 731-740: first off, the following function definition, I think, would cause the code to fail:
> 
> {{{
> def monkey2(a={(1+2) : 'wee'}):
>    return a[3]
> }}}

Voilà.


```
sage: def monkey2(a={(1+2) : 'wee'}):
....:        return a[3]
....: 
sage: sage.misc.sageinspect.sage_getargspec(monkey2)
ArgSpec(args=['a'], varargs=None, keywords=None, defaults=({3: 'wee'},))
```


> and in general, there's no way to avoid that with your approach, as you can't match nested parentheses with regular expressions.

By the way, it wasn't my trick. I copied it from the corresponding lines of _sage_getargspec_cython.
 
> Ok, moving back to realism, is this then really what we want? I mean, if a decorator is so insightful so as to save the wrapped function's src in its own _sage_src_, but does not save its argspec in _sage_argspec_, aren't we asking for errors?

In the near future (#11115) the cached method decorators will have _sage_argspec_.

> Of course, we could also retain this fix until such time as the cached_method is fixed, and ticket #11115 could have the removal of this code in its ticket. Was this what you had in mind all along?

Somehow.


---

Comment by SimonKing created at 2011-04-07 12:25:15

Replying to [comment:87 jsrn]:
> Oh, one more thing: I don't understand the "except TypeError" on line 763. When will the exception be thrown and why do you revert to Cython parsing in those cases?

Here is an example where the code is used:

```
sage: from sage.rings.polynomial.real_roots import bernstein_polynomial_factory_ratlist
sage: from sage.misc.sageinspect import sage_getargspec
sage: sage_getargspec(bernstein_polynomial_factory_ratlist.coeffs_bitsize)
ArgSpec(args=['self'], varargs=None, keywords=None, defaults=None)
```


You can see it when you insert some print statements in the relevant lines of code (that is what I just did). Note that this example is a doc test. I found it when in an early version of my patch the documentation did not build.


---

Comment by SimonKing created at 2011-04-07 12:30:09

Replying to [comment:90 SimonKing]:
> By the way, it wasn't my trick. I copied it from the corresponding lines of _sage_getargspec_cython.

Regarding the regular expression used: 

The regular expression just extracts the line of code in which the function's arguments are defined (or cdefined, if it is Cython). Then, that definition is turned into a dummy Python function (even if it was Cython code). And _sage_argspec_from_ast knows how to deal with that case.

In particular, the regular expression is _not_ used to extract the arguments directly! That would indeed be difficult.

By the way, providing typed arguments in Cython works as well:

```
sage: cython("cpdef int foo(bint x, int y=5) except -1: return 1")
sage: sage.misc.sageinspect.sage_getargspec(foo)
ArgSpec(args=['x', 'y'], varargs=None, keywords=None, defaults=(5,))
```



---

Comment by SimonKing created at 2011-04-07 12:35:35

I seems that the patchbot caught the wrong order in which to apply the patches. Therefore:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch


---

Comment by jsrn created at 2011-04-07 13:33:35

> Voilà.
> 
> {{{
> sage: def monkey2(a={(1+2) : 'wee'}):
> ....:        return a[3]
> ....: 
> sage: sage.misc.sageinspect.sage_getargspec(monkey2)
> ArgSpec(args=['a'], varargs=None, keywords=None, defaults=({3: 'wee'},))
> }}}
> 
> > and in general, there's no way to avoid that with your approach, as you can't match nested parentheses with regular expressions.
> 
> By the way, it wasn't my trick. I copied it from the corresponding lines of _sage_getargspec_cython.

I should have been more clear: the above example works with sage_getargspec as it never reaches the statement in question. What I meant was, that some object would reach the definition, then having that _sage_src_ (or something like it) would cause the regular-expression to fail. But now I'm pretty confused: which kind of objects did you envision are classinstances, are callable and have _sage_src_ attribute set? decorators which have not yet been applied to a function?

>  
> > Ok, moving back to realism, is this then really what we want? I mean, if a decorator is so insightful so as to save the wrapped function's src in its own _sage_src_, but does not save its argspec in _sage_argspec_, aren't we asking for errors?
> 
> In the near future (#11115) the cached method decorators will have _sage_argspec_.
> 
> > Of course, we could also retain this fix until such time as the cached_method is fixed, and ticket #11115 could have the removal of this code in its ticket. Was this what you had in mind all along?
> 
> Somehow.

Good :-)


---

Comment by jsrn created at 2011-04-07 13:42:07

> You can see it when you insert some print statements in the relevant lines of code (that is what I just did). Note that this example is a doc test. I found it when in an early version of my patch the documentation did not build.

Ok, thanks for the example. I think I get it.

I don't really have anything then; everything built fine and dandy and all tests passed. Green light from me.


---

Comment by SimonKing created at 2011-04-07 16:11:07

Replying to [comment:94 jsrn]:
> I should have been more clear: the above example works with sage_getargspec as it never reaches the statement in question. What I meant was, that some object would reach the definition, then having that _sage_src_ (or something like it) would cause the regular-expression to fail.

Again, the regular expression is not directly extracting the arguments from the source code, but it is only extracting the "head" of the definition.

Perhaps the following convinces you: We create an object with a _sage_src_ method returning the source code you suggested.

```
sage: cython('''
....: cdef class MyClass:
....:     def _sage_src_(self):
....:         return "def monkey2(a={(1+2) : 'wee'}):\\n    return a[3]"
....:     def __call__(self, x,y):
....:         return "something"
....: ''')
sage: O = MyClass()
sage: print O._sage_src_()
def monkey2(a={(1+2) : 'wee'}):
    return a[3]
```


Let us test that the relevant part of sage_getargspec is really executed:

```
sage: callable(O)
True
sage: import inspect
sage: hasattr(O,'_sage_argspec_')
False
sage: inspect.isfunction(O)
False
sage: inspect.ismethod(O)
False
sage: sage.misc.sageinspect.isclassinstance(O)
True
sage: hasattr(O,'_sage_src_')
True
```


Now, we would expect that sage_getargspec relies on the (fake) source code returned by O, not on the actual arguments of its `__call__` method. But then, indeed something goes wrong:

```
sage: sage.misc.sageinspect.sage_getargspec(O)
ArgSpec(args=['a'], varargs=None, keywords=None, defaults=({None: 'wee'},))
```


Why is it `{None: 'wee'}`, not `{3: 'wee'}`?

I can not work on it right now, but I think that needs to be addressed. So, needs, work...

> But now I'm pretty confused: which kind of objects did you envision are classinstances, are callable and have _sage_src_ attribute set? decorators which have not yet been applied to a function?

No. Decorators which _have_ been applied to a function. For example (without any patches applied): 

```
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: sage.misc.sageinspect.isclassinstance(I.groebner_basis)
True
sage: hasattr(I.groebner_basis,'_sage_src_')
True
```


So, "needs work" because of the monkeys.


---

Comment by SimonKing created at 2011-04-07 16:11:07

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-07 16:23:59

OK, the monkey fails because the regular expression does not correctly determine where the colong belongs to. One obtains the string `"def dummy(a={(1+2) :\n    return"`, which is then analyzed.

Too bad.

Another solution should be found. How complicated? Is there a parsing tool that counts opening and closing brackets? Outside strings? By this I mean the following: 

```
def foo(a="):", b=4):
    return "something"
```



---

Comment by SimonKing created at 2011-04-07 19:09:21

What about using the following little function:

```
def grep_parentheses(s):
    out = []
    single_quote = False
    double_quote = False
    level = 0
    for c in s:
        if level>0:
            out.append(c)
        if c=='(' and not single_quote and not double_quote:
            level += 1
        elif c=='"':
            double_quote = not double_quote
        elif c=="'":
            single_quote = not single_quote
        elif c==')' and not single_quote and not double_quote:
            if level == 1:
                return '('+''.join(out)
            level -= 1
    raise SyntaxError, "The given string does not contain balanced parentheses"
```


Wouldn't it correctly find the first pair of parentheses? And isn't the first pair of parentheses in the definition of a function exacty what we need?

For the exampe from my previous post, one gets:

```
sage: code = 'def foo(a="):", b=4):\n    return'
sage: grep_parentheses(code)
'(a="):", b=4)'
```



---

Comment by SimonKing created at 2011-04-07 19:31:47

Replying to [comment:98 SimonKing]:
> What about using the following little function:

Not there yet. It doesn't correctly recognises sillynesses such as
`code = 'def foo(a="\'):", b=4):\n    return'`.


---

Comment by SimonKing created at 2011-04-07 19:37:41

Better:

```
def grep_parentheses(s):
    out = []
    single_quote = False
    double_quote = False
    level = 0
    for c in s:
        if level>0:
            out.append(c)
        if c=='(' and not single_quote and not double_quote:
            level += 1
        elif c=='"' and not single_quote:
            double_quote = not double_quote
        elif c=="'" and not double_quote:
            single_quote = not single_quote
        elif c==')' and not single_quote and not double_quote:
            if level == 1:
                return '('+''.join(out)
            level -= 1
    raise SyntaxError, "The given string does not contain balanced parentheses"
```



---

Comment by SimonKing created at 2011-04-07 20:32:45

Even with the correct extraction of the head of a function's definition, `_sage_getargspec_from_ast` would not correctly parse some more difficult cases.

At some point, I think we have to accept that `sage_getargspec` can't solve all problems.


---

Comment by jsrn created at 2011-04-08 06:27:33

Replying to [comment:101 SimonKing]:
> Even with the correct extraction of the head of a function's definition, `_sage_getargspec_from_ast` would not correctly parse some more difficult cases.
> 
> At some point, I think we have to accept that `sage_getargspec` can't solve all problems.

Wow, you really worked on this. But the incorrect parsing thing was exactly my problem. And the above point hits exactly: you can have an arbitrary expression in the default argument assignment, so you need to parse an arbitrary Python (Sage) expression for it to correctly determine the ending parenthesis in all cases -- and short of calling the correct method deep inside IPython or something, this should be avoided! As I mentioned in the beginning, this is probably nitpicking and not very realistic, though one __could__ try to catch "argument weirdness" and give an appropriate error message.
Perhaps a wholly different approach in the given case should be considered; I will think about that later today. For now, I have some work to do (which I should have done yesterday ;-) )

Cheers


---

Comment by SimonKing created at 2011-04-08 08:16:33

I replaced the regular expression by the function that I sketched in my post above.

Here is an example that still fails:

```
sage: cython_code = [
... 'cdef class MyClass:',
... '    def _sage_src_(self):',
... '        return "def foo(x, a=\\\')\\\"\\\', b={(2+1):\\\'bar\\\'}): return\\n"',
... '    def __call__(self, m,n): return "something"']
sage: cython('\n'.join(cython_code))
sage: O = MyClass()
sage: print O._sage_src_()
def foo(x, a=')"', b={(2+1):'bar'}): return
```


When we use the "fake" source code to create a Python function, we can correctly analyse its arguments:

```
sage: def foo(x, a=')"', b={(2+1):'bar'}): return
...
sage: sage.misc.sageinspect.sage_getargspec(foo)
ArgSpec(args=['x', 'a', 'b'], varargs=None, keywords=None, defaults=(')"', {3: 'bar'}))
```


However, the analysis using `_sage_getargspec_from_ast` fails:

```
sage: sage.misc.sageinspect._sage_getargspec_from_ast(O._sage_src_())
ArgSpec(args=['x', 'a', 'b'], varargs=None, keywords=None, defaults=(')"', {None: 'bar'}))
```


This is why I believe that there is a bug in `_sage_getargspec_from_ast`.

The question is: Shall we start to debug it thoroughly, or shall we be happy that (with the patch that I am going to submit and in which I replace the regular expression by the parentheses finder) it will become less buggy.


---

Comment by SimonKing created at 2011-04-08 09:12:06

I see that the problem is in sage.misc.sageinspect.SageArgSpecVisitor. It can analyse various types of abstract source trees -- this is implemented in the `visit_*` methods, for `*` in `List`, `Tuple`, `Dict`, `Num`. But `* == BinOp` is missing, and would be needed in the example.

The generic `visit` method from the `ast` module has a bug, I believe: It returns `None`, and this is the `None` that we see as key of the dictionary that is the default value of b in the example above.

I am now trying to add that, and also for the `UnaryOp`. However, the question really is whether it would be worth the effort...


---

Comment by SimonKing created at 2011-04-08 09:30:24

It seems to work, and is not particularly difficult. So, I'll go for it.


---

Comment by jsrn created at 2011-04-08 10:03:24

Cool that you're fixing a bug in SageArgSpecVisitor.

But just to get straight here, the weird case covered in lines 730-741 is only implemented to fix decorators like cached_method, which doesn't correctly set the inspection attributes (more precisely, sets their _sage_src_ correctly but not _sage_argspec_). But for cached_method, this is going to be fixed in #11115. And for other decorators (if they exist), this should also be fixed. And after these fixes, we will remove the code in lines 730-741? In that case, shouldn't we just keep it simple and say that something like your regular expression takes care of all cases needed, and it will be deleted soon anyway?


---

Comment by SimonKing created at 2011-04-08 10:23:56

Replying to [comment:106 jsrn]:
> Cool that you're fixing a bug in SageArgSpecVisitor.
> 
> But just to get straight here, the weird case covered in lines 730-741 is only implemented to fix decorators like cached_method, which doesn't correctly set the inspection attributes (more precisely, sets their _sage_src_ correctly but not _sage_argspec_). But for cached_method, this is going to be fixed in #11115.

Right.

> And for other decorators (if they exist), this should also be fixed. And after these fixes, we will remove the code in lines 730-741?

I don't think so. If I am not mistaken, these lines (and a similar set of lines in a different place) will be used in different cases as well. And since it is not particularly difficult to extend the functionality of the `SageArgSpecVisitor`, I think we should aim for sufficient generality.


---

Comment by SimonKing created at 2011-04-08 10:58:46

The new patch version improves parsing of arguments a lot.

It provides a function `sage.misc.sageinspect._grep_first_pair_of_parentheses`, that is used to find the first matching pair of parentheses without being fooled by parentheses inside string variables. In other words, it finds the sub-string of a function definition that provides its arguments.

Then, it also extends the capabilities of the `SageArgSpecVisitor`. This is a parser for the argspec of a function. It used to be able to parse dicts, lists and tuples. It is now also able to parse binary and boolean and unitary operations, and comparisons. Hence, if those type of things appear in the default arguments of a function, `SageArgSpecVisitor` will find them.

This is relevant for Cython code. From the doctests:

```
sage: cython('def foo(x, a=\')"\', b={not (2+1==3):\'bar\'}): return')
sage: print sage.misc.sageinspect.sage_getsource(foo)
def foo(x, a=')"', b={not (2+1==3):'bar'}): return
sage: sage.misc.sageinspect.sage_getargspec(foo)
ArgSpec(args=['x', 'a', 'b'], varargs=None, keywords=None, defaults=(')"', {False: 'bar'}))
```


Both lines would simply fail with an error, without the patch. With the old patch, the last line would give a wrong answer.

I did not rebuild the documentation and I did not run long tests, yet. But I think it can be reviewed now.

For the patchbot:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-08 10:58:46

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-08 11:21:44

Here are some comments on your new patch:

You should add your name to the author list both in doc/common/sage_autodoc.py and sage/misc/decorators.py.

You demonstrate various underscore methods in your examples. While such methods should be documented, such that a developer can easily find out what needs to be implemented for obtaining a specific functionality, I think it would be better to use the "official" methods that use the underscore methods, such as sage.misc.sageinspect.sage_getsource or ...sage_getargspec. Simply mark them as indirect doctest.

I suggest to edit the new examples, so that the comments appear as proper text. It should also mention the ticket number. Note that you can use unformatted text by using double back ticks, and also note the spelling correction below.Hence,

```
    EXAMPLES:

    Demonstrate that ``_sage_src_`` and ``__doc__`` are retained from the
    decorated function (see trac ticket #9976)::

        sage: def square(f):
        ...     @sage_wraps(f)
        ...     def new_f(x):
        ...         return f(x)*f(x)
        ...     return new_f
```

instead of

```
    EXAMPLES::

        # Demonstrate the _sage_src_ and __doc__ are retained from the
        # decorated function
        sage: def square(f):
        ...     @sage_wraps(f)
        ...     def new_f(x):
        ...         return f(x)*f(x)
        ...     return new_f
```



---

Comment by SimonKing created at 2011-04-08 11:21:44

Changing status from needs_review to needs_work.


---

Comment by jsrn created at 2011-04-08 12:01:26

Replying to [comment:109 SimonKing]:
> Here are some comments on your new patch:

Thank you -- good comments; I'm still a rookie so thanks for the patience ;-)

> 
> You should add your name to the author list both in doc/common/sage_autodoc.py and sage/misc/decorators.py.

There were no authors' list in sage_autodoc, so I made one. Documentation is not created for sage_autodoc.py (heh, recursive documentation), so I guess that was the reason. Anyway, I'm always in doubt as to when a change constitutes something that should be on the authors' list. In time those lists will be terribly bloated, I guess :-S

> 
> You demonstrate various underscore methods in your examples. While such methods should be documented, such that a developer can easily find out what needs to be implemented for obtaining a specific functionality, I think it would be better to use the "official" methods that use the underscore methods, such as sage.misc.sageinspect.sage_getsource or ...sage_getargspec. Simply mark them as indirect doctest.

I completely agree! I didn't know "#indirect doctest" but as far as I could gather, it's used when doctesting a method/function without actually calling that method/function. Since that not what we're doing here, is it really necessary?

> 
> I suggest to edit the new examples, so that the comments appear as proper text. It should also mention the ticket number. Note that you can use unformatted text by using double back ticks, and also note the spelling correction below.Hence,
> {{{
>     EXAMPLES:
> 
>     Demonstrate that ``_sage_src_`` and ``__doc__`` are retained from the
>     decorated function (see trac ticket #9976)::
> 
>         sage: def square(f):
>         ...     `@`sage_wraps(f)
>         ...     def new_f(x):
>         ...         return f(x)*f(x)
>         ...     return new_f
> }}}
> instead of
> {{{
>     EXAMPLES::
> 
>         # Demonstrate the _sage_src_ and __doc__ are retained from the
>         # decorated function
>         sage: def square(f):
>         ...     `@`sage_wraps(f)
>         ...     def new_f(x):
>         ...         return f(x)*f(x)
>         ...     return new_f
> }}}
> 

Yup, done (I think). It seems that decorators.py does not appear in the reference manual; shouldn't that be changed (other ticket)? Do you know how?


---

Comment by jsrn created at 2011-04-08 12:51:26

Replying to [comment:108 SimonKing]:
> The new patch version improves parsing of arguments a lot.
> 
> It provides a function `sage.misc.sageinspect._grep_first_pair_of_parentheses`, that is used to find the first matching pair of parentheses without being fooled by parentheses inside string variables. In other words, it finds the sub-string of a function definition that provides its arguments.

I think there is still problems because you don't consider escaped quotes. For example, putting a single escaped ' in a string argument causes an error:


```
sage: sage: cython('def foo(x, a=\'\\\')"\', b={not (2+1==3):\'bar\'}): return')
sage: sage: print sage.misc.sageinspect.sage_getsource(foo)
def foo(x, a='\')"', b={not (2+1==3):'bar'}): return

sage: sage: sage.misc.sageinspect.sage_getargspec(foo)
ValueError
...
ValueError: Could not parse cython argspec
```


I wish there was some other way than (re)implementing an almost full expression parser for this :-S 

> I don't think so. If I am not mistaken, these lines (and a similar set of lines in a different  place) will be used in different cases as well. And since it is not particularly difficult to extend the functionality of the SageArgSpecVisitor, I think we should aim for sufficient generality. 

When compiling all documentation, the _grep-function is only called from sage_getarcspec on the CachedMethod or RequireField decorators. After these are (eventually) patched, I think it would be a good idea if sage_getargspec threw an error in this case: for then a code author would know he did something which is essentially wrong. It seems you are right that the grep-function is called from the _cython-function on several methods (apparently, Python methods within Cython source files, but I am not sure).

Btw, deleting the folder devel/sage/doc/output and running {{./sage -docbuild all html}} seems to rebuild the entire documentation from scratch. This produces a lot of warnings! They are all like this:


```
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/functions/transcendental.py:docstring of sage.functions.transcendental.Function_zetaderiv:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```


Did I do something wrong?


---

Comment by SimonKing created at 2011-04-08 13:08:32

Replying to [comment:110 jsrn]:
> ...
> > You demonstrate various underscore methods in your examples. While such methods should be documented, such that a developer can easily find out what needs to be implemented for obtaining a specific functionality, I think it would be better to use the "official" methods that use the underscore methods, such as sage.misc.sageinspect.sage_getsource or ...sage_getargspec. Simply mark them as indirect doctest.
> 
> I completely agree! I didn't know "#indirect doctest" but as far as I could gather, it's used when doctesting a method/function without actually calling that method/function. Since that not what we're doing here, is it really necessary?

"#indirect doctest" makes the sage coverage script happy. Namely, if you do "sage -coverage" on some file, it will complain if any function or method appears to not being tested in its doc string. Hence, it will complain if in the `__str__` method of `Foo` you just have `sage: print Foo`, because there is no `__str__` visible. But when you do `sage: print Foo  # indirect doctest`, then you assert that the invisible method _is_ actually tested.

Note that `#indirect doctest` does _not_ influence how the doctest is executed. It really is just for the coverage script.

And yes, I do think that having an indirect test is necessary, since what we want is to enable `sage_getsource` and `sage_getargspec` -- there is no point in demonstrating that a certain object has an attribute `_sage_doc_`, because that is not what is supposed to be called by the user. Mind that the tests in the documentation are, at the same time, examples.

> Yup, done (I think). It seems that decorators.py does not appear in the reference manual; shouldn't that be changed (other ticket)? Do you know how?

Probably it should be a different ticket.

How to add it:

There are some hand-written `.rst` files in doc/en/reference/. Probably you want to edit `misc.rst`, and insert the line

```
   sage/misc/decorators
```

right before `sage/misc/cachefunc`. I guess that would be a good place, because `cachefunc` provides decorators (even though they do not inherit from the stuff in `decorators.py`). 

And that should already be it - after `sage -docbuild reference html`, it should be there.


---

Comment by SimonKing created at 2011-04-08 13:30:37

Replying to [comment:111 jsrn]:
> I think there is still problems because you don't consider escaped quotes.

Right. I have to think about that.

> I wish there was some other way than (re)implementing an almost full expression parser for this :-S 

Indeed.

> When compiling all documentation, the _grep-function is only called from sage_getarcspec on the CachedMethod or RequireField decorators. After these are (eventually) patched, I think it would be a good idea if sage_getargspec threw an error in this case: for then a code author would know he did something which is essentially wrong.

I don't think so.

In some cases, `sage_getargspec` has to rely on source code. Here I am not talking about decorators and other fancy stuff (these can have `_sage_argspec_`), but about ordinary functions and methods. Also I am not talking about the output of some obscure `_sage_src_` method, but about actual source files.

Hence, `sage_getargspec` should be able to correctly parse anything that is valid code in Python or Cython. 

> Btw, deleting the folder devel/sage/doc/output and running {{./sage -docbuild all html}} seems to rebuild the entire documentation from scratch.

But "from scratch", it will be only for those parts that were recently rebuilt. So, when you want to re-build documentation of a file, you should touch it, do `sage -b`, and then `sage -docbuild ...`.

> This produces a lot of warnings! They are all like this:
> 
> {{{
> /home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/functions/transcendental.py:docstring of sage.functions.transcendental.Function_zetaderiv:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
> }}}
> 
> Did I do something wrong?

I don't think so.

At `sage/functions/transcendental.py` in line 166, I see that the doc string starts with """, not with r""". Hence, it is not a raw string. But then, in the latex example in line 183, the "\right" will be interpreted as a line break "\r" followed by "ight". You can see this if you do

```
sage: sage.functions.transcendental.Function_zetaderiv?
```


So, it is neither your nor my fault. But in a few seconds, I will upload a new version of my doc fixes patch.


---

Comment by SimonKing created at 2011-04-08 13:32:06

Patch updated.

For the patchbot:

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-08 13:49:43

My patch is updated, with a new doc test (demonstrating that your example with escaped quotes works):

```
        sage: cython('def foo(x, a=\'\\\')"\', b={not (2+1==3):\'bar\'}): return')
        sage: print sage.misc.sageinspect.sage_getsource(foo)
        def foo(x, a='\')"', b={not (2+1==3):'bar'}): return
        <BLANKLINE>
        sage: sage.misc.sageinspect.sage_getargspec(foo)
        ArgSpec(args=['x', 'a', 'b'], varargs=None, keywords=None, defaults=('\')"', {False: 'bar'}))
```



---

Comment by jsrn created at 2011-04-08 14:03:07

> I don't think so.
> 
> In some cases, `sage_getargspec` has to rely on source code. Here I am not talking about decorators and other fancy stuff (these can have `_sage_argspec_`), but about ordinary functions and methods. Also I am not talking about the output of some obscure `_sage_src_` method, but about actual source files.
> 
> Hence, `sage_getargspec` should be able to correctly parse anything that is valid code in Python or Cython. 

I think this leads to a long religious discussion on when to stop servicing and when to start putting restrictions on the freedom of writing code. One can do pretty sick things in Python, and there are both arguments for and against allowing/encouraging doing these things in a large system like Sage; and one of the "mechanisms" of controlling/limiting this could be via service functions like sage_getargspec. BUT: I definitely agree that the precedence already in sage_getargspec is to be as open-minded as possible, so your code and bugfix is an enhancement on the current trend. (one could always this religious discussion to sage-devel, probably leading to a long, pointless discussion with little outcome ;-) )

> 
> > Btw, deleting the folder devel/sage/doc/output and running {{./sage -docbuild all html}} seems to rebuild the entire documentation from scratch.
> 
> But "from scratch", it will be only for those parts that were recently rebuilt. So, when you want to re-build documentation of a file, you should touch it, do `sage -b`, and then `sage -docbuild ...`.

I thought so too, but it doesn't seem like that. Possibly, like Make, the docbuilder will look for whether the source files changed OR the result files are gone. If either is true, it rebuilds. If trying to rebuild just one or few file's documentation, it is a lot easier just touching the files. 

> I don't think so.
> 
> At `sage/functions/transcendental.py` in line 166, I see that the doc string starts with """, not with r""". Hence, it is not a raw string. But then, in the latex example in line 183, the "\right" will be interpreted as a line break "\r" followed by "ight". You can see this if you do
> {{{
> sage: sage.functions.transcendental.Function_zetaderiv?
> }}}
> 
> So, it is neither your nor my fault. But in a few seconds, I will upload a new version of my doc fixes patch.

Cool. Docbuilding....


---

Comment by jsrn created at 2011-04-08 14:07:43

Replying to [comment:112 SimonKing]
> "#indirect doctest" makes the sage coverage script happy. Namely, if you do "sage -coverage" on some file, it will complain if any function or method appears to not being tested in its doc string. Hence, it will complain if in the `__str__` method of `Foo` you just have `sage: print Foo`, because there is no `__str__` visible. But when you do `sage: print Foo  # indirect doctest`, then you assert that the invisible method _is_ actually tested.
> 
> Note that `#indirect doctest` does _not_ influence how the doctest is executed. It really is just for the coverage script.
> 
> And yes, I do think that having an indirect test is necessary, since what we want is to enable `sage_getsource` and `sage_getargspec` -- there is no point in demonstrating that a certain object has an attribute `_sage_doc_`, because that is not what is supposed to be called by the user. Mind that the tests in the documentation are, at the same time, examples.

Ok, I get that. But as opposed to your __str__ example, the doc-examples/tests of decorators.py are on class documentation or in the sage_wraps function. Therefore, the coverage script will see that the class/function in question are in the test; it doesn't know my intention to test the _sage_src_ or _sage_argspec_ fields anyway.


> 
> > Yup, done (I think). It seems that decorators.py does not appear in the reference manual; shouldn't that be changed (other ticket)? Do you know how?
> 
> Probably it should be a different ticket.
> 
> How to add it:
> 
> There are some hand-written `.rst` files in doc/en/reference/. Probably you want to edit `misc.rst`, and insert the line
> {{{
>    sage/misc/decorators
> }}}
> right before `sage/misc/cachefunc`. I guess that would be a good place, because `cachefunc` provides decorators (even though they do not inherit from the stuff in `decorators.py`). 
> 
> And that should already be it - after `sage -docbuild reference html`, it should be there.

Thanks. I'll possibly look into this.


---

Comment by jsrn created at 2011-04-09 08:54:34

I still seem to get some warnings when compiling the documentation; as before, they do not seem to be because of either of our patches. I couldn't figure out what was wrong with the first (not a very helpful error message). These are the warnings I get:


```
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/categories/category_types.py:docstring of sage.categories.category_types:2: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/combinat/sf/jack.py:docstring of sage.combinat.sf.jack.ZonalPolynomials:3: (WARNING/2) Literal block expected; none found.
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/functions/hyperbolic.py:docstring of sage.functions.hyperbolic.Function_csch:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/modular/modform/submodule.py:docstring of sage.modular.modform.submodule:2: (ERROR/3) Unexpected indentation.
/home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/schemes/generic/morphism.py:docstring of sage.schemes.generic.morphism.SchemeMorphism_structure_map:4: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/jsrn/sage-dev/devel/sagenb/sagenb/notebook/interact.py:docstring of sagenb.notebook.interact.ColorInput:4: (ERROR/3) Unexpected indentation.
/home/jsrn/sage-dev/devel/sagenb/sagenb/notebook/interact.py:docstring of sagenb.notebook.interact.input_grid:26: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/home/jsrn/sage-dev/devel/sagenb/sagenb/notebook/interact.py:docstring of sagenb.notebook.interact.input_grid:28: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```



---

Comment by SimonKing created at 2011-04-09 09:22:08

Replying to [comment:118 jsrn]:
> {{{
> /home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/categories/category_types.py:docstring of sage.categories.category_types:2: (ERROR/3) Unexpected indentation.
> <autodoc>:0: (ERROR/3) Unexpected indentation.

Mysterious indeed.

> /home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/combinat/sf/jack.py:docstring of sage.combinat.sf.jack.ZonalPolynomials:3: (WARNING/2) Literal block expected; none found.
> ...
> /home/jsrn/sage-dev/devel/sagenb/sagenb/notebook/interact.py:docstring of sagenb.notebook.interact.input_grid:28: (WARNING/2) Block quote ends without a blank line; unexpected unindent.

That looks like the doc bugs that I squashed in my second patch.

However, I think the important question is: Do we get these warnings without our patches? If we do then it would be ok to accept these warnings. If we don't then it could also be that without our patches the documentation was based on the wrong doc string (e.g., if a method is wrapped by some decorator). But keep in mind that it is not the purpose of this ticket to clean up all doc strings!

By the way, I slightly lost track: Did you provide indirect doctests for your patch, exhibiting the way `_sage_argspec` is supposed to be used? It would also be possible that I do, by a reviewer patch.

Concerning review: It seems that [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/dd7de9c504c13164) gave us permission that I review your patch and you review mine - provided that we honestly think we are non-biased with respect to the other person's patch.


---

Comment by SimonKing created at 2011-04-09 09:30:20

Replying to [comment:118 jsrn]:
> I still seem to get some warnings when compiling the documentation; as before, they do not seem to be because of either of our patches. I couldn't figure out what was wrong with the first (not a very helpful error message). These are the warnings I get:

Concerning two of the warnings: 

> /home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/categories/category_types.py:docstring of sage.categories.category_types:2: (ERROR/3) Unexpected indentation.

See [here](http://sagemath.org/doc/reference/sage/categories/category_types.html#sage.categories.category_types.ChainComplexes) for a broken doc string in that module.

> /home/jsrn/sage-dev/local/lib/python2.6/site-packages/sage/combinat/sf/jack.py:docstring of sage.combinat.sf.jack.ZonalPolynomials:3: (WARNING/2) Literal block expected; none found.

See [here](http://sagemath.org/doc/reference/sage/combinat/sf/jack.html#sage.combinat.sf.jack.JackPolynomials_p.scalar_jack_basis) for some broken doc string in that module. 

So, it could really be that it has nothing to do with our patches.


---

Comment by jsrn created at 2011-04-11 09:05:42

Replying to [comment:120 SimonKing]:
> So, it could really be that it has nothing to do with our patches.

I'm afraid it must have (though I don't know how): I popped all three patches, rebuilt (./sage -b), deleted doc/output, and rebuilt documentation (./sage -docbuild reference html). No warnings. Then a reapplied all three patches, rebuilt, delete doc/output, rebuilt documentation: all the mentioned warnings 
:-(((

> By the way, I slightly lost track: Did you provide indirect doctests for your patch, exhibiting the way _sage_argspec is supposed to be used? It would also be possible that I do, by a reviewer patch.
Yes I changed the old doctests to use sage_getargspec, though I did not flag them as #indirect doctest. As I wrote in comment 117, I don't understand why that flag needs to be used. 

> Concerning review: It seems that  sage-devel gave us permission that I review your patch and you review mine - provided that we honestly think we are non-biased with respect to the other person's patch. 
Yes, I saw that and I agree. I think we have been appropriately critical and meticulous about each other's patches ;-)


---

Comment by SimonKing created at 2011-04-13 14:44:26

I did several corrections in sage/categories/category_types.py: Some wrong indentations, some non-raw strings containing backslashes, etc. It seems that at least one broken documentation, namely of `AbelianCategory`, is inherited from sage/categories/category.py.

In sage/categories/category.py, I found a huge number of mistakes in the doc strings. Its a mess. I am trying to clean that now.


---

Comment by SimonKing created at 2011-04-13 15:10:59

sage/functions/hyperbolic.py: Here I found another non-raw string containing backslashes.

sage/modular/modform/submodule.py: That was caused by

```
EXAMPLE:
    sage: ...
```

versus

```
EXAMPLE::

    sage: ...
```


sage/schemes/generic/morphism.py was easy to fix.

sagenb/notebook/interact.py: Again some non-raw strings, and `:` versus `::`.

I am now updating my patch doc_fixes patch.


---

Attachment

Apply to devel/sagenb repository: Fix some syntax errors in interact documentation


---

Comment by SimonKing created at 2011-04-13 15:25:18

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-13 15:25:18

I updated my patch.

In fact I had to add another patch: It belongs to the devel/sagenb repository. So, be careful where you apply it!

Concerning the indirect doctests: Meanhile I think that you are right. There is no class method `_sage_argspec_`, and hence no documentation for it. So, an indirect test makes no sense.

I am now running long doctests (based on sage-4.7.alpha5). If they pass then I can give your patch a positive review. I hope that you will cross-verify the syntax fixes in the documentation.

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch 9976_notebook_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-13 17:15:15

The long tests pass all for me. The patch [attachment: trac_9976_decorated_generic_sigs_alternative.patch] looks fine to me, and it does what it claims. So, I give it a positive review.

I hope you (or someone else) can say the same about my patches, after the recent documentation fixes.


---

Comment by jhpalmieri created at 2011-04-13 20:54:44

There is a lot on this ticket, and I haven't read most of it.  But here is one comment nonetheless: suppose I have this in a Sage library file:

```
from sage.misc.cachefunc import CachedFunction

def test1():
    "This is a docstring for test1"
    pass

test2 = CachedFunction(test1)

@CachedFunction
def test3():
    "This is a docstring for test3"
    pass
```

Then if I import everything from this file, from the "sage:" prompt, I get the right docstrings for the right functions.  Great!  On the other hand, the function test3 is completely missing from the reference manual (as is test2, but I don't consider that as important).  This means that if you have a really important function that you want to cache, it seems as though you need to attach two names to it, a non-cached version for the reference manual and then a cached version for actual use.  Is that right?  Is there any way around it?  Or am I doing something wrong?


---

Comment by jhpalmieri created at 2011-04-13 21:05:57

Or is this issue with cached functions dealt with by #11115?


---

Comment by SimonKing created at 2011-04-13 21:24:24

Replying to [comment:127 jhpalmieri]:
> There is a lot on this ticket, and I haven't read most of it.  But here is one comment nonetheless: suppose I have this in a Sage library file:
> {{{
> from sage.misc.cachefunc import CachedFunction
> 
> def test1():
>     "This is a docstring for test1"
>     pass
> 
> test2 = CachedFunction(test1)
> 
> `@`CachedFunction
> def test3():
>     "This is a docstring for test3"
>     pass
> }}}
> Then if I import everything from this file, from the "sage:" prompt, I get the right docstrings for the right functions.  Great!  On the other hand, the function test3 is completely missing from the reference manual

Why do you think test3 is missing? The cached version of test3 has the name test3, and when you do "from mymodule import test3" then you are supposed to get the cached version of test 3, with the documentation saying "This is a docstring for test3". If I am not mistaken, this was the case even without our patches.

Concrete example, _without_ our patches:

```
sage: sage.databases.cunningham_tables.cunningham_prime_factors?
Type:           CachedFunction
Base Class:     <class 'sage.misc.cachefunc.CachedFunction'>
String Form:    Cached version of <function cunningham_prime_factors at 0x38e62a
8>
Namespace:      Interactive
File:           /mnt/local/king/SAGE/sage-4.6.2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py
Definition:     sage.databases.cunningham_tables.cunningham_prime_factors(self, *args, **kwds)
Docstring:
       List of all the prime numbers occuring in the so called Cunningham
       table. They occur in the factorization of numbers of type b^n+1 or
       b^n-1 with b in {2,3,5,6,7,10,11,12}. Data from
       http://cage.ugent.be/~jdemeyer/cunningham/

Class Docstring:
       Create a cached version of a function, which only recomputes values
       it hasn't already computed. Synonyme: ``cached_function``
...
```


In other words, it does show you the documentation of the wrapped function. In addition, it also shows you the documentation of `CachedFunction`. 

It seems that the Cunningham database was not included in the reference manual, but it _should_ show the documentation of the wrapped function, not of the wrapper class.

However, as you see, without our patches you will not get the correct argspec: It says "sage.databases.cunningham_tables.cunningham_prime_factors(self, *args, **kwds)", but should say "sage.databases.cunningham_tables.cunningham_prime_factors()". It also tells you that you find its definition in sage/misc/cachefunc.py, which is of course wrong.

The main point of this ticket is to improve the issue with argspec. Documentation as such worked before.


---

Comment by jhpalmieri created at 2011-04-13 21:31:48

Replying to [comment:129 SimonKing]:
> Replying to [comment:127 jhpalmieri]:

> > Then if I import everything from this file, from the "sage:" prompt, I get the right docstrings for the right functions.  Great!  On the other hand, the function test3 is completely missing from the reference manual
> 
> Why do you think test3 is missing? 

It's missing *from the reference manual*: I put this code at the bottom of sage/misc/latex.py (just to pick a file at random from among those included in the reference manual), ran "sage -b", and rebuilt the documentation.  The manual had test1 in it, but not test3.  I feel like this is a serious problem with decorated functions (or at least cached functions) and the reference manual: we shouldn't have to sacrifice quality and completeness of documentation to get better performance by caching things.


---

Comment by SimonKing created at 2011-04-13 21:34:48

Replying to [comment:128 jhpalmieri]:
> Or is this issue with cached functions dealt with by #11115?

As I have demonstrated in my preceding post, documentation has not been an issue for cached functions or methods. The correct format of the argspec used to be a problem, which is addressed here.

Note the following issue, without our patches:

```
sage: edit(sage.databases.cunningham_tables.cunningham_prime_factors,'vim')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (53, 0))
...
TypeError: arg is not a module, class, method, function, traceback, frame, or code object
```


I am not sure whether that problem is solved by the tickets from here, or whether you need my patch from #11115 in addition. It definitely works when you have _both_ patches. I am now testing if the patches from here would suffice, but this will take a while.


---

Comment by SimonKing created at 2011-04-13 21:39:39

Replying to [comment:130 jhpalmieri]:
> It's missing *from the reference manual*: I put this code at the bottom of sage/misc/latex.py (just to pick a file at random from among those included in the reference manual), ran "sage -b", and rebuilt the documentation.  The manual had test1 in it, but not test3. 

Really? That's odd.

> I feel like this is a serious problem with decorated functions (or at least cached functions) and the reference manual: we shouldn't have to sacrifice quality and completeness of documentation to get better performance by caching things.

Perhaps you confuse the purpose of the two tickets: Here, we have the purpose of getting the documentation of cached methods right, which also involves to broaden the capability of sage.misc.sageinspect -- it is not about performance at all. #11115 is about performance, but it should certainly not affect the documentation.

So, if a cached function really is not included into the references then that is a bug and should be addressed here. I'll be able to do some tests tomorrow.


---

Comment by jhpalmieri created at 2011-04-13 21:44:20

Replying to [comment:131 SimonKing]:
> Replying to [comment:128 jhpalmieri]:
> > Or is this issue with cached functions dealt with by #11115?
> 
> As I have demonstrated in my preceding post, documentation has not been an issue for cached functions or methods. 

I think you and I are using the word "documentation" differently.  I would say that "introspection" has not been an issue for cached functions or methods, at least if I understand you correctly.  But the autodoc feature of the Sphinx-built reference manual doesn't seem to work properly with cached functions; I don't think it ever has.  So there is an issue.  Maybe it doesn't belong on this ticket, but I was hoping you were dealing with it here.  If it doesn't belong here, do you have any ideas how to fix it?

> Perhaps you confuse the purpose of the two tickets: Here, we have the purpose of getting the documentation of cached methods right, which also involves to broaden the capability of sage.misc.sageinspect -- it is not about performance at all. #11115 is about performance, but it should certainly not affect the documentation.

I was using "performance" to refer to the purpose behind cached functions in general, not just #11115.  You should cache results from a function to speed it up, right?


---

Comment by SimonKing created at 2011-04-13 21:56:47

Before sleeping, a last data point: I've put your example into a file testmod.py. Even without our patches, one gets:

```
sage: import testmod
sage: dir(testmod)
['CachedFunction', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'test1', 'test2', 'test3']
```


AFAIK, the reference builder searches the members of a module, and thus should certainly include test1, test2 and test3.

Hm. Unless it skips class instances, which could very well be. If this was the case then (at least) we are not to blame for it, since it was like that before.

I already have a potential solution (should it be the case that class instances are not included into the references): It should be reasonable to include a class instance if its documentation is different from the documentation of its class.


---

Comment by SimonKing created at 2011-04-13 22:03:30

Replying to [comment:133 jhpalmieri]:
> But the autodoc feature of the Sphinx-built reference manual doesn't seem to work properly with cached functions; I don't think it ever has.  So there is an issue.  Maybe it doesn't belong on this ticket, but I was hoping you were dealing with it here.  If it doesn't belong here, do you have any ideas how to fix it?

On the one hand, the original purpose of this ticket was to fix the signature of decorated functions and methods - which means it does not belong here. On the other hand, it does say "signature of decorated _functions_/methods". So, if cached functions are not included in the references then it does belong here.

My snap diagnose is that the documentation builder skips class instances, unless they are members of another class. Hence, cached methods are documented, but cached functions aren't. By the way, it is no surprise that nobody complained about it, before, since `@`cached_method is hardly used, yet. Certainly not as frequently  as cached methods.

If it is easy to fix, I think we should try it here.


---

Comment by SimonKing created at 2011-04-13 22:05:11

Replying to [comment:135 SimonKing]:
> By the way, it is no surprise that nobody complained about it, before, since `@`cached_method is hardly used, yet. Certainly not as frequently  as cached methods.

Typo! I meant to write "`@`cached_function is hardly used".


---

Comment by jhpalmieri created at 2011-04-13 22:14:44

> Hm. Unless it skips class instances, which could very well be. If this was the case then (at least) we are not to blame for it, since it was like that before.

Oh, I wasn't blaming you at all, I just looked at the ticket and hoped that you might have fixed it along with the other issues here.

> By the way, it is no surprise that nobody complained about it, before, since `@`cached_function is hardly used, yet.

Correction: if you look at the sage-devel discussion cited in the ticket description, you'll find a complaint from me about exactly this issue.  :)


---

Comment by SimonKing created at 2011-04-14 06:21:45

I think I got it to work.

I inserted at the end of sage/misc/latex.py:

```
from sage.misc.cachefunc import cached_function

def test1():
    "This is a docstring for test1"
    pass

test2 = cached_function(test1)

@cached_function
def test3():
    "This is a docstring for test3"
    pass

class TestClass:
    "Some class documentation"
    def _sage_doc_(self):
        return "Some instance definition"
    def __call__(self):
        return 1

TestInstance = TestClass()
```


Then, I changed one line in doc/common/sage_autodoc.py, namely in `FunctionDocumenter.can_document_member()`: Instead of returning

```
return isinstance(member, (FunctionType, BuiltinFunctionType))
```

it should return

```
return isinstance(member, (FunctionType, BuiltinFunctionType)) or (isclassinstance(member) and _sage_getdoc_unformatted(member)!=_sage_getdoc_unformatted(member.__class__))
```


Then, in the reference page for sage/misc/latex.py, I find


```
class sage.misc.latex.TestClass¶

    Some class documentation

sage.misc.latex.TestInstance()¶

    Some instance definition
```

and

```
sage.misc.latex.test1()¶

    This is a docstring for test1

sage.misc.latex.test2()¶

    This is a docstring for test1

sage.misc.latex.test3()¶

    This is a docstring for test3
```


`test2 = cached_function(test1)` is not the recommended way of creating a cached function: It should be used as in the definition of test3. So, I think it is ok that the documentation of test1 appears twice. The above is just what we want, right?

I am preparing a patch now, and posting in a few minutes.


---

Comment by SimonKing created at 2011-04-14 06:26:55

OK, patch is posted.

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch 9976_notebook_doc_fixes.patch


---

Comment by jsrn created at 2011-04-14 06:39:42

Wow, a lot of action since I left work yesterday ;-)

Replying to [comment:138 SimonKing]:
> I think I got it to work.
> ...
> 
> `test2 = cached_function(test1)` is not the recommended way of creating a cached function: It should be used as in the definition of test3. So, I think it is ok that the documentation of test1 appears twice. The above is just what we want, right?
> 
> I am preparing a patch now, and posting in a few minutes.

Yes, I agree that is a sensible documentation output. I'll run it and test it -- also with the earlier concerns we had. I will also test timing, as it seems that your fix -- though seems to be working fine -- might cost some time to compute for many callables. We'll see...


---

Comment by SimonKing created at 2011-04-14 06:49:53

Replying to [comment:140 jsrn]:
> Yes, I agree that is a sensible documentation output. I'll run it and test it -- also with the earlier concerns we had. I will also test timing, as it seems that your fix -- though seems to be working fine -- might cost some time to compute for many callables. We'll see...

Is timing really an issue for building the documentation?

Also, I doubt that it will have a dramatic effect. After all, it just means to compare two strings for any callable class instance that happens to live on module level. It seems to me that such things do not occur very often.


---

Comment by jsrn created at 2011-04-14 07:02:43

Replying to [comment:141 SimonKing]:
> Replying to [comment:140 jsrn]:
> Is timing really an issue for building the documentation?
It takes me about ½ hour to build the documentation; it would very be nice if this at least didn't get worse...
> 
> Also, I doubt that it will have a dramatic effect. After all, it just means to compare two strings for any callable class instance that happens to live on module level. It seems to me that such things do not occur very often.
Ah, I had mixed up _sage_getdoc and _sage_getargspec -- as the latter sometimes parses the entire source code and builds an AST to go over, calls to this should not be too abundant. Indeed, the worst _sage_getdoc_unformatted seems to do is convert the string to unicode; this should not be very visible on timings.


---

Comment by jsrn created at 2011-04-14 07:51:02

Changing status from needs_review to needs_work.


---

Comment by jsrn created at 2011-04-14 07:51:02

When building the reference manual now, sage.combinat.partition_algebra fails explosively. This is due to it defines (on the top-level, to be included in the reference manual) functions applied using functools.partial. This method breaks different possibilities for later inspection; the error we see is due to Python's own inspect.getsourcelines throwing an error when given a function returned by functools.partial. Here is a minimal example:


```
sage: import functools, inspect
sage: basetwo = functools.partial(int,base=2)
sage: inspect.getsourcelines(basetwo)
<BOOM>
```


I don't know exactly what part of the patch caused this error to be seen now and not earlier (looking at http://sagemath.org/doc/reference/sage/combinat/partition_algebra.html, we can see that before the patch, the offensive elements of the module (e.g.SetPartitionsAk)  were simply not included in the reference manual), but it seems as though it is something that needs fixing.

It seems there are two possibilities:
1) Wrap the lines in sageinspect which causes the error and exits gracefully, producing some best-effort documentation in such weird cases.
2) Write a wrapper/alternative version of functools.partial which properly sets _sage_doc_ and _sage_getargspec_ etc. such that this shouldn't happen. This might entail switching to this partial function instead of functools.partial in other places of Sage than just partition_algebra.

1) should be easiest and perhaps is a good idea in any circumstance (owing to the discussion earlier on whether to service everything or service only well-formed callables). 2) should take some more effort and might be another ticket.


---

Comment by SimonKing created at 2011-04-14 08:45:24

Replying to [comment:143 jsrn]:
> When building the reference manual now, sage.combinat.partition_algebra fails explosively. 
> ...
> I don't know exactly what part of the patch caused this error to be seen now and not earlier (looking at http://sagemath.org/doc/reference/sage/combinat/partition_algebra.html, we can see that before the patch, the offensive elements of the module (e.g.SetPartitionsAk)  were simply not included in the reference manual)

Of course that's the reason why it has not been noticed before. It is something the _should_ probably be included in the reference, but has been skipped, because it was not a class but a class instance.

> 2) Write a wrapper/alternative version of functools.partial which properly sets _sage_doc_ and _sage_getargspec_ etc. such that this shouldn't happen. This might entail switching to this partial function instead of functools.partial in other places of Sage than just partition_algebra.

Why switching? I have not looked at the code of functools.partial, yet. But it sounds like providing a _sage_doc_ and _sage_getargspec_ in functools.partial would suffice for everything else that relies on it.

> 1) should be easiest and perhaps is a good idea in any circumstance (owing to the discussion earlier on whether to service everything or service only well-formed callables). 2) should take some more effort and might be another ticket.

It might be acceptable that after our patches there are still some functions that are not documented as nicely as they should. However, an _error_ building documentation is certainly not acceptable.


---

Comment by jsrn created at 2011-04-14 08:51:43

Replying to [comment:144 SimonKing]: 
> Of course that's the reason why it has not been noticed before. It is something the _should_ probably be included in the reference, but has been skipped, because it was not a class but a class instance.
Probably.
> 
> Why switching? I have not looked at the code of functools.partial, yet. But it sounds like providing a _sage_doc_ and _sage_getargspec_ in functools.partial would suffice for everything else that relies on it.
We can't (or shouldn't) change functools.partial because it's from the Python standard library. We should make a wrapper and put that somewhere in sage.misc, I guess?

> It might be acceptable that after our patches there are still some functions that are not documented as nicely as they should. However, an _error_ building documentation is certainly not acceptable.
Yeah, I agree. We can't fix all the world's problems in this ticket ;-)


---

Comment by SimonKing created at 2011-04-14 11:21:01

After preparing a lecture, I can now do some programming.

I find:

```
sage: sage.combinat.partition_algebra.SetPartitionsAk
<functools.partial object at 0x432d1b0>
sage: inspect.getargspec(sage.combinat.partition_algebra.SetPartitionsAk)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/mnt/local/king/SAGE/sage-4.7.alpha5/devel/sage-main/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.alpha5/local/lib/python/inspect.pyc in getargspec(func)
    801         func = func.im_func
    802     if not isfunction(func):
--> 803         raise TypeError('arg is not a Python function')
    804     args, varargs, varkw = getargs(func.func_code)
    805     return ArgSpec(args, varargs, varkw, func.func_defaults)
sage: sage.combinat.partition_algebra.SetPartitionsAk.args
('A',)
sage: sage.combinat.partition_algebra.SetPartitionsAk.keywords
```


Hence, even though `inspect` can not deal with `functools` (even though it is standard Python), it should be absolutely straight forward to extend `sage_getargspec` to that case.


---

Comment by SimonKing created at 2011-04-14 11:52:53

No, it should be even easier. Instances of functools.partial behave well enough, so that sageinspect can instruct all relevant information: In particula, sage_getsource works. And if that works, then sage_getargspec can simply use the source code analysis (to be precise: Study just the head of the definition).


---

Comment by SimonKing created at 2011-04-14 12:00:41

Sorry, I was mistaken. sage_getfile finds the wrong location, and so sage_getsource won't work either. But an instance of functools.partial has an attribute `.func`, which can then be used.


---

Attachment

Fixing some wrongly formatted doc strings


---

Comment by SimonKing created at 2011-04-14 12:30:09

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-14 12:30:09

I updated the inspection_of_cython.patch: In the relevant functions, I made a special case for instances of functools.partial.

By consequence, building the doc for sage.combinat.partition_algebra showed a couple of warnings, that were caused by syntax errors in the doc string (amazing, how often that occurs in sage/combinat...). It is fixed by an update of my doc_fixes.patch, so that its documentation builds without error, but includes the previously missing items.

The price to pay: Several items have the same documentation. I am willing to pay that price, for the alternative is to not have these docs in the references at all.

Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch 9976_notebook_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-14 12:37:05

PS: The following does not work yet.

```
sage: obj = sage.combinat.partition_algebra.SetPartitionsAk
sage: edit(obj,'vim')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (53, 0))
...
```


But that is a problem in the sage.misc.edit_module. I think it is out of the scope of this ticket. Better have a new one.


---

Comment by jsrn created at 2011-04-14 14:26:47

Good job. Some questions:

1) When doing my previous example and calling sageinspect.sage_getdoc(basetwo), I get the doc of functools.partial. Does this always happen or only in these toy examples?

2) Why doesn't this work, and should it?


```
sage: import functools
sage: import sage.misc.sageinspect as si
sage: def mybase(x=1, y=2):
....:     return x + y
sage: deriv = functools.partial(mybase, x=3)
sage: si.sage_getargspec(deriv)
<BOOM>
sage: si.sage_getsource(deriv)
<BOOM>
```


What if I put the stuff in a file?

3) Partial functions on partial functions seem to will never work with your patch; perhaps you should have the check in a while loop or call the method recursively. This might pertain to other checks in the codes as well!


---

Comment by SimonKing created at 2011-04-14 14:50:16

Replying to [comment:151 jsrn]:
> Good job. Some questions:
> 
> 1) When doing my previous example and calling sageinspect.sage_getdoc(basetwo), I get the doc of functools.partial. Does this always happen or only in these toy examples?
>  
> 2) Why doesn't this work, and should it?
> ...
> What if I put the stuff in a file?

What I did was designed to work on files.

Concerning doc: You did not provide `basetwo` with a custom documentation - if you modify its `__doc__` then it works:

```
sage: deriv.__doc__='blablabla'
sage: si.sage_getdoc(deriv)
'blablabla\n'
```


Certainly sage_getsource can not work on your example, since you do not have a source file.

I believe, however, that sage_getargspec should work on functools.partial, even if there is no source file.

> 3) Partial functions on partial functions seem to will never work with your patch; perhaps you should have the check in a while loop or call the method recursively. This might pertain to other checks in the codes as well!

When I recursively call sage_getargspec on the `.func` attribute then it should work fine. That would be better than asking for the source, in the first place.


---

Comment by SimonKing created at 2011-04-14 14:55:50

No, it is not as easy.

Again, in your `deriv` example:

```
sage: sage_getargspec(deriv.func)
ArgSpec(args=['x', 'y'], varargs=None, keywords=None, defaults=(1, 2))
sage: deriv.keywords
{'x': 3}
```


So, am I right that we want to have 

```
sage: sage_getargspec(deriv)
ArgSpec(args=['x', 'y'], varargs=None, keywords=None, defaults=(3, 2))
```

?


---

Comment by SimonKing created at 2011-04-14 15:04:19

It is still more complicated.

In Argspec, it is assumed that the arguments with default values come last. Apparently, that assumption does not hold, in general, if you apply `partial`:

```
sage: def blablubb(x,y):
....:     return x+y
....: 
sage: f = functools.partial(blablubb,x=3)
sage: f.keywords
{'x': 3}
```


So, what should sage_getargspec(f) return?? Should it raise an error, since the default values are in the wrong place?


---

Comment by SimonKing created at 2011-04-14 15:12:15

If you agree that it does not make sense (or is impossible, in general), to use the functools.partial default values into the argspec, then I really think that both sage_getfile, sage_getsourcelines and sage_getargspec should work recursively.

By consequence, it may fail if you work with Python code that is given interactively, but should work if the code has a source file. That would be another price to pay.


---

Comment by SimonKing created at 2011-04-14 17:46:00

I still don't know what answer I would expect from get_argspec on functools.partial, as in the following example:

```
sage: def f0(a,b,c,x,y,z): print a,b,c,x,y,z
....:
sage: f = functools.partial(f0,1,2,y=3)
```


Now, f can not be provided with a different value for a, b and y. It is possible to provide a value for c and x both by position and by name. A value for z must be provided by name, it is not possible by position.

That certainly does not fit into the scope of an `ArgSpec` named tuple, does it?

Do you agree that in the reference manual, the arguments of f should appear exactly as the arguments of f0? I don't think that there is an easy way to express the fact that some arguments of f can only be provided by name. Therefore, I think it must be left to the module author to state in the doc string which assignments were made to the arguments.

If you tell me that you do agree then I'll provide an update of my patch.


---

Comment by jsrn created at 2011-04-15 06:22:23

Phew, sometimes -- in the name of freedom -- Python standards have just not been thought through :-S Partial seems to be a _very_ confusing function in general, and it seems surprising and very un-Guido Rossum like to have it in the standard library. Notice that Python can not itself figure these things out; if we make wrong calls to your f function above, we get cryptic error messages:


```
sage: f()
...
TypeError: f0() takes exactly 6 non-keyword arguments (2 given)
sage: f(4,5)
...
TypeError: f0() takes exactly 6 non-keyword arguments (5 given)
```


so when I give no arguments, it thinks I gave 2 (to f0), but I have actually given 3. When I supply 2 arguments, it thinks I gave 5. Something is wrong here in the lines of what you have also found.

I think the most generally non-confusing, always working, and easiest to implement solution would be to always use the ArgSpec of the partially applied function (that is, recursively call the sage_get* function). The author of the module should then indeed be wary that his "hack" didn't cause anything to be widely erroneous in the documentation.

Alternatively, make a small heuristic that does the right thing in usual and well-behaved situations: Let e.g. f0 be a function with n positional arguments and m named arguments with default values. If a partial application of a funcion f0 sets the first s positional, sets the last t positional by name, and redefines a number of the m named arguments, then it is still possible to extract this information and enclose it in an ArgSpec. We might even consider giving a warning in cases where this is not done (as it is an error to write Sage code which doesn't document properly, or something). Thinking about it, I don't think this solution is very difficult to implement. However, one might argue that it will overly specialise the sageinspect functions to cater for one certain type of (misbehaving) wrapping, and that Sage authors in general should avoid applying partial to module-level entities.

I would be satisfied with both. I don't think it is good programming practice to use obscure wrapping in module-level entities, so I would accept the first as fine. On the other hand, Sage in several places already take the stance that programmers should be allowed to do whatever works; and in this philosophy, we should aim for the second one.

This patch just keeps going on an on...


---

Comment by jsrn created at 2011-04-15 06:22:23

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-04-15 07:56:01

Replying to [comment:157 jsrn]:
> Alternatively, make a small heuristic that does the right thing in usual and well-behaved situations: Let e.g. f0 be a function with n positional arguments and m named arguments with default values. If a partial application of a funcion f0 sets the first s positional, sets the last t positional by name, and redefines a number of the m named arguments, then it is still possible to extract this information and enclose it in an ArgSpec.

The following example shows the problem with your suggestion:

```
sage: import functools
sage: def f0(a,b,c,d,e,f,x=1,y=2,z=3): return
....: 
sage: f = functools.partial(f0)
sage: f = functools.partial(f0,1,e=4,f=5,z=6)
```

That is as in your suggestion: Providing values for the first s positional arguments by position (here: partial(0,1,...)), and providing values for the last t positional arguments by name (here: partial(..., e=4,f=5,...)), and also providing values for some of those arguments that already have a default value (here: partial(...,z=6)).

However, we can not have

```
sage: sage_getargspec(f)
ArgSpec(args=['c', 'd', 'x', 'y'], varargs=None, keywords=None, defaults=(1,2))
```

since it would appear as if you could provide the arguments x and y by position. Also, we must not include the new default values in `defaults` and keep the associated argument names in `args`: There is no way to re-assign them, and so, they are no longer arguments to the function!

Is there a way to express in an argspec that some arguments can _only_ be provided by name?

If there is no such way, then we must be even more restrictive. Note that all arguments of f0 are positional - that the last few of them have a default does not change the fact that they are positional. So, we can only infer an argspec, if partial assigns values to the first s positions and to the last t positions. Such as here:


```
sage: f = functools.partial(f0,1,f=5,x=6,y=7,z=8)
sage: sage_getargspec(f)    # not implemented
ArgSpec(args=['c', 'd', 'e'], varargs=None, keywords=None, defaults=None)
sage: f = functools.partial(f0,1,y=7,z=8)
sage: sage_getargspec(f)    # not implemented
ArgSpec(args=['c', 'd', 'e', 'f', 'x'], varargs=None, keywords=None, defaults=(1,))
```


> We might even consider giving a warning in cases where this is not done (as it is an error to write Sage code which doesn't document properly, or something). Thinking about it, I don't think this solution is very difficult to implement.

Like a deprecation warning? I think that would be not so good. If people have the freedom to use functools.partial, then we should cope with it.

So, what do you think: Try to infer an argspec in the restricted way that I sketched above, and return the argspec of the underlying function if that is impossible? Or _always_ return the argspec of the underlying function?

Cheers,
Simon


---

Comment by SimonKing created at 2011-04-15 08:01:20

Replying to [comment:158 SimonKing]:
> sage: f = functools.partial(f0,1,e=4,f=5,z=6)

Sorry, type: I meant `functools.partial(f0,1,2,e=4,f=5,z=6)`.


---

Comment by jsrn created at 2011-04-15 08:27:17

This is horrible! What were they thinking?!...

Ok, in this case I think it actually would be best to always return the argspec of the underlying function. It is bad to be forced to erase the default arguments from the argspec, even though they can still be set by name. There I would prefer these args to be in the documentation but then the doc text explained more in depth how it could be used. It is also easier to work around, once the code has been written in one way (and the code author suddenly discovers this documentation issue), I think.

>>  We might even consider giving a warning in cases where this is not done (as it is an error to write Sage code which doesn't document properly, or something). Thinking about it, I don't think this solution is very difficult to implement.
> 
> Like a deprecation warning? I think that would be not so good. If people have the freedom to use functools.partial, then we should cope with it. 

What I meant is to produce a warning in sage_autodoc or sageinspect.sage_* if we come upon a function with this behaviour -- but only on the module-level which is to be documented.

The rationale would be that functools.partial (in cases such as these) very much violates "principle of least surprise" and is therefore bad for the end-user. Code authors should be allowed to do whatever internally in the modules, but for the end-user, we wish them to have a straight-forward, Pythonic experience with Sage; suddenly having functions where arguments can _only_ be given by name and introspection and documentation strings is non-standard, lacking or broken is surprising and confusing. Even more so in a language such as Python, where we expect "one way to do it" and relatively well-behaved foundational syntax rules of the language (where, on the other hand, stuff like this would be practically mandatory in a Perl program ;-) ).

Of course, we should never introduce such things without consulting sage-devel first.

Cheers


---

Comment by SimonKing created at 2011-04-15 08:40:04

Replying to [comment:160 jsrn]:
> Ok, in this case I think it actually would be best to always return the argspec of the underlying function.

Right, let's do so. I'll update my patch accordingly.

> What I meant is to produce a warning in sage_autodoc or sageinspect.sage_* if we come upon a function with this behaviour -- but only on the module-level which is to be documented.
> 
> ...
> Of course, we should never introduce such things without consulting sage-devel first.

Sure. And I think that introducing such warning should _really_ be a different ticket. This here is already fat enough.


---

Comment by jsrn created at 2011-04-15 09:03:38

Replying to [comment:161 SimonKing]:
> Sure. And I think that introducing such warning should _really_ be a different ticket. This here is already fat enough.
Definitely! Let's get this monster out of the way...


---

Comment by SimonKing created at 2011-04-15 12:15:22

The patch is updated. It is now always (recursively) using the `.func` attribute of a `functools.partial` instance. With that change, things should look nice.

One idea concerning the warning: What one could do is modify `sage_getdoc`, so that it prepends a warning message to the doc string of any `functools.partial` instance. Then, the warning would both appear in the reference and in introspection via `?` (not via `??`, but I could be mistaken).

But that's a different ticket.

Needs review...


---

Comment by SimonKing created at 2011-04-15 12:15:22

Changing status from needs_work to needs_review.


---

Comment by jsrn created at 2011-04-15 16:02:35

I'm running doctests now. I've read through the code, and it looks good with many good comments and tests.

While we are waiting for the results, I do have one thing, though: I'm not really fond of the doc-tests that depend on completely unrelated code, like the ones demonstrating error in partition_algebra. It seems to incur a large penalty for developers in the long run, as any change in existing code will break doctests in completely unrelated modules.

Sure, most of these errors will be easy to fix, but then the doctest might become invalid (if e.g. partition_algebra moved away from using functools.partial), and the later developer would have to decide between 1) fixing the doctest and keeping it, even though it no longer serves its purpose, 2) remove the doctest, or 3) rewrite the doctest to use a different module or doctest-created objects. 1) and 2) would result in the error no longer being exercised, defeating the purpose of having this (non-educating) doctests lying around. 3) would be a huge and unwanted burden for the new developer to lift, and he might not have the prerequisites to do it.

One might disagree with this of course. So, is this something that you have seen many places in Sage (so that it is completely acceptable/encouraged doctesting)? Or is it because this particular doctest is impossible to write using dynamic objects (I haven't really yet fully understood which of the functions work on dynamic objects and which only on file-read ones)? Or is there a third reason?

Thanks for the green light on mine, by the way.
Cheers,
Johan


---

Comment by jsrn created at 2011-04-15 16:03:54

Replying to [comment:164 jsrn]:
> ... doc-tests that depend on completely unrelated code, like the ones demonstrating error in partition_algebra.
I meant to write "demonstrating that there is no longer an error with " ;-)


---

Comment by SimonKing created at 2011-04-15 16:34:09

Replying to [comment:164 jsrn]:
> One might disagree with this of course. So, is this something that you have seen many places in Sage (so that it is completely acceptable/encouraged doctesting)? Or is it because this particular doctest is impossible to write using dynamic objects (I haven't really yet fully understood which of the functions work on dynamic objects and which only on file-read ones)? Or is there a third reason?

Certainly the new test for sage_getfile, sage_getsource and sage_getsourcelines all have to use something that has a source file. So, a dynamic definition in Python would not work, since no file would be created - with the patch, introspection for Cython somehow works better than for Python, since there is always a file involved when you  compile Cython code.

However, the functools.partial test for sage_getargspec and sage_getdoc could be replaced by a "dynamic" test, if you prefer.


---

Comment by jsrn created at 2011-04-18 07:24:46

Back from weekend. All tests passed, so the code is good. I'd like dynamic tests for the two functools.partial doctests that you mentioned above, though. After that, it should be green light :-)


---

Comment by jsrn created at 2011-04-18 07:26:48

Yo, listen up thar Patchbot: Apply trac_9976_decorated_generic_sigs_alternative.patch 9976-inspection_of_cython.patch 9976_doc_fixes.patch 9976_notebook_doc_fixes.patch


---

Comment by SimonKing created at 2011-04-18 11:33:59

Replying to [comment:168 jsrn]:
> Yo, listen up thar Patchbot: 

I guess the problem is that the patchbot tries to apply the patches to sage-4.6.2. They do apply to sage-4.7.alpha5 (this is the version I am working with). So, I think we can review it, and if there is any problem merging the patches, the release manager will tell us.

I am now preparing a new and largely extended patch for #11115. After that, I will provide the two "dynamical" tests for the patches here.


---

Attachment

Improve inspection on Cython objects, functools.partial and other class instances; let sage_getargspec return an ArgSpec?; improve argument parsing; let a plot raise an AttributeError? if an attribute is missing; include cached functions in references


---

Comment by SimonKing created at 2011-04-18 16:48:33

I have updated my inspection_of_cython patch, by providing two dynamical tests for functools.partial (namely sage_getdoc and sage_getargspec). Such dynamical tests are impossible for sage_getfile and sage_getsource, since interactive Python code won't create a source file to inspect.

I already gave your patches a green light. So, I hope you are happy with my patches as well...


---

Comment by jsrn created at 2011-04-19 11:56:43

Great, very nice. Everything applies and works fine here, and I already looked through everything more than once. It's a-go.


---

Comment by jsrn created at 2011-04-19 11:56:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-20 12:53:24

Please change the commit message of [attachment:trac_9976_decorated_generic_sigs_alternative.patch] (use `hg qrefresh -e` for that).


---

Comment by jdemeyer created at 2011-04-20 12:55:41

Changing status from positive_review to needs_work.


---

Attachment

Alternative patch: more intrusive Sphinx patch which makes it easier to let decorators change the signature of the wrapped function.


---

Comment by jsrn created at 2011-04-24 18:02:05

Changing status from needs_work to positive_review.


---

Comment by jsrn created at 2011-04-24 18:02:05

Fixed commit message.


---

Comment by jdemeyer created at 2011-05-03 12:29:37

Resolution: fixed


---

Comment by jdemeyer created at 2011-05-24 10:36:00

Patch rebased to sage-4.7


---

Attachment
