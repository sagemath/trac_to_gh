# Issue 767: animate has cryptic error message when imagemagick is not installed

archive/issues_000767.json:
```json
{
    "body": "Assignee: boothby\n\nwhen creating an animated gif on a system without imagemagick installed, the animate() command  just outputs\n\n\"sh: convert: not found\"\n\ninstead of a more helpful error message (such as, \"please install imagemagick\")\n\nIssue created by migration from https://trac.sagemath.org/ticket/767\n\n",
    "created_at": "2007-09-30T22:11:24Z",
    "labels": [
        "notebook",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "animate has cryptic error message when imagemagick is not installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/767",
    "user": "@bobmoretti"
}
```
Assignee: boothby

when creating an animated gif on a system without imagemagick installed, the animate() command  just outputs

"sh: convert: not found"

instead of a more helpful error message (such as, "please install imagemagick")

Issue created by migration from https://trac.sagemath.org/ticket/767





---

archive/issue_comments_004534.json:
```json
{
    "body": "Attachment [767.patch](tarball://root/attachments/some-uuid/ticket767/767.patch) by @jhpalmieri created at 2008-09-30 16:58:56",
    "created_at": "2008-09-30T16:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4534",
    "user": "@jhpalmieri"
}
```

Attachment [767.patch](tarball://root/attachments/some-uuid/ticket767/767.patch) by @jhpalmieri created at 2008-09-30 16:58:56



---

archive/issue_comments_004535.json:
```json
{
    "body": "Changing keywords from \"\" to \"animate, ImageMagick\".",
    "created_at": "2008-09-30T17:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4535",
    "user": "@jhpalmieri"
}
```

Changing keywords from "" to "animate, ImageMagick".



---

archive/issue_comments_004536.json:
```json
{
    "body": "I'm attaching a patch; it depends on #4216.\n\nWith this patch, if 'convert' is not found, I get an error message like this:\n\n```\n/usr/local/share/sage/local/bin/sage-native-execute: 8: convert: not\nfound\n\nError: ImageMagick does not appear to be installed. Saving an\nanimation to a GIF file or displaying an animation requires\nImageMagick, so please install it and try again.\n\nSee www.imagemagick.org, for example.\n```\n\nSo the first line is cryptic (but could be useful in debugging, if the problem is something other than a missing 'convert'), while the rest of the message is friendlier.",
    "created_at": "2008-09-30T17:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4536",
    "user": "@jhpalmieri"
}
```

I'm attaching a patch; it depends on #4216.

With this patch, if 'convert' is not found, I get an error message like this:

```
/usr/local/share/sage/local/bin/sage-native-execute: 8: convert: not
found

Error: ImageMagick does not appear to be installed. Saving an
animation to a GIF file or displaying an animation requires
ImageMagick, so please install it and try again.

See www.imagemagick.org, for example.
```

So the first line is cryptic (but could be useful in debugging, if the problem is something other than a missing 'convert'), while the rest of the message is friendlier.



---

archive/issue_comments_004537.json:
```json
{
    "body": "Positive review on the patch. One small issue is that the animate.py doctest fails if convert is not installed:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t devel//sage/sage/plot/animate.py \nsage -t  devel/sage/sage/plot/animate.py                    \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/animate.py\", line 59:\n    sage: a.show()\nExpected nothing\nGot:\n    <BLANKLINE>\n    Error: ImageMagick does not appear to be installed. Saving an\n    animation to a GIF file or displaying an animation requires\n    ImageMagick, so please install it and try again.\n    <BLANKLINE>\n    See www.imagemagick.org, for example.\n**********************************************************************\n```\n\n\nOne way around this would be to make the doctest optional. \n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T17:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4537",
    "user": "mabshoff"
}
```

Positive review on the patch. One small issue is that the animate.py doctest fails if convert is not installed:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t devel//sage/sage/plot/animate.py 
sage -t  devel/sage/sage/plot/animate.py                    
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/animate.py", line 59:
    sage: a.show()
Expected nothing
Got:
    <BLANKLINE>
    Error: ImageMagick does not appear to be installed. Saving an
    animation to a GIF file or displaying an animation requires
    ImageMagick, so please install it and try again.
    <BLANKLINE>
    See www.imagemagick.org, for example.
**********************************************************************
```


One way around this would be to make the doctest optional. 

Thoughts?

Cheers,

Michael



---

archive/issue_comments_004538.json:
```json
{
    "body": "> One way around this would be to make the doctest optional. \n\nThis seems okay to me, but I also don't know enough about doctesting to know if there is any other choice.",
    "created_at": "2008-09-30T17:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4538",
    "user": "@jhpalmieri"
}
```

> One way around this would be to make the doctest optional. 

This seems okay to me, but I also don't know enough about doctesting to know if there is any other choice.



---

archive/issue_comments_004539.json:
```json
{
    "body": "Ironically I just checked the animate.py file and all but one of the convert commands are already optional. So I am posting a trivial reviewer patch on top of John's patch and will merge both of them.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T17:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4539",
    "user": "mabshoff"
}
```

Ironically I just checked the animate.py file and all but one of the convert commands are already optional. So I am posting a trivial reviewer patch on top of John's patch and will merge both of them.

Cheers,

Michael



---

archive/issue_comments_004540.json:
```json
{
    "body": "Sorry, I should have checked the doctesting myself. Also, I noticed that several functions (including the one that I patched, `gif`) don't have doctests.  When I get around to it, I will open up another ticket and fix this.\n\nAlso, in my experience, running `animate(...)` doesn't require convert, *showing* the animation does. So we can remove some of the `optional` flags, so that more things are doctested. I may try to do that in the same (soon to be forthcoming?) ticket.",
    "created_at": "2008-09-30T17:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4540",
    "user": "@jhpalmieri"
}
```

Sorry, I should have checked the doctesting myself. Also, I noticed that several functions (including the one that I patched, `gif`) don't have doctests.  When I get around to it, I will open up another ticket and fix this.

Also, in my experience, running `animate(...)` doesn't require convert, *showing* the animation does. So we can remove some of the `optional` flags, so that more things are doctested. I may try to do that in the same (soon to be forthcoming?) ticket.



---

archive/issue_comments_004541.json:
```json
{
    "body": "Attachment [trac_767_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket767/trac_767_doctest_fix.patch) by mabshoff created at 2008-09-30 18:16:46",
    "created_at": "2008-09-30T18:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4541",
    "user": "mabshoff"
}
```

Attachment [trac_767_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket767/trac_767_doctest_fix.patch) by mabshoff created at 2008-09-30 18:16:46



---

archive/issue_comments_004542.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-30T18:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4542",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_004543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-30T18:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/767#issuecomment-4543",
    "user": "mabshoff"
}
```

Resolution: fixed
