# Issue 3406: [with patch, needs review] improve TermOrder class

archive/issues_003406.json:
```json
{
    "body": "Assignee: malb\n\nCC:  cremona wstein\n\n* doctest coverage 100%\n* improved documentation\n* more Python-ic interface\n* warning issued if an unknown term ordering is used (this addresses parts of #3383)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3406\n\n",
    "created_at": "2008-06-12T22:40:27Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] improve TermOrder class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3406",
    "user": "malb"
}
```
Assignee: malb

CC:  cremona wstein

* doctest coverage 100%
* improved documentation
* more Python-ic interface
* warning issued if an unknown term ordering is used (this addresses parts of #3383)

Issue created by migration from https://trac.sagemath.org/ticket/3406





---

archive/issue_comments_023887.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-15T21:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23887",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_023888.json:
```json
{
    "body": "I am seeing doctest failures:\n\n```\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 11 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 12 doctests failed\n```\n\n\nI am seeing similar issues in #3407.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T08:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23888",
    "user": "mabshoff"
}
```

I am seeing doctest failures:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 11 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 12 doctests failed
```


I am seeing similar issues in #3407.

Cheers,

Michael



---

archive/issue_comments_023889.json:
```json
{
    "body": "fixes the doctest issues in ell_...",
    "created_at": "2008-06-23T17:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23889",
    "user": "malb"
}
```

fixes the doctest issues in ell_...



---

archive/issue_comments_023890.json:
```json
{
    "body": "Attachment\n\nThe updated patch fixes the doctest issue. Elliptic curves used an unknown term ordering and the old -- buggy! -- code fell back to 'lex' silently. Now it is 'lex' explicitly, please speak up if that is not what is wanted.",
    "created_at": "2008-06-23T17:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23890",
    "user": "malb"
}
```

Attachment

The updated patch fixes the doctest issue. Elliptic curves used an unknown term ordering and the old -- buggy! -- code fell back to 'lex' silently. Now it is 'lex' explicitly, please speak up if that is not what is wanted.



---

archive/issue_comments_023891.json:
```json
{
    "body": "With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. \n\nJohn: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-25T00:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23891",
    "user": "mabshoff"
}
```

With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. 

John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.

Cheers,

Michael



---

archive/issue_comments_023892.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T00:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23892",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T00:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23893",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023894.json:
```json
{
    "body": "Replying to [comment:6 mabshoff]:\n> With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. \n> \n> John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.\n\nI think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).\n\nSo I see no reason to block 3.0.4 -- unless I have misunderstood the point here!\n\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2008-06-25T07:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23894",
    "user": "cremona"
}
```

Replying to [comment:6 mabshoff]:
> With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. 
> 
> John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.

I think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).

So I see no reason to block 3.0.4 -- unless I have misunderstood the point here!

> 
> Cheers,
> 
> Michael



---

archive/issue_comments_023895.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> Replying to [comment:6 mabshoff]:\n\n> > John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.\n> \n> I think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).\n> \n> So I see no reason to block 3.0.4 -- unless I have misunderstood the point here!\n\nJohn,\n\nI am sure we do understand each other 100% in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-25T07:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3406#issuecomment-23895",
    "user": "mabshoff"
}
```

Replying to [comment:8 cremona]:
> Replying to [comment:6 mabshoff]:

> > John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.
> 
> I think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).
> 
> So I see no reason to block 3.0.4 -- unless I have misunderstood the point here!

John,

I am sure we do understand each other 100% in this case.

Cheers,

Michael
