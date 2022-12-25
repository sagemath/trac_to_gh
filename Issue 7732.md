# Issue 7732: remove binary files from ECL distribution

archive/issues_007732.json:
```json
{
    "body": "Assignee: tbd\n\nFigure out what these binary files are and if we can remove them:\n\n```\n         ecl-9.10.2-20091105cvs.p0/src/contrib/encodings/\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7732\n\n",
    "created_at": "2009-12-18T06:19:16Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "remove binary files from ECL distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7732",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Figure out what these binary files are and if we can remove them:

```
         ecl-9.10.2-20091105cvs.p0/src/contrib/encodings/
```


Issue created by migration from https://trac.sagemath.org/ticket/7732





---

archive/issue_comments_066317.json:
```json
{
    "body": "The author of ECL remarks:\n\n```\nDear William,\n\nthe encodings directory contains files which are needed by ECL to understand files in other formats -- windows encodings, japanese, russian, etc. It only works if you build ECL with support for Unicode (--enable-unicode)\n\nJuanjo\n```\n",
    "created_at": "2009-12-18T06:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66317",
    "user": "https://github.com/williamstein"
}
```

The author of ECL remarks:

```
Dear William,

the encodings directory contains files which are needed by ECL to understand files in other formats -- windows encodings, japanese, russian, etc. It only works if you build ECL with support for Unicode (--enable-unicode)

Juanjo
```




---

archive/issue_comments_066318.json:
```json
{
    "body": "More readable version:\n\n```\nDear William,\n\nthe encodings directory contains files which are needed by ECL to understand files in\n other formats -- windows encodings, japanese, russian, etc. It only works if you \nbuild ECL with support for Unicode (--enable-unicode)\n\nJuanjo\n```\n",
    "created_at": "2009-12-18T06:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66318",
    "user": "https://github.com/williamstein"
}
```

More readable version:

```
Dear William,

the encodings directory contains files which are needed by ECL to understand files in
 other formats -- windows encodings, japanese, russian, etc. It only works if you 
build ECL with support for Unicode (--enable-unicode)

Juanjo
```




---

archive/issue_comments_066319.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T06:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66319",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066320.json:
```json
{
    "body": "The new spkg is here:\n \n    http://wstein.org/home/wstein/patches/ecl-9.10.2-20091105cvs.p1.spkg",
    "created_at": "2009-12-18T06:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66320",
    "user": "https://github.com/williamstein"
}
```

The new spkg is here:
 
    http://wstein.org/home/wstein/patches/ecl-9.10.2-20091105cvs.p1.spkg



---

archive/issue_comments_066321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-21T13:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66321",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066322.json:
```json
{
    "body": "Looks safe and fine and works for me.",
    "created_at": "2009-12-21T13:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66322",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Looks safe and fine and works for me.



---

archive/issue_comments_066323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66323",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007944.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-03T22:19:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7732#event-7944"
}
```
