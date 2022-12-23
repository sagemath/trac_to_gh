# Issue 9533: Update GSL to the latest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/9533

Original creator: drkirkby

Original creation time: 2010-07-17 21:00:52

Assignee: tbd

CC:  leif mpatel

The version of the [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) in Sage is 1.10, which is almost 3 years old. The latest, 1.14 was released about 4 months ago. 

There is also a large number of bugs in the `spkg-check` and `spkg-install` files
 
 * `spkg-check` did not exit with a non-zero error code if the `make check` failed. It did however report the error, but it is highly likely to be missed in a large log file. This issue was reported at #9531, so that ticket can be closed when this one is closed. 
 * `spkg-install` did not exit if `configure` failed to configure properly. Again the error was reported. 
 * `spkg-install` did not exit if `make` failed to build GSL correctly. Again the error was reported. 
 * `spkg-install` did not exit if `make install` failed to install GSL properly. Again the error was reported. 
 * The self-tests were failing on some platforms, due to the fact `/bin/rm: cannot remove `libtoolT`. This was also true of the latest version, but exporting RM to "rm -f" solved that, as discussed at [solution for libtoolT error](http://toxpenguin.blogspot.com/2009/09/solution-for-libtoolt-error.html)


---

Comment by mpatel created at 2010-07-17 21:41:00

A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.


---

Comment by drkirkby created at 2010-07-17 21:59:26

Replying to [comment:1 mpatel]:
> A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.

I'm pretty sure we can, since I have built this multiple times on my Sun Blade 2000 SPARC with 2 threads and on my Sun Ultra 27 with 12 threads. This is outside the Sage environment, so my settings for MAKE would have been used. There were no problems building on either in parallel, so I don't think it will be a problem building with $MAKE. 

I'll test that before uploading a patch and providing a link. 

Dave


---

Comment by drkirkby created at 2010-07-18 00:21:24

I'm convinced this is ok built in parallel. I tested it several times in parallel (outside of Sage) before you even mentioned it. But after you said this, I used $MAKE in `spkg-install` and systematically checked it on different systems

 * 19 parallel builds on a Sun Ultra 27, with OpenSolaris using between 2 and 1000 threads. 
 * 5 parallel builds on bsd.math, with OS 10.6, using 4 threads.
 * 5 parallel builds on sage.math, with Ubunta, using 8 threads.
 * 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 64-bit)
 * 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 32-bit)
 
 
In all cases, all the self-tests for GSL passed. 


I've run the doctests on sage.math. I was quite expecting to get a few failures due to different results from different algorithms that might be used in the GSL library, but to my surprise:


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1095.8 seconds
kirkby@sage:/scratch/kirkby/sage-4.5$ 
```


Here's a link to the package. 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

I'm going to upload 3 patches. The first was all the updates. The second uses {{{$MAKE}} and the final one just prints an informative message when the tests pass. Is there a sensible way of reversing these patches once they are commited, so I don't need 3 of them? Anyway, the patches are for review only. They don't need to be applied to the package. 

The first patch is quite large, as it removes a big patch. 

Dave 
Dave


---

Attachment

Main patch, which makes many changes to clean up the spkg-check and spkg-install.


---

Attachment

Changes 'make' to '$MAKE' to allow faster parallel builds. This has been extensively tested


---

Comment by drkirkby created at 2010-07-18 00:23:26

Add a message to indicate the tests have passed.


---

Comment by drkirkby created at 2010-07-18 00:23:49

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-07-18 00:31:52

Changing type from defect to enhancement.


---

Comment by drkirkby created at 2010-07-18 00:40:59

On bsd.math


```
$ make ptestlong

<SNIP> 

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2503.7 seconds
[kirkby@bsd sage-4.5.rc1]$ 
```



---

Comment by leif created at 2010-07-18 01:22:58

At first glance (I only looked at the patches) ok, except
 * _Append_ to `CFLAGS` et al. rather than set/overwrite them
 * Typo: 1x s/builing/building/ (2nd patch SPKG.txt)
 * Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`
 * Move the "successful check" message out of the else part, right to the bottom ;-)

I don't know why you want to create a single patch, but you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.

I'll take a closer look at the package tomorrow, I think.


---

Comment by leif created at 2010-07-18 02:11:06

Replying to [comment:7 leif]:
> you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.

Oh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.


---

Comment by leif created at 2010-07-18 02:47:24

Replying to [comment:8 leif]:
> Oh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.

`hg import -f --no-commit ...` (three times) does the trick as well... :)


---

Comment by drkirkby created at 2010-07-18 07:14:53

Replying to [comment:7 leif]:
> At first glance (I only looked at the patches) ok, except
>  * _Append_ to `CFLAGS` et al. rather than set/overwrite them

OK. 

>  * Typo: 1x s/builing/building/ (2nd patch SPKG.txt)
Cheers

>  * Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`

