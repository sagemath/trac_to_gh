# Issue 7732: remove binary files from ECL distribution

archive/issues_007732.json:
```json
{
    "body": "Assignee: tbd\n\nFigure out what these binary files are and if we can remove them:\n\n```\n         ecl-9.10.2-20091105cvs.p0/src/contrib/encodings/\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7732\n\n",
    "created_at": "2009-12-18T06:19:16Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "remove binary files from ECL distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7732",
    "user": "was"
}
```
Assignee: tbd

Figure out what these binary files are and if we can remove them:

```
         ecl-9.10.2-20091105cvs.p0/src/contrib/encodings/
```


Issue created by migration from https://trac.sagemath.org/ticket/7732





---

archive/issue_comments_066433.json:
```json
{
    "body": "The author of ECL remarks:\n\n```\nDear William,\n\nthe encodings directory contains files which are needed by ECL to understand files in other formats -- windows encodings, japanese, russian, etc. It only works if you build ECL with support for Unicode (--enable-unicode)\n\nJuanjo\n```\n",
    "created_at": "2009-12-18T06:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66433",
    "user": "was"
}
```

The author of ECL remarks:

```
Dear William,

the encodings directory contains files which are needed by ECL to understand files in other formats -- windows encodings, japanese, russian, etc. It only works if you build ECL with support for Unicode (--enable-unicode)

Juanjo
```




---

archive/issue_comments_066434.json:
```json
{
    "body": "More readable version:\n\n```\nDear William,\n\nthe encodings directory contains files which are needed by ECL to understand files in\n other formats -- windows encodings, japanese, russian, etc. It only works if you \nbuild ECL with support for Unicode (--enable-unicode)\n\nJuanjo\n```\n",
    "created_at": "2009-12-18T06:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66434",
    "user": "was"
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

archive/issue_comments_066435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T06:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66435",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066436.json:
```json
{
    "body": "The new spkg is here:\n \n    http://wstein.org/home/wstein/patches/ecl-9.10.2-20091105cvs.p1.spkg",
    "created_at": "2009-12-18T06:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66436",
    "user": "was"
}
```

The new spkg is here:
 
    http://wstein.org/home/wstein/patches/ecl-9.10.2-20091105cvs.p1.spkg



---

archive/issue_comments_066437.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-21T13:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66437",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066438.json:
```json
{
    "body": "Looks safe and fine and works for me.",
    "created_at": "2009-12-21T13:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66438",
    "user": "drkirkby"
}
```

Looks safe and fine and works for me.



---

archive/issue_comments_066439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7732#issuecomment-66439",
    "user": "mhansen"
}
```

Resolution: fixed
