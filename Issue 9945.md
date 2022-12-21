# Issue 9945: Parallel build of Singular 3-1-1-4-package fails in other cases

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-19 05:50:37

Assignee: tbd

CC:  alexanderdreyer drkirkby fbissey jhpalmieri leif

This is a follow-up to #9733.  From [comment:ticket:9733:57 Comment 57 by François Bissey] at that ticket:

 Would you believe it. I committed the latest patch to the sage-on-gentoo tree 3 hours ago and 1 hour ago about one of our users reported a new parallel make failure at -j2 on x86.... in libfac this time.
 {{{
ar cr libsingcf_g.a canonicalform.og cf_algorithm.og cf_binom.og cf_char.og cf_chinese.og cf_cyclo.og cf_eval.og cf_factor.og cf_factory.og cf_gcd.og cf_gcd_charp.og cf_gcd_smallp.og cf_generator.og cf_globals.og cf_inline.og cf_irred.og cf_iter.og cf_iter_inline.og cf_linsys.og cf_map.og cf_map_ext.og cf_ops.og cf_primes.og cf_random.og cf_resultant.og cf_reval.og cf_switches.og cf_util.og debug.og DegreePattern.og ExtensionInfo.og fac_berlekamp.og fac_cantzass.og fac_distrib.og fac_ezgcd.og fac_iterfor.og fac_multihensel.og fac_multivar.og fac_sqrfree.og fac_univar.og fac_util.og facFqBivar.og facFqBivarUtil.og facFqFactorize.og facFqFactorizeUtil.og facFqSquarefree.og facHensel.og fieldGCD.og ffops.og ffreval.og gf_tabutil.og gfops.og imm.og initgmp.og int_cf.og int_int.og int_intdiv.og int_poly.og int_pp.og int_rat.og sm_sparsemod.og sm_util.og variable.og NTLconvert.og abs_fac.og bifac.og lgs.og singext.og
ranlib libsingcf_g.a
ar cr libsingcf.a canonicalform.o cf_algorithm.o cf_binom.o cf_char.o cf_chinese.o cf_cyclo.o cf_eval.o cf_factor.o cf_factory.o cf_gcd.o cf_gcd_charp.o cf_gcd_smallp.o cf_generator.o cf_globals.o cf_inline.o cf_irred.o cf_iter.o cf_iter_inline.o cf_linsys.o cf_map.o cf_map_ext.o cf_ops.o cf_primes.o cf_random.o cf_resultant.o cf_reval.o cf_switches.o cf_util.o debug.o DegreePattern.o ExtensionInfo.o fac_berlekamp.o fac_cantzass.o fac_distrib.o fac_ezgcd.o fac_iterfor.o fac_multihensel.o fac_multivar.o fac_sqrfree.o fac_univar.o fac_util.o facFqBivar.o facFqBivarUtil.o facFqFactorize.o facFqFactorizeUtil.o facFqSquarefree.o facHensel.o fieldGCD.o ffops.o ffreval.o gf_tabutil.o gfops.o imm.o initgmp.o int_cf.o int_int.o int_intdiv.o int_poly.o int_pp.o int_rat.o sm_sparsemod.o sm_util.o variable.o NTLconvert.o abs_fac.o bifac.o lgs.o singext.o
ranlib libsingcf.a
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates
mkdir /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates
./bin/install-sh -c -m 644 libsingcf.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf.a
./bin/install-sh -c -m 644 libsingcf_g.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf_g.a
./bin/install-sh -c -m 644 libsingcf_p.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf_p.a
install:  libsingcf_p.a does not exist
make[2]: [installcf] Error 1 (ignored)
./bin/install-sh -c -m 644 factory.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/factory.h
./bin/install-sh -c -m 644 cf_gmp.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/cf_gmp.h
./bin/install-sh -c -m 644 factoryconf.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/factoryconf.h
./bin/install-sh -c -m 644 ./ftmpl_inst.cc /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates/ftmpl_inst.cc
for file in ftmpl_array.cc ftmpl_factor.cc ftmpl_functions.h ftmpl_list.cc ftmpl_matrix.cc ftmpl_array.h ftmpl_factor.h ftmpl_list.h ftmpl_matrix.h; do \
		  ./bin/install-sh -c -m 644 ./templates/$file /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates/$file; \
		done
ranlib /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf.a
make[2]: Leaving directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/factory'
make install in libfac
make[2]: Entering directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/libfac'
./mkinstalldirs OPTOBJ
i686-pc-linux-gnu-g++ -O2 -march=athlon-xp -msse2 -pipe -fomit-frame-pointer -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include   -DHAVE_CONFIG_H  -c factor/SqrFree.cc -o OPTOBJ/SqrFree.o
mkdir OPTOBJ
Assembler messages:
Fatal error: can't create OPTOBJ/SqrFree.o: No such file or directory
i686-pc-linux-gnu-g++ -O2 -march=athlon-xp -msse2 -pipe -fomit-frame-pointer -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include   -DHAVE_CONFIG_H  -c factor/Factor.cc -o OPTOBJ/Factor.o
make[2]: *** [OPTOBJ/SqrFree.o] Error 2
make[2]: *** Waiting for unfinished jobs....
make[2]: Leaving directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/libfac'
make[1]: *** [install] Error 1
}}}


