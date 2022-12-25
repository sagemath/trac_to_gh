# Issue 9723: Sage will not start on 64-bit Solaris 10 - looks like related to M4RI upgrade

archive/issues_009723.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @jhpalmieri @malb @qed777 @dandrake @jdemeyer\n\n## Hardware/Software\n* [Sun T5240](http://www.oracle.com/us/products/servers-storage/servers/sparc-enterprise/t-series/031584.htm)\n* [T2 PLUS](http://www.oracle.com/us/products/servers-storage/microelectronics/031459.htm) processors running at 1167 MHz. (16 cores and 128 hardware threads in total).\n* 32 GB RAM\n* No swap space\n* gcc 4.4.1 configured to use the Sun linker and assembler.\n* Sage 4.5.3.alpha0, with the following 4 new .spkg files, which are necessary to allow Sage to build on 64-bit on Solaris/OpenSolaris on both SPARC and x64.\n  * ECL - #9643. This was not necessary for 64-bit SPARC, but it would have been for 64-bit Solaris or OpenSolaris x86 builds, and was included in this build.\n  * ATLAS #9508\n  * Singular #9397 (Despite the ticket's says OpenSolaris, there is a critical 64-bit fix for Solaris 10 on SPARC too. Many of the problems first observed on a 64-bit OpenSolaris port also affect the 64-bit Solaris 10 SPARC port). \n  * zn_poly #9358 (Again, despite what the ticket's title is, this is also another fix which is essential for Sage to build 64-bit on Solaris 10 SPARC)\n\n == Background ==\nAlthough a fully stable copy of Sage on 64-bit Solaris 10 SPARC has never been built, Sage has at least built and able to do computations. See for example [factoring 323232323923321 on 64-bit Solaris SPARC](http://groups.google.co.uk/group/sage-devel/msg/63dd0f2d01bcfe4e). \n\nAs shown above, Sage 4.5.0 could be made to work, though I believe more recent versions have worked too. \n\nI've previously built Sage 64-bit on SPARC on both `t2.math.washington.edu` and on one of my own Solaris 10 SPARC systems - either my Sun Blade 1000 or my Sun Blade 2000 - I can not recall which). \n\n == The problem ==\n\n4.5.3.alpha0, with the four .spkg files mentioned above, builds on Solaris 10 SPARC. The file install.log shows:\n\n\n```\nTo install gap, gp, singular, etc., scripts\nin a standard bin directory, start sage and\ntype something like\n   sage: install_scripts('/usr/local/bin')\nat the Sage command prompt.\n\nTo build the documentation, run\n   make doc\n\nSage build/upgrade complete!\n```\n\n\nHowever, the build fails to start at all on `t2.math.washington.edu`, whereas a previous Sage was just about usable, though it was unstable. Instead 4.5.3.alpha0 fails with:\n\n\n```\nkirkby@t2:64 ~/t2/64/sage-4.5.3.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n| Sage Version 4.5.3.alpha0, Release Date: 2010-08-09                |\n| Type notebook() for the GUI, and license() for information.        |\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6 \n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9 \n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     71 \n     72 from sage.rings.all      import *\n---> 73 from sage.matrix.all     import *\n     74 \n     75 # This must come before Calculus -- it initializes the Pynac library.\n\n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/all.py in <module>()\n----> 1 \n      2 \n      3 from matrix_space import MatrixSpace, is_MatrixSpace\n      4 from constructor import matrix, Matrix, random_matrix, diagonal_matrix, identity_matrix, block_matrix, block_diagonal_matrix, jordan_block, zero_matrix\n      5 from matrix import is_Matrix\n      6 from berlekamp_massey import berlekamp_massey\n      7 \n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in <module>()\n     35 import matrix_generic_sparse\n     36 \n---> 37 import matrix_modn_dense\n     38 import matrix_modn_sparse\n     39 \n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/matrix_integer_dense.pxd in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:14829)()\n\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/bin/matrix_mod2_dense.pxd in init sage.matrix.matrix_integer_dense (sage/matrix/matrix_integer_dense.c:39010)()\n\nImportError: ld.so.1: python: fatal: relocation error: file /rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so: symbol mzd_lqup: referenced symbol not found\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\n == Likely cause ==\nmzd_lqup issues reported have been part of M4RI problems, but M4RI has not been updated recently to my knowledge.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9723\n\n",
    "created_at": "2010-08-11T06:05:12Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage will not start on 64-bit Solaris 10 - looks like related to M4RI upgrade",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9723",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @jhpalmieri @malb @qed777 @dandrake @jdemeyer

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
kirkby@t2:64 ~/t2/64/sage-4.5.3.alpha0$ ./sage
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

