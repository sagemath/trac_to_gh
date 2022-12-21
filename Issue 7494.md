# Issue 7494: remove (or clean up) SAGE_ROOT/examples

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-19 22:55:57

Assignee: tbd

CC:  wdj

Did you know there is a directory SAGE_ROOT/examples?   Do you care?  Because if nobody seriously cares, I'm going to *delete it* from future versions of Sage, since it is still a mess, and the last nontrivial commit was 1.5 years ago (!):

```
changeset:   158:d18dad210d3b
user:        Mike Hansen <mhansen`@`gmail.com>
date:        Mon Apr 14 03:08:48 2008 -0700
summary:     Extract sagetex.py and sagetex.sty
```

I can put the same directory online somewhere, and move the fortran file that is used in one doctest out.  I'm just really curious if anybody knows about this directory and cares.


---

Comment by was created at 2009-11-19 23:28:08

#298 would be invalidated by doing this ticket.


---

Comment by kcrisman created at 2009-12-30 04:27:30

I was wondering about that directory too a few months ago.  So we don't do anything with it currently?  Here are comments.

I think it would be worth linking at least a few of the top-level ones to the wiki, and perhaps put in one of the documentation places, as some of the examples files there are definitely useful for templates.  

I bet some of the programming (Pyrex/SageX/Cython) examples might be useful too.  

I am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.

The linalg folder is definitely pointless, as permanents are now in the main library.

The worksheets folder seems pretty pointless in its current state.

The tests directory has some things that should be added as random doctests for those things, though.

The modsym directory stuff likely is already tested in that area, given how important it is to Sage!

The latex_embed is obviously superfluous at this point.

Fortran was has already discussed above.

Finance is *really* pointless.

The Groebner basis thing seems intriguing - perhaps should be incorporated in doctests for that elsewhere?

Is the Ajax thing now very very superfluous, given how much we use it?  It's not (that) old.

The GSL folder is quite large compared to the rest and perhaps has some examples which should be combined into one big file which is doctested, if those sorts of tests aren't.  It would seem valuable not to lose this many doctests -does it currently pass?


---

Comment by kcrisman created at 2010-04-27 19:47:31

> 
> I am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.

See #7936 for this - we can delete this one, at least.


---

Comment by kini created at 2011-06-14 22:38:50

The last nontrivial commit was 1.5 years before this ticket was created, but now it's been 1.5 years since this ticket was created! Can we get rid of this directory yet?


---

Comment by kcrisman created at 2011-06-14 22:45:58

I have asked about this a lot.   In order to give this, it would be really nice to move a few of the examples to other places - wiki, wherever.  

 * a few top-level things
 * some of the Cython ones?
 * tests has a few interesting random doctests
 * something fortran is needed somewhere, apparently?  According to the comment in was' original report
 * The GSL examples might be worth moing somewhere
 * Groebner useful in doctests?

Anyway, we shouldn't just completely delete in case there are useful tests.    But I totally agree on the overall strategy.


---

Comment by was created at 2011-08-24 06:26:52

Changing status from new to needs_review.


---

Comment by was created at 2011-08-24 06:26:52

Delete it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

I wrote almost everything in there, and it should just go. 

I give "delete the examples directory" a positive review.  To merge this ticket, do

```
cd SAGE_ROOT
rm -rf examples
```



---

Comment by was created at 2011-08-24 06:27:01

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-08-24 06:28:43

For future reference, I've put that directory here:

    http://wstein.org/old_sage_examples/


---

Comment by was created at 2011-08-24 06:31:40

I just realized that there is one thing that has to be done. Observe:

```
wstein`@`ubuntu:~/d/sage$ sage -grep "examples"|grep SAGE_ROOT
finance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]
finance/stock.py:            sage: finance.Stock('goog').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]
finance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + "/examples/finance/AAPL-minutely.csv")
misc/hg.py:hg_examples = HG('%s/data/examples'%SAGE_ROOT,
misc/inline_fortran.py:            sage: s = open(os.environ['SAGE_ROOT'] + '/examples/fortran/FIB1.F').read()
wstein`@`ubuntu:~/d/sage$ 
```


So the stuff in examples that are used in doctests need to be moved to the SAGE_ROOT/data/ directory.  Thus one needs to attach a patch that does this to this ticket, and that patch will need to be reviewed.


---

Comment by was created at 2011-08-24 06:31:40

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by was created at 2011-08-24 06:44:53

The patch  trac_7494.patch should change the core sage library so it doesn't depend on anything in the SAGE_ROOT/examples directory for testing.  It also does not put anything in the SAGE_ROOT/data directory, since that is not needed.


