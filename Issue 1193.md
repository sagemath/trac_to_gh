# Issue 1193: Can't apply patches under VMware

archive/issues_001193.json:
```json
{
    "body": "Assignee: cwitty\n\nWhen I attempt to apply a patch under VMware, I get an error:\n\n\n```\n _dispatch\n    ret = _runcommand(ui, options, cmd, d)\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py\", line 401, in\n _runcommand\n    return checkargs()\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py\", line 357, in\n checkargs\n    return cmdfunc()\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py\", line 340, in\n <lambda>\n    d = lambda: func(ui, repo, *args, **cmdoptions)\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/commands.py\", line 2691, i\nn unbundle\n    modheads = repo.addchangegroup(gen, 'unbundle', 'bundle:', + fname)\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/localrepo.py\", line 1849, \nin addchangegroup\n    if cl.addgroup(chunkiter, csmap, trp, 1) is None:\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/revlog.py\", line 1201, in\naddgroup\n    ifh, dfh)\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/revlog.py\", line 1026, in\n_addrevision\n    ptext = self.revision(self.node(prev))\n  File \"/usr/local/sage/local/lib/python2.5/mercurial/revlog.py\", line 948, in r\nevision\n    text = mdiff.patches(text, bins)\nmpatch.mpatchError: invalid patch\n```\n\n\nThis occurred most recently when I applied Yi's latest DSage patch, but it occurs even when I make a patch recording a trivial modification to a file.  \n\n(Shouldn't there be a \"mercurial\" component in the drop-down below?)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1193\n\n",
    "created_at": "2007-11-17T16:37:02Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Can't apply patches under VMware",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1193",
    "user": "https://github.com/jvoight"
}
```
Assignee: cwitty

When I attempt to apply a patch under VMware, I get an error:


```
 _dispatch
    ret = _runcommand(ui, options, cmd, d)
  File "/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py", line 401, in
 _runcommand
    return checkargs()
  File "/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py", line 357, in
 checkargs
    return cmdfunc()
  File "/usr/local/sage/local/lib/python2.5/mercurial/dispatch.py", line 340, in
 <lambda>
    d = lambda: func(ui, repo, *args, **cmdoptions)
  File "/usr/local/sage/local/lib/python2.5/mercurial/commands.py", line 2691, i
n unbundle
    modheads = repo.addchangegroup(gen, 'unbundle', 'bundle:', + fname)
  File "/usr/local/sage/local/lib/python2.5/mercurial/localrepo.py", line 1849, 
in addchangegroup
    if cl.addgroup(chunkiter, csmap, trp, 1) is None:
  File "/usr/local/sage/local/lib/python2.5/mercurial/revlog.py", line 1201, in
addgroup
    ifh, dfh)
  File "/usr/local/sage/local/lib/python2.5/mercurial/revlog.py", line 1026, in
_addrevision
    ptext = self.revision(self.node(prev))
  File "/usr/local/sage/local/lib/python2.5/mercurial/revlog.py", line 948, in r
evision
    text = mdiff.patches(text, bins)
mpatch.mpatchError: invalid patch
```


This occurred most recently when I applied Yi's latest DSage patch, but it occurs even when I make a patch recording a trivial modification to a file.  

(Shouldn't there be a "mercurial" component in the drop-down below?)

Issue created by migration from https://trac.sagemath.org/ticket/1193





---

archive/issue_comments_007384.json:
```json
{
    "body": "I believe this is a permission issue, so not really a bug on our end.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1193#issuecomment-7384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I believe this is a permission issue, so not really a bug on our end.

Cheers,

Michael



---

archive/issue_comments_007385.json:
```json
{
    "body": "The error message suggests corruption of the patch file itself.",
    "created_at": "2008-02-16T01:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1193#issuecomment-7385",
    "user": "https://github.com/williamstein"
}
```

The error message suggests corruption of the patch file itself.



---

archive/issue_comments_007386.json:
```json
{
    "body": "Whatever was causing the problem so very long ago is no longer--I checked and can now apply patches.  JV",
    "created_at": "2008-03-12T17:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1193#issuecomment-7386",
    "user": "https://github.com/jvoight"
}
```

Whatever was causing the problem so very long ago is no longer--I checked and can now apply patches.  JV



---

archive/issue_comments_007387.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-12T17:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1193#issuecomment-7387",
    "user": "https://github.com/jvoight"
}
```

Resolution: invalid



---

archive/issue_events_001329.json:
```json
{
    "actor": "@jvoight",
    "created_at": "2008-03-12T17:01:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1193",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1193#event-1329"
}
```
