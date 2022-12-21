# Issue 642: update to GMP-ECM-6.1.3

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-12 15:51:03

Assignee: mabshoff

CC:  michael.abshoff@googlemail.com


```
Hi,

GMP-ECM-6.1.3 has been released. This is a bugfix release.

Changes between ecm-6.1.2 and ecm-6.1.3:

   * fixed incorrect computation of memory use in stage 2, especially for
     machines that use Kronecker-Schoenhage multiplication even for large
     degrees, such as Core 2
   * fixed -B2scale option whose value hadn't been passed to the factoring
     routines
   * fixed default B2min for P-1 which could be truncated on 32 bit 
machines,
     causing stage 2 to take a little longer than necessary
   * fixed bug for modular multiplication modulo Fermat numbers 2^2^n+1, 
where
     a result of 2^2^n would be truncated to 0


The new version is available at https://gforge.inria.fr/projects/ecm/.

We would like to thank Peter-Lawrence Montgomery, Andreas Schindel and 
George Woltman for their bug reports.

Enjoy,
Alex
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-09-12 15:51:23

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-12 15:51:23

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-09-14 20:11:28

There is an update spkg at

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/ecm-6.1.3.spkg 

Changelog is in SPKG.txt

Cheers,

Michael


---

Comment by was created at 2007-09-14 21:48:16

Resolution: fixed