---

Comment by was created at 2011-08-24 06:48:21

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-08-24 12:16:51

So the Groebner, gsl, etc. tests aren't really useful? Ok by me.

Nice - thanks for looking at this "officially". Since there is a Sage Days going on and today is my first day of classes, I think someone will beat me to the review, but thanks for looking at this a bit more carefully. In some sense, you are the only person who can check it, since you're one of the few who really knows why these things were in in the first place :)


---

Comment by was created at 2011-08-24 23:48:02

Changing keywords from "" to "sd32".


---

Comment by rbeezer created at 2011-08-25 06:35:03

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2011-08-25 06:35:03

Trash it.  There's too much old misleading stuff about as is.

I renamed the examples directory, applied the patch, ran tests and got no failures.

I guess we need to alert the release manager somehow to actually delete the directory in the next distribution?  I'll put a note above, edit as necessary.


---

Comment by jhpalmieri created at 2011-08-25 21:59:22

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2011-08-25 21:59:22

This also needs a patch to the scripts repo, since `sage-make_devel_packages` tries to create a new examples spkg and fails with a nonzero exit status if it can't do that.  I'm attaching a patch.


---

Comment by jhpalmieri created at 2011-08-25 21:59:28

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-08-25 21:59:48

scripts repo


---

Comment by was created at 2011-09-27 01:23:17

Changing status from needs_review to positive_review.


---

Attachment

I'm good with jhpalmieri's cleanup of my patch.


---

Comment by leif created at 2011-09-27 18:34:17

The root repository certainly also has to get patched:

```sh
$ grep -win examples spkg/install spkg/standard/deps 
spkg/install:184:EXAMPLES=`$newest examples`
spkg/install:185:export EXAMPLES
spkg/standard/deps:48:     $(INST)/$(EXAMPLES) \
spkg/standard/deps:398:$(INST)/$(EXAMPLES): $(BASE) $(INST)/$(PATCH)
spkg/standard/deps:399:	$(INSTALL) "$(SAGE_SPKG) $(EXAMPLES) 2>&1" "tee -a $(SAGE_LOGS)/$(EXAMPLES).log"
```



---

Comment by leif created at 2011-09-27 18:34:17

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2011-09-27 19:41:33

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-09-27 19:41:33

I think this searches through all of the relevant files:

```
$ grep -win examples `hg manifest`
```

I'm attaching a patch for this.  In addition to the two files you found, it also patches libdist_filelist, which looks like it is _completely_ out of date, but it doesn't hurt to patch it anyway.


---

Comment by jhpalmieri created at 2011-09-27 19:41:46

root repo


---

Comment by leif created at 2011-09-29 01:59:00

Changing status from needs_review to positive_review.


---

Attachment

Ok, I've `sdist`ed with a version with the patches applied, built the new Sage distribution from scratch, and all (long) tests pass.

As expected, I got rid of the `examples/` directory and the spkg in the new distro.
(Note that also the examples spkg in `spkg/standard/` of the _original_ distribution got deleted; not sure whether this is intentional. In contrast, the `examples/` directory there remained.)

Upgrading from a path without an examples spkg _should_<sup>TM</sup> IMHO also work; haven't tried that [yet].




Don't know yet whether Jeroen's merger is "prepared" for such an operation, and since Sage 4.7.2.alpha3 is almost out, I don't think I'll attempt to merge this ticket into _this_ release. There'll certainly be an alpha4, or we could try with the next release candidate.

Unfortunately we don't win much regarding the size; the current examples spkg is just 2.0 MB, 3.9 MB uncompressed on my disk (i.e., the size of the `examples/` directory), and just 2.6 MB in "real" bytes.


---

Comment by jdemeyer created at 2011-10-04 21:12:05

Problems while building the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:8: (ERROR/3) Unexpected indentation.
```



---

Comment by jdemeyer created at 2011-10-04 21:12:05

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2011-10-04 22:36:55

I believe this referee patch should fix the documentation problem.


---

Comment by jhpalmieri created at 2011-10-04 22:36:55

Changing status from needs_work to needs_review.


---

Attachment

Sage library: fix docbuilding problem


---

Comment by leif created at 2011-10-05 00:09:06

Replying to [comment:22 jhpalmieri]:
> I believe this referee patch should fix the documentation problem.

Belief is not a technical category.

Nice patch by the way.


---

Comment by leif created at 2011-10-05 00:09:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-05 12:19:11

Resolution: fixed


---

Comment by jhpalmieri created at 2011-10-08 17:22:55

See #11907 for a followup.
