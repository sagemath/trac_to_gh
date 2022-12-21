# Issue 9896: pari-2.4.3.svn-12577 fails to build on itanium with gcc 4.5.1

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-09-11 06:08:39

Assignee: tbd

CC:  leif jdemeyer

On the skynet machines cleo (ia64-Linux-rhel) and iras (ia64-Linux-suse), each using gcc 4.5.1, the PARI spkg in 4.6.alpha0 fails to build:

```
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -fPIC -o mpqs.o ../src/modules/mpqs.c
../src/modules/krasner.c: In function 'GetRamifiedPol': 
../src/modules/krasner.c:878:1: error: unrecognizable insn: 
(insn:TI 7910 7861 7937 509 (parallel [ 
            (set (reg:DI 134 f6) 
                (asm_operands:DI ("xma.hu %0 = %2, %3, f0 
        ;; 
        xma.l %1 = %2, %3, f0") ("=&f") 0 [ 
                        (reg:DI 135 f7) 
                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) 
                    ] 
                     [ 
                        (asm_input:DI ("f") (null):0) 
                        (asm_input:DI ("f") (null):0) 
                    ] 
                     [] ../src/modules/krasner.c:878)) 
            (set (reg:DI 135 f7) 
                (asm_operands:DI ("xma.hu %0 = %2, %3, f0 
        ;; 
        xma.l %1 = %2, %3, f0") ("=f") 1 [ 
                        (reg:DI 135 f7) 
                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) 
                    ] 
                     [ 
                        (asm_input:DI ("f") (null):0) 
                        (asm_input:DI ("f") (null):0) 
                    ] 
                     [] ../src/modules/krasner.c:878)) 
        ]) -1 (nil)) 
../src/modules/krasner.c:878:1: internal compiler error: in 
get_attr_first_insn, at config/ia64/itanium2.md:1909 
Please submit a full bug report, 
with preprocessed source if appropriate. 
See <http://gcc.gnu.org/bugs.html> for instructions. 
make[3]: *** [krasner.o] Error 1
```



---

Comment by jdemeyer created at 2010-09-19 08:32:48

This is clearly a gcc bug.


---

Comment by mpatel created at 2010-09-25 10:46:01

With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I "enabled" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:


```
$ tar xjf pari-2.4.3.svn-12577.p5.spkg
$ cd pari-2.4.3.svn-12577.p5/src
$ ./Configure --graphic=none
$ make test-all
[...]
* Testing zn    for gp-sta..TIME=7      for gp-dyn..TIME=3
+++ [BUG] Total bench for gp-sta is 496414
+++ [BUG] Total bench for gp-dyn is 554345

PROBLEMS WERE NOTED. The following files list them in diff format:
Directory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64
        ellglobalred-sta.dif
        ellsea-sta.dif
        galois-sta.dif
        ellglobalred-dyn.dif
        ellsea-dyn.dif
        galois-dyn.dif
make[1]: *** [test-all] Error 1
make[1]: Leaving directory `/home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64'
make: *** [test-all] Error 2
```

I've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.


---

Comment by leif created at 2010-09-25 13:09:43

Replying to [comment:3 mpatel]:
> With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I "enabled" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:
> 

```
...
PROBLEMS WERE NOTED. The following files list them in diff format:
Directory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64
        ellglobalred-sta.dif
        ellsea-sta.dif
        galois-sta.dif
        ellglobalred-dyn.dif
        ellsea-dyn.dif
        galois-dyn.dif
