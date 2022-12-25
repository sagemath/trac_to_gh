# Issue 8130: UnicodeDecodeError (etc.) with view from the command line

archive/issues_008130.json:
```json
{
    "body": "Assignee: tbd\n\nTry this:\n\n```\nsage: s = u\"\u010d\"\nsage: view(s)\n```\n\nIt will throw a `UnicodeDecodeError`.  This much can be fixed using the \"experimental\" patch at #8083; however, after applying that patch,\n\n```\nsage: view(s)\n```\n\npops open a dvi/pdf file showing the wrong unicode character.\n\nSee #8083 and #8128 for tickets focusing on latex and unicode in the notebook.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8130\n\n",
    "created_at": "2010-01-30T04:51:58Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "UnicodeDecodeError (etc.) with view from the command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8130",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

Try this:

```
sage: s = u"č"
sage: view(s)
```

It will throw a `UnicodeDecodeError`.  This much can be fixed using the "experimental" patch at #8083; however, after applying that patch,

```
sage: view(s)
```

pops open a dvi/pdf file showing the wrong unicode character.

See #8083 and #8128 for tickets focusing on latex and unicode in the notebook.



Issue created by migration from https://trac.sagemath.org/ticket/8130





---

archive/issue_comments_071362.json:
```json
{
    "body": "What if we try just\n\n```python\nsage: s ='\u010d'\nsage: view(s)\nsage: s.decode('utf8')\nu'\\u010d'\n```\n\n?  This opens a PDF file for me that shows the expected character.",
    "created_at": "2010-01-30T11:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8130#issuecomment-71362",
    "user": "https://github.com/qed777"
}
```

What if we try just

```python
sage: s ='č'
sage: view(s)
sage: s.decode('utf8')
u'\u010d'
```

?  This opens a PDF file for me that shows the expected character.



---

archive/issue_comments_071363.json:
```json
{
    "body": "Should this be closed, or should \"view\" be able to handle unicode strings?",
    "created_at": "2010-01-30T16:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8130#issuecomment-71363",
    "user": "https://github.com/jhpalmieri"
}
```

Should this be closed, or should "view" be able to handle unicode strings?



---

archive/issue_comments_071364.json:
```json
{
    "body": "`view(u'\\u010d')` works for me, but I may well be misinterpreting your question.\u00a0 We could use `encoded_str` in place of `str` in some places.\n\nBy the way, it seems that [XeTeX / XeLaTeX](http://en.wikipedia.org/wiki/Xelatex) is currently one of the better ways to mix Unicode and LaTeX.  Unfortunately, the example in the article doesn't work for me with TeX Live on Linux --- the font is missing.",
    "created_at": "2010-01-31T00:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8130#issuecomment-71364",
    "user": "https://github.com/qed777"
}
```

`view(u'\u010d')` works for me, but I may well be misinterpreting your question.  We could use `encoded_str` in place of `str` in some places.

By the way, it seems that [XeTeX / XeLaTeX](http://en.wikipedia.org/wiki/Xelatex) is currently one of the better ways to mix Unicode and LaTeX.  Unfortunately, the example in the article doesn't work for me with TeX Live on Linux --- the font is missing.



---

archive/issue_comments_071365.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-31T00:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8130#issuecomment-71365",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: wontfix



---

archive/issue_comments_071366.json:
```json
{
    "body": "I don't think you're misinterpreting my question, I think I just don't understand unicode.  Let's close this, and if someone who wants or needs unicode (unlike me -- I was just playing around) has problems with view from the command line, we can open a new ticket.",
    "created_at": "2010-01-31T00:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8130#issuecomment-71366",
    "user": "https://github.com/jhpalmieri"
}
```

I don't think you're misinterpreting my question, I think I just don't understand unicode.  Let's close this, and if someone who wants or needs unicode (unlike me -- I was just playing around) has problems with view from the command line, we can open a new ticket.



---

archive/issue_events_008340.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-01-31T00:57:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8130",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8130#event-8340"
}
```
