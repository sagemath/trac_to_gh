# Issue 1932: weird hg bug?

archive/issues_001932.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  alexghitza\n\nI ran into a very strange bug using hg tonight, which seems to only occur on Macs. If you go into the directory sage/schemes/elliptic_curves/ on your favorite sage branch, and do any sort of complicated hg command -- for example, 'hg diff sha.py' or 'hg log -l 3' -- it fails, and you get the following traceback:\n\n\n```\nTraceback (most recent call last):\n  File \"/sage/local/bin/hg\", line 14, in <module>\n    mercurial.dispatch.run()\n  File \"/sage/local/lib/python/mercurial/dispatch.py\", line 20, in run\n    sys.exit(dispatch(sys.argv[1:]))\n  File \"/sage/local/lib/python/mercurial/dispatch.py\", line 29, in dispatch\n    return _runcatch(u, args)\n  File \"/sage/local/lib/python/mercurial/dispatch.py\", line 79, in _runcatch\n    except revlog.RevlogError, inst:\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 74, in __getattribute__\n    self._load()\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 46, in _load\n    mod = _origimport(head, globals, locals)\n  File \"/sage/local/lib/python/mercurial/revlog.py\", line 22, in <module>\n    _sha = sha.new\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 74, in __getattribute__\n    self._load()\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 46, in _load\n    mod = _origimport(head, globals, locals)\n  File \"/sage/devel/sage-main/sage/schemes/elliptic_curves/sha.py\", line 2, in <module>\n    from sage.rings.all import (\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/rings/all.py\", line 45, in <module>\n    from quotient_ring import QuotientRing\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py\", line 34, in <module>\n    from sage.interfaces.all import singular as singular_default, is_SingularElement\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/interfaces/all.py\", line 24, in <module>\n    from qsieve import qsieve\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/interfaces/qsieve.py\", line 11, in <module>\n    from sage.misc.all import tmp_dir\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/misc/all.py\", line 70, in <module>\n    from functional import (additive_order,\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"/sage/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 34, in <module>\n    from sage.rings.complex_double import CDF\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"integer.pxd\", line 9, in sage.rings.complex_double\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"integer.pyx\", line 158, in sage.rings.integer\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 83, in _demandimport\n    return _origimport(name, globals, locals, fromlist)\n  File \"rational.pxd\", line 7, in sage.rings.integer_ring\n  File \"/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\n  File \"rational.pyx\", line 48, in sage.rings.rational\nAttributeError: 'module' object has no attribute 'ZZ'\n```\n\n\nI've checked this on a 10.5 PPC, 10.5 Intel, and a 10.4 Intel. David Roe tried it on a 10.4 Intel and got this slightly different traceback:\n\n\n```\nTraceback (most recent call last):\n  File \"/Users/roed/Math/sage/local/bin/hg\", line 14, in <module>\n    mercurial.dispatch.run()\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py\", line 20, in run\n    sys.exit(dispatch(sys.argv[1:]))\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py\", line 29, in dispatch\n    return _runcatch(u, args)\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/dispatch.py\", line 79, in _runcatch\n    except revlog.RevlogError, inst:\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py\", line 74, in __getattribute__\n    self._load()\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py\", line 46, in _load\n    mod = _origimport(head, globals, locals)\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/revlog.py\", line 22, in <module>\n    _sha = sha.new\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py\", line 74, in __getattribute__\n    self._load()\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py\", line 46, in _load\n    mod = _origimport(head, globals, locals)\n  File \"/Users/roed/Math/sage-2.10/devel/sage-main/sage/schemes/elliptic_curves/sha.py\", line 1, in <module>\n    from sage.structure.sage_object import SageObject\n  File \"/Users/roed/Math/sage/local/lib/python/mercurial/demandimport.py\", line 99, in _demandimport\n    mod = _origimport(name, globals, locals)\nImportError: No module named sage.structure.sage_object\n```\n\n\nThe error disappears if you try it in any other directory (or, at least, any I've found!). Any ideas?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1932\n\n",
    "created_at": "2008-01-26T09:02:18Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "weird hg bug?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1932",
    "user": "craigcitro"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/1932





---

archive/issue_comments_012254.json:
```json
{
    "body": "No idea, but I'm getting the same error as in your first example (i.e. the one ending with \"AttributeError: 'module' object has no attribute 'ZZ'\") on my Intel laptop running Gentoo.",
    "created_at": "2008-01-26T09:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12254",
    "user": "AlexGhitza"
}
```

