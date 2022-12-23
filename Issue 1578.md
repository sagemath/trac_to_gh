# Issue 1578: [with patch, with bundle] Make polynomial .diff() accept optional argument times for repeated differentiation.

archive/issues_001578.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: polynomial diff times repeat\n\nMake polynomial .diff() accept optional argument times for repeated differentiation.\n\nMakes diff do its thing multiple time if requested.\n\n```\n-    def diff(self, MPolynomial_libsingular variable, have_ring=True):\n+    def diff(self, MPolynomial_libsingular variable, times=1, have_ring=True):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1578\n\n",
    "created_at": "2007-12-21T03:53:30Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, with bundle] Make polynomial .diff() accept optional argument times for repeated differentiation.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1578",
    "user": "ncalexan"
}
```
Assignee: malb

Keywords: polynomial diff times repeat

Make polynomial .diff() accept optional argument times for repeated differentiation.

Makes diff do its thing multiple time if requested.

```
-    def diff(self, MPolynomial_libsingular variable, have_ring=True):
+    def diff(self, MPolynomial_libsingular variable, times=1, have_ring=True):
```


Issue created by migration from https://trac.sagemath.org/ticket/1578





---

archive/issue_comments_010047.json:
```json
{
    "body": "Hmm, bundle and patch might need to be rebased.  Sorry.",
    "created_at": "2007-12-21T03:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10047",
    "user": "ncalexan"
}
```

Hmm, bundle and patch might need to be rebased.  Sorry.



---

archive/issue_comments_010048.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-12-21T08:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10048",
    "user": "mabshoff"
}
```

Changing priority from minor to major.



---

archive/issue_comments_010049.json:
```json
{
    "body": "The failures are okay, since they just have redundant information.  I tested things out and all tests passed.",
    "created_at": "2007-12-22T21:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10049",
    "user": "mhansen"
}
```

The failures are okay, since they just have redundant information.  I tested things out and all tests passed.



---

archive/issue_comments_010050.json:
```json
{
    "body": "Attachment\n\nThis should be the final version; use this over the two earlier bundles and one earlier patch.",
    "created_at": "2008-01-13T02:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10050",
    "user": "ncalexan"
}
```

Attachment

This should be the final version; use this over the two earlier bundles and one earlier patch.



---

archive/issue_comments_010051.json:
```json
{
    "body": "I deleted the older patches and bundles.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T02:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10051",
    "user": "mabshoff"
}
```

I deleted the older patches and bundles.

Cheers,

Michael



---

archive/issue_comments_010052.json:
```json
{
    "body": "'times' seems like an odd name for the argument--it returns the \"times-th derivative\"?",
    "created_at": "2008-01-13T08:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10052",
    "user": "robertwb"
}
```

'times' seems like an odd name for the argument--it returns the "times-th derivative"?



---

archive/issue_comments_010053.json:
```json
{
    "body": "How about accepting monomials instead of variables only. Then x<sup>2</sup> would encode 2-times x, and x<sup>2</sup>y<sup>3</sup> would mean 3-times y and 2-times x.",
    "created_at": "2008-01-13T11:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10053",
    "user": "malb"
}
```

How about accepting monomials instead of variables only. Then x<sup>2</sup> would encode 2-times x, and x<sup>2</sup>y<sup>3</sup> would mean 3-times y and 2-times x.



---

archive/issue_comments_010054.json:
```json
{
    "body": "I don't know if we implement any, but there are functions such that `d^2f/dxdy != d^2 f/dydx`. \n\nHowever, I think the ability to pass in a monomial is an excellent idea. Perhaps beyond the scope of this patch though.",
    "created_at": "2008-01-14T18:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10054",
    "user": "robertwb"
}
```

I don't know if we implement any, but there are functions such that `d^2f/dxdy != d^2 f/dydx`. 

However, I think the ability to pass in a monomial is an excellent idea. Perhaps beyond the scope of this patch though.



---

archive/issue_comments_010055.json:
```json
{
    "body": "Changing assignee from malb to ncalexan.",
    "created_at": "2008-01-18T16:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10055",
    "user": "malb"
}
```

Changing assignee from malb to ncalexan.



---

archive/issue_comments_010056.json:
```json
{
    "body": "In mathematica, you can pass a list to the differentiate command and the function will be differentiated with respect to successive elements of the list.  So maybe something like:\n\nf.diff([x,y,y,x])\n\ncould specify differentiating first wrt x, then y, then y, and then x again.\n\nThe command in the patch could be invoked as:\n\nf.diff([x]*3)\n\nI agree that f.diff(x,3) looks better, though.",
    "created_at": "2008-02-04T17:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10056",
    "user": "jason"
}
```

In mathematica, you can pass a list to the differentiate command and the function will be differentiated with respect to successive elements of the list.  So maybe something like:

f.diff([x,y,y,x])

could specify differentiating first wrt x, then y, then y, and then x again.

The command in the patch could be invoked as:

f.diff([x]*3)

I agree that f.diff(x,3) looks better, though.



---

archive/issue_comments_010057.json:
```json
{
    "body": "We should probably note that this is supported by symbolic polynomials already.\n\n\n```\nsage: x,y=var('x y')\nsage: f=exp(2*x*y)\nsage: f.diff(x)\n2*y*e^(2*x*y)\nsage: f.diff(x,x)\n4*y^2*e^(2*x*y)\nsage: f.diff(x,2)\n4*y^2*e^(2*x*y)\nsage: f.diff(x,2,y)\n8*x*y^2*e^(2*x*y) + 8*y*e^(2*x*y)\nsage: f.diff(x,2,y,y)\n16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)\nsage: f.diff(x,2,y,2)\n16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)\n```\n",
    "created_at": "2008-02-04T17:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10057",
    "user": "jason"
}
```

We should probably note that this is supported by symbolic polynomials already.


```
sage: x,y=var('x y')
sage: f=exp(2*x*y)
sage: f.diff(x)
2*y*e^(2*x*y)
sage: f.diff(x,x)
4*y^2*e^(2*x*y)
sage: f.diff(x,2)
4*y^2*e^(2*x*y)
sage: f.diff(x,2,y)
8*x*y^2*e^(2*x*y) + 8*y*e^(2*x*y)
sage: f.diff(x,2,y,y)
16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)
sage: f.diff(x,2,y,2)
16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)
```




---

archive/issue_comments_010058.json:
```json
{
    "body": "The patch looks ok to me, looking at the diffs (I have not tried applying it).",
    "created_at": "2008-02-16T17:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10058",
    "user": "cremona"
}
```

The patch looks ok to me, looking at the diffs (I have not tried applying it).



---

archive/issue_comments_010059.json:
```json
{
    "body": "there is action on this at #753",
    "created_at": "2008-02-28T03:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10059",
    "user": "dmharvey"
}
```

there is action on this at #753



---

archive/issue_comments_010060.json:
```json
{
    "body": "I am closing this since it has been superseded by #753.",
    "created_at": "2008-03-03T14:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10060",
    "user": "dmharvey"
}
```

I am closing this since it has been superseded by #753.



---

archive/issue_comments_010061.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-03T14:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10061",
    "user": "dmharvey"
}
```

Resolution: duplicate



---

archive/issue_comments_010062.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-03T16:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10062",
    "user": "mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_010063.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-03T16:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10063",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_010064.json:
```json
{
    "body": "This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T16:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10064",
    "user": "mabshoff"
}
```

This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.

Cheers,

Michael



---

archive/issue_comments_010065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T16:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1578#issuecomment-10065",
    "user": "mabshoff"
}
```

Resolution: fixed
