# Issue 705: Make vtk an easy-to-install optional sage package

archive/issues_000705.json:
```json
{
    "body": "Assignee: jkantor\n\nFrom Josh:\n\n\n```\nI have a vtk meta package in my spkgs directory.\nIt automatically attempts to detect the tcl/tk libs\nand rebuild python if the tk bindings were not compiled on linux and\nrebuilds python as a framework on OSX, it then builds VTK.\n```\n\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/\n\nIssue created by migration from https://trac.sagemath.org/ticket/705\n\n",
    "created_at": "2007-09-20T13:49:53Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "Make vtk an easy-to-install optional sage package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/705",
    "user": "https://github.com/williamstein"
}
```
Assignee: jkantor

From Josh:


```
I have a vtk meta package in my spkgs directory.
It automatically attempts to detect the tcl/tk libs
and rebuild python if the tk bindings were not compiled on linux and
rebuilds python as a framework on OSX, it then builds VTK.
```


http://sage.math.washington.edu/home/jkantor/spkgs/

Issue created by migration from https://trac.sagemath.org/ticket/705





---

archive/issue_comments_003694.json:
```json
{
    "body": "I tried your meta spkg on my laptop (Debian testing), and it failed even after I installed tcl8.4-dev and tk8.4-dev packages, with this error:\n\n```\ntest_tcl.c:2:24: error: tcl8.3/tcl.h: No such file or directory\ntest_tcl.c:3:23: error: tcl8.3/tk.h: No such file or directory\nIn file included from test_tcl.c:8:\n/usr/include/tcl8.4/tk.h:21:17: error: tcl.h: No such file or directory\n```\n\n\nAs you can see, tcl8.4/tk.h includes tcl.h without specifying a path, so it doesn't find /usr/include/tcl8.4/tcl.h.  Programs using tcl and tk need to be compiled with `-I/usr/include/tcl8.4`.",
    "created_at": "2007-10-26T04:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/705#issuecomment-3694",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I tried your meta spkg on my laptop (Debian testing), and it failed even after I installed tcl8.4-dev and tk8.4-dev packages, with this error:

```
test_tcl.c:2:24: error: tcl8.3/tcl.h: No such file or directory
test_tcl.c:3:23: error: tcl8.3/tk.h: No such file or directory
In file included from test_tcl.c:8:
/usr/include/tcl8.4/tk.h:21:17: error: tcl.h: No such file or directory
```


As you can see, tcl8.4/tk.h includes tcl.h without specifying a path, so it doesn't find /usr/include/tcl8.4/tcl.h.  Programs using tcl and tk need to be compiled with `-I/usr/include/tcl8.4`.



---

archive/issue_comments_003695.json:
```json
{
    "body": "\n```\nJosh,\n \nMichael Abshoff and I spent some time looking over the vtk packaging\nstuff you're doing.  I think you should put all the spkg's together\nin one big directory:\n \n     vtk_meta-1/\n        cmake-2.4.7.spkg\n        MayaVi-1.5.spkg\n        python-2.5.1-framework.spkg\n        PyVTK-0.4.74.spkg\n        vtk-5.0.3.p1.spkg\n \nThe version number on the directory is very important.\n \nThen put the spkg-install from your current vtk_meta in there.\nYou have to change your spkg-install slightly, so it works\nwith spkg's that are \"local\", i.e., it will be vasty simpler.\n \nThen you can just do\n \n    sage -pkg_nc vtk_meta-1    # nc for \"no compression\"\n \nto make a file vtk_meta-1.spkg that anyone can easily build\nanywhere by doing\n \n    sage -i vtk_meta-1.spkg\n \nOK?\n \nIf you don't do this, then there are a bunch of separate\noptional packages, and though you might not know this a\n*LOT* of people who install Sage immediately do \"sage -optional\"\nand proceed, in pretty much random order, to install one\noptional package after the other and play with it.  Having\na bunch that don't make sense by themselves, e.g., python-2.5.1-framework.spkg,\nin optional would reak havoc and confuse a large number of people.\n \nI'm sorry I suggested the more complicated setup that you\nactually implemented.  I hope you can see how the above suggestion\nwill be much simpler for people to use.\n \n```\n",
    "created_at": "2007-11-01T03:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/705#issuecomment-3695",
    "user": "https://github.com/williamstein"
}
```


```
Josh,
 
Michael Abshoff and I spent some time looking over the vtk packaging
stuff you're doing.  I think you should put all the spkg's together
in one big directory:
 
     vtk_meta-1/
        cmake-2.4.7.spkg
        MayaVi-1.5.spkg
        python-2.5.1-framework.spkg
        PyVTK-0.4.74.spkg
        vtk-5.0.3.p1.spkg
 
The version number on the directory is very important.
 
Then put the spkg-install from your current vtk_meta in there.
You have to change your spkg-install slightly, so it works
with spkg's that are "local", i.e., it will be vasty simpler.
 
Then you can just do
 
    sage -pkg_nc vtk_meta-1    # nc for "no compression"
 
to make a file vtk_meta-1.spkg that anyone can easily build
anywhere by doing
 
    sage -i vtk_meta-1.spkg
 
OK?
 
If you don't do this, then there are a bunch of separate
optional packages, and though you might not know this a
*LOT* of people who install Sage immediately do "sage -optional"
and proceed, in pretty much random order, to install one
optional package after the other and play with it.  Having
a bunch that don't make sense by themselves, e.g., python-2.5.1-framework.spkg,
in optional would reak havoc and confuse a large number of people.
 
I'm sorry I suggested the more complicated setup that you
actually implemented.  I hope you can see how the above suggestion
will be much simpler for people to use.
 
```




---

archive/issue_comments_003696.json:
```json
{
    "body": "UPDATE -- now it is made easier and simple, finally:\n\n\n```\nThe package vtk_meta-1.spkg in my spkg's\ndirectory should be ready now.\n\nIt requires tcl/tk dev libs to build on Linux\nas well as open gl.\n\nIt takes between 15-40+ minutes to compile\ndepending on cpu and whether or not python\nneeds to be rebuilt.\n\nNothing extra required on OSX.\nI'm curious if it works on leopard?\n\nAlso there is a pretty skeletal but functional\npatch in my spkgs, vtk_plot.hg that adds\nthree functions that allow plotting 2d surfaces and 3d isosurfaces.\n```\n",
    "created_at": "2007-11-03T14:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/705#issuecomment-3696",
    "user": "https://github.com/williamstein"
}
```

UPDATE -- now it is made easier and simple, finally:


```
The package vtk_meta-1.spkg in my spkg's
directory should be ready now.

It requires tcl/tk dev libs to build on Linux
as well as open gl.

It takes between 15-40+ minutes to compile
depending on cpu and whether or not python
needs to be rebuilt.

Nothing extra required on OSX.
I'm curious if it works on leopard?

Also there is a pretty skeletal but functional
patch in my spkgs, vtk_plot.hg that adds
three functions that allow plotting 2d surfaces and 3d isosurfaces.
```




---

archive/issue_events_000777.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-09T02:12:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/705#event-777"
}
```



---

archive/issue_comments_003697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T02:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/705#issuecomment-3697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003698.json:
```json
{
    "body": "William put this into the experimental package directory a while ago. So close this now.",
    "created_at": "2008-01-09T02:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/705#issuecomment-3698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William put this into the experimental package directory a while ago. So close this now.
