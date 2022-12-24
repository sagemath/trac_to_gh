# Issue 7765: In sage-4.3, the command "sage -bdist" is broken on OS X

archive/issues_007765.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  georgsweber\n\nOn OS X with sage-4.3, if you do \"sage -bdist\" it creates the dist/sage-* directory correctly. However, it doesn't create the dmg anymore.  It can evidently be made to do so by setting environment variables.  But the default \"sage -bdist\" doesn't create a bdist.     This is confusing and very inconsistent with the behavior on all other OS's.  For some reason Ivan Andrus changed this in #7546. \n\nThis will have to be fixed back for 4.3.1. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7765\n\n",
    "created_at": "2009-12-25T09:32:40Z",
    "labels": [
        "distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "In sage-4.3, the command \"sage -bdist\" is broken on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7765",
    "user": "@williamstein"
}
```
Assignee: tbd

CC:  georgsweber

On OS X with sage-4.3, if you do "sage -bdist" it creates the dist/sage-* directory correctly. However, it doesn't create the dmg anymore.  It can evidently be made to do so by setting environment variables.  But the default "sage -bdist" doesn't create a bdist.     This is confusing and very inconsistent with the behavior on all other OS's.  For some reason Ivan Andrus changed this in #7546. 

This will have to be fixed back for 4.3.1. 

Issue created by migration from https://trac.sagemath.org/ticket/7765





---

archive/issue_comments_066895.json:
```json
{
    "body": "Based on 4.3",
    "created_at": "2009-12-28T17:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66895",
    "user": "@kcrisman"
}
```

Based on 4.3



---

archive/issue_comments_066896.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-28T17:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66896",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066897.json:
```json
{
    "body": "Attachment [trac_7765-dmg.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg.patch) by @kcrisman created at 2009-12-28 17:20:50\n\nThis is a very naive solution, but hopefully it is sufficient.  Since I was the one who didn't realize that was changing standard behavior (in fact, I thought it was a feature!) on the previous ticket, I figure I should attempt to fix it.",
    "created_at": "2009-12-28T17:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66897",
    "user": "@kcrisman"
}
```

Attachment [trac_7765-dmg.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg.patch) by @kcrisman created at 2009-12-28 17:20:50

This is a very naive solution, but hopefully it is sufficient.  Since I was the one who didn't realize that was changing standard behavior (in fact, I thought it was a feature!) on the previous ticket, I figure I should attempt to fix it.



---

archive/issue_comments_066898.json:
```json
{
    "body": "Your patch has the line:\n\n```  \nif [ \"$SAGE_APP_DMG\" = \"no\" ]; then \n```\n\n\nThis seems to thus bizarrely assume that  SAGE_APP_DMG is either \"yes\" or \"no\". But it is an environment variable, so can be anything, and defaults to being \"\".   Did you test the above with SAGE_APP_DMG not set?",
    "created_at": "2010-02-07T06:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66898",
    "user": "@williamstein"
}
```

Your patch has the line:

```  
if [ "$SAGE_APP_DMG" = "no" ]; then 
```


This seems to thus bizarrely assume that  SAGE_APP_DMG is either "yes" or "no". But it is an environment variable, so can be anything, and defaults to being "".   Did you test the above with SAGE_APP_DMG not set?



---

archive/issue_comments_066899.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-07T06:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66899",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066900.json:
```json
{
    "body": "Like I said, it is a very naive solution; I never claimed to be a shell script expert :)  Will do my best to make it better but am not sure when I will have time.",
    "created_at": "2010-02-08T02:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66900",
    "user": "@kcrisman"
}
```

Like I said, it is a very naive solution; I never claimed to be a shell script expert :)  Will do my best to make it better but am not sure when I will have time.



---

archive/issue_comments_066901.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> Your patch has the line:\n> {{{  \n> if [ \"$SAGE_APP_DMG\" = \"no\" ]; then \n> }}}\n> \n> This seems to thus bizarrely assume that  SAGE_APP_DMG is either \"yes\" or \"no\". But it is an environment variable, so can be anything, and defaults to being \"\".   Did you test the above with SAGE_APP_DMG not set?\n\nWell, apparently as long as you don't have SAGE_APP_DMG being 'no', it will make the dmg.   At least, that's what happened when I tested this, and Sage worked.  Should I change\n\n```\n        echo 'If you wish to create a disk image please set'\n        echo 'SAGE_APP_DMG=yes'\n```\n\nto something about\n\n```\n        echo 'If you wish to create a disk image please do'\n        echo 'unset SAGE_APP_DMG'\n```\n\nor something similar?\n\nI just don't know what is best; since we want the default to be making a dmg, I guess any of these options make it maximally hard to *not* make a dmg, but maybe they are not very 'shell-script'-y.  I'm putting this as 'needs review' again, but feel free to put it back to 'needs work' with any comments that would make it better.",
    "created_at": "2010-02-08T19:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66901",
    "user": "@kcrisman"
}
```

