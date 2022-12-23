# Issue 9905: Move the RPy package outside of the R package

Issue created by migration from https://trac.sagemath.org/ticket/9906

Original creator: mpatel

Original creation time: 2010-09-13 23:08:55

Assignee: tbd

CC:  leif kcrisman vbraun kini

We include the RPy spkg in the R spkg and install the former from the latter.  It would be less potentially confusing to move RPy outside of R but make it depend on R and any other prerequisites in `spkg/standard/deps`.

Related: #3086.


---

Comment by leif created at 2010-09-14 07:05:54

It would also allow independent updates and potentially improve compression.


---

Comment by leif created at 2010-09-20 22:26:49

When touching the R package, one should also consider #9847 (i.e. R environment variables potentially disturbing the build).


---

Comment by leif created at 2010-09-25 18:04:38

Changing priority from minor to critical.


---

Comment by leif created at 2010-09-25 18:04:38

Changing type from enhancement to defect.


---

Comment by leif created at 2010-09-25 18:04:38

See [comment:ticket:9896:95 this comment] for another important reason.


---

Comment by leif created at 2010-09-25 18:10:14

(Having Rpy in R's spkg is the culprit of [comment:ticket:8306:29 this build error].)


---

Comment by leif created at 2010-09-26 04:07:57

I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... (including updated `deps` and `spkg/install`)

I also cleaned up both packages a little, and tried to address #9847, too.


---

Comment by leif created at 2010-09-26 04:07:57

Changing assignee from tbd to leif.


---

Comment by drkirkby created at 2010-10-01 13:43:20

Replying to [comment:5 leif]:
> I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... 

How soon is soon? 

If you can make these available, it will help those that want to update the source code. 

Dave


---

Comment by leif created at 2010-11-03 01:41:43

Personal note:

 * Add patching `libR.pc` to `spkg-install`, making `rhome` and `rincludedir` relative to `$SAGE_ROOT`. (Currently no `prefix=...` definition.)


---

Comment by kcrisman created at 2011-04-25 14:23:13

Changing priority from critical to major.


---

Comment by kcrisman created at 2011-08-03 15:06:25

So... does this activity mean you will be posting something on e.g. spkg-upload? 

:)


---

Comment by leif created at 2011-08-05 10:21:04

Changing status from new to needs_review.


---

Comment by leif created at 2011-08-05 10:32:57

Replying to [comment:11 kcrisman]:
> So... does this activity mean you will be posting something on e.g. spkg-upload? 

Looks like. Before the spkgs have their first anniversary...

There are (still) some things that could be done, e.g. using `patch` and patching the `pkg-config` file (`libR.pc`) from `spkg-install`.

We could also perhaps either recompress the contained recommended R packages (`.tar.gz`) with `bzip2` or decompress them to plain `tar` files, as we compress the whole spkg with `bzip2` anyway. Haven't yet tried that though.

RPy (and perhaps R) should IMHO be upgraded on a follow-up ticket.


---

Comment by leif created at 2011-08-05 11:24:10

I see the hardcoding issues shouldn't be hard to fix; the current (more or less superfluous) patch to `R.sh.in` and the corresponding Python script do only half of the job, namely setting `R_HOME_DIR` to `$SAGE_LOCAL/lib/R/`, but not changing `R_SHARE_DIR`, `R_INCLUDE_DIR` and `R_DOC_DIR`.

But before I do so, I think the new spkgs should first be tested as they are.

I'll then make a p6, either here or (preferably) on a follow-up ticket if no other issues arise with the p5.


---

Comment by kcrisman created at 2011-08-05 17:54:37

Yes, a different ticket would be fine.    I didn't realize these spkgs were actually ready :)

Comments/questions:
 * The rpy2 patch looks fine, and those are nice additions (the sanity checks, I mean).  
 * Really excellent work clarifying things on the r patch, adding all those checks etc.  I wouldn't have thought of any of them, but they all make loads of sense, though probably won't affect a million users.  I'm probably the one responsible for the .DS* stuff - I always try to check, but sometimes one forgets.
 * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)
 * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?
 * What happened to Dave's favorite `"x$SAGE64" = xyes` (you removed the 'x's)?
 * Any reason to include the old RPy installation in the `if false` block?  Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.

Note I have not actually installed or tested this yet :)


---

Comment by leif created at 2011-08-07 03:53:02

_Sorry for the delay, no trac notifications..._ >B-|

Replying to [comment:15 kcrisman]:
> Yes, a different ticket would be fine.

#9668 if you don't object...



> I didn't realize these spkgs were actually ready :)

I didn't know either. ;-)

More or less just completed the Changelog entries.



> Comments/questions: 

>  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)

It's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)

Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in _RPy's_ `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.

IIRC there were also problems with `R_PROFILE` when _using_ Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.



>  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?

Well, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)



>  * What happened to Dave's favorite `"x$SAGE64" = xyes` (you removed the 'x's)?

