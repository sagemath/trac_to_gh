# Issue 9418: Add GNU patch as a standard package.

Issue created by migration from https://trac.sagemath.org/ticket/9418

Original creator: drkirkby

Original creation time: 2010-07-03 08:29:24

Assignee: GeorgSWeber

CC:  leif

As discussed here:

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3

GNU patch

http://www.gnu.org/software/patch/

is to be added as a standard package to Sage, to allow the use of 'patch' to be used to make patches, rather than to us 'cp' as now. 

A new package may be found here 

http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg

but the file `spkg/standard/deps will need to be updated` too. There are several tickets currently open (#9274, #9351 and #9412) for making updates to 'deps' so these need to be coordinated. 

Once this is done, the [Sage Developers Guide](http://www.sagemath.org/doc/developer/) will need to be updated to reflect a new method to create patches. A separate ticket will be opened for that. 

Dave


---

Comment by drkirkby created at 2010-11-13 18:20:03

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-11-13 23:04:22

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-13 23:04:22

Would you care to provide a `spkg/deps` patch so we can test that too?


---

Comment by jdemeyer created at 2010-11-13 23:05:04

Changing keywords from "" to "patch spkg".


---

Attachment

Patch for the install file in the sage_scripts-4.6.1.alpha1 package.


---

Attachment

Replacement 'install' file


---

Comment by drkirkby created at 2010-11-13 23:59:20

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-11-13 23:59:20

I'm somewhat puzzled. There seems to be two copies of the install file - one in `$SAGE_ROOT/spkg/install`, and another in the sage-scripts package. 

I think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package. That has a repository, but there are uncommitted changes. 

Dave


---

Comment by drkirkby created at 2010-11-14 00:06:22

I just realised, I ommitted to add PATCH as a dependancy of GAP. It's implied anyway, due to the fact readline, sage and termcap all depend on patch, and gap depends on all them. But I will correct it to make it clearer. 

IMHO, it would be a lot nice if this file was sorted alphabetically a bit better, but I wont do that now.


---

Comment by drkirkby created at 2010-11-14 00:06:22

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-11-14 00:15:24

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-11-14 00:16:44

Changing keywords from "patch spkg" to "patch spkg".


---

Comment by drkirkby created at 2010-11-14 00:36:12

SPKG.txt


---

Attachment

spkg-check


---

Attachment

spkg-install


---

Comment by drkirkby created at 2010-11-14 00:38:27

I realised I had not stuck a Mercurial repository in the package - I guess I was expecting people to want to make changes. But I've added one now. I don't know if its normal to add the SPKG.txt, spkg-install and spkg-check files to a new package, but I've them here anyway. No doubt Leif will find something wrong!

Dave


---

Comment by drkirkby created at 2010-11-14 00:43:33

What I meant to say was, I don't know if its normal to attach those 3 files to the ticket. But it can't do any harm I guess.


---

Comment by jdemeyer created at 2010-11-14 09:47:58

Replying to [comment:5 drkirkby]:
> I think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package.

At some point during the installation (or during sdist maybe?), the `install` from the `sage_scripts` package gets copied to `spkg/install`.  Also, `sage-spkg`, `sage-env`, `sage-make_relative` are copied to `spkg/base`.  Don't ask me why, but that's the way it is.


---

Comment by jdemeyer created at 2010-11-14 09:56:28

David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a "as-needed" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?


---

Comment by jdemeyer created at 2010-11-14 10:13:31

Proof-of-concept spkg using patch: [http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg)


---

Comment by drkirkby created at 2010-11-14 10:35:24

Replying to [comment:12 jdemeyer]:
> David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a "as-needed" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?
I do not think that would be a good idea. Every time someone wants to add a patch, they would need to create one for 'deps' too. A lot of people don't know how to use that file. Note even my initial comments I noted there were several tickets touching 'deps' and these would need to be coordinated. To make matters even more complicated, the 'deps' file is not under revision control, which make s updating that file more problematic. 

If the `patch` package took a long time to build, then I could see it would slow the build of Sage, as it introduces a sometimes unnecessary dependency. But for a package which takes less than 4 seconds to build *and* run all the self tests, I think it is better to add it to 'deps' now, so every package could use it now. 

It also avoids the very real risk someone will create a patch, which will work on their system since either
 * patch has already benn built.
 * There's a suitable version of patch on their system.

The patch would fail to install on another computer, because patch is not built at that point in time. Since the order of building packages is not fixed. 

IMHO, `patch` should be built early, so it can be used with the minimum amount of effort.


Dave


---

Attachment

Added ticket number to file name


---

Comment by jdemeyer created at 2010-11-14 23:46:43

I suggest a small "sanity check" at the end of `spkg-install` to check that the `patch` in the PATH is the right one.  Something like

```
if ! patch --version | grep >/dev/null 'patch 2.6.1'; then
    echo "Cannot to find the patch program we just installed"
    exit 1
fi
```


I know you like `grep >/dev/null`  ;-)


---

Comment by jdemeyer created at 2010-11-14 23:48:47

Also: do we really *need* all the 64-bit checking stuff?


---

Comment by jdemeyer created at 2010-11-15 00:02:29

Regarding `deps`: is there a reason that SQLALCHEMY doesn't have PATCH as dependency?

Also, some packages are their own "upstream", so should never include patches.  These are genus2reduction, extcode, examples, sagenb (and possibly more).


---

Comment by drkirkby created at 2010-11-15 00:38:24

Yes, I feel we do need the 64-bit things. Sure, a 32-bit version of patch would probably do all we want, but the same is true of some other commands like 'rubiks'. But building them all 64-bit makes it much easier to detect if there are any 32-bit code by mistake. Knowing that every single library and ever single binary should be 64-bit makes finding any 32-bit objects very easy. 

Having the option to specify another another 64-bit flag could be useful in a port. Having spent ages sorting out the mess someone created by assuming only 64-bit OS X would be supported, and the option would be `-m64`, I'm reluctant to inflict such a stupid thing on someone else. 

SQLALCHEMY is an oversight. That does need correcting. 

I don't think it's safe to assume that just because a package is it's own upstream, that it will not necessarily ever be patched by someone other than the developer. Consider genus2reduction. That is currently at patch level 8, There are no patches, but many times people have changed spkg-install. What gives you confidence that someone might not need to change a file in this package? 64-bit support as added to genus2reduction, but on the Pari package, adding 64-bit supported needed updating of makefiles. How can you be so confident that a change in genus2reduction would not need a patch? 

To me, removing dependencies will not speed up the build of Sage, but could potentially lead to problems. Being able to say "you can use patch for *any* package not in the BASE group (`prereq`, `bzip2 etc`, `dir` and `sage_scripts`), is much easier than documenting you can use patch on most package, not not A, B, C, D, E ...etc. 

I fail to see what is gained by removing what may be a technically unnecessary dependency, but in practice will have no harmful effect, and can stop difficult problems occurring. 

With few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. 

But it's 0037 AM here, and I'm not going to be making any changes for 8 hours at least. 

Dave


---

Comment by jdemeyer created at 2010-11-15 09:10:09

Dave, I agree with all of your post above.


---

Comment by jdemeyer created at 2010-11-15 09:11:52

Replying to [comment:20 drkirkby]:
> With few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. 

You can also consider it to be a sanity check that SAGE_LOCAL and PATH have sensible values.


---

Comment by cremona created at 2010-11-15 11:35:46


```
SAGE_CHECK='yes' sage -f http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg
```

worked fine on 64-bit ubuntu and 32-bit Suse, with 4.6.1.alpha1 and 4.6.1.alpha0 respectively.

For a positive review is it enough that this spkg builds fine on all supported systems, or do we also need to have at least one other spkg converted to use it and build ok?


---

Comment by drkirkby created at 2010-11-15 11:48:17

There are a couple of issues to be fixed
 * SQLALCHEMY is not listed as depending on patch, when it should be. 
 * Jeroen felt testin that patch actually reported the right version would be sensible. 
 * I think it would be sensible the self-tests of the package are run on every system, not just with SAGE_CHECK=yes. Since
   * They take less than half a second on my machine (3.33 GHz Xeon). 
   * A bad version of patch could create all sorts of problems. 

I will address these today, but I have to do some other things. I'll put it to needs work for now, until I get chance to do this. 

Dave


---

Comment by drkirkby created at 2010-11-15 11:48:17

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-11-15 12:26:51

On the 64-bit ubuntu system, I installed the new version of the Sphinx package (with -f) and did a full test.  All OK except this:

```
sage -t -long ./sage/misc/sagedoc.py
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 891:
    sage: len(search_doc('tree', interact=False).splitlines()) > 2000
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    False
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 893:
    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 200
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    True
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 496:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    False
**********************************************************************
```

Before installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?


---

Attachment

Corectted 'deps' file, with SQLALCHEMY taken care of


---

Comment by drkirkby created at 2010-11-15 12:41:53

Updated deps patch, with ticket name and with the SQLALCHEMY resolved


---

Attachment

I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 

It would be useful to get this tested in its current state, as changes will be minimal

dave


---

Comment by jdemeyer created at 2010-11-15 13:20:33

Replying to [comment:26 cremona]:
> Before installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?

In any case, I doubt this is an issue regarding _patch_.  The main point was to test whether the spkg installed.


---

Comment by cremona created at 2010-11-15 14:20:37

Replying to [comment:27 drkirkby]:
> I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 

That would be a colour patch, I presume?


---

Comment by drkirkby created at 2010-11-15 15:01:44

Replying to [comment:29 cremona]:
> Replying to [comment:27 drkirkby]:
> > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 
> 
> That would be a colour patch, I presume?
> 
I think it will be showed as red and green in the browser, though the paint was white!

dave


---

Comment by jdemeyer created at 2010-11-16 15:39:30

Patch >= 2.6 seems to be broken on OS X 10.4 (and supposedly also Solaris).  I have tested upstream patch 2.5.9 and that works fine.

So I propose to use [http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz](http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz)


---

Comment by jdemeyer created at 2010-11-16 16:07:23

I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)

