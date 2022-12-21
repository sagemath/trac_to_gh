# Issue 5996: Wigner 3j, 6j, 9j, Clebsch-Gordan, Racah and Gaunt coefficients

Issue created by migration from Trac.

Original creator: jrasch

Original creation time: 2009-05-06 13:27:07

Assignee: burcin

CC:  certik jdc

Python file for calculating Wigner 3j, 6j, 9j, Clebsch-Gordan, Racah and Gaunt coefficients (integrals over 3 spherical
harmonics) exactly. 

Has already received some positive review at 
http://groups.google.com/group/sage-devel/browse_thread/thread/ca312a02de54553e



---

Comment by mabshoff created at 2009-05-06 21:28:49

Someone needs to turn this into a proper patch.

Cheers,

Michael


---

Attachment

The wigner.py file has just been updated so that it passes all tests in sage-4.0 since the new symbolic manipulations return slightly different resutls.

Could someone turn this into a patch and review this please?


---

Comment by AlexGhitza created at 2009-06-01 10:57:53

I am attaching a patch (against 4.0).  I had to make some trivial changes to the original code to get this to play nicely within Sage.  A couple of issues remain: (a) doctest coverage is not at 100% since two helper functions are not doctested, (b) the docs need to be rest-ified, and (c) the docs should be added to the reference manual.

So I'm leaving this as "needs work".


---

Attachment


---

Comment by jrasch created at 2009-06-01 22:31:07

Thanks for converting this into a patch.

Concerning (a): doctest coverage is infact 100%. The functions test_calc_factlist() and test_bigDeltacoeff() are the doctest functions for _calc_factlist() and _bigDeltacoeff(), respectively. Unfortunately, putting the doctests into the original functions causes a exception.
If this can be fixed (maybe removing the underscores, but they are supposed to be private), then the doctests can be merged and the test functions deleted.

Concerning (b), (c), I would be happy to help, but I do not know sage well enough. Any help appreciated.


---

Attachment


---

Comment by jrasch created at 2009-06-14 11:18:14

All functions now have doc tests, redundant functions
test_calc_factlist() and test_bigDeltacoeff() have been removed.


---

Comment by ncalexan created at 2009-06-14 22:32:16

I want to merge this but the docstrings are not ReST-ified.  Can we get a docstring update and a positive review, Alex?


---

Comment by jrasch created at 2009-06-20 15:45:36

Added path to remove all Latex formulas and replace them with text formulas in accordance with the ReST system.


---

Attachment

OK, I finally managed to get around to looking at this.  There were still some ReST issues, which I fixed in the latest patch `trac_5996_doc.patch`.  I also added the documentation to the reference manual.

If someone can double-check my patch, we're good to go.

The patches need to be applied in the order they appear on the ticket.


---

Comment by mvngu created at 2009-07-11 13:53:32

I'm reviewing the coding style and docstring formatting. Here are some problems I notice with the coding style:
 1. It doesn't follow many of the coding conventions in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html). In particular, don't use camel case for function name. The following functions are currently in camel case: `Wigner3j`, `ClebschGordan`, `_bigDeltacoeff`, `Racah`, `Wigner6j`, `Wigner9j`, `Gaunt`.
 1. The Python code is mostly squashed together and makes little use of white space. For example, instead of writing a function signature like this:

```
def _bigDeltacoeff(aa,bb,cc,prec=None):
```

 it should be written as follows:

```
def _big_delta_coeff(aa, bb, cc, prec=None):
```

 which makes use of white space so it doesn't look like code is squashed together. Another example, don't do this

```
if(int(aa+bb-cc)!=(aa+bb-cc)):
```

 Instead, write it like this:

```
if int(aa + bb - cc) != (aa + bb - cc):
```

 This means that the whole module needs to be reformatted to make use of white space.
 1. The docstring of some functions don't follow the guidelines [here](http://www.sagemath.org/doc/developer/conventions.html#docstring-content). In particular, the docstring should be organized with the following two items first:
  1. A one-sentence description of the function, followed by a blank line.
  1. An INPUT and an OUTPUT block for input and output arguments (see below for format). The type names should be descriptive, but do not have to represent the exact Sage/Python types. For example, use “integer” for anything that behaves like an integer; you do not have to put a precise type name such as int.

If no one beats me to it, I'll upload a patch to address the issues I raised above.


---

Comment by jrasch created at 2009-07-12 14:37:59

Could I just suggest that we merge this into Sage as is, since IMHO it is a piece of functionality that should be of interest to a number of computational physicist and chemists.