Yes.

>  * Move the "successful check" message out of the else part, right to the bottom ;-)

Yes, good idea. It saves a few bytes. 

> I don't know why you want to create a single patch
I think its more difficult to read patches when they are very small. I'd personally rather see one patch that fixes all the problems, rather than loads of patches fixing parts of it. But I'll just add another patch here. 

Dave


---

Comment by drkirkby created at 2010-07-18 08:40:11

Patch taking into account comments by reviewer, and a bit of a tidyup.


---

Attachment

Leif,
I've taken your comments into account. I realised that despite what src/INSTALL says, -g -O2 were not added. So I've added them back, as they were before. I also noticed the web site I gave for the solution to the libtool problem (export RM="rm -f") was not the correct one. So I updated the web link in the description of this, and also in SPKG.txt

I also reformatted SPKG.txt so no lines are wider than 80 characters. 

I've replaced the package, so it can still be found at http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

Dave


---

Comment by drkirkby created at 2010-07-18 08:53:06

Slightlly simpler spkg-check


---

Attachment

A few (more general) questions:
 * Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)
 * Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?
 * Anything to add if `SAGE_FAT_BINARY` is `yes`?
 * I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.
 * Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.

P.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding "dead code" below it. Looking at the (fairly small) file in whole this seems less a danger... :)


---

Comment by leif created at 2010-07-18 19:31:17

Just for the record (mhansen?):
  _"GSL should compile with GCC under Cygwin on Microsoft Windows.There is a gsl package in the standard Cygwin distribution which contains any patches needed."_


---

Comment by drkirkby created at 2010-07-18 20:42:29

Replying to [comment:13 leif]:
> A few (more general) questions:
>  * Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)

I think that would be wise. I will address that. 

>  * Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?

To be practical, SAGE_DEBUG is not really going to be very useful, as too few packages use it. But I can make that change. Even if every .spkg in Sage used SAGE_DEBUG that way, many upstream packages add -O2 anyway. 

>  * Anything to add if `SAGE_FAT_BINARY` is `yes`?

I do not believe so. This does not link with anything other than ATLAS. 

>  * I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.

In general you are right, but in this case it is not necessary. I know that, as I was using SAGE64 set to yes to add the -m64 option. That's a pretty critical option on 64-bit builds, but it was not necessary to add it. I assume that's in the Makefile which has already been created. 

But I accept it would be safer, just in case GSL change the build process in some way. I am aware of cases where this has been an issue in `spkg-check`. I'll modify that. 

>  * Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.

Yes, again, it may be safer to do this. 

> P.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding "dead code" below it. Looking at the (fairly small) file in whole this seems less a danger... :)

No problem. I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. 

Dave


---

Attachment

Adds support for SAGE_DEBUG, CFLAG64, checks SAGE_ROOT and exports LDFLAGS on 64-bit builds


---

Comment by drkirkby created at 2010-07-18 22:05:38

I've made those changes. The package can be found here

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

It's interesting to compare compile and test times both with and without SAGE_DEBUG

 * SAGE_DEBUG=yes, SAGE_CHECK unset =  30.7s
 * SAGE_DEBUG unset, SAGE_CHECK unset = 50.7s
 * SAGE_DEBUG=yes, SAGE_CHECK=yes 1m:24s
 * SAGE_DEBUG unset, SAGE_CHECK=yes 1m:34s

So it takes 20 seconds longer to build when using optimisation. That time penalty drops to 10 seconds when the tests are run, as they obviously run quicker. (All times are measured on a 3.33 GHz Sun Ultra 27)


---

Comment by leif created at 2010-07-18 22:09:43

Replying to [comment:15 drkirkby]:
> I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. 

Well, without `exit` the script returns `$?`, which is even better, though in some cases (or bad scripts) this is not desirable.

----
I must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?


---

Comment by drkirkby created at 2010-07-18 22:38:39

Replying to [comment:17 leif]:

> I must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?

