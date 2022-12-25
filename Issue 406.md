# Issue 406: notebook -- improve support for other system modes

archive/issues_000406.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nOn 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:\n> Some other minor issues about using GAP within the notebook, under\n> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at\n> the top.  The following things don't work correctly:\n> \n> 0) If I type something that gives an error in GAP, the error\n> message is buried in a python exception/backtrace.\n> \n> 1) If I type \"?SymmetricGroup\" (which works within GAP), all I see\n> is\n> \n>    Help: Showing `Reference: SymmetricGroup'\n>    Page from 104\n> \n> It's similar with other \"?foo\" commands.\n> \n> 2) If I type \"SymmetricGroup?\" and hit tab, it shows me help about\n> sage's wrapped SymmetricGroup function.  I don't think this will\n> be helpful for functions not wrapped by sage.\n> \n> 3) When I try to use tab completion, it inserts \"gap.\" before the\n> command (and probably ignores functions not wrapper by sage).\n\nI am aware of each of these issues (which also happen with\nthe other interfaces).  They are *not* features in my mind, but\nbugs, and they need to be fixed by somebody (either me or\nsomebody else). \n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/406\n\n",
    "created_at": "2007-07-27T03:01:47Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- improve support for other system modes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/406",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
> 
> 3) When I try to use tab completion, it inserts "gap." before the
> command (and probably ignores functions not wrapper by sage).

I am aware of each of these issues (which also happen with
the other interfaces).  They are *not* features in my mind, but
bugs, and they need to be fixed by somebody (either me or
somebody else). 

William
```


Issue created by migration from https://trac.sagemath.org/ticket/406





---

archive/issue_comments_001985.json:
```json
{
    "body": "4) If I use GAP Print(...) commands in a short notebook entry, I see the output.  But if the entry is longer, I don't see the output.",
    "created_at": "2007-07-27T16:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1985",
    "user": "https://github.com/jdchristensen"
}
```

4) If I use GAP Print(...) commands in a short notebook entry, I see the output.  But if the entry is longer, I don't see the output.



---

archive/issue_comments_001986.json:
```json
{
    "body": "In order to focus this ticket, I've broken up each issue into separate\ntickets and made this ticket just issue 3 in the original description, which is below\n\n```\nOn 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:\n> Some other minor issues about using GAP within the notebook, under\n> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at\n> the top.  The following things don't work correctly:\n> \n> 0) If I type something that gives an error in GAP, the error\n> message is buried in a python exception/backtrace.\n> \n> 1) If I type \"?SymmetricGroup\" (which works within GAP), all I see\n> is\n> \n>    Help: Showing `Reference: SymmetricGroup'\n>    Page from 104\n> \n> It's similar with other \"?foo\" commands.\n> \n> 2) If I type \"SymmetricGroup?\" and hit tab, it shows me help about\n> sage's wrapped SymmetricGroup function.  I don't think this will\n> be helpful for functions not wrapped by sage.\n> \n> 3) When I try to use tab completion, it inserts \"gap.\" before the\n> command (and probably ignores functions not wrapper by sage).\n\nI am aware of each of these issues (which also happen with\nthe other interfaces).  They are *not* features in my mind, but\nbugs, and they need to be fixed by somebody (either me or\nsomebody else). \n\nWilliam\n```\n",
    "created_at": "2008-05-10T21:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1986",
    "user": "https://github.com/williamstein"
}
```

In order to focus this ticket, I've broken up each issue into separate
tickets and made this ticket just issue 3 in the original description, which is below

```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
> 
> 3) When I try to use tab completion, it inserts "gap." before the
> command (and probably ignores functions not wrapper by sage).

I am aware of each of these issues (which also happen with
the other interfaces).  They are *not* features in my mind, but
bugs, and they need to be fixed by somebody (either me or
somebody else). 

William
```




---

archive/issue_comments_001987.json:
```json
{
    "body": "Attachment [sage-406.patch](tarball://root/attachments/some-uuid/ticket406/sage-406.patch) by @williamstein created at 2008-05-10 22:13:07",
    "created_at": "2008-05-10T22:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1987",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-406.patch](tarball://root/attachments/some-uuid/ticket406/sage-406.patch) by @williamstein created at 2008-05-10 22:13:07



---

archive/issue_comments_001988.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-10T22:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1988",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_events_000974.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-05-10T22:13:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/406#event-974"
}
```



---

archive/issue_comments_001989.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-05-10T22:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1989",
    "user": "https://github.com/williamstein"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_001990.json:
```json
{
    "body": "Trac #406:\n\n1. Fix the problem where hitting tab when switched into another worksheet\n   mode sticks system. at the front of each completion.  Similar fixes \n   for help via foo([tab key}] and source code via foo??[tab]. \n\n2. When switching systems, get rid of the very annoying \n   confirmation dialog.   (Just commented it out for now.)\n\n3. Fix *very serious* bug that prevented loading a worksheet that was set\n   to an optional mode.   In sage-3.0.1 loading a worksheet that is in\n   an optional mode (e.g., mathematica or maple or Magma, say) was\n   completely broken.  This patch fixes that problem. \n\nNOTE: This patch has no new tests illustrating that ift fixes\nanything, since we have no automated way of testing any of the\nabove right now.",
    "created_at": "2008-05-10T22:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1990",
    "user": "https://github.com/williamstein"
}
```

Trac #406:

1. Fix the problem where hitting tab when switched into another worksheet
   mode sticks system. at the front of each completion.  Similar fixes 
   for help via foo([tab key}] and source code via foo??[tab]. 

2. When switching systems, get rid of the very annoying 
   confirmation dialog.   (Just commented it out for now.)

3. Fix *very serious* bug that prevented loading a worksheet that was set
   to an optional mode.   In sage-3.0.1 loading a worksheet that is in
   an optional mode (e.g., mathematica or maple or Magma, say) was
   completely broken.  This patch fixes that problem. 

NOTE: This patch has no new tests illustrating that ift fixes
anything, since we have no automated way of testing any of the
above right now.



---

archive/issue_comments_001991.json:
```json
{
    "body": "Patch works for me -- I have only tested that tab completion for magma is now useful.\nIn terms of refereeing the patch, I only understood the x[len(prepend):] bit and that seems plausible to me.",
    "created_at": "2008-05-11T00:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1991",
    "user": "https://github.com/nbruin"
}
```

Patch works for me -- I have only tested that tab completion for magma is now useful.
In terms of refereeing the patch, I only understood the x[len(prepend):] bit and that seems plausible to me.



---

archive/issue_comments_001992.json:
```json
{
    "body": "This seems to fix the problem (part 3, that is, the others are #3152).  I tested it in R mode, latex mode, gap mode, and python mode.  All of these saved/reloaded OK, and were robust under switching between modes.  Command completion appears fixed in R and gap (btw it would be pretty cool to have latex command completion but I assume that would be a pain).  \nSince this is a second opinion I think it is time to give a full positive review and start merging it in.",
    "created_at": "2008-05-12T09:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1992",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This seems to fix the problem (part 3, that is, the others are #3152).  I tested it in R mode, latex mode, gap mode, and python mode.  All of these saved/reloaded OK, and were robust under switching between modes.  Command completion appears fixed in R and gap (btw it would be pretty cool to have latex command completion but I assume that would be a pain).  
Since this is a second opinion I think it is time to give a full positive review and start merging it in.



---

archive/issue_events_000975.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-12T10:59:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/406#event-975"
}
```



---

archive/issue_comments_001993.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T10:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1993",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_001994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T10:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/406#issuecomment-1994",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