Just to be clear: I have no problem with anyone improving the code. I personally would like to unmerge my ticket that hacked out the latex formatting as soon as the notebook functionality can deal better with latex formatted doc strings. It might also be of interest to reimplement the algorithms in Cython (although I am unsure about the speed up one would get). However, all this could be done in later tickets.


---

Comment by mvngu created at 2009-07-12 14:44:52

Replying to [comment:11 jrasch]:
> Could I just suggest that we merge this into Sage as is, since IMHO it is a piece of functionality that should be of interest to a number of computational physicist and chemists.


Yes, it would be good to have this merged in Sage 4.1.1. But as they now stand, the patches do not conform to a number of coding conventions in addition to conventions regarding docstring formatting.


---

Comment by burcin created at 2009-07-12 15:07:36

Jens, thank you for your contribution, but we cannot import the functions with their current camel case names to the top level Sage namespace. Once we do that, for backward compatibility we'd have to provide the functions with those names and deprecation notices for at least 6 months. The effort to fix the names now is much less than the effort that will go into maintaining this afterwards. Thus I agree with Minh, this ticket still needs work.

I didn't check all the issues raised by Minh, since there are quite a few patches, but I hope someone will put in the work to improve the patches so they can be included in 4.1.1. Since Minh volunteered in comment:10, I don't think this will be a problem.


---

Attachment

OK, I think I fixed all the issues that Minh pointed out, and replaced my latest patch.

In reply to Jens' comment about latex: I have fixed things so that the docstrings do have the nice latex expressions in them, which means that the pdf and html versions of the reference manual will have nicely typeset formulae.


---

Comment by mvngu created at 2009-07-13 12:48:52

Replying to [comment:14 AlexGhitza]:
> OK, I think I fixed all the issues that Minh pointed out, and replaced my latest patch.
I appreciate that you've taken the time to make the code and docstring conform to the coding styles. It's a tedious task that causes short-term pain. But the long-term benefit is that at least the Sage library is standardized on a coding convention. Your new patch should make the reviewing process easier for me.



> In reply to Jens' comment about latex: I have fixed things so that the docstrings do have the nice latex expressions in them, which means that the pdf and html versions of the reference manual will have nicely typeset formulae.
Note that with Sage 4.1, the HTML version of the reference manual is a bit broken. The HTML version of the reference does build successfully. However, if the docstring for a function or class uses the ".. MATH::" tag, then it won't render in the generated HTML version. That is, when you use a web browser to view the corresponding HTML page that documents the function, anything typeset within the ".. MATH::" tag won't show up. You can get a quick glimpse of the rendered math expression, but you have to refresh the page every second. And the math expression would only be displayed for a fraction of a second. This issue was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cb1687577bf5843e/b453af3a0750ba23) thread and the corresponding ticket is #6512.


---

Attachment

reviewer patch


---

Comment by mvngu created at 2009-07-15 20:32:54

I've made some minor reformatting of the docstrings and fixed references so that there is only one reference defined for a paper cited in the module. That way, we don't get a lot of warnings about duplicate citations when building the reference manual. That is, only define one reference. Afterwards, if you need to cite that reference, use the convention for citing it and don't define the same reference locally for a function. Some functions use `<>` when it should be `!=`. At least in Python 2.6.x, using `<>` is OK and is kept in that version for backward compatibility. We should now only use `!=`. These issues, and some minor ones, are addressed in the reviewer patch `trac_5996-reviewer.patch`. Positive review to the ticket as a whole. Patches should be merged in this order:

 1. `trac_5996.patch`
 1. `12428.patch`
 1. `12429.patch`
 1. `trac_5996_doc.patch`
 1. `trac_5996-reviewer.patch`


---

Comment by mvngu created at 2009-07-16 15:24:29

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by jrasch created at 2009-07-16 21:12:15

Changing assignee from burcin to jrasch.


---

Comment by jrasch created at 2009-07-16 21:12:15

Changing status from new to assigned.


---

Comment by jrasch created at 2009-07-16 21:12:15

Just wanted to say thanks for your help and work.


---

Comment by mvngu created at 2009-07-16 21:20:00

Resolution: fixed


---

Comment by kcrisman created at 2013-06-12 15:52:40

Just as a followup, note that 

```
sage: gaunt(1,1,1,0,1,-1)
0
sage: gaunt(int(1),int(1),int(1),int(0),int(1),int(-1))
1/2*sqrt(3)/sqrt(pi)
```

This was noted at [this ask.sagemath question](http://ask.sagemath.org/question/2683/different-answers-with-gaunt).  I've opened #14735 for this.
