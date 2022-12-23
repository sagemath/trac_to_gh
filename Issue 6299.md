# Issue 6299: major scoping error introduced by refactoring dsage

archive/issues_006299.json:
```json
{
    "body": "Assignee: boothby\n\nConfiguration of dsage / notebook's secure certificate was completely 100% broken by factoring Dsage out from sage:\n\n\n```\n----------------------------------------------------------------------\nsage: notebook.setup()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()\n\nAttributeError: NotebookObject instance has no attribute 'settup'\nsage: notebook.setup()\nUsing dsage certificates.\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-4.0.2.rc0/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.pyc in notebook_setup(self)\n     39         print \"Using dsage certificates.\"\n     40         dsage = os.path.join(DOT_SAGE, 'dsage')\n---> 41         sage.dsage.all.dsage.setup()\n     42         shutil.copyfile(dsage + '/cacert.pem', private_pem)\n     43         shutil.copyfile(dsage + '/pubcert.pem', public_pem)\n\nNameError: global name 'sage' is not defined\nsage: \n\n----\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6299\n\n",
    "created_at": "2009-06-15T15:37:32Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "major scoping error introduced by refactoring dsage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6299",
    "user": "was"
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

archive/issue_comments_050254.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-15T19:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50254",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_050255.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-15T19:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50255",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050256.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-06-15T19:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50256",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_050257.json:
```json
{
    "body": "`notebook.setup()` worked for me on sage.math.",
    "created_at": "2009-06-15T20:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50257",
    "user": "ncalexan"
}
```

`notebook.setup()` worked for me on sage.math.



---

archive/issue_comments_050258.json:
```json
{
    "body": "works for me too; tested on 4.0.2.rc0",
    "created_at": "2009-06-15T22:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50258",
    "user": "boothby"
}
```

works for me too; tested on 4.0.2.rc0



---

archive/issue_comments_050259.json:
```json
{
    "body": "merged into 4.0.2.rc1",
    "created_at": "2009-06-15T23:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50259",
    "user": "was"
}
```

merged into 4.0.2.rc1



---

archive/issue_comments_050260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T23:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6299#issuecomment-50260",
    "user": "was"
}
```

Resolution: fixed