Like you, I can't understand the ATLAS thing. The [GSL web site](http://www.gnu.org/software/gsl/) mentions it:

_GSL requires a BLAS library for vector and matrix operations. The default CBLAS library supplied with GSL can be replaced by the tuned ATLAS library for better performance_

But when I tried building a 32-bit GSL in Sage, where there were all 64-bit libraries (including ATLAS), this built fine. Had it really tried to link to the ATLAS library, then the build would have failed. So quite how you link to ATLAS to get better performance is beyond me. It is certainly not linking to ATLAS in Sage. That means there is an unnecessary dependency in 'deps' but I'm not going to worry over this. 

Dave


---

Comment by drkirkby created at 2010-07-18 22:40:17

Any attempt to use ATLAS rather than CBLAS should be on another ticket.


---

Comment by leif created at 2010-07-18 22:52:11

Replying to [comment:19 drkirkby]:
> Any attempt to use ATLAS rather than CBLAS should be on another ticket.

I agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.


---

Comment by leif created at 2010-07-18 23:02:15

The GSL web site also lists _"Some applications using GSL that we know of"_; Sage is missing there... ;-)


---

Comment by drkirkby created at 2010-07-18 23:13:24

Replying to [comment:20 leif]:
> Replying to [comment:19 drkirkby]:
> > Any attempt to use ATLAS rather than CBLAS should be on another ticket.
> 
> I agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.
Agreed. but that should be on another ticket too. It is unrelated to the update of the package, and could potentially cause problems due to a change in the build order, if the deps file is not 100% OK. We still seem to be uncovering errors in that file with the parallel builds, so I'm not keen to do that change on this ticket. 

Dave


---

Comment by drkirkby created at 2010-07-19 01:38:34

Mike Hansen has reported that this builds on Cygwin, and all tests pass


```
> > If you export SAGE_CHECK=yes, the self-tests will run. So far they pass on
> > every system I've checked this on.
I forgot to post this yesterday, but I built it on Cygwin and all tests passed.

--Mike
```


It's now been tested on 
 * Cygwin
 * Linux
 * OpenSolaris
 * OS X
 * Solaris

Can this get a positive review? 

Dave


---

Comment by pjeremy created at 2010-07-19 22:27:00

sage-check also succeeds for mw on both FreeBSD-8.1/amd64 and Cygwin 1.7.5


---

Comment by drkirkby created at 2010-07-20 00:03:21

Also on the HP-UX operating system


```
-bash-4.0$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
```


on an old HP C3600 (552 MHz, big-endian PA-RISC processor)


```
The self-tests of GSL were successfully passed
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.3/spkg/build/gsl-1.14 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
No such file or directory: python
Finished installing gsl-1.14.spkg

real	30m47.515s
user	27m32.320s
sys	2m0.120s
```


So the GSL library has now been shown to build and pass all tests on:

 * Cygwin 
 * FreeBSD
 * HP-UX
 * Linux
 * OpenSolaris 
 * OS X 
 * Solaris

I wish all the code in Sage was as portable!

Dave


---

Comment by leif created at 2010-07-20 15:23:53

As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.
 * Dependencies: *None* - GSL does currently *not* depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`
 * Add a _"Special Update/Build Instructions"_ section that mentions that GSL could *in principle* use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).

Currently building Sage 4.5.1 with GSL 1.14 from scratch...

(I've already tested the spkg with 4.5 "final" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting "frame"work regarding parallel testing and timeouts on the slower machine...)


---

Attachment

Changes only to SPKG.txt (nothing to actual code). Reflects reviewer comments, and some extra information I thought was informative.


---

Comment by drkirkby created at 2010-07-20 17:10:04

Fix a silly typo


---

Attachment

Replying to [comment:26 leif]:
> As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.
>  * Dependencies: *None* - GSL does currently *not* depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`
>  * Add a _"Special Update/Build Instructions"_ section that mentions that GSL could *in principle* use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).
> 

Sure. I made a few other changes to that file too - hopefully to your approval. No code was changed. 

> Currently building Sage 4.5.1 with GSL 1.14 from scratch...

Good. 
 
