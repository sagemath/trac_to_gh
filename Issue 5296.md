# Issue 5296: Update the OS X Readme

archive/issues_005296.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mabshoff\n\nWith the switch to an app bundle distribution for Mac OS X, the file \"$SAGE_ROOT/sage-README-osx.txt\" contains obsolete parts (the \"steps 4 - 6\", and the last lines right at the end).\n\nA -bdist'ed OS X .dmg contains another README.txt file of the same outdated content, probably it is just the first one copied during creation of the .dmg. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5296\n\n",
    "created_at": "2009-02-17T20:19:04Z",
    "labels": [
        "component: distribution",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update the OS X Readme",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5296",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: mabshoff

CC:  mabshoff

With the switch to an app bundle distribution for Mac OS X, the file "$SAGE_ROOT/sage-README-osx.txt" contains obsolete parts (the "steps 4 - 6", and the last lines right at the end).

A -bdist'ed OS X .dmg contains another README.txt file of the same outdated content, probably it is just the first one copied during creation of the .dmg. 

Issue created by migration from https://trac.sagemath.org/ticket/5296





---

archive/issue_comments_040663.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40663",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040664.json:
```json
{
    "body": "Attachment [sage-README-osx.txt](tarball://root/attachments/some-uuid/ticket5296/sage-README-osx.txt) by @kcrisman created at 2009-09-23 20:19:42",
    "created_at": "2009-09-23T20:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40664",
    "user": "https://github.com/kcrisman"
}
```

Attachment [sage-README-osx.txt](tarball://root/attachments/some-uuid/ticket5296/sage-README-osx.txt) by @kcrisman created at 2009-09-23 20:19:42



---

archive/issue_comments_040665.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2009-09-23T20:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40665",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_040666.json:
```json
{
    "body": "I don't know how to check whether this \"works\", but at any rate once Sage is automatically distributed in the app bundle, this should go in. \n\nI'm also changing priority, since no one has complained in half a year.",
    "created_at": "2009-09-23T20:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40666",
    "user": "https://github.com/kcrisman"
}
```

I don't know how to check whether this "works", but at any rate once Sage is automatically distributed in the app bundle, this should go in. 

I'm also changing priority, since no one has complained in half a year.



---

archive/issue_comments_040667.json:
```json
{
    "body": "I'm fine with changing the priority. As far as I remember, Michael Abshoff asked me to create this ticket. Unfortunately, nobody seems to want to work on \"app-ifying\" Sage on OS X since his leave.",
    "created_at": "2009-09-24T22:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40667",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

I'm fine with changing the priority. As far as I remember, Michael Abshoff asked me to create this ticket. Unfortunately, nobody seems to want to work on "app-ifying" Sage on OS X since his leave.



---

archive/issue_comments_040668.json:
```json
{
    "body": "Changing assignee from mabshoff to @gvol.",
    "created_at": "2009-11-27T21:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40668",
    "user": "https://github.com/gvol"
}
```

Changing assignee from mabshoff to @gvol.



---

archive/issue_comments_040669.json:
```json
{
    "body": "Now that I hopefully have a little more time I plan to work on \"app-ifying\" Sage.  What is preventing us from distributing sage in the app bundle automatically?  Is there a reason we don't just make SAGE_APP_BUNDLE=yes the default?",
    "created_at": "2009-11-27T21:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40669",
    "user": "https://github.com/gvol"
}
```

Now that I hopefully have a little more time I plan to work on "app-ifying" Sage.  What is preventing us from distributing sage in the app bundle automatically?  Is there a reason we don't just make SAGE_APP_BUNDLE=yes the default?



---

archive/issue_comments_040670.json:
```json
{
    "body": "Apparently there were some movement issues, that is to say moving the Sage installation within the computer didn't always work properly.  There is an open ticket about this, #5254.  #5261 is also related.  I like #7546, too - can't review it in detail now, but it would be great to finally get this taken care of, and I would be happy to help out with reviewing duties once I'm in a position to do so.",
    "created_at": "2009-11-28T04:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40670",
    "user": "https://github.com/kcrisman"
}
```

Apparently there were some movement issues, that is to say moving the Sage installation within the computer didn't always work properly.  There is an open ticket about this, #5254.  #5261 is also related.  I like #7546, too - can't review it in detail now, but it would be great to finally get this taken care of, and I would be happy to help out with reviewing duties once I'm in a position to do so.



---

archive/issue_comments_040671.json:
```json
{
    "body": "Now that #5254, #5261, and #7546 are more or less resolved, we should resolve this situation.  Note that sage-bdist doesn't currently automatically make an app bundle yet, and this should probably be resolved on sage-devel, for the following reason: some people, perhaps many, will want to have both the notebook and command line options, but the current script makes the notebook only.  We should definitely eventually distribute a notebook-only one, but I'm not sure that should be the default until we have both available.  Ideally, this would be yet another environment variable for sage-bdist :)\n\nBut we're very, very close!  So much thanks to iandrus for making huge leaps over my initial small steps on all this.",
    "created_at": "2009-12-08T15:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40671",
    "user": "https://github.com/kcrisman"
}
```

Now that #5254, #5261, and #7546 are more or less resolved, we should resolve this situation.  Note that sage-bdist doesn't currently automatically make an app bundle yet, and this should probably be resolved on sage-devel, for the following reason: some people, perhaps many, will want to have both the notebook and command line options, but the current script makes the notebook only.  We should definitely eventually distribute a notebook-only one, but I'm not sure that should be the default until we have both available.  Ideally, this would be yet another environment variable for sage-bdist :)

But we're very, very close!  So much thanks to iandrus for making huge leaps over my initial small steps on all this.



---

archive/issue_comments_040672.json:
```json
{
    "body": "Attachment [sage-README-osx.2.txt](tarball://root/attachments/some-uuid/ticket5296/sage-README-osx.2.txt) by @gvol created at 2010-03-30 21:22:23",
    "created_at": "2010-03-30T21:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40672",
    "user": "https://github.com/gvol"
}
```

Attachment [sage-README-osx.2.txt](tarball://root/attachments/some-uuid/ticket5296/sage-README-osx.2.txt) by @gvol created at 2010-03-30 21:22:23



---

archive/issue_comments_040673.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-30T21:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40673",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040674.json:
```json
{
    "body": "I'm not sure I made the readme any simpler, but at least it should be accurate once we start distributing the sage application.",
    "created_at": "2010-03-30T21:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40674",
    "user": "https://github.com/gvol"
}
```

I'm not sure I made the readme any simpler, but at least it should be accurate once we start distributing the sage application.



---

archive/issue_comments_040675.json:
```json
{
    "body": "See also #6938.",
    "created_at": "2010-03-31T16:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40675",
    "user": "https://github.com/jhpalmieri"
}
```

See also #6938.



---

archive/issue_comments_040676.json:
```json
{
    "body": "This looks fine to me.  Positive review if we ever actually distribute these.\n\nWhat we really need to do is distribute the notebook binary and also just a regular (perhaps non-bundle) binary, but maybe this is a lot to host when it comes to mirrors?  \n\nOr, again, figure out how to make the app bundle let you choose between command line and notebook.",
    "created_at": "2010-04-22T01:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40676",
    "user": "https://github.com/kcrisman"
}
```

This looks fine to me.  Positive review if we ever actually distribute these.

What we really need to do is distribute the notebook binary and also just a regular (perhaps non-bundle) binary, but maybe this is a lot to host when it comes to mirrors?  

Or, again, figure out how to make the app bundle let you choose between command line and notebook.



---

archive/issue_comments_040677.json:
```json
{
    "body": "With respect to #6938, be sure to only do this with the copy in /local/bin .  The other one should probably be removed.",
    "created_at": "2010-04-28T18:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40677",
    "user": "https://github.com/kcrisman"
}
```

With respect to #6938, be sure to only do this with the copy in /local/bin .  The other one should probably be removed.



---

archive/issue_comments_040678.json:
```json
{
    "body": "#9873 is related, and may eventually supersede this.",
    "created_at": "2010-09-08T14:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40678",
    "user": "https://github.com/kcrisman"
}
```

#9873 is related, and may eventually supersede this.



---

archive/issue_comments_040679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T11:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40679",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040680.json:
```json
{
    "body": "## Release manager\n\nPlease close this ticket as a \"duplicate\" when #9873 is merged.",
    "created_at": "2010-09-28T11:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40680",
    "user": "https://github.com/qed777"
}
```

## Release manager

Please close this ticket as a "duplicate" when #9873 is merged.



---

archive/issue_comments_040681.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> == Release manager ==\n> \n> Please close this ticket as a \"duplicate\" when #9873 is merged.\n\nOr, 'merge' this one first and then #9873 (as noted in that ticket's comments).",
    "created_at": "2010-09-29T18:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40681",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:12 mpatel]:
> == Release manager ==
> 
> Please close this ticket as a "duplicate" when #9873 is merged.

Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).



---

archive/issue_comments_040682.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Replying to [comment:12 mpatel]:\n> > == Release manager ==\n> > \n> > Please close this ticket as a \"duplicate\" when #9873 is merged.\n> \n> Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).\nSorry for the noise - jhpalmieri is right in his comments in #9873.  Treat as previously mentioned.",
    "created_at": "2010-09-29T20:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40682",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:13 kcrisman]:
> Replying to [comment:12 mpatel]:
> > == Release manager ==
> > 
> > Please close this ticket as a "duplicate" when #9873 is merged.
> 
> Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).
Sorry for the noise - jhpalmieri is right in his comments in #9873.  Treat as previously mentioned.



---

archive/issue_comments_040683.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-29T23:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40683",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_005552.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-29T23:17:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5296#event-5552"
}
```
