# Issue 8059: update Singular SPKG to newest upstream release

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2010-01-25 19:05:12

Assignee: tbd

CC:  polybori drkirkby alexghitza jsp fbissey alexanderdreyer

The Singular team accepted most of our patches upstream. They are in the 3-1-0-9 release, which also is a first step to make things easier for library developers.


---

Comment by malb created at 2010-01-25 19:07:15

Here's the new SPKG:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.spkg

You also need to apply the patch I am going to upload in a second.

 * CCing Dave so we can make sure there is no regression w.r.t. Solaris etc. 
 * CCing PolyBoRi so Michael can take a look at my changes (he knows the code base)
 * CCing Alex since he reviewed Singular SPKGs before :)


---

Attachment


---

Comment by malb created at 2010-01-25 19:07:40

Changing status from new to needs_review.


---

Comment by malb created at 2010-01-25 19:36:43

*Doctests on sage.math*:

The only failure is in gen.pyx. I don't see how this can be caused by my changes.


```
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.1/devel/sage/sage/libs/pari/gen.pyx", line 2950:
    sage: pari(sqrt(2)).frac()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_77[3]>", line 1, in <module>
        pari(sqrt(Integer(2))).frac()###line 2950:
    sage: pari(sqrt(2)).frac()
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/functions/other.py", line 812, in sqrt
        return x.sqrt(*args, **kwds)
      File "integer.pyx", line 4440, in sage.rings.integer.Integer.sqrt (sage/rings/integer.c:25864)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/functions/other.py", line 755, in _do_sqrt
        z = SR(x) ** one_half
      File "expression.pyx", line 2218, in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11255)
      File "integer.pyx", line 1603, in sage.rings.integer.Integer.__pow__ (sage/rings/integer.c:11625)
      File "rational.pyx", line 2082, in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15560)
    ImportError: /mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/symbolic/power_helper.so: failed to map segment from shared object: Cannot allocate memory

**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.1/devel/sage/sage/libs/pari/gen.pyx", line 2977:
    sage: pari(sqrt(-2)).imag()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_78[3]>", line 1, in <module>
        pari(sqrt(-Integer(2))).imag()###line 2977:
    sage: pari(sqrt(-2)).imag()
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/functions/other.py", line 812, in sqrt
        return x.sqrt(*args, **kwds)
      File "integer.pyx", line 4424, in sage.rings.integer.Integer.sqrt (sage/rings/integer.c:25709)
      File "/mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/functions/other.py", line 755, in _do_sqrt
        z = SR(x) ** one_half
      File "expression.pyx", line 2218, in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11255)
      File "integer.pyx", line 1603, in sage.rings.integer.Integer.__pow__ (sage/rings/integer.c:11625)
      File "rational.pyx", line 2082, in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15560)
    ImportError: /mnt/usb1/scratch/malb/sage-4.3.1/local/lib/python/site-packages/sage/symbolic/power_helper.so: failed to map segment from shared object: Cannot allocate memory
```



---

Comment by malb created at 2010-01-25 19:38:17

Also, the same doctest passes for me locally, so I will assume for now that this has nothing to do with my patch (famous last words, I know).


---

Comment by AlexGhitza created at 2010-01-26 00:34:58

I'm testing this on a couple of machines and will report.

I have two questions about the spkg:

1. Should we remove dist/, see #5903 ?
2. In src/, should we remove doc/ and emacs/ ?  It's really just a question of making the spkg smaller by about 10%, since AFAIK these won't get used from Sage.  We routinely do this with other spkgs.

I'm happy to do this and post a new spkg, but I wanted to see what Martin thought about it.


---

Comment by malb created at 2010-01-26 00:55:47

Replying to [comment:6 AlexGhitza]:
> I have two questions about the spkg:
> 
> 1. Should we remove dist/, see #5903 ?

Yes, that sounds reasonable.

> 2. In src/, should we remove doc/ and emacs/ ?  It's really just a question of making the spkg smaller by about 10%, since AFAIK these won't get used from Sage.  We routinely do this with other spkgs.

I just checked and it still builds with these two directories removed. 

Thus, I've updated the SPKG accordingly. Same place, same name.


---

Comment by PolyBoRi created at 2010-01-26 08:12:47

I did not have any time to test it.
But most changes introduce passing the ring explicitly to Singular.
This avoid current ring problems (which can be quite annoying and hard to debug).

nlGetNumerator seems a new addition in Singular (maybe, a special wish of Martin?).

Cheers,
Michael


---

Comment by malb created at 2010-01-26 08:27:28

Replying to [comment:8 PolyBoRi]:
> I did not have any time to test it.
> But most changes introduce passing the ring explicitly to Singular.
> This avoid current ring problems (which can be quite annoying and hard to debug).

Yep, that's a great direction things are developing.
 
> nlGetNumerator seems a new addition in Singular (maybe, a special wish of Martin?).

It's just `nlGetNom` renamed


---

Comment by PolyBoRi created at 2010-01-26 08:35:58

Then, what I can still comment are wild casts like

```
<napoly*>pNext(<poly*>z)
```

But they are also okay as napoly is just a typedef for polyrec*.
So, from reading Malbs code, it looks good.
Still someone needs to test it and check it for Sages formal criteria


---

Comment by AlexGhitza created at 2010-01-26 10:37:58

Replying to [comment:7 malb]:
> I just checked and it still builds with these two directories removed. 
> 
> Thus, I've updated the SPKG accordingly. Same place, same name.

Unless I am looking at the wrong SPKG, you forgot to take `dist/` out of version control:


```
[ghitza`@`cartan singular-3-1-0-9-20100125]$ hg status
! dist/debian/changelog
! dist/debian/compat
! dist/debian/control
! dist/debian/control.in
! dist/debian/copyright
! dist/debian/libsingular-dev.install
! dist/debian/libsingular0.install
! dist/debian/patches/change-library-search-path.patch
! dist/debian/patches/sage-bugfixes.patch
! dist/debian/patches/series
! dist/debian/rules
! dist/debian/singular.install
```


Apart from this, I'm happy.


---

Comment by malb created at 2010-01-26 15:05:20

Replying to [comment:10 PolyBoRi]:
> Then, what I can still comment are wild casts like
> But they are also okay as napoly is just a typedef for polyrec*.

There used to be a `naIter` function which is gone in 3-1-0-9 and Singular internally uses `pNext()` as well. Thus I feel my casting is justified :)


---

Comment by malb created at 2010-01-26 15:09:05

> Unless I am looking at the wrong SPKG, you forgot to take `dist/` out of version control:

fixed. Is that a positive review then?


---

Comment by AlexGhitza created at 2010-01-26 20:59:10

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-26 20:59:10

Yes.


---

Comment by jsp created at 2010-01-28 22:40:09

As is the spkg failed to build on Open Solaris x64 with SAGE64=yes.



```
g++ -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -DHAVE_CONFIG_H -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include  -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -O3 -g -fPIC -o cf_factor.o
In file included from /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include/NTL/vec_ZZ.h:5,
                 from /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include/NTL/ZZX.h:5,
                 from /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include/NTL/ZZXFactoring.h:5,
                 from NTLconvert.h:23,
                 from cf_factor.cc:33:
/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include/NTL/ZZ.h: In function ‘long int NTL::MulModPrecon(long int, long int, long int, long unsigned int)’:
/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include/NTL/ZZ.h:1795: error: ‘MulHiUL’ was not declared in this scope
make[2]: *** [cf_factor.o] Error 1
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.2.alpha0/spkg/build/singular-3-1-0-9-20100125/src/factory'
make[1]: *** [install] Error 1
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.2.alpha0/spkg/build/singular-3-1-0-9-20100125/src'
make: *** [/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.

real	0m24.240s
user	0m12.235s
sys	0m9.934s
sage: An error occurred while installing singular-3-1-0-9-20100125

```



Maybe it will install a some FLAGS are set globally (-m64) in this case).

As Open Solaris is not a supported platform I'll not interfere with the positive review.

Jaap


---

Comment by AlexGhitza created at 2010-01-28 23:41:42

Jaap,

Did the previous Singular spkg build properly on Open Solaris?  If so, I wonder if it's just a problem in spkg-install, or a more serious issue with Singular itself.


---

Comment by jsp created at 2010-01-28 23:45:17

If CFLAGS and friends are set tight. Building on Open Solaris fails on



