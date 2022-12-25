# Issue 4647: Disable dependency code cacheing in setup.py

archive/issues_004647.json:
```json
{
    "body": "Assignee: mabshoff\n\nUnless we do the following -upgrade will likely break for a ton of people:\n\n```\n[3:57pm] craigcitro: wstein: so i'm only here for 3 seconds between xmas decorating, but i had a thought\n[3:57pm] craigcitro: the dependency checking code in setup.py seems to be causing a lot of heartache\n[3:57pm] craigcitro: so why don't we just not cache it? it still only takes like .6 seconds to build the whole dependency tree\n[3:58pm] mabshoff: +1\n[3:58pm] craigcitro: and if it build fresh every time, we'll avoid a ton of these issues\n[3:58pm] craigcitro: and then when i have time to sit down and debug a bunch of these crazy situations, we can add it back in\n[3:58pm] craigcitro: just comment out all the lines about pickle/unpickle/etc in setup.py\n[4:00pm] ghtdak1 left the chat room. (Remote closed the connection)\n[4:00pm] craigcitro: mabshoff: do you want to make a patch that does that for rc0?\n[4:00pm] craigcitro: and see how it works out?\n[4:00pm] craigcitro: i have to run right now -- getting the tree out of the car and putting up xmas lights. \n[4:00pm] mabshoff: I will put it on my list, but no promises.\n```\nOne problem I see is that currently deleting the Cython cache triggers a full rebuild, so that need to be considered. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4647\n\n",
    "created_at": "2008-11-29T00:04:28Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Disable dependency code cacheing in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Unless we do the following -upgrade will likely break for a ton of people:

```
[3:57pm] craigcitro: wstein: so i'm only here for 3 seconds between xmas decorating, but i had a thought
[3:57pm] craigcitro: the dependency checking code in setup.py seems to be causing a lot of heartache
[3:57pm] craigcitro: so why don't we just not cache it? it still only takes like .6 seconds to build the whole dependency tree
[3:58pm] mabshoff: +1
[3:58pm] craigcitro: and if it build fresh every time, we'll avoid a ton of these issues
[3:58pm] craigcitro: and then when i have time to sit down and debug a bunch of these crazy situations, we can add it back in
[3:58pm] craigcitro: just comment out all the lines about pickle/unpickle/etc in setup.py
[4:00pm] ghtdak1 left the chat room. (Remote closed the connection)
[4:00pm] craigcitro: mabshoff: do you want to make a patch that does that for rc0?
[4:00pm] craigcitro: and see how it works out?
[4:00pm] craigcitro: i have to run right now -- getting the tree out of the car and putting up xmas lights. 
[4:00pm] mabshoff: I will put it on my list, but no promises.
```
One problem I see is that currently deleting the Cython cache triggers a full rebuild, so that need to be considered. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4647





---

archive/issue_comments_034913.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_034914.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-29T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034915.json:
```json
{
    "body": "Attachment [trac_4645_4647.patch](tarball://root/attachments/some-uuid/ticket4647/trac_4645_4647.patch) by mabshoff created at 2008-11-29 06:29:04\n\nThis patch covers #4645 as well as this ticket #4647. I did the minimally invasive version to make reenabling the caching code as simple as possible.\n\nOnce this patch is applied it survives:\n\n* a sage -b after deleting the Cython cache file\n* a sage -ba\n* a sage -b after applying the patch from #4206 - which caused us to disabled the caching for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4645_4647.patch](tarball://root/attachments/some-uuid/ticket4647/trac_4645_4647.patch) by mabshoff created at 2008-11-29 06:29:04

This patch covers #4645 as well as this ticket #4647. I did the minimally invasive version to make reenabling the caching code as simple as possible.

Once this patch is applied it survives:

* a sage -b after deleting the Cython cache file
* a sage -ba
* a sage -b after applying the patch from #4206 - which caused us to disabled the caching for now.

Cheers,

Michael



---

archive/issue_comments_034916.json:
```json
{
    "body": "Two more data points:\n\n* disabling the caching adds a little less than a second to each \"sage -b\" run\n* reverting #4206 and then running sage -b again leads to a working Sage\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Two more data points:

* disabling the caching adds a little less than a second to each "sage -b" run
* reverting #4206 and then running sage -b again leads to a working Sage

Cheers,

Michael



---

archive/issue_comments_034917.json:
```json
{
    "body": "This looks good. I've added a second patch which cuts out one or two more lines (it was actually raising and catching an exception every time, which didn't need to happen), and adds comments pointing to this trac ticket, and trac #4651, which is the request to add caching back in. I also deleted a few leftover debugging print statements that were commented out, since they're no longer necessary.",
    "created_at": "2008-11-29T07:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34917",
    "user": "https://github.com/craigcitro"
}
```

This looks good. I've added a second patch which cuts out one or two more lines (it was actually raising and catching an exception every time, which didn't need to happen), and adds comments pointing to this trac ticket, and trac #4651, which is the request to add caching back in. I also deleted a few leftover debugging print statements that were commented out, since they're no longer necessary.



---

archive/issue_comments_034918.json:
```json
{
    "body": "Positive review for the second patch. I left the exception structure in there since someone has to put them back in anyway, but I can live with the changes as is.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T07:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review for the second patch. I left the exception structure in there since someone has to put them back in anyway, but I can live with the changes as is.

Cheers,

Michael



---

archive/issue_comments_034919.json:
```json
{
    "body": "Attachment [trac-4647-pt2.patch](tarball://root/attachments/some-uuid/ticket4647/trac-4647-pt2.patch) by @craigcitro created at 2008-11-29 07:41:15",
    "created_at": "2008-11-29T07:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34919",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4647-pt2.patch](tarball://root/attachments/some-uuid/ticket4647/trac-4647-pt2.patch) by @craigcitro created at 2008-11-29 07:41:15



---

archive/issue_comments_034920.json:
```json
{
    "body": "New patch, rebased against mabshoff's current `setup.py`. Applies fine to the copy I got from `/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage-main` on sage.math.",
    "created_at": "2008-11-29T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34920",
    "user": "https://github.com/craigcitro"
}
```

New patch, rebased against mabshoff's current `setup.py`. Applies fine to the copy I got from `/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage-main` on sage.math.



---

archive/issue_comments_034921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T07:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034922.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-29T07:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4647#issuecomment-34922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_events_010609.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-29T07:48:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4647",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4647#event-10609"
}
```
