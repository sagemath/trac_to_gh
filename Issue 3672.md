# Issue 3672: wrong hg repository url in documentation

archive/issues_003672.json:
```json
{
    "body": "Assignee: tba\n\n* in `http://www.sagemath.org/doc/html/prog/node72.html` - last line\n* here:\n\n```\n/sage/doc$ grep -r \"sagemath.org/sage//hg\" *\nprog/node31.html:cd \"/home/jaap/sage/devel/doc\" &amp;&amp; hg pull -u http://sagemath.org/sage//hg//doc-main\nprog/node31.html:pulling from http://sagemath.org/sage//hg//doc-main\nprog/node31.html:cd \"/home/jaap/sage/devel/doc\" &amp;&amp; hg bundle  tmphg http://sagemath.org/sage//hg//doc-main\n```\n\n* ... and probably elsewhere, too:\n\nreplace `http://sagemath.org/sage/[/]hg` -> `http://hg.sagemath.org/` or `http://www.sagemath.org/hg/` (and probably a trailing \"`sage-main`\" in node31.html)\n\n[backref: posting in sage-devel by bill hart](http://groups.google.com/group/sage-devel/msg/43f43fe73c851d44)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3672\n\n",
    "created_at": "2008-07-18T09:58:05Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "wrong hg repository url in documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3672",
    "user": "@haraldschilly"
}
```
Assignee: tba

* in `http://www.sagemath.org/doc/html/prog/node72.html` - last line
* here:

```
/sage/doc$ grep -r "sagemath.org/sage//hg" *
prog/node31.html:cd "/home/jaap/sage/devel/doc" &amp;&amp; hg pull -u http://sagemath.org/sage//hg//doc-main
prog/node31.html:pulling from http://sagemath.org/sage//hg//doc-main
prog/node31.html:cd "/home/jaap/sage/devel/doc" &amp;&amp; hg bundle  tmphg http://sagemath.org/sage//hg//doc-main
```

* ... and probably elsewhere, too:

replace `http://sagemath.org/sage/[/]hg` -> `http://hg.sagemath.org/` or `http://www.sagemath.org/hg/` (and probably a trailing "`sage-main`" in node31.html)

[backref: posting in sage-devel by bill hart](http://groups.google.com/group/sage-devel/msg/43f43fe73c851d44)

Issue created by migration from https://trac.sagemath.org/ticket/3672





---

archive/issue_comments_025961.json:
```json
{
    "body": "I think with the transition to Sphinx-based documentation (3.4) this has been fixed.",
    "created_at": "2009-04-22T07:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3672#issuecomment-25961",
    "user": "@dandrake"
}
```

I think with the transition to Sphinx-based documentation (3.4) this has been fixed.



---

archive/issue_comments_025962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T07:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3672#issuecomment-25962",
    "user": "@dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_025963.json:
```json
{
    "body": "In fact, I checked in the current Developer's Guide, and it's *definitely* fixed.",
    "created_at": "2009-04-22T07:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3672#issuecomment-25963",
    "user": "@dandrake"
}
```

In fact, I checked in the current Developer's Guide, and it's *definitely* fixed.
