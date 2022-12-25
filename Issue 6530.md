# Issue 6530: methods not shown in documentation search

archive/issues_006530.json:
```json
{
    "body": "Assignee: @haraldschilly\n\nI did a search, on www.sagemath.org, for \"gram schmidt\".  In the Documentation section, there was no link returned for the documentation of the method \"gram_schmidt\", although this was exactly what I was looking for:\n\nhttp://www.sagemath.org/doc/reference/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.gram_schmidt\n\nPerhaps our custom Google search can be tweaked?\n\nIssue created by migration from https://trac.sagemath.org/ticket/6530\n\n",
    "created_at": "2009-07-14T07:39:42Z",
    "labels": [
        "component: website/wiki",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "methods not shown in documentation search",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6530",
    "user": "https://trac.sagemath.org/admin/accounts/users/gpannwitz"
}
```
Assignee: @haraldschilly

I did a search, on www.sagemath.org, for "gram schmidt".  In the Documentation section, there was no link returned for the documentation of the method "gram_schmidt", although this was exactly what I was looking for:

http://www.sagemath.org/doc/reference/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.gram_schmidt

Perhaps our custom Google search can be tweaked?

Issue created by migration from https://trac.sagemath.org/ticket/6530





---

archive/issue_comments_053135.json:
```json
{
    "body": "technically, it is all set so that it should work. I've added some redundant sites:\n\n```\n\thttp://www.sagemath.org/doc/numerical_sage    doc \n\thttp://www.sagemath.org/doc/a_tour_of_sage/    doc \n\thttp://www.sagemath.org/doc/installation/    doc \n\thttp://www.sagemath.org/doc/reference/    doc \n\thttp://www.sagemath.org/doc/developer/    developer \n\thttp://www.sagemath.org/doc/constructions    doc \n\thttp://www.sagemath.org/doc/tutorial/    doc \n```\n\n(label \"doc\" is for used for documentation)\n\nand a master page for the reference to point to all pages\n\n```\nhttp://www.sagemath.org/doc/reference/genindex-all.html [extract linked partial sites]   doc   \n```\n\n\nmaybe it works now better, but i'm not sure.",
    "created_at": "2009-07-14T08:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6530#issuecomment-53135",
    "user": "https://github.com/haraldschilly"
}
```

technically, it is all set so that it should work. I've added some redundant sites:

```
	http://www.sagemath.org/doc/numerical_sage    doc 
	http://www.sagemath.org/doc/a_tour_of_sage/    doc 
	http://www.sagemath.org/doc/installation/    doc 
	http://www.sagemath.org/doc/reference/    doc 
	http://www.sagemath.org/doc/developer/    developer 
	http://www.sagemath.org/doc/constructions    doc 
	http://www.sagemath.org/doc/tutorial/    doc 
```

(label "doc" is for used for documentation)

and a master page for the reference to point to all pages

```
http://www.sagemath.org/doc/reference/genindex-all.html [extract linked partial sites]   doc   
```


maybe it works now better, but i'm not sure.



---

archive/issue_events_006766.json:
```json
{
    "actor": "https://github.com/haraldschilly",
    "created_at": "2009-11-19T22:03:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6530",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6530#event-6766"
}
```



---

archive/issue_comments_053136.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T22:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6530#issuecomment-53136",
    "user": "https://github.com/haraldschilly"
}
```

Resolution: fixed



---

archive/issue_comments_053137.json:
```json
{
    "body": "tested again, it finds \"gram_schmidt\" now. only \"gram schmidt\" seems to be too vague. ticket can be closed.",
    "created_at": "2009-11-19T22:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6530#issuecomment-53137",
    "user": "https://github.com/haraldschilly"
}
```

tested again, it finds "gram_schmidt" now. only "gram schmidt" seems to be too vague. ticket can be closed.
