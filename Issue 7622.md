# Issue 7622: Fix OSX plist copyright situation

archive/issues_007622.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @gvol @mwhansen @williamstein\n\nFrom #5261: \n\n```\nremove the extra copyright work in credits as well as give credit to \"William Stein and the Sage Development Team\"\n```\n\n\n```\nSomeone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.\n```\n\nThis shouldn't be hard to fix.  Use hg_sage.extcode!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7622\n\n",
    "created_at": "2009-12-08T15:27:34Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Fix OSX plist copyright situation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7622",
    "user": "https://github.com/kcrisman"
}
```
Assignee: mvngu

CC:  @gvol @mwhansen @williamstein

From #5261: 

```
remove the extra copyright work in credits as well as give credit to "William Stein and the Sage Development Team"
```


```
Someone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.
```

This shouldn't be hard to fix.  Use hg_sage.extcode!

Issue created by migration from https://trac.sagemath.org/ticket/7622





---

archive/issue_comments_065013.json:
```json
{
    "body": "Attachment [trac_7622.patch](tarball://root/attachments/some-uuid/ticket7622/trac_7622.patch) by @kcrisman created at 2009-12-14 16:57:39\n\nBased on 4.3.alpha1",
    "created_at": "2009-12-14T16:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65013",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7622.patch](tarball://root/attachments/some-uuid/ticket7622/trac_7622.patch) by @kcrisman created at 2009-12-14 16:57:39

Based on 4.3.alpha1



---

archive/issue_comments_065014.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T16:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65014",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065015.json:
```json
{
    "body": "I hope this will be good; I have put 2005- rather than 2005-2009 or whatever so that it won't have to be updated constantly.  I have also cc:ed two people who should be able to review the correctness of this attribution, which is the one found on all documentation but (curiously) nowhere I can find on the software itself.",
    "created_at": "2009-12-14T16:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65015",
    "user": "https://github.com/kcrisman"
}
```

I hope this will be good; I have put 2005- rather than 2005-2009 or whatever so that it won't have to be updated constantly.  I have also cc:ed two people who should be able to review the correctness of this attribution, which is the one found on all documentation but (curiously) nowhere I can find on the software itself.



---

archive/issue_comments_065016.json:
```json
{
    "body": "Attachment [trac_7622-reviewer.patch](tarball://root/attachments/some-uuid/ticket7622/trac_7622-reviewer.patch) by mvngu created at 2009-12-15 00:29:53\n\nreviewer patch",
    "created_at": "2009-12-15T00:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7622-reviewer.patch](tarball://root/attachments/some-uuid/ticket7622/trac_7622-reviewer.patch) by mvngu created at 2009-12-15 00:29:53

reviewer patch



---

archive/issue_comments_065017.json:
```json
{
    "body": "The relevant Mercurial repository is\n\n\n```\nSAGE_ROOT/data/extcode\n```\n\n\nAt least with Sage 4.3.rc0, it has a junk file which should be removed:\n\n\n```\n[mvngu@sage extcode]$ pwd\n/scratch/mvngu/build/sage-4.3.rc0/data/extcode\n[mvngu@sage extcode]$ hg st\n? sage/ext/.DS_Store.rej\n```\n\n\nSo I removed that junk file as follows:\n\n\n```\n[mvngu@sage extcode]$ rm -rf sage/ext/.DS_Store.rej\n[mvngu@sage extcode]$ hg st\n<no output>\n```\n\n\nI applied `trac_7622.patch` against Sage 4.3.rc0 successfully. I also attached `trac_7622-reviewer.patch` which fixes the copyright notice in another file specific to OS X. The reviewer patch also ensures that the copyright notices are consistent with that shown on the standard documentation. In particular, I use \"2005-2009\" as is used on the documentation. I have created a [wiki page](http://wiki.sagemath.org/UpdateCopyright) which lists files that need to be updated when the copyright notice is updated. Patches should be applied in this order:\n\n1. Delete the file `data/extcode/sage/ext/.DS_Store.rej`\n2. Apply `trac_7622.patch`\n3. Finally, apply `trac_7622-reviewer.patch`\n \nOnly my patch needs review.",
    "created_at": "2009-12-15T00:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The relevant Mercurial repository is


```
SAGE_ROOT/data/extcode
```


At least with Sage 4.3.rc0, it has a junk file which should be removed:


```
[mvngu@sage extcode]$ pwd
/scratch/mvngu/build/sage-4.3.rc0/data/extcode
[mvngu@sage extcode]$ hg st
? sage/ext/.DS_Store.rej
```


So I removed that junk file as follows:


```
[mvngu@sage extcode]$ rm -rf sage/ext/.DS_Store.rej
[mvngu@sage extcode]$ hg st
<no output>
```


I applied `trac_7622.patch` against Sage 4.3.rc0 successfully. I also attached `trac_7622-reviewer.patch` which fixes the copyright notice in another file specific to OS X. The reviewer patch also ensures that the copyright notices are consistent with that shown on the standard documentation. In particular, I use "2005-2009" as is used on the documentation. I have created a [wiki page](http://wiki.sagemath.org/UpdateCopyright) which lists files that need to be updated when the copyright notice is updated. Patches should be applied in this order:

1. Delete the file `data/extcode/sage/ext/.DS_Store.rej`
2. Apply `trac_7622.patch`
3. Finally, apply `trac_7622-reviewer.patch`
 
Only my patch needs review.



---

archive/issue_events_018111.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2009-12-15T13:27:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7622#event-18111"
}
```



---

archive/issue_comments_065018.json:
```json
{
    "body": "It would be good if this got into 4.3 still, since it is not about functionality but rather clarifying copyright.\n\nThe \"junk\" file is fallout from iandrus' changing the Mac app structure from a tar.gz file to a normal directory structure, and hopefully this will fix things from that.\n\nThe other patch looks good to me - we hadn't noticed that other plist that needed this.  It applies fine as well.\n\nHowever, I think that this wiki page is liable to get lost in the wilderness.  Maybe not right away, since 2010 is so close, but for 2011... can anyone think of somewhere this can link to that would be more prominent?  Or, perhaps one should open a ticket for 2010, and put on there to open a ticket for 2011 once that ticket is closed... maybe.",
    "created_at": "2009-12-15T13:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65018",
    "user": "https://github.com/kcrisman"
}
```

It would be good if this got into 4.3 still, since it is not about functionality but rather clarifying copyright.

The "junk" file is fallout from iandrus' changing the Mac app structure from a tar.gz file to a normal directory structure, and hopefully this will fix things from that.

The other patch looks good to me - we hadn't noticed that other plist that needed this.  It applies fine as well.

However, I think that this wiki page is liable to get lost in the wilderness.  Maybe not right away, since 2010 is so close, but for 2011... can anyone think of somewhere this can link to that would be more prominent?  Or, perhaps one should open a ticket for 2010, and put on there to open a ticket for 2011 once that ticket is closed... maybe.



---

archive/issue_comments_065019.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T13:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65019",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065020.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T16:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7622#issuecomment-65020",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018112.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T16:08:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7622",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7622#event-18112"
}
```
