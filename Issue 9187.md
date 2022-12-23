# Issue 9187: Update ECL's spkg-install for building multiple spkgs in parallel

Issue created by migration from https://trac.sagemath.org/ticket/9187

Original creator: mpatel

Original creation time: 2010-06-08 08:42:58

Assignee: tbd

CC:  drkirkby jhpalmieri leif jsp

To build ECL with `SAGE_PARALLEL_SPKG_BUILD="yes"` on Mac OS X, we need to add, e.g.,

```sh
MAKEFLAGS=
export MAKEFLAGS
```

to the package's `spkg-install`.

Please see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).


---

Comment by mpatel created at 2010-06-08 09:15:26

I think we should work from #8951.


---

Comment by mpatel created at 2010-06-09 02:26:45

spkg patch.  Set empty `MAKEFLAGS`.


---

Comment by mpatel created at 2010-06-09 02:30:02

Changing status from new to needs_review.


---

Attachment

I've put a new spkg at

 * http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.4.1.p0.spkg

(Or should it be p1?)  This is based against the package mentioned in [comment:ticket:8951:10 this comment] at #8951.


---

Comment by drkirkby created at 2010-06-18 12:24:12

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2010-06-18 12:24:12

Unfortunately, there are two spkgs on #8951 and neither have the patches from #8089 and both claim in SPKG.txt to have things they do not. 

I intend creating a 10.4.1 package which has this, and all other relevant fixes in the one package. Since no ecl-10.4.1.spkg has been merged, this should be called ecl-10.4.1.spkg. The patch levels start at 0, not 1, but in this case as nothing has been merged, there is no need to increment the patch level. 

Please see #9264, which will have these changes, those which are listed as being in #8591 but are not, and also that at #8089

Dave


---

Comment by drkirkby created at 2010-06-18 17:05:57

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-18 17:05:57

The attached patch is ok and deserves positive review. However, the .spkg attached is not ideal, as it overlooks some other changes which need merging. I think a new .spkg needs to be created, which has all the minor changes together.


---

Comment by drkirkby created at 2010-06-21 08:55:49

There is no need to merge this now. 

#9264, which has positive review, includes this patch, along with several others related to ECL. All the relevant problems with ECL are solved by #9264, including this one. 

Dave


---

Comment by rlm created at 2010-06-25 11:18:33

Resolution: duplicate


---

Comment by mpatel created at 2010-07-12 01:29:44

Resolution changed from duplicate to 


---

Comment by mpatel created at 2010-07-12 01:29:44

Related tickets: #9264, #9460, #9474.


---

Comment by mpatel created at 2010-07-12 01:29:44

Changing status from closed to new.


---

Comment by mpatel created at 2010-07-12 20:27:15

spkg patch rebased vs. #9474.


---

Attachment

Here's a new spkg based on #9474:

 http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg

It works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.


---

Comment by jhpalmieri created at 2010-07-12 21:17:50

This works for me on sage.math and on an OS X box running 10.6, in both cases building spkg's in parallel.  I'm building on t2 now; if there are problems, I'll report them.


---

Comment by drkirkby created at 2010-07-12 21:29:47

Replying to [comment:9 mpatel]:
> Here's a new spkg based on #9474:
> 
>  http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg
> 
> It works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.

It works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok.


---

Comment by jhpalmieri created at 2010-07-12 21:50:56

Replying to [comment:11 drkirkby]:

> It works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok. 

That's what I meant, too.  The same is also true on t2 now: this version of ecl has built successfully as part of a parallel build, but the full build has several more hours to go...


---

Comment by cremona created at 2010-07-13 16:21:31

I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)


---

Comment by drkirkby created at 2010-07-13 16:38:30

Replying to [comment:13 cremona]:
> I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)

I think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. 

You also need to export MAKE, with something like

$ export MAKE="make -j6"

or however many threads you want. Do not put a space between the 'j' and the '6'. 

Dave


---

Comment by cremona created at 2010-07-13 16:41:17

