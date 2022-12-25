# Issue 9761: Update zn_poly's SPKG.txt to indicate it depends on Python.

archive/issues_009761.json:
```json
{
    "body": "Assignee: mvngu\n\nAs noted at #9761, although the spkg-install script for zn_poly is a bash script, it actually calls a Python script `zn_poly-*/src/makemakefile.py`. Therefore the SPKG.txt file should indicate this dependency, as it is far from obvious. \n\nClearly this is a minor issue, but one worth fixing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9762\n\n",
    "created_at": "2010-08-18T11:49:26Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update zn_poly's SPKG.txt to indicate it depends on Python.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9761",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

As noted at #9761, although the spkg-install script for zn_poly is a bash script, it actually calls a Python script `zn_poly-*/src/makemakefile.py`. Therefore the SPKG.txt file should indicate this dependency, as it is far from obvious. 

Clearly this is a minor issue, but one worth fixing. 

Issue created by migration from https://trac.sagemath.org/ticket/9762





---

archive/issue_comments_095477.json:
```json
{
    "body": "Replying to [ticket:9762 drkirkby]:\n> Clearly this is a minor issue, but one worth fixing. \n\nIt's \"only\" documentation... ;-)",
    "created_at": "2010-08-18T12:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95477",
    "user": "https://github.com/nexttime"
}
```

Replying to [ticket:9762 drkirkby]:
> Clearly this is a minor issue, but one worth fixing. 

It's "only" documentation... ;-)



---

archive/issue_comments_095478.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> Replying to [ticket:9762 drkirkby]:\n> > Clearly this is a minor issue, but one worth fixing. \n> \n> It's \"only\" documentation... ;-)\n> \nTrue, but #9603 is more important, as it actually stops something building!\n\nDave",
    "created_at": "2010-08-18T13:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95478",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:1 leif]:
> Replying to [ticket:9762 drkirkby]:
> > Clearly this is a minor issue, but one worth fixing. 
> 
> It's "only" documentation... ;-)
> 
True, but #9603 is more important, as it actually stops something building!

Dave



---

archive/issue_comments_095479.json:
```json
{
    "body": "The `SPKG.txt` now says:\n\n```\n## Dependencies\n\n * GMP/MPIR\n * (some) Python (to create the Makefile)\n * GNU patch\n * NTL apparently only if we configured zn_poly differently (same for FLINT)\n```\n",
    "created_at": "2015-04-14T11:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95479",
    "user": "https://github.com/mezzarobba"
}
```

The `SPKG.txt` now says:

```
## Dependencies

 * GMP/MPIR
 * (some) Python (to create the Makefile)
 * GNU patch
 * NTL apparently only if we configured zn_poly differently (same for FLINT)
```




---

archive/issue_comments_095480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-14T11:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95480",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095481.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-14T12:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95481",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095482.json:
```json
{
    "body": "Oh yes, fixed years ago...",
    "created_at": "2015-04-14T13:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95482",
    "user": "https://github.com/nexttime"
}
```

Oh yes, fixed years ago...



---

archive/issue_events_009892.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-14T23:03:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9761#event-9892"
}
```



---

archive/issue_comments_095483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-14T23:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9761#issuecomment-95483",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