```
gcc -g -pg -O3 -I. -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -O2 -g -m64 -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -DHAVE_CONFIG_H -c omBinPage.c -o omBinPage.op
/var/tmp//ccciayz2.s: Assembler messages:
/var/tmp//ccciayz2.s:31: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:110: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:183: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:270: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:477: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:805: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:1240: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:1718: Error: junk ``@`' after expression
/var/tmp//ccciayz2.s:2041: Error: junk ``@`' after expression
make[2]: *** [omBinPage.op] Error 1
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.2.alpha0/spkg/build/singular-3-1-0-9-20100125/src/omalloc'
make[1]: *** [install] Error 1
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.2.alpha0/spkg/build/singular-3-1-0-9-20100125/src'
make: *** [/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.

```


Actually this is the same failure I had before.

What is the use of -gp in building singular for sage?

If I remove -gp in Makefile and Makefile.in all, over singular builds on
Open Solaris x64 64 bit

Jaap


---

Comment by jsp created at 2010-01-28 23:45:17

Remove assignee tbd.


---

Comment by jsp created at 2010-01-28 23:47:17

Replying to [comment:16 AlexGhitza]:
> Jaap,
> 
> Did the previous Singular spkg build properly on Open Solaris?  If so, I wonder if it's just a problem in spkg-install, or a more serious issue with Singular itself.
> 

The -gp flag leads to problems on Open Solaris.

Jaap


---

Comment by malb created at 2010-01-28 23:56:23

`man gcc` says:


```
-pg Generate extra code to write profile information suitable for the analysis program gprof.  You must use this option when compiling the source files you want data about, and you must also use it when linking.
```


so this shouldn't be used by default anyway.


---

Comment by jsp created at 2010-01-28 23:59:25

Replying to [comment:19 malb]:
> `man gcc` says:
> 
> {{{
> -pg Generate extra code to write profile information suitable for the analysis program gprof.  You must use this option when compiling the source files you want data about, and you must also use it when linking.
> }}}
> 
> so this shouldn't be used by default anyway.

+1

Thanks.

Jaap


---

Comment by AlexGhitza created at 2010-01-29 00:18:43

Martin, do you want to remove this option in the spkg?  I'd be happy to do some test builds to make sure that it doesn't break anything on other architectures.  But if the fix is this simple to make it build on Open Solaris, we might as well do it now.


---

Comment by jsp created at 2010-01-29 00:23:54

Replying to [comment:21 AlexGhitza]:
> Martin, do you want to remove this option in the spkg?  I'd be happy to do some test builds to make sure that it doesn't break anything on other architectures.  But if the fix is this simple to make it build on Open Solaris, we might as well do it now.

I think it need upstream work. In the former release it was in patches.
Now it is in source :(

Removing -gp will not break anything in sage. We do no profiling!

Jaap


---

Comment by malb created at 2010-01-29 00:28:01

Looking at Jaap's error again it comes from omalloc. For omalloc all targets are built which are
 * libomalloc (normal)
 * libomalloc_ndebug (no debugging symbols)
 * libomalloc_p (for profiling)

We shouldn't mess with the `-pg` switch but should convince omalloc's autotools not to build the profiling version on top of the other two.


---

Comment by jsp created at 2010-01-29 00:33:34

One more comment. Only developers of a program or other software can put interest in
profiling there product.

So once more: let's ask upstream to remove this option.

For now it is an option to introduce some patches again in the spkg-install :(


Shall we set status to needs work?

Jaap


---

Comment by drkirkby created at 2010-01-29 06:43:04

I would also add I think adding profiling information by default is a bad idea. 
 
 * Adding profiling information will slow the code quite considerably.
 * The -pg option is not portable, so it would hamper efforts to build with a non-GNU compiler.
 * The purposely add an option which is breaking a build on Open Solaris, when an Open Solaris port is in progress, seems a bad idea. 
 * As Jaap points out, only developers want this information - not end users. 

I would be tempted to set it to 'needs work', but feel I can't really do so, since Open Solaris is not supported on Sage. So the fact an option breaks on an unsupported operating system is not a sufficiently good reason for rejecting it. But I would urge the person that created the ticket, or the reviewer to do so. (BTW, the Reviewer field is not filled in). 

Dave


---

Comment by malb created at 2010-01-29 09:47:57

Changing status from positive_review to needs_work.


---

Comment by malb created at 2010-01-29 09:47:57

Guys,

no one wants to add -pg to the default options for Singular and no one did! Most Singular libraries are built in several flavours as explained above but not all of them are used of course. It's the build of an unused library that is going wrong.

There is a discussion on this issue on [libsingular-devel]:

  http://groups.google.com/group/libsingular-devel/browse_thread/thread/43d157fe730e8798

where Hans Schönemann suggested to patch omalloc. It is still puzzling why the build breaks now since IIRC nothing changed in that area.


---

Comment by malb created at 2010-02-01 01:01:53

Is anybody working on patching the Makefiles? It might take a few days before I'll get around to do it.


---

Comment by jsp created at 2010-02-05 14:51:12

Replying to [comment:27 malb]:
> Is anybody working on patching the Makefiles? It might take a few days before I'll get around to do it.

Are you getting around to do it?

Jaap


---

Comment by malb created at 2010-02-05 14:54:01

Not yet, feel free to go ahead ;)


---

Comment by malb created at 2010-02-09 17:21:31

I thought about this patch-all-Makefiles approach some more. I came to the conclusion that it would be a bad idea. Jaap's GCC or the Singular's configuration script is broken. GCC accepts `-pg` and that GCC what is called. That it fails hints at either a bug in the OpenSolaris GCC or at a problem choosing the right assembler or linker. 

Patching all Makefiles would have serious repercussions: this patch would never be accepted upstream and thus we would have to go through a very tedious and error-prone process of patching every Makefile with every SPKG update. Since I am right now the only person who does these updates at the moment, I think I refuse to increase my workload like this based on one faulty setup. 

Note that I am happy to investigate and push upstream any fix which triggers this error in the configuration script. I want Sage to build and work on OpenSolaris and Solaris. It's just this approach which I deem incorrect.


---

Comment by drkirkby created at 2010-02-09 23:44:58

If there are a lot of Makefiles, then patching would be tedious and require more work with upgrades. However, it should not be too hard to create a small script which patches the Makefiles and call that script from spkg-install. 

I've not checked this on the Singular sources, but this sed script, which I called 'nopg' could be used to replace ' -pg ' with nothing

{{{#!/bin/sh 
sed 's/ -pg //g' $1 > /tmp/Makefile-without-pg-option.$$
mv /tmp/Makefile-without-pg-option.$$  $1
```


then in spkg-install have:


```
find src -name Makefile -exec /path/to/nopg {} \;
```


I tried it on a gcc source distribution, which has loads of 'configure' scripts, replacing 'echo' with 'zzzzzzzzzzzzzzzzz' and sure enough, all the configure script have strings of zzzzz's in them. 


It would be necessary to check the files have the required changes, and no other changes, but that should be a simple solution. 

Dave 

Dave


---

Comment by drkirkby created at 2010-02-09 23:47:45

PS, the substitution would be from ' -pg ' to nothing at all, so it would not break if files in the makefile have -pg in their names.


---

Comment by malb created at 2010-02-10 00:35:42

That indeed might be a viable solution. However, we should still investigate what exactly breaks Jaap's setup instead of working around the issue which we don't understand.


---

Comment by malb created at 2010-02-10 13:33:05

A new SPKG is available at #8228, you will need the attached patch for this ticket to make it work.


---

Comment by malb created at 2010-03-03 12:53:45

I vote to review 3-1-0-9 without considering Jaap's bug and then opening a new ticket where Jaap gives more details so that we can address the bug. Right now, Sage crashes in a fairly basic situation and we thus should upgrade.


---

Comment by AlexGhitza created at 2010-03-03 13:21:17

Martin, this is probably not the question you want to hear, but: would it be worth it to go straight to 3-1-1, since it was just released?


---

Comment by malb created at 2010-03-03 13:45:05

Replying to [comment:36 AlexGhitza]:
> Martin, this is probably not the question you want to hear, but: would it be worth it to go straight to 3-1-1, since it was just released?

I'll make you a deal: if you review it I'll make a Singular-3-1-1 SPKG :)


---

Comment by AlexGhitza created at 2010-03-03 22:31:57

Fine, I'll take that.  I should be able to do it this weekend.


---

Attachment


---

Comment by malb created at 2010-03-05 13:25:24

A new SPKG is available at

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-0-20100305.spkg


---

Comment by malb created at 2010-03-05 13:26:03

There are doctest failures in the scheme subdirectory. I reported one bug upstream already.


---

Comment by malb created at 2010-03-05 14:31:55

Doctest failures:


```
The following tests failed:

        sage -t  devel/sage/sage/schemes/plane_curves/projective_curve.py # 14 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/curve.py # 6 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 6 doctests failed
```



---

Comment by malb created at 2010-03-05 14:40:19

After fixing a typo in a Singular routine

  http://groups.google.com/group/libsingular-devel/browse_frm/thread/de4c7123c71f2150

I get a bit further, but I need some help now:

I assume '32' is wrong in the failure below?


```python
sage -t  "devel/sage/sage/schemes/plane_curves/constructor.py"
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage/sage/schemes/plane_curves/constructor.py", line 72:
    sage: C.genus()
Expected:
    0
Got:
    32
```



Am I correct that the following is also wrong?


