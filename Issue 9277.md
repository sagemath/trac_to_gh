# Issue 9277: Flint's spkg-check file does not work on 64-bit (SAGE64 only works on OS X)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-19 21:38:52

Assignee: AlexGhitza

CC:  jsp

Just when I thought I'd got rid of all the junk like this from spkg-install files:


---

Comment by drkirkby created at 2010-06-19 21:44:49

Changing component from algebra to build.


---

Comment by drkirkby created at 2010-06-19 21:44:49

Changing assignee from AlexGhitza to GeorgSWeber.


---

Comment by drkirkby created at 2010-06-19 23:57:10

Here's an updated package

http://boxen.math.washington.edu/home/kirkby/patches/flint-1.5.0.p5.spkg

which has a trivial fix to remove the OS X restriction. 

It was also desirable to remove these 3 lines from spkg-install, since if SAGE_CHECK was set to yes, the test suite got executed twice, which just wastes time. 


```
if [ "$SAGE_CHECK" = "yes" ]; then
    cd ..; ./spkg-check
fi
```


After that change, on my Sun Ultra 27 running OpenSolaris x64, the test suite builds, runs once, and passes all the tests. 



```
Testing zmod_poly_factor()... Cpu = 2060 ms  Wall = 2061 ms ... ok
Testing zmod_poly_2x2_mat_mul_classical_strassen()... Cpu = 330 ms  Wall = 326 ms ... ok
Testing zmod_poly_2x2_mat_mul()... Cpu = 1070 ms  Wall = 1073 ms ... ok

All tests passed
Testing zmod_mat_row_reduce_gauss()... Cpu = 470 ms  Wall = 473 ms ... ok

All tests passed
Testing ZZ_to_fmpz()... Cpu = 530 ms  Wall = 536 ms ... ok
Testing ZZ_to_F_mpz()... Cpu = 460 ms  Wall = 457 ms ... ok
Testing ZZX_to_fmpz_poly()... Cpu = 1710 ms  Wall = 1710 ms ... ok

All tests passed
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/flint-1.5.0.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing flint-1.5.0.p5.spkg
```



---

Comment by drkirkby created at 2010-06-19 23:57:10

Changing status from new to needs_review.


---

Attachment

Mercurial patch which permits a 64-bit build of test suite and ensures tests dont run twice


---

Comment by jsp created at 2010-06-20 10:21:53

Looks good to me.

Positive review.

Jaap


---

Comment by jsp created at 2010-06-20 10:21:53

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:42:08

Resolution: fixed
