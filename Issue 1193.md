# Issue 1193: Can't apply patches under VMware

Issue created by migration from https://trac.sagemath.org/ticket/1193

Original creator: jvoight

Original creation time: 2007-11-17 16:37:02

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


---

Comment by mabshoff created at 2008-02-15 22:52:58

I believe this is a permission issue, so not really a bug on our end.

Cheers,

Michael


---

Comment by was created at 2008-02-16 01:04:14

The error message suggests corruption of the patch file itself.


---

Comment by jvoight created at 2008-03-12 17:01:54

Whatever was causing the problem so very long ago is no longer--I checked and can now apply patches.  JV


---

Comment by jvoight created at 2008-03-12 17:01:54

Resolution: invalid
