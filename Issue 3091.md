# Issue 3091: help() should give Sage help, not Python

archive/issues_003091.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nWhen I fired up Sage having never used it before, the first thing I tried after '1+1' and 'f(x) = x + x' followed by 'f(2)' was 'help'.  I was disappointed to see that it gave the Python help system.  I know Python, and I suspect even most Sage users who don't are more likely to want Sage help than Python help when they start out.\n\n\n```\nsage: help\nType help() for interactive help, or help(object) for help about object.\nsage: help()\n\nWelcome to Python 2.5!  This is the online help utility.\n\nIf this is your first time using Python, you should definitely check out\nthe tutorial on the Internet at http://www.python.org/doc/tut/.\n\nEnter the name of any module, keyword, or topic to get help on writing\nPython programs and using Python modules.  To quit this help utility and\nreturn to the interpreter, just type \"quit\".\n\nTo get a list of available modules, keywords, or topics, type \"modules\",\n\"keywords\", or \"topics\".  Each module also comes with a one-line summary\nof what it does; to list the modules whose summaries contain a given word\nsuch as \"spam\", type \"modules spam\".\n\nhelp> \n```\n\n\nI wound up using 'locals()' to see what was around -- a Python trick -- then 'help' on individual values that looked interesting.  I still don't know how to find introductory, overview help on Sage from the interactive prompt, or a list of functions without using tricks from a Python background.  I'm sure there's documentation on the web, but it's nice to be able to get to it while at the prompt.\n\nOf course the native Python 'help' function is invaluable for printing and paging through docstrings, once one knows the name of something.  I'm referring to its behavior with no arguments -- it should begin to give a clue about syntax, what's available, and where to look on the web, for Sage rather than for Python.\n\nThanks!\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3091\n\n",
    "created_at": "2008-05-03T07:32:46Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "help() should give Sage help, not Python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3091",
    "user": "gnprice"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

When I fired up Sage having never used it before, the first thing I tried after '1+1' and 'f(x) = x + x' followed by 'f(2)' was 'help'.  I was disappointed to see that it gave the Python help system.  I know Python, and I suspect even most Sage users who don't are more likely to want Sage help than Python help when they start out.


```
sage: help
Type help() for interactive help, or help(object) for help about object.
sage: help()

Welcome to Python 2.5!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://www.python.org/doc/tut/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> 
```


I wound up using 'locals()' to see what was around -- a Python trick -- then 'help' on individual values that looked interesting.  I still don't know how to find introductory, overview help on Sage from the interactive prompt, or a list of functions without using tricks from a Python background.  I'm sure there's documentation on the web, but it's nice to be able to get to it while at the prompt.

Of course the native Python 'help' function is invaluable for printing and paging through docstrings, once one knows the name of something.  I'm referring to its behavior with no arguments -- it should begin to give a clue about syntax, what's available, and where to look on the web, for Sage rather than for Python.

Thanks!


Issue created by migration from https://trac.sagemath.org/ticket/3091





---

archive/issue_comments_021338.json:
```json
{
    "body": "I just watched another first-time Sage user try typing 'help()' at the prompt. =)\n\nGreg",
    "created_at": "2008-05-07T01:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3091#issuecomment-21338",
    "user": "gnprice"
}
```

I just watched another first-time Sage user try typing 'help()' at the prompt. =)

Greg



---

archive/issue_comments_021339.json:
```json
{
    "body": "I think we can close this ticket.",
    "created_at": "2009-11-14T19:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3091#issuecomment-21339",
    "user": "@qed777"
}
```

I think we can close this ticket.



---

archive/issue_comments_021340.json:
```json
{
    "body": "With #6820 merged, should we close this ticket?",
    "created_at": "2010-01-16T19:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3091#issuecomment-21340",
    "user": "@qed777"
}
```

With #6820 merged, should we close this ticket?



---

archive/issue_comments_021341.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-01-16T19:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3091#issuecomment-21341",
    "user": "@qed777"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_021342.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-16T20:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3091#issuecomment-21342",
    "user": "@jhpalmieri"
}
```

Resolution: duplicate
