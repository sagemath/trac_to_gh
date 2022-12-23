# Issue 425: Squash warning cause by using "-Wstrict-prototypes" in cython

archive/issues_000425.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb\n\nWhen compiling C code in cython some times \"-Wstrict-prototypes\" is added, causing the following warning:\n\n cc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for C/ObjC but not for C++\n\nIssue created by migration from https://trac.sagemath.org/ticket/425\n\n",
    "created_at": "2007-08-13T01:06:43Z",
    "labels": [
        "packages: standard",
        "trivial",
        "enhancement"
    ],
    "title": "Squash warning cause by using \"-Wstrict-prototypes\" in cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/425",
    "user": "mabshoff"
}
```
Assignee: was

CC:  robertwb

When compiling C code in cython some times "-Wstrict-prototypes" is added, causing the following warning:

 cc1plus: warning: command line option "-Wstrict-prototypes" is valid for C/ObjC but not for C++

Issue created by migration from https://trac.sagemath.org/ticket/425





---

archive/issue_comments_002131.json:
```json
{
    "body": "IIRC this gcc option is added by `python-cflags`:\n\n\n```\nSAGE_ROOT/local/bin/python2.5-config --cflags\n-I/home/malb/SAGE/local/include/python2.5 \\ \n-I/home/malb/SAGE/local/include/python2.5 \\\n-fno-strict-aliasing -DNDEBUG -g -O3 -Wall \\\n-Wstrict-prototypes\n```\n",
    "created_at": "2007-08-13T10:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/425#issuecomment-2131",
    "user": "malb"
}
```

IIRC this gcc option is added by `python-cflags`:


```
SAGE_ROOT/local/bin/python2.5-config --cflags
-I/home/malb/SAGE/local/include/python2.5 \ 
-I/home/malb/SAGE/local/include/python2.5 \
-fno-strict-aliasing -DNDEBUG -g -O3 -Wall \
-Wstrict-prototypes
```




---

archive/issue_comments_002132.json:
```json
{
    "body": "I agree with malb here that it is Python which is at fault here. Since this is only a minor annoyance I think we should just invalidate it.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T12:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/425#issuecomment-2132",
    "user": "mabshoff"
}
```

I agree with malb here that it is Python which is at fault here. Since this is only a minor annoyance I think we should just invalidate it.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_002133.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-23T23:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/425#issuecomment-2133",
    "user": "malb"
}
```

Resolution: invalid



---

archive/issue_comments_002134.json:
```json
{
    "body": "I'm all for **invalid**ating.",
    "created_at": "2008-08-23T23:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/425#issuecomment-2134",
    "user": "malb"
}
```

I'm all for **invalid**ating.



---

archive/issue_comments_002135.json:
```json
{
    "body": "Agreed. This is a distutils problem anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T23:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/425#issuecomment-2135",
    "user": "mabshoff"
}
```

Agreed. This is a distutils problem anyway.

Cheers,

Michael
