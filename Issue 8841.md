# Issue 8841: os x 10.4 -- sage-4.4.1 doesn't start up

archive/issues_008841.json:
```json
{
    "body": "Assignee: tbd\n\nThis is a result of updating the parI spkg, probably -- see #8837.\n\nAfter applying #8837, the sage build finishes.  However, startup fails:\n\n```\nvarro:~/screen/varro/sage-4.4.1.alpha3 wstein$ ./sage -br\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 4.00543212891e-05 seconds\nFinished compiling Cython code (time = 4.20907592773 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.395891904831 seconds.\nrunning install_lib\nrunning install_egg_info\nRemoving /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n| Sage Version 4.4.1.alpha3, Release Date: 2010-04-30                |\n| Type notebook() for the GUI, and license() for information.        |\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/private/var/automount/home/wstein/screen/varro/sage-4.4.1.alpha3/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6 \n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9 \n\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     62 get_sigs()\n     63 \n---> 64 from sage.misc.all       import *         # takes a while\n     65 \n     66 from sage.misc.sh import sh\n\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/all.py in <module>()\n     68 from sage_eval import sage_eval, sageobj\n     69 \n---> 70 from sage_input import sage_input\n     71 \n     72 from cython import cython_lambda, cython_create_local_so\n\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/sage_input.py in <module>()\n    161 \"\"\"\n    162 \n--> 163 from sage.misc.functional import parent\n    164 import math\n    165 \n\n/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/functional.py in <module>()\n     36 \n     37 \n---> 38 from sage.rings.complex_double import CDF\n     39 from sage.rings.real_double import RDF, RealDoubleElement\n     40 \n\n/private/var/automount/home/wstein/screen/varro/sage-4.4.1.alpha3/local/bin/gen.pxd in init sage.rings.complex_double (sage/rings/complex_double.c:14177)()\n\nImportError: dlopen(/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/libs/pari/gen.so, 2): Symbol not found: _rnfidealtwoelement\n  Referenced from: /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/libs/pari/gen.so\n  Expected in: /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib//libcsage.dylib\n\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8841\n\n",
    "created_at": "2010-05-02T20:13:00Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "os x 10.4 -- sage-4.4.1 doesn't start up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8841",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

This is a result of updating the parI spkg, probably -- see #8837.

After applying #8837, the sage build finishes.  However, startup fails:

```
varro:~/screen/varro/sage-4.4.1.alpha3 wstein$ ./sage -br

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 4.00543212891e-05 seconds
Finished compiling Cython code (time = 4.20907592773 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.395891904831 seconds.
running install_lib
running install_egg_info
Removing /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
| Sage Version 4.4.1.alpha3, Release Date: 2010-04-30                |
| Type notebook() for the GUI, and license() for information.        |
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/private/var/automount/home/wstein/screen/varro/sage-4.4.1.alpha3/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/all.py in <module>()
     62 get_sigs()
     63 
---> 64 from sage.misc.all       import *         # takes a while
     65 
     66 from sage.misc.sh import sh

/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/all.py in <module>()
     68 from sage_eval import sage_eval, sageobj
     69 
---> 70 from sage_input import sage_input
     71 
     72 from cython import cython_lambda, cython_create_local_so

/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/sage_input.py in <module>()
    161 """
    162 
--> 163 from sage.misc.functional import parent
    164 import math
    165 

/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/misc/functional.py in <module>()
     36 
     37 
---> 38 from sage.rings.complex_double import CDF
     39 from sage.rings.real_double import RDF, RealDoubleElement
     40 

/private/var/automount/home/wstein/screen/varro/sage-4.4.1.alpha3/local/bin/gen.pxd in init sage.rings.complex_double (sage/rings/complex_double.c:14177)()

ImportError: dlopen(/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/libs/pari/gen.so, 2): Symbol not found: _rnfidealtwoelement
  Referenced from: /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/python2.6/site-packages/sage/libs/pari/gen.so
  Expected in: /home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib//libcsage.dylib

Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


Issue created by migration from https://trac.sagemath.org/ticket/8841





---

archive/issue_comments_081150.json:
```json
{
    "body": "Strange, I cannot confirm this. Did you apply the new spkg \"into\" a formerly unsuccessful build, or did you rebuild everything from scratch? I did the latter, i.e. taking a freshly unzipped source distribution Sage-4.4.1.rc0, replacing pari-2.3.5.spkg with pari-2.3.5.p0.spkg, and then typing\"make\". It's still building the docs at the moment, but opening a second terminal gives me on my MacIntel with OS X 10.4.11:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: 2 + 2\n4\nsage: \n```\n",
    "created_at": "2010-05-02T22:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81150",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Strange, I cannot confirm this. Did you apply the new spkg "into" a formerly unsuccessful build, or did you rebuild everything from scratch? I did the latter, i.e. taking a freshly unzipped source distribution Sage-4.4.1.rc0, replacing pari-2.3.5.spkg with pari-2.3.5.p0.spkg, and then typing"make". It's still building the docs at the moment, but opening a second terminal gives me on my MacIntel with OS X 10.4.11:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: 2 + 2
4
sage: 
```




---

archive/issue_comments_081151.json:
```json
{
    "body": "I wonder if this is now a PPC-only issue on OSX 10.4.  I will try downloading and building Sage on my PPC machine overnight tonight if no one has dealt with it by then to see what happens.",
    "created_at": "2010-05-03T14:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81151",
    "user": "https://github.com/kcrisman"
}
```

I wonder if this is now a PPC-only issue on OSX 10.4.  I will try downloading and building Sage on my PPC machine overnight tonight if no one has dealt with it by then to see what happens.



---

archive/issue_comments_081152.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-04T11:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81152",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081153.json:
```json
{
    "body": "I think this ticket is invalid - but see below.  Georg gets it working on Macintel, and I just built it on PPC G4.  Doctests are still running (and will be all day), but it's made it all the way up to \n\n```\nsage -t  \"devel/sage/sage/interfaces/ecm.py\"                \n         [56.6 s]\nsage -t  \"devel/sage/sage/interfaces/expect.py\"             \n         [54.5 s]\nsage -t  \"devel/sage/sage/interfaces/fricas.py\"             \n         [11.4 s]\nsage -t  \"devel/sage/sage/interfaces/frobby.py\"             \n         [12.6 s]\nsage -t  \"devel/sage/sage/interfaces/gap.py\"                \n```\n\nwith nary a failure, and \n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: 2+2\n4\nsage: integrate(x^3,x)\n1/4*x^4\n```\n\nI'm sure there will be a couple timeout failures with only 1.25 GHz and 1 GB of memory, but based on these results I think we're okay with fresh builds.\n| Sage Version 4.4.1, Release Date: 2010-05-02                       |\n| Type notebook() for the GUI, and license() for information.        |\nTo close this ticket, I think we need a quick update to README.txt to indicate we still support OS X 10.4 :)  I'll put \"needs review\", but no author.",
    "created_at": "2010-05-04T11:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81153",
    "user": "https://github.com/kcrisman"
}
```

I think this ticket is invalid - but see below.  Georg gets it working on Macintel, and I just built it on PPC G4.  Doctests are still running (and will be all day), but it's made it all the way up to 

```
sage -t  "devel/sage/sage/interfaces/ecm.py"                
         [56.6 s]
sage -t  "devel/sage/sage/interfaces/expect.py"             
         [54.5 s]
sage -t  "devel/sage/sage/interfaces/fricas.py"             
         [11.4 s]
sage -t  "devel/sage/sage/interfaces/frobby.py"             
         [12.6 s]
sage -t  "devel/sage/sage/interfaces/gap.py"                
```

with nary a failure, and 

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 2+2
4
sage: integrate(x^3,x)
1/4*x^4
```

I'm sure there will be a couple timeout failures with only 1.25 GHz and 1 GB of memory, but based on these results I think we're okay with fresh builds.
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
To close this ticket, I think we need a quick update to README.txt to indicate we still support OS X 10.4 :)  I'll put "needs review", but no author.



---

archive/issue_events_021575.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-09T00:48:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8841#event-21575"
}
```



---

archive/issue_events_021576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-09T00:48:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8841#event-21576"
}
```



---

archive/issue_comments_081154.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-05-09T00:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: invalid



---

archive/issue_comments_081155.json:
```json
{
    "body": "Closing this ticket as invalid. See #8935 to update README.txt to reflect support for Mac OS X 10.4.x.",
    "created_at": "2010-05-09T00:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8841#issuecomment-81155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this ticket as invalid. See #8935 to update README.txt to reflect support for Mac OS X 10.4.x.