I get eye cancer from such, it's worse readable and hence error-prone. If `test "" = foo` would evaluate to `true` (on some supported systems) Sage would certainly break in many places, not just because _we_ use that all around. _Quoting_ is important.

(The broken instance of `test` was btw. a shell built-in version [besides some _really very old_ `test` implementations which were less robust w.r.t. invalid expressions], and we explicitly use `bash` anyway. Prepending characters to variable expansions can make sense in different contexts, and is sometimes used to save the quotes, though the latter is also quite ugly. Similar applies to _not_ using `-o` and `-a`.)

If one wanted to go really safe, one would either explicitly use `bash`'s built-in version of `test` (`[This is the Trac macro *"$SAGE64" = yes * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#"$SAGE64" = yes -macro)`), use `case "$SAGE64" in yes) ...`, or perhaps

```sh
[ "${SAGE64:-no}" = yes ]
```

which is the equivalent of Python's

```python
os.environ.get("SAGE64", "no") == "yes"
```




>  * Any reason to include the old RPy installation in the `if false` block?

Not really.

> Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.

Sure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.



> Note I have not actually installed or tested this yet :)

Hope you'll do so later. :)


---

Comment by kcrisman created at 2011-08-08 14:11:07

> > Yes, a different ticket would be fine.
> #9668 if you don't object...
No, that is quite natural.
> >  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)
> It's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)
I didn't realize that.  
> Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in _RPy's_ `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.
So maybe that's a "needs work"?
> IIRC there were also problems with `R_PROFILE` when _using_ Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.
Yes, that's a different ticket, and notoriously hard to track down at times.
> >  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?
> 
> Well, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)
Ok.
> >  * Any reason to include the old RPy installation in the `if false` block?
> Not really.
> > Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.
> Sure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.
Well, either way that wouldn't hold up this ticket.
> > Note I have not actually installed or tested this yet :)
> Hope you'll do so later. :)
But not today :(


---

Comment by leif created at 2011-08-09 05:46:12

Replying to [comment:17 kcrisman]:
> > > Yes, a different ticket would be fine.
> > #9668 if you don't object...
> No, that is quite natural.

Ok.




> > Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in _RPy's_ `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.
> So maybe that's a "needs work"?

`R_PROFILE` doesn't appear in any of RPy's source files, so I don't think so. (I perhaps checked that last year, but forgot about it. :D )


---

Comment by kcrisman created at 2011-08-10 21:16:38

Just a note to self/any other reviewer of what would have to be tested.
 * Upgrading rpy2 by itself.
 * Upgrading r by itself.
 * Then upgrading rpy2 after having upgraded r.
 * And test R and rpy2 after each step.
 * Test with and without `R_PROFILE` set.
 * Test with and without `SAGE_CHECK` set.
 * Test with `SAGE_CHECK` yes with and without parallel make.
 * Test on (at least) Linux and Mac.
 * Test with and without spaces in the path.
Remind me why this is needed again?  :-)


---

Comment by kcrisman created at 2011-08-19 13:48:07

Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.


---

Comment by leif created at 2011-08-21 00:57:20

Replying to [comment:20 kcrisman]:
> Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.

For the record: #10967 will be addressed at #9668, by an R 2.10.1.p6 spkg there, so I've made the former ticket depend on the latter, and changed its milestone to _"duplicate/invalid/won't fix"_.


---

Comment by leif created at 2011-10-09 15:49:43

Ping.

I think we should merge this before it further rottens; I'll not be able to finish #9668 in the next days (and right now don't know when I'll do that), but it's not a dependency anyway, just a further improvement...


---

Comment by kcrisman created at 2011-10-10 02:13:08

Sorry, I just won't have time to do that laundry list of testing in the near future.  (As you may have noticed from my relative lack of activity elsewhere.)   And there isn't really anything breaking because of this weirdness, thankfully... My apologies :(


---

Comment by jason created at 2011-11-15 05:15:33

Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.


---

Comment by kcrisman created at 2011-11-20 01:17:32

Changing keywords from "" to "r-project".


---

Comment by kcrisman created at 2011-11-20 01:18:18

Replying to [comment:25 jason]:
> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.

Regarding this, see #12057.


---

Comment by jdemeyer created at 2011-12-09 10:49:56

Replying to [comment:25 jason]:
> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.

Well, this didn't happen.  R will be upgraded to version 2.14 in #12057 which will normally be merged in sage-4.8.alpha4.  So, this ticket needs to be rebased...


---

Comment by jdemeyer created at 2011-12-09 10:49:56

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-12-09 11:03:38

Replying to [comment:25 jason]:
> I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)
Testing is easy, I wouldn't mind doing that.


---

Comment by kcrisman created at 2011-12-09 14:55:01

> > I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)
> Testing is easy, I wouldn't mind doing that.
I had the same problem, because it would require a lot of manual stuff, but if you can use the buildbot to test a rebased version of this that would be fantastic.


---

Comment by kcrisman created at 2012-01-17 14:55:36

Apparently we also should take care of some references to sage-env or something which are soon to disappear - see #11073, in particular [comment:73:ticket:11073 this comment].


