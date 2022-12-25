# Issue 5341: jsmath broken on wiki

archive/issues_005341.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  wstein\n\nApache thinks that the static pages for the wiki should still be handled by moinmoin. E.g.,\n\nhttp://wiki.sagemath.org/moin_static171/jsmath/jsMath.js\n\nThe help pages say that an `Alias` directive should be placed in the config before `ScriptAlias`:\n\nhttp://moinmo.in/HelpOnInstalling/ApacheOnLinux#Configure_Apache\n\n\n\n```\n<mabs|4666> Yep, make it an issue for all wikis.\n<mabs|4666> or at least mpir, l-functions and sage\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5341\n\n",
    "created_at": "2009-02-22T20:41:16Z",
    "labels": [
        "component: website/wiki",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "jsmath broken on wiki",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5341",
    "user": "https://github.com/burcin"
}
```
Assignee: boothby

CC:  wstein

Apache thinks that the static pages for the wiki should still be handled by moinmoin. E.g.,

http://wiki.sagemath.org/moin_static171/jsmath/jsMath.js

The help pages say that an `Alias` directive should be placed in the config before `ScriptAlias`:

http://moinmo.in/HelpOnInstalling/ApacheOnLinux#Configure_Apache



```
<mabs|4666> Yep, make it an issue for all wikis.
<mabs|4666> or at least mpir, l-functions and sage
```




Issue created by migration from https://trac.sagemath.org/ticket/5341





---

archive/issue_comments_041066.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041067.json:
```json
{
    "body": "This is due to a bad simlink:\n`jsmath -> ../../../../data/extcode/notebook/javascript/jsmath/`\nin\n`$SAGE_LOCAL/share/moin/htdocs`\n\nChanging this in `spkg-install` to\n`jsmath -> ../../../../data/extcode/javascript/jsmath/`\nfixes the problem.\n\nThe updated spkg can be found at #3693.",
    "created_at": "2009-03-07T03:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41067",
    "user": "https://github.com/rlmill"
}
```

This is due to a bad simlink:
`jsmath -> ../../../../data/extcode/notebook/javascript/jsmath/`
in
`$SAGE_LOCAL/share/moin/htdocs`

Changing this in `spkg-install` to
`jsmath -> ../../../../data/extcode/javascript/jsmath/`
fixes the problem.

The updated spkg can be found at #3693.



---

archive/issue_comments_041068.json:
```json
{
    "body": "In order to fix this issue for existing wiki's, you'll also need to change `moin_static171` to `moin_static172` in\n\n`data/plugin/parser/jsmath.py`\n\nwithin the sage_wiki directory, after upgrading the spkg.",
    "created_at": "2009-03-07T03:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41068",
    "user": "https://github.com/rlmill"
}
```

In order to fix this issue for existing wiki's, you'll also need to change `moin_static171` to `moin_static172` in

`data/plugin/parser/jsmath.py`

within the sage_wiki directory, after upgrading the spkg.



---

archive/issue_comments_041069.json:
```json
{
    "body": "jsmath is loaded for the sage wiki now. However, the version of jsmath on the wiki is v3.3d, while Sage 4.0.1 comes with v3.6b. This seems to be the latest version available on the jsMath web site as well.\n\nIt would be great if the version of the jsMath on the wiki as well as the plugin, etc. configuration matched that of the main Sage distribution.",
    "created_at": "2009-06-13T17:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41069",
    "user": "https://github.com/burcin"
}
```

jsmath is loaded for the sage wiki now. However, the version of jsmath on the wiki is v3.3d, while Sage 4.0.1 comes with v3.6b. This seems to be the latest version available on the jsMath web site as well.

It would be great if the version of the jsMath on the wiki as well as the plugin, etc. configuration matched that of the main Sage distribution.



---

archive/issue_comments_041070.json:
```json
{
    "body": "I've upgraded the jsmath install and restarted the wiki.  Note that the wiki is running from sage-3.3, since the latest version of sage has an *ANCIENT* version of moinmoin installed into it.\n\nPlease check and verify that the new jsmath is working, then close this ticket.",
    "created_at": "2009-06-14T11:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41070",
    "user": "https://github.com/williamstein"
}
```

I've upgraded the jsmath install and restarted the wiki.  Note that the wiki is running from sage-3.3, since the latest version of sage has an *ANCIENT* version of moinmoin installed into it.

Please check and verify that the new jsmath is working, then close this ticket.



---

archive/issue_comments_041071.json:
```json
{
    "body": "The jsmath version on the wiki is still v3.3d, not v3.6b, so I don't see any change after the jsmath ugrade.\n\nSince the jsmath on the wiki is working atm, this ticket can be closed. The old version doesn't matter so much.\n\nIt would be nice if the wiki allowed previewing math input, but that should be a separate ticket.\n\nI don't have the right to close tickets on trac, feel free to close this.",
    "created_at": "2009-06-15T10:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41071",
    "user": "https://github.com/burcin"
}
```

The jsmath version on the wiki is still v3.3d, not v3.6b, so I don't see any change after the jsmath ugrade.

Since the jsmath on the wiki is working atm, this ticket can be closed. The old version doesn't matter so much.

It would be nice if the wiki allowed previewing math input, but that should be a separate ticket.

I don't have the right to close tickets on trac, feel free to close this.



---

archive/issue_events_005598.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-06-15T13:36:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5341#event-5598"
}
```



---

archive/issue_comments_041072.json:
```json
{
    "body": "> I don't have the right to close tickets on trac, feel free to close this. \n\nDo you think it is a good/bad thing that suddenly most users do not have the ability to change the status of tickets?  This was a change mabshoff made a few weeks ago without discussion.",
    "created_at": "2009-06-15T13:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41072",
    "user": "https://github.com/williamstein"
}
```

> I don't have the right to close tickets on trac, feel free to close this. 

Do you think it is a good/bad thing that suddenly most users do not have the ability to change the status of tickets?  This was a change mabshoff made a few weeks ago without discussion.



---

archive/issue_comments_041073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T13:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5341#issuecomment-41073",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
