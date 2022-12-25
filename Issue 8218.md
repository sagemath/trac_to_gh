# Issue 8218: Finite Field move

archive/issues_008218.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb\n\nKeywords: finite fields\n\nMoves all of the finite field files, the integer_mod files and the base classes from sage.rings.ring and sage.structure.element into their own folder in sage.rings.  In preparation for more work on finite fields.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8218\n\n",
    "created_at": "2010-02-09T03:39:15Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Finite Field move",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8218",
    "user": "https://github.com/roed314"
}
```
Assignee: @aghitza

CC:  @robertwb

Keywords: finite fields

Moves all of the finite field files, the integer_mod files and the base classes from sage.rings.ring and sage.structure.element into their own folder in sage.rings.  In preparation for more work on finite fields.

Issue created by migration from https://trac.sagemath.org/ticket/8218





---

archive/issue_comments_072360.json:
```json
{
    "body": "Attachment [trac_8218_move.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move.patch) by @roed314 created at 2010-02-09 04:06:39\n\nJust moves the files",
    "created_at": "2010-02-09T04:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72360",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8218_move.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move.patch) by @roed314 created at 2010-02-09 04:06:39

Just moves the files



---

archive/issue_comments_072361.json:
```json
{
    "body": "Changing assignee from @aghitza to @roed314.",
    "created_at": "2010-02-09T04:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72361",
    "user": "https://github.com/roed314"
}
```

Changing assignee from @aghitza to @roed314.



---

archive/issue_comments_072362.json:
```json
{
    "body": "The files that are moved into sage.rings.finite_rings are:\n\n```\ninteger_mod.pyx -> finite_rings/integer_mod.pyx\ninteger_mod.pxd -> finite_rings/integer_mod.pxd\ninteger_mod_ring.py -> finite_rings/integer_mod_ring.py\nfinite_field.py -> finite_rings/constructor.py\nfinite_field_prime_modn.py -> finite_rings/finite_field_prime_modn.py\nfinite_field_element.py -> finite_rings/element_ext_pari.py\nfinite_field_ext_pari.py -> finite_rings/finite_field_ext_pari.py\nfinite_field_givaro.pyx -> finite_rings/element_givaro.pyx\nfinite_field_givaro.pxd -> finite_rings/element_givaro.pxd\nfinite_field_ntl_gf2e.pyx -> finite_rings/finite_field_ntl_gf2e.pyx\nfinite_field_ntl_gf2e.pxd -> finite_rings/finite_field_ntl_gf2e.pxd\nfinite_field_morphism.py -> finite_rings/homset.py\npart of ring.pyx -> finite_rings/finite_field_base.pyx\npart of ring.pxd -> finite_rings/finite_field_base.pxd\npart of sage/structure/element.pyx -> sage/rings/finite_rings/element_base.pyx\npart of sage/structure/element.pxd -> sage/rings/finite_rings/element_base.pxd\n```",
    "created_at": "2010-02-09T04:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72362",
    "user": "https://github.com/roed314"
}
```

The files that are moved into sage.rings.finite_rings are:

```
integer_mod.pyx -> finite_rings/integer_mod.pyx
integer_mod.pxd -> finite_rings/integer_mod.pxd
integer_mod_ring.py -> finite_rings/integer_mod_ring.py
finite_field.py -> finite_rings/constructor.py
finite_field_prime_modn.py -> finite_rings/finite_field_prime_modn.py
finite_field_element.py -> finite_rings/element_ext_pari.py
finite_field_ext_pari.py -> finite_rings/finite_field_ext_pari.py
finite_field_givaro.pyx -> finite_rings/element_givaro.pyx
finite_field_givaro.pxd -> finite_rings/element_givaro.pxd
finite_field_ntl_gf2e.pyx -> finite_rings/finite_field_ntl_gf2e.pyx
finite_field_ntl_gf2e.pxd -> finite_rings/finite_field_ntl_gf2e.pxd
finite_field_morphism.py -> finite_rings/homset.py
part of ring.pyx -> finite_rings/finite_field_base.pyx
part of ring.pxd -> finite_rings/finite_field_base.pxd
part of sage/structure/element.pyx -> sage/rings/finite_rings/element_base.pyx
part of sage/structure/element.pxd -> sage/rings/finite_rings/element_base.pxd
```



---

