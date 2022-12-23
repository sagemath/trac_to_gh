# Issue 3317: a citation system for Sage components

Issue created by migration from https://trac.sagemath.org/ticket/3317

Original creator: mhampton

Original creation time: 2008-05-28 00:20:03

Assignee: mhampton

CC:  burcin novoselt ranosch polybori jakobkroeker

Keywords: citations

Sage could use some sort of citation system that identifies what components/packages are used in a given computation or worksheet.  After some discussion, it is unclear what the architecture of that should be.


---

Comment by mhampton created at 2008-05-28 00:42:11

Some thoughts:

From: "Fernando Perez" <fperez....`@`gmail.com>
Date: May 27, 7:02 pm
Subject: Citing Sage and Used Systems
To: sage-devel

This is certainly not an easy problem if one wants a '100%' solution,
in the sense that tracking down every single line of code in any given
computation isn't easy.  But here's  a quick idea that can give an
'80%' solution for all in-process sage/python/extension code (it won't
work for code done by external processes like maxima, I'm afraid). If
you run in the ipython console a program via '%run -p' it will be
executed under the control of the profiler, and the result will tell
you what functions were called, how many times, etc.  Similarly %prun
lets you execute single statements with profiler control.  The
profiler results object can be returned and analyzed further, if I
recall correctly there is some information in there about where
functions come from.


---

Comment by jhpalmieri created at 2011-03-22 18:36:27

Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?


---

Comment by burcin created at 2011-03-22 18:58:52

Replying to [comment:3 jhpalmieri]:
> Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?

This basically does what is described in comment:1. We need to do much better than that.

We are working on a system which allows developers to annotate (decorate?) functions with citation information. The decorated functions will add the citation entries to a central database at runtime. This database can be queried to get the list of packages/papers/algorithms used in various formats.

In short, I don't think we can close this yet.


---

Comment by ranosch created at 2011-08-12 13:24:56

Burcin Erocal, Michael Brickenstein and I (Niels Ranosch) have been working on a new citation system for about a month now: https://bitbucket.org/niels_mfo/sage-citation

The patches will be attached. What do you think about it?

You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg

Cheers.


---

Comment by kcrisman created at 2011-08-12 14:39:38

Hi!  If this doesn't slow things down, it is a really good idea, especially given that Sage is not trying to cover up the other programs inside of it.   I assume that (given the comments on the blog) you will post timing information in critical areas eventually.

I have one substantive comment, I think:
> You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg
Hmm, so does that mean we would need to make `pybtex` a standard package in order for this to work?  (Currently there is a probationary period needed, which we have recently [been enforcing](http://trac.sagemath.org/sage_trac/ticket/11563).)  

Or are you suggesting this would be an optional spkg (for now), which means your examples would have to be optional for now?

Here follow a couple silly comments that don't actually review much, but might still be worthwhile to ponder.
 * Missing "to": `in order make it faster` 
 * A _lot_ of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.
 * What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.

Good luck!


---

Comment by jhpalmieri created at 2011-08-12 15:47:43

Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?


---

Comment by ranosch created at 2011-08-15 06:56:59

Replying to [comment:8 kcrisman]:
> Hi!  If this doesn't slow things down, it is a really good idea, especially given that Sage is not trying to cover up the other programs inside of it.   I assume that (given the comments on the blog) you will post timing information in critical areas eventually.

At least that's what I plan to do. I'm not quite sure on how to benchmark (and what), but I'm open for suggestions. Benchmarking the decorated pass-function is unsatisfying.


> I have one substantive comment, I think:
> > You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg
> Hmm, so does that mean we would need to make `pybtex` a standard package in order for this to work?  (Currently there is a probationary period needed, which we have recently [been enforcing](http://trac.sagemath.org/sage_trac/ticket/11563).)  

Well, I put the design, as if pybtex was a standard-spkg. But it might as well be a good idea to make it optional: If people really pybtex' features, they can install it. It could be the following: If pybtex is not installed, the printed citations will just be the exact content of the bibfile, otherwise parsed (and maybe converted).
But there might be disadvantages: If the bibtex is parsed by pybtex, syntax-errors and illegal formatting might be found by pybtex. The output would probably be more consistent (more homogeneous and more compliant to design).

I am in favour of pre-parsing everything through pybtex, but I don't know, what is actually better.


> Or are you suggesting this would be an optional spkg (for now), which means your examples would have to be optional for now?
> 
> Here follow a couple silly comments that don't actually review much, but might still be worthwhile to ponder.
>  * Missing "to": `in order make it faster` 

Thanks.


>  * A _lot_ of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.

You are right. It is more a coincidence than anything else; still, it has to be changed.


>  * What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.

I won't :-).
For this citation system, it is indispensable, that the decorator gets widespread into sage. In my opinion, it is best if people decorate their own functions (and possibly make their own bibtex-entries). The example shows, how a function should be decorated.
(The deprecation-message can be uncommented later, as soon as the "new" citation system is more accurate than the old one.)


---

Comment by ranosch created at 2011-08-15 07:07:46

Replying to [comment:9 jhpalmieri]:
> Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?

Ehm .. I think so, but don't know. Still, I'm quite a newbie.


---

Comment by ranosch created at 2011-08-16 15:15:18

Corrected some of the errors and included my benchmark results for the decorated pass-function (in `citation/__init__.py`'s `_benchmark_`-function).

Another problem came to my mind: If a user tries to make an instance of one of the citables, strange things will happen. But I'm not sure, if we should really care about that.

Is the documentation alright?


Cheers.


---

Comment by ranosch created at 2011-08-26 11:56:22

Changing status from new to needs_review.


---

Comment by ranosch created at 2011-08-26 11:56:22

The benchmarking results are available on [http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html](http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html) and [https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/](https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/).

I still think, it would be best, if pybtex would become a standard package.

Is there any work needed for the reference manual (referring to jhpalmieri's comment)?


---

Comment by ranosch created at 2011-09-26 11:17:57

Changing keywords from "citations" to "citations, sd34".


---

Comment by ranosch created at 2011-09-27 16:43:41

bibtex-data of some components


---

Attachment


---

Attachment

Uploaded an updated version (with the sage citation included) and accidently added `trac-3317-example-usage.2.patch` ... please ignore this file.


---

Comment by mhansen created at 2011-12-17 20:17:48

I'm not convinced that it is the best idea to have it so that anytime a function is called we have to log that its citation, even in the case where we don't care about that data.


---

Comment by itaibn created at 2012-05-01 11:48:21

Changing status from needs_review to needs_work.


---

Comment by itaibn created at 2012-05-01 11:48:21

This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.


---

Comment by AlexanderDreyer created at 2012-05-02 07:29:40

Replying to [comment:20 itaibn]:
> This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.
The dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. 

But you also set the ticket to `needs_work`. The authors might be interested what you require them to change. (You say that Sage won't start, but this is true for all integration patches when you forget to install the spkg in question.)


---

Comment by AlexanderDreyer created at 2012-05-02 07:37:05

Replying to [comment:21 AlexanderDreyer]:
> The dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. 
Correction myself: of course it is not the *only* intention of the ticket, but an *important one*.


---

Comment by itaibn created at 2012-05-02 22:33:59

Changing status from needs_work to needs_review.


---

Comment by itaibn created at 2012-05-02 22:33:59

I'm sorry, I didn't read the ticket description carefully enough. I have modified the ticket to redact my earlier modifications.


---

Comment by ranosch created at 2012-05-22 09:43:47

Sorry for not having responded.

Replying to [comment:18 mhansen]:
> I'm not convinced that it is the best idea to have it so that anytime a function is called we have to log that its citation, even in the case where we don't care about that data.

What exactly are your concerns? Speed? Integrity?

In my opinion it would be very nice to have tracked the used components, no matter if we care for this data. And it's not meant to log every function call. Only rather important functions should be decorated (could say "cite-worthy", but that's a vague term). Maybe there should be rules on what makes some worth citing in Sage.

----

Replying to [comment:20 itaibn]:

Well thanks for pointing out, that it might be unclear that you need the spkg. I thought it will be enough if the dependency is mentioned as the dependency of the corresponding ticket, but I'm willing to change the description if that's not clear enough.

I'm currently updating the spkg to a newer version, should I directly include the link to it when done?

----

Replying to [comment:22 AlexanderDreyer]:

The intention of this ticket (as far as I see it) is to track sage's components and their citations. Pybtex is our tool of choice. Therefore, yes, it is important.


---

Attachment

New citation system


---

Comment by ranosch created at 2012-05-28 16:00:02

Fixed bugs and doctests.


---

Comment by ranosch created at 2012-05-28 22:43:27

environment changes for the citation system


---

Attachment

New citation system


---

Comment by ranosch created at 2012-05-28 22:44:19

bibtex-data of some components


---

Attachment

Example usage in multipolynomial-libsingular


---

Comment by zimmerma created at 2014-08-25 15:12:34

would it be possible to add in the description some concrete example demonstrating what functionality this ticket adds to Sage?

Paul


---

Comment by burcin created at 2014-08-27 11:58:32

Changing type from task to enhancement.


---

Comment by jdemeyer created at 2014-11-13 14:03:28

Changing component from packages: standard to misc.


---

Comment by saraedum created at 2016-04-21 17:04:30

Changing status from needs_review to needs_work.


---

Comment by saraedum created at 2016-04-21 17:04:30

The patches do not apply anymore (not too surprising after so many years.)


---

Comment by saraedum created at 2016-04-21 17:06:10

To be honest I like the approach used by `citation.pyx` better because it does not add any performance overhead unless you care. Then again, the output generated by the patches here is really nice…
