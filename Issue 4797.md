# Issue 4797: upgrade -- if upgrading Cython run -ba instead of -b

archive/issues_004797.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb\n\nWhen upgrading Cython like at #4639 we should really run a -ba on upgrade and not just a -b since the new Cython version in this case does fix some fundamental issues the way exceptions are handled. In general I would be sleep much better if we do this in general since many potentially odd Heisenbugs that disappear after either a partial -b or a -ba would be avoided that way.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4797\n\n",
    "created_at": "2008-12-14T14:44:14Z",
    "labels": [
        "component: packages",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "upgrade -- if upgrading Cython run -ba instead of -b",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @robertwb

When upgrading Cython like at #4639 we should really run a -ba on upgrade and not just a -b since the new Cython version in this case does fix some fundamental issues the way exceptions are handled. In general I would be sleep much better if we do this in general since many potentially odd Heisenbugs that disappear after either a partial -b or a -ba would be avoided that way.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4797





---

archive/issue_events_010972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-15T18:29:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10972"
}
```



---

archive/issue_events_010973.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-20T23:19:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10973"
}
```



---

archive/issue_events_010974.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-20T23:19:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.2.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10974"
}
```



---

archive/issue_comments_036290.json:
```json
{
    "body": "I can live with this issue being fixed in 3.3 since we will not upgrade Cython in 3.2.2->3.2.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T22:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I can live with this issue being fixed in 3.3 since we will not upgrade Cython in 3.2.2->3.2.3.

Cheers,

Michael



---

archive/issue_events_010975.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-26T22:54:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.2.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10975"
}
```



---

archive/issue_events_010976.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-26T22:54:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10976"
}
```



---

archive/issue_comments_036291.json:
```json
{
    "body": "Ooops. Reassigned this time :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T22:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops. Reassigned this time :)

Cheers,

Michael



---

archive/issue_comments_036292.json:
```json
{
    "body": "Does anybody have any idea how to implement this?   Here is one idea.  We make it so there is a command like \"sage -ba\" that doesn't actually rebuild the sage library, then we make the cython spkg-install call that command.  It could be called \"sage -ba_nobuild\" or something.  This is way better, I think, than \"sage -ba\" trying to detect if cython was upgraded.  \n\nThe disadvantage is that it might make testing installing the cython SPKG inconvenient.",
    "created_at": "2008-12-29T06:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36292",
    "user": "https://github.com/williamstein"
}
```

Does anybody have any idea how to implement this?   Here is one idea.  We make it so there is a command like "sage -ba" that doesn't actually rebuild the sage library, then we make the cython spkg-install call that command.  It could be called "sage -ba_nobuild" or something.  This is way better, I think, than "sage -ba" trying to detect if cython was upgraded.  

The disadvantage is that it might make testing installing the cython SPKG inconvenient.



---

archive/issue_comments_036293.json:
```json
{
    "body": "Yes, this would make testing Cython spkgs a major pain. I think this probably best belongs in the upgrade script--it could touch all .pyx files after upgrading the Cython script.",
    "created_at": "2008-12-29T19:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36293",
    "user": "https://github.com/robertwb"
}
```

Yes, this would make testing Cython spkgs a major pain. I think this probably best belongs in the upgrade script--it could touch all .pyx files after upgrading the Cython script.



---

archive/issue_comments_036294.json:
```json
{
    "body": "Yes and no. When I test Cython releases I delete the build tree and then do a -ba anyway since that is the only reliable way to test. Obviously if someone is testing \"just\" the spkg this ought to be not enforced, so RobertWB's idea seems the way to go.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-29T19:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes and no. When I test Cython releases I delete the build tree and then do a -ba anyway since that is the only reliable way to test. Obviously if someone is testing "just" the spkg this ought to be not enforced, so RobertWB's idea seems the way to go.

Cheers,

Michael



---

archive/issue_comments_036295.json:
```json
{
    "body": "Yep, when you test a Cython release (assuming I've done my job) it should just work. That's different when I'm hunting down a bug and want to keep re-compiling a certain file (e.g. that last memory leak).",
    "created_at": "2008-12-29T20:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36295",
    "user": "https://github.com/robertwb"
}
```

Yep, when you test a Cython release (assuming I've done my job) it should just work. That's different when I'm hunting down a bug and want to keep re-compiling a certain file (e.g. that last memory leak).



---

archive/issue_comments_036296.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36296",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_036297.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36297",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_036298.json:
```json
{
    "body": "Changing keywords from \"\" to \"upgrade cython\".",
    "created_at": "2010-11-02T22:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36298",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "upgrade cython".



---

archive/issue_comments_036299.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-11-02T22:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36299",
    "user": "https://github.com/jdemeyer"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_036300.json:
```json
{
    "body": "Changing component from packages to build.",
    "created_at": "2010-11-02T22:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36300",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from packages to build.



---

archive/issue_comments_036301.json:
```json
{
    "body": "This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)\n\nAt least for upgrades to final versions, this should IMHO **never** be necessary.",
    "created_at": "2010-11-03T20:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36301",
    "user": "https://github.com/nexttime"
}
```

This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)

At least for upgrades to final versions, this should IMHO **never** be necessary.



---

archive/issue_comments_036302.json:
```json
{
    "body": "P.S.: Explicitly touching some files in `spkg-install` that *are* contained in the extension modules' `include_dirs` can also avoid `sage -ba`, though of course a hack.",
    "created_at": "2010-11-03T20:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36302",
    "user": "https://github.com/nexttime"
}
```

P.S.: Explicitly touching some files in `spkg-install` that *are* contained in the extension modules' `include_dirs` can also avoid `sage -ba`, though of course a hack.



---

archive/issue_comments_036303.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n> This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)\n\nI created ticket #10124 to implement this.",
    "created_at": "2010-11-04T20:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36303",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:11 leif]:
