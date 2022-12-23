# Issue 4701: magma/sage interface -- coercion for single variable polynomials broken in some cases

archive/issues_004701.json:
```json
{
    "body": "Assignee: was\n\nFix this:\n\n```\nsage: R.<x> = GF(9,'a')[]\nsage: magma(x)\nboom\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4701\n\n",
    "created_at": "2008-12-05T00:32:30Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "magma/sage interface -- coercion for single variable polynomials broken in some cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4701",
    "user": "was"
}
```
Assignee: was

Fix this:

```
sage: R.<x> = GF(9,'a')[]
sage: magma(x)
boom
```


Issue created by migration from https://trac.sagemath.org/ticket/4701





---

archive/issue_comments_035414.json:
```json
{
    "body": "The attached patch fixes the problem by using _ref instead of name in the polynomial ring conversion function, just like in the multivariate case.   It also fixes a bunch of spots in the output of doctests where the magma variable names _sage_[n] were hard coded, by replacing them by _sage_[...].  Finally I updated the docstring of _ref to more clearly explain what it does.  So it's basically two lines of code followed by a bunch of doctest fixes/improvements.",
    "created_at": "2008-12-05T01:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35414",
    "user": "was"
}
```

The attached patch fixes the problem by using _ref instead of name in the polynomial ring conversion function, just like in the multivariate case.   It also fixes a bunch of spots in the output of doctests where the magma variable names _sage_[n] were hard coded, by replacing them by _sage_[...].  Finally I updated the docstring of _ref to more clearly explain what it does.  So it's basically two lines of code followed by a bunch of doctest fixes/improvements.



---

archive/issue_comments_035415.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-05T01:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35415",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_035416.json:
```json
{
    "body": "Attachment\n\nThere are problems.  My referee patch includes a few failing doctests.\n\n\n```\nsage: R = GF(3^5, 'a') # optional - magma\nsage: a = magma(R.gen()) # optional - magma\nsage: a^3 # optional - magma\na^3\nsage: a^3 + a # optional - magma\na^47\nsage: a.sage()\na\nsage: a.sage().parent()\nFinite Field in a of size 3^5\nsage: a.Eltseq()\n[ 0, 1, 0, 0, 0 ]\nsage: a.Sage()\nGF(243, 'a'.replace('$.', 'x').replace('.', ''), modulus=GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 1, 2, 0, 0, 0, 1 ]))(GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 0, 1 ]))\n```\n",
    "created_at": "2008-12-05T08:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35416",
    "user": "ncalexan"
}
```

Attachment

There are problems.  My referee patch includes a few failing doctests.


```
sage: R = GF(3^5, 'a') # optional - magma
sage: a = magma(R.gen()) # optional - magma
sage: a^3 # optional - magma
a^3
sage: a^3 + a # optional - magma
a^47
sage: a.sage()
a
sage: a.sage().parent()
Finite Field in a of size 3^5
sage: a.Eltseq()
[ 0, 1, 0, 0, 0 ]
sage: a.Sage()
GF(243, 'a'.replace('$.', 'x').replace('.', ''), modulus=GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 1, 2, 0, 0, 0, 1 ]))(GF(3)['a'.replace('$.', 'x').replace('.', '')]([ 0, 1 ]))
```




---

archive/issue_comments_035417.json:
```json
{
    "body": "Attachment\n\nAfter some discussion on IRC, wstein and I decided to review this positive and open a new ticket for the referee comments.  Apply trac_4701.patch and trac_4701_part2.patch only.",
    "created_at": "2008-12-06T23:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35417",
    "user": "ncalexan"
}
```

Attachment

After some discussion on IRC, wstein and I decided to review this positive and open a new ticket for the referee comments.  Apply trac_4701.patch and trac_4701_part2.patch only.



---

archive/issue_comments_035418.json:
```json
{
    "body": "See #4730 -- for dealing with conversions of finite field elements.",
    "created_at": "2008-12-06T23:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35418",
    "user": "was"
}
```

See #4730 -- for dealing with conversions of finite field elements.



---

archive/issue_comments_035419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35419",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035420.json:
```json
{
    "body": "Merged trac_4701.patch and trac_4701_part2.patch only in Sage 3.2.2.alpha1.\n\nNick: The issues I reported stem from the referee patch which I did apply accidentally [well, I didn't read the ticket in as much detail as I should have :(] and those are already #4730 as wstein pointed out on the last comment.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T09:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4701#issuecomment-35420",
    "user": "mabshoff"
}
```

Merged trac_4701.patch and trac_4701_part2.patch only in Sage 3.2.2.alpha1.

Nick: The issues I reported stem from the referee patch which I did apply accidentally [well, I didn't read the ticket in as much detail as I should have :(] and those are already #4730 as wstein pointed out on the last comment.

Cheers,

Michael
