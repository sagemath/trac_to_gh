# Issue 3007: gap.Factorization? is useless

archive/issues_003007.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee this thread.  The solution suggested by Steve Linton below does *not* work exactly as suggested.\n\n```\n\n\nForwarded conversation\nSubject: [sage-support] Documentation with several entries\n------------------------\n\nFrom: Hector Villafuerte <hectorvd@gmail.com>\nDate: Tue, Apr 22, 2008 at 5:12 PM\nTo: sage-support@googlegroups.com\n\n\n\nHi,\nwhile trying this:\nsage: gap.Factorization?\n\nI got this...\n\nType:        <class 'sage.interfaces.gap.GapFunction'>\nDefinition:  gap.Factorization( [noargspec] )\nDocstring:\nHelp: several entries match this topic - type ?2 to get match [2]\n\n[1] Reference: factorization\n[2] Reference: Factorization\n\n\nWhich I can't get to work in either the Notebook or the command line. Any ideas?\nThanks!\n--\n Hector\n\n--~--~---------~--~----~------------~-------~--~----~\nTo post to this group, send email to sage-support@googlegroups.com\nTo unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com\nFor more options, visit this group at http://groups.google.com/group/sage-support\nURLs: http://www.sagemath.org\n-~----------~----~----~----~------~----~------~--~---\n\n----------\nFrom: William Stein <wstein@gmail.com>\nDate: Wed, Apr 23, 2008 at 7:42 AM\nTo: Steve Linton <sal@cs.st-and.ac.uk>\n\n\nAny thoughts about how to disambiguate this sort of thing in the context\nof Sage?  Of course, you can just plead that you work on the gap interface\nalmost 2.5 years ago and remember nothing :-)\n--\nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org\n----------\nFrom: Steve Linton <sal@cs.st-and.ac.uk>\nDate: Wed, Apr 23, 2008 at 8:34 AM\nTo: William Stein <wstein@gmail.com>\n\n\ngap.2? might just work.\n\nYou simply need to send GAP ?2 or HELP(\"2\");\n\nThe message is being generated from HELP_SHOW_MATCHES in lib/helpbase.gi (line\n713). I dare say we could move that message to a global variable so that you\ncould change it to  \"type gap.2? ....\" in a future release.\n\n       Steve\n--\nSteve Linton    School of Computer Science  &\n     Centre for Interdisciplinary Research in Computational Algebra\n            University of St Andrews    Tel   +44 (1334) 463269\nhttp://www.cs.st-and.ac.uk/~sal          Fax   +44 (1334) 463278\nThe University is a charity registered in Scotland : No SC013532\n\n\n\n-- \nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3007\n\n",
    "closed_at": "2013-03-29T18:55:55Z",
    "created_at": "2008-04-23T17:09:20Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gap.Factorization? is useless",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3007",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

See this thread.  The solution suggested by Steve Linton below does *not* work exactly as suggested.

```


Forwarded conversation
Subject: [sage-support] Documentation with several entries
------------------------

From: Hector Villafuerte <hectorvd@gmail.com>
Date: Tue, Apr 22, 2008 at 5:12 PM
To: sage-support@googlegroups.com



Hi,
while trying this:
sage: gap.Factorization?

I got this...

Type:        <class 'sage.interfaces.gap.GapFunction'>
Definition:  gap.Factorization( [noargspec] )
Docstring:
Help: several entries match this topic - type ?2 to get match [2]

[1] Reference: factorization
[2] Reference: Factorization


Which I can't get to work in either the Notebook or the command line. Any ideas?
Thanks!
--
 Hector

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support@googlegroups.com
To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URLs: http://www.sagemath.org
-~----------~----~----~----~------~----~------~--~---

----------
From: William Stein <wstein@gmail.com>
Date: Wed, Apr 23, 2008 at 7:42 AM
To: Steve Linton <sal@cs.st-and.ac.uk>


Any thoughts about how to disambiguate this sort of thing in the context
of Sage?  Of course, you can just plead that you work on the gap interface
almost 2.5 years ago and remember nothing :-)
--
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
----------
From: Steve Linton <sal@cs.st-and.ac.uk>
Date: Wed, Apr 23, 2008 at 8:34 AM
To: William Stein <wstein@gmail.com>


gap.2? might just work.

You simply need to send GAP ?2 or HELP("2");

The message is being generated from HELP_SHOW_MATCHES in lib/helpbase.gi (line
713). I dare say we could move that message to a global variable so that you
could change it to  "type gap.2? ...." in a future release.

       Steve
--
Steve Linton    School of Computer Science  &
     Centre for Interdisciplinary Research in Computational Algebra
            University of St Andrews    Tel   +44 (1334) 463269
http://www.cs.st-and.ac.uk/~sal          Fax   +44 (1334) 463278
The University is a charity registered in Scotland : No SC013532



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org 
```

Issue created by migration from https://trac.sagemath.org/ticket/3007





---

archive/issue_comments_020635.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20635",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020636.json:
```json
{
    "body": "The following works except that it's not properly offset, i.e. you have to hit space a few times before you find the documentation for `Factorization`.\n\n```\nsage: gap.Factorization?\nType:\t\tGapFunction\nBase Class:\t<class 'sage.interfaces.gap.GapFunction'>\nString Form:\tFactorization\nNamespace:\tInteractive\nLoaded File:\t/Users/gvol/SageStuff/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/interfaces/gap.py\nSource File:\t/Users/gvol/SageStuff/sage-5.0.rc0/devel/sage/sage/interfaces/gap.py\nDefinition:\tgap.Factorization(self, *args, **kwds)\nDocstring:\n    Help: several entries match this topic - type ?2 to get match [2]\n    \n    [1] Reference: factorization\n    [2] Reference: Factorization\n\nCall def:\tgap.Factorization(self, *args, **kwds)\n\nCall docstring:\n    x.__init__(...) initializes x; see help(type(x)) for signature\n\n\nsage: gap.\"2\"?\n...the real documentation...\n```",
    "created_at": "2012-06-05T18:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20636",
    "user": "https://github.com/gvol"
}
```

The following works except that it's not properly offset, i.e. you have to hit space a few times before you find the documentation for `Factorization`.

```
sage: gap.Factorization?
Type:		GapFunction
Base Class:	<class 'sage.interfaces.gap.GapFunction'>
String Form:	Factorization
Namespace:	Interactive
Loaded File:	/Users/gvol/SageStuff/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/interfaces/gap.py
Source File:	/Users/gvol/SageStuff/sage-5.0.rc0/devel/sage/sage/interfaces/gap.py
Definition:	gap.Factorization(self, *args, **kwds)
Docstring:
    Help: several entries match this topic - type ?2 to get match [2]
    
    [1] Reference: factorization
    [2] Reference: Factorization

Call def:	gap.Factorization(self, *args, **kwds)

Call docstring:
    x.__init__(...) initializes x; see help(type(x)) for signature


sage: gap."2"?
...the real documentation...
```



---

archive/issue_events_006835.json:
```json
{
    "actor": "https://github.com/gvol",
    "created_at": "2013-03-10T22:24:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3007#event-6835"
}
```



---

archive/issue_comments_020637.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-10T22:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20637",
    "user": "https://github.com/gvol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020638.json:
```json
{
    "body": "This has been fixed in 5.7.",
    "created_at": "2013-03-10T22:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20638",
    "user": "https://github.com/gvol"
}
```

This has been fixed in 5.7.



---

archive/issue_comments_020639.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-20T23:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20639",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006836.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-29T18:55:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3007#event-6836"
}
```



---

archive/issue_comments_020640.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T18:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3007#issuecomment-20640",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
