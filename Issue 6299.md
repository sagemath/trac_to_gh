# Issue 6299: major scoping error introduced by refactoring dsage

archive/issues_006299.json:
```json
{
    "body": "Assignee: boothby\n\nConfiguration of dsage / notebook's secure certificate was completely 100% broken by factoring Dsage out from sage:\n\n\n```\n----------------------------------------------------------------------\nsage: notebook.setup()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()\n\nAttributeError: NotebookObject instance has no attribute 'settup'\nsage: notebook.setup()\nUsing dsage certificates.\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-4.0.2.rc0/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.pyc in notebook_setup(self)\n     39         print \"Using dsage certificates.\"\n     40         dsage = os.path.join(DOT_SAGE, 'dsage')\n---> 41         sage.dsage.all.dsage.setup()\n     42         shutil.copyfile(dsage + '/cacert.pem', private_pem)\n     43         shutil.copyfile(dsage + '/pubcert.pem', public_pem)\n\nNameError: global name 'sage' is not defined\nsage: \n\n----\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6299\n\n",
    "created_at": "2009-06-15T15:37:32Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "major scoping error introduced by refactoring dsage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6299",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Configuration of dsage / notebook's secure certificate was completely 100% broken by factoring Dsage out from sage:


```
----------------------------------------------------------------------
sage: notebook.setup()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()

AttributeError: NotebookObject instance has no attribute 'settup'
sage: notebook.setup()
Using dsage certificates.
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.0.2.rc0/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.pyc in notebook_setup(self)
     39         print "Using dsage certificates."
     40         dsage = os.path.join(DOT_SAGE, 'dsage')
---> 41         sage.dsage.all.dsage.setup()
     42         shutil.copyfile(dsage + '/cacert.pem', private_pem)
     43         shutil.copyfile(dsage + '/pubcert.pem', public_pem)

NameError: global name 'sage' is not defined
sage: 

----

```


Issue created by migration from https://trac.sagemath.org/ticket/6299





---

archive/issue_comments_050158.json:
```json
{
    "body": "Attachment [trac_6299.patch](tarball://root/attachments/some-uuid/ticket6299/trac_6299.patch) by @mwhansen created at 2009-06-15 19:02:45",
    "created_at": "2009-06-15T19:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50158",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6299.patch](tarball://root/attachments/some-uuid/ticket6299/trac_6299.patch) by @mwhansen created at 2009-06-15 19:02:45



---

archive/issue_comments_050159.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-15T19:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50159",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050160.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-06-15T19:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50160",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_050161.json:
```json
{
    "body": "`notebook.setup()` worked for me on sage.math.",
    "created_at": "2009-06-15T20:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50161",
    "user": "https://github.com/ncalexan"
}
```

`notebook.setup()` worked for me on sage.math.



---

archive/issue_comments_050162.json:
```json
{
    "body": "works for me too; tested on 4.0.2.rc0",
    "created_at": "2009-06-15T22:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50162",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me too; tested on 4.0.2.rc0



---

archive/issue_events_006541.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-06-15T23:18:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6299#event-6541"
}
```



---

archive/issue_comments_050163.json:
```json
{
    "body": "merged into 4.0.2.rc1",
    "created_at": "2009-06-15T23:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50163",
    "user": "https://github.com/williamstein"
}
```

merged into 4.0.2.rc1



---

archive/issue_comments_050164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T23:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50164",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
