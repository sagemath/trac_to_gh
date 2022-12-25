# Issue 9724: Sage allows creation of variables with empty name

archive/issues_009724.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @haraldschilly\n\nKeywords: variable empty name\n\nSage allows you to create a variable with an empty name.  While this at first appears not to cause any problems, one thing it does break is reset():\n\n```\nsage: var(' ')\n(, )\nsage: whos\nVariable   Type          Data/Info\n----------------------------------\n           Expression    \nsage: reset()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (437, 0))\n\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/all_cmdline.pyc in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/misc/reset.so in sage.misc.reset.reset (sage/misc/reset.c:838)()\n\nIndexError: string index out of range\nsage: del globals()['']\nsage: reset()\n```\nSage also allows the creation of variables with other illegal names (e.g. '1a' or '1'), but for these at least reset() still works.  There are two ways to fix this, the first is to disallow the creation of such variables via var(), but then all illegal cases would have to be taken care of, and it wouldn't help if you created illegal variables manually by inserting them into globals() (but I would argue that if you do this, you're on your own anyway).  The second way to fix the behaviour above would be to make reset() able to delete empty variables too.  This however is only viable if these variables don't break anything else, other than the case mentioned above.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9724\n\n",
    "created_at": "2010-08-11T09:47:33Z",
    "labels": [
        "component: symbolics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage allows creation of variables with empty name",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9724",
    "user": "https://trac.sagemath.org/admin/accounts/users/logix"
}
```
Assignee: @burcin

CC:  @haraldschilly

Keywords: variable empty name

Sage allows you to create a variable with an empty name.  While this at first appears not to cause any problems, one thing it does break is reset():

```
sage: var(' ')
(, )
sage: whos
Variable   Type          Data/Info
----------------------------------
           Expression    
sage: reset()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (437, 0))

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/usr/local/sage/local/lib/python2.6/site-packages/sage/all_cmdline.pyc in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/misc/reset.so in sage.misc.reset.reset (sage/misc/reset.c:838)()

IndexError: string index out of range
sage: del globals()['']
sage: reset()
```
Sage also allows the creation of variables with other illegal names (e.g. '1a' or '1'), but for these at least reset() still works.  There are two ways to fix this, the first is to disallow the creation of such variables via var(), but then all illegal cases would have to be taken care of, and it wouldn't help if you created illegal variables manually by inserting them into globals() (but I would argue that if you do this, you're on your own anyway).  The second way to fix the behaviour above would be to make reset() able to delete empty variables too.  This however is only viable if these variables don't break anything else, other than the case mentioned above.

Issue created by migration from https://trac.sagemath.org/ticket/9724





---

archive/issue_comments_094838.json:
```json
{
    "body": "Perhaps one could add a warning message giving a hint in other cases, too.\n\nFrom `#sage-devel` (IRC):\n\n```\n<cousteau> weird, I can't make the notebook display the same that real LaTeX\n I have a variable which I called {m}:   var('{m}')   In real LaTeX, it nicely displays as an m, but in the notebook it keeps the braces\n same for a variable called \\mu\\Omega\n does the notebook just get the latex() of the variables? or does it do something else?\n var('sui', latex_name=\"s_{u,i}\")   :'( I shoild read the manual first\n```",
    "created_at": "2010-08-16T22:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94838",
    "user": "https://github.com/nexttime"
}
```

Perhaps one could add a warning message giving a hint in other cases, too.

From `#sage-devel` (IRC):

```
<cousteau> weird, I can't make the notebook display the same that real LaTeX
 I have a variable which I called {m}:   var('{m}')   In real LaTeX, it nicely displays as an m, but in the notebook it keeps the braces
 same for a variable called \mu\Omega
 does the notebook just get the latex() of the variables? or does it do something else?
 var('sui', latex_name="s_{u,i}")   :'( I shoild read the manual first
```



---

archive/issue_events_024333.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2011-06-18T05:17:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9724#event-24333"
}
```



---

archive/issue_comments_094839.json:
```json
{
    "body": "Fixed in the patch on #7496:\n\n```\nsage: var(' ')\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.7.1.alpha2/devel/sage-main/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/calculus/var.so in sage.calculus.var.var (sage/calculus/var.c:687)()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6276)()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6048)()\n\nValueError: The name \"\" is not a valid Python identifier.\n```",
    "created_at": "2011-06-18T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94839",
    "user": "https://github.com/vbraun"
}
```

Fixed in the patch on #7496:

```
sage: var(' ')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.7.1.alpha2/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/calculus/var.so in sage.calculus.var.var (sage/calculus/var.c:687)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6276)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6048)()

ValueError: The name "" is not a valid Python identifier.
```



---

archive/issue_comments_094840.json:
```json
{
    "body": "Changing keywords from \"variable empty name\" to \"sd31\".",
    "created_at": "2011-06-18T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94840",
    "user": "https://github.com/vbraun"
}
```

Changing keywords from "variable empty name" to "sd31".



---

archive/issue_comments_094841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-18T05:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94841",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094842.json:
```json
{
    "body": "Apparently this means this should be closed.  Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)\n\nI'm assuming that Mariah's comment on #7496 means she checked this out, so I'm putting her and Volker as reviewers for closing this.",
    "created_at": "2011-06-24T00:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94842",
    "user": "https://github.com/kcrisman"
}
```

Apparently this means this should be closed.  Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)

I'm assuming that Mariah's comment on #7496 means she checked this out, so I'm putting her and Volker as reviewers for closing this.



---

archive/issue_comments_094843.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-24T00:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94843",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094844.json:
```json
{
    "body": "It does work.  This is not mentioned in the patch for #7496, though, so I'm adding a doctest there.",
    "created_at": "2011-06-24T03:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94844",
    "user": "https://github.com/kcrisman"
}
```

It does work.  This is not mentioned in the patch for #7496, though, so I'm adding a doctest there.



---

archive/issue_events_024334.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-24T15:03:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9724#event-24334"
}
```



---

archive/issue_comments_094845.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)\n\nNo, it is easier if you change the milestone to \"sage-duplicate/invalid/wontfix\" and set to \"positive_review\".  This gives me the best overview on [http://trac.sagemath.org/sage_trac/report/40](http://trac.sagemath.org/sage_trac/report/40).  I will then close the ticket.",
    "created_at": "2011-06-24T15:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94845",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:3 kcrisman]:
> Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)

No, it is easier if you change the milestone to "sage-duplicate/invalid/wontfix" and set to "positive_review".  This gives me the best overview on [http://trac.sagemath.org/sage_trac/report/40](http://trac.sagemath.org/sage_trac/report/40).  I will then close the ticket.



---

archive/issue_comments_094846.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-06-24T15:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9724#issuecomment-94846",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
