# Issue 3317: a citation system for Sage components

archive/issues_003317.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @burcin @novoselt ranosch polybori jakobkroeker\n\nKeywords: citations\n\nSage could use some sort of citation system that identifies what components/packages are used in a given computation or worksheet.  After some discussion, it is unclear what the architecture of that should be.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3317\n\n",
    "created_at": "2008-05-28T00:20:03Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "a citation system for Sage components",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3317",
    "user": "mhampton"
}
```
Assignee: mhampton

CC:  @burcin @novoselt ranosch polybori jakobkroeker

Keywords: citations

Sage could use some sort of citation system that identifies what components/packages are used in a given computation or worksheet.  After some discussion, it is unclear what the architecture of that should be.

Issue created by migration from https://trac.sagemath.org/ticket/3317





---

archive/issue_comments_022974.json:
```json
{
    "body": "Some thoughts:\n\nFrom: \"Fernando Perez\" <fperez....`@`gmail.com>\nDate: May 27, 7:02 pm\nSubject: Citing Sage and Used Systems\nTo: sage-devel\n\nThis is certainly not an easy problem if one wants a '100%' solution,\nin the sense that tracking down every single line of code in any given\ncomputation isn't easy.  But here's  a quick idea that can give an\n'80%' solution for all in-process sage/python/extension code (it won't\nwork for code done by external processes like maxima, I'm afraid). If\nyou run in the ipython console a program via '%run -p' it will be\nexecuted under the control of the profiler, and the result will tell\nyou what functions were called, how many times, etc.  Similarly %prun\nlets you execute single statements with profiler control.  The\nprofiler results object can be returned and analyzed further, if I\nrecall correctly there is some information in there about where\nfunctions come from.",
    "created_at": "2008-05-28T00:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22974",
    "user": "mhampton"
}
```

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

archive/issue_comments_022975.json:
```json
{
    "body": "Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?",
    "created_at": "2011-03-22T18:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22975",
    "user": "@jhpalmieri"
}
```

Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?



---

archive/issue_comments_022976.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?\n\nThis basically does what is described in comment:1. We need to do much better than that.\n\nWe are working on a system which allows developers to annotate (decorate?) functions with citation information. The decorated functions will add the citation entries to a central database at runtime. This database can be queried to get the list of packages/papers/algorithms used in various formats.\n\nIn short, I don't think we can close this yet.",
    "created_at": "2011-03-22T18:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22976",
    "user": "@burcin"
}
```

Replying to [comment:3 jhpalmieri]:
> Right now we have the code in sage/misc/citation.pyx.  Is that good enough so that this ticket should be closed?

This basically does what is described in comment:1. We need to do much better than that.

We are working on a system which allows developers to annotate (decorate?) functions with citation information. The decorated functions will add the citation entries to a central database at runtime. This database can be queried to get the list of packages/papers/algorithms used in various formats.

In short, I don't think we can close this yet.



---

archive/issue_comments_022977.json:
```json
{
    "body": "Burcin Erocal, Michael Brickenstein and I (Niels Ranosch) have been working on a new citation system for about a month now: https://bitbucket.org/niels_mfo/sage-citation\n\nThe patches will be attached. What do you think about it?\n\nYou'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg\n\nCheers.",
    "created_at": "2011-08-12T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22977",
    "user": "ranosch"
}
```

Burcin Erocal, Michael Brickenstein and I (Niels Ranosch) have been working on a new citation system for about a month now: https://bitbucket.org/niels_mfo/sage-citation

The patches will be attached. What do you think about it?

You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg

Cheers.



---