> This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)

I created ticket #10124 to implement this.



---

archive/issue_comments_036304.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> I created ticket #10124 to implement this.\n\n#10214",
    "created_at": "2010-11-04T21:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36304",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 jdemeyer]:
> I created ticket #10124 to implement this.

#10214



---

archive/issue_comments_036305.json:
```json
{
    "body": "Running `sage -ba` *explicitly* is not even necessary upon (true) Cython upgrades, though we could implement this in `spkg/install`.\n\nWe just have to make any Cython file / extension module depend on a single, distinct file of the Cython distribution (e.g. header) and preferably make sure this is *only* touched when really necessary.\n\nTherefore it would make sense to use a Sage-specific file for such, which is created and managed by our `spkg-install` for Cython.\n\nPeople upgrading the Cython package will best know if a complete rebuild will be necessary, depending on the Cython version found in the current installation subject to upgrade.",
    "created_at": "2010-11-04T22:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36305",
    "user": "https://github.com/nexttime"
}
```

Running `sage -ba` *explicitly* is not even necessary upon (true) Cython upgrades, though we could implement this in `spkg/install`.

We just have to make any Cython file / extension module depend on a single, distinct file of the Cython distribution (e.g. header) and preferably make sure this is *only* touched when really necessary.

Therefore it would make sense to use a Sage-specific file for such, which is created and managed by our `spkg-install` for Cython.

People upgrading the Cython package will best know if a complete rebuild will be necessary, depending on the Cython version found in the current installation subject to upgrade.



---

archive/issue_comments_036306.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-10-05T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36306",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_010977.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T08:56:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10977"
}
```



---

archive/issue_comments_036307.json:
```json
{
    "body": "Closing this since I haven't seen this problem at all recently.",
    "created_at": "2012-10-05T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4797#issuecomment-36307",
    "user": "https://github.com/jdemeyer"
}
```

Closing this since I haven't seen this problem at all recently.



---

archive/issue_events_010978.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T08:56:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10978"
}
```



---

archive/issue_events_010979.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T08:56:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4797",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4797#event-10979"
}
```