```python
sage -t  "devel/sage/sage/schemes/plane_curves/curve.py"
   ? ideal defines not a curve
   ? leaving normal.lib::genus
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage/sage/schemes/plane_curves/curve.py", line 79:
    sage: C.geometric_genus()
```



---

Comment by malb created at 2010-03-05 14:48:21

The different behaviour in pure Singular:


```c
> ring r = 7,(x,y),dp;
> LIB("normal.lib");
> ideal i = x^10 + x^3 + y^2;
> genus(i);
32
```



---

Comment by AlexGhitza created at 2010-03-07 01:14:09

Martin, I just tried the new spkg but I'm running into trouble very quickly: after doing `sage -f ...`, I'm getting errors when doing `sage -b`

This is under sage-4.3.4.alpha0, and I got it now on two machines (including sage.math)


---

Comment by malb created at 2010-03-07 12:54:34

Did you apply `singular-3-1-1-0.patch`?


---

Comment by AlexGhitza created at 2010-03-08 02:49:41

Hmmm  that's pretty embarrassing.

So it builds fine now.  Note that applying the patch to either 4.3.3 or 4.3.4.alpha0 results in one rejection.  It is actually harmless, but it might be good to rebase anyway.

I'm pretty sure that the (geometric) genus should be 0 in the doctest that fails claiming it's 32.  (In particular, both Macaulay2 and Magma say 0.)

I guess this should be reported upstream, since they know better what they've changed since 3-1-0-9 in normal.lib.


---

Comment by malb created at 2010-03-08 23:00:55

The bug I isolated above will be fixed in the next release:


```
Hi Martin,

Thank you for reporting this bug.
It will be corrected in the next release.

Gert-Martin


2010/3/8 Martin Albrecht <malb`@`informatik.uni-bremen.de>:
> Hi,
>
> the following output is wrong in 3-1-1-0 and was correct in the previous
> version:
>
>> ring r = 7,(x,y),dp;
>> LIB("normal.lib");
>> ideal i = x^10 + x^3 + y^2;
>> genus(i);
> 32 //should be 0
```


We should try to make sure that we report all bugs (I think there is another one were curves are considered not to be curves) before they cut the new release.


---

Comment by AlexGhitza created at 2010-03-09 11:32:53

> We should try to make sure that we report all bugs (I think there is another one were curves are considered not to be curves) before they cut the new release.

Yep.  If I have some time (cross fingers) I'll try to test 3-1-1-0 with a few more examples and see if I catch anything else.  Any idea what the timeline is for the new release?


---

Comment by malb created at 2010-03-09 11:35:17

No idea, but I just reported another bug upstream:


```c
> ring r = 5,(x,y,z),dp;
> ideal i = -x^3 + y^2*z - 2*x*z^2 + y*z^2;
> LIB("normal.lib");
> genus(i);
   ? ideal defines not a curve
   ? leaving normal.lib::genus
```


Another thing we might want to tackle is that it seems that our libsingular interface isn't very good at recovering from errors. I'm not sure how to address this; I guess I'll ask upstream some time.


---

Comment by malb created at 2010-03-09 14:38:29

Reply from upstream:


```
This is not a bug, Singular computes only the genus
of a curve, as is said in the manual:

genus(i) or genus(i,1); I a 1-dimensional ideal

In the example the ideal defines a surface.
Gert-Martin

2010/3/9  <owner-singular-team`@`mathematik.uni-kl.de>:
> #212: wrong computation of genus / error when calling genus
> --------------------------------------------------------------+-------------
>  Reporter:  Martin Albrecht <malb`@`…                           |       Owner:  somebody
>     Type:  defect                                            |      Status:  new
>  Priority:  minor                                             |   Milestone:  Releases 3-1-1 and higher
> Component:  singular-libs                                     |     Version:  3-1-1
>  Keywords:  genus                                             |
> --------------------------------------------------------------+-------------
>
> Comment(by seelisch):
>
>  Here's another bug related to genus:
>
>  > ring r = 5,(x,y,z),dp;
>  > > ideal i = -x3 + y2*z - 2*x*z2 + y*z2;
>  > > LIB("normal.lib");
>  > > genus(i);
>    ? ideal defines not a curve
>    ? leaving normal.lib::genus
```



Alex, can you look into this?


---

Comment by malb created at 2010-03-09 22:12:58


```
Dear Martin,

I realize that the example was a homogeneous
polynomial in 3 variables. So, this can be interpreted
as an affine surface but also as a homogeneous curve.

Probably the second was meant. In this case it makes
sense to compute the genus. We shall take care
about this in the next release.

Best,
Gert-Martin
```



---

Comment by malb created at 2010-06-02 18:44:21

There's a new Singular version at

   http://www.mathematik.uni-kl.de/ftp/pub/Math/Singular/SOURCES/3-1-1/

which might or might not fix the bug


---

Comment by malb created at 2010-07-10 14:11:37

I've updated the Singular SPKG to 3-1-1-3 which fixes the genus issue. However, this release segfaults a lot! I'm in the process of resolving this (cf. [libsingular-devel])

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-3.p0.spkg


---

Comment by drkirkby created at 2010-07-10 20:44:38

Replying to [comment:53 malb]:
> I've updated the Singular SPKG to 3-1-1-3 which fixes the genus issue. However, this release segfaults a lot! I'm in the process of resolving this (cf. [libsingular-devel])
> 
> http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-3.p0.spkg

Hi Martin Albrecht , 
A few comments. 

 * Is it possible you could request the upstream developers distribute the source code so the files generated by tools like autoconf, flex, actually have later modification times of the generated file newer than the file they are generated from? 

Currently libparse.cc, which is the output from 'flex' has exactly the same modification time (to the ns) as the file it was supposedly generated from (libparse.l). I doubt 'flex' actually run in < 1 ns!


```
-rw-r-----   1 drkirkby staff     109422 2010-02-03 13:58:03.000000000 +0000 src/Singular/libparse.cc
-rw-r-----   1 drkirkby staff      30875 2010-02-03 13:58:03.000000000 +0000 src/Singular/libparse.l
```

Likewise for these files. Clearly autoconf did not run in under a ns. 

```
-rwxr-x---   1 drkirkby staff      85614 2010-03-03 11:36:23.000000000 +0000 src/factory/configure
-rw-r-----   1 drkirkby staff      13992 2010-03-03 11:36:23.000000000 +0000 src/factory/configure.in
```


This will save us having to 'touch' the files. 

 * There's a problem with the `build()` part of spkg-install. 

The script author probably assumes that if any one of the items in `build()` fail, then `build()` will fail and so the error will be reported. However, that is not the case. As long as the last item in `build()`, which is (`install_docs`), does not fail, the return code from `build()` will be 0. So if for example I modify the `build()` section to:


```
build()
{
    clean_headers
    # This SHOULD break the build
    rm /non-existant-file

    patch

    distclean

    config 

    build_singular

    build_libsingular
 
    build_factory

    build_libfac

    create_singular_script

    install_docs
}

build

if [ $? -ne 0 ]; then
    echo "Error somewhere building Singular."
    exit 1
fi

```


then when I build Singular, I see:


```
Building a 64-bit version of Singular
rm: /non-existant-file: No such file or directory
make: *** No rule to make target `distclean'.  Stop.
creating cache ./config.cache
checking uname for singular... ix86-SunOS
checking for gcc... gcc -m64
...
Successfully installed singular-3-1-1-3.p1
```


In other words, the error of trying to delete  /non-existant-file does not cause the build to fail, as it should do. That means if the library fails to build, but the docuemtation installs ok, then the script will not show the error. Each part should be checked individually. 

I've not checked this, but believe the following would work:


```
build()
{
   for i in clean_headers patch distclean config build_singular build_libsingular build_factory build_libfac create_singular_script install_docs ; do
   $i
   if [ $? -ne 0 ]; then
     echo "Error building Singular when running '$i'."
     exit 1
   fi
   done
}
```


 * There are in fact a lot of parts in spkg-install which are not checked for errors. 

 * François Bissey has said the previous version of Singular built some unnecessary targets, which adds to the build time of Singular. Given this is the longest package to build (taking almost 6 minutes on my PC), it would be worth reducing them if you have not already done so. I've cc'ed François on the ticket, as he knows a lot more about this package than me. 

 * It does built on OpenSolaris, though I've not checked it on anything else. I'll wait until you have sorted out the segfaults first!

PS, The first 3-1-1-3 to go into Sage should be called singular-3-1-1-3.spkg and not have a '.p0' in the name. 

Dave


---

Comment by fbissey created at 2010-07-10 22:54:41

Thanks for adding me Dave I will update my patch to simplify slightly
the build to this version of singular. I know from experience in sage-on-gentoo
that sage will build and the tests will be ok if you remove the build_factory
and build_libfac targets. 
As a bonus the creation of the link LIB to lib is 1) bogus 2) useless.
In a build of singular LIB usually contains the the *.lib files. Those files
are installed in share/singular thanks to some of the instructions in the build.
Before being removed and recreated the link actually points to share/singular.
Removing the link didn't harm any tests.

The only issue with removing these 2 targets may be the optional Macaulay2
spkg. We have some discussions atm in gentoo about singular - the components
it provides - and Macaulay2. So while sage builds ok, Macaulay2 should be checked.


---

Comment by drkirkby created at 2010-07-11 08:56:17

Replying to [comment:53 malb]:
> I've updated the Singular SPKG to 3-1-1-3 which fixes the genus issue. However, this release segfaults a lot! 

Hi Martin, 

do you see this warning message about `warning: returning reference to temporary`? I got that warnings when building on OpenSolaris - see below. 


```
g++ -m64 -O2 -g -m64 -fPIC -pipe -fno-implicit-templates -I. -I../kernel -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -O2 -g -m64 -DNDEBUG -DOM_NDEBUG -Dix86_SunOS -DHAVE_CONFIG_H -c iparith.cc
In file included from ../kernel/ring.h:13,
                 from subexpr.h:16,
                 from ipid.h:13,
                 from iparith.cc:20:
