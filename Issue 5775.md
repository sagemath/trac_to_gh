# Issue 5775: Building the documentation after -bdisting is broken

archive/issues_005775.json:
```json
{
    "body": "Assignee: mhansen\n\nThis is a tree that was bdisted from 3.4.1.rc2:\n\n```\nsphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel\n/sage/doc/output/doctrees/en/tutorial   .  /scratch/mabshoff/sage-\n3.4.1.rc3/devel/sage/doc/output/html/en/tutorial\nBuild finished.  The built documents can be found in /scratch\n/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/tutorial\nsphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel\n/sage/doc/output/doctrees/en/website   .  /scratch/mabshoff/sage-\n3.4.1.rc3/devel/sage/doc/output/html/en/website\nBuild finished.  The built documents can be found in /scratch\n/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/website\nTraceback (most recent call last): \n File \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common\n/builder.py\", line 668, in <module>\n    getattr(get_builder(name), type)()\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common\n/builder.py\", line 258, in _wrapper\n    getattr(get_builder(document), name)(*args, **kwds)\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common\n/builder.py\", line 348, in _wrapper\n    for module_name in self.get_modified_modules():\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common\n/builder.py\", line 415, in get_modified_modules\n    added, changed, removed = env.get_outdated_files(False)\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-\npackages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py\", line 400, in get_outdated_files\n    newmtime = path.getmtime(self.doc2path(docname))\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python\n/posixpath.py\", line 143, in getmtime\n    return os.stat(filename).st_mtime\nOSError: [Errno 2] No such file or directory: '/scratch/mabshoff\n/sage-3.4.1.rc2/devel/sage-main/doc/en/reference/sage/combinat/word/\nmorphism.rst'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5775\n\n",
    "created_at": "2009-04-13T07:51:55Z",
    "labels": [
        "distribution",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Building the documentation after -bdisting is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5775",
    "user": "mabshoff"
}
```
Assignee: mhansen

This is a tree that was bdisted from 3.4.1.rc2:

```
sphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel
/sage/doc/output/doctrees/en/tutorial   .  /scratch/mabshoff/sage-
3.4.1.rc3/devel/sage/doc/output/html/en/tutorial
Build finished.  The built documents can be found in /scratch
/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/tutorial
sphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel
/sage/doc/output/doctrees/en/website   .  /scratch/mabshoff/sage-
3.4.1.rc3/devel/sage/doc/output/html/en/website
Build finished.  The built documents can be found in /scratch
/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/website
Traceback (most recent call last): 
 File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 668, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 258, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 415, in get_modified_modules
    added, changed, removed = env.get_outdated_files(False)
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-
packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py", line 400, in get_outdated_files
    newmtime = path.getmtime(self.doc2path(docname))
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python
/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/scratch/mabshoff
/sage-3.4.1.rc2/devel/sage-main/doc/en/reference/sage/combinat/word/
morphism.rst'
```


Issue created by migration from https://trac.sagemath.org/ticket/5775





---

archive/issue_comments_045161.json:
```json
{
    "body": "To reproduce this: **-bdist**, unpack in some other place, run **make** -> **boom**.\n\nNote that deleting the output directory and restarting **make** gets past this problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T08:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5775#issuecomment-45161",
    "user": "mabshoff"
}
```

To reproduce this: **-bdist**, unpack in some other place, run **make** -> **boom**.

Note that deleting the output directory and restarting **make** gets past this problem.

Cheers,

Michael



---

archive/issue_comments_045162.json:
```json
{
    "body": "I don't care too much about this, so I am bumping it to 3.4.2 for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T22:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5775#issuecomment-45162",
    "user": "mabshoff"
}
```

I don't care too much about this, so I am bumping it to 3.4.2 for now.

Cheers,

Michael



---

archive/issue_comments_045163.json:
```json
{
    "body": "I don't see this problem any more. The process of \"-bdist\", unpack at a different directory, then run \"make\" works for me with Sage 4.3.2.alpha1. I'm closing this as fixed.",
    "created_at": "2010-02-02T23:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5775#issuecomment-45163",
    "user": "mvngu"
}
```

I don't see this problem any more. The process of "-bdist", unpack at a different directory, then run "make" works for me with Sage 4.3.2.alpha1. I'm closing this as fixed.



---

archive/issue_comments_045164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T23:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5775#issuecomment-45164",
    "user": "mvngu"
}
```

Resolution: fixed
