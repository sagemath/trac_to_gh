# Issue 6694: [with patch, needs review] Live reference manual worksheets

archive/issues_006694.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jhpalmieri\n\nSage generates live \"docbrowser\" worksheets for the tutorial, developer's guide, and constructions guide, but not for the reference manual.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6694\n\n",
    "created_at": "2009-08-09T06:07:47Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Live reference manual worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6694",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @jhpalmieri

Sage generates live "docbrowser" worksheets for the tutorial, developer's guide, and constructions guide, but not for the reference manual.

Issue created by migration from https://trac.sagemath.org/ticket/6694





---

archive/issue_comments_054902.json:
```json
{
    "body": "Attachment [trac_6694-live_ref_manual.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual.patch) by @qed777 created at 2009-08-09 06:10:36",
    "created_at": "2009-08-09T06:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54902",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6694-live_ref_manual.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual.patch) by @qed777 created at 2009-08-09 06:10:36



---

archive/issue_comments_054903.json:
```json
{
    "body": "I've attached a first take.  I haven't tested it extensively, but it seems to work for several pages at different depths in the reference manual's hierarchy.\n\nShould we change the green background color for Sage output?  Perhaps we can insert a CSS directive after `default.css` in `twist.py` (see lines 194+).\n\nActually, the patch is not specific to the manual, so we should be able to add other complex documents, including textbooks, specialized tutorials, etc.",
    "created_at": "2009-08-09T06:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54903",
    "user": "https://github.com/qed777"
}
```

I've attached a first take.  I haven't tested it extensively, but it seems to work for several pages at different depths in the reference manual's hierarchy.

Should we change the green background color for Sage output?  Perhaps we can insert a CSS directive after `default.css` in `twist.py` (see lines 194+).

Actually, the patch is not specific to the manual, so we should be able to add other complex documents, including textbooks, specialized tutorials, etc.



---

archive/issue_comments_054904.json:
```json
{
    "body": "Attachment [trac_6694-live_ref_manual_v2.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v2.patch) by @qed777 created at 2009-08-09 18:00:30\n\nHandle nonexistent pages better.  Apply only this patch.",
    "created_at": "2009-08-09T18:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54904",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6694-live_ref_manual_v2.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v2.patch) by @qed777 created at 2009-08-09 18:00:30

Handle nonexistent pages better.  Apply only this patch.



---

archive/issue_comments_054905.json:
```json
{
    "body": "The new version does not throw an exception for, e.g., `http://localhost:8000/doc/live/reference/foo.html`.",
    "created_at": "2009-08-09T18:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54905",
    "user": "https://github.com/qed777"
}
```

The new version does not throw an exception for, e.g., `http://localhost:8000/doc/live/reference/foo.html`.



---

archive/issue_comments_054906.json:
```json
{
    "body": "Attachment [trac_6694-css.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-css.patch) by @qed777 created at 2009-08-09 19:55:18\n\nStyle tweaks.  Apply before or after \"live_ref_manual\" patch.",
    "created_at": "2009-08-09T19:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54906",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6694-css.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-css.patch) by @qed777 created at 2009-08-09 19:55:18

Style tweaks.  Apply before or after "live_ref_manual" patch.



---

archive/issue_comments_054907.json:
```json
{
    "body": "Feel free to edit the optional CSS patch.",
    "created_at": "2009-08-09T19:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54907",
    "user": "https://github.com/qed777"
}
```

Feel free to edit the optional CSS patch.



---

archive/issue_comments_054908.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Feel free to edit the optional CSS patch.\n\nOr ignore it altogether!",
    "created_at": "2009-09-21T03:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54908",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 mpatel]:
> Feel free to edit the optional CSS patch.

Or ignore it altogether!



---

archive/issue_comments_054909.json:
```json
{
    "body": "This seems to work great, and I would give it a positive review except that I just saw William Stein comment that in his notebook refactoring he is switching all path joining to use os.path.join.  In this patch, there are lines:\n\npath = self.docpath + '/' + '/'.join(segments) \n\nand\n\npath = self.docpath + '/' + '/'.join(segments[ind:])\n\nthat should be changed to use os.path.join().",
    "created_at": "2009-09-22T16:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This seems to work great, and I would give it a positive review except that I just saw William Stein comment that in his notebook refactoring he is switching all path joining to use os.path.join.  In this patch, there are lines:

path = self.docpath + '/' + '/'.join(segments) 

and

path = self.docpath + '/' + '/'.join(segments[ind:])

that should be changed to use os.path.join().



---

archive/issue_comments_054910.json:
```json
{
    "body": "Normalize real paths. Apply only this patch.",
    "created_at": "2009-09-23T00:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54910",
    "user": "https://github.com/qed777"
}
```

Normalize real paths. Apply only this patch.



---

archive/issue_comments_054911.json:
```json
{
    "body": "Attachment [trac_6694-live_ref_manual_v3.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v3.patch) by @qed777 created at 2009-09-23 00:45:20\n\nUse os.path.join(). Apply only this patch.",
    "created_at": "2009-09-23T00:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54911",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6694-live_ref_manual_v3.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v3.patch) by @qed777 created at 2009-09-23 00:45:20

Use os.path.join(). Apply only this patch.



---

archive/issue_comments_054912.json:
```json
{
    "body": "Attachment [trac_6694-live_ref_manual_v3.2.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v3.2.patch) by @qed777 created at 2009-09-23 00:47:04\n\nPlease try [attachment:trac_6694-live_ref_manual_v3.2.patch v3.2].",
    "created_at": "2009-09-23T00:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54912",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6694-live_ref_manual_v3.2.patch](tarball://root/attachments/some-uuid/ticket6694/trac_6694-live_ref_manual_v3.2.patch) by @qed777 created at 2009-09-23 00:47:04

Please try [attachment:trac_6694-live_ref_manual_v3.2.patch v3.2].



---

archive/issue_comments_054913.json:
```json
{
    "body": "Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.",
    "created_at": "2009-09-23T14:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.



---

archive/issue_comments_054914.json:
```json
{
    "body": "Replying to [comment:9 mhampton]:\n> Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.\n\nNo problem.  To really tax a browser, try \"evaluating all\" cells in a long section of the manual.",
    "created_at": "2009-09-23T14:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54914",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:9 mhampton]:
> Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.

No problem.  To really tax a browser, try "evaluating all" cells in a long section of the manual.



---

archive/issue_events_015784.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T09:46:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6694#event-15784"
}
```



---

archive/issue_events_015785.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T09:46:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6694#event-15785"
}
```



---

archive/issue_comments_054915.json:
```json
{
    "body": "Merged `trac_6694-live_ref_manual_v3.2.patch`.",
    "created_at": "2009-09-24T09:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6694-live_ref_manual_v3.2.patch`.



---

archive/issue_comments_054916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T09:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054917.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6694#issuecomment-54917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
