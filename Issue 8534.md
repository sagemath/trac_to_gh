# Issue 8534: Optional packages that fail to install on Solaris 10 (SPARC) on sage-4.3.4.alpha1

Issue created by migration from https://trac.sagemath.org/ticket/8534

Original creator: drkirkby

Original creation time: 2010-03-14 01:31:15

Assignee: tbd

CC:  jsp mvngu jhpalmieri chapoton dimpase

Sage version 4.3.4.alpha1 is the first release to actually build and pass all doc tests on Solaris 10 (SPARC). A list is given of the succeess and failures. The system used was:

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow optional packages to install. 

 == Optional packages which fail to install == 
Here is a list of the optional packages which fail to install. Hopefully this list can be reduced over time. 

 * ace-5.0.p0 #8531
 * database_gap-4.4.12 #8514
 * database_stein_watkins_mini #8512
 * extra_docs-20070208 #8518
 * frobby-0.7.6 #8515
 * gap_packages-4.4.12_2 #8520
 * ginv-1.9-20080723 #8516
 * gmpy-1.0.1 ##8517
 * graphviz-2.16.1.p0 #7438
 * libcocoa-0.9930 #8521 (see also #8527)
 * mpi4py-1.1.0 #8532
 * nauty-24b7.p1 #7439 (also fails on Ununta 9.10)
 * openmpi-1.1.4 #8522 (this is an old version of MPI)
 * p_group_cohomology-1.2 ##8523
 * valgrind (this will never install, as it is x86 only)


 == Optional packages that build successfully == 

 * biopython-1.53.p0
 * cbc-2.3.p1
 * cunningham_tables-1.0
 * database_cremona_ellcurve-20071019.p0
 * database_jones_numfield-v4
 * database_kohel-20060803
 * database_odlyzko_zeta
 * database_sloane_oeis-2005-12
 * database_symbolic_data-20070206
 * fricas-1.0.8
 * gdbm-1.8.3
 * glpk-4.38.p4
 * gnuplotpy-1.8
 * guppy-0.1.8
 * java3d-20070901
 * jsmath-image-fonts-1.4.p3
 * kash3-2008-07-31
 * knoboo-20080411
 * lie-2.2.2.p3
 * lrs-4.2b.p1
 * mpc-0.5.p0
 * nzmath-0.6.0
 * openopt-0.24
 * openssl-0.9.8d.p1
 * phc-2.3.53.p0
 * pyopenssl-0.8
 * pyx-0.10
 * sage-mode-0.6
 * trac-0.11.5.p0

 == Important == 
At the time of writing, no doc tests have been run on the installed packages


---

Comment by kcrisman created at 2012-06-05 14:02:00

Removing fixed ones, and also 
 * frobby-0.7.6 #8515
because it is now an experimental spkg.  Updating #8515 accordingly.


---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-19 18:48:31

Resolution: invalid