---

Attachment

patch for libfac makefile


---

Comment by mpatel created at 2010-09-19 06:03:14

François has posted a patch at #9733 for the libfac problem.  We could merge it into a new singular-3-1-1-4.p3.spkg here.


---

Comment by fbissey created at 2010-09-19 06:08:45

Patch attached with a slightly more descriptive name.


---

Comment by leif created at 2010-09-19 11:23:26

Patch again looks reasonable.

I only wonder how often we'll again have to create a new Singular spkg for almost the "same" reason... ;-)

Funny that the new race condition showed up with just _two_ `make` jobs, after so much excessive testing by Dave and others.


---

Comment by drkirkby created at 2010-09-19 12:30:21

Replying to [comment:5 leif]:
> Patch again looks reasonable.
> 
> I only wonder how often we'll again have to create a new Singular spkg for almost the "same" reason... ;-)

Yes, it's a bit worrying. 

> Funny that the new race condition showed up with just _two_ `make` jobs, after so much excessive testing by Dave and others.
 
I expect it depends on very much on the time a compiler takes to compile code and for the linker to link it. On any one system, if file `foo.c` takes longer to compile than file `foobar.c` then that's likely to be the same irrespective of the system load. 

I was wondering about the possibility of using a wrapper script for gcc, such that there was a random delay between 0 and 50 ms, before gcc actually started compiling. The `nanosleep` function should provide that possibility. Then implement something similar for the linker so there was a random delay before it started linking. Of course that would slow the build process, but would probably have a higher probability of inducing build failures. 

One would need to think carefully about how to seed the random number generators then. Probably using `/dev/random` would be best. 

It would be some effort to write the code for this, but once written it should make detection of race conditions much easier for any bit of Sage. 

Another idea, which *may* help would be to randomly change the number of processors online for those of us with multi-processor machines. I'm less certain about whether that would be useful, though it be be very much easier to implement. Although this machine is only quad core, it's hyperthreaded, so I could have from one to eight threads active at any one time. 

I suspect a search of Google would find other similar (but hopefully better) methods of inducing effects that are likely to uncover race conditions. 

Dave


---

Comment by leif created at 2010-09-19 13:33:54

I was thinking of similar testing w.r.t. `spkg/standard/deps`, i.e. inter-spkg dependencies, where adding (not necessarily random) `sleep` would suffice, especially to the build (time) of packages that get early and almost instantly built.

For Makefiles, IMHO careful reading (and / or a "makefile-lint") would be better, which is obviously harder [to implement]. Unfortunately, the steps actually taken in a build also heavily depend on the system and its configuration, so I expect it to be undecidable in general. Nevertheless, one could catch at least _some_ missing dependencies without "brute-force" trial and error.


---

Comment by leif created at 2010-09-19 13:46:02

P.S.: For `deps`, I'd prefer _generating_ it from _formal_ (dependency) specs given in (or for) the spkgs, like every proper package system / installer does. These usually also include specs of the required _versions_.

Sorry, a bit off-ticket-topic.


---

Comment by AlexanderDreyer created at 2010-09-21 03:13:05

Is there already a spkg around? (Sorry, I was out of office and off.)
I put one with fbissey's patch here:
http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p3.spkg


---

Comment by leif created at 2010-09-21 09:39:57

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-09-21 09:55:54

By all means someone review this, as I expect it fixes the bug. 

Within the next 24 hours I will have implemented a random delay in front of gcc and will build this a few hundred times with random delays. That might help discover any more similar issues, if they exist. 

