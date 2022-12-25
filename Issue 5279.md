# Issue 5279: Experimental ParaView Package

archive/issues_005279.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mkoeppe\n\nKeywords: 3D, Data Vizualization\n\nParaview is based on VTK, comes with it's own implementation of vtk.\n\n[http://www.paraview.org/Wiki/ParaView](http://www.paraview.org/Wiki/ParaView)\n\nFrom the wiki web site:\n\n```\nParaView is an open-source, multi-platform application designed to visualize\ndata sets of size varying from small to very large. The goals of\nthe ParaView project include developing an open-source, multi-platform visualization\napplication that support distributed computational models to process\nlarge data sets.\nIt has an open, flexible, and intuitive user interface.\nFurthermore, ParaView is built on an extensible architecture based on open standards.\nParaView runs on distributed and shared memory parallel as well as single processor\nsystems and has been succesfully tested on Windows, Linux, Mac OS X, IBM Blue Gene,\nCray XT3 and various Unix workstations and clusters.\nUnder the hood, ParaView uses the Visualization Toolkit as the data processing\nand rendering engine and has a user interface written using the\nQt cross-platform application framework.\n```\n\n\nDependencies:\n\nOpenGL\n\nQt4\n\nopenmpi for multi processor usage.\n\nTry it! See:\n\n[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg)\n\n[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png)\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/5279\n\n",
    "created_at": "2009-02-15T21:25:24Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Experimental ParaView Package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5279",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

CC:  @mkoeppe

Keywords: 3D, Data Vizualization

Paraview is based on VTK, comes with it's own implementation of vtk.

[http://www.paraview.org/Wiki/ParaView](http://www.paraview.org/Wiki/ParaView)

From the wiki web site:

```
ParaView is an open-source, multi-platform application designed to visualize
data sets of size varying from small to very large. The goals of
the ParaView project include developing an open-source, multi-platform visualization
application that support distributed computational models to process
large data sets.
It has an open, flexible, and intuitive user interface.
Furthermore, ParaView is built on an extensible architecture based on open standards.
ParaView runs on distributed and shared memory parallel as well as single processor
systems and has been succesfully tested on Windows, Linux, Mac OS X, IBM Blue Gene,
Cray XT3 and various Unix workstations and clusters.
Under the hood, ParaView uses the Visualization Toolkit as the data processing
and rendering engine and has a user interface written using the
Qt cross-platform application framework.
```


Dependencies:

OpenGL

Qt4

openmpi for multi processor usage.

Try it! See:

[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg)

[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png)

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/5279





---

archive/issue_comments_040437.json:
```json
{
    "body": "Im working on sage.math.\n\nI tried to install and get:\n\n```\n./spkg-install: line 19: cmake: command not found\nls: cannot access /home/wstein/build/sage-3.4/spkg/installed/cmake-2.4.8: No such file or directory\nFailed to find cmake-2.4.8  Install cmake-2.4.8 \nor install cmake-2.4 or higher\n\nreal    0m0.118s\nuser    0m0.000s\nsys     0m0.000s\n```\n\n\nSo please list cmake as a dependency.\n\nI then install cmake and...\n\n```\n-- Check if system supports 64 bit streams\n-- Check if system supports 64 bit streams - yes\n-- Cannot determine repository type. Please set UPDATE_TYPE to 'cvs' or 'svn'. CTest update will not work.\n-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a\n-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a\n-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a\n-- Plugin: Prism enabled\n-- Configuring done\nError configuring ParaView\n\nreal    0m47.134s\nuser    0m21.880s\nsys     0m12.220s\nsage: An error occurred while installing paraview-3.4.0\n```\n\n\nMaybe you could at least get this to build on sage.math?",
    "created_at": "2009-03-16T00:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40437",
    "user": "https://github.com/williamstein"
}
```

Im working on sage.math.

I tried to install and get:

```
./spkg-install: line 19: cmake: command not found
ls: cannot access /home/wstein/build/sage-3.4/spkg/installed/cmake-2.4.8: No such file or directory
Failed to find cmake-2.4.8  Install cmake-2.4.8 
or install cmake-2.4 or higher

real    0m0.118s
user    0m0.000s
sys     0m0.000s
```


So please list cmake as a dependency.

I then install cmake and...

```
-- Check if system supports 64 bit streams
-- Check if system supports 64 bit streams - yes
-- Cannot determine repository type. Please set UPDATE_TYPE to 'cvs' or 'svn'. CTest update will not work.
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Plugin: Prism enabled
-- Configuring done
Error configuring ParaView

real    0m47.134s
user    0m21.880s
sys     0m12.220s
sage: An error occurred while installing paraview-3.4.0
```


Maybe you could at least get this to build on sage.math?



---

archive/issue_comments_040438.json:
```json
{
    "body": "The discussion on google groups seems to be relevant here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/6094c90ac284edd/b8454dd45de731c4?lnk=gst&q=paraview#b8454dd45de731c4\n\nI think this package as is will not build on sage.math.\n\nA month ago I got the server version running on sage.math. So maybe we will have to make two spkgs: a desktop vesion and a server version.\n\nJaap",
    "created_at": "2009-03-16T13:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40438",
    "user": "https://github.com/jaapspies"
}
```

The discussion on google groups seems to be relevant here:

http://groups.google.com/group/sage-devel/browse_thread/thread/6094c90ac284edd/b8454dd45de731c4?lnk=gst&q=paraview#b8454dd45de731c4

I think this package as is will not build on sage.math.

A month ago I got the server version running on sage.math. So maybe we will have to make two spkgs: a desktop vesion and a server version.

Jaap



---

archive/issue_comments_040439.json:
```json
{
    "body": "maybe we can close this one after 13 years of inactivity ?",
    "created_at": "2022-04-20T19:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40439",
    "user": "https://github.com/fchapoton"
}
```

maybe we can close this one after 13 years of inactivity ?



---

archive/issue_comments_040440.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-04-20T19:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40440",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-04-21T12:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40441",
    "user": "https://github.com/dcoudert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040442.json:
```json
{
    "body": "I agree.",
    "created_at": "2022-04-21T12:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40442",
    "user": "https://github.com/dcoudert"
}
```

I agree.



---

archive/issue_comments_040443.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-04-21T15:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5279#issuecomment-40443",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_005534.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2022-04-21T15:28:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5279#event-5534"
}
```
