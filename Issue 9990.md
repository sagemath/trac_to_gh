# Issue 9990: rubiks is failing to install proplerly on AIX as it's assuming the GNU install program.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-23 22:41:02

Assignee: drkirkby

CC:  chapoton

*== Hardware and software ==
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 

 == The Problem ==
rubiks is failing to install. I believe it is believing the `install` program is the `GNU install`, whereas in fact IBM provide their own on AIX, which is not compatible. 

This is the first `install` program in the PATH

```
-bash-4.1$ command -v install
/usr/bin/install
```

We can see this is not the GNU install program. 

```
-bash-4.1$ /usr/bin/install -h
getopt: Not a recognized flag: h
Usage: install [-c DirectoryA] [-f DirectoryB] [-i] [-m] [-M Mode] [-O Owner]
               [-G Group] [-S] [-n DirectoryC] [-o] [-s] File [DirectoryX ...]
-bash-4.1$ /usr/bin/install --help
getopt: Not a recognized flag: -
getopt: Not a recognized flag: h
getopt: Not a recognized flag: e
getopt: Not a recognized flag: l
getopt: Not a recognized flag: p
Usage: install [-c DirectoryA] [-f DirectoryB] [-i] [-m] [-M Mode] [-O Owner]
               [-G Group] [-S] [-n DirectoryC] [-o] [-s] File [DirectoryX ...]

```


This results in some odd permission problems when rubiks tries to install itself:


```
gcc -O -DLARGE_MEM -DVERBOSE -o sizekoc2 sizekoc2.o
size sizekoc2
sizekoc2: 48541 + 2387 + 409577660 + 2525 + 77886 = 409708999
make[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/rubiks-20070912.p12/src/dik'
make[3]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/rubiks-20070912.p12/src/reid'
make[3]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.
gcc  -O2  -g  -Wall     optimal.c   -o optimal
gcc  -O2  -g  -Wall     twist.c   -o twist
make[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/rubiks-20070912.p12/src/reid'
mkdir -p /home/users/drkirkby/sage-4.6.alpha1/local/bin
/usr/bin/install reid/optimal /home/users/drkirkby/sage-4.6.alpha1/local/bin
find: cannot chdir to </etc/security> : Permission denied
find: cannot chdir to </etc/tunables> : Permission denied
find: cannot chdir to </etc/iscsi> : Permission denied
find: cannot chdir to </etc/ppp> : Permission denied
find: cannot chdir to </usr/lib/boot/network> : Permission denied
find: cannot chdir to </usr/lib/drivers/crypto> : Permission denied
install: File optimal was not found.
make[2]: *** [install] Error 2
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/rubiks-20070912.p12/src'

real    10m38.826s
user    5m19.612s
sys     0m8.383s
sage: An error occurred while installing rubiks-20070912.p12
```



---

Attachment

Build failure observed on an RS/6000 running AIX 5.3.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-25 13:34:12

Resolution: invalid