Dave


---

Comment by leif created at 2010-09-21 10:30:35

The changelog lacks an entry for the p3.

François, perhaps you could ask the original reporter to test this, too?

(Such that we don't run into the next race condition after this ticket has been merged.)

His/her system appears to be a good test platform... ;-)


---

Comment by fbissey created at 2010-09-21 10:40:25

Replying to [comment:12 leif]:
> The changelog lacks an entry for the p3.
> 
> François, perhaps you could ask the original reporter to test this, too?
> 
> (Such that we don't run into the next race condition after this ticket has been merged.)
> 
> His/her system appears to be a good test platform... ;-)
I posted the patch only after he reported back that it worked for him.
You could say that he has a good test platform. Single core system,
he has a 64bit base system and a 32bit system in a chroot. In this particular
case the problem only appeared in the 32bit chroot.

He reported quite a number of issues for the sage-on-gentoo port over the years.


---

Comment by leif created at 2010-09-21 10:48:35

Replying to [comment:13 fbissey]:
> I posted the patch only after he reported back that it worked for him.

Sorry, [comment:ticket:9733:58 you already said so], forgot that.


---

Comment by leif created at 2010-09-21 11:15:32

Dave, if you don't want to mess around with `/dev/urandom` (and `hd`?), you could use the pid of a subshell (`rand_raw=`sh -c 'echo $$'``) as the source for a pseudo random number (perhaps "recursively", i.e. the pid of the nth subshell where n is itself a pseudo-random number), and feed that to

```sh
sleep `expr $base + $rand_raw % $modulus \* $scale`
```


Plain `rand_raw` is of course bad on an otherwise idle system, also depending on how long you sleep.


---

Comment by leif created at 2010-09-21 11:58:30

Minimalistic C program (not very robust) to implement `nanosleep` analogous to `sleep(1)`.


---

Attachment

Dave, I've attached a [minimalistic C implementation](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9946/nanosleep.c) of a command `nanosleep <nanoseconds>`.


---

Comment by drkirkby created at 2010-09-21 12:17:34

Causes a random delay up to a maximum of that set by an enviroment variable MAX_COMPILER_DELAY_IN_MICRO_SECONDS


---

Attachment

I thought I'd commented on the file I added, but I forgot. 

I'd already done on this before Leif posted his file, though we both made use of `nanosleep()` Rather than take an argument like Leif's, mine reads the value of the environment variable `MAX_COMPILER_DELAY_IN_MICRO_SECONDS `. It reads from `/dev/urandom`

What I'm less sure about, is what is a sensible maximum delay to use. That's a difficult question to answer I think. Any ideas?


---

Comment by AlexanderDreyer created at 2010-09-21 13:03:44

Replying to [comment:12 leif]:
> The changelog lacks an entry for the p3.
I fixed that (typical late-night copy&paste mistake)

http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p3.spkg 
(same location as above)


---

Comment by leif created at 2010-09-21 13:18:14


```C
    if (sizeof(int) != 4) {
        fprintf(stderr,"Your system is odd. On everying except a Cray X MP, an int is 4 bytes\n");
        fprintf(stderr,"Exiting...\n");
        exit(3);
    }
```

LOL, ever heard of 16-bit systems (or compilers)? And even some old compilers on 32-bit systems had 2-byte `int`s IIRC (of course that's odd). I can't await having `sizeof(int)>=16`... ;-)

The allocation of `delay_as_string` is useless (actually a space leak :) ) unless you `str[n]cpy()` the result of `getenv(...)` to it, but who cares.


---

Comment by drkirkby created at 2010-09-21 13:49:20

Replying to [comment:19 leif]:
> {{{
> #!C
>     if (sizeof(int) != 4) {
>         fprintf(stderr,"Your system is odd. On everying except a Cray X MP, an int is 4 bytes\n");
>         fprintf(stderr,"Exiting...\n");
>         exit(3);
>     }
> }}}
> LOL, ever heard of 16-bit systems (or compilers)? And even some old compilers on 32-bit systems had 2-byte `int`s IIRC (of course that's odd). I can't await having `sizeof(int)>=16`... ;-)

No, but when I was testing http://atlc.sourceforge.net/ for portability, I found on a Cray X MP running Unicos that:

 * sizeof(long)=8
 * sizeof(int)=8
 * sizeof(short)=8