---

Comment by leif created at 2012-03-21 13:10:09

Argh!


---

Comment by jdemeyer created at 2012-09-04 12:04:04

Apply to SAGE_ROOT. Activates RPY in spkg/install and spkg/standard/deps


---

Attachment

Why should `R` depend on `PYTHON`?  The old `spkg/standard/deps` claims "Note that even with a separate RPy spkg (#9906), Sage's R will still depend on "Python, but I see no reason for this.  So I removed the explicit PYTHON dependency.  But it still indirectly depends on PYTHON via PYTHON->ATLAS->R.


---

Comment by jdemeyer created at 2012-09-04 12:08:16

Changing keywords from "r-project" to "r-project spkg".


---

Attachment

Diff for the R spkg. For reference / review only.


---

Comment by jdemeyer created at 2012-09-04 13:36:17

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-09-04 19:39:39

There is also some general cleanup that could happen; for example:

```diff
diff --git a/spkg-install b/spkg-install
--- a/spkg-install
+++ b/spkg-install
@@ -67,15 +67,6 @@ if [ "$UNAME" = "SunOS" ]; then
     SUN_FLAGS="--without-ICU"; export SUN_FLAGS
 fi
 
-# let's remove old install, even the wrongly installed ones
-rm -rf "$SAGE_LOCAL"/lib/r
-rm -rf "$SAGE_LOCAL"/lib/R
-rm -rf "$SAGE_LOCAL"/lib64/R
-rm -rf "$SAGE_LOCAL"/lib64/r
-# and let's also nuke some leftovers on SAGE_LOCAL/lib
-rm -rf "$SAGE_LOCAL"/lib/libRblas.so "$SAGE_LOCAL"/lib/libRlapack.so "$SAGE_LOCAL"/lib/libR.so
-rm -rf "$SAGE_LOCAL"/lib/libRblas.dylib "$SAGE_LOCAL"/lib/libRlapack.dylib "$SAGE_LOCAL"/lib/libR.dylib
-
 cd src
 
 # Apply patches.  See SPKG.txt for information about what each patch
@@ -131,6 +122,15 @@ if [ $? -ne 0 ]; then
     exit 1
 fi
 
+# Before installing, remove old install, even the wrongly installed ones.
+rm -rf "$SAGE_LOCAL"/lib/r
+rm -rf "$SAGE_LOCAL"/lib/R
+rm -rf "$SAGE_LOCAL"/lib64/R
+rm -rf "$SAGE_LOCAL"/lib64/r
+# and let's also nuke some leftovers on SAGE_LOCAL/lib
+rm -rf "$SAGE_LOCAL"/lib/libRblas.so "$SAGE_LOCAL"/lib/libRlapack.so "$SAGE_LOCAL"/lib/libR.so
+rm -rf "$SAGE_LOCAL"/lib/libRblas.dylib "$SAGE_LOCAL"/lib/libRlapack.dylib "$SAGE_LOCAL"/lib/libR.dylib
+
 # Disable parallel make install, which is supposedly broken
 $MAKE -j1 vignettes  # Needed for help system
 $MAKE -j1 install
@@ -168,7 +168,7 @@ if [ $? -ne 0 ] || [ ! -f "$SAGE_ROOT"/s
 fi
 
 if [ "$UNAME" = "Darwin" ]; then
-    echo "Copying fake java and javac compiler on OSX"
+    echo "Removing fake java and javac compiler on OSX."
     rm -f "$SAGE_LOCAL"/bin/java
     rm -f "$SAGE_LOCAL"/bin/javac
 fi
```

Should this happen on another ticket?


---

Comment by jdemeyer created at 2012-09-04 19:43:22

Replying to [comment:44 jhpalmieri]:
> Should this happen on another ticket?
Yes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.


---

Comment by jdemeyer created at 2012-09-04 20:00:35

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-09-04 20:00:35

rpy2 needs a version bump, otherwise it won't be downloaded when upgrading.


---

Comment by jdemeyer created at 2012-09-04 20:09:30

Changing status from needs_work to needs_review.


---

Attachment

Diff for the rpy2 spkg (w.r.t. to the one in the current R spkg). For reference / review only.


---

Comment by jhpalmieri created at 2012-09-05 04:41:42

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2012-09-05 04:41:42

Looks good to me. Builds and passes tests, and works when upgrading.


---

Comment by jdemeyer created at 2012-09-06 05:23:52

Resolution: fixed


---

Comment by kcrisman created at 2012-09-06 19:19:00

> > Should this happen on another ticket?
> Yes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.
You can cc: me on this new ticket too when you make it.


---

Comment by jdemeyer created at 2012-09-07 09:49:50

Replying to [comment:50 kcrisman]:
> You can cc: me on this new ticket too when you make it.
To be honest, this is not something I feel like working on, so I'm going to make that ticket.


---

Comment by jdemeyer created at 2012-09-10 14:03:32

Okay, I'm making the follow-up anyway: #13443.
