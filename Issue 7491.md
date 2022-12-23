# Issue 7491: solve(x==x,x) fails

archive/issues_007491.json:
```json
{
    "body": "Assignee: burcin\n\n\n```\nsage: solve([x==x],x)\n```\n\ngives an exception.\n\nMaxima says this:\n\n```\n$ maxima -q\n(%i1) solve([x=x],x);\n(%o1)                                 all\n(%i2) \n```\n\n\nThere is a short [discussion](http://groups.google.cz/group/sage-devel/browse_thread/thread/ce3a256a9102c7fc) about this topic. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7491\n\n",
    "created_at": "2009-11-19T07:36:11Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "solve(x==x,x) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7491",
    "user": "robert.marik"
}
```
Assignee: burcin


```
sage: solve([x==x],x)
```

gives an exception.

Maxima says this:

```
$ maxima -q
(%i1) solve([x=x],x);
(%o1)                                 all
(%i2) 
```


There is a short [discussion](http://groups.google.cz/group/sage-devel/browse_thread/thread/ce3a256a9102c7fc) about this topic. 

Issue created by migration from https://trac.sagemath.org/ticket/7491





---

archive/issue_comments_063271.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-19T08:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7491#issuecomment-63271",
    "user": "robert.marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063272.json:
```json
{
    "body": "Attachment\n\nattached patch does the following\n\n```\n[marik@um-bc107 /opt/sage]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: solve\nsage: y=var('y');solve(SR(0),y,solution_dict=True)\n{y: r1}\nsage: y=var('y');solve(SR(0),y,solution_dict=True,multiplicities=True)\n({y: r1}, [])\nsage: solve(x==x,x,multiplicities=True)\n([x == r1], [])\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\n\n\nAll tests in symbolic and calculus passed.",
    "created_at": "2009-11-19T08:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7491#issuecomment-63272",
    "user": "robert.marik"
}
```

Attachment

attached patch does the following

```
[marik@um-bc107 /opt/sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: solve
sage: y=var('y');solve(SR(0),y,solution_dict=True)
{y: r1}
sage: y=var('y');solve(SR(0),y,solution_dict=True,multiplicities=True)
({y: r1}, [])
sage: solve(x==x,x,multiplicities=True)
([x == r1], [])
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
```


All tests in symbolic and calculus passed.



---

archive/issue_comments_063273.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-04T17:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7491#issuecomment-63273",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063274.json:
```json
{
    "body": "Positive review.  I'm not sure what the changes in relation.py bring to the game, but they don't hurt either.",
    "created_at": "2009-12-04T17:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7491#issuecomment-63274",
    "user": "kcrisman"
}
```

Positive review.  I'm not sure what the changes in relation.py bring to the game, but they don't hurt either.



---

archive/issue_comments_063275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T16:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7491#issuecomment-63275",
    "user": "mhansen"
}
```

Resolution: fixed
