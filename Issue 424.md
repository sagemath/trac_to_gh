# Issue 424: GMP development code for fast GCD

Issue created by migration from https://trac.sagemath.org/ticket/424

Original creator: dmharvey

Original creation time: 2007-08-11 17:16:52

Assignee: somebody

The GMP development page
   http://gmplib.org/devel/
has some code for fast GCD/XGCD of huge operands. It might not appear for a while in official releases, but they claim it's stable, and I'm interested in patching it into SAGE. I tried to do this and got stuck on configuration problems that a linux/GNU guru could help with.



---

Comment by was created at 2007-08-16 09:41:32

I tried for a while to get the patch to work.  I think it doesn't work against
the latest GMP release (plain vanilla), which is newer than the last change of that patch:


```
`echo gcd | sed 's/_$//'`    -O2 -m64 -mtune=k8 -c -o gcd.lo gcd.c
 gcc -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMP -I.. -DOPERATION_gcd -O2 -m64 -mtune=k8 -c gcd.c  -fPIC -DPIC -o .libs/gcd.o
gcd.c: In function 'gcd_schoenhage':
gcd.c:702: error: storage size of 'hgcd' isn't known
gcd.c:703: error: storage size of 'quotients' isn't known
gcd.c:704: error: array type has incomplete element type
gcd.c:748: error: 'GCD_SCHOENHAGE_THRESHOLD' undeclared (first use in this function)
gcd.c:748: error: (Each undeclared identifier is reported only once
gcd.c:748: error: for each function it appears in.)
gcd.c:778: error: storage size of '__nhgcd_swap4_left_tmp' isn't known
gcd.c:796: error: invalid use of undefined type 'struct hgcd_row'
gcd.c:800: error: storage size of '__nhgcd_swap4_2_tmp' isn't known
gcd.c: In function '__gmpn_gcd':
gcd.c:831: error: 'GCD_SCHOENHAGE_THRESHOLD' undeclared (first use in this function)
make[2]: *** [gcd.lo] Error 1
make[2]: Leaving directory `/home/was/sage2.8/sage-2.8/spkg/build/gmp-4.2.1.p9/src/mpn'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/was/sage2.8/sage-2.8/spkg/build/gmp-4.2.1.p9/src'
make: *** [all] Error 2
```


This isn't a problem with autoconf, etc.,  -- it s  a problem with the patch simply not working.

William


---

Comment by dmharvey created at 2007-08-21 01:08:14

Well no, I *did* actually get the patch compiling in a standalone setting, after manually fiddling with autoconf (etc) output files. But I couldn't get it compiling in SAGE, now I can't quite remember why.

It might help to check out the doc/configuration file in GMP, which explains in some detail how to add new files to GMP.


---

Comment by dmharvey created at 2007-09-06 16:52:47

patch that at least puts some files in the right places


---

Attachment

I've attached an initial patch which I believe puts all the right files and new lines of code in the right places. I haven't tried building yet. Apply this patch by `patch -p1 < gcd1.patch` in the gmp-4.2.1 directory.


---

Comment by dmharvey created at 2007-09-06 19:27:57

fixed up various configuration/build files to work properly


---

Attachment

patch for gmp spkg


---

Attachment

I just attached a patch (`fastgcd.hg`) which should be applied to the GMP spkg (`gmp-4.2.1.p9.spkg`. BTW the file `spkg-install~` should be deleted from that spkg too.) This patch supersedes the files `gcd1.patch` and `gcd2.patch`. This new patch adds all relevant files, and also modifies the build scripts. (It also addresses #605, I hope). I've tested it on OSX ppc and intel, haven't tested it on sage.math yet.


---

Comment by was created at 2007-09-09 16:53:03

Resolution: fixed