> (I've already tested the spkg with 4.5 "final" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting "frame"work regarding parallel testing and timeouts on the slower machine...)

You do not surprise me with regard to the doctesting framework. However, before wasting any time on them, do check to see if there are any patches recently added to trac for this, as I know there were several such patches. I'm not the release manager, but if I were, I'd get those patches in on the alpha0. If you can't rely on the test code, what can you rely on? 

Dave


---

Comment by leif created at 2010-07-20 17:48:37

Oh, I actually took the _"val"_ as an abbreviation, and thought you did mean this one:
  _Force GSL to be buil*d* with no optimisation if SAGE_DEBUG is set to "yes"_

Maybe to your surprise, I'm ok with the rest. ;-)

(The only thing that could be clarified is _"64-bit builds"_ meaning 64-bit builds on systems where the compiler default is 32-bit, i.e. when `SAGE64` is "yes".)

Leif


---

Attachment

Clarify what are 64-bit builds


---

Comment by drkirkby created at 2010-07-20 18:11:47

I've updated SPKG.txt to make it clearer what are 64-bit builds. 

Package can be found here. 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg


---

Comment by leif created at 2010-07-20 19:43:49

I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: *Nothing! 8D*

(A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other _Sage packages_ that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)

The only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.
But since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an _additional_ run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS="$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas"` and then `make check`.)


---

Comment by leif created at 2010-07-20 21:03:11

Final `ptestlong` now running - will take nearly 4 hours...


---

Comment by drkirkby created at 2010-07-20 21:12:09

Replying to [comment:30 leif]:
> I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: *Nothing! 8D*
> 
> (A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other _Sage packages_ that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)
> 
> The only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.
> But since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an _additional_ run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS="$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas"` and then `make check`.)

I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket. 

Other tasks, *if* we tackle them, should be on another ticket. 

There are three related issues I am aware of

 * Sage ships with `blas-20070724.spkg` which is a BLAS library, and according to François Bissey, this is unnecessary, as we have ATLAS. http://groups.google.co.uk/group/sage-devel/msg/a75a7e796a5c3a91
 * We should be updating ATLAS. It was agreed to update ATLAS, and I said I would do it, but it far from a trivial affair. I need to discuss with Carl Witty how to build this in parallel. ATLAS takes about 8-10 hours to build in 't2' as there are no tuning parameters for that processor. 
 * I've got no idea what GSL is used for in Sage. If it's just special functions, which is quite possible, then its pointless worrying about it anyway. 

My biggest priority now is to get Sage working properly on OpenSolaris - it builds, but just dumps core as soon as one starts it. Hence I want to be able to verify the different parts of Sage are working - I'm less concerned if they are fully optimised. 

If I believe the tools on Solaris, starting Sage, before one gets to the 

```
sage:
```


prompt, there is already several memory leaks. I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. 

Dave


---

Comment by leif created at 2010-07-20 21:28:40

Replying to [comment:32 drkirkby]:
> Replying to [comment:30 leif]:
> > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: *Nothing! 8D* [...]
> 
> I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.

Yes, I agree. I only wanted to say that regarding GSL _nothing_ further has to be done - not even on a follow-up ticket.

> [...]
> I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. 

Agree on that, too. Removing unnecessary parts or extra upstream baggage and improving the documentation are other things I consider important, the former of course less.


---

Comment by drkirkby created at 2010-07-20 21:47:38

Replying to [comment:33 leif]:
> Replying to [comment:32 drkirkby]:
> > Replying to [comment:30 leif]:
> > > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: *Nothing! 8D* [...]
> > 
> > I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.
> 
> Yes, I agree. I only wanted to say that regarding GSL _nothing_ further has to be done - not even on a follow-up ticket.

Given what you have discovered, I suspect SPKG.txt in this package should be changed again. Can you suggest a set of changes. I'll then make sure the information is correct. 

Dave


---

Comment by leif created at 2010-07-20 22:56:30

Suggestion:

```patch
diff --git a/SPKG.txt b/SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
@@ -38,17 +38,15 @@

 == Dependencies ==

- * None - GSL does currently not depend on any other Sage package to 
-   compile, link and pass all GSL's self-tests. However, as of 
-   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps. 
+ * None - GSL 1.14 does not depend on any other Sage package to compile,
+   link and pass all of GSL's self-tests. Despite that fact, as of 
+   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps.
+   (It comes with its own CBLAS implementation that is e.g. used when running
+   the GSL test suite during installation; however, the Sage library only
+   uses it as a fall-back, if e.g. ATLAS's CBLAS library is not present.)

 == Special Update/Build Instructions ==
- * According to the GSL web page: http://www.gnu.org/software/gsl/
-   "GSL requires a BLAS library for vector and matrix operations. The 
-   default CBLAS library supplied with GSL can be replaced by the tuned 
-   ATLAS library for better performance". Exactly how one would use ATLAS is
-   not clear (there are no obvious options for the 'configure' script), 
-   but in principle it could be done. 
+ * Currently nothing special to be done.
```



