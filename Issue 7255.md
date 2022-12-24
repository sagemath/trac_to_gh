# Issue 7255: sagenb notebook: reset() causes the worksheet to stop working.  fix this.

archive/issues_007255.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7255\n\n",
    "created_at": "2009-10-20T19:28:49Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sagenb notebook: reset() causes the worksheet to stop working.  fix this.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7255",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/7255





---

archive/issue_comments_060274.json:
```json
{
    "body": "patch to sagenb repo to fix this problem",
    "created_at": "2009-10-20T22:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60274",
    "user": "was"
}
```

patch to sagenb repo to fix this problem



---

archive/issue_comments_060275.json:
```json
{
    "body": "Attachment [trac_sagenb_7255.patch](tarball://root/attachments/some-uuid/ticket7255/trac_sagenb_7255.patch) by was created at 2009-10-20 22:11:26\n\nReset doesn't touch _ names, so the fix is easy -- just use `import sagenb.notebook.interact as _interact_` then everywhere in code refer to `_interact_` instead of `sagenb.notebook.interact`.  This is better on many levels.",
    "created_at": "2009-10-20T22:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60275",
    "user": "was"
}
```

Attachment [trac_sagenb_7255.patch](tarball://root/attachments/some-uuid/ticket7255/trac_sagenb_7255.patch) by was created at 2009-10-20 22:11:26

Reset doesn't touch _ names, so the fix is easy -- just use `import sagenb.notebook.interact as _interact_` then everywhere in code refer to `_interact_` instead of `sagenb.notebook.interact`.  This is better on many levels.



---

archive/issue_comments_060276.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-20T22:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60276",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060277.json:
```json
{
    "body": "I'm getting these errors when applying the patch - what directory should this be done from?\n\napplying /Users/mh/sagestuff/trac_sagenb_7255.patch\nunable to find 'sagenb/data/sage/js/notebook_lib.js' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/sage/js/notebook_lib.js.rej\nunable to find 'sagenb/notebook/interact.py' for patching\n5 out of 5 hunks FAILED -- saving rejects to file sagenb/notebook/interact.py.rej\nunable to find 'sagenb/notebook/worksheet.py' for patching\n2 out of 2 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej\nabort: patch failed to apply",
    "created_at": "2009-10-20T22:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60277",
    "user": "mhampton"
}
```

I'm getting these errors when applying the patch - what directory should this be done from?

applying /Users/mh/sagestuff/trac_sagenb_7255.patch
unable to find 'sagenb/data/sage/js/notebook_lib.js' for patching
1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/sage/js/notebook_lib.js.rej
unable to find 'sagenb/notebook/interact.py' for patching
5 out of 5 hunks FAILED -- saving rejects to file sagenb/notebook/interact.py.rej
unable to find 'sagenb/notebook/worksheet.py' for patching
2 out of 2 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej
abort: patch failed to apply



---

archive/issue_comments_060278.json:
```json
{
    "body": "OK, this seems to fix the problem.  I had some troubles with the patch at first but I think they are my fault.  Patch should be installed in \n\nspkg/build/sagenb-0.3.3/src/ \n\nand then\n\nsage -python setup.py install\n\nAfter doing this and doing sage -b, I got some strange errors about certain libraries, for example:\n\n___gmpz_tdiv_r_2exp referenced from libmpfr expected to be defined in /Volumes/E/sage-4.1.2.rc0/local/lib/libgmp.3.dylib\n\nMy sage install originally was in /Volumes/E/sage-4.1.2.rc0, and then I upgraded and renamed it.  I think this can be ignored as a quirk of my setup, I've been doing quite a bit of cloning and some patch reviews on it, so I am going ahead and giving this a positive review.",
    "created_at": "2009-10-21T02:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60278",
    "user": "mhampton"
}
```

OK, this seems to fix the problem.  I had some troubles with the patch at first but I think they are my fault.  Patch should be installed in 

spkg/build/sagenb-0.3.3/src/ 

and then

sage -python setup.py install

After doing this and doing sage -b, I got some strange errors about certain libraries, for example:

___gmpz_tdiv_r_2exp referenced from libmpfr expected to be defined in /Volumes/E/sage-4.1.2.rc0/local/lib/libgmp.3.dylib

My sage install originally was in /Volumes/E/sage-4.1.2.rc0, and then I upgraded and renamed it.  I think this can be ignored as a quirk of my setup, I've been doing quite a bit of cloning and some patch reviews on it, so I am going ahead and giving this a positive review.



---

archive/issue_comments_060279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-24T06:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7255#issuecomment-60279",
    "user": "was"
}
```

Resolution: fixed
