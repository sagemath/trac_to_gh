# Issue 12: confusing behaviour of pAdicField with series_print == False

archive/issues_000012.json:
```json
{
    "body": "Assignee: somebody\n\nThe following behaviour, while strictly speaking not incorrect, is quite confusing:\n\n```\nsage: K = pAdicField(5, series_print=False)\nsage:  K(37, prec=1)\n 5^0 * (37 + O(5^1))\n```\n\n\nReally, it should be reducing 37 mod 5 when you do the conversion, or at the very least when you print it out, otherwise you don't realise that 37 + O(5) and 7 + O(5) are really the same thing. (This caused me a few hours of head-scratching today because I thought that two things didn't agree when actually they did.)\n\nIf you use the default series_print=True, then this doesn't happen:\n\n```\nsage: K = pAdicField(5)\nsage:  K(37, prec=1)\n 2 + O(5)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/12\n\n",
    "created_at": "2006-09-12T20:15:57Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "confusing behaviour of pAdicField with series_print == False",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/12",
    "user": "dmharvey"
}
```
Assignee: somebody

The following behaviour, while strictly speaking not incorrect, is quite confusing:

```
sage: K = pAdicField(5, series_print=False)
sage:  K(37, prec=1)
 5^0 * (37 + O(5^1))
```


Really, it should be reducing 37 mod 5 when you do the conversion, or at the very least when you print it out, otherwise you don't realise that 37 + O(5) and 7 + O(5) are really the same thing. (This caused me a few hours of head-scratching today because I thought that two things didn't agree when actually they did.)

If you use the default series_print=True, then this doesn't happen:

```
sage: K = pAdicField(5)
sage:  K(37, prec=1)
 2 + O(5)
```



Issue created by migration from https://trac.sagemath.org/ticket/12





---

archive/issue_comments_000060.json:
```json
{
    "body": "This option doesn't exist anymore....",
    "created_at": "2007-01-13T01:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/12",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/12#issuecomment-60",
    "user": "was"
}
```

This option doesn't exist anymore....



---

archive/issue_comments_000061.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-01-13T01:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/12",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/12#issuecomment-61",
    "user": "was"
}
```

Resolution: invalid
