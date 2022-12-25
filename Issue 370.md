# Issue 370: improve the documentation of show

archive/issues_000370.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n> One suggestion I have arising from my problems is that the\n> documentation for the show command be improved.  It is a very\n> important function for most users.\n\nAgreed -- the documentation for show now is terrible.  It doesn't\neven mention that it can be used to show the typeset version of\nan object!\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/370\n\n",
    "created_at": "2007-05-19T04:56:48Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "improve the documentation of show",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/370",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
> One suggestion I have arising from my problems is that the
> documentation for the show command be improved.  It is a very
> important function for most users.

Agreed -- the documentation for show now is terrible.  It doesn't
even mention that it can be used to show the typeset version of
an object!

William
```


Issue created by migration from https://trac.sagemath.org/ticket/370





---

archive/issue_comments_001770.json:
```json
{
    "body": "What is the status of this?  Here is the current documentation when doing show?\n\n\n```\n        Show a graphics object x.\n    \n        OPTIONAL INPUT:\n            filename -- (default: None) string\n    \n        SOME OF THESE MAY APPLY:\n            dpi -- dots per inch\n            figsize -- [width, height] (same for square aspect)\n            axes -- (default: True)\n            fontsize -- positive integer\n            frame -- (default: False) draw a MATLAB-like frame around the image\n    \n        EXAMPLES:\n            sage: show(graphs(3))\n            sage: show(list(graphs(3)))\n\n```\n",
    "created_at": "2008-02-27T12:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/370#issuecomment-1770",
    "user": "https://github.com/mwhansen"
}
```

What is the status of this?  Here is the current documentation when doing show?


```
        Show a graphics object x.
    
        OPTIONAL INPUT:
            filename -- (default: None) string
    
        SOME OF THESE MAY APPLY:
            dpi -- dots per inch
            figsize -- [width, height] (same for square aspect)
            axes -- (default: True)
            fontsize -- positive integer
            frame -- (default: False) draw a MATLAB-like frame around the image
    
        EXAMPLES:
            sage: show(graphs(3))
            sage: show(list(graphs(3)))

```




---

archive/issue_comments_001771.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T12:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/370#issuecomment-1771",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_001772.json:
```json
{
    "body": "Unless the request is specified, I'm all for closing it.\n\n\n```\n[13:19] <mabshoff> malb: what is your take on #370 ?\n[13:19] <malb> it looks alright\n[13:20] <mabshoff> If you also think it should be closed as fixed please do so.\n```\n",
    "created_at": "2008-04-01T12:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/370#issuecomment-1772",
    "user": "https://github.com/malb"
}
```

Unless the request is specified, I'm all for closing it.


```
[13:19] <mabshoff> malb: what is your take on #370 ?
[13:19] <malb> it looks alright
[13:20] <mabshoff> If you also think it should be closed as fixed please do so.
```




---

archive/issue_events_000392.json:
```json
{
    "actor": "@malb",
    "created_at": "2008-04-01T12:25:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/370",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/370#event-392"
}
```
