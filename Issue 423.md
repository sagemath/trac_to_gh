# Issue 423: command line help() --> modules fails for *some* people

archive/issues_000423.json:
```json
{
    "body": "Assignee: @williamstein\n\nDavid Harvey says\n\n```\n\nI can confirm this:\n\n\nsage: help()\n\nWelcome to Python 2.5!  This is the online help utility.\n\nIf this is your first time using Python, you should definitely check out\nthe tutorial on the Internet at http://www.python.org/doc/tut/.\n\nEnter the name of any module, keyword, or topic to get help on writing\nPython programs and using Python modules.  To quit this help utility and\nreturn to the interpreter, just type \"quit\".\n\nTo get a list of available modules, keywords, or topics, type \"modules\",\n\"keywords\", or \"topics\".  Each module also comes with a one-line summary\nof what it does; to list the modules whose summaries contain a given word\nsuch as \"spam\", type \"modules spam\".\n\nhelp> modules\n\nPlease wait a moment while I gather a list of all available modules...\n\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/Users/wdj/sagefiles/sage-2.7/<ipython console> in <module>()\n\n...\n\n++++++++++++++++++++++++++++++++++++++++++\n```\n\n\nFor other people (e.g., me) there's no problem.  Hmm. \n\nIssue created by migration from https://trac.sagemath.org/ticket/423\n\n",
    "created_at": "2007-08-10T20:55:49Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "command line help() --> modules fails for *some* people",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/423",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

David Harvey says

```

I can confirm this:


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

help> modules

Please wait a moment while I gather a list of all available modules...

---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/wdj/sagefiles/sage-2.7/<ipython console> in <module>()

...

++++++++++++++++++++++++++++++++++++++++++
```


For other people (e.g., me) there's no problem.  Hmm. 

Issue created by migration from https://trac.sagemath.org/ticket/423





---

archive/issue_comments_002112.json:
```json
{
    "body": "fixed by patching python itself (for sage-2.8.2)",
    "created_at": "2007-08-18T23:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/423#issuecomment-2112",
    "user": "https://github.com/williamstein"
}
```

fixed by patching python itself (for sage-2.8.2)



---

archive/issue_comments_002113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T23:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/423#issuecomment-2113",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