archive/issue_comments_072363.json:
```json
{
    "body": "It would be good to do this as a mercurial bundle, so that the history and other merges will follow correctly.",
    "created_at": "2010-02-09T18:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72363",
    "user": "https://github.com/robertwb"
}
```

It would be good to do this as a mercurial bundle, so that the history and other merges will follow correctly.



---

archive/issue_comments_072364.json:
```json
{
    "body": "Bundle replacing trac_8218_move.patch.  This should allow us to keep the repository information.",
    "created_at": "2010-02-09T20:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72364",
    "user": "https://github.com/roed314"
}
```

Bundle replacing trac_8218_move.patch.  This should allow us to keep the repository information.



---

archive/issue_comments_072365.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72365",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072366.json:
```json
{
    "body": "Attachment [trac_8218_move.bundle](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move.bundle) by @roed314 created at 2010-02-09 20:09:08\n\nI created the bundle with \n\n```\nsage -hg bundle -r 13801 --base 13800 ~/patches-out/trac_8218_move.bundle\n```\nI believe this is right, but it's been a while since I used bundles.",
    "created_at": "2010-02-09T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72366",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8218_move.bundle](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move.bundle) by @roed314 created at 2010-02-09 20:09:08

I created the bundle with 

```
sage -hg bundle -r 13801 --base 13800 ~/patches-out/trac_8218_move.bundle
```
I believe this is right, but it's been a while since I used bundles.



---

archive/issue_comments_072367.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T20:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72367",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072368.json:
```json
{
    "body": "Oops.  Forgot to fix pickles.  Doing so now...",
    "created_at": "2010-02-09T20:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72368",
    "user": "https://github.com/roed314"
}
```

Oops.  Forgot to fix pickles.  Doing so now...



---

archive/issue_comments_072369.json:
```json
{
    "body": "Attachment [trac_8218_fixes.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes.patch) by @roed314 created at 2010-02-09 21:37:39\n\nFixes the imports.",
    "created_at": "2010-02-09T21:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72369",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8218_fixes.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes.patch) by @roed314 created at 2010-02-09 21:37:39

Fixes the imports.



---

archive/issue_comments_072370.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-09T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72370",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072371.json:
```json
{
    "body": "Pickling should work now.",
    "created_at": "2010-02-09T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72371",
    "user": "https://github.com/roed314"
}
```

Pickling should work now.



---

