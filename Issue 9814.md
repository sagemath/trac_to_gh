# Issue 9814: ATLAS fails to build on a PA-RISC system running HP-UX

archive/issues_009814.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @nexttime @fchapoton\n\n == Hardware ==\n* HP C3600\n* 1 x 552 MHz PA-RISC CPU\n* 8 GB RAM \n* HP-UX 11.11B \n* gcc 4.3.4 configured to use the GNU assembler and HP linker.\n* sage-4.5.3.alpha2 (containing ATLAS 3.8.3)\n\n == The problem ==\n\nThis is the first failure observed when building Sage on HP-UX. \n\n\n```\ngcc -I/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//CONFIG/include  -g -w -o xprobe_comp probe_comp.o atlconf_misc.o \nrm -f config1.out\nmake atlas_run atldir=/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build exe=xprobe_comp args=\"-v 0 -o atlconf.txt -O 9 -A 0 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/home/drkirkby/sage-4.5.3.alpha2/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32\" \\\n                redir=config1.out\nmake[3]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\ncd /home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build ; ./xprobe_comp -v 0 -o atlconf.txt -O 9 -A 0 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/home/drkirkby/sage-4.5.3.alpha2/local/bin/sage_fortran' -Fa if '-fPIC'  -b 32 > config1.out\ncc1: error: unrecognized command line option \"-m32\"\nmake[4]: *** [IRunCComp] Error 1\n\n\nUnable to find usable compiler for ICC; abortingMake sure compilers are in your path, and specify good compilers to configure\n(see INSTALL.txt or 'configure --help' for details)make[3]: *** [atlas_run] Error 1\nmake[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nmake[2]: *** [IRun_comp] Error 2\nmake[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nAssertion failed: !system(ln), file /home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//CONFIG/src/config.c, line 125\n\nOS configured as HPUX (9)\n\nAssembly configured as GAS_PARISC (5)\n\nBad VECFLAG value=0, ierr=0, ln2='VECFLAG=0\n'\n\nVector ISA Extension configured as   (0,0)\n\nBad MACHTYPE value=0, ierr=0, ln2='MACHTYPE=0\n'\n\nArchitecture configured as  UNKNOWN (0)\n\nBad CPU MHZ value=0, ierr=0, ln2='CPU MHZ=0\n'\n\nClock rate configured as 0Mhz\nCannot detect CPU throttling.\n/bin/sh: 25822 Abort(coredump)\nxconfig exited with 134\nmake[2]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nmake -f Make.top build\nmake[3]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nmake[3]: Make.top: No such file or directory\nmake[3]: *** No rule to make target `Make.top'.  Stop.\nmake[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nmake[2]: *** [build] Error 2\nmake[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/atlas-3.8.3.p14/ATLAS-build'\nFailed to build ATLAS.\nFailed to build ATLAS.\n\nreal\t0m11.736s\nuser\t0m7.720s\nsys\t0m2.080s\nsage: An error occurred while installing atlas-3.8.3.p14\n```\n\n\nAn upgrade of ATLAS would be the first obvious thing to try. \n\nI'm cc'ing Leif, as I know how much he loves HP-UX !!! \n\nIssue created by migration from https://trac.sagemath.org/ticket/9815\n\n",
    "created_at": "2010-08-27T05:52:43Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ATLAS fails to build on a PA-RISC system running HP-UX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9814",
    "user": "drkirkby"
}
```
Assignee: @aghitza

CC:  @nexttime @fchapoton

 == Hardware ==
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

Issue created by migration from https://trac.sagemath.org/ticket/9815





---

archive/issue_comments_096791.json:
```json
{
    "body": "Changing component from algebra to porting.",
    "created_at": "2010-09-02T11:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96791",
    "user": "@aghitza"
}
```

Changing component from algebra to porting.



---

archive/issue_comments_096792.json:
```json
{
    "body": "Changing assignee from @aghitza to drkirkby.",
    "created_at": "2010-09-02T11:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96792",
    "user": "@aghitza"
}
```

Changing assignee from @aghitza to drkirkby.



---

archive/issue_comments_096793.json:
```json
{
    "body": "Changing component from porting to porting: AIX or HP-UX.",
    "created_at": "2015-09-08T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96793",
    "user": "@jdemeyer"
}
```

Changing component from porting to porting: AIX or HP-UX.



---

archive/issue_comments_096794.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96794",
    "user": "@embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_096795.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96795",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096796.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96796",
    "user": "@mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_096797.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-24T06:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9814#issuecomment-96797",
    "user": "@fchapoton"
}
```

Resolution: invalid
