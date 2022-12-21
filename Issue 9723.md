# Issue 9723: Sage will not start on 64-bit Solaris 10 - looks like related to M4RI upgrade

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-11 06:05:12

Assignee: drkirkby

CC:  jsp jhpalmieri malb mpatel ddrake jdemeyer

## Hardware/Software
 * [Sun T5240](http://www.oracle.com/us/products/servers-storage/servers/sparc-enterprise/t-series/031584.htm)
 * [T2 PLUS](http://www.oracle.com/us/products/servers-storage/microelectronics/031459.htm) processors running at 1167 MHz. (16 cores and 128 hardware threads in total).
 * 32 GB RAM
 * No swap space
 * gcc 4.4.1 configured to use the Sun linker and assembler.
 * Sage 4.5.3.alpha0, with the following 4 new .spkg files, which are necessary to allow Sage to build on 64-bit on Solaris/OpenSolaris on both SPARC and x64.
   * ECL - #9643. This was not necessary for 64-bit SPARC, but it would have been for 64-bit Solaris or OpenSolaris x86 builds, and was included in this build.
   * ATLAS #9508
   * Singular #9397 (Despite the ticket's says OpenSolaris, there is a critical 64-bit fix for Solaris 10 on SPARC too. Many of the problems first observed on a 64-bit OpenSolaris port also affect the 64-bit Solaris 10 SPARC port). 
   * zn_poly #9358 (Again, despite what the ticket's title is, this is also another fix which is essential for Sage to build 64-bit on Solaris 10 SPARC)

 == Background ==
Although a fully stable copy of Sage on 64-bit Solaris 10 SPARC has never been built, Sage has at least built and able to do computations. See for example [factoring 323232323923321 on 64-bit Solaris SPARC](http://groups.google.co.uk/group/sage-devel/msg/63dd0f2d01bcfe4e). 

As shown above, Sage 4.5.0 could be made to work, though I believe more recent versions have worked too. 

I've previously built Sage 64-bit on SPARC on both `t2.math.washington.edu` and on one of my own Solaris 10 SPARC systems - either my Sun Blade 1000 or my Sun Blade 2000 - I can not recall which). 

 == The problem ==

4.5.3.alpha0, with the four .spkg files mentioned above, builds on Solaris 10 SPARC. The file install.log shows:


```
To install gap, gp, singular, etc., scripts
in a standard bin directory, start sage and
type something like
   sage: install_scripts('/usr/local/bin')
at the Sage command prompt.

To build the documentation, run
   make doc

Sage build/upgrade complete!
```


However, the build fails to start at all on `t2.math.washington.edu`, whereas a previous Sage was just about usable, though it was unstable. Instead 4.5.3.alpha0 fails with:


```
kirkby`@`t2:64 ~/t2/64/sage-4.5.3.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
| Sage Version 4.5.3.alpha0, Release Date: 2010-08-09                |
| Type notebook() for the GUI, and license() for information.        |
/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/all.py in <module>()
     71 
     72 from sage.rings.all      import *
---> 73 from sage.matrix.all     import *
     74 
     75 # This must come before Calculus -- it initializes the Pynac library.


/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/all.py in <module>()
----> 1 
      2 
      3 from matrix_space import MatrixSpace, is_MatrixSpace
      4 from constructor import matrix, Matrix, random_matrix, diagonal_matrix, identity_matrix, block_matrix, block_diagonal_matrix, jordan_block, zero_matrix
      5 from matrix import is_Matrix
      6 from berlekamp_massey import berlekamp_massey
      7 

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in <module>()
     35 import matrix_generic_sparse
     36 
---> 37 import matrix_modn_dense
     38 import matrix_modn_sparse
     39 

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/matrix_integer_dense.pxd in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:14829)()

/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/matrix_mod2_dense.pxd in init sage.matrix.matrix_integer_dense (sage/matrix/matrix_integer_dense.c:39010)()

ImportError: ld.so.1: python: fatal: relocation error: file /rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so: symbol mzd_lqup: referenced symbol not found
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

 == Likely cause ==
mzd_lqup issues reported have been part of M4RI problems, but M4RI has not been updated recently to my knowledge.


---

Comment by malb created at 2010-08-11 12:12:51

Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)


---

Comment by drkirkby created at 2010-08-11 12:24:53

Replying to [comment:4 malb]:
> Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)

I've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? 

Would it be worth while trying to install the 4MRI package before rebuilding the library? If so, will the libraries just be overwritten with new ones, or will there be old ones left which cause a problem? 

It's odd why this problem is only seen on 64-bit Solaris!

Dave


---

Comment by drkirkby created at 2010-08-11 12:29:09

I'm cc'ing the release managers, who might know if the library patch got merged by mistake, without the library, or what else might have caused this. 

Dave


---

Comment by kcrisman created at 2010-08-11 12:55:17

I know it's a long shot, but is #9721 conceivably related?


---

Comment by mpatel created at 2010-08-11 22:30:15

Replying to [comment:5 drkirkby]:
> Replying to [comment:4 malb]:
> > Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)
> 
> I've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? 

I did not find any mention of the patches at #9475 in `hg log -R devel/sage`.

Maybe it's worth it to try with #9475 + #9717?


---

Comment by drkirkby created at 2010-08-11 22:42:38

I see what's happened here. By mistake I downloaded the latest M4RI. I have two packages in spkg/standard:


```
-rw-r--r--   1 drkirkby sage     1236812 Jul 25 23:52 libm4ri-20100221.spkg
-rw-r--r--   1 drkirkby sage      908163 Jul 27 11:12 libm4ri-20100730.spkg
```


I rekon libm4ri-20100730.spkg was installed instead of the older one. But since I'd not put in any of the patches, it fails. 

In the short term I am going to remove the updated .spkg and build the older one, then remake the library. Sage has been very unstable on 64-bit SPARC, so I'm not keen to introduce even more possible issues that have not been tested and found fine by many. 

Dave


---

Comment by drkirkby created at 2010-08-11 22:43:04

I suspect this can probably be closed as invalid, since I made a mistake.


---

Comment by kcrisman created at 2011-03-04 16:49:51

Any update on this? If it really is invalid, we can ask the release manager to close it.  Or drkirkby can too, since I think he has privileges :)


---

Comment by drkirkby created at 2011-03-04 22:30:52

Resolution: invalid


---

Comment by drkirkby created at 2011-03-04 22:30:52

Yes, this was my mistake and can be closed as invalid.


---

Comment by jdemeyer created at 2011-03-06 15:46:24

Replying to [comment:12 drkirkby]:
> Yes, this was my mistake and can be closed as invalid. 

Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.


---

Comment by kcrisman created at 2011-03-07 00:51:57

Replying to [comment:13 jdemeyer]:
> Replying to [comment:12 drkirkby]:
> > Yes, this was my mistake and can be closed as invalid. 
> 
> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.
Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?


---

Comment by jdemeyer created at 2011-03-07 10:31:11

Replying to [comment:14 kcrisman]:
> Replying to [comment:13 jdemeyer]:
> > Replying to [comment:12 drkirkby]:
> > > Yes, this was my mistake and can be closed as invalid. 
> > 
> > Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.
> Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?

Which kind of "privileges" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.

It is more a matter of making sure the release manager can keep track of opening/closing tickets.  Currently, I list all closed tickets in the release notes (this is how it was done historically, although one could argue against this practice).


---

Comment by kcrisman created at 2011-03-07 13:44:20

> > > > Yes, this was my mistake and can be closed as invalid. 
> > > 
> > > Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.
> > Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?
> 
> Which kind of "privileges" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.

Ok, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?


---

Comment by drkirkby created at 2011-03-07 14:14:04

Replying to [comment:16 kcrisman]:

> > Which kind of "privileges" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.
> 
> Ok, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?

I can't find the message, but William wrote something to the effect on sage-devel that he did not want people closing tickets unless they had admin privileges on the trac server. 

I did not feel in this instance the closing this ticket as invalid should have any impact on the current release, which is why I did it without discussing it with the release manager. 

Dave


---

Comment by drkirkby created at 2011-03-07 14:17:15

Replying to [comment:13 jdemeyer]:
> Replying to [comment:12 drkirkby]:
> > Yes, this was my mistake and can be closed as invalid. 
> 
> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.

I can't possibly see why it should be "positive review". There's no patch or change for anyone to review. I guess I "reviewed" my decision to create the ticket, and decided my original decision to open the ticket was incorrect. But now I'm listed as a reviewer!!!

Dave
