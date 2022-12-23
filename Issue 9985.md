# Issue 9985: MPFI fails to build on AIX 5.3 - appears not to know .a is the extension for shared libraries on AIX

Issue created by migration from https://trac.sagemath.org/ticket/9986

Original creator: drkirkby

Original creation time: 2010-09-23 21:00:39

Assignee: drkirkby

CC:  cwitty@newtonlabs.com chapoton

Using the following system: 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1

MPFI fails to build. The important part of the error message is:


```
checking for gmp.h... yes
checking for valid GMP... yes
checking for mpfr.h... yes
checking MPFR library... configure: error: /home/users/drkirkby/sage-4.6.alpha1/local/lib/libmpfr.so or libmpfr.dylib not found
Error configuring mpfi

real    4m28.501s
user    0m52.337s
sys     0m27.257s
sage: An error occurred while installing mpfi-1.3.4-cvs20071125.p8
```


The extension for shared libraries on AIX is .a - not .so or .dylib.

Dave 


---

Attachment

Build failure observed on an RS/6000 running AIX 5.3


---

Comment by Snark created at 2011-05-02 11:37:45

Could you give MPFI's latest svn a try (outside of sage, I mean)?

I have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...


---

Comment by Snark created at 2011-05-02 11:37:45

Changing status from new to needs_info.


---

Comment by drkirkby created at 2011-05-03 06:29:37

Replying to [comment:1 Snark]:
> Could you give MPFI's latest svn a try (outside of sage, I mean)?
> 
> I have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...

Sure, my AIX box is not on now, but I'll try later. 

I later found out that .so is a permitted extension for the libraries on AIX, though all the systems libraries are .a. It appears the .a files can have both static and shared objects in the same library - I don't fully understand it, and are no AIX guru. I just have an old machine I bought long ago to ensure my code was portable. 

I'll give the svn a go later today after I've woke up properly and powered up the RS/6000. 

BTW, I'm not sure if you are an MPFI developer, but if so, and the latest svn does not work, you are welcome to have an account on the AIX box to try. Either way, on AIX, I think it would be useful if you permitted the .a extension too. 


Dave


---

Comment by drkirkby created at 2011-05-03 06:35:25

Replying to [comment:1 Snark]:
> Could you give MPFI's latest svn a try (outside of sage, I mean)?

Can you please give me the command to get the latest svn snapshot. I tried googling, but can only find links to download stable versions, not snapshots. 

Dave


---

Comment by Snark created at 2011-05-03 07:24:55

I'm not an MPFI developper -- I just looked at it because I have things to do within sage which require good quality packages (from a portability point of view).

This will get you their most up-to-date sources :
svn checkout svn://scm.gforge.inria.fr/svn/mpfi/trunk/mpfi mpfi

Notice that as it isn't a proper snapshot but the raw code, you'll need to run ./autogen.sh, then make -- the ./autogen.sh step will build and run the configure script.

Hope this helps.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2020-06-25 13:33:47

Resolution: invalid
