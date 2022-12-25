# Issue 4511: sage-combinat script won't work with two digit version numbers (for example: 3.2)

archive/issues_004511.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nKeywords: sage-combinat script\n\nChange the version number in $SAGE_ROOT/local/bin/sage-banner to 3.2 and then watch 'sage -combinat config' fail.\n\nI'll fix this right away.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4511\n\n",
    "created_at": "2008-11-13T10:45:09Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "sage-combinat script won't work with two digit version numbers (for example: 3.2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4511",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

Keywords: sage-combinat script

Change the version number in $SAGE_ROOT/local/bin/sage-banner to 3.2 and then watch 'sage -combinat config' fail.

I'll fix this right away.

Issue created by migration from https://trac.sagemath.org/ticket/4511





---

archive/issue_comments_033390.json:
```json
{
    "body": "Attachment [sage-combinat-script-4511.patch](tarball://root/attachments/some-uuid/ticket4511/sage-combinat-script-4511.patch) by @saliola created at 2008-11-13 10:53:24\n\npatch against version 3.2.rc0",
    "created_at": "2008-11-13T10:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33390",
    "user": "https://github.com/saliola"
}
```

Attachment [sage-combinat-script-4511.patch](tarball://root/attachments/some-uuid/ticket4511/sage-combinat-script-4511.patch) by @saliola created at 2008-11-13 10:53:24

patch against version 3.2.rc0



---

archive/issue_comments_033391.json:
```json
{
    "body": "For the record: my previous patch to the script did not cause this---it would have failed anyway---but it did make me realize that this would be a problem!\n\nTechnical note: the get_sage_version function will now return the version number with any non-numeric stuff stripped off. For example \"3.2.rc0\" will be returned as \"3.2\".",
    "created_at": "2008-11-13T11:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33391",
    "user": "https://github.com/saliola"
}
```

For the record: my previous patch to the script did not cause this---it would have failed anyway---but it did make me realize that this would be a problem!

Technical note: the get_sage_version function will now return the version number with any non-numeric stuff stripped off. For example "3.2.rc0" will be returned as "3.2".



---

archive/issue_events_010223.json:
```json
{
    "actor": "https://github.com/saliola",
    "created_at": "2008-11-13T11:06:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4511#event-10223"
}
```



---

archive/issue_comments_033392.json:
```json
{
    "body": "Thanks!\n\nI am not sure I have the latest sage-combinat script under hand.\nPlease double check that qselect_backward_compatibility_patches also\nsupports 2 digits version numbers, in particular in the version\nguards.\n\nOnce you have done this, I'll give a positive review.\n\nCheers,\n\t\t\t\tNicolas",
    "created_at": "2008-11-13T13:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33392",
    "user": "https://github.com/nthiery"
}
```

Thanks!

I am not sure I have the latest sage-combinat script under hand.
Please double check that qselect_backward_compatibility_patches also
supports 2 digits version numbers, in particular in the version
guards.

Once you have done this, I'll give a positive review.

Cheers,
				Nicolas



---

archive/issue_comments_033393.json:
```json
{
    "body": "```\n>> sage -version\n>> sage -combinat qselect\nActive guards:\nSkip backward compatibility patches for sage 3.0.2\nSkip backward compatibility patches for sage 3.0.3\nSkip backward compatibility patches for sage 3.0.4\nSkip backward compatibility patches for sage 3.0.6\nSkip backward compatibility patches for sage 3.1.2\nSkip backward compatibility patches for sage 3.1.3\nUpdating guards\n  sage -hg qselect -q -n\n  sage -hg qselect\nno active guards\n```\n| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |\nAnd here I've change the version number to 3.1 (by editing sage-banner):\n\n```\n>> sage -version\n>> sage -combinat qselect\nActive guards:\nSkip backward compatibility patches for sage 3.0.2\nSkip backward compatibility patches for sage 3.0.3\nSkip backward compatibility patches for sage 3.0.4\nSkip backward compatibility patches for sage 3.0.6\nKeep backward compatibility patches for sage 3.1.2\nKeep backward compatibility patches for sage 3.1.3\nUpdating guards\n  sage -hg qselect -q -n\n  sage -hg qselect 3_1_2 3_1_3\n```",
    "created_at": "2008-11-13T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33393",
    "user": "https://github.com/saliola"
}
```

```
>> sage -version
>> sage -combinat qselect
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1.2
Skip backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect
no active guards
```
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
And here I've change the version number to 3.1 (by editing sage-banner):

```
>> sage -version
>> sage -combinat qselect
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_1_2 3_1_3
```



---

archive/issue_comments_033394.json:
```json
{
    "body": "Attachment [sage-combinat-script-4511-patch2.patch](tarball://root/attachments/some-uuid/ticket4511/sage-combinat-script-4511-patch2.patch) by @saliola created at 2008-11-14 19:29:13\n\napply only this patch",
    "created_at": "2008-11-14T19:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33394",
    "user": "https://github.com/saliola"
}
```

Attachment [sage-combinat-script-4511-patch2.patch](tarball://root/attachments/some-uuid/ticket4511/sage-combinat-script-4511-patch2.patch) by @saliola created at 2008-11-14 19:29:13

apply only this patch



---

archive/issue_comments_033395.json:
```json
{
    "body": "Whoever reviews this can apply it and test it with the following command (it creates a new branch so it won't mess up your combinat installation):\n\n```\nsage -combinat install --branch=temp_combinat\n```\n\nBut, I checked it throughly and it is working correctly (note that in the above the output the 3.1 guard isn't selected, but below it is).\n\nThe docstring of qselect_backward_compatibility_patches:\n\n```\n    r\"\"\"\n    Selects the appropriate guards for this version of sage\n    e.g. if we are running sage 3.0.2, then we want to apply all\n    the patches which are guarded by 3_0_3, 3_0_4, ...\n    \"\"\"\n```\n\nThe current available guards are: 3_0_2, 3_0_3, 3_0_4, 3_0_6, 3_1, 3_1_2, 3_1_3. So for the current version 3.2, we should apply no patches, and that is what happens:\n\n```\n>> sage -combinat install\n...\nupdating working directory\n43 files updated, 0 files merged, 0 files removed, 0 files unresolved\nActive guards:\nSkip backward compatibility patches for sage 3.0.2\nSkip backward compatibility patches for sage 3.0.3\nSkip backward compatibility patches for sage 3.0.4\nSkip backward compatibility patches for sage 3.0.6\nSkip backward compatibility patches for sage 3.1\nSkip backward compatibility patches for sage 3.1.2\nSkip backward compatibility patches for sage 3.1.3\nUpdating guards\n  sage -hg qselect -q -n\n  sage -hg qselect\nno active guards\n...\n```\n\nFor version 3.1 (I only changed the version number in sage-banner), we want to apply all patches guarded by 3_1_2 and 3_1_3:\n\n```\n>> sage -combinat install\n...\nupdating working directory\n43 files updated, 0 files merged, 0 files removed, 0 files unresolved\nActive guards:\nSkip backward compatibility patches for sage 3.0.2\nSkip backward compatibility patches for sage 3.0.3\nSkip backward compatibility patches for sage 3.0.4\nSkip backward compatibility patches for sage 3.0.6\nSkip backward compatibility patches for sage 3.1\nKeep backward compatibility patches for sage 3.1.2\nKeep backward compatibility patches for sage 3.1.3\nUpdating guards\n  sage -hg qselect -q -n\n  sage -hg qselect 3_1_2 3_1_3\nnumber of unguarded, unapplied patches has changed from 31 to 33\n...\n```\n\n\nFor version 3.0.6 (again, I only changed the version number in sage-banner), we want to apply all patches guarded by 3_0_6, 3_1, 3_1_2, 3_1_3.\n\n```\n>> sage -combinat install\n...\nupdating working directory\n43 files updated, 0 files merged, 0 files removed, 0 files unresolved\nActive guards:\nSkip backward compatibility patches for sage 3.0.2\nSkip backward compatibility patches for sage 3.0.3\nSkip backward compatibility patches for sage 3.0.4\nKeep backward compatibility patches for sage 3.0.6\nKeep backward compatibility patches for sage 3.1\nKeep backward compatibility patches for sage 3.1.2\nKeep backward compatibility patches for sage 3.1.3\nUpdating guards\n  sage -hg qselect -q -n\n  sage -hg qselect 3_0_6 3_1 3_1_2 3_1_3\nnumber of unguarded, unapplied patches has changed from 31 to 36\n...\n```",
    "created_at": "2008-11-14T19:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33395",
    "user": "https://github.com/saliola"
}
```

Whoever reviews this can apply it and test it with the following command (it creates a new branch so it won't mess up your combinat installation):

```
sage -combinat install --branch=temp_combinat
```

But, I checked it throughly and it is working correctly (note that in the above the output the 3.1 guard isn't selected, but below it is).

The docstring of qselect_backward_compatibility_patches:

```
    r"""
    Selects the appropriate guards for this version of sage
    e.g. if we are running sage 3.0.2, then we want to apply all
    the patches which are guarded by 3_0_3, 3_0_4, ...
    """
```

The current available guards are: 3_0_2, 3_0_3, 3_0_4, 3_0_6, 3_1, 3_1_2, 3_1_3. So for the current version 3.2, we should apply no patches, and that is what happens:

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1
Skip backward compatibility patches for sage 3.1.2
Skip backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect
no active guards
...
```

For version 3.1 (I only changed the version number in sage-banner), we want to apply all patches guarded by 3_1_2 and 3_1_3:

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_1_2 3_1_3
number of unguarded, unapplied patches has changed from 31 to 33
...
```


For version 3.0.6 (again, I only changed the version number in sage-banner), we want to apply all patches guarded by 3_0_6, 3_1, 3_1_2, 3_1_3.

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Keep backward compatibility patches for sage 3.0.6
Keep backward compatibility patches for sage 3.1
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_0_6 3_1 3_1_2 3_1_3
number of unguarded, unapplied patches has changed from 31 to 36
...
```



---

archive/issue_comments_033396.json:
```json
{
    "body": "```\nI'd like to give a positive review, but the wiki won't allow me to\naccess the trac guidelines (surge protection) to check how I am\nsupposed to do that. I'll try again tomorrow morning, unless someone\ndoes this for me in the mean time.\n\nIn case you have 2 minutes, can you update the doc string line 203?\n\nCheers,\n\t\t\t\tNicolas\n```",
    "created_at": "2008-11-14T22:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
I'd like to give a positive review, but the wiki won't allow me to
access the trac guidelines (surge protection) to check how I am
supposed to do that. I'll try again tomorrow morning, unless someone
does this for me in the mean time.

In case you have 2 minutes, can you update the doc string line 203?

Cheers,
				Nicolas
```



---

archive/issue_comments_033397.json:
```json
{
    "body": "Merged sage-combinat-script-4511-patch2.patch in Sage 3.2.rc1",
    "created_at": "2008-11-15T04:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-combinat-script-4511-patch2.patch in Sage 3.2.rc1



---

archive/issue_comments_033398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T04:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4511#issuecomment-33398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010224.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-15T04:48:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4511",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4511#event-10224"
}
```