No idea, but I'm getting the same error as in your first example (i.e. the one ending with "AttributeError: 'module' object has no attribute 'ZZ'") on my Intel laptop running Gentoo.



---

archive/issue_comments_012255.json:
```json
{
    "body": "It works with hg 0.9.4, but not with 0.9.5 on Ubuntu 7.10 on an AMD processor.\n\nThe 0.9.4 distributed with Ubuntu works fine.  The sage -hg version blows up like you have in the ticket.",
    "created_at": "2008-01-27T02:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12255",
    "user": "jason"
}
```

It works with hg 0.9.4, but not with 0.9.5 on Ubuntu 7.10 on an AMD processor.

The 0.9.4 distributed with Ubuntu works fine.  The sage -hg version blows up like you have in the ticket.



---

archive/issue_comments_012256.json:
```json
{
    "body": "I think it has to do with Python (hg is a python program) picking up\nsomething in the local path.  A workaround is to change to another directory one\nup and run the same command, e.g, \n\n```\n   cd ..\n   hg diff elliptic_curves/sha.py\n```\n\nworks.\n\nI'm not saying this isn't a bug though!",
    "created_at": "2008-01-27T02:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12256",
    "user": "was"
}
```

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

archive/issue_comments_012257.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-21T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12257",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012258.json:
```json
{
    "body": "Changing assignee from mabshoff to craigcitro.",
    "created_at": "2008-05-21T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12258",
    "user": "craigcitro"
}
```

Changing assignee from mabshoff to craigcitro.



---

archive/issue_comments_012259.json:
```json
{
    "body": "So I know what's going on now, but I'm not sure what the right thing to do to fix this is. Here's what's happening: there's a python module called `sha`, and mercurial tries to load that when it runs. Sadly, though, `.` is earlier in the search path than the python system libraries, so it loads our sha.py first. I can think of several fixes:\n\n1. Rename `sha.py` to something else.\n2. Force mercurial to not have `.` in the path with higher precedence than the python libraries. \n3. Force mercurial to always run from the root directory of the branch.\n\nI'm not sure that I really like any of these options, but that's all I can think of offhand. If someone has a convincing opinion, I'm happy to implement it.",
    "created_at": "2008-05-21T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12259",
    "user": "craigcitro"
}
```

So I know what's going on now, but I'm not sure what the right thing to do to fix this is. Here's what's happening: there's a python module called `sha`, and mercurial tries to load that when it runs. Sadly, though, `.` is earlier in the search path than the python system libraries, so it loads our sha.py first. I can think of several fixes:

1. Rename `sha.py` to something else.
2. Force mercurial to not have `.` in the path with higher precedence than the python libraries. 
3. Force mercurial to always run from the root directory of the branch.

I'm not sure that I really like any of these options, but that's all I can think of offhand. If someone has a convincing opinion, I'm happy to implement it.



---

archive/issue_comments_012260.json:
```json
{
    "body": "I was told by wstein that sage is *not* to have any modules named the same as python modules.  Bad things happen (I believe there is a note to this effect in the python docs too).  So I vote for renaming our sha.py.",
    "created_at": "2008-09-10T02:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12260",
    "user": "jason"
}
```

I was told by wstein that sage is *not* to have any modules named the same as python modules.  Bad things happen (I believe there is a note to this effect in the python docs too).  So I vote for renaming our sha.py.



---

archive/issue_comments_012261.json:
```json
{
    "body": "Yes, how about ell_sha.py ?",
    "created_at": "2008-09-10T02:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12261",
    "user": "AlexGhitza"
}
```

Yes, how about ell_sha.py ?



---

archive/issue_comments_012262.json:
```json
{
    "body": "That could work -- although there are already a lot of `ell_` files in that directory already, which slows down tab completion. :) How about `tate_sha.py`?\n\nI'll make the patch as soon as we have a new name.",
    "created_at": "2008-09-10T03:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12262",
    "user": "craigcitro"
}
```

That could work -- although there are already a lot of `ell_` files in that directory already, which slows down tab completion. :) How about `tate_sha.py`?

I'll make the patch as soon as we have a new name.



---

archive/issue_comments_012263.json:
```json
{
    "body": "tate_sha.py sounds good to me.",
    "created_at": "2008-09-16T13:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12263",
    "user": "AlexGhitza"
}
```

tate_sha.py sounds good to me.



---

