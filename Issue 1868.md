# Issue 1868: New mayavi2 package

archive/issues_001868.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis spkg needs cmake-2.4.7.spkg (already in experimental), vtk-5.0.3.spkg, setuptools-0.6.spkg\nand wxPython-2.8.7.1 (already in experimental as wxPython-linux-2.8.7.1.spk).\n\n```\nThe following is working on Fedora 7/8 (and Ubuntu?):\n\n > Dependencies for Sage:\n >\n\n >   - http://www.wxpython.org wxPython-2.6.x or higher for the UI\n >   - vtk-5.0.3\n >   - setuptools-0.6b\n\n1) Install wxPython-2.8.7.1:\n    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/wxPython-2.8.7.1.spkg\n\n2) Install vtk-5.0.3:\n\n    install cmake (also an experimental spkg):\n    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/cmake-2.4.7.spkg\n    and\n    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/vtk-5.0.3.spkg\n\n3) Install setuptools:\n    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/setuptools-0.6.spkg\n\n4) Install mayavi_2.0.20080117.spkg\n    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/mayavi_2.0.20080117.spkg\n\n```\n\n\nThis new spkg will install its dependencies automagically.\n\nEventually\n\n\n```\n./sage -i mayavi_2.0.20080117\n```\n\n\nwill do the trick.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1868\n\n",
    "created_at": "2008-01-20T17:57:55Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "New mayavi2 package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1868",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

This spkg needs cmake-2.4.7.spkg (already in experimental), vtk-5.0.3.spkg, setuptools-0.6.spkg
and wxPython-2.8.7.1 (already in experimental as wxPython-linux-2.8.7.1.spk).

```
The following is working on Fedora 7/8 (and Ubuntu?):

 > Dependencies for Sage:
 >

 >   - http://www.wxpython.org wxPython-2.6.x or higher for the UI
 >   - vtk-5.0.3
 >   - setuptools-0.6b

1) Install wxPython-2.8.7.1:
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/wxPython-2.8.7.1.spkg

2) Install vtk-5.0.3:

    install cmake (also an experimental spkg):
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/cmake-2.4.7.spkg
    and
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/vtk-5.0.3.spkg

3) Install setuptools:
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/setuptools-0.6.spkg

4) Install mayavi_2.0.20080117.spkg
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/mayavi_2.0.20080117.spkg

```


This new spkg will install its dependencies automagically.

Eventually


```
./sage -i mayavi_2.0.20080117
```


will do the trick.

Issue created by migration from https://trac.sagemath.org/ticket/1868





---

archive/issue_comments_011800.json:
```json
{
    "body": "This experimental package could easily be included, I think.\n\nJaap",
    "created_at": "2008-01-29T20:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11800",
    "user": "https://github.com/jaapspies"
}
```

This experimental package could easily be included, I think.

Jaap



---

archive/issue_comments_011801.json:
```json
{
    "body": "Once this gets a positive review from some people trying it out, it will be posted to the sage official spkg webpage.",
    "created_at": "2008-02-28T20:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11801",
    "user": "https://github.com/williamstein"
}
```

Once this gets a positive review from some people trying it out, it will be posted to the sage official spkg webpage.



---

archive/issue_comments_011802.json:
```json
{
    "body": "This package seems to work for me.",
    "created_at": "2008-02-29T23:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11802",
    "user": "https://github.com/jasongrout"
}
```

This package seems to work for me.



---

archive/issue_comments_011803.json:
```json
{
    "body": "These packages work for me (and have for weeks; I'm sorry, I should have reviewed this ticket a long time ago.)  32-bit x86 debian testing, using the non-free nvidia graphics drivers.",
    "created_at": "2008-03-01T01:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11803",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

These packages work for me (and have for weeks; I'm sorry, I should have reviewed this ticket a long time ago.)  32-bit x86 debian testing, using the non-free nvidia graphics drivers.



---

archive/issue_comments_011804.json:
```json
{
    "body": "Merged in the experimental package repo",
    "created_at": "2008-03-01T21:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in the experimental package repo



---

archive/issue_comments_011805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-01T21:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1868#issuecomment-11805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
