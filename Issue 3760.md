# Issue 3760: sage -t -long ell_finite_field.py fails with an out of memory error on 32-bit intel os x.

archive/issues_003760.json:
```json
{
    "body": "Assignee: was\n\n\n```\nTrying:\n    for p in prime_range(Integer(10000)):           #long time (~20s)###line 1014:_sage_    >>> for p in prime_range(10000):           #long time (~20s)\n          if p != Integer(389):\n              G=E.change_ring(GF(p)).abelian_group()\nExpecting nothing\n\nerror: no more memory\nSystem 5116k:5116k Appl 4666k/449k Malloc 4088k/3k Valloc 1024k/445k Pages 159/97 Regions 2:2\n\nhalt 14  \n\n         [19.0 s]\nexit code: 768\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long --verbose devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py\nTotal time for all tests: 19.0 seconds\nbsd:sage-3.1.alpha0 was$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3760\n\n",
    "created_at": "2008-08-02T19:05:06Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "title": "sage -t -long ell_finite_field.py fails with an out of memory error on 32-bit intel os x.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3760",
    "user": "was"
}
```
Assignee: was


```
Trying:
    for p in prime_range(Integer(10000)):           #long time (~20s)###line 1014:_sage_    >>> for p in prime_range(10000):           #long time (~20s)
          if p != Integer(389):
              G=E.change_ring(GF(p)).abelian_group()
Expecting nothing

error: no more memory
System 5116k:5116k Appl 4666k/449k Malloc 4088k/3k Valloc 1024k/445k Pages 159/97 Regions 2:2