---

Comment by leif created at 2010-07-20 23:05:21

Oh, I also changed the item regarding the addition of the _"Special Update/Build Instructions"_ section, which is missing above...


---

Comment by leif created at 2010-07-20 23:20:39


```diff

- * Added the "Special Update/Build Instructions" section from SPKG.txt which
-   was previously missing. 
+ * Added the "Special Update/Build Instructions" section to SPKG.txt which
+   was previously missing, though currently no special steps are required.

  * Added notes to SPKG.txt about an unnecessary ATLAS dependency in
-   $SAGE_ROOT/spkg/standard/deps
+   $SAGE_ROOT/spkg/standard/deps, and an explanation why GSL does *not*
+   depend on ATLAS.

- * Added notes to SPKG.txt about how ATLAS could in principle be used to 
-   improve the performance of some of GSL's functionality. 

- * Force GSL to be build with no optimisation if SAGE_DEBUG is set to "yes"
+ * Force GSL to be built with no optimisation if SAGE_DEBUG is set to "yes"
```

(This snippet looks a bit funny, but one should be able to see what I've changed in addition.)


---

Comment by leif created at 2010-07-20 23:54:07

Just found something else:

There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.


---

Comment by drkirkby created at 2010-07-21 07:32:37

Replying to [comment:38 leif]:
> Just found something else:
> 
> There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.

I disagree. Can you show me an example of how `[ -z $foobar ]` produces a syntax error, which can be solved by use of `[ -z "$foobar" ]`? I accept the quotes can do no harm, but I do not believe they are necessary. 

I need to go out soon - I look at the other changes later today. 

BTW, what was the result of your ptestlong? 

Dave


---

Attachment

Put quotes around CFLAG64 and SPKG_ROOT and update SPKG.txt to reflect discoveries about ATLAS


---

Comment by drkirkby created at 2010-07-21 11:27:34

Replying to [comment:39 drkirkby]:
> Replying to [comment:38 leif]:
> > Just found something else:
> > 
> > There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.
> 
I now accept you were right over this (someone else has [confirmed you were right on comp.unix.shell](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/8541f3ab19a1766b#)).  I've made what I think are all the changes you suggest now.

The package is at

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

Is that OK now? 

Dave


---

Comment by leif created at 2010-07-21 12:44:57

Well, this one:

```
 * Added notes to SPKG.txt about how ATLAS could in principle be used to
   improve the performance of some of GSL's functionality.
```

is still there, but never mind.

## Note to the release managers

*All patches here are to the spkg's repo, i.e. no patches have to be applied to the Sage library.*


---

Comment by leif created at 2010-07-21 12:44:57

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-07-21 13:16:19

Replying to [comment:41 leif]:
> Well, this one:
> {{{
>  * Added notes to SPKG.txt about how ATLAS could in principle be used to
>    improve the performance of some of GSL's functionality.
> }}}
> is still there, but never mind.

Thank you for the positive review. 

I thought I might as well fix it, so just removed that from SPKG.txt. 

Dave


---

Attachment

Remove a minor erro in the coments.


---

Comment by drkirkby created at 2010-07-21 13:19:56

## Note to the release managers
'''As Leif says above, all the patches here are in the package repository. Nothing is needed for the Sage library

The package can be found here.''' 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg


---

Comment by leif created at 2010-07-21 14:30:36

Replying to [comment:31 leif]:
> Final `ptestlong` now running - will take nearly 4 hours...

In addition to the numerous tests by others above, I've successfully tested the new package with both Sage 4.5 and 4.5.1 on Ubuntu 9.04 x86 and x86_64, gcc 4.3.3 and gcc 4.5.0, by installing the package as well as building Sage from scratch with it. (All `ptestlong`s passed.)


---

Comment by drkirkby created at 2010-07-21 23:55:42

## Note to the release managers

Perhaps this is stating it too many times, but better too often than too rare. 

The positively reviewed package can be found here.

 http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

No changes are needed to the Sage library - you do *not* t need to apply any of the patches on this ticket - they are all in the repository for the .spkg.


---

Comment by mpatel created at 2010-08-09 09:38:45

Resolution: fixed