archive/issue_comments_072372.json:
```json
{
    "body": "Has this been checked on Solaris? The patches are huge, so there is a good chance this will break on one platform or another. \n\nThere's general information about building on Solaris at\n\nhttp://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\nhttp://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary\nwhich will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-22T00:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72372",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Has this been checked on Solaris? The patches are huge, so there is a good chance this will break on one platform or another. 

There's general information about building on Solaris at

http://wiki.sagemath.org/solaris

Information specifically for 't2' at

http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary
which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_072373.json:
```json
{
    "body": "Remove assignee @roed314.",
    "created_at": "2010-02-22T00:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72373",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Remove assignee @roed314.



---

archive/issue_comments_072374.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-22T00:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72374",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_072375.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-22T19:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72375",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072376.json:
```json
{
    "body": "The content, not the size, of the patches would determine whether there's any platform-dependent code here, and I highly doubt there is. \n\nWhat I've looked at so far looks good (I started to do this myself once, but unfortunately there was some hitch and by the time I got to it again rebasing was neigh impossible). I hope to be able to get a review on this soon (just a matter of finding time).",
    "created_at": "2010-02-22T19:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72376",
    "user": "https://github.com/robertwb"
}
```

The content, not the size, of the patches would determine whether there's any platform-dependent code here, and I highly doubt there is. 

What I've looked at so far looks good (I started to do this myself once, but unfortunately there was some hitch and by the time I got to it again rebasing was neigh impossible). I hope to be able to get a review on this soon (just a matter of finding time).



---

archive/issue_comments_072377.json:
```json
{
    "body": "I do realise it is the content, not the size, but small innocuous looking patches have screwed up the build either on not only Solaris, but also Linux and OS X too. \n\nIt's difficult to me to see how we can know unless it is tested.",
    "created_at": "2010-02-22T19:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72377",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I do realise it is the content, not the size, but small innocuous looking patches have screwed up the build either on not only Solaris, but also Linux and OS X too. 

It's difficult to me to see how we can know unless it is tested.



---

archive/issue_comments_072378.json:
```json
{
    "body": "Rebased against 4.3.3: a bundle including all the moves; should be applied first",
    "created_at": "2010-02-23T14:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72378",
    "user": "https://github.com/roed314"
}
```

Rebased against 4.3.3: a bundle including all the moves; should be applied first



---

archive/issue_comments_072379.json:
```json
{
    "body": "Attachment [trac_8218_move_433.bundle](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move_433.bundle) by @JohnCremona created at 2010-03-02 17:26:49\n\nHow do I apply a bundle?  Can it be done in queues?",
    "created_at": "2010-03-02T17:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72379",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8218_move_433.bundle](tarball://root/attachments/some-uuid/ticket8218/trac_8218_move_433.bundle) by @JohnCremona created at 2010-03-02 17:26:49

How do I apply a bundle?  Can it be done in queues?



---

archive/issue_comments_072380.json:
```json
{
    "body": "Within the deve/sage directory,\n\n```\nsage -hg unbundle trac_8218_move_433.bundle\n```",
    "created_at": "2010-03-02T17:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72380",
    "user": "https://github.com/roed314"
}
```

Within the deve/sage directory,

```
sage -hg unbundle trac_8218_move_433.bundle
```



---

archive/issue_comments_072381.json:
```json
{
    "body": "Oh, and it can't be done in queues.  If you want to work with a patch, use `trac_8218_move.patch` instead.  I think that should apply; if not the only thing that patch or the bundle do is move a bunch of files (see a previous comment for the list).  If one of the hunks fails, just use `sage -hg rename`.",
    "created_at": "2010-03-02T17:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72381",
    "user": "https://github.com/roed314"
}
```

Oh, and it can't be done in queues.  If you want to work with a patch, use `trac_8218_move.patch` instead.  I think that should apply; if not the only thing that patch or the bundle do is move a bunch of files (see a previous comment for the list).  If one of the hunks fails, just use `sage -hg rename`.



---

archive/issue_comments_072382.json:
```json
{
    "body": "Sorry, still failing.  After I unbundle the bundle I can neither run Sage nor rebuild it nor apply the \"fix\" patch, and have to delete the entire clone.  The \"move\" patch does not apply to 4.3.3.\n\nIf you could post the exact sequence of commands needs to go from a fresh 4.3.3, starting with (say) sage -clone 8218  and ending with sage -br (or similar), then I'll willingly test it.",
    "created_at": "2010-03-02T20:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72382",
    "user": "https://github.com/JohnCremona"
}
```

Sorry, still failing.  After I unbundle the bundle I can neither run Sage nor rebuild it nor apply the "fix" patch, and have to delete the entire clone.  The "move" patch does not apply to 4.3.3.

If you could post the exact sequence of commands needs to go from a fresh 4.3.3, starting with (say) sage -clone 8218  and ending with sage -br (or similar), then I'll willingly test it.



---

archive/issue_comments_072383.json:
```json
{
    "body": "Try the following (and let me know if it doesn't work):\n\n```\ncd $SAGE-ROOT\nsage -clone 8218\ncd devel/sage-8218/\nsage -hg unbundle trac_8218_move.bundle\nsage -hg merge\nsage -hg commit -m \"Merge\"\nsage -hg qinit\nsage -hg qimport trac_8218_fixes_433.patch\nsage -hg qpush\nsage -br\n```",
    "created_at": "2010-03-05T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72383",
    "user": "https://github.com/roed314"
}
```

Try the following (and let me know if it doesn't work):

```
cd $SAGE-ROOT
sage -clone 8218
cd devel/sage-8218/
sage -hg unbundle trac_8218_move.bundle
sage -hg merge
sage -hg commit -m "Merge"
sage -hg qinit
sage -hg qimport trac_8218_fixes_433.patch
sage -hg qpush
sage -br
```



---

archive/issue_comments_072384.json:
```json
{
    "body": "OK, I did that (except with the bundle trac_8218_move_433.bundle),  applying it all to 4.3.4.alpha0.  The merge is ok (one piece of fuzz).  The rebuild took a long time.  But sage -br ended up not running properly:\n\n```\nAttributeError                            Traceback (most recent call last)\n\n/home/john/sage-current/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/home/john/sage-4.3.4.alpha0/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6 \n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9 \n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     70 get_sigs()\n     71 \n---> 72 from sage.rings.all      import *\n     73 from sage.matrix.all     import *\n     74 \n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/all.py in <module>()\n     88 \n     89 # Algebraic numbers\n\n---> 90 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n     91                    AlgebraicReal, is_AlgebraicReal,\n     92                    AlgebraicField, is_AlgebraicField, QQbar,\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/qqbar.py in <module>()\n   1410 \n   1411 # Cache some commonly-used polynomial rings\n\n-> 1412 QQx = QQ['x']\n   1413 QQx_x = QQx.gen()\n   1414 QQy = QQ['y']\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2551)()\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)\n    341                 raise TypeError, \"if second arguments is a string with no commas, then there must be no other non-optional arguments\"\n    342             name = arg1\n--> 343             R = _single_variate(base_ring, name, sparse, implementation)\n    344         else:\n    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):\n\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)\n    421 \n    422         elif base_ring.is_field(proof = False):\n--> 423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)\n    424 \n    425         elif base_ring.is_integral_domain(proof = False):\n\n/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, element_class, implementation)\n   1194         if implementation is None: implementation=\"NTL\"\n   1195         if implementation == \"NTL\" and \\\n-> 1196                 sage.rings.finite_field.is_FiniteField(base_ring):\n   1197             p=base_ring.characteristic()\n   1198             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext\n\nAttributeError: 'module' object has no attribute 'finite_field'\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```",
    "created_at": "2010-03-06T22:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72384",
    "user": "https://github.com/JohnCremona"
}
```

OK, I did that (except with the bundle trac_8218_move_433.bundle),  applying it all to 4.3.4.alpha0.  The merge is ok (one piece of fuzz).  The rebuild took a long time.  But sage -br ended up not running properly:

```
AttributeError                            Traceback (most recent call last)

/home/john/sage-current/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/home/john/sage-4.3.4.alpha0/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/home/john/sage-current/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/home/john/sage-current/local/lib/python2.6/site-packages/sage/all.py in <module>()
     70 get_sigs()
     71 
---> 72 from sage.rings.all      import *
     73 from sage.matrix.all     import *
     74 

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/all.py in <module>()
     88 
     89 # Algebraic numbers

---> 90 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     91                    AlgebraicReal, is_AlgebraicReal,
     92                    AlgebraicField, is_AlgebraicField, QQbar,

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/qqbar.py in <module>()
   1410 
   1411 # Cache some commonly-used polynomial rings

-> 1412 QQx = QQ['x']
   1413 QQx_x = QQx.gen()
   1414 QQy = QQ['y']

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2551)()

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):