archive/issue_comments_022978.json:
```json
{
    "body": "Hi!  If this doesn't slow things down, it is a really good idea, especially given that Sage is not trying to cover up the other programs inside of it.   I assume that (given the comments on the blog) you will post timing information in critical areas eventually.\n\nI have one substantive comment, I think:\n> You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg\nHmm, so does that mean we would need to make `pybtex` a standard package in order for this to work?  (Currently there is a probationary period needed, which we have recently [been enforcing](http://trac.sagemath.org/sage_trac/ticket/11563).)  \n\nOr are you suggesting this would be an optional spkg (for now), which means your examples would have to be optional for now?\n\nHere follow a couple silly comments that don't actually review much, but might still be worthwhile to ponder.\n* Missing \"to\": `in order make it faster` \n* A *lot* of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.\n* What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.\n\nGood luck!",
    "created_at": "2011-08-12T14:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22978",
    "user": "@kcrisman"
}
```

Hi!  If this doesn't slow things down, it is a really good idea, especially given that Sage is not trying to cover up the other programs inside of it.   I assume that (given the comments on the blog) you will post timing information in critical areas eventually.

I have one substantive comment, I think:
> You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg
Hmm, so does that mean we would need to make `pybtex` a standard package in order for this to work?  (Currently there is a probationary period needed, which we have recently [been enforcing](http://trac.sagemath.org/sage_trac/ticket/11563).)  

Or are you suggesting this would be an optional spkg (for now), which means your examples would have to be optional for now?

Here follow a couple silly comments that don't actually review much, but might still be worthwhile to ponder.
* Missing "to": `in order make it faster` 
* A *lot* of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.
* What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.

Good luck!



---

archive/issue_comments_022979.json:
```json
{
    "body": "Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?",
    "created_at": "2011-08-12T15:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22979",
    "user": "@jhpalmieri"
}
```

Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?



---

archive/issue_comments_022980.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Hi!  If this doesn't slow things down, it is a really good idea, especially given that Sage is not trying to cover up the other programs inside of it.   I assume that (given the comments on the blog) you will post timing information in critical areas eventually.\n\nAt least that's what I plan to do. I'm not quite sure on how to benchmark (and what), but I'm open for suggestions. Benchmarking the decorated pass-function is unsatisfying.\n\n\n> I have one substantive comment, I think:\n> > You'll need our pybtex-spkg in order to make it work: http://sage.math.washington.edu/home/burcin/spkg/pybtex-0.15.spkg\n> Hmm, so does that mean we would need to make `pybtex` a standard package in order for this to work?  (Currently there is a probationary period needed, which we have recently [been enforcing](http://trac.sagemath.org/sage_trac/ticket/11563).)  \n\nWell, I put the design, as if pybtex was a standard-spkg. But it might as well be a good idea to make it optional: If people really pybtex' features, they can install it. It could be the following: If pybtex is not installed, the printed citations will just be the exact content of the bibfile, otherwise parsed (and maybe converted).\nBut there might be disadvantages: If the bibtex is parsed by pybtex, syntax-errors and illegal formatting might be found by pybtex. The output would probably be more consistent (more homogeneous and more compliant to design).\n\nI am in favour of pre-parsing everything through pybtex, but I don't know, what is actually better.\n\n\n> Or are you suggesting this would be an optional spkg (for now), which means your examples would have to be optional for now?\n> \n> Here follow a couple silly comments that don't actually review much, but might still be worthwhile to ponder.\n>  * Missing \"to\": `in order make it faster` \n\nThanks.\n\n\n>  * A *lot* of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.\n\nYou are right. It is more a coincidence than anything else; still, it has to be changed.\n\n\n>  * What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.\n\nI won't :-).\nFor this citation system, it is indispensable, that the decorator gets widespread into sage. In my opinion, it is best if people decorate their own functions (and possibly make their own bibtex-entries). The example shows, how a function should be decorated.\n(The deprecation-message can be uncommented later, as soon as the \"new\" citation system is more accurate than the old one.)",
    "created_at": "2011-08-15T06:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22980",
    "user": "ranosch"
}
```

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


>  * A *lot* of the examples refer to Michael Brickenstein, which seems somewhat less than advisable.  I mean no disrespect here - clearly he is contributing loads and deserves citations!  But for the first-time reader of this documentation, it would be nice to have a bigger variety of citations, perhaps even beyond Sage components to the subcomponents.  For instance, the ones in the bibtex patch.

You are right. It is more a coincidence than anything else; still, it has to be changed.


>  * What does [trac-3317-example-usage.patch] exactly have an example of?  I see the ``@`cites(citable_items.slimgb)` - is this demonstrating that we get the same thing through the new decorator as we would have from `sage.misc.citation`?  This comment is probably just my ignorance speaking, feel free to ignore it.

I won't :-).
For this citation system, it is indispensable, that the decorator gets widespread into sage. In my opinion, it is best if people decorate their own functions (and possibly make their own bibtex-entries). The example shows, how a function should be decorated.
(The deprecation-message can be uncommented later, as soon as the "new" citation system is more accurate than the old one.)



---

archive/issue_comments_022981.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?\n\nEhm .. I think so, but don't know. Still, I'm quite a newbie.",
    "created_at": "2011-08-15T07:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22981",
    "user": "ranosch"
}
```

Replying to [comment:9 jhpalmieri]:
> Should some of the new code (e.g., `citation/__init__.py`) be in the reference manual?

Ehm .. I think so, but don't know. Still, I'm quite a newbie.



---

archive/issue_comments_022982.json:
```json
{
    "body": "Corrected some of the errors and included my benchmark results for the decorated pass-function (in `citation/__init__.py`'s `_benchmark_`-function).\n\nAnother problem came to my mind: If a user tries to make an instance of one of the citables, strange things will happen. But I'm not sure, if we should really care about that.\n\nIs the documentation alright?\n\n\nCheers.",
    "created_at": "2011-08-16T15:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22982",
    "user": "ranosch"
}
```

Corrected some of the errors and included my benchmark results for the decorated pass-function (in `citation/__init__.py`'s `_benchmark_`-function).

Another problem came to my mind: If a user tries to make an instance of one of the citables, strange things will happen. But I'm not sure, if we should really care about that.

Is the documentation alright?


Cheers.



---

archive/issue_comments_022983.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-26T11:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22983",
    "user": "ranosch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_022984.json:
```json
{
    "body": "The benchmarking results are available on [http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html](http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html) and [https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/](https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/).\n\nI still think, it would be best, if pybtex would become a standard package.\n\nIs there any work needed for the reference manual (referring to jhpalmieri's comment)?",
    "created_at": "2011-08-26T11:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22984",
    "user": "ranosch"
}
```

The benchmarking results are available on [http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html](http://sage-citation.blogspot.com/2011/08/awful-benchmarks.html) and [https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/](https://bitbucket.org/niels_mfo/sage-citation/src/74ea62a5c9b3/benchmark/).

I still think, it would be best, if pybtex would become a standard package.

Is there any work needed for the reference manual (referring to jhpalmieri's comment)?



---

archive/issue_comments_022985.json:
```json
{
    "body": "Changing keywords from \"citations\" to \"citations, sd34\".",
    "created_at": "2011-09-26T11:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22985",
    "user": "ranosch"
}
```

Changing keywords from "citations" to "citations, sd34".



---

archive/issue_comments_022986.json:
```json
{
    "body": "bibtex-data of some components",
    "created_at": "2011-09-27T16:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22986",
    "user": "ranosch"
}
```

bibtex-data of some components



---

archive/issue_comments_022987.json:
```json
{
    "body": "Attachment [trac-3317-bib-data.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-bib-data.patch) by ranosch created at 2011-09-27 16:43:54",
    "created_at": "2011-09-27T16:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22987",
    "user": "ranosch"
}
```

Attachment [trac-3317-bib-data.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-bib-data.patch) by ranosch created at 2011-09-27 16:43:54



---

archive/issue_comments_022988.json:
```json
{
    "body": "Attachment [trac-3317-example-usage.2.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-example-usage.2.patch) by ranosch created at 2011-09-27 16:53:17\n\nUploaded an updated version (with the sage citation included) and accidently added `trac-3317-example-usage.2.patch` ... please ignore this file.",
    "created_at": "2011-09-27T16:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22988",
    "user": "ranosch"
}
```

Attachment [trac-3317-example-usage.2.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-example-usage.2.patch) by ranosch created at 2011-09-27 16:53:17

Uploaded an updated version (with the sage citation included) and accidently added `trac-3317-example-usage.2.patch` ... please ignore this file.



---

archive/issue_comments_022989.json:
```json
{
    "body": "I'm not convinced that it is the best idea to have it so that anytime a function is called we have to log that its citation, even in the case where we don't care about that data.",
    "created_at": "2011-12-17T20:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22989",
    "user": "@mwhansen"
}
```

I'm not convinced that it is the best idea to have it so that anytime a function is called we have to log that its citation, even in the case where we don't care about that data.



---

archive/issue_comments_022990.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-01T11:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22990",
    "user": "@itaibn"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_022991.json:
```json
{
    "body": "This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.",
    "created_at": "2012-05-01T11:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22991",
    "user": "@itaibn"
}
```

This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.



---

archive/issue_comments_022992.json:
```json
{
    "body": "Replying to [comment:20 itaibn]:\n> This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.\nThe dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. \n\nBut you also set the ticket to `needs_work`. The authors might be interested what you require them to change. (You say that Sage won't start, but this is true for all integration patches when you forget to install the spkg in question.)",
    "created_at": "2012-05-02T07:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22992",
    "user": "@alexanderdreyer"
}
```

Replying to [comment:20 itaibn]:
> This patch doesn't fail nicely when you don't have `pybtex`. I didn't know it was a dependency and so sage was unable to start. I modified the ticket to indicate the dependency.
The dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. 

But you also set the ticket to `needs_work`. The authors might be interested what you require them to change. (You say that Sage won't start, but this is true for all integration patches when you forget to install the spkg in question.)



---

archive/issue_comments_022993.json:
```json
{
    "body": "Replying to [comment:21 AlexanderDreyer]:\n> The dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. \nCorrection myself: of course it is not the **only** intention of the ticket, but an **important one**.",
    "created_at": "2012-05-02T07:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22993",
    "user": "@alexanderdreyer"
}
```

Replying to [comment:21 AlexanderDreyer]:
> The dependency had been explicitly mentioned in the ticket already. Since the only intention of this ticket is to integrate pybtex into Sage, it make sense to explicitly mention the spkg for convenience. 
Correction myself: of course it is not the **only** intention of the ticket, but an **important one**.



---

archive/issue_comments_022994.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-02T22:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22994",
    "user": "@itaibn"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022995.json:
```json
{
    "body": "I'm sorry, I didn't read the ticket description carefully enough. I have modified the ticket to redact my earlier modifications.",
    "created_at": "2012-05-02T22:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22995",
    "user": "@itaibn"
}
```

I'm sorry, I didn't read the ticket description carefully enough. I have modified the ticket to redact my earlier modifications.



---

archive/issue_comments_022996.json:
```json
{
    "body": "Sorry for not having responded.\n\nReplying to [comment:18 mhansen]:\n> I'm not convinced that it is the best idea to have it so that anytime a function is called we have to log that its citation, even in the case where we don't care about that data.\n\nWhat exactly are your concerns? Speed? Integrity?\n\nIn my opinion it would be very nice to have tracked the used components, no matter if we care for this data. And it's not meant to log every function call. Only rather important functions should be decorated (could say \"cite-worthy\", but that's a vague term). Maybe there should be rules on what makes some worth citing in Sage.\n\n----\n\nReplying to [comment:20 itaibn]:\n\nWell thanks for pointing out, that it might be unclear that you need the spkg. I thought it will be enough if the dependency is mentioned as the dependency of the corresponding ticket, but I'm willing to change the description if that's not clear enough.\n\nI'm currently updating the spkg to a newer version, should I directly include the link to it when done?\n\n----\n\nReplying to [comment:22 AlexanderDreyer]:\n\nThe intention of this ticket (as far as I see it) is to track sage's components and their citations. Pybtex is our tool of choice. Therefore, yes, it is important.",
    "created_at": "2012-05-22T09:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22996",
    "user": "ranosch"
}
```

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

archive/issue_comments_022997.json:
```json
{
    "body": "Attachment [trac-3317-citation-system-integrated.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-citation-system-integrated.patch) by ranosch created at 2012-05-28 15:55:50\n\nNew citation system",
    "created_at": "2012-05-28T15:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22997",
    "user": "ranosch"
}
```

Attachment [trac-3317-citation-system-integrated.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-citation-system-integrated.patch) by ranosch created at 2012-05-28 15:55:50

New citation system



---

archive/issue_comments_022998.json:
```json
{
    "body": "Fixed bugs and doctests.",
    "created_at": "2012-05-28T16:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22998",
    "user": "ranosch"
}
```

Fixed bugs and doctests.



---

archive/issue_comments_022999.json:
```json
{
    "body": "environment changes for the citation system",
    "created_at": "2012-05-28T22:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-22999",
    "user": "ranosch"
}
```

environment changes for the citation system



---

archive/issue_comments_023000.json:
```json
{
    "body": "Attachment [trac-3317-citation-system.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-citation-system.patch) by ranosch created at 2012-05-28 22:43:46\n\nNew citation system",
    "created_at": "2012-05-28T22:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23000",
    "user": "ranosch"
}
```

Attachment [trac-3317-citation-system.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-citation-system.patch) by ranosch created at 2012-05-28 22:43:46

New citation system



---

archive/issue_comments_023001.json:
```json
{
    "body": "bibtex-data of some components",
    "created_at": "2012-05-28T22:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23001",
    "user": "ranosch"
}
```

bibtex-data of some components



---

archive/issue_comments_023002.json:
```json
{
    "body": "Attachment [trac-3317-example-usage.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-example-usage.patch) by ranosch created at 2012-05-28 22:45:10\n\nExample usage in multipolynomial-libsingular",
    "created_at": "2012-05-28T22:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23002",
    "user": "ranosch"
}
```

Attachment [trac-3317-example-usage.patch](tarball://root/attachments/some-uuid/ticket3317/trac-3317-example-usage.patch) by ranosch created at 2012-05-28 22:45:10

Example usage in multipolynomial-libsingular



---

archive/issue_comments_023003.json:
```json
{
    "body": "would it be possible to add in the description some concrete example demonstrating what functionality this ticket adds to Sage?\n\nPaul",
    "created_at": "2014-08-25T15:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23003",
    "user": "@zimmermann6"
}
```

would it be possible to add in the description some concrete example demonstrating what functionality this ticket adds to Sage?

Paul



---

archive/issue_comments_023004.json:
```json
{
    "body": "Changing type from task to enhancement.",
    "created_at": "2014-08-27T11:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23004",
    "user": "@burcin"
}
```

Changing type from task to enhancement.



---

archive/issue_comments_023005.json:
```json
{
    "body": "Changing component from packages: standard to misc.",
    "created_at": "2014-11-13T14:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23005",
    "user": "@jdemeyer"
}
```

Changing component from packages: standard to misc.



---

archive/issue_comments_023006.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-04-21T17:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23006",
    "user": "@saraedum"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023007.json:
```json
{
    "body": "The patches do not apply anymore (not too surprising after so many years.)",
    "created_at": "2016-04-21T17:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23007",
    "user": "@saraedum"
}
```

The patches do not apply anymore (not too surprising after so many years.)



---

archive/issue_comments_023008.json:
```json
{
    "body": "To be honest I like the approach used by `citation.pyx` better because it does not add any performance overhead unless you care. Then again, the output generated by the patches here is really nice\u2026",
    "created_at": "2016-04-21T17:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3317#issuecomment-23008",
    "user": "@saraedum"
}
```

To be honest I like the approach used by `citation.pyx` better because it does not add any performance overhead unless you care. Then again, the output generated by the patches here is really nice…
