# Issue 2159: Gröbner bases over any field (cont'd)

archive/issues_002159.json:
```json
{
    "body": "Assignee: malb\n\nThis is a followup of {#2111}.\n\n```\nR.<x,y> = PolynomialRing(GF(2147483659),order='lex')\nI=ideal([x^3-2*y^2,3*x+y^4])\nI.dimension()\n...\n   ? no ring active\n   ? `ideal` is undefined\n   ? error occurred in STDIN line 170: `ideal sage85=[x + 1431655773*y^4, y^12 + 54*y^2];\nsage: I.variety()\n...\n   ? `2147483659` greater than 2147483647(max. integer representation)\n   ? error occurred in STDIN line 172: `ring sage86=2147483659,(x, y),lp;`\n   ? expected ring-expression. type 'help ring;'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2159\n\n",
    "created_at": "2008-02-14T17:25:14Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "title": "Gr\u00f6bner bases over any field (cont'd)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2159",
    "user": "zimmerma"
}
```
Assignee: malb

This is a followup of {#2111}.

```
R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
I=ideal([x^3-2*y^2,3*x+y^4])
I.dimension()
...
   ? no ring active
   ? `ideal` is undefined
   ? error occurred in STDIN line 170: `ideal sage85=[x + 1431655773*y^4, y^12 + 54*y^2];
sage: I.variety()
...
   ? `2147483659` greater than 2147483647(max. integer representation)
   ? error occurred in STDIN line 172: `ring sage86=2147483659,(x, y),lp;`
   ? expected ring-expression. type 'help ring;'
```


Issue created by migration from https://trac.sagemath.org/ticket/2159





---

archive/issue_comments_014173.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14173",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014174.json:
```json
{
    "body": "patch for dimension() to work in fields of large prime characteristic",
    "created_at": "2009-01-24T10:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14174",
    "user": "john_perry"
}
```

patch for dimension() to work in fields of large prime characteristic



---

archive/issue_comments_014175.json:
```json
{
    "body": "Attachment\n\nI'll submit a separate patch for variety, hopefully tomorrow.",
    "created_at": "2009-01-24T10:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14175",
    "user": "john_perry"
}
```

Attachment

I'll submit a separate patch for variety, hopefully tomorrow.



---

archive/issue_comments_014176.json:
```json
{
    "body": "**Review**\n* the doctest output of `verbose` should be changed to ignore the line numbers:\n\n```\nverbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation. \n```\n\n* `deg_lms` is referenced in a comment but doesn't exist;\n* could you give a reference for the algorithm implemented?",
    "created_at": "2009-01-24T11:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14176",
    "user": "malb"
}
```

**Review**
* the doctest output of `verbose` should be changed to ignore the line numbers:

```
verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation. 
```

* `deg_lms` is referenced in a comment but doesn't exist;
* could you give a reference for the algorithm implemented?



---

archive/issue_comments_014177.json:
```json
{
    "body": "Sorry, addressed all the issues you raised now. I was very surprised to learn that I had not cited the algorithm...",
    "created_at": "2009-01-24T18:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14177",
    "user": "john_perry"
}
```

Sorry, addressed all the issues you raised now. I was very surprised to learn that I had not cited the algorithm...



---

archive/issue_comments_014178.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T18:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14178",
    "user": "john_perry"
}
```

Attachment



---

archive/issue_comments_014179.json:
```json
{
    "body": "`variety` will take quite a bit of work. We should split that into a separate ticket & commit the patch for `dimension`, assuming that passes review.",
    "created_at": "2009-01-25T03:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14179",
    "user": "john_perry"
}
```

`variety` will take quite a bit of work. We should split that into a separate ticket & commit the patch for `dimension`, assuming that passes review.



---

archive/issue_comments_014180.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-25T19:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14180",
    "user": "malb"
}
```

Changing status from assigned to new.



---

archive/issue_comments_014181.json:
```json
{
    "body": "Changing assignee from malb to john_perry.",
    "created_at": "2009-01-25T19:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14181",
    "user": "malb"
}
```

Changing assignee from malb to john_perry.



---

archive/issue_comments_014182.json:
```json
{
    "body": "positive review for `dimension_mods.2.patch`",
    "created_at": "2009-01-31T18:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14182",
    "user": "malb"
}
```

positive review for `dimension_mods.2.patch`



---

archive/issue_comments_014183.json:
```json
{
    "body": "The variety stuff is now #5146",
    "created_at": "2009-01-31T18:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14183",
    "user": "malb"
}
```

The variety stuff is now #5146



---

archive/issue_comments_014184.json:
```json
{
    "body": "Merged dimension_mods.2.patch in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14184",
    "user": "mabshoff"
}
```

Merged dimension_mods.2.patch in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_014185.json:
```json
{
    "body": "Merged dimension_mods.2.patch in Sage 3.3.alpha4 and this time also closed the ticket :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T06:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14185",
    "user": "mabshoff"
}
```

Merged dimension_mods.2.patch in Sage 3.3.alpha4 and this time also closed the ticket :)

Cheers,

Michael



---

archive/issue_comments_014186.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T06:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2159#issuecomment-14186",
    "user": "mabshoff"
}
```

Resolution: fixed