The latter was a real pain to me. 

So nothing would totally surprise me. 

I've now set this up compiling in 5 different directories on machine 

 * Maximum delay of 1 second (mean 500 ms)
 * Maximum delay of 100 ms (mean 50 ms)
 * Maximum delay of 10 ms (mean 5 ms)
 * Maximum delay of 1 ms (mean 500 us) 
 * Maximum delay of 100 us (mean = 50 us)

I suspect that the first of these is too long, so will slow builds considerably and the last is too short, so will not be too different from no delay. 

 
> The allocation of `delay_as_string` is useless (actually a space leak :) ) unless you `str[n]cpy()` the result of `getenv(...)` to it, but who cares.
> 

Yes, you are correct. I'll change that, but it's not a big deal for now. It's a start. 


I don't know how this would fit in with Nathann's:

_... though my way of seeing it would really be to avoid spending hours wondering "how it could fail" when it seems so easy to just test it and write patches when errors are reported. _


Somehow I doubt it would fit in too well. 

If I don't get any problems, and there are are problems found by others, it would make me wonder how else one could try to find such problems. This was my best stab at an answer, but perhaps it is not ideal. 

I think really there should be a delay on the linker too, which I have not implemented. I've only done this on the compilers gcc, g++ and gfortran. 

Dave


---

Comment by leif created at 2010-09-21 14:06:38

Replying to [comment:20 drkirkby]:
> [...] when I was testing http://atlc.sourceforge.net/ for portability, I found on a Cray X MP running Unicos that:
> 
>  * sizeof(long)=8
>  * sizeof(int)=8
>  * sizeof(short)=8
> 
> The latter was a real pain to me.

IIRC the C standard requires
  `sizeof(short) <= sizeof(int) <= sizeof(long)`
but also
  `sizeof(short) < sizeof(long)`
so Cray would violate the latter.

> I don't know how this would fit in with Nathann's:
> 
> _... though my way of seeing it would really be to avoid spending hours wondering "how it could fail" when it seems so easy to just test it and write patches when errors are reported. _
> 
> 
> Somehow I doubt it would fit in too well. 
> 
> If I don't get any problems, and there are are problems found by others, it would make me wonder how else one could try to find such problems. This was my best stab at an answer, but perhaps it is not ideal.

You mean I should upload a reviewer patch? ;-)

> I think really there should be a delay on the linker too, which I have not implemented. I've only done this on the compilers gcc, g++ and gfortran. 

The linker isn't often used directly, and `libtool` calls `gcc` for linking:

```sh
ld -shared -o p_Procs_FieldIndep.so p_Procs_Lib_FieldIndep.dl_o
ld -shared -o p_Procs_FieldZp.so p_Procs_Lib_FieldZp.dl_o
ld -shared -o p_Procs_FieldQ.so p_Procs_Lib_FieldQ.dl_o
ld -shared -o p_Procs_FieldGeneral.so p_Procs_Lib_FieldGeneral.dl_o
ld -shared -o dbmsr.so ndbm.dl_o sing_dbm.dl_o -lc_nonshared
```

