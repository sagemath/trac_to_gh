# Issue 7048: ATLAS ignores CC variable, then dumps core when trying to build with Sun Studio on  Solaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-28 09:18:16

Assignee: tbd

CC:  dimpase

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

I tried to build Sage with Sun Studio and see: 

```
atlas-3.8.3.p9/src/src/auxil/ATL_hescal.c
atlas-3.8.3.p9/src/src/auxil/ATL_axpy.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Platform detected to be 32 bits
system_atlas.py:6: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.
  fortran = os.popen2(os.environ['SAGE_LOCAL']+'/bin/'+'which_fortran')[1].read()
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9
Deal with PPC4 7447 model and Itanium 2
Updating archinfo_x86.c
Updating probe_comp.c
Updating Make.top
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
gcc -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/include  -g -w -c /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/src/atlconf_misc.c
gcc -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/include  -g -w -o xconfig /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/src/config.c atlconf_misc.o
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
./xconfig -d s /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src/ -d b /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build  -Ss flapack /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/liblapack.a -Si cputhrchk 0 -Fa alg -fPIC -t 0 -C if /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/bin/sage_fortran -b 32
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
gcc -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/include  -g -w -c /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/src/probe_comp.c
gcc -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/include  -g -w -o xprobe_comp probe_comp.o atlconf_misc.o
rm -f config1.out
make atlas_run atldir=/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build exe=xprobe_comp args="-v 0 -o atlconf.txt -O 2 -A 28 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32" \
                redir=config1.out
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
cd /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build ; ./xprobe_comp -v 0 -o atlconf.txt -O 2 -A 28 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32 > config1.out
UNKNOWN COMPILER '/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/bin/sage_fortran' for F77: you must also supply flags!
make[3]: *** [atlas_run] Error 7
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
make[2]: *** [IRun_comp] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
Assertion failed: !system(ln), file /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build/../src//CONFIG/src/config.c, line 125

OS configured as SunOS (2)

Assembly configured as GAS_SPARC (3)

Bad VECFLAG value=0, ierr=0, ln2='VECFLAG=0
'

Vector ISA Extension configured as   (0,0)

Architecture configured as  USIII (28)

Clock rate configured as 1200Mhz
Cannot detect CPU throttling.
Abort - core dumped
xconfig exited with 134
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
make -f Make.top build
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
make[3]: Make.top: No such file or directory
make[3]: *** No rule to make target `Make.top'.  Stop.
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
make[2]: *** [build] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/atlas-3.8.3.p9/ATLAS-build'
Failed to build ATLAS.
Failed to build ATLAS.

real    0m11.364s
user    0m5.163s
sys     0m4.042s
```



---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by slelievre created at 2020-08-22 07:16:35

Resolution: invalid
