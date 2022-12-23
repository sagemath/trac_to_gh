# Issue 3911: come up with a good framework for citing stuff in docstrings

archive/issues_003911.json:
```json
{
    "body": "Assignee: tba\n\nthe framework should allow to generate a bibliography etc. while not reinventing the wheel: BibTeX? By citing in docstrings I mean stuff like this:\n\n```\nINPUT:\n   foo -- bar (as described in [BCDT]\n\nREFERENCES:\n[BCDT] Breuil, Conrad, Diamond, Taylor, \"Modularity ....\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3911\n\n",
    "created_at": "2008-08-20T14:29:10Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "come up with a good framework for citing stuff in docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3911",
    "user": "malb"
}
```
Assignee: tba

the framework should allow to generate a bibliography etc. while not reinventing the wheel: BibTeX? By citing in docstrings I mean stuff like this:

```
INPUT:
   foo -- bar (as described in [BCDT]

REFERENCES:
[BCDT] Breuil, Conrad, Diamond, Taylor, "Modularity ...."
```


Issue created by migration from https://trac.sagemath.org/ticket/3911





---

archive/issue_comments_027974.json:
```json
{
    "body": "This is fixed thanks to Sphinx and ReST which has native support for this.",
    "created_at": "2009-04-27T13:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3911#issuecomment-27974",
    "user": "malb"
}
```

This is fixed thanks to Sphinx and ReST which has native support for this.



---

archive/issue_comments_027975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-27T13:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3911#issuecomment-27975",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_027976.json:
```json
{
    "body": "Well, it should be documented in some way how we do things things. If such documentation exists a link from the ticket would be nice.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-27T15:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3911#issuecomment-27976",
    "user": "mabshoff"
}
```

Well, it should be documented in some way how we do things things. If such documentation exists a link from the ticket would be nice.

Cheers,

Michael



---

archive/issue_comments_027977.json:
```json
{
    "body": "It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations",
    "created_at": "2009-04-27T15:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3911#issuecomment-27977",
    "user": "malb"
}
```

It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations



---

archive/issue_comments_027978.json:
```json
{
    "body": "Replying to [comment:3 malb]:\n> It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations\n\nI now that. I meant in Sage's documentation so that documentation writes in Sage will use it :).\n\nCheers,\n\nMichael",
    "created_at": "2009-04-27T15:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3911#issuecomment-27978",
    "user": "mabshoff"
}
```

Replying to [comment:3 malb]:
> It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations

I now that. I meant in Sage's documentation so that documentation writes in Sage will use it :).

Cheers,

Michael
