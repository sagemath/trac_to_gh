# Issue 5350: [with patch, needs review] sage-clone should use hard links for the build directory

archive/issues_005350.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  cwitty robertwb ralf@hemmecke.de\n\nWe copy the build directory when we're cloning the tree. This wastes disk space, and makes switching between branches slow, since new files need to be loaded from disk while the previous ones might already be in the cache.\n\nAttached patch to the scripts repository changes the sage-clone script to hard link the build directory. On my laptop this saves >450 MB per clone.\n\n\n```\nburcin@karr ~/sage/sage-3.3/devel $ du -sh sage-*\n593M    sage-hl\n125M    sage-hl1\n557M    sage-main\n```\n\n\nAlso the time to clone on my laptop goes from:\n\n```\nreal    0m14.709s\nuser    0m4.640s\nsys     0m1.924s\n```\n\nto\n\n```\nreal    0m6.100s\nuser    0m4.712s\nsys     0m0.928s\n```\n\nabout 2.8 seconds of which is spent in the sage -b step.\n\nUnfortunately, hard linking the .c, .cpp, and .h files doesn't work. This might be a problem with how cython handles its output when the output file is already present. This would save another ~100MB if it works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5350\n\n",
    "created_at": "2009-02-23T18:53:19Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] sage-clone should use hard links for the build directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5350",
    "user": "burcin"
}
```
Assignee: burcin

CC:  cwitty robertwb ralf@hemmecke.de

We copy the build directory when we're cloning the tree. This wastes disk space, and makes switching between branches slow, since new files need to be loaded from disk while the previous ones might already be in the cache.

Attached patch to the scripts repository changes the sage-clone script to hard link the build directory. On my laptop this saves >450 MB per clone.


```
burcin@karr ~/sage/sage-3.3/devel $ du -sh sage-*
593M    sage-hl
125M    sage-hl1
557M    sage-main
```


Also the time to clone on my laptop goes from:

```
real    0m14.709s
user    0m4.640s
sys     0m1.924s
```

to

```
real    0m6.100s
user    0m4.712s
sys     0m0.928s
```

about 2.8 seconds of which is spent in the sage -b step.

Unfortunately, hard linking the .c, .cpp, and .h files doesn't work. This might be a problem with how cython handles its output when the output file is already present. This would save another ~100MB if it works.

Issue created by migration from https://trac.sagemath.org/ticket/5350





---

archive/issue_comments_041214.json:
```json
{
    "body": "make sage-clone use hard links",
    "created_at": "2009-02-23T18:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41214",
    "user": "burcin"
}
```

make sage-clone use hard links



---

archive/issue_comments_041215.json:
```json
{
    "body": "Attachment\n\nI don't think we want this in a critical stable release :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-23T19:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41215",
    "user": "mabshoff"
}
```

Attachment

I don't think we want this in a critical stable release :)

Cheers,

Michael



---

archive/issue_comments_041216.json:
```json
{
    "body": "Cython 0.11 will make hard links on .c and .cpp files work too. \n\nhttp://trac.cython.org/cython_trac/ticket/220 and #4987",
    "created_at": "2009-03-18T04:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41216",
    "user": "robertwb"
}
```

Cython 0.11 will make hard links on .c and .cpp files work too. 

http://trac.cython.org/cython_trac/ticket/220 and #4987



---

archive/issue_comments_041217.json:
```json
{
    "body": "rebased for 4.0.1",
    "created_at": "2009-06-07T12:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41217",
    "user": "burcin"
}
```

rebased for 4.0.1



---

archive/issue_comments_041218.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-07T12:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41218",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041219.json:
```json
{
    "body": "Attachment\n\nattachment:trac_5350-clone_hardlink-take2.patch is a new version of the patch. It is rebased to 4.0.1. We now use hard links for autogenerated cython files and documentation output too.",
    "created_at": "2009-06-07T12:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41219",
    "user": "burcin"
}
```

Attachment

attachment:trac_5350-clone_hardlink-take2.patch is a new version of the patch. It is rebased to 4.0.1. We now use hard links for autogenerated cython files and documentation output too.



---

archive/issue_comments_041220.json:
```json
{
    "body": "Everything works fine, and the speedup is impressive, but I agree that a two-digit release might not be appropriate for something so invasive.",
    "created_at": "2009-06-21T22:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41220",
    "user": "rlm"
}
```

Everything works fine, and the speedup is impressive, but I agree that a two-digit release might not be appropriate for something so invasive.



---

archive/issue_comments_041221.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5350#issuecomment-41221",
    "user": "boothby"
}
```

Resolution: fixed