I also added the sanity check that I mentioned, not yet the `make check`.


---

Comment by drkirkby created at 2010-11-16 16:50:45

Replying to [comment:33 jdemeyer]:
> I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)
> 
> I also added the sanity check that I mentioned, not yet the `make check`.

I built it on OpenSolaris OK. There's a `make check` which I had created. 

However, the version you have now used has no test facility, so `make-check` should simply be removed. The developers must have added the facility to test on more recent versions only. 

I've created a version at 

http://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg

which has the spkg-check file removed, and so notes to say not to update to 2.6 or 2.6.1. I will add a Mecurial patch in a minute. 


Dave


---

Comment by drkirkby created at 2010-11-16 16:55:30

Remove the spkg-check file, as this version of patch has no self-tests that can be run.


---

Attachment

I've checked the version at 

http://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg

installs OK on 

 * OpenSolaris 06/2009 (my machine hawk).
 * Solaris 10 SPARC (t2.math)
 * Solaris 10 x86 (fulvia on skynet)
 * Linux (sage.math)  
 * OS X 10.6 (bsd.math)
 
I can confirm that 2.6.1 did fail to install on Solaris 10 on SPARC (t2.math)

Dave


---

Comment by drkirkby created at 2010-11-16 17:33:39

We need info about if this builds OK on other operating systems. 

