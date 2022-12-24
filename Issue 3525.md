# Issue 3525: notebook -- new welcome page

archive/issues_003525.json:
```json
{
    "body": "Assignee: was\n\nTake the static page at http://timothyclemans.com/nb_homepage/ and merge it into the Sage Notebook code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3525\n\n",
    "created_at": "2008-06-28T06:40:47Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- new welcome page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3525",
    "user": "TimothyClemans"
}
```
Assignee: was

Take the static page at http://timothyclemans.com/nb_homepage/ and merge it into the Sage Notebook code.

Issue created by migration from https://trac.sagemath.org/ticket/3525





---

archive/issue_comments_024850.json:
```json
{
    "body": "Attachment [extcode-3525.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525.patch) by TimothyClemans created at 2008-06-28 08:06:35",
    "created_at": "2008-06-28T08:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24850",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3525.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525.patch) by TimothyClemans created at 2008-06-28 08:06:35



---

archive/issue_comments_024851.json:
```json
{
    "body": "Changing component from number theory to notebook.",
    "created_at": "2008-06-28T08:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24851",
    "user": "TimothyClemans"
}
```

Changing component from number theory to notebook.



---

archive/issue_comments_024852.json:
```json
{
    "body": "Changing assignee from was to TimothyClemans.",
    "created_at": "2008-06-28T08:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24852",
    "user": "TimothyClemans"
}
```

Changing assignee from was to TimothyClemans.



---

archive/issue_comments_024853.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T08:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24853",
    "user": "TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024854.json:
```json
{
    "body": "Attachment [sage-3525.patch](tarball://root/attachments/some-uuid/ticket3525/sage-3525.patch) by TimothyClemans created at 2008-06-28 08:07:56",
    "created_at": "2008-06-28T08:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24854",
    "user": "TimothyClemans"
}
```

Attachment [sage-3525.patch](tarball://root/attachments/some-uuid/ticket3525/sage-3525.patch) by TimothyClemans created at 2008-06-28 08:07:56



---

archive/issue_comments_024855.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-28T08:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24855",
    "user": "TimothyClemans"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_024856.json:
```json
{
    "body": "From Harald Schilly:\n\n\n```\nLooks good, yes. Just small remarks what I would change...\n\n1) The border around the sign-in formular is thin. Why not the same as\nthose two below? I would suggest to make all three borders small...\n\n2) The top header is an image. The serif-italic letters don't look\nvery well on my screen. (no subpixel hinting compared to directly\nrendered italic letters on my lcd) .. I would suggest to not use an\nimage, just the text string with a fixed font size (16pt?, italic,\nserif) and absolute placement.\n\n3) The forgot password page does not exist. I think, it should look\nthe same, except the login box and the middle content replaced by an\nexplanation and so on.\n\n4) maybe less screenshots (just a 3x2 matrix) but with larger images?\nso that someone could see more!\n\n5) it's not xhtml valid\nI strongly suggest to use xhtml transitional, since this is better for\ncompatibility and browsers like ie6 work better with that. xhtml\nstrict is just some sort of a more theoretical wish that will never\ncome true ;)\nbut anyways, ending a formular input tag with /> is not ok. browsers\ndon't understand real xml ...\n\n6) maybe more margin-borders on the left and right side of the middle\ncontent, to give everything a bit more \"air\" so that it looks less\ntight...\n\ngreetings Harald\n\n\nOn Sat, Jun 28, 2008 at 08:38, William Stein <wstein@gmail.com> wrote:\n> What do you think of\n>\n> http://timothyclemans.com/nb_homepage/\n>\n> --\n> William Stein\n> Associate Professor of Mathematics\n> University of Washington\n> http://wstein.org\n>\n```\n",
    "created_at": "2008-06-28T10:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24856",
    "user": "TimothyClemans"
}
```

From Harald Schilly:


```
Looks good, yes. Just small remarks what I would change...

1) The border around the sign-in formular is thin. Why not the same as
those two below? I would suggest to make all three borders small...

2) The top header is an image. The serif-italic letters don't look
very well on my screen. (no subpixel hinting compared to directly
rendered italic letters on my lcd) .. I would suggest to not use an
image, just the text string with a fixed font size (16pt?, italic,
serif) and absolute placement.

3) The forgot password page does not exist. I think, it should look
the same, except the login box and the middle content replaced by an
explanation and so on.

4) maybe less screenshots (just a 3x2 matrix) but with larger images?
so that someone could see more!

5) it's not xhtml valid
I strongly suggest to use xhtml transitional, since this is better for
compatibility and browsers like ie6 work better with that. xhtml
strict is just some sort of a more theoretical wish that will never
come true ;)
but anyways, ending a formular input tag with /> is not ok. browsers
don't understand real xml ...

6) maybe more margin-borders on the left and right side of the middle
content, to give everything a bit more "air" so that it looks less
tight...

greetings Harald


