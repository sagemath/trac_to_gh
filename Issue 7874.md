# Issue 7874: Typeset labels for interact controls

archive/issues_007874.json:
```json
{
    "body": "Assignee: was\n\nCC:  rbeezer\n\nCan we typeset the labels of interact controls\n\n```python\n@interact\ndef test(x=slider(-2,2,1, label='$x^2$')):\n    print \"Doing nothing in an interact\"\n```\n\n?\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/312cab9514bece7c).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7874\n\n",
    "created_at": "2010-01-08T21:34:57Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Typeset labels for interact controls",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7874",
    "user": "mpatel"
}
```
Assignee: was

CC:  rbeezer

Can we typeset the labels of interact controls

```python
@interact
def test(x=slider(-2,2,1, label='$x^2$')):
    print "Doing nothing in an interact"
```

?

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/312cab9514bece7c).

Issue created by migration from https://trac.sagemath.org/ticket/7874





---

archive/issue_comments_068395.json:
```json
{
    "body": "Attachment [trac_7874-typeset_interact_labels.patch](tarball://root/attachments/some-uuid/ticket7874/trac_7874-typeset_interact_labels.patch) by mpatel created at 2010-01-08 21:40:21\n\n`jsMath.Process()` wrapped output text for interacts.  sagenb repo.",
    "created_at": "2010-01-08T21:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68395",
    "user": "mpatel"
}
```

Attachment [trac_7874-typeset_interact_labels.patch](tarball://root/attachments/some-uuid/ticket7874/trac_7874-typeset_interact_labels.patch) by mpatel created at 2010-01-08 21:40:21

`jsMath.Process()` wrapped output text for interacts.  sagenb repo.



---

archive/issue_comments_068396.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-08T21:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68396",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068397.json:
```json
{
    "body": "The attached patch works for me with the example above, but it is *not* extensively tested.",
    "created_at": "2010-01-08T21:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68397",
    "user": "mpatel"
}
```

The attached patch works for me with the example above, but it is *not* extensively tested.



---

archive/issue_comments_068398.json:
```json
{
    "body": "`sage.misc.html.html` `print`s HTML code as a side-effect.  The server captures this as output from the worksheet process, but the position depends, I think, on the order of evaluation.",
    "created_at": "2010-01-08T21:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68398",
    "user": "mpatel"
}
```

`sage.misc.html.html` `print`s HTML code as a side-effect.  The server captures this as output from the worksheet process, but the position depends, I think, on the order of evaluation.



---

archive/issue_comments_068399.json:
```json
{
    "body": "Hi Pat,\n\nThanks for the quick work on this one!  I was going to try to test it with my original purpose.  But I can't seem to find a sagenb repo in my development tree.\n\nWhat does it take to apply and run the patch?  I have a 4.3.1.alpha1 installation and know how to apply patches in /sage/devel.  is it much different?  Do I get everything I need in the Sage source distribution?\n\nThanks,\nRob",
    "created_at": "2010-01-08T22:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68399",
    "user": "rbeezer"
}
```

Hi Pat,

Thanks for the quick work on this one!  I was going to try to test it with my original purpose.  But I can't seem to find a sagenb repo in my development tree.

What does it take to apply and run the patch?  I have a 4.3.1.alpha1 installation and know how to apply patches in /sage/devel.  is it much different?  Do I get everything I need in the Sage source distribution?

Thanks,
Rob



---

archive/issue_comments_068400.json:
```json
{
    "body": "Please see [SageNB's home](http://nb.sagemath.org/) for brief directions.  In particular,\n\n```sh\nmkdir tmp; cd tmp\nwget http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.4.9.spkg\ntar jxvf sagenb-0.4.9.spkg\ncd sagenb-0.4.9/src/sagenb\nsage -hg pull http://boxen.math.washington.edu:8100\nsage -hg update\n```\n\nThen apply the patch, do\n\n```sh\nsage -python setup.py develop\n```\n\nand run the notebook.  (The \"develop\" command, unlike the \"install\" command, just tells `setuptools` to use the current directory as the installation.)  To revert to original version, you can `hg qpop` the patch (if you're using [queues](http://wiki.sagemath.org/MercurialQueues)) or do\n\n```sh\nsage -f sagenb-0.4.9.spkg\n```\n\nPlease let me know, if you have questions.",
    "created_at": "2010-01-08T22:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68400",
    "user": "mpatel"
}
```

Please see [SageNB's home](http://nb.sagemath.org/) for brief directions.  In particular,

```sh
mkdir tmp; cd tmp
wget http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.4.9.spkg
tar jxvf sagenb-0.4.9.spkg
cd sagenb-0.4.9/src/sagenb
sage -hg pull http://boxen.math.washington.edu:8100
sage -hg update
```

Then apply the patch, do

```sh
sage -python setup.py develop
```

and run the notebook.  (The "develop" command, unlike the "install" command, just tells `setuptools` to use the current directory as the installation.)  To revert to original version, you can `hg qpop` the patch (if you're using [queues](http://wiki.sagemath.org/MercurialQueues)) or do

```sh
sage -f sagenb-0.4.9.spkg
```

Please let me know, if you have questions.



---

archive/issue_comments_068401.json:
```json
{
    "body": "Or use `SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg`.",
    "created_at": "2010-01-08T22:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68401",
    "user": "mpatel"
}
```

Or use `SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg`.



---

archive/issue_comments_068402.json:
```json
{
    "body": "Perfect!  Thanks for the primer.  I'll get back to it later today.",
    "created_at": "2010-01-08T22:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68402",
    "user": "rbeezer"
}
```

Perfect!  Thanks for the primer.  I'll get back to it later today.



---

archive/issue_comments_068403.json:
```json
{
    "body": "Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.",
    "created_at": "2010-01-09T00:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68403",
    "user": "mpatel"
}
```

Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.



---

archive/issue_comments_068404.json:
```json
{
    "body": "mpatel,\n\nWorks just fine for me with the interact I was building.  Leads with four sliders all with nice labels.  Screenshot here, and I'll post on sage-devel and sagenb.\n\nThanks - this will make interacts look all the better.\n\nRob",
    "created_at": "2010-01-09T00:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68404",
    "user": "rbeezer"
}
```

mpatel,

Works just fine for me with the interact I was building.  Leads with four sliders all with nice labels.  Screenshot here, and I'll post on sage-devel and sagenb.

Thanks - this will make interacts look all the better.

Rob



---

archive/issue_comments_068405.json:
```json
{
    "body": "Attachment [interact-controls-formatted.png](tarball://root/attachments/some-uuid/ticket7874/interact-controls-formatted.png) by rbeezer created at 2010-01-09 00:52:04\n\nReplying to [comment:7 mpatel]:\n> Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.\n\nYes, to adventurous, no to spare time.  But I think adventure wins.  \n\nBut (this is embarrassing) I've never installed an spkg.  How should I do this so I can back it out again without having a mess on my hands?  ;-)  I don't have anything important to lose, so it won't be a crisis if I screw up.  Can you give me another short primer?\n\nShould have said above: I don't think I know enough to give a review.  But I'm going to go right now and advertise how good the patch is and see if we can get one.\n\nRob",
    "created_at": "2010-01-09T00:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68405",
    "user": "rbeezer"
}
```

Attachment [interact-controls-formatted.png](tarball://root/attachments/some-uuid/ticket7874/interact-controls-formatted.png) by rbeezer created at 2010-01-09 00:52:04

Replying to [comment:7 mpatel]:
> Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.

Yes, to adventurous, no to spare time.  But I think adventure wins.  

But (this is embarrassing) I've never installed an spkg.  How should I do this so I can back it out again without having a mess on my hands?  ;-)  I don't have anything important to lose, so it won't be a crisis if I screw up.  Can you give me another short primer?

Should have said above: I don't think I know enough to give a review.  But I'm going to go right now and advertise how good the patch is and see if we can get one.

Rob



---

archive/issue_comments_068406.json:
```json
{
    "body": "To install any spkg, local or remote, just do, e.g.,\n\n```\nsage -f http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg\n```\n\nTo revert to the \"default\" spkg (or another version), just do, e.g.,\n\n```\nsage -f $SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg\n```\n\n(The default should already be part of the source distribution.)  Actually, `sage -advanced` also gives `sage -i thepackage.spkg` as a way to install an spkg.  The `-f` option forces a reinstall, even if the package is already installed.\n\nAs always, please let me know, if there are questions and/or problems.",
    "created_at": "2010-01-09T01:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68406",
    "user": "mpatel"
}
```

To install any spkg, local or remote, just do, e.g.,

```
sage -f http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg
```

To revert to the "default" spkg (or another version), just do, e.g.,

```
sage -f $SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg
```

(The default should already be part of the source distribution.)  Actually, `sage -advanced` also gives `sage -i thepackage.spkg` as a way to install an spkg.  The `-f` option forces a reinstall, even if the package is already installed.

As always, please let me know, if there are questions and/or problems.



---

archive/issue_comments_068407.json:
```json
{
    "body": "Hmmm... I just tried the first line, but I got an error.  It may be better to download the spkg first and rename it:\n\n```\nwget http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg\nmv sagenb-0.5-7666b2.spkg sagenb-0.5.spkg\nsage -f sagenb-0.5.spkg\n```\n\nI apologize for this.",
    "created_at": "2010-01-09T01:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68407",
    "user": "mpatel"
}
```

Hmmm... I just tried the first line, but I got an error.  It may be better to download the spkg first and rename it:

```
wget http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg
mv sagenb-0.5-7666b2.spkg sagenb-0.5.spkg
sage -f sagenb-0.5.spkg
```

I apologize for this.



---

archive/issue_comments_068408.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\nI thought it was that easy.  ;-)  I'll get to it a bit later this evening.  Thanks.",
    "created_at": "2010-01-09T01:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68408",
    "user": "rbeezer"
}
```

Replying to [comment:10 mpatel]:
I thought it was that easy.  ;-)  I'll get to it a bit later this evening.  Thanks.



---

archive/issue_comments_068409.json:
```json
{
    "body": "The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)",
    "created_at": "2010-01-09T01:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68409",
    "user": "mpatel"
}
```

The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)



---

archive/issue_comments_068410.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)\n\nLooks like the package has been fixed, so no renaming is needed.",
    "created_at": "2010-01-10T06:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68410",
    "user": "rbeezer"
}
```

Replying to [comment:13 mpatel]:
> The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)

Looks like the package has been fixed, so no renaming is needed.



---

archive/issue_comments_068411.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T20:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68411",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068412.json:
```json
{
    "body": "LGTM. Nice work.",
    "created_at": "2010-01-17T20:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68412",
    "user": "timdumol"
}
```

LGTM. Nice work.



---

archive/issue_comments_068413.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68413",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_068414.json:
```json
{
    "body": "The milestone should be sage-4.3.1.",
    "created_at": "2010-01-25T00:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7874#issuecomment-68414",
    "user": "mpatel"
}
```

The milestone should be sage-4.3.1.