Replying to [comment:2 was]:
> Your patch has the line:
> {{{  
> if [ "$SAGE_APP_DMG" = "no" ]; then 
> }}}
> 
> This seems to thus bizarrely assume that  SAGE_APP_DMG is either "yes" or "no". But it is an environment variable, so can be anything, and defaults to being "".   Did you test the above with SAGE_APP_DMG not set?

Well, apparently as long as you don't have SAGE_APP_DMG being 'no', it will make the dmg.   At least, that's what happened when I tested this, and Sage worked.  Should I change

```
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
```

to something about

```
        echo 'If you wish to create a disk image please do'
        echo 'unset SAGE_APP_DMG'
```

or something similar?

I just don't know what is best; since we want the default to be making a dmg, I guess any of these options make it maximally hard to *not* make a dmg, but maybe they are not very 'shell-script'-y.  I'm putting this as 'needs review' again, but feel free to put it back to 'needs work' with any comments that would make it better.



---

archive/issue_comments_066902.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T19:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66902",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066903.json:
```json
{
    "body": "I'll see how much time time I find this weekend.\nThe current situation is annoying me, too.",
    "created_at": "2010-02-13T06:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66903",
    "user": "GeorgSWeber"
}
```

I'll see how much time time I find this weekend.
The current situation is annoying me, too.



---

archive/issue_comments_066904.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-14T13:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66904",
    "user": "GeorgSWeber"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066905.json:
```json
{
    "body": "After the patch \"trac_7765-dmg.patch\" from seven weeks ago, the functionality is as (I think) it should be, i.e. unless an environment variable \"SAGE_APP_DMG\" both exists and has a value of \"no\", the dmg will be built. Good.\n\nAs for the documentation/printout statements, one might think of something along the following lines to be more verbose:\n\n``` \n    if [ \"$SAGE_APP_DMG\" = \"no\" ]; then\n        echo 'If you wish to create a disk image please set'\n        echo 'SAGE_APP_DMG=yes'\n        echo '(or to anything else but the current SAGE_APP_DMG=no,'\n        echo ' or completely unset SAGE_APP_DMG)'\n    else\n        echo \"Creating dmg\"\n        echo '(If you don't wish to create a disk image please set'\n        echo ' SAGE_APP_DMG=no)'\n        DYLD_LIBRARY_PATH=$SAGE_ORIG_DYLD_LIBRARY_PATH; export DYLD_LIBRARY_PATH\n        hdiutil create -srcfolder \"$TARGET\" -format UDBZ \"$TARGET\".dmg\n    fi\n```\n\nCould you update the patch, or should I do it (I didn't because otherwise I couldn't be the reviewer, could I)?",
    "created_at": "2010-02-14T13:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66905",
    "user": "GeorgSWeber"
}
```

After the patch "trac_7765-dmg.patch" from seven weeks ago, the functionality is as (I think) it should be, i.e. unless an environment variable "SAGE_APP_DMG" both exists and has a value of "no", the dmg will be built. Good.

As for the documentation/printout statements, one might think of something along the following lines to be more verbose:

``` 
    if [ "$SAGE_APP_DMG" = "no" ]; then
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
        echo '(or to anything else but the current SAGE_APP_DMG=no,'
        echo ' or completely unset SAGE_APP_DMG)'
    else
        echo "Creating dmg"
        echo '(If you don't wish to create a disk image please set'
        echo ' SAGE_APP_DMG=no)'
        DYLD_LIBRARY_PATH=$SAGE_ORIG_DYLD_LIBRARY_PATH; export DYLD_LIBRARY_PATH
        hdiutil create -srcfolder "$TARGET" -format UDBZ "$TARGET".dmg
    fi
