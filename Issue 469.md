# Issue 469: Integrate the PolyBoRi framework

Issue created by migration from https://trac.sagemath.org/ticket/469

Original creator: malb

Original creation time: 2007-08-20 22:01:34

Assignee: was

CC:  malb

PolyBoRi is a framework for doing computation within the boolean ring, i.e. the ring F_2[x_1,...,x_n]/<x_1<sup>2+x_1,x_n</sup>2+x_n>. From the benchmarks presented in http://www.itwm.fraunhofer.de/zentral/download/berichte/bericht122.pdf it not only features very fast arithmetic in that ring but also a very fast Gröbner basis engine. PolyBoRi is GPL'd and should be wrapped for SAGE.


---

Comment by malb created at 2007-08-20 22:01:47

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-21 22:53:41

Changing assignee from malb to burcin.


---

Comment by mabshoff created at 2007-12-04 14:21:14

Alexander Dreyer did comment on the build time of PolyBoRi:

```
The essential part of PolyBoRi (using the built-ininterface) can be
built in about 3 minutes on a Intel(R) Xeon(R) CPU5148  @ 2.33GHz
(using one cpu only). I'll try to find the corresponding scons
commands for the spkg and the Sage-wrapper and give to to Burcin.

Best regards,
  Alexander
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-04 14:54:04


```
There is a new PolyBoRi package available at:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg

Changes are:
        - Alexander's changes to speed up the build process
        - Update to the latest CVS version
        - pass on MAKEOPTS to scons to allow parallel builds

Building the package takes 4 mins 20 seconds on a single Intel(R)
Pentium (R) D CPU 3.40GHz. Parallel make options (-jn) speed up the
build as expected.

Burcin 
```



---

Comment by mabshoff created at 2007-12-09 14:18:28

Okay, I have stuck 

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg

into 2.9.alpha2. Burcin, please send me a patch/bundle against some 2.9 release for the code that does the actual integrations with Sage.

Cheers,

Michael


---

Comment by burcin created at 2007-12-10 17:31:04

New bundle against 2.9.alpha4:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori_wrapper-2.9.alpha4-20071204.hg

New package:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r5.spkg

Changes to the package:

r4 -> r5

* Make symlinks relative

r3 -> r4

* Remove popd, pushd from spkg-install


---

Comment by burcin created at 2007-12-10 17:31:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-10 22:34:23

Ok, I updated the spkg as well applied the bundle. I also disabled doctests until you can send in the missing bits.

Cheers,

Michael


---

Comment by burcin created at 2007-12-12 13:01:48

fix doctests in pbori.pyx


---

Attachment

Merged in 2.9.alpha6. - Finally. Doctests pass.


---

Comment by mabshoff created at 2007-12-12 18:37:38

Resolution: fixed
