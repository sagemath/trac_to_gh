# Issue 5296: Update the OS X Readme

archive/issues_005296.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mabshoff\n\nWith the switch to an app bundle distribution for Mac OS X, the file \"$SAGE_ROOT/sage-README-osx.txt\" contains obsolete parts (the \"steps 4 - 6\", and the last lines right at the end).\n\nA -bdist'ed OS X .dmg contains another README.txt file of the same outdated content, probably it is just the first one copied during creation of the .dmg. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5296\n\n",
    "created_at": "2009-02-17T20:19:04Z",
    "labels": [
        "distribution",
        "critical",
        "bug"
    ],
    "title": "Update the OS X Readme",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5296",
    "user": "GeorgSWeber"
}
```
Assignee: mabshoff

CC:  mabshoff

With the switch to an app bundle distribution for Mac OS X, the file "$SAGE_ROOT/sage-README-osx.txt" contains obsolete parts (the "steps 4 - 6", and the last lines right at the end).

A -bdist'ed OS X .dmg contains another README.txt file of the same outdated content, probably it is just the first one copied during creation of the .dmg. 

Issue created by migration from https://trac.sagemath.org/ticket/5296





---

archive/issue_comments_040742.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40742",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040743.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-23T20:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40743",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_040744.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2009-09-23T20:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40744",
    "user": "kcrisman"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_040745.json:
```json
{
    "body": "I don't know how to check whether this \"works\", but at any rate once Sage is automatically distributed in the app bundle, this should go in. \n\nI'm also changing priority, since no one has complained in half a year.",
    "created_at": "2009-09-23T20:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40745",
    "user": "kcrisman"
}
```

I don't know how to check whether this "works", but at any rate once Sage is automatically distributed in the app bundle, this should go in. 

I'm also changing priority, since no one has complained in half a year.



---

archive/issue_comments_040746.json:
```json
{
    "body": "I'm fine with changing the priority. As far as I remember, Michael Abshoff asked me to create this ticket. Unfortunately, nobody seems to want to work on \"app-ifying\" Sage on OS X since his leave.",
    "created_at": "2009-09-24T22:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40746",
    "user": "GeorgSWeber"
}
```

I'm fine with changing the priority. As far as I remember, Michael Abshoff asked me to create this ticket. Unfortunately, nobody seems to want to work on "app-ifying" Sage on OS X since his leave.



---

archive/issue_comments_040747.json:
```json
{
    "body": "Changing assignee from mabshoff to iandrus.",
    "created_at": "2009-11-27T21:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40747",
    "user": "iandrus"
}
```

Changing assignee from mabshoff to iandrus.



---

archive/issue_comments_040748.json:
```json
{
    "body": "Now that I hopefully have a little more time I plan to work on \"app-ifying\" Sage.  What is preventing us from distributing sage in the app bundle automatically?  Is there a reason we don't just make SAGE_APP_BUNDLE=yes the default?",
    "created_at": "2009-11-27T21:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40748",
    "user": "iandrus"
}
```

Now that I hopefully have a little more time I plan to work on "app-ifying" Sage.  What is preventing us from distributing sage in the app bundle automatically?  Is there a reason we don't just make SAGE_APP_BUNDLE=yes the default?



---

archive/issue_comments_040749.json:
```json
{
    "body": "Apparently there were some movement issues, that is to say moving the Sage installation within the computer didn't always work properly.  There is an open ticket about this, #5254.  #5261 is also related.  I like #7546, too - can't review it in detail now, but it would be great to finally get this taken care of, and I would be happy to help out with reviewing duties once I'm in a position to do so.",
    "created_at": "2009-11-28T04:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40749",
    "user": "kcrisman"
}
```

Apparently there were some movement issues, that is to say moving the Sage installation within the computer didn't always work properly.  There is an open ticket about this, #5254.  #5261 is also related.  I like #7546, too - can't review it in detail now, but it would be great to finally get this taken care of, and I would be happy to help out with reviewing duties once I'm in a position to do so.



---

archive/issue_comments_040750.json:
```json
{
    "body": "Now that #5254, #5261, and #7546 are more or less resolved, we should resolve this situation.  Note that sage-bdist doesn't currently automatically make an app bundle yet, and this should probably be resolved on sage-devel, for the following reason: some people, perhaps many, will want to have both the notebook and command line options, but the current script makes the notebook only.  We should definitely eventually distribute a notebook-only one, but I'm not sure that should be the default until we have both available.  Ideally, this would be yet another environment variable for sage-bdist :)\n\nBut we're very, very close!  So much thanks to iandrus for making huge leaps over my initial small steps on all this.",
    "created_at": "2009-12-08T15:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40750",
    "user": "kcrisman"
}
```

Now that #5254, #5261, and #7546 are more or less resolved, we should resolve this situation.  Note that sage-bdist doesn't currently automatically make an app bundle yet, and this should probably be resolved on sage-devel, for the following reason: some people, perhaps many, will want to have both the notebook and command line options, but the current script makes the notebook only.  We should definitely eventually distribute a notebook-only one, but I'm not sure that should be the default until we have both available.  Ideally, this would be yet another environment variable for sage-bdist :)

But we're very, very close!  So much thanks to iandrus for making huge leaps over my initial small steps on all this.



---

archive/issue_comments_040751.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-30T21:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40751",
    "user": "iandrus"
}
```