On Sat, Jun 28, 2008 at 08:38, William Stein <wstein@gmail.com> wrote:
> What do you think of
>
> http://timothyclemans.com/nb_homepage/
>
> --
> William Stein
> Associate Professor of Mathematics
> University of Washington
> http://wstein.org
>
```




---

archive/issue_comments_024857.json:
```json
{
    "body": "used Tidy to deal with point 5 of Harald's criticism",
    "created_at": "2008-06-28T10:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24857",
    "user": "TimothyClemans"
}
```

used Tidy to deal with point 5 of Harald's criticism



---

archive/issue_comments_024858.json:
```json
{
    "body": "Attachment [extcode-3525_2.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_2.patch) by was created at 2008-06-28 12:30:57",
    "created_at": "2008-06-28T12:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24858",
    "user": "was"
}
```

Attachment [extcode-3525_2.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_2.patch) by was created at 2008-06-28 12:30:57



---

archive/issue_comments_024859.json:
```json
{
    "body": "Regarding the negative review could you tell me if you want all of Harald's suggestions implemented? \n\n1) I can do easily by switching in the css which background is called for a:link and a:hover\n\n2) Maybe do this in another ticket if others also complain\n\n3) A very minimalistic \"account recovery\" page will be in sage-3.0.4. Anything regarding it should be a different ticket\n\n4) I don't want to change them because A) I like it the way it is B) it would be very time consuming for me\n\n5) Done\n\n6) Sure",
    "created_at": "2008-06-28T14:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24859",
    "user": "TimothyClemans"
}
```

Regarding the negative review could you tell me if you want all of Harald's suggestions implemented? 

1) I can do easily by switching in the css which background is called for a:link and a:hover

2) Maybe do this in another ticket if others also complain

3) A very minimalistic "account recovery" page will be in sage-3.0.4. Anything regarding it should be a different ticket

4) I don't want to change them because A) I like it the way it is B) it would be very time consuming for me

5) Done

6) Sure



---

archive/issue_comments_024860.json:
```json
{
    "body": "For a positive review it is enough to do 1, 5, 6.",
    "created_at": "2008-06-28T14:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24860",
    "user": "was"
}
```

For a positive review it is enough to do 1, 5, 6.



---

archive/issue_comments_024861.json:
```json
{
    "body": "Attachment [extcode-3525_3.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_3.patch) by TimothyClemans created at 2008-06-28 14:52:42\n\nmargins increased blue line under interactive computer programming changed to reflect new margins\n\nBorder for \"Sign up\" and \"Published worksheets\" is now 1px.",
    "created_at": "2008-06-28T14:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24861",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3525_3.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_3.patch) by TimothyClemans created at 2008-06-28 14:52:42

margins increased blue line under interactive computer programming changed to reflect new margins

Border for "Sign up" and "Published worksheets" is now 1px.



---

archive/issue_comments_024862.json:
```json
{
    "body": "Attachment [extcode-3525_4.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_4.patch) by TimothyClemans created at 2008-06-28 14:58:59\n\nforgot to change which images are preloaded (the ones for signup and published worksheets)",
    "created_at": "2008-06-28T14:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24862",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3525_4.patch](tarball://root/attachments/some-uuid/ticket3525/extcode-3525_4.patch) by TimothyClemans created at 2008-06-28 14:58:59

forgot to change which images are preloaded (the ones for signup and published worksheets)



---

archive/issue_comments_024863.json:
```json
{
    "body": "In extcode-3525_3.patch I see \n\n\n```\ndiff -r 84e3731cc21b -r 40c4b0aa9491 notebook/images/head.gif\nBinary file notebook/images/head.gif has changed\n```\n\n\nIs the actual image stored in the patch? If not then how do I put package images for inclusion?",
    "created_at": "2008-06-28T21:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24863",
    "user": "TimothyClemans"
}
```

In extcode-3525_3.patch I see 


```
diff -r 84e3731cc21b -r 40c4b0aa9491 notebook/images/head.gif
Binary file notebook/images/head.gif has changed
```


Is the actual image stored in the patch? If not then how do I put package images for inclusion?



---

archive/issue_comments_024864.json:
```json
{
    "body": "extcode_combined.patch is a git style patch that should contained the required images",
    "created_at": "2008-07-06T02:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24864",
    "user": "TimothyClemans"
}
```

extcode_combined.patch is a git style patch that should contained the required images



---

archive/issue_comments_024865.json:
```json
{
    "body": "Attachment [extcode_combined.patch](tarball://root/attachments/some-uuid/ticket3525/extcode_combined.patch) by TimothyClemans created at 2008-07-07 22:45:15\n\nThe combined extcode patch is mess. Various fixes aren't in the patch ...",
    "created_at": "2008-07-07T22:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24865",
    "user": "TimothyClemans"
}
```

Attachment [extcode_combined.patch](tarball://root/attachments/some-uuid/ticket3525/extcode_combined.patch) by TimothyClemans created at 2008-07-07 22:45:15

The combined extcode patch is mess. Various fixes aren't in the patch ...



---

archive/issue_comments_024866.json:
```json
{
    "body": "What is the status of this patch, Timothy?",
    "created_at": "2010-08-27T15:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24866",
    "user": "jason"
}
```

What is the status of this patch, Timothy?



---

archive/issue_comments_024867.json:
```json
{
    "body": "Changing keywords from \"editor_wstein\" to \"editor_wstein, stale\".",
    "created_at": "2010-08-27T15:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24867",
    "user": "jason"
}
```

Changing keywords from "editor_wstein" to "editor_wstein, stale".



---

archive/issue_comments_024868.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-09-17T18:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24868",
    "user": "kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_024869.json:
```json
{
    "body": "This is not a bad idea in general, but at this point the discussion about looks are subsumed into ideas about \"newUI\" and \"themes\" upstream.  Any new welcome page discussion should arrive there.  Sadly, wontfix is probably most appropriate for this six-year-old ticket.",
    "created_at": "2014-09-17T18:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24869",
    "user": "kcrisman"
}
```

This is not a bad idea in general, but at this point the discussion about looks are subsumed into ideas about "newUI" and "themes" upstream.  Any new welcome page discussion should arrive there.  Sadly, wontfix is probably most appropriate for this six-year-old ticket.



---

archive/issue_comments_024870.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-09-18T17:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3525#issuecomment-24870",
    "user": "vbraun"
}
```

Resolution: wontfix
