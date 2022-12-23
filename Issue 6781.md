# Issue 6781: Library access to ecl

Issue created by migration from https://trac.sagemath.org/ticket/6781

Original creator: nbruin

Original creation time: 2009-08-20 20:00:57

CC:  burcin

ecl can be run "embedded" and has a fairly clean C interface, which should be tightly wrappable in cython.
There are good macros provided for accessing ecl objects, and many of the atomic values should be fairly easily mappable to/from sage or python native datatypes. Hence, data communication on binary level with the ecl library should be doable, and would be a stepping stone towards a binary interface with maxima.

ISSUES:

1. I quote from Section 5.2 of the ECL reference manual:

The collector will not scan the data sectors. If you embed ECL in another program, or link libraries with ECL, you will have to notify ECL which variables point to lisp objects.

So, cython wrapper objects that keep track of an object under ECL memory management will have to do something, but the manual doesn't say what.

2. Maxima currently gets built as a stand-alone executable. Somewhere in the build process, there must exist a lisp-environment that has Maxima built but not running. In order to communicate with maxima as a library (via ECL's API), one would have to get such an image. It does look like Maxima just store its state in LISP's global state, so just calling maxima routines from LISP should work.


---

Attachment

Patch to allow library access to ecl


---

Comment by nbruin created at 2009-08-22 00:09:40

the new patch (which should apply cleanly against 4.1.1) provides enough interface to communicate with ecl via strings.
as proof of concept, there is also a routine to parse CONSes into python lists. Assuming there is an appropriate Maxima image, this interface can already be used to communicate with Maxima. Example session:


```
sage: from sage.libs.ecl import *
sage: init_ecl()
sage: 
sage: ecl_eval("(require 'asdf)");
;;; Loading #P"/usr/local/sage/4.1.1/local/lib/ecl-9.4.1/asdf.fas"
;;; Loading #P"/usr/local/sage/4.1.1/local/lib/ecl-9.4.1/cmp.fas"
;;; Loading #P"/usr/local/sage/4.1.1/local/lib/ecl-9.4.1/sysfun.lsp"
sage: ecl_eval('(load "%s")'%(SAGE_ROOT+"/local/lib/maxima/maxima.fasb"))
;;; Loading "/usr/local/sage/4.1.1/local/lib/maxima/maxima.fasb"
<ECL: #P"/usr/local/sage/4.1.1/local/lib/maxima/maxima.fasb" >
sage: ecl_eval('(in-package :maxima)')
<ECL: #<"MAXIMA" package> >
sage: 
sage: #There is a maxima macro to ease expression parsing
sage: string_to_object("#$x^2$")
<ECL: (MEVAL* '((MEXPT) $X 2)) >
sage: 
sage: #we can also execute maxima routines
sage: L=ecl_eval('($integrate #$x^2$ #$x$)')
sage: L
<ECL: ((MTIMES SIMP) ((RAT SIMP) 1 3) ((MEXPT SIMP) $X 3)) >
sage: #rudimentary parsing of ECL constructs into python
sage: L.python()

[[<ECL: MTIMES >, [<ECL: SIMP >, <ECL: NIL >]],
 [[[<ECL: RAT >, [<ECL: SIMP >, <ECL: NIL >]],
   [<ECL: 1 >, [<ECL: 3 >, <ECL: NIL >]]],
  [[[<ECL: MEXPT >, [<ECL: SIMP >, <ECL: NIL >]],
    [<ECL: $X >, [<ECL: 3 >, <ECL: NIL >]]],
   <ECL: NIL >]]]
```



---

Comment by nbruin created at 2009-09-01 00:20:45

With the new maxima package, the building of maxima.fasb is even easier. The following lines can be appended to spkg-install in "maxima-5.19.1.p0.spkg" (for now available from http://sage.math.washington.edu/home/ghitza/maxima-5.19.1.p0.spkg):

```
cd src/src
ecl -eval "(require 'asdf)" -eval '(load "maxima-build.lisp")' -eval  '(asdf:make-build :maxima :type :fasl)' -eval "(quit)"
cp maxima.fasb $SAGE_LOCAL/lib/maxima
cd ../..
```

We should probably try to catch errors a little better, although the hard part of the building has already happened at this point. It might also be nice to build maxima as a ".fas", which seems to be the more usual format for ecl. We could even just place it in ecl's library then and avoid pathnames altogether.

Furthermore, ecl's cvs version seems to build cleanly in sage too (modulo instabilities inherent to cvs versions). In principle all obstacles have been solved:
 - we can simply remove ECL's signal handlers after boot. As long as sage's signal handlers return when they are supposed to, we should be fine with that.
 - the new rewrites of ecl's bignums allow for an option to prevent ecl from assigning memory management functions to gmp (with very little effect. It only means that some bignum registers will live outside of ecl's normal heap) The memory manager turned out to be the source of the segfault on closing and would have led to segfaults in many extensive computations.


---

Comment by nbruin created at 2009-09-15 01:12:30

As Juanjo suggested on:

http://sourceforge.net/mailarchive/message.php?msg_name=c159f9ab0809140803h1cfc3473p17a7b7afb82a4e71%40mail.gmail.com

we can do a good error-catch by using CL's equivalent of try...except:

```
(defun my-safe-eval (form)
    (handler-case
        (values (eval form))
        (serious-condition (c) (return-from my-safe-eval (values nil (princ-to-string c))))))
```

we lose any multiple return values, but detecting if an error occurred is cheap via NVALUES. VALUES(1) will be a nice string
describing the error (princ seems to turn the condition object into the most informative string)

Furthermore, it seems that renaming a ".fasb" to ".fas" is all that is needed to make the file respond to the usual
"require". If we furthermore symbolically link <ECL-LIBRARY>/maxima.fas to maxima.fasb then loading maxima is really as easy as
(require 'maxima).

To find out the pathname of the current ecl library, do 

```
ecl -eval "(princ (SI:GET-LIBRARY-PATHNAME))" -eval "(quit)"
```



---

Comment by nbruin created at 2009-10-26 04:37:04

Set assignee to nbruin.


---

Comment by nbruin created at 2009-10-26 04:37:27

Changing status from new to needs_review.


---

Comment by nbruin created at 2009-10-26 04:40:08

Changing component from symbolics to packages.


---

Comment by kcrisman created at 2009-11-02 15:44:03

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-02 15:44:03

So far, this looks good.  For some reason I am having trouble with #7287 working properly, and it's possible this is to blame, but this patch on its own seems ok.  I can't give it a positive review, because I do not know enough about Lisp to competently judge it, but various tests I got from random Lisp websites for things not in the doctests also gave correct answers, which is good!

A couple of very minor things:  I notice a few functions in the 800s which aren't separated by a blank line, which makes it harder to read.  There is also a typo in init_ecl - it should be "Do not", not "No not".  I also occasionally get output like this:

```
sage: ecl_eval("(command object)");
outputsage:
```

as opposed to 

```
sage: ecl_eval("(command object)");
output
sage:
```

I can't determine very well when this happens, though it seems to occur fairly reliably after various print commands, like 

```
sage: ecl_eval("(print 3)") ;

3 sage: 
```

Note that if I don't use the ;, since it returns the ECL object, I don't have the problem then:

```
sage: ecl_eval("(print 3)")

3 <ECL: 3>
sage: 
```


So I'm putting this to "needs work" because of these very minor issues, but really it seems good and we just need someone who knows something about Lisp to review it!  Looks nice.


---

Comment by nbruin created at 2009-11-02 18:29:25

Replying to [comment:8 kcrisman]:
> {{{
> sage: ecl_eval("(command object)");
> outputsage:
> }}}
> as opposed to 
> {{{
> sage: ecl_eval("(command object)");
> output
That is not the fault of the interface. Compare:

```
sage: os.system("echo hi");
hi
sage: os.system("echo -n hi");
hisage: 
```

I think most common lisp print routines do NOT include a trailing newline, so I think the above behaviour is expected. ecl_eval and friends should not send anything to STDOUT by themselves.

Thanks for spotting the typos.

I'm changing back to needs_review to invite a more lisp-savvy reviewer.


---

Comment by kcrisman created at 2009-11-04 15:14:37

Is it possible to do this?

ERROR: Please define a s == loads(dumps(s)) doctest.

Now, I get 

```
sage: dumps(x)
---------------------------------------------------------------------------
PicklingError                             Traceback (most recent call last)
<snip>
PicklingError: Can't pickle <type 'ecl.EclObject'>: import of module ecl failed
```

so maybe it isn't possible to do this, but I thought I'd point it out anyway in case it's trivial to fix this and I just don't realize it.


---

Comment by kcrisman created at 2009-11-04 15:14:46

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2009-11-05 16:27:24

Replying to [comment:10 kcrisman]:
> Is it possible to do this?
> 
> ERROR: Please define a s == loads(dumps(s)) doctest.

I noticed that sage doctesting routines prefer to have a test like that. My first reaction is "can't be done". Common Lisp's general approach to saving state is just that: Dump a memory image, so CL is not going to be much help for implementing a workable solution.

I am sure that for many particular ECL structures, one can come up with a reasonable pickling procedure. How do other interfaces solve that (pari, magma, maxima/pexpect, maple)?

For our intended use of the ECL interface, we do not need pickling. A symbolic expression would get translated to Maxima, processed and translated back into SR. So LISP expressions would not persist beyond short timespans.


---

Comment by was created at 2009-11-06 05:56:10

> I noticed that sage doctesting routines prefer to have a test like that.
>  My first reaction is "can't be done". 

Yes it can.    If s == loads(dumps(s)) will be false for any element, or raise an error, put a discussion of that fact in a docstring and put in a doctest like this:

```
sage: s == loads(dumps(s))
boom or False
```

There's no reason to hide that this doesn't work from users.

> How do other interfaces solve that (pari, magma, maxima/pexpect, maple)

magma can't.  pari has the amazing property that for any pretty much any x in pari we have eval(str(x)) == x (with pari notation).    I think the same is true in maxima for symbolic expressions.

This code is new, so is going to be held to a higher standard before being included than code from 2005.


---

Comment by nbruin created at 2009-11-07 04:26:43

Yes, pickling is so nice to have that it makes sense to mention explicitly when it doesn't work. ECL does not support serialization natively, so there is nothing to interface with on that end. There are independent serialization libraries for CL that claim to work with ECL. I do not know their quality.

There is CL-STORE:

http://common-lisp.net/project/cl-store/

current version 0.8.10

which even claims to be able to serialize CLOS object instances. I am not advocating including an extra lisp library at this point, but if someone at some point really want lisp serialization, that would be a place to start looking.

I am updating the attached patch ecllib.patch with:
 - extra newlines between some defs
 - fixed typo
 - `__reduce__` method raising a NotImplementedError and a docstring.


---

Comment by kcrisman created at 2009-11-10 22:36:33

In case there was question - this reviewer still thinks it looks good, still waiting on a Lisp expert to review it.  Problem is, does the Sage team have any of those other than the author?


---

Comment by kcrisman created at 2009-12-21 02:06:28

Does this still work with the newest Maxima?  We don't have an spkg yet, but hopefully will soon - [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7)


---

Attachment

Rebased against 4.3, with str -> bytes changes


---

Comment by nbruin created at 2010-01-16 09:03:46

Updated the patch to apply against 4.3. Cython started to complain about not being able to translate str -> C types anymore and recommended using "bytes" instead. That change has been propagated seemingly without adverse side-effects. Patch seems to work fine in 4.3 now.


---

Comment by burcin created at 2010-02-04 11:42:30

Hi Nils,

Sorry for not looking at this before. I just read the patch and it looks really good. I'd like to try to get this in the next release if possible, to prepare for #7377 proper.

A few quick comments after reading the patch (didn't apply or build yet, maybe over the weekend):
 * The module name you declare on line 431 of `module_list.py` should be sage.libs.ecl.ecl.
 * We would normally put the declarations imported from a header file in a `decl.pxd` in `sage/libs/ecl/`. I suggest renaming the current `ecl.pxd` to `decl.pxd`, and using `from sage.libs.ecl.decl cimport ...` in `ecl.pyx` to import the declarations you need. Then `ecl.pxd` can be used to declare the Cython methods/classes from `ecl.pyx` which should be available for imports from other modules.
 * In `ecl.pyx`, I'm not sure if you need both of these lines

```
cimport sage.rings.integer 
from sage.rings.integer cimport Integer
```

 * line 280 in `ecl.pyx` should be `elif pyobj is None:`. Testing with `is` is much faster than a comparison.
 * Including a TODO list at the beginning could be helpful. For example you can note that optimizing conversion of gmp integers and rationals needs work. My editor highlights "TODO" so you can also just put that as a part of the comment in the `python_to_ecl()` function.
 * In `ecl.pyx`, line 653 - 664 are redundant.
 * The doctests for `car()`, `cdr()`, `caar()`, etc. are very instructive, but they are all the same. If anything goes wrong we'll get the same error from all the functions, not knowing where to look. Since this is not going to be exposed much to the users, I suggest putting the instructive example somewhere along the top of the file, and including a test only for the corresponding function in the docstring.
 * It's more pythonic to use `is_character()`, `is_null()`, `is_list()`, etc. instead of `characterp()`, `nullp()`, `listp()`, ...
 * You can replace line 996-997 of `ecl.pyx` with the following:

```
cdef EclObject obj = <EclObject>PY_NEW(EclObject)
```

 This will avoid the python class initialization overhead and make things slightly faster.


Thanks a lot for your work.


---

Comment by nbruin created at 2010-02-08 07:43:52

Thanks for your feedback! It'll be nice to get this in.

>  * The module name you declare on line 431 of `module_list.py` should be sage.libs.ecl.ecl.

Are you sure? the current thing seems to work too and I like not typing the extra ecl.

>  * We would normally put the declarations imported from a header file in a `decl.pxd` in `sage/libs/ecl/`. I suggest renaming the current `ecl.pxd` to `decl.pxd`, and using `from sage.libs.ecl.decl cimport ...` in `ecl.pyx` to import the declarations you need. Then `ecl.pxd` can be used to declare the Cython methods/classes from `ecl.pyx` which should be available for imports from other modules.

Sure. However, I just picked and chose from the ecl headers, and I orthogonalized some of the names. Wouldn't moving those to decl.pxd raise the false impression that the declarations there are a literal translation of ecl.h ?

>  * In `ecl.pyx`, I'm not sure if you need both of these lines
> {{{
> cimport sage.rings.integer 
> from sage.rings.integer cimport Integer
> }}}

I guess we can try without, but I think I put it in because it didn't work without.

>  * line 280 in `ecl.pyx` should be `elif pyobj is None:`. Testing with `is` is much faster than a comparison.

Good one!
>  * Including a TODO list at the beginning could be helpful. For example you can note that optimizing conversion of gmp integers and rationals needs work. My editor highlights "TODO" so you can also just put that as a part of the comment in the `python_to_ecl()` function.

You have a good editor. Mine doesn't do that.

>  * In `ecl.pyx`, line 653 - 664 are redundant.

But they don't hurt performance either do they? I like them for documentation purposes, so that I know the codes that go into a rich_cmp

>  * The doctests for `car()`, `cdr()`, `caar()`, etc. are very instructive, but they are all the same. If anything goes wrong we'll get the same error from all the functions, not knowing where to look. Since this is not going to be exposed much to the users, I suggest putting the instructive example somewhere along the top of the file, and including a test only for the corresponding function in the docstring.

Do you think any time spent on tuning those tests is well-spent? They're really just there because they need some test. If they fail, nothing in ecl will work.

>  * It's more pythonic to use `is_character()`, `is_null()`, `is_list()`, etc. instead of `characterp()`, `nullp()`, `listp()`, ...

but characters not being strings is not very pythonic either. We're interfacing with a different language, so I think it makes sense to depart from python's naming conventions. Also, CL routines are standard and well-documented. If we use those names, we get a well-defined interface without thinking. If we start changing function names for wrappers, we need to start thinking and may screw up.

>  * You can replace line 996-997 of `ecl.pyx` with the following:
> {{{
> cdef EclObject obj = <EclObject>PY_NEW(EclObject)
> }}}

Great!

I'll see if I can update the patch once you've had some run time with it and commented on its functionality.


---

Comment by drkirkby created at 2010-02-22 00:03:31

Has this been checked on Solaris? There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by drkirkby created at 2010-02-22 00:03:31

Changing status from needs_review to needs_info.


---

Comment by burcin created at 2010-02-25 13:03:27

Replying to [comment:20 nbruin]:
> Thanks for your feedback! It'll be nice to get this in.

I'm sorry I took so long to respond. At least I managed to test your patch(es, with #7377) in the meanwhile. 

I'm generally happy with how they look / work and I'd like to get them merged as soon as possible (I know I'm the main cause of delays). Feel free to change this ticket to positive review once the minor issues below are resolved.

> >  * The module name you declare on line 431 of `module_list.py` should be sage.libs.ecl.ecl.
> 
> Are you sure? the current thing seems to work too and I like not typing the extra ecl.

The convention is to make the module name correspond to the file name. If you think a single file will be enough, then you can just remove the directory `ecl` and put the `ecl.p*` files under `sage/libs/` directly. I'm afraid I have to insist on one of these options.

> >  * We would normally put the declarations imported from a header file in a `decl.pxd` in `sage/libs/ecl/`. I suggest renaming the current `ecl.pxd` to `decl.pxd`, and using `from sage.libs.ecl.decl cimport ...` in `ecl.pyx` to import the declarations you need. Then `ecl.pxd` can be used to declare the Cython methods/classes from `ecl.pyx` which should be available for imports from other modules.
> 
> Sure. However, I just picked and chose from the ecl headers, and I orthogonalized some of the names. Wouldn't moving those to decl.pxd raise the false impression that the declarations there are a literal translation of ecl.h ?

It's common to change the types or the function names a little. This is a minor issue though, I just think the code will be easier to maintain that way. 

> >  * In `ecl.pyx`, I'm not sure if you need both of these lines
> > {{{
> > cimport sage.rings.integer 
> > from sage.rings.integer cimport Integer
> > }}}
> 
> I guess we can try without, but I think I put it in because it didn't work without.

OK.

> >  * line 280 in `ecl.pyx` should be `elif pyobj is None:`. Testing with `is` is much faster than a comparison.
> 
> Good one!
> >  * Including a TODO list at the beginning could be helpful. For example you can note that optimizing conversion of gmp integers and rationals needs work. My editor highlights "TODO" so you can also just put that as a part of the comment in the `python_to_ecl()` function.
> 
> You have a good editor. Mine doesn't do that.

I just use `vim`. :)
> 
> >  * In `ecl.pyx`, line 653 - 664 are redundant.
> 
> But they don't hurt performance either do they? I like them for documentation purposes, so that I know the codes that go into a rich_cmp

Why don't you just put them in comments? Looking at the code, especially if you're scrolling up, it's not immediately clear that those lines are never used. If they are only for information, they should be comments.

> >  * The doctests for `car()`, `cdr()`, `caar()`, etc. are very instructive, but they are all the same. If anything goes wrong we'll get the same error from all the functions, not knowing where to look. Since this is not going to be exposed much to the users, I suggest putting the instructive example somewhere along the top of the file, and including a test only for the corresponding function in the docstring.
> 
> Do you think any time spent on tuning those tests is well-spent? They're really just there because they need some test. If they fail, nothing in ecl will work.

OK.

> >  * It's more pythonic to use `is_character()`, `is_null()`, `is_list()`, etc. instead of `characterp()`, `nullp()`, `listp()`, ...
> 
> but characters not being strings is not very pythonic either. We're interfacing with a different language, so I think it makes sense to depart from python's naming conventions. Also, CL routines are standard and well-documented. If we use those names, we get a well-defined interface without thinking. If we start changing function names for wrappers, we need to start thinking and may screw up.

OK.
 
> >  * You can replace line 996-997 of `ecl.pyx` with the following:
> > {{{
> > cdef EclObject obj = <EclObject>PY_NEW(EclObject)
> > }}}
> 
> Great!

I see that you used `EclObject.__new__()` in your last patch attached to #7377. How does that compare with using `PY_NEW()` in terms of performance?

AFAICT, some of the changes I suggest above are available in the last patch attached to #7377. Can you submit a patch with only that changes above to this ticket? Then we can get this ticket merged without waiting to solve the problems with the other one. If you don't have time, I can also make a patch with these changes (hopefully in reasonable time).

Many thanks for this interface again!

BTW, I don't see why this needs to be tested on Solaris. (In any case, expecting every developer to test their patches on solaris is unreasonable, IMHO.)


---

Comment by burcin created at 2010-02-25 13:03:27

Changing status from needs_info to needs_work.


---

Comment by drkirkby created at 2010-02-25 13:37:25

Replying to [comment:22 burcin]:
Many thanks for this interface again!
> 
> BTW, I don't see why this needs to be tested on Solaris. (In any case, expecting every developer to test their patches on solaris is unreasonable, IMHO.)

That might be your opinion, but I suggest you take that up with William. 

Quoting from the Sage developer's guide. 

http://www.sagemath.org/doc/developer/inclusion.html

_Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden._

From the Sage installation guide 

http://www.sagemath.org/doc/installation/source.html

_We do plan to fully support Solaris - it’s a very important platform. Work is ongoing._

William has taken hardware (specifically 't2') from Sun for Sage development, as well as an OpenSolaris machine from elsewhere. He also sent me an email on the 16th December 2009, underlying the importance of getting Sage working on Solaris


```
David,

(1) I couldn't get anywhere building Sage on x86 Solaris on skynet (fulvia).  Can you?  This was pretty annoying to the people that bought us fulvia.

(2) Sun wants to know if we have a Sage available yet for t2.  See below.

I really need to shift into the mode of actually providing something that *works* on Solaris, despite hickups, rather than just polishing foundations...
```


As such, I do not believe it is unreasonable that the packages are tested on Solaris. If Solaris is important, and the current version of this package works on Solaris, a failure to work on Solaris would be a reason for the changes not to be incorporated. 

Dave


---

Comment by drkirkby created at 2010-02-25 13:50:58

I realise the library access is not currently in Sage (I was confusing it with another ticket) but the rest of the comments apply. Given Solaris is considered *very important platform* things need to work there.


---

Comment by burcin created at 2010-02-25 13:57:45

Replying to [comment:23 drkirkby]:
> Replying to [comment:22 burcin]:
> > 
> > BTW, I don't see why this needs to be tested on Solaris. (In any case, expecting every developer to test their patches on solaris is unreasonable, IMHO.)
> 
> That might be your opinion, but I suggest you take that up with William. 
> 
> Quoting from the Sage developer's guide. 
> 
> http://www.sagemath.org/doc/developer/inclusion.html
> 
> _Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden._
<snip>

This ticket is not talking about including a new package in Sage.


> As such, I do not believe it is unreasonable that the packages are tested on Solaris. If Solaris is important, and the current version of this package works on Solaris, a failure to work on Solaris would be a reason for the changes not to be incorporated. 

Again, there is no new package associated to this ticket. It just contains a single patch to be applied to the Sage library. The package was merged with #7287.

I maintain my position that requiring every single patch submitted to Sage be tested on Solaris is unreasonable (unless this process is automated somehow).


---

Comment by drkirkby created at 2010-02-25 14:40:15

I find it hard to believe it could be much simpler to test a package on Solaris using the instructions at 

http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

which require the user to 

 * Add 3 lines to the bottom of their $HOME/.profile 
 * Extract the file http://boxen.math.washington.edu/sage/solaris/sage-4.3.0.1.tar
 * incorporate their changes. 
 * Log into 't2'
 * Type 'make' 

Is that hard or unreasonable, given the notes in the developers guide, installation guide and the contents of the email I just posted from William? 

Looking at the patches, I doubt this will have any Solaris specific issues, but it would be appreciated very much if someone could check it. The patches are quite old, so there should be no issues with the fact the current version for Solaris is a month or two old. 

I believe the issues which caused the library to fail to build recently have probably been resolved, so soon the latest version of Sage should build OK. 

Micheal was paid full-time to work on the Solaris port, though I realise he did do other things too. I know for a fact he was actually appointed to do the Solaris port. He has been the only full-time paid employee for the Sage project. 

Given the hardware costs and Micheal's salary, it is probably not unreasonable to estimate around $100,000 has been spent on the Solaris port. 

Dave


---

Comment by burcin created at 2010-04-02 23:34:41

apply after `ecllib.patch`


---

Comment by burcin created at 2010-04-02 23:38:17

Changing keywords from "" to "ecl, library".


---

Comment by burcin created at 2010-04-02 23:38:17

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-04-02 23:38:17

Changing component from packages to interfaces.


---

Attachment

attachment:trac_6781-review.patch contains some minor changes also mentioned in comment:22. I give a positive review to attachment:ecllib.patch, if someone can review my changes this will be good to go.

The patches to be applied are:
 * attachment:ecllib.patch
 * attachment:trac_6781-review.patch


---

Comment by nbruin created at 2010-04-12 00:33:45

That all looks great. However, I think the PY_NEW call should really be

```
cdef EclObject obj = EclObject.__new__(EclObject)
```

According to
http://wiki.cython.org/FAQ#CanCythoncreateobjectsorapplyoperatorstolocallycreatedobjectsaspureCcode.3F
it seems that PY_NEW was a hack that was only required prior to Cython 0.12

A lot of the includes are not necessary either for the code to seemingly work properly. Wouldn't it be better to leave them out?

I am probably not allowed to give the patch a positive review, but I can confirm that the original reviewer requested those changes to be made and they look fine to me (the author of the original enhancement).

Thanks for trying to unstall the inclusion of this patch!


---

Attachment

Replying to [comment:28 nbruin]:
> That all looks great. However, I think the PY_NEW call should really be
 {{{
 cdef EclObject obj = EclObject.__new__(EclObject)
 }}}
> According to
> http://wiki.cython.org/FAQ#CanCythoncreateobjectsorapplyoperatorstolocallycreatedobjectsaspureCcode.3F
> it seems that PY_NEW was a hack that was only required prior to Cython 0.12

Thanks for pointing this out. I didn't know the new convention.

> A lot of the includes are not necessary either for the code to seemingly work properly. Wouldn't it be better to leave them out?

The includes weren't necessary at all after getting rid of the `PY_NEW` call. 

I uploaded a new patch attachment:trac_6781-review.take2.patch addressing these comments. The new patch replaces attachment:trac_6781-review.patch.

> I am probably not allowed to give the patch a positive review, but I can confirm that the original reviewer requested those changes to be made and they look fine to me (the author of the original enhancement).

You can change the ticket to positive review. I reviewed your patch and gave a positive review, if you're ok with my additional changes and think that they deserve a positive review, then the whole ticket is good to go. 

> Thanks for trying to unstall the inclusion of this patch!

I want to get the rest of the interface (#7377) merged ASAP as well. Unfortunately we had a setback with #8645. I hope the latter gets resolved soon so we can proceed.


Based on Nils' comments above, I am changing this to a positive review.

The patches to be applied are:
 * attachment:ecllib.patch
 * attachment:trac_6781-review.take2.patch


---

Comment by burcin created at 2010-04-12 08:55:12

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-04-12 12:56:41

Awesome! I'm very sorry I haven't been able to work on this (or Sage) at all the last several months. Great work, and thanks.


---

Comment by burcin created at 2010-04-12 22:58:14

The author credit for this ticket belongs entirely to Nils. I just made minor changes as a reviewer.


---

Comment by jhpalmieri created at 2010-04-15 20:05:44

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 20:05:44

Merged in 4.4.alpha0:

 - ecllib.patch
 - trac_6781-review.take2.patch


---

Comment by jhpalmieri created at 2010-04-16 02:47:51

Changing status from closed to needs_work.


---

Comment by jhpalmieri created at 2010-04-16 02:47:51

If I understand this correctly, it requires ecl to be built before Sage.  Is that right?  If so, the file SAGE_ROOT/spkg/standard/deps needs to be changed.  Please review my changes.


---

Comment by jhpalmieri created at 2010-04-16 02:49:27

new version of SAGE_ROOT/spkg/standard/deps


---

Attachment

diff for the file "deps"


---

Comment by jhpalmieri created at 2010-04-16 02:51:08

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-04-16 02:51:22

Resolution changed from fixed to 


---

Comment by jhpalmieri created at 2010-04-16 02:51:22

Changing status from closed to new.


---

Comment by jhpalmieri created at 2010-04-16 02:51:29

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-16 02:51:52

(Okay, I think this has the right label now.)


---

Comment by burcin created at 2010-04-16 10:38:23

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-04-16 10:38:23

It didn't occur to me that we need to update the dependencies, sorry for the trouble.

I'm not sure what it takes to review the `deps` file. The proposed change definitely makes sense, but I don't think I can test it easily. I'm giving a positive review nevertheless.


---

Comment by jhpalmieri created at 2010-04-16 17:15:19

Merged new version of "deps" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 17:15:19

Resolution: fixed