archive/issue_comments_012264.json:
```json
{
    "body": "Okay, I'm attaching two patches that fix this issue. The first moves `sha.py` to `sha_tate.py` (because that still tab-completes the same). It creates a new `sha.py` which simply raises a `DeprecationWarning` with a reference to the new module, and this trac ticket. This should be applied now. Of course, since there is still a `sha.py` in the hg repository, it doesn't actually fix this bug. The second patch simply removes `sha.py` -- this should be applied one or two versions down the road (I don't know what our deprecation policy is), and **actually** fixes the problem.",
    "created_at": "2008-09-23T06:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12264",
    "user": "craigcitro"
}
```

Okay, I'm attaching two patches that fix this issue. The first moves `sha.py` to `sha_tate.py` (because that still tab-completes the same). It creates a new `sha.py` which simply raises a `DeprecationWarning` with a reference to the new module, and this trac ticket. This should be applied now. Of course, since there is still a `sha.py` in the hg repository, it doesn't actually fix this bug. The second patch simply removes `sha.py` -- this should be applied one or two versions down the road (I don't know what our deprecation policy is), and **actually** fixes the problem.



---

archive/issue_comments_012265.json:
```json
{
    "body": "apply later",
    "created_at": "2008-09-23T06:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12265",
    "user": "craigcitro"
}
```

apply later



---

archive/issue_comments_012266.json:
```json
{
    "body": "Attachment [trac-1932-pt2.patch](tarball://root/attachments/some-uuid/ticket1932/trac-1932-pt2.patch) by AlexGhitza created at 2008-09-23 06:34:05\n\napply now (ignore the other patch with same name)",
    "created_at": "2008-09-23T06:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12266",
    "user": "AlexGhitza"
}
```

Attachment [trac-1932-pt2.patch](tarball://root/attachments/some-uuid/ticket1932/trac-1932-pt2.patch) by AlexGhitza created at 2008-09-23 06:34:05

apply now (ignore the other patch with same name)



---

archive/issue_comments_012267.json:
```json
{
    "body": "Attachment [trac-1932-pt1.2.patch](tarball://root/attachments/some-uuid/ticket1932/trac-1932-pt1.2.patch) by AlexGhitza created at 2008-09-23 06:39:57\n\npositive review.  i had to tweak craig's first patch a bit (after checking with him) and i tried to just replace it but trac didn't like that.\n\ni checked both the deprecation warning with the first patch, and the fact that the issue is completely resolved with the second patch (yay i can use hg in schemes/elliptic_curves/ again!)\n\nso: apply trac-1932-pt1.2.patch now, and apply trac-1932-pt2.patch when the deprecation period is over.",
    "created_at": "2008-09-23T06:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12267",
    "user": "AlexGhitza"
}
```

Attachment [trac-1932-pt1.2.patch](tarball://root/attachments/some-uuid/ticket1932/trac-1932-pt1.2.patch) by AlexGhitza created at 2008-09-23 06:39:57

positive review.  i had to tweak craig's first patch a bit (after checking with him) and i tried to just replace it but trac didn't like that.

i checked both the deprecation warning with the first patch, and the fact that the issue is completely resolved with the second patch (yay i can use hg in schemes/elliptic_curves/ again!)

so: apply trac-1932-pt1.2.patch now, and apply trac-1932-pt2.patch when the deprecation period is over.



---

archive/issue_comments_012268.json:
```json
{
    "body": "Craig,\n\nplease open another ticket for trac-1932-pt2.patch since once I merge trac-1932-pt1.2.patch I will close this ticket. Add something like \"merge by August 2009\" to the subject so that we will merge this once we have waited six months (or whatever timeframe we come up with). Once that ticket is open it would be nice if you mentioned it here so that one can easily follow up. We might even want to add a deprecation milestone in trac for those tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T09:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12268",
    "user": "mabshoff"
}
```

Craig,

please open another ticket for trac-1932-pt2.patch since once I merge trac-1932-pt1.2.patch I will close this ticket. Add something like "merge by August 2009" to the subject so that we will merge this once we have waited six months (or whatever timeframe we come up with). Once that ticket is open it would be nice if you mentioned it here so that one can easily follow up. We might even want to add a deprecation milestone in trac for those tickets.

Cheers,

Michael



---

archive/issue_comments_012269.json:
```json
{
    "body": "Merged trac-1932-pt1.2.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T10:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12269",
    "user": "mabshoff"
}
```

Merged trac-1932-pt1.2.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_012270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T10:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1932#issuecomment-12270",
    "user": "mabshoff"
}
```

Resolution: fixed
