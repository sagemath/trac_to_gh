# Issue 7362: Make worksheet auto-sync and collaborative editing smarter and more granular

archive/issues_007362.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout @haraldschilly\n\nWe ought to make collaborative worksheet editing somewhat more intuitive, even if we stop short (for now) of implementing full-strength [operational transformations](http://en.wikipedia.org/wiki/Operational_transformation) or employing the [Wave Federation Protocol](http://www.waveprotocol.org/).\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/d46ab54616c03b88/df5e0b2e82af4d5a#df5e0b2e82af4d5a).\n\nFrom [comment:11:ticket:7254 this comment] at #7254:\n\n     The browser and server do not update their `state_number`s if a new cell is added at the end of a sheet, when text cells are added, or cells are deleted. Should we add these to the list, along with the `'delete_all_output'`, `'pretty_print'`, `'system'` worksheet commands? \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7362\n\n",
    "created_at": "2009-10-31T14:43:10Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Make worksheet auto-sync and collaborative editing smarter and more granular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7362",
    "user": "@qed777"
}
```
Assignee: boothby

CC:  @jasongrout @haraldschilly

We ought to make collaborative worksheet editing somewhat more intuitive, even if we stop short (for now) of implementing full-strength [operational transformations](http://en.wikipedia.org/wiki/Operational_transformation) or employing the [Wave Federation Protocol](http://www.waveprotocol.org/).

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/d46ab54616c03b88/df5e0b2e82af4d5a#df5e0b2e82af4d5a).

From [comment:11:ticket:7254 this comment] at #7254:

     The browser and server do not update their `state_number`s if a new cell is added at the end of a sheet, when text cells are added, or cells are deleted. Should we add these to the list, along with the `'delete_all_output'`, `'pretty_print'`, `'system'` worksheet commands? 



Issue created by migration from https://trac.sagemath.org/ticket/7362





---

archive/issue_comments_061689.json:
```json
{
    "body": "See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.",
    "created_at": "2009-11-06T02:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7362#issuecomment-61689",
    "user": "@qed777"
}
```

See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.



---

archive/issue_comments_061690.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.\nThe links:\n\n* [MobWrite](http://code.google.com/p/google-mobwrite/) - [theory](http://code.google.com/p/google-mobwrite/wiki/Theory), [client setup](http://code.google.com/p/google-mobwrite/wiki/WebClient), [server setup](http://code.google.com/p/google-mobwrite/wiki/Daemon), [status](http://code.google.com/p/google-mobwrite/wiki/Status).\n* [Cola](http://wiki.eclipse.org/RT_Shared_Editing) - Real-time shared editing in Eclipse - [screencast](http://www.vimeo.com/1195398).\n\nMobWrite seems to be a good option, provided it doesn't overload client and server.  We can call `mobwrite.share` for new input cells and `mobwrite.unshare` for deleted cells.  *If* MobWrite cannot synchronize arbitrary HTML, perhaps we can `mobwrite.share` a hidden auxiliary cell that holds the escaped HTML of its corresponding output cell.  We can update the output cell's `innerHTML` when MobWrite triggers the auxiliary's `onchange` handler.  Of course, this assumes that we don't run more than one synchronization algorithm at a time.",
    "created_at": "2009-11-11T18:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7362#issuecomment-61690",
    "user": "@qed777"
}
```

Replying to [comment:1 mpatel]:
> See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.
The links:

* [MobWrite](http://code.google.com/p/google-mobwrite/) - [theory](http://code.google.com/p/google-mobwrite/wiki/Theory), [client setup](http://code.google.com/p/google-mobwrite/wiki/WebClient), [server setup](http://code.google.com/p/google-mobwrite/wiki/Daemon), [status](http://code.google.com/p/google-mobwrite/wiki/Status).
* [Cola](http://wiki.eclipse.org/RT_Shared_Editing) - Real-time shared editing in Eclipse - [screencast](http://www.vimeo.com/1195398).

MobWrite seems to be a good option, provided it doesn't overload client and server.  We can call `mobwrite.share` for new input cells and `mobwrite.unshare` for deleted cells.  *If* MobWrite cannot synchronize arbitrary HTML, perhaps we can `mobwrite.share` a hidden auxiliary cell that holds the escaped HTML of its corresponding output cell.  We can update the output cell's `innerHTML` when MobWrite triggers the auxiliary's `onchange` handler.  Of course, this assumes that we don't run more than one synchronization algorithm at a time.



---

archive/issue_comments_061691.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-11-11T18:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7362#issuecomment-61691",
    "user": "@qed777"
}
```

Changing priority from minor to major.



---

archive/issue_comments_061692.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7362#issuecomment-61692",
    "user": "boothby"
}
```

Resolution: invalid



---

archive/issue_comments_061693.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7362#issuecomment-61693",
    "user": "boothby"
}
```

Closing deprecated notebook tickets
