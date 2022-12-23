# Issue 407: improve how gap workspace caching works

archive/issues_000407.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:\n> \n> \"David Joyner\" <wdjoyner@gmail.com> writes:\n> \n> > Could you please try gap_reset_workspace() and then restart SAGE\n> > and see if the examples start?\n> \n> That fixed it!  Thanks.  Not sure what I did.  The problem occurred on\n> two different systems, which my home directory is mirrored between.\n> If it happens again, I'll report any additional info I can think of.\n\nVery interesting.  When you install the gap database, SAGE runs\ngap_reset_workspace() to update the cached workspace on the machine\non which the database is installed.  Because a single home directory could\nbe used by multiple machines, there are potentially multiple gap workspace\ncache files, and for you only one was updated.   \n\nThis is an annoying design (due to me), since multiple users of a single\nSAGE install will all have to type gap_reset_workspace() to get the new gap\nlibraries (when one installs, e.g., the small group database). \n\nI should change the implementation so when installing database_gap (or\nanything else that might invalidate the stored gap workspace, or more precisely\nmake it not optimal), then *all* gap workspace cache files from all users of\nthat SAGE install become invalid.  They would then be regenerated (which takes\nonly a few seconds) the next time any user starts GAP from a SAGE session.\nI could do this by assigning a sequence number, e.g., in a file like \nlocal/lib/gap-sequence-number, which is incremented any time gap is updated\nin some way.  Then I could make the cached workspace (or another file\nwith a similar name next to the gap workspace file) also store this \nsequence number (the cached workspaces are in ~/.sage/gap/).  \nThen whenever a gap interpreter is first started in interface/gap.py, \nthis sequence number is checked, and if it doesn't match, then the gap workspace\nis regenerated.  This should completely eliminate all future gap_reset_workspace\nsynchronization errors. \n\nI'll wait to see if anybody thinks the above idea is stupid, and if not,\nI'll implement it (which shouldn't take long). \n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/407\n\n",
    "created_at": "2007-07-27T03:16:33Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "improve how gap workspace caching works",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/407",
    "user": "was"
}
```
Assignee: was


```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> 
> "David Joyner" <wdjoyner@gmail.com> writes:
> 
> > Could you please try gap_reset_workspace() and then restart SAGE
> > and see if the examples start?
> 
> That fixed it!  Thanks.  Not sure what I did.  The problem occurred on
> two different systems, which my home directory is mirrored between.
> If it happens again, I'll report any additional info I can think of.

Very interesting.  When you install the gap database, SAGE runs
gap_reset_workspace() to update the cached workspace on the machine
on which the database is installed.  Because a single home directory could
be used by multiple machines, there are potentially multiple gap workspace
cache files, and for you only one was updated.   

This is an annoying design (due to me), since multiple users of a single
SAGE install will all have to type gap_reset_workspace() to get the new gap
libraries (when one installs, e.g., the small group database). 

I should change the implementation so when installing database_gap (or
anything else that might invalidate the stored gap workspace, or more precisely
make it not optimal), then *all* gap workspace cache files from all users of
that SAGE install become invalid.  They would then be regenerated (which takes
only a few seconds) the next time any user starts GAP from a SAGE session.
I could do this by assigning a sequence number, e.g., in a file like 
local/lib/gap-sequence-number, which is incremented any time gap is updated
in some way.  Then I could make the cached workspace (or another file
with a similar name next to the gap workspace file) also store this 
sequence number (the cached workspaces are in ~/.sage/gap/).  
Then whenever a gap interpreter is first started in interface/gap.py, 
this sequence number is checked, and if it doesn't match, then the gap workspace
is regenerated.  This should completely eliminate all future gap_reset_workspace
synchronization errors. 

I'll wait to see if anybody thinks the above idea is stupid, and if not,
I'll implement it (which shouldn't take long). 

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/407





---

archive/issue_comments_002004.json:
```json
{
    "body": "Looks like a duplicate of #527.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T02:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/407#issuecomment-2004",
    "user": "mabshoff"
}
```

Looks like a duplicate of #527.

Cheers,

Michael



---

archive/issue_comments_002005.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-06T23:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/407#issuecomment-2005",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002006.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-11-03T14:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/407#issuecomment-2006",
    "user": "was"
}
```

Resolution: duplicate