(That's all.)


---

Comment by drkirkby created at 2010-09-21 18:58:02

Replying to [comment:21 leif]:
> Replying to [comment:20 drkirkby]:
> > [...] when I was testing http://atlc.sourceforge.net/ for portability, I found on a Cray X MP running Unicos that:
> > 
> >  * sizeof(long)=8
> >  * sizeof(int)=8
> >  * sizeof(short)=8
> > 
> > The latter was a real pain to me.
> 
> IIRC the C standard requires
>   `sizeof(short) <= sizeof(int) <= sizeof(long)`
> but also
>   `sizeof(short) < sizeof(long)`
> so Cray would violate the latter.

I was not aware of `sizeof(short) < sizeof(long)` was part of the C standard. I don't have a copy of the standard. If anyone does, please email me one! 

I guess the $15,000,000 [Cray X-MP](http://en.wikipedia.org/wiki/Cray_X-MP) introduced in 1982 pre-dated the latest C99 standard by a few years. 

If you want to try a Cray, go to http://www.cray-cyber.org/access/index.php and get an account. 

At the time I used the X-MP, (at least I think it was an X-MP, but I see they only have a Y-MP now), it was *painfully* slow to do anything. You really needed to use the vector processors properly to get the performance, and I had no intension of doing that. But I reckon my code is quite portable, as it must be one of the only programs to have been run on a supercomputer and a Sony Playstation games console! I think Sage would need a good few patches to ever be that portable. 


> > I don't know how this would fit in with Nathann's:
> > 
> > _... though my way of seeing it would really be to avoid spending hours wondering "how it could fail" when it seems so easy to just test it and write patches when errors are reported. _
> > 
> > 
> > Somehow I doubt it would fit in too well. 
> > 
> > If I don't get any problems, and there are are problems found by others, it would make me wonder how else one could try to find such problems. This was my best stab at an answer, but perhaps it is not ideal.
> 
> You mean I should upload a reviewer patch? ;-)
> 
> > I think really there should be a delay on the linker too, which I have not implemented. I've only done this on the compilers gcc, g++ and gfortran. 
> 
> The linker isn't often used directly, and `libtool` calls `gcc` for linking:
> {{{
> #!sh
> ld -shared -o p_Procs_FieldIndep.so p_Procs_Lib_FieldIndep.dl_o
> ld -shared -o p_Procs_FieldZp.so p_Procs_Lib_FieldZp.dl_o
> ld -shared -o p_Procs_FieldQ.so p_Procs_Lib_FieldQ.dl_o
> ld -shared -o p_Procs_FieldGeneral.so p_Procs_Lib_FieldGeneral.dl_o
> ld -shared -o dbmsr.so ndbm.dl_o sing_dbm.dl_o -lc_nonshared
> }}}
> (That's all.)
 

OK. So hopefully random delays on the compiler will work. 

Things are looking ok so far. I've built this 

 * 29 times with a mean delay of 500 ms (maximum 1 second)
 * 44 times with a mean delay of 50 ms  (maximum 100 ms)
 * 46 times with a mean delay of 5 ms   (maximum 10 ms)
 * 46 times with a mean delay of 500 us (maximum 1 ms)
 * 46 times with a mean delay of 50 us. (maximum 100 us)

If by around 0830 GMT tomorrow, this has not failed, I'll give it a positive review. By that time it should have built nearly 100 times with the longest delay and certainly 100 times with the shorter delays. 



Dave


---

Comment by drkirkby created at 2010-09-22 07:31:19

I had a bit of a shock this morning. Instead of my computer running flat out building Singular, it was relatively idle. This suggested the Singular processes had died. But luckily it was not an error. The loop had a limit of 100, so they had all finished. 

So I've now built this version of Singular 500 times, with random delays before calling gcc. 

 * 100 times with a mean delay of 500 ms (maximum 1 second)
 * 100 times with a mean delay of 50 ms (maximum 100 ms)
 * 100 times with a mean delay of 5 ms (maximum 10 ms)
 * 100 times with a mean delay of 500 us (maximum 1 ms)
 * 100 times with a mean delay of 50 us. (maximum 100 us) 

*IF* there are any further problems found, then I don't know how we go about testing for them. At least random testing has not discovered them. 

So positive review. 

Dave


---

Comment by drkirkby created at 2010-09-22 07:31:19

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2010-09-22 07:40:31

`@`Dave: Thanks a lot for the extensive tests! (Also in the name of the Singular-Team).

All the newly found dependencies will be added upstream. Some of them are in fact not only unexpected, but also they were not intended that way. (In fact these are bugs, which will be fixed.)


---

Comment by drkirkby created at 2010-09-22 08:38:10

Replying to [comment:24 AlexanderDreyer]:
> `@`Dave: Thanks a lot for the extensive tests! (Also in the name of the Singular-Team).
> 
> All the newly found dependencies will be added upstream. Some of them are in fact not only unexpected, but also they were not intended that way. (In fact these are bugs, which will be fixed.)

You are welcome. I've changed the tag about "Report Upstream", since these changes are not yet in a stable release of Singular. Look at all the options on that, and determine what's the most appropriate. 

Of course it's good I found no flaws, though I must admit it would have been nice to know whether adding random delays before calling gcc/g++ was useful or not. I guess I could try the previous version with random delays and see if I can uncover the same bug as the other person. 

Trying to build the whole of Sage with random delays might be useful, but it would not be possible to build it 500 times in any reasonable amount of time. 

But I better stop there, as I would only confirm Leif's belief I'm addicted to testing! 

Dave


---

Comment by mpatel created at 2010-09-29 08:40:01

Resolution: fixed