../kernel/polys-impl.h:177:1: warning: "pPolyAssumeReturn" redefined
../kernel/polys-impl.h:176:1: warning: this is the location of the previous definition
In file included from ../kernel/walkMain.h:5,
                 from ../kernel/walkProc.h:3,
                 from iparith.cc:56:
../kernel/int64vec.h: In member function 'const int& int64vec::operator[](int) const':
../kernel/int64vec.h:51: warning: returning reference to temporary
```


That sounds the sort of error which could result in segfaults. 

I'm attaching a patch which gives much improved error checking.

Dave


---

Comment by drkirkby created at 2010-07-11 09:08:19

Based on Martin's singular-3-1-1-3 package, but with improved error checking.


---

Attachment

I just realised I copied a bit too little of that warning message. The message is about returning reference to temporary memory:


```
../kernel/int64vec.h:51: warning: returning reference to temporary memory
```


That looks like it could result in segfaults to me. 

Dave


---

Attachment

Simplify the building of singular


---

Comment by malb created at 2010-07-11 12:51:44

> The only issue with removing these 2 targets may be the optional Macaulay2 spkg. We > have some discussions atm in gentoo about singular - the components it provides - 
> and Macaulay2. So while sage builds ok, Macaulay2 should be checked.

I'm pretty sure Macaulay2 will fail if we drop libfac and libcf. Thus I'm not applying the second patch for now.


---

Comment by malb created at 2010-07-11 12:58:05

I've applied David's patch to 

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-3.spkg

and also changed the name in accordance with his comments. I've also forwarded David's comments to the Singular team at:

http://groups.google.com/group/libsingular-devel/browse_thread/thread/e67e6b2afe1d8314


---

Comment by drkirkby created at 2010-07-11 21:51:02

Replying to [comment:58 malb]:
> > The only issue with removing these 2 targets may be the optional Macaulay2 spkg. We > have some discussions atm in gentoo about singular - the components it provides - 
> > and Macaulay2. So while sage builds ok, Macaulay2 should be checked.
> 
> I'm pretty sure Macaulay2 will fail if we drop libfac and libcf. Thus I'm not applying the second patch for now.

It would be good if this Macaulay2 could be made to rebuild Singular in this case. Perhaps have an environment variable that determines if those two targets are built or not. 

```
build() 
{
    patch
    distclean
    config 
    build_singular
    build_libsingular
    if [ "x$SAGE_USING_Macaulay2" = xyes  ] ; then  
       build_factory
       build_libfac
    fi
    create_singular_script
    install_docs
} 
```

Then ensure Macaulay2 

 * exports SAGE_USING_Macaulay2 = "yes"
 * Rebuilds Singular. This time build_factory & build_libfac would built, due to the environment variable being set to "yes"

I guess this depends on the popularity of Macaulay2. If 20% of people install it, then we might as well build all targets. If however only 1% of people install Macaulay2, then I doubt it warrants slowing the build process for everyone. 

Currently I believe Singular is the slowest package to build in Sage (at least on my OpenSolaris machine), though neither R or Maxima are building, so I can't say for sure. But Singular definately takes a long time to build, so if that could be improved, it would be nice. Of course, it depends on how long those targets take to build. If the savings from not building them are only small, we might as well build them. 

Another option might be to let an environment variable be used to stop those two targets building, but by default build them all. 

Dave


---

Comment by fbissey created at 2010-07-11 21:59:26

To build both singular and Macaulay2 our current approach
is too try to build omalloc factory and libfac first, and then move on to the 
rest of singular/Macaulay2. That approach makes sense in the context of Gentoo.
If it works I may try to adapt the singular spkg build process to match it.

It is not a done deal that this approach will work however.

Francois


---

Comment by malb created at 2010-07-12 15:17:42

If you don't mind I'd suggest to open a new ticket to address the libfac issue (by including libfac in the Macaulay SPKG for example). Right now, we have crashes in Sage because of bugs in older versions of Singular and I'd like to focus on fixing those for now. With the updated patch I'll attach in a minute, I'm down to two doctest failures with the most recent Singular version:


```
sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 3 doctests failed
sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_element.py # 4 doctests failed
```



---

Comment by drkirkby created at 2010-07-12 16:06:34

Replying to [comment:62 malb]:
> If you don't mind I'd suggest to open a new ticket to address the libfac issue (by including libfac in the Macaulay SPKG for example). 

No problem. That makes sence. 

Dave


---

Attachment

fixed many SIGSEGVs


---

Comment by malb created at 2010-07-12 22:57:54

I've updated the singular-3-1-1-3.spkg according to Hans' comments on [libsingular-devel] and reverted some overly aggressive changes to singuler-3-1-1-3.patch. With this I'm down to one problem:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  

**********************************************************************

File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/rings/polynomial/toy_d_basis.py", line 38:

sage: gb = d_basis(I); gb

Expected:

[x - 2020, y - 11313, 22627]

Got:

[1]

**********************************************************************

File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/rings/polynomial/toy_d_basis.py", line 41:

sage: gb[-1].factor()

Expected:

11^3 * 17

Got:

1

**********************************************************************

File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/rings/polynomial/toy_d_basis.py", line 208:

sage: gb = d_basis(I); gb

Expected:

[x - 2020, y - 11313, 22627]

Got:

    [1]
```



---

Comment by malb created at 2010-07-15 17:12:34

Changing status from needs_work to needs_review.


---

Attachment

The Singular team cut us a new release which

 * passes all doctests on sage.math
 * supports parallel make

The SPKG is at

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.spkg


---

Comment by malb created at 2010-07-15 17:19:45

*On sage.math:*

*make -j 20*


```
real    3m55.543
user    8m10.720
sys     0m49.920s
```



*make*


```
real    8m12.656s
user    7m39.400s
sys     0m43.580s
```



---

Comment by drkirkby created at 2010-07-15 17:29:25

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-07-15 17:29:25

On a Sun Ultra 27 (3.33 GHz, quad core, 8 threads), running OpenSolaris:

```
drkirkby`@`hawk:~/sage-4.5.rc0$ echo $MAKE
make -j12
```

the build fails with:

```
g++ -m64 -O2 -g -m64 -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -O2 -g -m64  -DHAVE_CONFIG_H  -c charset/csutil.cc -o OPTOBJ/csutil.o
g++ -m64 -O2 -g -m64 -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -O2 -g -m64  -DHAVE_CONFIG_H  -c charset/charset.cc -o OPTOBJ/charset.o
Assembler messages:
Fatal error: can't create OPTOBJ/version.o: No such file or directory
g++ -m64 -O2 -g -m64 -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -O2 -g -m64  -DHAVE_CONFIG_H  -c charset/reorder.cc -o OPTOBJ/reorder.o
g++ -m64 -O2 -g -m64 -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -I/export/home/drkirkby/sage-4.5.rc0/local/include -O2 -g -m64  -DHAVE_CONFIG_H  -c charset/alg_factor.cc -o OPTOBJ/alg_factor.o
make[2]: *** [OPTOBJ/version.o] Error 1
make[2]: *** Waiting for unfinished jobs....
mkdir OPTOBJ
make[2]: Leaving directory `/export/home/drkirkby/sage-4.5.rc0/spkg/build/singular-3-1-1-4/src/libfac'
make[1]: *** [install] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.rc0/spkg/build/singular-3-1-1-4/src'
make: *** [/export/home/drkirkby/sage-4.5.rc0/local/bin/Singular-3-1-1] Error 2
Unable to build Singular.

real    0m18.232s
user    1m18.531s
sys     0m8.304s
sage: An error occurred while installing singular-3-1-1-4

