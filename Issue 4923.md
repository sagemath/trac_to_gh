# Issue 4923: convert sage.plot.* docstrings to Sphinx

archive/issues_004923.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4923\n\n",
    "created_at": "2009-01-01T22:55:12Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "convert sage.plot.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4923",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4923





---

archive/issue_comments_037357.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-02T02:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37357",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_037358.json:
```json
{
    "body": "I don't have the time or energy to review this fully right now, but I noticed one small issue: in line 61 in plot.py, \"Type {?} after each primitive\", change \"{?}\" to \"?\"",
    "created_at": "2009-01-07T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37358",
    "user": "jhpalmieri"
}
```

I don't have the time or energy to review this fully right now, but I noticed one small issue: in line 61 in plot.py, "Type {?} after each primitive", change "{?}" to "?"



---

archive/issue_comments_037359.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-21T19:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37359",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_037360.json:
```json
{
    "body": "Looks good except for the following mostly minor changes:\n\nplot.py, line 990: change 'suming' to 'summing'  (not your fault, an old typo)\n\nline 1141: I think EXAMPLES is indented too far: check the page [http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show)\n\nline 1827: `'-' (dashed)` should say `'--' (dashed)`\n\nline 2559: a dash \"--\" in some text got turned into a hyphen \"-\"\n\nline 2913: change \"increase\" to \"increases\" (the subject of the sentence is \"lowering\", which is singular) (not your fault)",
    "created_at": "2009-02-21T23:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37360",
    "user": "jhpalmieri"
}
```

Looks good except for the following mostly minor changes:

plot.py, line 990: change 'suming' to 'summing'  (not your fault, an old typo)

line 1141: I think EXAMPLES is indented too far: check the page [http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show)

line 1827: `'-' (dashed)` should say `'--' (dashed)`

line 2559: a dash "--" in some text got turned into a hyphen "-"

line 2913: change "increase" to "increases" (the subject of the sentence is "lowering", which is singular) (not your fault)



---

archive/issue_comments_037361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37361",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037362.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nMike: please open a ticket for the review problems.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37362",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Mike: please open a ticket for the review problems.

Cheers,

Michael



---

archive/issue_comments_037363.json:
```json
{
    "body": "See #5376.",
    "created_at": "2009-02-26T15:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37363",
    "user": "jhpalmieri"
}
```

See #5376.



---

archive/issue_comments_037364.json:
```json
{
    "body": "Thanks John.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T16:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4923#issuecomment-37364",
    "user": "mabshoff"
}
```

Thanks John.

Cheers,

Michael
