# Issue 3912: sage -t foo.tex should also test listings blocks not only verbatim

archive/issues_003912.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mvngu\n\nsage -t can check stuff in \n\n```\n\\begin{verbatim}\nsage: 2 + 3\n5\n\\end{verbatim}\n```\n\n\nI propose to also support \n\n```\n\\begin{lstlisting}\nsage: 2 + 3\n5\n\\end{llstisting}\n```\n\nwhich looks so much nicer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3912\n\n",
    "created_at": "2008-08-20T14:31:47Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "sage -t foo.tex should also test listings blocks not only verbatim",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3912",
    "user": "@malb"
}
```
Assignee: tba

CC:  mvngu

sage -t can check stuff in 

```
\begin{verbatim}
sage: 2 + 3
5
\end{verbatim}
```


I propose to also support 

```
\begin{lstlisting}
sage: 2 + 3
5
\end{llstisting}
```

which looks so much nicer.

Issue created by migration from https://trac.sagemath.org/ticket/3912





---

archive/issue_comments_027979.json:
```json
{
    "body": "Changing keywords from \"\" to \"doctest\".",
    "created_at": "2014-07-25T09:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27979",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "doctest".



---

archive/issue_comments_027980.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-25T10:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27980",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_027981.json:
```json
{
    "body": "Changing keywords from \"doctest\" to \"doctest, latex\".",
    "created_at": "2014-07-25T10:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27981",
    "user": "@fchapoton"
}
```

Changing keywords from "doctest" to "doctest, latex".



---

archive/issue_comments_027982.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-07-25T10:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27982",
    "user": "@fchapoton"
}
```

New commits:



---

archive/issue_comments_027983.json:
```json
{
    "body": "See http://mvngu.wordpress.com/2010/06/27/typesetting-sage-code-listings-in-latex/ for nice parameters for the package `listings`.",
    "created_at": "2014-07-25T11:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27983",
    "user": "@fchapoton"
}
```

See http://mvngu.wordpress.com/2010/06/27/typesetting-sage-code-listings-in-latex/ for nice parameters for the package `listings`.



---

archive/issue_comments_027984.json:
```json
{
    "body": "[Line 153](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n153) contains a left parenthesis which is never closed.\n\nCould you also unify [Line 1142](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1142) and [Line 1219](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1219).",
    "created_at": "2014-07-27T09:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27984",
    "user": "@a-andre"
}
```

[Line 153](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n153) contains a left parenthesis which is never closed.

Could you also unify [Line 1142](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1142) and [Line 1219](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1219).



---

archive/issue_comments_027985.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-27T09:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27985",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027986.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-27T09:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27986",
    "user": "@a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-28T03:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3912#issuecomment-27987",
    "user": "@vbraun"
}
```

Resolution: fixed
