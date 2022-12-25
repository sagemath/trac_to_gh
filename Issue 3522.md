# Issue 3522: [with spkgs, needs review] New experimental mayavi2 spkg based on vtk_5.2 for linux

archive/issues_003522.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nThere were problems building mayavi2 experimental spkg on Fedora 9 and other\nnew Linuxes:\n1) vtk-5.0.4 does not build with tcl/tk-8.5.1\n2) vtk-5.0.4 will not build with gcc-4.3\n\nBoth problems are solved with vtk-5.2 from svn.\n\nI checked out mayavi_2.2.0 and it worked for me on Fedora 8 and Fedora 9:\n```\n\nhttp://sage.math.washington.edu/home/jsp/mayavi_2.2.0.spkg\n\n```\nDepends on:\n```\nhttp://sage.math.washington.edu/home/jsp/vtk-5.2.spkg\n\n```\n(and experimental spkgs cmake-2.4.8 and wxPython-2.8.7.1)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3522\n\n",
    "created_at": "2008-06-27T14:26:11Z",
    "labels": [
        "component: packages: experimental",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with spkgs, needs review] New experimental mayavi2 spkg based on vtk_5.2 for linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3522",
    "user": "https://github.com/jaapspies"
}
```
Assignee: mabshoff


```
There were problems building mayavi2 experimental spkg on Fedora 9 and other
new Linuxes:
1) vtk-5.0.4 does not build with tcl/tk-8.5.1
2) vtk-5.0.4 will not build with gcc-4.3

Both problems are solved with vtk-5.2 from svn.

I checked out mayavi_2.2.0 and it worked for me on Fedora 8 and Fedora 9:
```

http://sage.math.washington.edu/home/jsp/mayavi_2.2.0.spkg

```
Depends on:
```
http://sage.math.washington.edu/home/jsp/vtk-5.2.spkg

```
(and experimental spkgs cmake-2.4.8 and wxPython-2.8.7.1)
```


Issue created by migration from https://trac.sagemath.org/ticket/3522





---

archive/issue_comments_024772.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-02T20:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3522#issuecomment-24772",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024773.json:
```json
{
    "body": "Jaap,\n\nboth spkgs looks good to me. I checked in the relevant files into the repos. One thing I noticed was that both archives contain the full svn history, but after the disaster last time around I left them there. Sorry that it took so long.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T06:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3522#issuecomment-24773",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jaap,

both spkgs looks good to me. I checked in the relevant files into the repos. One thing I noticed was that both archives contain the full svn history, but after the disaster last time around I left them there. Sorry that it took so long.

Cheers,

Michael



---

archive/issue_events_008037.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T06:57:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3522#event-8037"
}
```



---

archive/issue_events_008038.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T06:58:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3522#event-8038"
}
```



---

archive/issue_comments_024774.json:
```json
{
    "body": "Merged into the experimental package repo in Sage 3.1.alpha1",
    "created_at": "2008-08-11T06:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3522#issuecomment-24774",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged into the experimental package repo in Sage 3.1.alpha1



---

archive/issue_comments_024775.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T06:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3522#issuecomment-24775",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
