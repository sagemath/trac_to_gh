# Issue 4024: [with spkg, needs review] upgrade M4RI to newest upstream release

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-31 19:21:03

Assignee: malb

Keywords: spkg

The newest M4RI upstream release improves performance, has some bug fixes and support for parallel matrix elimination (only makes sense on an Opteron). 

## 20080624 (Sage 3.1.2.alpha3)

### Matrix Elimination
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.809 |  1.820 |  1.821 |  1.850 |
| 16384 |  7.625 |  7.772 |  7.761 |  8.090 |
| 20000 | 13.746 | 13.932 | 13.899 | 14.370 |
| 32000 | 45.865 | 46.001 | 46.081 | 46.121 |
### Matrix Multiplication
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.817 |  1.822 |  1.821 |  1.839 |
| 16384 |  6.856 |  6.895 |  6.865 |  7.012 |
| 20000 | 12.690 | 12.703 | 12.699 | 12.761 |
| 32000 | 52.878 | 53.929 | 53.460 | 58.142 |
## 20080826 (newest upstream)
### Matrix Elimination
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.501 |  1.509 |  1.515 |  1.515 |
| 16384 |  6.468 |  6.670 |  6.801 |  6.990 |
| 20000 | 11.877 | 11.901 | 11.910 | 11.934 |
| 32000 | 41.513 | 41.623 | 41.671 | 41.691 |
### Matrix Multiplication


---

Comment by malb created at 2008-08-31 19:22:00

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080831.spkg

It is based on 20080624 from 3.1.2.alpha3 so it should have all SPKG.txt fixes applied.


---

Comment by malb created at 2008-09-01 11:23:57

See #4027


---

Comment by mabshoff created at 2008-09-01 12:10:21

The spkg at

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg

works for me and fixes the at #4027 reported segfault on OSX.

Positive review.

Cheers,

Micheal


---

Comment by mabshoff created at 2008-09-01 12:11:08

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 12:11:08

Merged in Sage 3.1.2.alpha4