Replying to [comment:14 drkirkby]:
> Replying to [comment:13 cremona]:
> > I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)
> 
> I think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. 
> 
> You also need to export MAKE, with something like
> 
> $ export MAKE="make -j6"
> 
> or however many threads you want. Do not put a space between the 'j' and the '6'.

Thanks -- I use -j 10, and luckily the machine is in an air-conditioned room!
 
> 
> Dave


---

Comment by drkirkby created at 2010-07-13 16:48:19

John, 

I'm not sure if you mis-understood me there. 

`$ export MAKE="make -j 10"`

will not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use 

`$ export MAKE="make -j10"`

I assume you are aware you also need a library patch

http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch

(only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 


Dave


---

Comment by cremona created at 2010-07-13 16:52:17

Replying to [comment:16 drkirkby]:
> John, 
> 
> I'm not sure if you mis-understood me there. 
> 
> `$ export MAKE="make -j 10"`
> 
> will not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use 
> 
> `$ export MAKE="make -j10"`

It's ok, I knew that...

> 
> I assume you are aware you also need a library patch
> 
> http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch
> 

... and that.  83 spkgs now installed and counting....

> (only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 
> 
> 
> Dave


---

Comment by jhpalmieri created at 2010-07-13 17:18:37

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-13 17:18:37

I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?


---

Comment by leif created at 2010-07-13 17:27:43

I think this ecl-10.2.1.p1.spkg can be merged into rc1, but could you MacOS X testers check which version of Boehm GC is used during install (i.e., the one shipped with Sage or the one included in ECL)?

```sh
$ grep -i boehm spkg/logs/ecl-10.2.1.p1.log | head -n 2
```

should show soemthing like

```
checking whether we can use the existing Boehm-Weiser library ... yes
checking if we need to copy GC private headers ... checking if we use Boehm-Demers-Weiser precise garbage collector... yes
```

or

```
checking if we use Boehm-Demers-Weiser precise garbage collector... yes
configure: Configuring included Boehm GC library:
```

(The latter is from Dave's install log on bsd.math/MacOS X 10.4.0.)


---

Comment by cremona created at 2010-07-13 17:28:39

Replying to [comment:18 jhpalmieri]:
> I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?

It finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!


---

Comment by jhpalmieri created at 2010-07-13 17:40:49

On my OS X box, it says:

```
checking if we use Boehm-Demers-Weiser precise garbage collector... yes
...
configure: Configuring included Boehm GC library:
```

I'm not an expert in these things, but in src/src/configure, it says:

```
        darwin*)
                thehost='darwin'
                shared='yes'
                ...
                # The Boehm-Weiser GC library shipped with Fink does not work
                # well with our signal handler.
                enable_boehm=included
```

which leads me to believe that on OS X, it will be a little work to use Sage's installation of boehm_gc.  I think this should go on a follow-up ticket, and it should probably be done in coordination with the ecl people.


---

Comment by jhpalmieri created at 2010-07-13 17:41:38

(That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)


---

Comment by leif created at 2010-07-13 17:51:17

Replying to [comment:22 jhpalmieri]:
> (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)

That's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.

I agree we should open a _new_ ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.

The package has to be cleaned up anyway, and perhaps we switch back to ECL 10.*4*.1.


---

Comment by rlm created at 2010-07-13 17:54:42

Replying to [comment:23 leif]:
> Replying to [comment:22 jhpalmieri]:
> I agree we should open a _new_ ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.

4.5.1.


---

Comment by leif created at 2010-07-13 18:03:22

Replying to [comment:24 rlm]:
> 4.5.1.

That's what I meant by _changing the milestone rather than the priority_. ;-)


---

Comment by cremona created at 2010-07-13 18:24:56

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-07-13 18:24:56

Replying to [comment:20 cremona]:
> Replying to [comment:18 jhpalmieri]:
> > I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?
> 
> It finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!

All tests passed == +++


---

Comment by rlm created at 2010-07-13 18:38:28

Merged

http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg


---

Comment by rlm created at 2010-07-13 18:38:28

Resolution: fixed


---

Comment by leif created at 2010-07-13 18:41:30

Replying to [comment:23 leif]:
> Replying to [comment:22 jhpalmieri]:
> > (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)
> 
> That's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.

Just for the record: The patch just avoids a dumb deprecation _error_(!), and it is already included in ECL's Boehm GC (otherwise ECL wouldn't have built on MacOS X 10.6).


---

Comment by leif created at 2010-07-13 19:58:55

For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):

```
leif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ du -ch src/msvc/ src/contrib/encodings/
16K	src/msvc/ecl
8.0K	src/msvc/gc
8.0K	src/msvc/gmp/mpz
32K	src/msvc/gmp/mpn/generic
76K	src/msvc/gmp/mpn/amd64i
48K	src/msvc/gmp/mpn/x86i/pentium4/sse2
32K	src/msvc/gmp/mpn/x86i/pentium4/mmx
92K	src/msvc/gmp/mpn/x86i/pentium4
48K	src/msvc/gmp/mpn/x86i/p6/mmx
8.0K	src/msvc/gmp/mpn/x86i/p6/p3mmx
128K	src/msvc/gmp/mpn/x86i/p6
300K	src/msvc/gmp/mpn/x86i
412K	src/msvc/gmp/mpn
12K	src/msvc/gmp/build.vc8/gen-fib
16K	src/msvc/gmp/build.vc8/gen-fac_ui
28K	src/msvc/gmp/build.vc8/lib_gmpxx
256K	src/msvc/gmp/build.vc8/dll_gmp_amd64
16K	src/msvc/gmp/build.vc8/gen-bases
372K	src/msvc/gmp/build.vc8/lib_gmp
240K	src/msvc/gmp/build.vc8/dll_gmp_p4
40K	src/msvc/gmp/build.vc8/lib_gmp_p0
36K	src/msvc/gmp/build.vc8/lib_gmp_p3
240K	src/msvc/gmp/build.vc8/dll_gmp_p0
180K	src/msvc/gmp/build.vc8/dll_mpfr
28K	src/msvc/gmp/build.vc8/gen-psqr
72K	src/msvc/gmp/build.vc8/lib_gmp_gc
40K	src/msvc/gmp/build.vc8/lib_gmp_p4
48K	src/msvc/gmp/build.vc8/lib_gmp_amd64
436K	src/msvc/gmp/build.vc8/dll_gmp_gc
240K	src/msvc/gmp/build.vc8/dll_gmp_p3
208K	src/msvc/gmp/build.vc8/lib_mpfr
4.8M	src/msvc/gmp/build.vc8
5.2M	src/msvc/gmp
8.0K	src/msvc/c
16K	src/msvc/util
12K	src/msvc/doc
5.3M	src/msvc/
544K	src/contrib/encodings/
5.8M	total
leif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ tar cj src/msvc/ src/contrib/encodings/ | wc -c
859300
```



---

Comment by drkirkby created at 2010-07-13 20:23:44

Replying to [comment:29 leif]:
> For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):

That's up to Robert, but I tend to feel saving about 840 KB is of relatively low importance, and can be left for 4.5.1. Especially considering there is a new version of ECL available, and we would expect to resolve the ECL/Maxima issues some time in the near future. So the ecl package will probably be updated for 4.5.1. 

Dave


---

Comment by rlm created at 2010-07-13 21:47:21

Replying to [comment:29 leif]:
> For a 4.5 final, we should remove the unnecessary baggage

Please open a ticket and make a p2 with only these changes. I think it's too late for 4.5.


---

Comment by leif created at 2010-07-14 00:09:24

Replying to [comment:31 rlm]:
> Replying to [comment:29 leif]:
> > For a 4.5 final, we should remove the unnecessary baggage
> 
> Please open a ticket and make a p2 with only these changes. I think it's too late for 4.5.

Ticket up at #9493.

I unfortunately cannot upload an spkg because I don't have an account on sage.math.

(Perhaps I'll ask again someone to upload it from an e-mail attachment, but it's still fairly large.)
