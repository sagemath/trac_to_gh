# Issue 2313: old spkg's -- delete to save space

archive/issues_002313.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n\n\nOn Mon, Feb 25, 2008 at 9:40 PM, Jonathan Bober <jwbober@gmail.com> wrote:\n> \n>  An old sage directory that I have that's been upgraded only a few times\n>  has an spkg directory that's got more than 850 megs. This was only\n>  upgraded from 2.8.15.alpha1 to 2.10.1, so I imagine that this directory\n>  can get even larger. With the exception of the 'installed' directory,\n>  can everything else be safely deleted?\n\nNo.\n\n>  (Actually, the same question stands for a new sage install, in which the\n>  spkg directory holds abound 200 megs. Is there a reason that already\n>  installed spkg's should be kept around?)\n\nIf you delete spkg/standard then the dependency system will get completely confused\nand rebuild all of Sage from scratch.\n\nIf you use the following script you can shrink all the files to be empty, and everything\nwill work fine:\n\nlogin@sage:~$ more /usr/local/bin/shrink \n#!/usr/bin/env python\n\nimport os\n\nfor F in os.listdir('.'):\n    print F\n    if F.endswith('.spkg'):\n       open(F,'w').close()\n\n---\n\nThe main issue is that the build system was written when there were\n3 Sage users in the whole world, and issues like this weren't our\ntop priority.   Nobody ever got around to dealing with this.  I'm not\ngoing to immediately suggest the right fix, since there are several options\nand I'd rather people discuss them. \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2313\n\n",
    "created_at": "2008-02-26T06:18:18Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "old spkg's -- delete to save space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2313",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff


```


On Mon, Feb 25, 2008 at 9:40 PM, Jonathan Bober <jwbober@gmail.com> wrote:
> 
>  An old sage directory that I have that's been upgraded only a few times
>  has an spkg directory that's got more than 850 megs. This was only
>  upgraded from 2.8.15.alpha1 to 2.10.1, so I imagine that this directory
>  can get even larger. With the exception of the 'installed' directory,
>  can everything else be safely deleted?

No.

>  (Actually, the same question stands for a new sage install, in which the
>  spkg directory holds abound 200 megs. Is there a reason that already
>  installed spkg's should be kept around?)

If you delete spkg/standard then the dependency system will get completely confused
and rebuild all of Sage from scratch.

If you use the following script you can shrink all the files to be empty, and everything
will work fine:

login@sage:~$ more /usr/local/bin/shrink 
#!/usr/bin/env python

import os

for F in os.listdir('.'):
    print F
    if F.endswith('.spkg'):
       open(F,'w').close()

---

The main issue is that the build system was written when there were
3 Sage users in the whole world, and issues like this weren't our
top priority.   Nobody ever got around to dealing with this.  I'm not
going to immediately suggest the right fix, since there are several options
and I'd rather people discuss them. 

```


Issue created by migration from https://trac.sagemath.org/ticket/2313





---

archive/issue_comments_015355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-02T02:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2313#issuecomment-15355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002489.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-02T02:21:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2313",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2313#event-2489"
}
```



---

archive/issue_comments_015356.json:
```json
{
    "body": "Now that #463 is merged this ticket can be closed since -upgrade will delete any older and no longer used spkgs.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T02:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2313#issuecomment-15356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Now that #463 is merged this ticket can be closed since -upgrade will delete any older and no longer used spkgs.

Cheers,

Michael