Attachment



---

archive/issue_comments_040752.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-30T21:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40752",
    "user": "iandrus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040753.json:
```json
{
    "body": "I'm not sure I made the readme any simpler, but at least it should be accurate once we start distributing the sage application.",
    "created_at": "2010-03-30T21:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40753",
    "user": "iandrus"
}
```

I'm not sure I made the readme any simpler, but at least it should be accurate once we start distributing the sage application.



---

archive/issue_comments_040754.json:
```json
{
    "body": "See also #6938.",
    "created_at": "2010-03-31T16:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40754",
    "user": "jhpalmieri"
}
```

See also #6938.



---

archive/issue_comments_040755.json:
```json
{
    "body": "This looks fine to me.  Positive review if we ever actually distribute these.\n\nWhat we really need to do is distribute the notebook binary and also just a regular (perhaps non-bundle) binary, but maybe this is a lot to host when it comes to mirrors?  \n\nOr, again, figure out how to make the app bundle let you choose between command line and notebook.",
    "created_at": "2010-04-22T01:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40755",
    "user": "kcrisman"
}
```

This looks fine to me.  Positive review if we ever actually distribute these.

What we really need to do is distribute the notebook binary and also just a regular (perhaps non-bundle) binary, but maybe this is a lot to host when it comes to mirrors?  

Or, again, figure out how to make the app bundle let you choose between command line and notebook.



---

archive/issue_comments_040756.json:
```json
{
    "body": "With respect to #6938, be sure to only do this with the copy in /local/bin .  The other one should probably be removed.",
    "created_at": "2010-04-28T18:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40756",
    "user": "kcrisman"
}
```

With respect to #6938, be sure to only do this with the copy in /local/bin .  The other one should probably be removed.



---

archive/issue_comments_040757.json:
```json
{
    "body": "#9873 is related, and may eventually supersede this.",
    "created_at": "2010-09-08T14:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40757",
    "user": "kcrisman"
}
```

#9873 is related, and may eventually supersede this.



---

archive/issue_comments_040758.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T11:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40758",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040759.json:
```json
{
    "body": "## Release manager\n\nPlease close this ticket as a \"duplicate\" when #9873 is merged.",
    "created_at": "2010-09-28T11:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40759",
    "user": "mpatel"
}
```

## Release manager

Please close this ticket as a "duplicate" when #9873 is merged.



---

archive/issue_comments_040760.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> == Release manager ==\n> \n> Please close this ticket as a \"duplicate\" when #9873 is merged.\n\nOr, 'merge' this one first and then #9873 (as noted in that ticket's comments).",
    "created_at": "2010-09-29T18:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40760",
    "user": "kcrisman"
}
```

Replying to [comment:12 mpatel]:
> == Release manager ==
> 
> Please close this ticket as a "duplicate" when #9873 is merged.

Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).



---

archive/issue_comments_040761.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Replying to [comment:12 mpatel]:\n> > == Release manager ==\n> > \n> > Please close this ticket as a \"duplicate\" when #9873 is merged.\n> \n> Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).\nSorry for the noise - jhpalmieri is right in his comments in #9873.  Treat as previously mentioned.",
    "created_at": "2010-09-29T20:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40761",
    "user": "kcrisman"
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

archive/issue_comments_040762.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-29T23:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5296#issuecomment-40762",
    "user": "mpatel"
}
```

Resolution: duplicate