halt 14  

         [19.0 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t -long --verbose devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py
Total time for all tests: 19.0 seconds
bsd:sage-3.1.alpha0 was$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/3760





---

archive/issue_comments_026707.json:
```json
{
    "body": "Could someone with 32-bit intel os x try this again, since it is possible that the patch for #3961 (merged in 3.1.2.alpha2) fixes this.\n\nIf not I can try to look into it but I'm not sure how to as it works fine on my laptop.",
    "created_at": "2008-09-04T16:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26707",
    "user": "cremona"
}
```

Could someone with 32-bit intel os x try this again, since it is possible that the patch for #3961 (merged in 3.1.2.alpha2) fixes this.

If not I can try to look into it but I'm not sure how to as it works fine on my laptop.



---

archive/issue_comments_026708.json:
```json
{
    "body": "#4179 is a duplicate of this ticket and has some additional info.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T08:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26708",
    "user": "mabshoff"
}
```

#4179 is a duplicate of this ticket and has some additional info.

Cheers,

Michael



---

archive/issue_comments_026709.json:
```json
{
    "body": "Just for the record: I had tried to get a grip on this issue, the outcome is trac ticket #4181 --- once that ticket is fixed, this one will (most probably) be resolved, too. Hopefully.\n\nCheers,\n\ngsw",
    "created_at": "2008-11-15T22:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26709",
    "user": "GeorgSWeber"
}
```

Just for the record: I had tried to get a grip on this issue, the outcome is trac ticket #4181 --- once that ticket is fixed, this one will (most probably) be resolved, too. Hopefully.

Cheers,

gsw



---

archive/issue_comments_026710.json:
```json
{
    "body": "The following code specifically seems to expose the problem:\n\n```\nE = EllipticCurve('389a')\nfor p in prime_range(Integer(10000)): \n    if p != Integer(389):\n        G=E.change_ring(GF(p)).abelian_group()\n```\n\nOn sage.math the memory increase is about 70 MB with Sage 3.2.2.rc0, so I have no idea how this could fail on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T03:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26710",
    "user": "mabshoff"
}
```

The following code specifically seems to expose the problem:

```
E = EllipticCurve('389a')
for p in prime_range(Integer(10000)): 
    if p != Integer(389):
        G=E.change_ring(GF(p)).abelian_group()
```

On sage.math the memory increase is about 70 MB with Sage 3.2.2.rc0, so I have no idea how this could fail on OSX.

Cheers,

Michael



---

archive/issue_comments_026711.json:
```json
{
    "body": "This exposes the problem much more clearly on my MacBook Pro:\n\n```\nteragon:sage-3.3.rc2 wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: E = EllipticCurve('389a')\nsage: time v = [E.change_ring(GF(p)) for p in prime_range(10000) if p != 389]\n| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |\n| Type notebook() for the GUI, and license() for information.        |\nerror: no more memory\nSystem 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2\n\nhalt 14\n```\n",
    "created_at": "2009-02-19T18:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26711",
    "user": "was"
}
```

This exposes the problem much more clearly on my MacBook Pro:

```
teragon:sage-3.3.rc2 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E = EllipticCurve('389a')
sage: time v = [E.change_ring(GF(p)) for p in prime_range(10000) if p != 389]
| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |
| Type notebook() for the GUI, and license() for information.        |
error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2

halt 14
```




---

archive/issue_comments_026712.json:
```json
{
    "body": "This is really a problem with Singular.  It has nothing to do with elliptic curve:\n\n\n```\nteragon:sage-3.3.rc2 wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: v = prime_range(4974); len(v)\n666\nsage: w = [GF(p)['x,y'] for p in v]\n| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |\n| Type notebook() for the GUI, and license() for information.        |\nerror: no more memory (mminit.cc)\nSystem 4608k:4608k Appl 4510k/97k Malloc 4093k/2k Valloc 512k/95k Pages 121/7 Regions 1:1\n\nhalt 14\nteragon:sage-3.3.rc2 wstein$ uname -a\nDarwin teragon.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386\n```\n\n\n\nArgh!",
    "created_at": "2009-02-19T19:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26712",
    "user": "was"
}
```

This is really a problem with Singular.  It has nothing to do with elliptic curve:


```
teragon:sage-3.3.rc2 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: v = prime_range(4974); len(v)
666
sage: w = [GF(p)['x,y'] for p in v]
| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |
| Type notebook() for the GUI, and license() for information.        |
error: no more memory (mminit.cc)
System 4608k:4608k Appl 4510k/97k Malloc 4093k/2k Valloc 512k/95k Pages 121/7 Regions 1:1

halt 14
teragon:sage-3.3.rc2 wstein$ uname -a
Darwin teragon.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386
```



Argh!



---

archive/issue_comments_026713.json:
```json
{
    "body": "By the way, it says \"mminit.cc\" in the above, since I hardcoded that into the singular library -- the message is being printed from a hardcoded message in mminit.cc in the singular *kernel*.",
    "created_at": "2009-02-19T19:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26713",
    "user": "was"
}
```

By the way, it says "mminit.cc" in the above, since I hardcoded that into the singular library -- the message is being printed from a hardcoded message in mminit.cc in the singular *kernel*.



---

archive/issue_comments_026714.json:
```json
{
    "body": "Yippieh:\n\n```\nsage: v = prime_range(4974); len(v)\n666\nsage: w = [GF(p)['x,y'] for p in v]\nsage: \n```\n",
    "created_at": "2009-02-22T22:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26714",
    "user": "GeorgSWeber"
}
```

Yippieh:

```
sage: v = prime_range(4974); len(v)
666
sage: w = [GF(p)['x,y'] for p in v]
sage: 
```




---

archive/issue_comments_026715.json:
```json
{
    "body": "Unless someone fixes #5344 in the next 24 hours this will not go into 3.4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-22T23:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26715",
    "user": "mabshoff"
}
```

Unless someone fixes #5344 in the next 24 hours this will not go into 3.4.

Cheers,

Michael



---

archive/issue_comments_026716.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-02-22T23:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26716",
    "user": "mabshoff"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_026717.json:
```json
{
    "body": "For the record:\n\nThe underlying problem is now known: Singular/omalloc relies on a version 2.6.5 of dlmalloc from 1998, and that version behaves bad on Macs.\n\nIn the course of the investigation, another Singular/kernel bug got in the way.\n\nI think I know how to *circumvent* this Singular/kernel bug (\"just\" drop in the recent dlmalloc 2.8.3 at the place of the old version, and/or prevent omalloc's \"configure\" from setting the macro \"OMALLOC_USES_MALLOC\"), but I thought I try and fix that other bug first.\n\n\nBTW:\nFrom the historical remarks in v2.8.3 in dlmalloc it seems plausible that the old v2.6.5 is the culprit also for the bad behaviour on Fedora 9/10 systems --- but this is ticket #5278. Which probably should be closed as a dupe (to this ticket here).",
    "created_at": "2009-02-23T08:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26717",
    "user": "GeorgSWeber"
}
```

For the record:

The underlying problem is now known: Singular/omalloc relies on a version 2.6.5 of dlmalloc from 1998, and that version behaves bad on Macs.

In the course of the investigation, another Singular/kernel bug got in the way.

I think I know how to *circumvent* this Singular/kernel bug ("just" drop in the recent dlmalloc 2.8.3 at the place of the old version, and/or prevent omalloc's "configure" from setting the macro "OMALLOC_USES_MALLOC"), but I thought I try and fix that other bug first.


BTW:
From the historical remarks in v2.8.3 in dlmalloc it seems plausible that the old v2.6.5 is the culprit also for the bad behaviour on Fedora 9/10 systems --- but this is ticket #5278. Which probably should be closed as a dupe (to this ticket here).



---

archive/issue_comments_026718.json:
```json
{
    "body": "Fixed in Sage 3.4.alpha0 via #4181 and #5344.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26718",
    "user": "mabshoff"
}
```

Fixed in Sage 3.4.alpha0 via #4181 and #5344.

Cheers,

Michael



---

archive/issue_comments_026719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3760#issuecomment-26719",
    "user": "mabshoff"
}
```

Resolution: fixed
