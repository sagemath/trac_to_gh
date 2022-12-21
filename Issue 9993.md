# Issue 9993: gcc 4.2.4 generates an internal compiler issue when buidling symmetrica on AIX 5.3

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-24 00:45:18

Assignee: tbd

This would not appear to be a Sage problem as such, but rather of gcc. 
 == Hardware and software ==
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 (which has singular-3-1-1-4.p2)

 == The problem ==

```
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE zykelind.c
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE zyk.c
: In function 'mult_hashtable_hashtable_faktor':
:596: internal compiler error: Segmentation fault
Please submit a full bug report,
with preprocessed source if appropriate.
See <URL:http://gcc.gnu.org/bugs.html> for instructions.
make[2]: *** [tmh.o] Error 1
make[2]: Target `test' not remade because of errors.
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/symmetrica-2.0.p5/src'
Error building symmetrica.

real    37m5.981s
user    87m12.220s
sys     0m31.967s
sage: An error occurred while installing symmetrica-2.0.p5
```



---

Comment by drkirkby created at 2010-09-24 00:49:03

Changing component from PLEASE CHANGE to AIX or HP-UX ports.


---

Comment by drkirkby created at 2010-09-24 00:49:03

Changing assignee from tbd to drkirkby.


---

Comment by mmezzarobba created at 2015-04-13 13:14:00

Does anyone still care?


---

Comment by mmezzarobba created at 2015-04-13 13:14:00

Changing status from new to needs_info.


---

Comment by aapitzsch created at 2015-06-27 11:10:40

Changing status from needs_info to positive_review.


---

Comment by aapitzsch created at 2015-06-27 11:10:40

Replying to [comment:2 mmezzarobba]:
> Does anyone still care?

No.


---

Comment by vbraun created at 2015-07-17 20:06:20

Resolution: wontfix
