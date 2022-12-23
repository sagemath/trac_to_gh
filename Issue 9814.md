# Issue 9814: ATLAS fails to build on a PA-RISC system running HP-UX

Issue created by migration from https://trac.sagemath.org/ticket/9815

Original creator: drkirkby

Original creation time: 2010-08-27 05:52:43

Assignee: AlexGhitza

CC:  leif chapoton

*== Hardware ==
 * HP C3600
 * 1 x 552 MHz PA-RISC CPU
 * 8 GB RAM 
 * HP-UX 11.11B 
 * gcc 4.3.4 configured to use the GNU assembler and HP linker.
 * sage-4.5.3.alpha2 (containing ATLAS 3.8.3)

 == The problem ==

This is the first failure observed when building Sage on HP-UX. 


```
gcc -I/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//CONFIG/include  -g -w -o xprobe_comp probe_comp.o atlconf_misc.o 
rm -f config1.out
make atlas_run atldir=/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build exe=xprobe_comp args="-v 0 -o atlconf.txt -O 9 -A 0 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/home/drkirkby/sage-4.5.3.alpha2/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32" \
                redir=config1.out
make[3]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
cd /home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build ; ./xprobe_comp -v 0 -o atlconf.txt -O 9 -A 0 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/home/drkirkby/sage-4.5.3.alpha2/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32 > config1.out
cc1: error: unrecognized command line option "-m32"
make[4]: *** [IRunCComp] Error 1


Unable to find usable compiler for ICC; abortingMake sure compilers are in your path, and specify good compilers to configure
(see INSTALL.txt or 'configure --help' for details)make[3]: *** [atlas_run] Error 1
make[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make[2]: *** [IRun_comp] Error 2
make[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
Assertion failed: !system(ln), file /home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//CONFIG/src/config.c, line 125

OS configured as HPUX (9)

Assembly configured as GAS_PARISC (5)

Bad VECFLAG value=0, ierr=0, ln2='VECFLAG=0
'

Vector ISA Extension configured as   (0,0)

Bad MACHTYPE value=0, ierr=0, ln2='MACHTYPE=0
'

Architecture configured as  UNKNOWN (0)

Bad CPU MHZ value=0, ierr=0, ln2='CPU MHZ=0
'

Clock rate configured as 0Mhz
Cannot detect CPU throttling.
/bin/sh: 25822 Abort(coredump)
xconfig exited with 134
make[2]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make -f Make.top build
make[3]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make[3]: Make.top: No such file or directory
make[3]: *** No rule to make target `Make.top'.  Stop.
make[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make[2]: *** [build] Error 2
make[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'
Failed to build ATLAS.
Failed to build ATLAS.

real	0m11.736s
user	0m7.720s
sys	0m2.080s
sage: An error occurred while installing atlas-3.8.3.p14
```


An upgrade of ATLAS would be the first obvious thing to try. 

I'm cc'ing Leif, as I know how much he loves HP-UX !!! 


---

Comment by AlexGhitza created at 2010-09-02 11:07:47

Changing component from algebra to porting.


---

Comment by AlexGhitza created at 2010-09-02 11:07:47

Changing assignee from AlexGhitza to drkirkby.


---

Comment by jdemeyer created at 2015-09-08 12:45:40

Changing component from porting to porting: AIX or HP-UX.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-24 06:29:03

Resolution: invalid
