# Issue 9996: Tachyon does not even try to build on AIX

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-24 02:18:12

Assignee: drkirkby

## Hardware and software
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 (which has tachyon-0.98beta.p11)

## The problem

```
Warning: Attempted to overwrite SAGE_ROOT environment variable
tachyon-0.98beta.p11
Machine:
AIX aixbox 3 5 000245984C00
Deleting directories from past builds of previous/current versions of tachyon-0.98beta.p11
Extracting package /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/tachyon-0.98beta.p11.spkg ...
-rw-r--r--   1 drkirkby staff        509381 25 Jul 22:53 /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/tachyon-0.98beta.p11.spkg
tachyon-0.98beta.p11/
tachyon-0.98beta.p11/dist/
<SNIP>
tachyon-0.98beta.p11/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
AIX aixbox 3 5 000245984C00
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: powerpc-ibm-aix5.3.0.0
Configured with: ../stage/gcc-4.2.4/configure --disable-shared --enable-threads=posix --prefix=/opt/pware --with-long-double-128 --with-
mpfr=/opt/pware --with-gmp=/opt/pware
Thread model: aix
gcc version 4.2.4
****************************************************
Tachyon build for AIX not implemented (for SAGE) - please complain on sage-devel

real    0m0.218s
user    0m0.049s
sys     0m0.045s
sage: An error occurred while installing tachyon-0.98beta.p11
```



---

Comment by mhampton created at 2010-09-24 11:55:17

Could you please try this with the updated tachyon package from 5281?


---

Comment by drkirkby created at 2010-09-24 12:36:59

Replying to [comment:1 mhampton]:
> Could you please try this with the updated tachyon package from 5281?
Sure. I'm at a Starbucks cafe now, so will try later. The RS/6000 is switched off now, so I can't remotely access it.


---

Comment by drkirkby created at 2010-09-25 10:13:00

There are two reasons this is not working. 
 * There's nothing in `SPKG.txt` to handle the case of AIX
 * There's no target in the file `Make-arch` that will work with a generic compiler on AIX. The targets all assume the use of IBM's compiler. 

Two targets will be added for AIX, and since HP-UX will suffer the same problem, another two targets will be added for HP-UX. These 4 targets are:
 * `aix-generic`
 * `aix-generic-thr`
 * `hpux-generic`
 * `hpux-generic-thr`

We might as well try building with the threaded versions (aix-generic-thr and hpux-generic-thr) on both AIX and HP-UX.


---

Comment by drkirkby created at 2010-09-25 10:17:48

I forgot to say, these 4 targets can be added to the Tachyon upgrade ticket #5281, so I am not intending to add a patch here, but rather this ticket can be closed when #5281 is closed. This assumes #5281 does not drag on for ages, as the ticket has been open for 20 months! If that ticket drags on and on, then I'll add patches to this ticket.


---

Comment by jdemeyer created at 2011-02-06 09:55:27

Resolution: duplicate


---

Comment by jdemeyer created at 2011-02-06 09:55:27

Fixed by #5281.
