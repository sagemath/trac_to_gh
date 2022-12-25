# Issue 4671: [with patch; needs review] sage-3.2.1 startup time: it sucks again

archive/issues_004671.json:
```json
{
    "body": "Assignee: boothby\n\nOn OS X the Sage startup time is horrible.  Doing sage -startuptime yields:\n\n```\n## Slowest (including children)\n1.604 sage.all (None)\n0.453 sage.server.all (sage.all)\n0.449 notebook.all (sage.server.all)\n0.445 notebook_object (notebook.all)\n0.441 notebook (notebook_object)\n0.352 worksheet (notebook)\n0.345 twist (worksheet)\n0.329 sage.misc.all (sage.all)\n0.246 twisted.web2 (twist)\n0.125 sage_timeit_class (sage.misc.all)\n0.125 sage_timeit (sage_timeit_class)\n```\n\n\nI'm pretty suspicious, because the twisted stuff does *not* have to be imported at all for Sage to startup and in fact I put a lot of effort into making sure they don't (it's really annoying that they are suddenly being imported again!)\n\nThe tiny attached patch just moves a few imports and for me on OS X reduces the startup time of Sage from about 1.64 to 1.273.  It also includes a doctest that makes sure twisted will *never* get imported on startup by default.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4671\n\n",
    "created_at": "2008-12-02T05:24:14Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch; needs review] sage-3.2.1 startup time: it sucks again",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4671",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

On OS X the Sage startup time is horrible.  Doing sage -startuptime yields:

```
## Slowest (including children)
1.604 sage.all (None)
0.453 sage.server.all (sage.all)
0.449 notebook.all (sage.server.all)
0.445 notebook_object (notebook.all)
0.441 notebook (notebook_object)
0.352 worksheet (notebook)
0.345 twist (worksheet)
0.329 sage.misc.all (sage.all)
0.246 twisted.web2 (twist)
0.125 sage_timeit_class (sage.misc.all)
0.125 sage_timeit (sage_timeit_class)
```


