# Issue 4514: Equality test fails for element coerced back into GL(2,7)

archive/issues_004514.json:
```json
{
    "body": "Assignee: tbd\n\nThe element below is constructed as an element of GL(2,7), but when converted into an element in GL(2,7) it is not equal to itself.\n\n```\nsage: G = GL(2,7)\nsage: z = G.center().an_element()\nsage: z\n[3 0]\n[0 3]\nsage: z in G\nTrue\nsage: G(z)\n[3 0]\n[0 3]\nsage: G(z) == z\nFalse\nsage: G(G(z)) == G(z)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4514\n\n",
    "created_at": "2008-11-13T17:20:00Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Equality test fails for element coerced back into GL(2,7)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4514",
    "user": "saliola"
}
```
Assignee: tbd

The element below is constructed as an element of GL(2,7), but when converted into an element in GL(2,7) it is not equal to itself.

```
sage: G = GL(2,7)
sage: z = G.center().an_element()
sage: z
[3 0]
[0 3]
sage: z in G
True
sage: G(z)
[3 0]
[0 3]
sage: G(z) == z
False
sage: G(G(z)) == G(z)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/4514





---

archive/issue_comments_033507.json:
```json
{
    "body": "Hmm. Maybe this isn't a bug afterall: the element z isn't really from G, but from G.center().",
    "created_at": "2008-11-13T17:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4514#issuecomment-33507",
    "user": "saliola"
}
```

Hmm. Maybe this isn't a bug afterall: the element z isn't really from G, but from G.center().



---

archive/issue_comments_033508.json:
```json
{
    "body": "So: let's close this as invalid?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T05:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4514#issuecomment-33508",
    "user": "mabshoff"
}
```

So: let's close this as invalid?

Cheers,

Michael



---

archive/issue_comments_033509.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-11-14T17:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4514#issuecomment-33509",
    "user": "saliola"
}
```

Resolution: invalid



---

archive/issue_comments_033510.json:
```json
{
    "body": "That's fine with me. I left it as is in case someone else might have something to say, but I think it has been long enough.",
    "created_at": "2008-11-14T17:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4514#issuecomment-33510",
    "user": "saliola"
}
```

That's fine with me. I left it as is in case someone else might have something to say, but I think it has been long enough.