/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    421 
    422         elif base_ring.is_field(proof = False):
--> 423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)
    424 
    425         elif base_ring.is_integral_domain(proof = False):

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, element_class, implementation)
   1194         if implementation is None: implementation="NTL"
   1195         if implementation == "NTL" and \
-> 1196                 sage.rings.finite_field.is_FiniteField(base_ring):
   1197             p=base_ring.characteristic()
   1198             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext

AttributeError: 'module' object has no attribute 'finite_field'
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

archive/issue_comments_072385.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T22:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72385",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072386.json:
```json
{
    "body": "It looks like some additional patches got applied after what I based mine on...  Sorry about that.  I'll update the patch and post a new one soon.\n\nThis does illustrate why I'd like to get this reviewed.  :-)",
    "created_at": "2010-03-07T05:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72386",
    "user": "https://github.com/roed314"
}
```

It looks like some additional patches got applied after what I based mine on...  Sorry about that.  I'll update the patch and post a new one soon.

This does illustrate why I'd like to get this reviewed.  :-)



---

archive/issue_comments_072387.json:
```json
{
    "body": "Attachment [trac_8218_fixes_433.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes_433.patch) by @roed314 created at 2010-03-12 01:00:12\n\nRebased against 4.3.3: should be applied after the bundle.",
    "created_at": "2010-03-12T01:00:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72387",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8218_fixes_433.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes_433.patch) by @roed314 created at 2010-03-12 01:00:12

Rebased against 4.3.3: should be applied after the bundle.



---

archive/issue_comments_072388.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-12T01:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72388",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072389.json:
```json
{
    "body": "You may need to clear out old files in the $SAGE_ROOT/devel/sage-8218/build directory.",
    "created_at": "2010-03-12T01:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72389",
    "user": "https://github.com/roed314"
}
```

You may need to clear out old files in the $SAGE_ROOT/devel/sage-8218/build directory.



---

archive/issue_comments_072390.json:
```json
{
    "body": "Sorry about this.  I made a new clone of 4.3.4.alpha1 and followed the instructions to the letter, but the final qpush gave this:\n\n```\napplying trac_8218_fixes_433.patch\npatching file sage/crypto/util.py\nHunk #1 FAILED at 31\n1 out of 1 hunks FAILED -- saving rejects to file sage/crypto/util.py.rej\npatching file sage/homology/chain_complex.py\nHunk #1 succeeded at 382 with fuzz 1 (offset 3 lines).\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8218_fixes_433.patch\n```\n\nIt might be better if someone who had any idea what they were doing took over this review -- I am clearly not competent!  For a start, if I depart in the slightest way from the list of commands then it does not work at all, but I don't understand why.\n\nMeanwhile I'll keep this clone in case sending any of the files will help (but despite the message here, there is nothing left in the \"working directory\").",
    "created_at": "2010-03-13T14:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72390",
    "user": "https://github.com/JohnCremona"
}
```

Sorry about this.  I made a new clone of 4.3.4.alpha1 and followed the instructions to the letter, but the final qpush gave this:

```
applying trac_8218_fixes_433.patch
patching file sage/crypto/util.py
Hunk #1 FAILED at 31
1 out of 1 hunks FAILED -- saving rejects to file sage/crypto/util.py.rej
patching file sage/homology/chain_complex.py
Hunk #1 succeeded at 382 with fuzz 1 (offset 3 lines).
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8218_fixes_433.patch
```

It might be better if someone who had any idea what they were doing took over this review -- I am clearly not competent!  For a start, if I depart in the slightest way from the list of commands then it does not work at all, but I don't understand why.

Meanwhile I'll keep this clone in case sending any of the files will help (but despite the message here, there is nothing left in the "working directory").



---

archive/issue_comments_072391.json:
```json
{
    "body": "I managed to successfully build this under 4.3.4.alpha1. I had the same failure at the final qpush as John above, but I found the .rej file and merged it by hand. Build was fine, but time-consuming (why doesn't sage -b know about parallel processing?). I got just two doctest failures, one in /sage/crypto/public_key/blum_goldwasser.py and one in doc/en/reference/coercion.rst; both were trivial to fix. \n\nI will upload a new patch replacing trac_8218_fixes_433.patch, which fixes the merge fuzz problems and corrects the two doctests.",
    "created_at": "2010-03-16T12:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72391",
    "user": "https://github.com/loefflerd"
}
```

I managed to successfully build this under 4.3.4.alpha1. I had the same failure at the final qpush as John above, but I found the .rej file and merged it by hand. Build was fine, but time-consuming (why doesn't sage -b know about parallel processing?). I got just two doctest failures, one in /sage/crypto/public_key/blum_goldwasser.py and one in doc/en/reference/coercion.rst; both were trivial to fix. 

I will upload a new patch replacing trac_8218_fixes_433.patch, which fixes the merge fuzz problems and corrects the two doctests.



---

archive/issue_comments_072392.json:
```json
{
    "body": "Set assignee to @loefflerd.",
    "created_at": "2010-03-16T12:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72392",
    "user": "https://github.com/loefflerd"
}
```

Set assignee to @loefflerd.



---

archive/issue_comments_072393.json:
```json
{
    "body": "Attachment [trac_8218_fixes_434alpha1.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes_434alpha1.patch) by @loefflerd created at 2010-03-16 12:40:16\n\napply after bundle (instead of trac_8218_fixes_433.patch)",
    "created_at": "2010-03-16T12:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72393",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8218_fixes_434alpha1.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_fixes_434alpha1.patch) by @loefflerd created at 2010-03-16 12:40:16