Issue created by migration from https://trac.sagemath.org/ticket/9723





---

archive/issue_comments_094822.json:
```json
{
    "body": "Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)",
    "created_at": "2010-08-11T12:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94822",
    "user": "https://github.com/malb"
}
```

Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)



---

archive/issue_comments_094823.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n> Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)\n\nI've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? \n\nWould it be worth while trying to install the 4MRI package before rebuilding the library? If so, will the libraries just be overwritten with new ones, or will there be old ones left which cause a problem? \n\nIt's odd why this problem is only seen on 64-bit Solaris!\n\nDave",
    "created_at": "2010-08-11T12:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94823",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:4 malb]:
> Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)

I've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? 

Would it be worth while trying to install the 4MRI package before rebuilding the library? If so, will the libraries just be overwritten with new ones, or will there be old ones left which cause a problem? 

It's odd why this problem is only seen on 64-bit Solaris!

Dave



---

archive/issue_comments_094824.json:
```json
{
    "body": "I'm cc'ing the release managers, who might know if the library patch got merged by mistake, without the library, or what else might have caused this. \n\nDave",
    "created_at": "2010-08-11T12:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94824",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm cc'ing the release managers, who might know if the library patch got merged by mistake, without the library, or what else might have caused this. 

Dave



---

archive/issue_comments_094825.json:
```json
{
    "body": "I know it's a long shot, but is #9721 conceivably related?",
    "created_at": "2010-08-11T12:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94825",
    "user": "https://github.com/kcrisman"
}
```

I know it's a long shot, but is #9721 conceivably related?



---

archive/issue_comments_094826.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> Replying to [comment:4 malb]:\n> > Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)\n> \n> I've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? \n\nI did not find any mention of the patches at #9475 in `hg log -R devel/sage`.\n\nMaybe it's worth it to try with #9475 + #9717?",
    "created_at": "2010-08-11T22:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94826",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:5 drkirkby]:
> Replying to [comment:4 malb]:
> > Hi, this is indeed an error which comes from M4RI. However, I don't understand why. It seems you have a patch applied to the Sage tree which uses the new M4RI API but the new M4RI SPKG is not included (IIRC alpha0 is not supposed to include the M4RI update)
> 
> I've not applied any patch. Could it be the patch was applied by mistake in the 4.5.3.alpha0 source code? 

I did not find any mention of the patches at #9475 in `hg log -R devel/sage`.

Maybe it's worth it to try with #9475 + #9717?



---

archive/issue_comments_094827.json:
```json
{
    "body": "I see what's happened here. By mistake I downloaded the latest M4RI. I have two packages in spkg/standard:\n\n\n```\n-rw-r--r--   1 drkirkby sage     1236812 Jul 25 23:52 libm4ri-20100221.spkg\n-rw-r--r--   1 drkirkby sage      908163 Jul 27 11:12 libm4ri-20100730.spkg\n```\n\n\nI rekon libm4ri-20100730.spkg was installed instead of the older one. But since I'd not put in any of the patches, it fails. \n\nIn the short term I am going to remove the updated .spkg and build the older one, then remake the library. Sage has been very unstable on 64-bit SPARC, so I'm not keen to introduce even more possible issues that have not been tested and found fine by many. \n\nDave",
    "created_at": "2010-08-11T22:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94827",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I see what's happened here. By mistake I downloaded the latest M4RI. I have two packages in spkg/standard:


```
-rw-r--r--   1 drkirkby sage     1236812 Jul 25 23:52 libm4ri-20100221.spkg
-rw-r--r--   1 drkirkby sage      908163 Jul 27 11:12 libm4ri-20100730.spkg
```


I rekon libm4ri-20100730.spkg was installed instead of the older one. But since I'd not put in any of the patches, it fails. 

In the short term I am going to remove the updated .spkg and build the older one, then remake the library. Sage has been very unstable on 64-bit SPARC, so I'm not keen to introduce even more possible issues that have not been tested and found fine by many. 

Dave



---

archive/issue_comments_094828.json:
```json
{
    "body": "I suspect this can probably be closed as invalid, since I made a mistake.",
    "created_at": "2010-08-11T22:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94828",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I suspect this can probably be closed as invalid, since I made a mistake.



---

archive/issue_comments_094829.json:
```json
{
    "body": "Any update on this? If it really is invalid, we can ask the release manager to close it.  Or drkirkby can too, since I think he has privileges :)",
    "created_at": "2011-03-04T16:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94829",
    "user": "https://github.com/kcrisman"
}
```

Any update on this? If it really is invalid, we can ask the release manager to close it.  Or drkirkby can too, since I think he has privileges :)



---

archive/issue_comments_094830.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-03-04T22:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94830",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution: invalid



---

archive/issue_events_024331.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2011-03-04T22:30:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9723#event-24331"
}
```



---

archive/issue_comments_094831.json:
```json
{
    "body": "Yes, this was my mistake and can be closed as invalid.",
    "created_at": "2011-03-04T22:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94831",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, this was my mistake and can be closed as invalid.



---

archive/issue_events_024332.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2011-03-04T22:30:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9723#event-24332"
}
```



---

archive/issue_comments_094832.json:
```json
{
    "body": "Replying to [comment:12 drkirkby]:\n> Yes, this was my mistake and can be closed as invalid. \n\nPlease do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.",
    "created_at": "2011-03-06T15:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94832",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:12 drkirkby]:
> Yes, this was my mistake and can be closed as invalid. 

Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.



---

archive/issue_comments_094833.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Replying to [comment:12 drkirkby]:\n> > Yes, this was my mistake and can be closed as invalid. \n> \n> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.\nMight be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?",
    "created_at": "2011-03-07T00:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94833",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:13 jdemeyer]:
> Replying to [comment:12 drkirkby]:
> > Yes, this was my mistake and can be closed as invalid. 
> 
> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.
Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?



---

archive/issue_comments_094834.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Replying to [comment:13 jdemeyer]:\n> > Replying to [comment:12 drkirkby]:\n> > > Yes, this was my mistake and can be closed as invalid. \n> > \n> > Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.\n> Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?\n\nWhich kind of \"privileges\" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.\n\nIt is more a matter of making sure the release manager can keep track of opening/closing tickets.  Currently, I list all closed tickets in the release notes (this is how it was done historically, although one could argue against this practice).",
    "created_at": "2011-03-07T10:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94834",
    "user": "https://github.com/jdemeyer"
}
```

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

archive/issue_comments_094835.json:
```json
{
    "body": "> > > > Yes, this was my mistake and can be closed as invalid. \n> > > \n> > > Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.\n> > Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?\n> \n> Which kind of \"privileges\" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.\n\nOk, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?",
    "created_at": "2011-03-07T13:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94835",
    "user": "https://github.com/kcrisman"
}
```

> > > > Yes, this was my mistake and can be closed as invalid. 
> > > 
> > > Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.
> > Might be worth getting some elucidation from the devel list on this, then, as William gave a few people like Minh and Dave privileges for just this reason.  Is there really a positive review of anything when Dave just made a mistake?  Or are you saying just in order for the release manager to keep track of what is happening?
> 
> Which kind of "privileges" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.

Ok, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?



---

archive/issue_comments_094836.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n\n> > Which kind of \"privileges\" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.\n> \n> Ok, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?\n\nI can't find the message, but William wrote something to the effect on sage-devel that he did not want people closing tickets unless they had admin privileges on the trac server. \n\nI did not feel in this instance the closing this ticket as invalid should have any impact on the current release, which is why I did it without discussing it with the release manager. \n\nDave",
    "created_at": "2011-03-07T14:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94836",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:16 kcrisman]:

> > Which kind of "privileges" do you mean?  Everybody has the ability to close tickets, you don't any special privileges for that.
> 
> Ok, then I must have misinterpreted something a (long) while ago.  It seemed that some actions were not possible except for those who had been given permission to do them, and I thought that closing tickets was one of them.  Now I wonder what that action was?

I can't find the message, but William wrote something to the effect on sage-devel that he did not want people closing tickets unless they had admin privileges on the trac server. 

I did not feel in this instance the closing this ticket as invalid should have any impact on the current release, which is why I did it without discussing it with the release manager. 

Dave



---

archive/issue_comments_094837.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Replying to [comment:12 drkirkby]:\n> > Yes, this was my mistake and can be closed as invalid. \n> \n> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.\n\nI can't possibly see why it should be \"positive review\". There's no patch or change for anyone to review. I guess I \"reviewed\" my decision to create the ticket, and decided my original decision to open the ticket was incorrect. But now I'm listed as a reviewer!!!\n\nDave",
    "created_at": "2011-03-07T14:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9723#issuecomment-94837",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:13 jdemeyer]:
> Replying to [comment:12 drkirkby]:
> > Yes, this was my mistake and can be closed as invalid. 
> 
> Please do not close tickets yourself.  Instead put it to `positive_review` with a `sage-duplicate/invalid/wontfix` milestone.

I can't possibly see why it should be "positive review". There's no patch or change for anyone to review. I guess I "reviewed" my decision to create the ticket, and decided my original decision to open the ticket was incorrect. But now I'm listed as a reviewer!!!

Dave
