# Issue 9033: Singular does not try to build 64-bit on OpenSolaris.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-24 10:43:56

Assignee: drkirkby

CC:  jsp dimpase

On a Sun Ultra 27 running OpenSolaris x64, Singular is not attempting to build as a 64-bit binary, but also fails to build fully as a 32-bit binary. (It does however build partially as 32-bit).


```
singular-3-1-0-4-20100214/src/svd/tests/
singular-3-1-0-4-20100214/src/svd/tests/testsvdunit.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************

<snip>
gcc -O3 -g -fPIC -I. -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -c omBinPage.c
<snip>
g++ -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -O3 -g -fPIC -o cf_factor.o
In file included from /export/home/drkirkby/sage-4.4.2/local/include/NTL/vec_ZZ.h:5,
                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZX.h:5,
                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZXFactoring.h:5,
                 from NTLconvert.h:23,
                 from cf_factor.cc:33:
/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h: In function ‘long int NTL::MulModPrecon(long int, long int, long int, long unsigned int)’:
/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h:1795: error: ‘MulHiUL’ was not declared in this scope
make[2]: *** [cf_factor.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src/factory'
make[1]: *** [install] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src'
make: *** [/export/home/drkirkby/sage-4.4.2/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.

real    0m13.142s
user    0m8.853s
sys     0m4.226s
sage: An error occurred while installing singular-3-1-0-4-20100214
```


The files 

```
$SAGE_LOCAL/lib/omalloc_debug.o
$SAGE_LOCAL/lib/omalloc.o
```


are being installed as 32-bit bit objects. 

It's somewhat worrying this does not build fully. If it built fully as 32-bit, one would expect converting it to 64-bit would be relatively easy (add option -m64), but the problem could be a bit more serious than this. I've not investigated yet. 


---

Comment by drkirkby created at 2010-05-24 18:21:40

For other OpenSolaris issues, see #9026


---

Comment by mkoeppe created at 2020-07-08 16:33:14

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:33:14

outdated, should be closed


---

Comment by dimpase created at 2020-07-08 18:37:26

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