```


The previous version did build on this machine. It looks to me like the parallel building is not working correctly, as it is trying to use 
Have you checked on 't2.amth' and/or 'bsd.math'? 

I simply don't have time to check everyone's packages on Solaris. I alway try to check that mind at least build on Solaris, Linux and OS X. 

Dave


---

Comment by malb created at 2010-07-15 18:05:14

I've replaced the SPKG with one where the dependencies are fixed. As soon as I have a working Sage installation on t2 I'll try to build it there in parallel.

PS: Please allow me a bit more than *20 minutes* to test a package on Solaris next time before you complain that I didn't test it yet.


---

Comment by malb created at 2010-07-15 18:55:08

on *t2.math.washington.edu* with *MAKE="make -j32"*


```
real    36m43.246s
user    61m52.416s
sys     4m55.036s
Successfully installed singular-3-1-1-4
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/home/malb/t2/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/spkg/build/singular-3-1-1-4
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing singular-3-1-1-4.spkg
```



David, is that faster or slower than without the parallel build option?


---

Comment by drkirkby created at 2010-07-15 19:18:14

Replying to [comment:68 malb]:
> I've replaced the SPKG with one where the dependencies are fixed. As soon as I have a working Sage installation on t2 I'll try to build it there in parallel.

Thank you. 

> PS: Please allow me a bit more than *20 minutes* to test a package on Solaris next time before you complain that I didn't test it yet.

Well it was marked for review. I think if you want a reviewer to look at it, you should have checked it on the support platforms - Linux, OS X and Solaris. I know 't2' is not the fastest machine in the world, but with parallel builds, it is pretty decent. Basically the T5240 is designed for a very different task to what we use it for. 

Dave


---

Comment by drkirkby created at 2010-07-15 19:23:38

Replying to [comment:69 malb]:
> on *t2.math.washington.edu* with *MAKE="make -j32"*
> 
> {{{
> real    36m43.246s
> user    61m52.416s
> sys     4m55.036s
> Successfully installed singular-3-1-1-4
> Now cleaning up tmp files.
> rm: Cannot remove any directory in the path of the current working directory
> /home/malb/t2/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/spkg/build/singular-3-1-1-4
> Making Sage/Python scripts relocatable...
> Making script relocatable
> Finished installing singular-3-1-1-4.spkg
> }}}
> 
> 
> David, is that faster or slower than without the parallel build option?

I can't tell you that for sure - you would need to test it. However, the fact it has used 67 minutes of CPU time, but took 37 minutes to build, suggests the parallel build is working. I doubt any overhead could explain that difference. 

That should be quite useful, as Singular is probably in the top 3 of packages taking the longest to build. In fact, it might have the !#1 spot. So it's worth making Singular work in parallel, whereas for some packages, it's hardly worth the bother. 

Dave


---

Comment by malb created at 2010-07-15 20:11:25

on *bsd.math.washington.edu* with *MAKE=make -j8*


```
real    6m12.144s
user    8m16.609s
sys     1m5.636s
```



---

Comment by was created at 2010-07-15 20:39:16

REFEREE REPORT:

 * builds and passes all tests with sage-4.5 on sage.math
 * everything in spkg-install looks fine to me.
 
There are a bunch of .cvsignore files all over:

```
wstein`@`sage:~/build/sage-4.5.alphastein1/singular-3-1-1-4/src$ hg status|grep "\!"|grep cvsignore
! IntegerProgramming/.cvsignore
! Singular/.cvsignore
! doc/.cvsignore
! factory/.cvsignore
! factory/ftest/.cvsignore
! kernel/.cvsignore
! libfac/.cvsignore
! omalloc/.cvsignore
```



I will give this a positive review if:

  - the cvsignore's are removed
  - build testing passes on everything


---

Comment by was created at 2010-07-15 20:51:20

Hey, I'm wrong -- you got *rid* of the .cvsignores!

This gets a positive so long as it builds on stuff.


---

Comment by was created at 2010-07-15 20:51:57

Hey, I'm wrong -- you got *rid* of the .cvsignores!

This gets a positive so long as it builds on stuff.


---

Comment by malb created at 2010-07-15 20:52:37

All tests pass on bsd.math


---

Comment by malb created at 2010-07-15 21:08:23

William just finished compiling this SPKG on Cygwin.


---

Comment by was created at 2010-07-15 22:45:40

Amazingly, this fully works on Cygwin!!


---

Comment by malb created at 2010-07-16 13:17:49

Also builds on Itanium Linux (iras)


---

Comment by malb created at 2010-07-18 08:16:53

I didn't manage to build R on Itaninum, thus I do get some doctest failures. The genus failure is also unrelated to this ticket, thus I claim it tests successfully on Itanium Linux


```
sage -t  "devel/sage/sage/interfaces/r.py"
sage -t  "devel/sage/sage/interfaces/expect.py"
sage -t  "devel/sage/sage/stats/test.py"
sage -t  "devel/sage/sage/stats/r.py"
sage -t  "devel/sage/sage/graphs/genus.pyx"
```



---

Comment by drkirkby created at 2010-07-18 09:06:44

Are there any Singular self-tests? There is no `spkg-check` file, so these are not run if SAGE_CHECK is set to yes.


---

Comment by malb created at 2010-07-21 16:47:38

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-21 16:48:36

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-07-25 20:53:09

Changing status from positive_review to needs_info.


---

Comment by drkirkby created at 2010-07-25 20:53:09

This currently has positive review, and I'm listed as the reviewer, though I have not given it positive review.

From what I see above, the only evidence of this working on Solaris is that the package builds. It's not clear Sage can even build on Solaris with this. 


Dave


---

Comment by drkirkby created at 2010-07-26 01:04:45

Please see #9583


---

Comment by jhpalmieri created at 2010-07-26 02:11:46

Should this be called "singular....p0.spkg", since there is some patching involved?  Rather than 3-1-1-4, should the version number be 3.1.1.4?  That seems to be the current style for singular in sage, but I've seen it both ways.

I'm going to try building this on t2 later tonight.  I'll restore the positive review if it works.


---

Comment by drkirkby created at 2010-07-26 02:19:43

Replying to [comment:86 jhpalmieri]:
> Should this be called "singular....p0.spkg", since there is some patching involved?  Rather than 3-1-1-4, should the version number be 3.1.1.4?  That seems to be the current style for singular in sage, but I've seen it both ways.

I do not believe it should have a .p0, since its never actually gone into Sage at this point. So if further changes are made, it can still remain 3.1.1.4. That's my understanding of the situation. 

Dave


---

Comment by jhpalmieri created at 2010-07-26 03:00:32

At least with Sage 4.5.2.alpha0, while this builds on several platforms (I haven't tried on Solaris yet), the Sage library fails to build.  I get an error like this:

```
sage/libs/singular/function.cpp: In function ‘void initfunction()’:
sage/libs/singular/function.cpp:14355: error: ‘__pyx_f_4sage_5rings_10polynomial_34multi_polynomial_ideal_libsingular_sage_ideal_to_singular_ideal’ was not declared in this scope
make[1]: *** [installed/sage-4.5.2.alpha0] Error 1
```

(This is with sage-4.5.2.alpha0 plus the singular spkg here, attempting to build from scratch.)


---

Comment by jhpalmieri created at 2010-07-26 03:00:32

Changing status from needs_info to needs_work.


---

Comment by jhpalmieri created at 2010-07-26 03:42:34

More specifically, I have failures on 

 - sage.math
 - skynet machine taurus (x86_64-Linux-nehalem-fc) -- built from scratch twice, failed the same way both times
 - skynet machine eno (x86_64-Linux-core2-fc) -- on an existing sage 4.5.2.alpha0 install, tried just "sage -i ..." then "sage -ba"  fails
 - an OS X 10.6 box -- tried "sage -i ..." then "sage -ba" fails

Maybe it's not compatible with #1396?


---

Comment by malb created at 2010-07-26 08:27:03

Hi jhpalmieri, can you give me instructions how to reproduce this problem, i.e. what patches you've merged etc.?


---

Comment by ddrake created at 2010-07-26 13:47:08

Related ticket: #9599. That ticket will require a Singular spkg update, and the spkg here fixes that problem. If the spkg here is merged, make a note of that on #9599.


---

Comment by AlexanderDreyer created at 2010-07-26 14:34:07

`@`jhpalmieri The spkg does need  [singular-3-1-1-4.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8059/singular-3-1-1-4.patch) to be applied to the Sage library.


---

Comment by jhpalmieri created at 2010-07-26 14:52:16

Replying to [comment:90 malb]:
> Hi jhpalmieri, can you give me instructions how to reproduce this problem, i.e. what patches you've merged etc.?

I took a tarball for Sage 4.5.2.alpha0, dropped in the new singular spkg (singular-3-1-1-4.spkg), and ran "make".  I'll try again now with an already built version of Sage, running "sage -i singular-3-1-1-4.spkg" and then installing the 3-1-1-4 patch -- I hadn't done that before.


---

Comment by jhpalmieri created at 2010-07-26 15:14:28

Oh, the patch doesn't apply cleanly to Sage 4.5.2.alpha0: 

```
applying /home/palmieri/singular-3-1-1-4.patch
patching file sage/libs/singular/option.pyx
Hunk #1 succeeded at 108 with fuzz 1 (offset 14 lines).
Hunk #2 FAILED at 313
Hunk #3 FAILED at 349
2 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/option.pyx.rej
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #9 succeeded at 790 with fuzz 1 (offset -10 lines).
patching file sage/libs/singular/singular.pyx
Hunk #1 succeeded at 30 with fuzz 1 (offset 0 lines).
```

Sage does start after this, though.  There are a few doctest failures, but they look like random unrelated ones.

Note that #1396 may be backed out of Sage 4.5.2, so you might want to coordinate with that patch rather than just rebasing against some version of 4.5.2.  Also, please test on t2.math or another solaris box: the patch at #1396 caused a segfault on t2.math but not on any other platform...


---

Comment by drkirkby created at 2010-08-02 16:25:52

As a note, #1396 was backed out, despite the fact it is still shows as fixed. I've suggested to the release manager that he changes it to "need work" which would avoid the confusion. 

Is there any progress on this ticket? I created #9397 with the aim of making a small change to the current version of Singular in Sage, so it would build 64-bit on Solaris. I then set it from 'needs review' to 'needs info' thinking there was no point in getting that reviewed if this ticket gets merged. (It had at the time got positive review).

But this has been open 6 months now, and no comments added for 7 days. I'm tempted to try to get #9397 reviewed. 

Dave


---

Comment by SimonKing created at 2010-08-03 16:47:50

Replying to [comment:95 drkirkby]:
> But this has been open 6 months now, and no comments added for 7 days. I'm tempted to try to get #9397 reviewed. 

Sorry, I had been working on different things. 

On t2, I have applied the patch to sage 4.5.1 and installed the singular-3-1-1-4.spkg. Then, I did `make ptestlong`. Result:

```
The following tests failed:

        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_fiel
