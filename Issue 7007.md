# Issue 7007: generator of RR['t'] has a float attached

archive/issues_007007.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n[20:22] <jason-> here's something funny:\n[20:22] <jason-> sage: QQ['t'].gen()\n[20:22] <jason-> t\n[20:22] <jason-> sage: RR['t'].gen()\n[20:22] <jason-> 1.00000000000000*t\n[20:23] <jason-> what's the extra 1.0000000 in there for?\n[20:24] <jason-> that means that I get a very funny variables() function:\n[20:24] <jason-> sage: R.<t>=RR[]\n[20:24] <jason-> sage: (t^2).variables()\n[20:24] <jason-> (1.00000000000000*t,)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7007\n\n",
    "created_at": "2009-09-25T01:29:49Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "generator of RR['t'] has a float attached",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7007",
    "user": "@jasongrout"
}
```
Assignee: tbd


```
[20:22] <jason-> here's something funny:
[20:22] <jason-> sage: QQ['t'].gen()
[20:22] <jason-> t
[20:22] <jason-> sage: RR['t'].gen()
[20:22] <jason-> 1.00000000000000*t
[20:23] <jason-> what's the extra 1.0000000 in there for?
[20:24] <jason-> that means that I get a very funny variables() function:
[20:24] <jason-> sage: R.<t>=RR[]
[20:24] <jason-> sage: (t^2).variables()
[20:24] <jason-> (1.00000000000000*t,)
```


Issue created by migration from https://trac.sagemath.org/ticket/7007





---

archive/issue_comments_057944.json:
```json
{
    "body": "Same problem: \n\n```\nsage: RDF['t'].gen(0)\n1.0*t\n```\n",
    "created_at": "2009-09-25T01:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57944",
    "user": "@jasongrout"
}
```

Same problem: 

```
sage: RDF['t'].gen(0)
1.0*t
```




---

archive/issue_comments_057945.json:
```json
{
    "body": "This is nice, but it's a little troubling that it returns things looking \"exact\" that aren't actually exact.   Are there any Sage defaults for this?",
    "created_at": "2009-09-29T18:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57945",
    "user": "@kcrisman"
}
```

This is nice, but it's a little troubling that it returns things looking "exact" that aren't actually exact.   Are there any Sage defaults for this?



---

archive/issue_comments_057946.json:
```json
{
    "body": "Maybe the more natural fix to this is to change symbolic/expression_conversions.py in PolynomialConverter.__init__ , where instead of checking repr(v) one would check ring.base_ring()(1)*v, I think.  For this to work, there needs to be consistency in the representations of these, of course.\n\nHowever, as it turns out, somebody (Pynac?) simplifies like this patch does already, but for the symbolic ring, though only for the case with Ring(1), not Ring(2) or others.\n\n```\nsage: RR(1)*x\nx\nsage: RR(2)*x\n2.000..000*x\n```\n\nReverting that to at least printing 1.0 (and cutting off the extra zeros, which happens for RDF) seems to be the best strategy.  Then one could change PolynomialConverter.  But I don't know how to fix Pynac representations of this kind.\n\nIncidentally, note that #5755 probably will be fixed by this ticket, one way or another (the current patch fixes it, though as noted above not in a manner to my liking).",
    "created_at": "2009-09-29T18:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57946",
    "user": "@kcrisman"
}
```

Maybe the more natural fix to this is to change symbolic/expression_conversions.py in PolynomialConverter.__init__ , where instead of checking repr(v) one would check ring.base_ring()(1)*v, I think.  For this to work, there needs to be consistency in the representations of these, of course.

However, as it turns out, somebody (Pynac?) simplifies like this patch does already, but for the symbolic ring, though only for the case with Ring(1), not Ring(2) or others.

```
sage: RR(1)*x
x
sage: RR(2)*x
2.000..000*x
```

Reverting that to at least printing 1.0 (and cutting off the extra zeros, which happens for RDF) seems to be the best strategy.  Then one could change PolynomialConverter.  But I don't know how to fix Pynac representations of this kind.

Incidentally, note that #5755 probably will be fixed by this ticket, one way or another (the current patch fixes it, though as noted above not in a manner to my liking).



---

archive/issue_comments_057947.json:
```json
{
    "body": "Attachment [trac_7007.patch](tarball://root/attachments/some-uuid/ticket7007/trac_7007.patch) by @mwhansen created at 2009-09-29 19:41:45",
    "created_at": "2009-09-29T19:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57947",
    "user": "@mwhansen"
}
```

Attachment [trac_7007.patch](tarball://root/attachments/some-uuid/ticket7007/trac_7007.patch) by @mwhansen created at 2009-09-29 19:41:45



---

archive/issue_comments_057948.json:
```json
{
    "body": "After talking on IRC, I think this patch is okay.  In Sage, there is no such thing as the pure variable in this case; the variable is the polynomial 1.0000000*x.  As such, I think it's fine to extend the printing conveniences to 1.0000*x that are currently given to 1*x.\n\nPlus this fixes at least two issues (here and #5755).",
    "created_at": "2009-09-29T20:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57948",
    "user": "@jasongrout"
}
```

After talking on IRC, I think this patch is okay.  In Sage, there is no such thing as the pure variable in this case; the variable is the polynomial 1.0000000*x.  As such, I think it's fine to extend the printing conveniences to 1.0000*x that are currently given to 1*x.

Plus this fixes at least two issues (here and #5755).



---

archive/issue_comments_057949.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7007#issuecomment-57949",
    "user": "@mwhansen"
}
```

Resolution: fixed