I've changed from Needs Work -> Needs Info, as I think this *should* need no further changes. 

Can someone confirm it works on OS X 10.4? If so, I think this will be ready for review. 

Dave


---

Comment by drkirkby created at 2010-11-16 17:33:39

Changing status from needs_work to needs_info.


---

Comment by jdemeyer created at 2010-11-16 18:18:12

David's spkg works on OS X 10.4 (as expected)


---

Comment by drkirkby created at 2010-11-16 18:56:43

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-11-16 18:56:43

With this now checked on 

 * Linux (sage.math)
 * OpenSolaris 06/2009 (my machine hawk).
 * Solaris 10 SPARC (t2.math)
 * Solaris 10 x86 (fulvia on skynet)   
 * OS X 10.6 (bsd.math) 
 * OS X 10.4 

I think this is enough for a positive review. I've set to needs review. If someone else feels likewise, we might as well set this to positive. 

If there are any issues on fully supported platforms, the buildbot should find them.

Will the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. 

Dave


---

Comment by jdemeyer created at 2010-11-16 19:00:26

Replying to [comment:39 drkirkby]:
> Will the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. 

Yes, it will be in the next alpha (unless there is major breakage on my own testing systems), but it still needs_review (#10118).


---

Comment by drkirkby created at 2010-11-16 19:06:01

PS, it would be useful to attach a build log of the failure to build on OS X 10.4 with patch 2.6.1, along with the config.log for OS X. Just log building the upstream source, outside of Sage. I'll do likewise for Solaris 10 on SPARC.

Then I can report the bug with patch 2.6.1 upstream, and provide links to the failed logs. Having provided links to failed builds on two platforms, the developers should be in a good position to fix the bug. 

Dave


---

Comment by jdemeyer created at 2010-11-18 09:36:51

Fixed a trivial typo (`cannot to find...` -> `cannot find`) in `spkg-install`.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)


---

Comment by jdemeyer created at 2010-11-18 09:36:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-19 07:54:07

Resolution: fixed


---

Comment by jhpalmieri created at 2010-11-20 19:42:50

See #10299 for a follow-up.


---

Comment by leif created at 2010-11-21 22:42:00

Replying to [comment:30 drkirkby]:
> Replying to [comment:29 cremona]:
> > Replying to [comment:27 drkirkby]:
> > > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 
> > 
> > That would be a colour patch, I presume?
> > 
> I think it will be showed as red and green in the browser, though the paint was white!

Should we ask Microsoft if we can make `paint` a standard spkg as well?

----

Stop environmental pollution...

We already have nice environment variables like "`R`" and "`PYTHON`"; can we rename it to e.g. `GNU_PATCH` in `spkg/install` and `spkg/standard/deps`?

----

P.S.: Why not add the `patch` spkg to `$(BASE)` (and make it depend on the previous three `$(BASE)` packages)?

As is, *all* standard spkgs will get rebuilt on an upgrade (to a version of Sage with `patch` "newly" included) anyway. (Therefore I would actually prefer adding `patch` as a dependency selectively. `spkg/standard/deps` will be under revision control soon...)


---

Comment by jdemeyer created at 2010-11-22 08:05:42

Leif: I don't have any particular feelings either in favour of or against your suggestions.  Feel free to open a new ticket for these issues.

About `$(BASE)`: I never quite understood the difference between `spkg/base` and `spkg/standard`.  What is the difference?