d.py # File not found
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny
.py # File not found
        sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py # File not found
```


This seems a bit strange to me.

First, why can the files not be found?

Second, why is it not mentioned in the summary that some tests in fact timed out? Namely:

```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [1801.8 s]
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.9 s]
```


Since I am not experienced with t2, I don't know if this doctest result is good or bad.


---

Comment by jhpalmieri created at 2010-08-03 17:53:04

Hi Simon,

These messages ("File not found") are more or less typical when the doctests time out.  I think people are working on improving that part of doctest reporting.  Since t2 can be pretty slow, some timeouts are not unusual.  I wouldn't worry about the ones you saw.  If you really want to try again, try `export SAGE_TIMEOUT_LONG=6000` to change the time out for long tests from 1800 seconds to 6000 seconds; then you shouldn't see these.  (6000 seconds is a lot more than you should need, even on t2.)


---

Comment by SimonKing created at 2010-08-03 18:42:40

Replying to [comment:97 jhpalmieri]:
> These messages ("File not found") are more or less typical when the doctests time out.  ... If you really want to try again, try `export SAGE_TIMEOUT_LONG=6000`

OK, doing it now.

Thanks,
Simon


---

Comment by drkirkby created at 2010-08-03 21:15:09

I'v'e just edited 


```
/usr/local/gcc-4.4.1-sun-linker/gcc441sun
```


the file I recommend people source, and added to it:


```
SAGE_TIMEOUT=1000 
export SAGE_TIMEOUT
SAGE_TIMEOUT_LONG=6000
export SAGE_TIMEOUT_LONG
```


I've found on my own 900 MHz SPARC that the default SAGE_TIMEOUT_LONG (1800 s) is *just* about long enough, but the SAGE_TIMEOUT (360 s) is too far too short. I'm not even sure if 1000 seconds for SAGE_TIMEOUT is enough on t2, but it probably is. 

Obviously one can unset those variables if one wants, but it would seem sensible to have the defaults so tests should pass. 


Dave


---

Comment by SimonKing created at 2010-08-03 23:16:43

Replying to [comment:98 SimonKing]:
> Replying to [comment:97 jhpalmieri]:
> > These messages ("File not found") are more or less typical when the doctests time out.  ... If you really want to try again, try `export SAGE_TIMEOUT_LONG=6000`
> 
> OK, doing it now.

Again, the setting is: Sage 4.5.1 plus singular-3-1-1-4.patch plus singular-3-1-1-4.spkg. `sage -ptestlong` on t2 with `export SAGE_TIMEOUT_LONG=6000` results in exactly one doctest failure:

```
sage -t  -long devel/sage/sage/parallel/decorate.py
**********************************************************************
File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/devel/sage-main/sag
e/parallel/decorate.py", line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
Exception raised:
    Traceback (most recent call last):
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/bin/nca
doctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/bin/sag
edoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compile
flags)
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/bin/nca
doctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[9]>", line 1, in <module>
        v = list(f([Integer(1),Integer(2),Integer(4)])); v.sort(); v###line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/pyt
hon/site-packages/sage/parallel/multiprocessing_sage.py", line 64, in parallel_i
ter
        p = Pool(processes)
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/pyt
hon2.6/multiprocessing/__init__.py", line 227, in Pool
        return Pool(processes, initializer, initargs)
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/pyt
hon2.6/multiprocessing/pool.py", line 104, in __init__
        w.start()
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/pyt
hon2.6/multiprocessing/process.py", line 104, in start
        self._popen = Popen(self)
      File "/scratch/sking/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/pyt
hon2.6/multiprocessing/forking.py", line 94, in __init__
        self.pid = os.fork()
    OSError: [Errno 12] Not enough space
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/SimonKing/.sage//tmp/.doctest_decorate
.py
         [46.5 s]
