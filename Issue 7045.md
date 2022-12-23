# Issue 7045: [with spkg; needs review] update libgcrypt to the latest version 1.4.4

Issue created by migration from https://trac.sagemath.org/ticket/7045

Original creator: drkirkby

Original creation time: 2009-09-28 01:11:08

Assignee: tbd

CC:  mvngu

The current libgcrypt in Sage will not build with Sun Studio. I managed to mess up an update #6758, but Minh's correction ignores my fixes to the C source code, so that will not build on Sun Studio. 

Here is an spkg with the latest upstream version. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.4/

It's been tested on

 * Sun Studio 12.1 on my own SPARC running Solaris 10 update 7 in 32-bit mode
 * sage.math (64-bit)
 * bsd.math in 32-bit mode only 







---

Comment by mvngu created at 2009-09-28 06:39:00

I have checked in all existing changes in David's name. Based on David's spkg, I did some general clean up:

 * spell check the files `SPKG.txt` and `spkg-install`
 * format spkg-check and spkg-install in a consistent way
 
A new spkg based on David's and with the above changes is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/libgcrypt-1.4.4.p0.spkg


---

Comment by mvngu created at 2009-10-01 06:27:07

See #5833 for a duplicate of the current ticket.


---

Comment by was created at 2009-10-01 15:52:09


```
> > Building on 64-bit SuSE with SAGE_CHECK="yes" failed at libgcrypt,
> > with a bunch of errors in the gcrypt test script:
>
> Can you try using the updated libgcrypt spkg at ticket #7045 [1]?
>
> [1]http://trac.sagemath.org/sage_trac/ticket/7045
>
> --
> Regards
> Minh Van Nguyen

The new spkg 1.4.4.p0 seems to fix the problem.

David
```



---

Comment by awebb created at 2009-10-04 09:55:34

Built with SAGE_CHECK="yes" on Ubuntu 9.10 beta (AMD64) and everything worked. Also worked in the context of a 'make testlong'. 

Adam


---

Comment by mhansen created at 2009-10-16 08:56:48

Adam,

Do you have a copy of this spkg?  The link above is now broken.


---

Comment by mvngu created at 2009-10-16 09:16:59

Replying to [comment:6 mhansen]:
> Do you have a copy of this spkg?  The link above is now broken.

The spkg is now restored. Here are the changes I added in addition to drkirkby's changes:

 * committed drkirkby's changes in his name
 * spell check the files `SPKG.txt` and `spkg-install`
 * format `spkg-check` and `spkg-install` in a consistent way
 * add executable bits to `spkg-install`


---

Comment by mhansen created at 2009-10-16 09:20:57

Resolution: fixed


---

Comment by mhansen created at 2009-10-16 09:20:57

Looks good.
