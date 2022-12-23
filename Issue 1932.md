# Issue 1932: weird hg bug?

Issue created by migration from https://trac.sagemath.org/ticket/1932

Original creator: craigcitro

Original creation time: 2008-01-26 09:02:18

Assignee: mabshoff

CC:  alexghitza

I ran into a very strange bug using hg tonight, which seems to only occur on Macs. If you go into the directory sage/schemes/elliptic_curves/ on your favorite sage branch, and do any sort of complicated hg command -- for example, 'hg diff sha.py' or 'hg log -l 3' -- it fails, and you get the following traceback:


```
Traceback (most recent call last):
  File "/sage/local/bin/hg", line 14, in <module>
    mercurial.dispatch.run()
  File "/sage/local/lib/python/mercurial/dispatch.py", line 20, in run
    sys.exit(dispatch(sys.argv[1:]))
  File "/sage/local/lib/python/mercurial/dispatch.py", line 29, in dispatch
    return _runcatch(u, args)
  File "/sage/local/lib/python/mercurial/dispatch.py", line 79, in _runcatch
    except revlog.RevlogError, inst:
  File "/sage/local/lib/python/mercurial/demandimport.py", line 74, in __getattribute__
    self._load()
  File "/sage/local/lib/python/mercurial/demandimport.py", line 46, in _load
    mod = _origimport(head, globals, locals)
  File "/sage/local/lib/python/mercurial/revlog.py", line 22, in <module>
    _sha = sha.new
  File "/sage/local/lib/python/mercurial/demandimport.py", line 74, in __getattribute__
    self._load()
  File "/sage/local/lib/python/mercurial/demandimport.py", line 46, in _load
    mod = _origimport(head, globals, locals)
  File "/sage/devel/sage-main/sage/schemes/elliptic_curves/sha.py", line 2, in <module>
    from sage.rings.all import (
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/rings/all.py", line 45, in <module>
    from quotient_ring import QuotientRing
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 34, in <module>
    from sage.interfaces.all import singular as singular_default, is_SingularElement
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/interfaces/all.py", line 24, in <module>
    from qsieve import qsieve
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/interfaces/qsieve.py", line 11, in <module>
    from sage.misc.all import tmp_dir
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/misc/all.py", line 70, in <module>
    from functional import (additive_order,
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "/sage/local/lib/python2.5/site-packages/sage/misc/functional.py", line 34, in <module>
    from sage.rings.complex_double import CDF
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "integer.pxd", line 9, in sage.rings.complex_double
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "integer.pyx", line 158, in sage.rings.integer
  File "/sage/local/lib/python/mercurial/demandimport.py", line 83, in _demandimport
    return _origimport(name, globals, locals, fromlist)
  File "rational.pxd", line 7, in sage.rings.integer_ring
  File "/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
  File "rational.pyx", line 48, in sage.rings.rational
AttributeError: 'module' object has no attribute 'ZZ'
```


I've checked this on a 10.5 PPC, 10.5 Intel, and a 10.4 Intel. David Roe tried it on a 10.4 Intel and got this slightly different traceback:


```
Traceback (most recent call last):
  File "/Users/roed/Math/sage/local/bin/hg", line 14, in <module>
    mercurial.dispatch.run()
  File "/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py", line 20, in run
    sys.exit(dispatch(sys.argv[1:]))
  File "/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py", line 29, in dispatch
    return _runcatch(u, args)
  File "/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py", line 79, in _runcatch
    except revlog.RevlogError, inst:
  File "/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py", line 74, in __getattribute__
    self._load()
  File "/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py", line 46, in _load
    mod = _origimport(head, globals, locals)
  File "/Users/roed/Math/sage/local/lib/python/mercurial/revlog.py", line 22, in <module>
    _sha = sha.new
  File "/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py", line 74, in __getattribute__
    self._load()
  File "/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py", line 46, in _load
    mod = _origimport(head, globals, locals)
  File "/Users/roed/Math/sage-2.10/devel/sage-main/sage/schemes/elliptic_curves/sha.py", line 1, in <module>
    from sage.structure.sage_object import SageObject
  File "/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py", line 99, in _demandimport
    mod = _origimport(name, globals, locals)
ImportError: No module named sage.structure.sage_object
```