```


So, not enough space. Does that mean the hard disc (or at least `/scratch` or my home directory) is too full?

Anyway, I repeated the failing test separately, and then it succeeded:

```
sage subshell$ sage -t  -long devel/sage/sage/parallel/decorate.py
sage -t -long "devel/sage/sage/parallel/decorate.py"
         [48.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 48.8 seconds
```


So, can one say that all tests pass on t2?


Looking at the previous posts, it seems that the status is:

 - "builds and passes all tests with sage-4.5" on sage.math (William)
 - "All tests pass on bsd.math" (Martin)
 - "Amazingly, this fully works on Cygwin!!" (William)
 - With a little effort (extending timeout and running one test separately) all tests of sage-4.5.1+patch+spkg pass on t2.
 - "the patch doesn't apply cleanly to Sage 4.5.2.alpha0" (John).

Do you agree that this is a positive review *once the patch is rebased*, and that William, John and myself should be added to the list of referees?

Cheers,

Simon


---

Comment by jhpalmieri created at 2010-08-03 23:58:09

> Do you agree that this is a positive review once the patch is rebased, and that William, John and myself should be added to the list of referees?

That sounds okay to me.  The rebasing should perhaps be coordinated with #9599 (the re-merging of #1396).


---

Comment by SimonKing created at 2010-08-04 00:05:22

Replying to [comment:101 jhpalmieri]:
> > Do you agree that this is a positive review once the patch is rebased, and that William, John and myself should be added to the list of referees?
> 
> That sounds okay to me.  The rebasing should perhaps be coordinated with #9599 (the re-merging of #1396).

I don't think that much co-ordination is needed here. Apparently this ticket is more important than #9599, and #9599 will certainly not happen without the patch from  here. 

So, I'll simply wait until a rebased version of singular-3-1-1-4.patch is available, and will then base on it a new version of my patch from #1396 for re-merging -- which then needs to be tested for segfault on t2, of course.


---

Comment by jhpalmieri created at 2010-08-04 00:50:58

With #1396 backed out, this applies, so it doesn't need to be rebased.  (One hunk applies "with fuzz".)  The commit message doesn't include the trac number, but that's the only problem.

So should it get a positive review now?


---

Comment by SimonKing created at 2010-08-04 16:38:06

Replying to [comment:103 jhpalmieri]:
> With #1396 backed out, this applies, so it doesn't need to be rebased.  (One hunk applies "with fuzz".)

Good!

>  The commit message doesn't include the trac number, but that's the only problem.

Well, I recently got a "needs work" for the same reason...

> So should it get a positive review now?

I wouldn't oppose. Any veto?


---

Comment by drkirkby created at 2010-08-04 17:22:53

Changing status from needs_work to positive_review.


---

Comment by drkirkby created at 2010-08-04 17:22:53

Replying to [comment:104 SimonKing]:
> Replying to [comment:103 jhpalmieri]:
> > With #1396 backed out, this applies, so it doesn't need to be rebased.  (One hunk applies "with fuzz".)
> 
> Good!
> 
> >  The commit message doesn't include the trac number, but that's the only problem.
> 
> Well, I recently got a "needs work" for the same reason...
> 
> > So should it get a positive review now?
> 
> I wouldn't oppose. Any veto?

Me neither. I'm going to set it to positive review. 

Dave


---

Comment by mpatel created at 2010-08-07 03:08:00

I'm working on 4.5.3.alpha0, which will contain a mix of spkg updates and repository patches from report {32}.  Should I attempt to merge this ticket into 4.5.3 or wait for a dedicated Sage release?  Also, can someone indicate exactly which spkg and patch to apply?  Thanks!


---

Comment by mpatel created at 2010-08-07 03:10:42

Also also: Please ensure that any patches to merge include the ticket number in the first lines of their commit strings.


---

Comment by drkirkby created at 2010-08-07 12:13:23

Replying to [comment:106 mpatel]:
> I'm working on 4.5.3.alpha0, which will contain a mix of spkg updates and repository patches from report {32}.  Should I attempt to merge this ticket into 4.5.3 or wait for a dedicated Sage release?  Also, can someone indicate exactly which spkg and patch to apply?  Thanks!

Does this have to be called 4.5.3? I'd feel a lot happier calling it 4.6.0 if there's a major upgrade like Singular. But I think you should try to upgrade Singular. 

I don't see the need of a dedicated release - there are lots of updates that have almost no chance of conflicting with this. 

I guess I'm one of the people that believes increments in the last digit are just minor changes (bug fixes) and not major new components. It's just the release number I don't like - I think its right to merge this, and some .spkg updates. Pari seems to have stalled again, so I'd go for Singular. 

That said, I seem to be in a minority who feel version numbers should reflect the sort of updates that take place. Almost everyone seems happy with random numbers!

Dave


---

Comment by SimonKing created at 2010-08-08 19:49:50

Hi!

Replying to [comment:106 mpatel]:
>  Also, can someone indicate exactly which spkg and patch to apply?  Thanks!

I think it is singular-3-1-1-4.patch (but this needs to be rebased) and http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.spkg 

Best regards,
Simon


---

Comment by jhpalmieri created at 2010-08-08 20:58:27

Replying to [comment:109 SimonKing]:
> Hi!
> 
> Replying to [comment:106 mpatel]:
> >  Also, can someone indicate exactly which spkg and patch to apply?  Thanks!
> 
> I think it is singular-3-1-1-4.patch (but this needs to be rebased) and http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.spkg 

I think that's right, and I don't think it needs to be rebased.  At least, I've built on a few machines using this combination, and the patch applied cleanly (albeit with some fuzz), and tests passed.


---

Attachment

Updated commit string.  Use with `singular-3-1-1-4.spkg`.


---

Comment by mpatel created at 2010-08-08 21:59:49

Thanks.  I'll use

 * [attachment:singular-3-1-1-4.2.patch] (updated commit string)
 * http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.spkg


---

Comment by mpatel created at 2010-08-09 08:07:17

There might still be a problem with parallel builds.  With 4.5.2 on sage.math, I applied [attachment:singular-3-1-1-4.2.patch], copied [singular-3-1-1-4.spkg](http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.spkg) to `SAGE_ROOT`, and ran

```sh
#!/bin/bash

set -o pipefail

JOBS=20
RUNS=50
for I in `seq $RUNS`;
do
    LOG="singular-3-1-1-4-j$JOBS.log.$I"
    if [ ! -f "$LOG" ]; then
        env MAKE="make -j$JOBS" ./sage -f singular-3-1-1-4.spkg 2>&1 | tee "$LOG"
        CODE=$?
        echo $0 run $I of $RUNS: code= $CODE
    fi
done
```

All runs ended with exit code 0 (maybe I didn't retrieve the code correctly?), but

```sh
grep "An error occurred" singular-3-1-1-4*log* | sort -n
```

shows that 21 of the 50 runs failed.

I've put the logs [here](http://sage.math.washington.edu/home/mpatel/trac/8059/).

According to

```sh
$ grep "No such file or dir" sing*log* | grep -v "cannot remove" | cut -d ':' -f 2- | sort | uniq -c
      1 abs_fac.cc:2:21: error: factory.h: No such file or directory
      1 bifac.cc:1:21: error: factory.h: No such file or directory
      1 cntrlc.o: No such file or directory
     11 g++: cntrlc.o: No such file or directory
     28 g++: extra.o: No such file or directory
      4 g++: feOpt.o: No such file or directory
      1 g++: g++: cntrlc.o: No such file or directory
      4 g++: g++: extra.o: No such file or directoryextra.o: No such file or directory
      2 g++: misc_ip.o: No such file or directory
      1 lgs.h:13:21: error: factory.h: No such file or directory
```

and some digging, the `gcc -o gentable` and `gcc -o gentable2` commands, at least, sometimes don't have all of their dependencies already built.  For example, `singular-3-1-1-4-j20.log.14` contains

```
g++ -O3 -g -fPIC -pipe -I. -I../kernel -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/include -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/include -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2
-singular/local/include  -fno-implicit-templates -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H -DGENTABLE \
             -o gentable1 claptmpl.o iparith.cc tesths.cc mpsr_Tok.cc \
             grammar.o scanner.o attrib.o eigenval_ip.o extra.o fehelp.o feOpt.o ipassign.o ipconv.o ipid.o iplib.o ipprint.o ipshell.o lists.o sdb.o fglm.o interpolation.o silink.o subexpr.o janet.o wrapper.o 
libparse.o sing_win.o gms.o pcv.o maps_ip.o walk.o walk_ip.o cntrlc.o misc_ip.o calcSVD.o Minor.o MinorProcessor.o MinorInterface.o  slInit_Dynamic.o -ldl -rdynamic -L../kernel -lkernel -L/mnt/usb1/scratch/mpat
el/tmp/sage-4.5.2-singular/local/lib -L/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/lib  -lm -lsingfac -lsingcf -lntl -lgmp -lreadline -lncurses -lm  -lomalloc ../kernel/mmalloc.o
g++ -O3 -g -fPIC -pipe -I. -I../kernel -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/include -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/include -I/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2
-singular/local/include  -fno-implicit-templates -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H -DGENTABLE \
             -o gentable2 claptmpl.o iparith.cc tesths.cc mpsr_Tok.cc \
             grammar.o scanner.o attrib.o eigenval_ip.o extra.o fehelp.o feOpt.o ipassign.o ipconv.o ipid.o iplib.o ipprint.o ipshell.o lists.o sdb.o fglm.o interpolation.o silink.o subexpr.o janet.o wrapper.o 
libparse.o sing_win.o gms.o pcv.o maps_ip.o walk.o walk_ip.o cntrlc.o misc_ip.o calcSVD.o Minor.o MinorProcessor.o MinorInterface.o  slInit_Dynamic.o -ldl -rdynamic -L../kernel -lkernel -L/mnt/usb1/scratch/mpat
el/tmp/sage-4.5.2-singular/local/lib -L/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-singular/local/lib  -lm -lsingfac -lsingcf -lntl -lgmp -lreadline -lncurses -lm  -lomalloc ../kernel/mmalloc.o
g++: extra.o: No such file or directory
g++: extra.o: No such file or directory
```

Please see `singular-3-1-1-4-j20.log.47` for the `factory.h` errors.

If I didn't make a mistake:  What if we return to serial builds for this ticket but open a new one for building Singular in parallel?


---

Comment by mpatel created at 2010-08-09 08:07:17

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2010-08-09 08:21:31

I hope this ticket does finally get merged. It solves all my Solaris issues, and has less patches. 

However, I would appreciate if someone could review #9397, which does not update Singular, but has a couple of changes needed to get 64-bit builds of Singular on Solaris. 

All the changes are in this ticket, so if this ticket gets merged, then there's no need for #9397. But clearly there is a possibility this ticket will cause problems and not get merged, so it would be nice if #9397 could be merged in that case. But it needs review. 

Dave


---

Comment by fbissey created at 2010-08-09 09:19:15

I would like to mention at this stage that we have adopted this patch
in sage-on-gentoo and use it with singular-3.1.1.4 from the system
(we had to fix the path for dlopen in singular.pyx - the only place
in the whole sage spkg where there is a dlopen call). 
We are quite happy with it on x86 and amd64, I should fully test on 
ppc as well, probably over the next week end (it takes that much time).


---

Attachment

Restore serial builds.  SPKG repo patch.


---

Comment by mpatel created at 2010-08-11 00:31:03

I've made

 http://sage.math.washington.edu/home/mpatel/trac/8059/singular-3-1-1-4.p0.spkg

which restores building the package in serial, for now.  The changes are in [attachment:trac_8059_spkg-restore_serial_build.patch].  The p0 package installs consistently for me on sage.math (47 good runs out of 47, so far).

Thoughts?


---

Comment by jhpalmieri created at 2010-08-11 21:36:57

I think that changing to serial is fine for now.  I just re-ran some of your tests, but with `JOBS=4` instead of `JOBS=20`.  It worked fine.  I've seen this before with some other packages, especially on t2: if you build with too many threads, it doesn't work, but it's fine with not as many.  (For example, mpir pretty consistently doesn't seem to work for me on t2 with MAKE='make -j12', but MAKE='make -j4' is fine.)

Is this ready for review?


---

Comment by mpatel created at 2010-08-11 21:58:24

For what it's worth, with 4.5.3.alpha0 + [singular-3-1-1-4.p0.spkg](http://sage.math.washington.edu/home/mpatel/trac/8059/singular-3-1-1-4.p0.spkg) + [attachment:singular-3-1-1-4.2.patch], the long doctests pass for me on bsd and sage.math.


---

Comment by mpatel created at 2010-08-11 21:58:24

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-08-11 22:13:38

Since the only change is to disable parallel building, I think we can restore the positive review.


---

Comment by jhpalmieri created at 2010-08-11 22:13:38

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2010-08-12 11:34:12

I this this issue occurs only if you have a lot of CPU cores, but slow hard disks. Anyway, the patch at think !http://www.singular.uni-kl.de:8002/trac/ticket/250 should cure it.


---

Comment by drkirkby created at 2010-08-12 11:59:35

Replying to [comment:119 AlexanderDreyer]:
> I this this issue occurs only if you have a lot of CPU cores, but slow hard disks. Anyway, the patch at think !http://www.singular.uni-kl.de:8002/trac/ticket/250 should cure it.

That looks a very trivial change. If I understand correctly, just one line


```
$(basefactorysrc:.cc=.o):      factory.h
```


is added. But it might be better to put it on another ticket, otherwise this could drag on for ages - the ticket is already 7-months old. 

Singular is one of the slowest packages build for me on my Ultra 27, taking about 8 minutes if I recall correctly. But I'm concerned that delaying this much longer will cause more problems than a few minutes of wall time will make. 

BTW, I've run with 1000 threads on systems with only 4 cores. It's not optimal, but does allow a reasonable simulation of larger parallel builds to be made. 

A big problem in my opinion, is that the server disk.math, which serves all the home directories has been mis-configured to increase the speed of NFS. So failures on home directories might not be code errors, but simply mis-configuration of the server. 


Dave


---

Comment by AlexanderDreyer created at 2010-08-12 12:08:02

Yeah, this should be another ticket. BTW, I also hat to a another trivial fix to fix the gentable issue during parallel build.


---

Comment by AlexanderDreyer created at 2010-08-12 12:23:02

THe parallel build issue is now #9733.


---

Comment by mpatel created at 2010-08-15 08:02:32

Resolution: fixed


---

Comment by leif created at 2010-08-15 20:37:54

_Almost all_ generated files (`configure`, `grammar.cc` etc.) *again* carry the same time stamp as their sources... :(

I wonder if we should touch _all of them_ in `spkg-install`, not just two.

<flame>
I thought the upstream developers had learned at Sage Days 23.5, but perhaps 3.1.1.4 was just prepared too early...
</flame>


---

Comment by drkirkby created at 2010-08-15 21:28:45

Replying to [comment:127 leif]:
> _Almost all_ generated files (`configure`, `grammar.cc` etc.) *again* carry the same time stamp as their sources... :(

I don't know what method they use to create the tarball, but its hard to see how this can happen. Unless they touch all files before releasing, it's hard to understand how they can created a configure script with the same timestamp as the file it is generated from. 

Perhaps they copy them with `cp` at one point, and don't preserve modification times (`cp -p`). Whatever it is they are doing, it is wrong. 


> I wonder if we should touch _all of them_ in `spkg-install`, not just two.

Anything that should be touched should be. 
 
> <flame>
> I thought the upstream developers had learned at Sage Days 23.5, but perhaps 3.1.1.4 was just prepared too early...
> </flame>

No comment. 


BTW, is this really 3-1-1-4, or is it a snapshot? If the latter, then it's quite possible someone in the Sage community created the configure script and did not preserve modification times. In which case, the upstream developers are not to blame. 


Dave


---

Comment by AlexanderDreyer created at 2010-08-16 06:58:57

> _Almost all_ generated files (`configure`, `grammar.cc` etc.) *again* carry the same time stamp as their sources... :(

These files *can* be generated, but there is no need to do so (if you are not a Singular-kernel developer). In fact they are pre-generated in the repo:
http://www.singular.uni-kl.de/svn/trunk/
(That's why the time stamps are equal.)

The reason for this is that the generators for these files (e.g. *specific* version of autotools and lex) are not available on all supported platforms.

Of course, there are attempts to change this, but this cannot be done within 2,5 days. If (and only if) the tools of Sage distribution are capable of generating these files, then the correct solution would be to to remove them complete during patching.

> <flame>
> I thought the upstream developers had learned at Sage Days 23.5, but perhaps 3.1.1.4 was just prepared too early...
> </flame>
This wasn't at topic at SD23.5.


---

Comment by drkirkby created at 2010-08-16 09:10:29

Replying to [comment:129 AlexanderDreyer]:
> > _Almost all_ generated files (`configure`, `grammar.cc` etc.) *again* carry the same time stamp as their sources... :(
> 
> These files *can* be generated, but there is no need to do so (if you are not a Singular-kernel developer). In fact they are pre-generated in the repo:
> http://www.singular.uni-kl.de/svn/trunk/
> (That's why the time stamps are equal.)
> 
> The reason for this is that the generators for these files (e.g. *specific* version of autotools and lex) are not available on all supported platforms.
> 
> Of course, there are attempts to change this, but this cannot be done within 2,5 days. If (and only if) the tools of Sage distribution are capable of generating these files, then the correct solution would be to to remove them complete during patching.

IIRC, I got a message that it would try to generate the files using my autoconf, which is an older version, but it might not work. That's very dangerous. 

Also, this means if the tools exist, the file get generated needlessly, slowing the build. 

But it will not take 2.5 days to touch them in the spkg-install file. 

Dave


---

Comment by leif created at 2010-08-16 21:39:05

Replying to [comment:129 AlexanderDreyer]:
> > _Almost all_ generated files (`configure`, `grammar.cc` etc.) *again* carry the same time stamp as their sources... :(
> 
> These files *can* be generated, but there is no need to do so (if you are not a Singular-kernel developer). In fact they are pre-generated in the repo:
> http://www.singular.uni-kl.de/svn/trunk/
> (That's why the time stamps are equal.)

And exactly *that* can (and did) cause problems; the distributed generated files should be
 * *newer* than their sources,
 * up-to-date.

See http://trac.sagemath.org/sage_trac/ticket/9160#comment:22 (and http://trac.sagemath.org/sage_trac/ticket/9160#comment:20 for the latter issue, or the whole ticket...) and also [this thread on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/fbf5b7f781c3f523#).

Unfortunately we hadn't had the time to add more comments on this to `SPKG.txt`, but I expected the people further working on the Singular spkg to be aware of these issues, or take a look at previous tickets related to the spkg. (And I didn't edit the SD 23.5 wiki page, because at that time it didn't seem appropriate, but asked for other people propagating these things.)

> The reason for this is that the generators for these files (e.g. *specific* version of autotools and lex) are not available on all supported platforms.
> 
> Of course, there are attempts to change this, but this cannot be done within 2,5 days. If (and only if) the tools of Sage distribution are capable of generating these files, then the correct solution would be to to remove them complete during patching.
> 
> > <flame>
> > I thought the upstream developers had learned at Sage Days 23.5, but perhaps 3.1.1.4 was just prepared too early...
> > </flame>
> This wasn't at topic at SD23.5.

Obviously unfortunately not, see above. I expected it to be one.


---

Comment by AlexanderDreyer created at 2010-08-16 21:51:00

> Obviously unfortunately not, see above. I expected it to be one.
Neither #9160 wasn't reported upstream, nor the spkg-maintainers were CCed.


---

Comment by leif created at 2010-08-16 22:07:22

Replying to [comment:132 AlexanderDreyer]:
> > Obviously unfortunately not, see above. I expected it to be one.
> Neither #9160 wasn't reported upstream, nor the spkg-maintainers were CCed.

Well, the spkg maintainer (and some of the people involved in this ticket here) actually participated the discussion on sage-devel (which referred to #9160).

(And I remember the spkg maintainer telling me _"You don't need to cc anybody, we'll look through the tickets anyway..."_ ;-) )

That's why I had been a bit annoyed or disappointed, and the reason for the flame.


---

Comment by AlexanderDreyer created at 2010-08-16 22:42:12

> (And I remember the spkg maintainer telling me _"You don't need to cc anybody, we'll look through the tickets anyway..."_ ;-) )
I guess it was not clear, that this is to be fixed upstream. (It's merely a packaging problem.)

> That's why I had been a bit annoyed or disappointed, and the reason for the flame.
No reason to flam the upstream developers. In particular, as the ticket stated, that it had not been reported to them.