```

Could you update the patch, or should I do it (I didn't because otherwise I couldn't be the reviewer, could I)?



---

archive/issue_comments_066906.json:
```json
{
    "body": "Attachment [trac_7765-dmg.2.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg.2.patch) by @gvol created at 2010-03-07 15:54:25\n\nSorry about that, mabshoff mentioned that making a dmg should be optional since it takes so long e.g. when testing things.  For some reason I took that to mean not the default.  I created a new patch trac_7765-dmg.2.patch so that either of you can referee it.",
    "created_at": "2010-03-07T15:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66906",
    "user": "@gvol"
}
```

Attachment [trac_7765-dmg.2.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg.2.patch) by @gvol created at 2010-03-07 15:54:25

Sorry about that, mabshoff mentioned that making a dmg should be optional since it takes so long e.g. when testing things.  For some reason I took that to mean not the default.  I created a new patch trac_7765-dmg.2.patch so that either of you can referee it.



---

archive/issue_comments_066907.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-07T15:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66907",
    "user": "@gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066908.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-22T07:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66908",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066909.json:
```json
{
    "body": "I see one problem with this script that no one has yet noticed, and perhaps was William's initial question about it. \n\n```\nMoving final distribution file to /Users/.../sage-4.3.5/dist\nmv: rename sage-Sage2-PowerMacintosh-Darwin.* to /Users/.../sage-4.3.5/dist/sage-Sage2-PowerMacintosh-Darwin.*: No such file or directory\n```\n\nRight!  Because\n\n```\nif [ \"$UNAME\" = \"Darwin\" ]; then\n...\n    else\n        echo 'If you wish to create a disk image please set'\n        echo 'SAGE_APP_DMG=yes'\n        echo '(or to anything else but the current SAGE_APP_DMG=no,'\n        echo ' or completely unset SAGE_APP_DMG)'\n    fi\nelse\n    echo \"Creating tar.gz\"\n    tar zcvf \"$TARGET\".tar.gz \"$TARGET\"\nfi\n```\n\nbut\n\n```\necho \"Moving final distribution file to $SAGE_ROOT/dist\"\n\nmv $TARGET $SAGE_ROOT/dist/\nmv $TARGET.* $SAGE_ROOT/dist/\n```\n\nSo the point is that when SAGE_APP_DMG=no, not only is there not a DMG, but not even a .tgz file is created!  Which yields the weird error message I always see from the very last line.\n\nHowever, testing once again showed that default behavior is now .dmg creation (as it was with the other version of the patch), and none of this should affect anything other than Darwin, so we just have to make sure that we add the right lines to the \"else\" above and then this should be good to go.  I'll do that in the morning, and then (sigh) we'll need yet another review...",
    "created_at": "2010-04-22T07:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66909",
    "user": "@kcrisman"
}
```

I see one problem with this script that no one has yet noticed, and perhaps was William's initial question about it. 

```
Moving final distribution file to /Users/.../sage-4.3.5/dist
mv: rename sage-Sage2-PowerMacintosh-Darwin.* to /Users/.../sage-4.3.5/dist/sage-Sage2-PowerMacintosh-Darwin.*: No such file or directory
```

Right!  Because

```
if [ "$UNAME" = "Darwin" ]; then
...
    else
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
        echo '(or to anything else but the current SAGE_APP_DMG=no,'
        echo ' or completely unset SAGE_APP_DMG)'
    fi
else
    echo "Creating tar.gz"
    tar zcvf "$TARGET".tar.gz "$TARGET"
fi
```

but

```
echo "Moving final distribution file to $SAGE_ROOT/dist"

mv $TARGET $SAGE_ROOT/dist/
mv $TARGET.* $SAGE_ROOT/dist/
```

So the point is that when SAGE_APP_DMG=no, not only is there not a DMG, but not even a .tgz file is created!  Which yields the weird error message I always see from the very last line.

However, testing once again showed that default behavior is now .dmg creation (as it was with the other version of the patch), and none of this should affect anything other than Darwin, so we just have to make sure that we add the right lines to the "else" above and then this should be good to go.  I'll do that in the morning, and then (sigh) we'll need yet another review...



---

archive/issue_comments_066910.json:
```json
{
    "body": "Attachment [trac_7765-dmg-or-tgz.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg-or-tgz.patch) by @kcrisman created at 2010-04-22 12:52:51\n\nBased on Sage 4.3.5 - apply only this to scripts repo",
    "created_at": "2010-04-22T12:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66910",
    "user": "@kcrisman"
}
```

Attachment [trac_7765-dmg-or-tgz.patch](tarball://root/attachments/some-uuid/ticket7765/trac_7765-dmg-or-tgz.patch) by @kcrisman created at 2010-04-22 12:52:51

Based on Sage 4.3.5 - apply only this to scripts repo



---

archive/issue_comments_066911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-22T12:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66911",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066912.json:
```json
{
    "body": "Okay, ready for review. Downgrading to critical since it's been four months.",
    "created_at": "2010-04-22T12:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66912",
    "user": "@kcrisman"
}
```

Okay, ready for review. Downgrading to critical since it's been four months.



---

archive/issue_comments_066913.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-04-22T12:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66913",
    "user": "@kcrisman"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_066914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T00:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7765#issuecomment-66914",
    "user": "@williamstein"
}
```

Resolution: fixed