I'm pretty suspicious, because the twisted stuff does *not* have to be imported at all for Sage to startup and in fact I put a lot of effort into making sure they don't (it's really annoying that they are suddenly being imported again!)

The tiny attached patch just moves a few imports and for me on OS X reduces the startup time of Sage from about 1.64 to 1.273.  It also includes a doctest that makes sure twisted will *never* get imported on startup by default.



Issue created by migration from https://trac.sagemath.org/ticket/4671





---

archive/issue_comments_035115.json:
```json
{
    "body": "Attachment [trac_4671.patch](tarball://root/attachments/some-uuid/ticket4671/trac_4671.patch) by @williamstein created at 2008-12-02 05:24:55",
    "created_at": "2008-12-02T05:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35115",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4671.patch](tarball://root/attachments/some-uuid/ticket4671/trac_4671.patch) by @williamstein created at 2008-12-02 05:24:55



---

archive/issue_comments_035116.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-12-02T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35116",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_035117.json:
```json
{
    "body": "Bad mhansen: This patch breaks pickling all over the combinat tree:\n\n```\n\tsage -t -long devel/sage/sage/combinat/root_system/weight_space.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_reducible.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_dual.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_E.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/type_A.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/root_space.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/root_system.py # 3 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/dynkin_diagram.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/cartan_type.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/ambient_space.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 4 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/letters.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/sloane_functions.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/weyl_group.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/combinat/root_system/weyl_characters.py # 4 doctests failed\n```\n\nProbably a trivial problem, but \"needs work\" nonetheless :p\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T08:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35117",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bad mhansen: This patch breaks pickling all over the combinat tree:

```
	sage -t -long devel/sage/sage/combinat/root_system/weight_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_reducible.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_dual.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_E.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_A.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/root_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/root_system.py # 3 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/dynkin_diagram.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/cartan_type.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/ambient_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 4 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/letters.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/sloane_functions.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/weyl_group.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/weyl_characters.py # 4 doctests failed
```

Probably a trivial problem, but "needs work" nonetheless :p

Cheers,

Michael



---

archive/issue_comments_035118.json:
```json
{
    "body": "This is really really weird.  The *only* thing I change is to remove two instances of \"import twist\" in the notebook code.  The *only* doctests in the whole Sage tree that break are those combinat pickles.  Absolutely nothing else breaks (I just tested this).  If one tries them by hand on the command line they break, but if one does\n\n```\n  sage: import sage.server.notebook.twist\n```\n\nthen they suddenly work. \n\nAnd those tests are not just pickle tests that fail.\n\nMike -- can you think of anything that combinat code uses that might somehow have something to do with twisted or twist.py being imported?",
    "created_at": "2008-12-04T21:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35118",
    "user": "https://github.com/williamstein"
}
```

This is really really weird.  The *only* thing I change is to remove two instances of "import twist" in the notebook code.  The *only* doctests in the whole Sage tree that break are those combinat pickles.  Absolutely nothing else breaks (I just tested this).  If one tries them by hand on the command line they break, but if one does

```
  sage: import sage.server.notebook.twist
```

then they suddenly work. 

And those tests are not just pickle tests that fail.

Mike -- can you think of anything that combinat code uses that might somehow have something to do with twisted or twist.py being imported?



---

archive/issue_comments_035119.json:
```json
{
    "body": "Attachment [trac_4671-2.patch](tarball://root/attachments/some-uuid/ticket4671/trac_4671-2.patch) by @mwhansen created at 2008-12-16 17:15:57",
    "created_at": "2008-12-16T17:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35119",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4671-2.patch](tarball://root/attachments/some-uuid/ticket4671/trac_4671-2.patch) by @mwhansen created at 2008-12-16 17:15:57



---

archive/issue_comments_035120.json:
```json
{
    "body": "I've put up a new patch which imports twisted.persisted.styles, but still make startup time way faster.\n\n\n```\n<mhansen> No\n<mhansen> I still have no idea why it's happening.\n<mhansen> And I found it.  [08:40]\n<mhansen> Twisted has some code in twisted.persistant.styles that allows you\n          to pickle things that aren't picklable normally.  [08:42]\n<mhansen> Importing just that takes .110s on my machine while doing import\n          twist takes 0.675s.  [08:48]\n<mhansen> Doing so causes wstein|afk's doctest to fail.  [08:49]\n<wstein|afk> mhansen -- importing twisted.persistant.styles and changing my\n             doctest is a good solution.  [09:02]\n```\n",
    "created_at": "2008-12-16T17:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35120",
    "user": "https://github.com/mwhansen"
}
```

I've put up a new patch which imports twisted.persisted.styles, but still make startup time way faster.


```
<mhansen> No
<mhansen> I still have no idea why it's happening.
<mhansen> And I found it.  [08:40]
<mhansen> Twisted has some code in twisted.persistant.styles that allows you
          to pickle things that aren't picklable normally.  [08:42]
<mhansen> Importing just that takes .110s on my machine while doing import
          twist takes 0.675s.  [08:48]
<mhansen> Doing so causes wstein|afk's doctest to fail.  [08:49]
<wstein|afk> mhansen -- importing twisted.persistant.styles and changing my
             doctest is a good solution.  [09:02]
```




---

archive/issue_comments_035121.json:
```json
{
    "body": "We should attempt to get this into 3.2.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T11:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We should attempt to get this into 3.2.3.

Cheers,

Michael



---

archive/issue_comments_035122.json:
```json
{
    "body": "The patch trac_4671-2.patch fixes the picklig issue and reduces the startup time significantly. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T21:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch trac_4671-2.patch fixes the picklig issue and reduces the startup time significantly. Positive review.

Cheers,

Michael



---

archive/issue_comments_035123.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004919.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T21:30:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4671#event-4919"
}
```



---

archive/issue_comments_035124.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4671#issuecomment-35124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