...
```

> I've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.

These 2*3 tests _must_ fail, because they depend on data files which aren't (yet) present / installed at that point. (We don't ship the ellglobalred data at all since it's 14 MB, and therefore patch `config/get_tests`.)


---

Comment by leif created at 2010-09-25 13:32:26

(You could temporarily patch `src/config/get_tests` with `patches/get_tests.patch`, run `src/Configure` with also e.g. `--prefix=/tmp/pari` and `make install-data` before running `make test-all`. I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.)


---

Comment by leif created at 2010-09-25 13:54:03

Replying to [comment:5 leif]:
> I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.

You don't need to do that, i.e you can simply run `make install-data && make test-all` after copying `patches/files/get_tests` to `src/config` and configuring with some temporary installation directory.


---

Comment by jdemeyer created at 2010-10-02 08:26:32

Are there any plans to report this upstream to gcc?


---

Comment by mpatel created at 2010-10-02 08:35:00

The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).


---

Comment by drkirkby created at 2010-10-02 10:30:39

Replying to [comment:8 mpatel]:
> The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).
Except that was marked as "RESOLVED FIXED" back in January 2008. Another bug report should be created. The gcc developers require the preprocessed file - see http://gcc.gnu.org/bugs/

As another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. 

Dave


---

Comment by jdemeyer created at 2010-10-02 17:07:16

Replying to [comment:9 drkirkby]:
> As another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. 

I have posed the question at [http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html)


---

Comment by mpatel created at 2010-10-09 05:28:29

Sage 4.6.alpha3 [compiles on cleo with the default compiler](http://build.sagemath.org/sage/builders/cleo%20full/builds/11) (gcc version 4.1.2 20080704 (Red Hat 4.1.2-44) and passes the tests (except for known blockers).

With the default on iras (gcc version 4.1.2 20070115 (prerelease) (SUSE Linux)), I had problems installing Python (see #10082), IPython, PolyBoRi, and R.  I don't know which of these, if any, stems from the build configuration.


---

Comment by mpatel created at 2010-10-09 05:30:15

Changing priority from blocker to critical.


---

Comment by mpatel created at 2010-10-09 05:35:32

Can we isolate a possible test case from `krasner.c`?


---

Comment by jdemeyer created at 2010-10-09 07:51:34

Replying to [comment:13 mpatel]:
> Can we isolate a possible test case from `krasner.c`?

I'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.


---

Comment by mpatel created at 2010-10-09 07:56:55

Replying to [comment:14 jdemeyer]:
> Replying to [comment:13 mpatel]:
> > Can we isolate a possible test case from `krasner.c`?
> 
> I'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.

I'm not sure about whether William is in charge of the Skynet cluster, but he can ask the Skynet administrator Mariah Lenox to give you an account.


---

Comment by jdemeyer created at 2010-10-15 08:51:58

Confirmed, even with vanilla PARI 2.4.3.
Compiling with -O2 instead of -O3 works.


---

Comment by jdemeyer created at 2010-10-15 09:10:38

Could it be related to this: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43603


---

Comment by jdemeyer created at 2010-10-16 12:38:15

Minimal testcase exhibiting the bug


---

Attachment

Cool.  Thanks!


---

Comment by mpatel created at 2010-10-17 05:50:11

Replying to [comment:16 jdemeyer]:
> Confirmed, even with vanilla PARI 2.4.3.
> Compiling with -O2 instead of -O3 works.

I've successfully built 4.6.alpha3 on cleo and iras with `SAGE_DEBUG=yes`, which turns off `-O3` for at least PARI.


---

Comment by jdemeyer created at 2010-12-10 14:15:12

Resolution: duplicate


---

Comment by jpflori created at 2013-03-01 10:09:27

Isn't that overkill to use (and wait for) #10572 rather than adding three lines in spkg-install to pass -O2 on ia64 and some GCC versions?
I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.
(This just made me think the problem on Cygwin with ECL and GCC 4.6.3 (but not 4.7.2) reported at http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061 which I encountered as well could be dealt with by just dropping the optimizaiton level.)


---

Comment by jdemeyer created at 2013-03-06 12:34:59

Replying to [comment:23 jpflori]:
> I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.
Are you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?

I would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.


---

Comment by jpflori created at 2013-03-14 17:00:24

Replying to [comment:24 jdemeyer]:
> Replying to [comment:23 jpflori]:
> > I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.
> Are you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?
It happens when compiling krasner.c so I think its the same bug, see http://trac.sagemath.org/sage_trac/ticket/10508#comment:319.
> 
> I would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.


---

Comment by jdemeyer created at 2013-03-29 04:07:29

See #14378.