apply after bundle (instead of trac_8218_fixes_433.patch)



---

archive/issue_comments_072394.json:
```json
{
    "body": "As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)",
    "created_at": "2010-03-16T13:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72394",
    "user": "https://github.com/loefflerd"
}
```

As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)



---

archive/issue_comments_072395.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-16T13:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72395",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072396.json:
```json
{
    "body": "Replying to [comment:20 davidloeffler]:\n> As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)\n\n\nThere are not two different forks of the code base.  There are no Mercurial branches. \n\nBe aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. \n\nDave",
    "created_at": "2010-03-16T15:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72396",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:20 davidloeffler]:
> As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)


There are not two different forks of the code base.  There are no Mercurial branches. 

Be aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. 

Dave



---

archive/issue_comments_072397.json:
```json
{
    "body": "Replying to [comment:21 drkirkby]:\n> There are not two different forks of the code base.  There are no Mercurial branches. \n> \n> Be aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. \n\n\nAh! That's a totally different story then. Somehow I had got the incorrect impression that 4.3.0.1 was the latest Solaris version. I will run some tests on T2 and see what happens. Perhaps I had better do the same for the other tickets I have reviewed lately. My apologies!\n\nDavid",
    "created_at": "2010-03-16T16:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72397",
    "user": "https://github.com/loefflerd"
}
```

Replying to [comment:21 drkirkby]:
> There are not two different forks of the code base.  There are no Mercurial branches. 
> 
> Be aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. 


Ah! That's a totally different story then. Somehow I had got the incorrect impression that 4.3.0.1 was the latest Solaris version. I will run some tests on T2 and see what happens. Perhaps I had better do the same for the other tickets I have reviewed lately. My apologies!

David



---

archive/issue_comments_072398.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-16T16:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72398",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072399.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-03-16T16:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72399",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_072400.json:
```json
{
    "body": "Aargh! 19 hours later, my copy of 4.3.4.alpha1 I was building on T2 for testing is still only half-compiled, and in the meantime 4.3.4.rc0 has come out which is going to break this again!",
    "created_at": "2010-03-17T11:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72400",
    "user": "https://github.com/loefflerd"
}
```

Aargh! 19 hours later, my copy of 4.3.4.alpha1 I was building on T2 for testing is still only half-compiled, and in the meantime 4.3.4.rc0 has come out which is going to break this again!



---

archive/issue_comments_072401.json:
```json
{
    "body": "Attachment [trac_8218_doc.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_doc.patch) by @loefflerd created at 2010-03-18 15:34:53\n\napply after bundle + trac_8218_fixes_434alpha1.patch",
    "created_at": "2010-03-18T15:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72401",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8218_doc.patch](tarball://root/attachments/some-uuid/ticket8218/trac_8218_doc.patch) by @loefflerd created at 2010-03-18 15:34:53

apply after bundle + trac_8218_fixes_434alpha1.patch



---

archive/issue_comments_072402.json:
```json
{
    "body": "Here's a sneaky thing which I only discovered by accident: the reference manual index still points to the removed files in sage/rings that have been moved to sage/rings/finite_rings. This doesn't show up as an error if you install the bundle + patch and then build docs, because the old files are still floating around in the build directory.\n\nI'm putting this back to \"needs_review\"; once I can get a fully working Sage running on T2 I will test it on that and put it back to \"positive review\" if it passes.",
    "created_at": "2010-03-18T15:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72402",
    "user": "https://github.com/loefflerd"
}
```

Here's a sneaky thing which I only discovered by accident: the reference manual index still points to the removed files in sage/rings that have been moved to sage/rings/finite_rings. This doesn't show up as an error if you install the bundle + patch and then build docs, because the old files are still floating around in the build directory.

I'm putting this back to "needs_review"; once I can get a fully working Sage running on T2 I will test it on that and put it back to "positive review" if it passes.



---

archive/issue_comments_072403.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-18T15:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72403",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072404.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-21T14:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72404",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072405.json:
```json
{
    "body": "All seems to be well.",
    "created_at": "2010-03-21T14:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72405",
    "user": "https://github.com/loefflerd"
}
```

All seems to be well.



---

archive/issue_comments_072406.json:
```json
{
    "body": "Replying to [comment:26 davidloeffler]:\n> All seems to be well.\n\n\nDavid,\n\nCan you list here exactly what needs to be applied (and how)?  I want to start looking at the derivative patches for finite fields, so I have to get a clone with this one installed first -- and as you can see from earlier comments, I have not had much success so far.",
    "created_at": "2010-04-03T14:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72406",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:26 davidloeffler]:
> All seems to be well.


David,

Can you list here exactly what needs to be applied (and how)?  I want to start looking at the derivative patches for finite fields, so I have to get a clone with this one installed first -- and as you can see from earlier comments, I have not had much success so far.



---

archive/issue_comments_072407.json:
```json
{
    "body": "Hi John,\n\nFirst apply the bundle trac_8218_move_433.bundle, using the commands:\n\n```\nhg unbundle http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8218/trac_8218_move_433.bundle\nhg merge\nhg ci -m \"merged finite field bundle\"\n```\nThen use queues in the normal way to import the patches `trac_8218_fixes_434alpha1.patch` and `trac_8218_doc.patch` (in that order). This does work on 4.3.5, I just checked.\n\nBut the ball is in David Roe's court as far as the finite field patches are concerned. The sequence is #8218 --> #8332 -> #7880 -> #7883 -> #8333 -> #8334 -> #8335. So far\n\n- #8218 has a positive review\n- #7880 has a positive review\n- #7883 has been looked at by both me and Rob Bradshaw and we both agree that it needs more work.\n\nFurther downstream, #8333 builds independently of #7883, but many things in #8333 are horribly broken unless you also apply #8334, which does *not* build independently of #7883.\n\nDavid",
    "created_at": "2010-04-04T09:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72407",
    "user": "https://github.com/loefflerd"
}
```

Hi John,

First apply the bundle trac_8218_move_433.bundle, using the commands:

```
hg unbundle http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8218/trac_8218_move_433.bundle
hg merge
hg ci -m "merged finite field bundle"
```
Then use queues in the normal way to import the patches `trac_8218_fixes_434alpha1.patch` and `trac_8218_doc.patch` (in that order). This does work on 4.3.5, I just checked.

But the ball is in David Roe's court as far as the finite field patches are concerned. The sequence is #8218 --> #8332 -> #7880 -> #7883 -> #8333 -> #8334 -> #8335. So far

- #8218 has a positive review
- #7880 has a positive review
- #7883 has been looked at by both me and Rob Bradshaw and we both agree that it needs more work.

Further downstream, #8333 builds independently of #7883, but many things in #8333 are horribly broken unless you also apply #8334, which does *not* build independently of #7883.

David



---

archive/issue_comments_072408.json:
```json
{
    "body": "Replying to [comment:28 davidloeffler]:\n> Hi John,\n> \n\n...\n> \n> David\n> \n\n\nThanks!  I saw that some of the later patches had had positive reviews too, so maybe it's a bit late for me to join in.  But I thought that for a complicated interrelated set of patches like this, which non-trivial mathematical content, it would be good to have a small set of people looking at it rather than individuals.",
    "created_at": "2010-04-04T09:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72408",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:28 davidloeffler]:
> Hi John,
> 

...
> 
> David
> 


Thanks!  I saw that some of the later patches had had positive reviews too, so maybe it's a bit late for me to join in.  But I thought that for a complicated interrelated set of patches like this, which non-trivial mathematical content, it would be good to have a small set of people looking at it rather than individuals.



---

archive/issue_comments_072409.json:
```json
{
    "body": "I built this fine (following David L's instructions above).  Rebuilding the docs produced this:\n\n```\n/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field.rst:: WARNING: document isn't included in any toctree\n/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field_element.rst:: WARNING: document isn't included in any toctree\n/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod.rst:: WARNING: document isn't included in any toctree\n/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod_ring.rst:: WARNING: document isn't included in any toctree\n```\nIs this fixed later in the series?  If not, it should be fixed here.  So I am putting this back to \"needs work\".",
    "created_at": "2010-04-04T11:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72409",
    "user": "https://github.com/JohnCremona"
}
```

I built this fine (following David L's instructions above).  Rebuilding the docs produced this:

```
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field_element.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod_ring.rst:: WARNING: document isn't included in any toctree
```
Is this fixed later in the series?  If not, it should be fixed here.  So I am putting this back to "needs work".



---

archive/issue_comments_072410.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-04T11:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72410",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072411.json:
```json
{
    "body": "I had this too. I don't think it's a problem with the patch, it is because our documentation build system doesn't do the right thing when source files are removed and produces spurious warnings.",
    "created_at": "2010-04-04T12:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72411",
    "user": "https://github.com/loefflerd"
}
```

I had this too. I don't think it's a problem with the patch, it is because our documentation build system doesn't do the right thing when source files are removed and produces spurious warnings.



---

archive/issue_comments_072412.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-04T12:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72412",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072413.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-04T12:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72413",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019663.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T05:18:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8218#event-19663"
}
```



---

archive/issue_comments_072414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72414",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_072415.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_8218_move_433.bundle\n- trac_8218_fixes_434alpha1.patch\n- trac_8218_doc.patch",
    "created_at": "2010-04-15T05:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8218#issuecomment-72415",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_8218_move_433.bundle
- trac_8218_fixes_434alpha1.patch
- trac_8218_doc.patch