The error disappears if you try it in any other directory (or, at least, any I've found!). Any ideas?




---

Comment by AlexGhitza created at 2008-01-26 09:10:54

No idea, but I'm getting the same error as in your first example (i.e. the one ending with "AttributeError: 'module' object has no attribute 'ZZ'") on my Intel laptop running Gentoo.


---

Comment by jason created at 2008-01-27 02:35:58

It works with hg 0.9.4, but not with 0.9.5 on Ubuntu 7.10 on an AMD processor.

The 0.9.4 distributed with Ubuntu works fine.  The sage -hg version blows up like you have in the ticket.


---

Comment by was created at 2008-01-27 02:39:13

I think it has to do with Python (hg is a python program) picking up
something in the local path.  A workaround is to change to another directory one
up and run the same command, e.g, 

```
   cd ..
   hg diff elliptic_curves/sha.py
```

works.

I'm not saying this isn't a bug though!


---

Comment by craigcitro created at 2008-05-21 07:38:37

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-05-21 07:38:37

Changing assignee from mabshoff to craigcitro.


---

Comment by craigcitro created at 2008-05-21 07:38:37

So I know what's going on now, but I'm not sure what the right thing to do to fix this is. Here's what's happening: there's a python module called `sha`, and mercurial tries to load that when it runs. Sadly, though, `.` is earlier in the search path than the python system libraries, so it loads our sha.py first. I can think of several fixes:

 1. Rename `sha.py` to something else.
 1. Force mercurial to not have `.` in the path with higher precedence than the python libraries. 
 1. Force mercurial to always run from the root directory of the branch.

I'm not sure that I really like any of these options, but that's all I can think of offhand. If someone has a convincing opinion, I'm happy to implement it.


---

Comment by jason created at 2008-09-10 02:36:53

I was told by wstein that sage is *not* to have any modules named the same as python modules.  Bad things happen (I believe there is a note to this effect in the python docs too).  So I vote for renaming our sha.py.


---

Comment by AlexGhitza created at 2008-09-10 02:44:21

Yes, how about ell_sha.py ?


---

Comment by craigcitro created at 2008-09-10 03:14:26

That could work -- although there are already a lot of `ell_` files in that directory already, which slows down tab completion. :) How about `tate_sha.py`?

I'll make the patch as soon as we have a new name.


---

Comment by AlexGhitza created at 2008-09-16 13:59:27

tate_sha.py sounds good to me.


---

Comment by craigcitro created at 2008-09-23 06:03:04

Okay, I'm attaching two patches that fix this issue. The first moves `sha.py` to `sha_tate.py` (because that still tab-completes the same). It creates a new `sha.py` which simply raises a `DeprecationWarning` with a reference to the new module, and this trac ticket. This should be applied now. Of course, since there is still a `sha.py` in the hg repository, it doesn't actually fix this bug. The second patch simply removes `sha.py` -- this should be applied one or two versions down the road (I don't know what our deprecation policy is), and *actually* fixes the problem.


---

Comment by craigcitro created at 2008-09-23 06:03:42

apply later


---

Attachment

apply now (ignore the other patch with same name)


---

Attachment

positive review.  i had to tweak craig's first patch a bit (after checking with him) and i tried to just replace it but trac didn't like that.

i checked both the deprecation warning with the first patch, and the fact that the issue is completely resolved with the second patch (yay i can use hg in schemes/elliptic_curves/ again!)

so: apply trac-1932-pt1.2.patch now, and apply trac-1932-pt2.patch when the deprecation period is over.


---

Comment by mabshoff created at 2008-09-23 09:05:02

Craig,

please open another ticket for trac-1932-pt2.patch since once I merge trac-1932-pt1.2.patch I will close this ticket. Add something like "merge by August 2009" to the subject so that we will merge this once we have waited six months (or whatever timeframe we come up with). Once that ticket is open it would be nice if you mentioned it here so that one can easily follow up. We might even want to add a deprecation milestone in trac for those tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 10:24:10

Merged trac-1932-pt1.2.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 10:24:10

Resolution: fixed
