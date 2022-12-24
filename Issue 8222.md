# Issue 8222: sagenb -- misc improvements to the notebook graph editor

archive/issues_008222.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @williamstein @fchapoton\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8222\n\n",
    "created_at": "2010-02-09T20:04:59Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sagenb -- misc improvements to the notebook graph editor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8222",
    "user": "@williamstein"
}
```
Assignee: @rlmill

CC:  @williamstein @fchapoton



Issue created by migration from https://trac.sagemath.org/ticket/8222





---

archive/issue_comments_072565.json:
```json
{
    "body": "this is a very ugly first draft",
    "created_at": "2010-02-09T20:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72565",
    "user": "kevinc"
}
```

this is a very ugly first draft



---

archive/issue_comments_072566.json:
```json
{
    "body": "Attachment [8222.patch](tarball://root/attachments/some-uuid/ticket8222/8222.patch) by kevinc created at 2010-03-09 19:46:00\n\na quick test (gets reverted in following patch)",
    "created_at": "2010-03-09T19:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72566",
    "user": "kevinc"
}
```

Attachment [8222.patch](tarball://root/attachments/some-uuid/ticket8222/8222.patch) by kevinc created at 2010-03-09 19:46:00

a quick test (gets reverted in following patch)



---

archive/issue_comments_072567.json:
```json
{
    "body": "Attachment [8222-part2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-part2.patch) by kevinc created at 2010-03-09 19:47:35\n\ncleaned up code, added orientation slider and auto maximize checkbox",
    "created_at": "2010-03-09T19:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72567",
    "user": "kevinc"
}
```

Attachment [8222-part2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-part2.patch) by kevinc created at 2010-03-09 19:47:35

cleaned up code, added orientation slider and auto maximize checkbox



---

archive/issue_comments_072568.json:
```json
{
    "body": "Attachment [8222-part4.patch](tarball://root/attachments/some-uuid/ticket8222/8222-part4.patch) by kevinc created at 2010-03-09 20:11:50\n\nFixed crashes when calling graph_editor for graphs with multiple components or fewer than 4 vertices, increased graph editor size.",
    "created_at": "2010-03-09T20:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72568",
    "user": "kevinc"
}
```

Attachment [8222-part4.patch](tarball://root/attachments/some-uuid/ticket8222/8222-part4.patch) by kevinc created at 2010-03-09 20:11:50

Fixed crashes when calling graph_editor for graphs with multiple components or fewer than 4 vertices, increased graph editor size.



---

archive/issue_comments_072569.json:
```json
{
    "body": "I added 8222.patch but then both 8222-part2.patch and 8222-part3.patch failed. Maybe I am doing something wrong?!? \n\nKevin, can you make one big patch (here is how to do that http://stackoverflow.com/questions/1224379/exporting-mercurial-patch-against-an-old-revision).\n\nRado",
    "created_at": "2010-03-21T05:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72569",
    "user": "rkirov"
}
```

I added 8222.patch but then both 8222-part2.patch and 8222-part3.patch failed. Maybe I am doing something wrong?!? 

Kevin, can you make one big patch (here is how to do that http://stackoverflow.com/questions/1224379/exporting-mercurial-patch-against-an-old-revision).

Rado



---

archive/issue_comments_072570.json:
```json
{
    "body": "Alright got it to work. I am uploading a big patch that contains part1,2,3 for the sagenb spkg. Part4 still needs to be applied separately to the sage tree.\n\nEverything looks great, I will post a proper review tomorrow.",
    "created_at": "2010-03-21T05:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72570",
    "user": "rkirov"
}
```

Alright got it to work. I am uploading a big patch that contains part1,2,3 for the sagenb spkg. Part4 still needs to be applied separately to the sage tree.

Everything looks great, I will post a proper review tomorrow.



---

archive/issue_comments_072571.json:
```json
{
    "body": "contains part1,2,3 of kevin's patches",
    "created_at": "2010-03-21T06:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72571",
    "user": "rkirov"
}
```

contains part1,2,3 of kevin's patches



---

archive/issue_comments_072572.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-22T00:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72572",
    "user": "rkirov"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_072573.json:
```json
{
    "body": "Attachment [8222-big.patch](tarball://root/attachments/some-uuid/ticket8222/8222-big.patch) by rkirov created at 2010-03-22 00:08:07\n\nGreat work! I loved the spring-electric layout with auto-max (that's how I imagined it all along). Everything worked as expect, so the patch is basically ready to go. However, since we are making basically an User Interface, I have some comments on the design decisions.\n\nI am mostly guided by the mantra that passing UI decisions to the user is not a solution. We should man up and fix the most useful behavior that 99% of users will use (and maybe add the sliders hidden behind a \"tweak\" button or skip them all together).\n\n\n- Correct me if wrong but Live with auto-max, spring-el. and default sliders give exactly what I expect on 99% of the graphs. I suggest we make this default (and get rid or hide everything else).\n\n\n- Similarly, I see no reason for live behavior that shoots vertices out of screen. Link auto-max along with live. At the same time, when graph is paused (not live) auto-max should be off.\n\n\n- Numbering for vertices should be off by default (graph theorists seldom number their vertices).\n\n\n- I see only two useful vertex sizes, one for unnumbered vertices and one for numbered. The vertex size slider can be skipped (or hidder by \"tweaks\" button).\n\n\n- Unnumbered vertices should be filled black.\n\n\n- There should be a warning (use JS confirm) with circle layout, since it can potentially destroy a carefully planned layout and there is no undo.\n\nRado",
    "created_at": "2010-03-22T00:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72573",
    "user": "rkirov"
}
```

Attachment [8222-big.patch](tarball://root/attachments/some-uuid/ticket8222/8222-big.patch) by rkirov created at 2010-03-22 00:08:07

Great work! I loved the spring-electric layout with auto-max (that's how I imagined it all along). Everything worked as expect, so the patch is basically ready to go. However, since we are making basically an User Interface, I have some comments on the design decisions.

I am mostly guided by the mantra that passing UI decisions to the user is not a solution. We should man up and fix the most useful behavior that 99% of users will use (and maybe add the sliders hidden behind a "tweak" button or skip them all together).


- Correct me if wrong but Live with auto-max, spring-el. and default sliders give exactly what I expect on 99% of the graphs. I suggest we make this default (and get rid or hide everything else).


- Similarly, I see no reason for live behavior that shoots vertices out of screen. Link auto-max along with live. At the same time, when graph is paused (not live) auto-max should be off.


- Numbering for vertices should be off by default (graph theorists seldom number their vertices).


- I see only two useful vertex sizes, one for unnumbered vertices and one for numbered. The vertex size slider can be skipped (or hidder by "tweaks" button).


- Unnumbered vertices should be filled black.


- There should be a warning (use JS confirm) with circle layout, since it can potentially destroy a carefully planned layout and there is no undo.

Rado



---

archive/issue_comments_072574.json:
```json
{
    "body": "I have implemented my vision (all of the comments above) at http://www.math.uiuc.edu/~rkirov2/js-graph-editor/ and also at the repo http://bitbucket.org/radokirov/js-graph-editor .",
    "created_at": "2010-03-22T20:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72574",
    "user": "rkirov"
}
```

I have implemented my vision (all of the comments above) at http://www.math.uiuc.edu/~rkirov2/js-graph-editor/ and also at the repo http://bitbucket.org/radokirov/js-graph-editor .



---

archive/issue_comments_072575.json:
```json
{
    "body": "Attachment [8222-sagenb.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb.patch) by rkirov created at 2010-03-23 04:53:32\n\ncontains kevin's code, my improvements and the new processing library.",
    "created_at": "2010-03-23T04:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72575",
    "user": "rkirov"
}
```

Attachment [8222-sagenb.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb.patch) by rkirov created at 2010-03-23 04:53:32

contains kevin's code, my improvements and the new processing library.



---

archive/issue_comments_072576.json:
```json
{
    "body": "Attachment [8222-sage.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sage.patch) by rkirov created at 2010-03-23 04:54:23\n\ncontains kevin's patch, and my JSON-fication of the graph editor code",
    "created_at": "2010-03-23T04:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72576",
    "user": "rkirov"
}
```

Attachment [8222-sage.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sage.patch) by rkirov created at 2010-03-23 04:54:23

contains kevin's patch, and my JSON-fication of the graph editor code



---

archive/issue_comments_072577.json:
```json
{
    "body": "I tried applying 8222-sagenb.patch and 8222-sage.patch to 4.3.4.  The \"sage\" patch applied fine, but I got several failures with the sagenb patch.\n\nFinding no hg repo for the notebook I initiated one where I thought it belonged, at\n\n`local/lib/python2.6/site-packages/sagenb-0.7.<something>-py2.6.egg`\n\n(I can't recall the version number on the notebook and am not on the right machine).\n\nDo I need to install the development version of the notebook? (I've done this before, the drill with python setup.py -develop......)  Or do I need to apply more than just the two patches?\n\nAnyway, any guidance in testing this on a stock Sage install would be welcome.\n\nThanks,\nRob",
    "created_at": "2010-03-26T17:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72577",
    "user": "@rbeezer"
}
```

I tried applying 8222-sagenb.patch and 8222-sage.patch to 4.3.4.  The "sage" patch applied fine, but I got several failures with the sagenb patch.

Finding no hg repo for the notebook I initiated one where I thought it belonged, at

`local/lib/python2.6/site-packages/sagenb-0.7.<something>-py2.6.egg`

(I can't recall the version number on the notebook and am not on the right machine).

Do I need to install the development version of the notebook? (I've done this before, the drill with python setup.py -develop......)  Or do I need to apply more than just the two patches?

Anyway, any guidance in testing this on a stock Sage install would be welcome.

Thanks,
Rob



---

archive/issue_comments_072578.json:
```json
{
    "body": "due to complaint I made replacement for sagenb-big patch. Based on sagenb-0.7.5.3",
    "created_at": "2010-03-26T21:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72578",
    "user": "rkirov"
}
```

due to complaint I made replacement for sagenb-big patch. Based on sagenb-0.7.5.3



---

archive/issue_comments_072579.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-26T21:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72579",
    "user": "rkirov"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072580.json:
```json
{
    "body": "Attachment [8222-sagenb-mega.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb-mega.patch) by rkirov created at 2010-03-26 21:09:35\n\nHi Rob,\n\nYou are the second person complaining for the sagenb patch so I probably made the wrong patch. So I erased my sagenb folder, pasted the new code and made a new patch. Try 8222-sagenb-mega.patch. It has everything to make the graph_editor look like the one on my website. Also has fix for the loop bug you found, which the old one didn't have.\n\nThere is a hg repo for the notebook, you don't need to recreate anything. Just extract and go to /sagenb-0.7.5.3/src/sagenb . Now all your \"hg patch\" commands should work.\n\nHere is a summary of everything needed to make this run:\n1) apply 8222-sage.patch to Sage.\n2) untar sagenb (with tar -xvf sagenb-0.7.5.3.spgk)\n3) apply 8222-sagenb-mega.patch in sagenb-0.7.5.3/src/sagenb with \"hg patch 8222-sagenb-mega.patch\"\n4) run SAGEPATH/sage -python setup.py -develop in sagenb-0.7.5.3/src/sagenb\n5) run sage and enjoy!\n\nRado",
    "created_at": "2010-03-26T21:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72580",
    "user": "rkirov"
}
```

Attachment [8222-sagenb-mega.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb-mega.patch) by rkirov created at 2010-03-26 21:09:35

Hi Rob,

You are the second person complaining for the sagenb patch so I probably made the wrong patch. So I erased my sagenb folder, pasted the new code and made a new patch. Try 8222-sagenb-mega.patch. It has everything to make the graph_editor look like the one on my website. Also has fix for the loop bug you found, which the old one didn't have.

There is a hg repo for the notebook, you don't need to recreate anything. Just extract and go to /sagenb-0.7.5.3/src/sagenb . Now all your "hg patch" commands should work.

Here is a summary of everything needed to make this run:
1) apply 8222-sage.patch to Sage.
2) untar sagenb (with tar -xvf sagenb-0.7.5.3.spgk)
3) apply 8222-sagenb-mega.patch in sagenb-0.7.5.3/src/sagenb with "hg patch 8222-sagenb-mega.patch"
4) run SAGEPATH/sage -python setup.py -develop in sagenb-0.7.5.3/src/sagenb
5) run sage and enjoy!

Rado



---

archive/issue_comments_072581.json:
```json
{
    "body": "Hi Rado,\n\nThanks - those instructions worked just fine for me and it is running nicely.  Comments later after some testing.\n\nFor anybody else - two minor items - I could only find 0.7.5.1 in the directory specified on the notebook project page (which is what I used), and step (4) doesn't have a dash before \"develop\".\n\nRob",
    "created_at": "2010-03-27T04:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72581",
    "user": "@rbeezer"
}
```

Hi Rado,

Thanks - those instructions worked just fine for me and it is running nicely.  Comments later after some testing.

For anybody else - two minor items - I could only find 0.7.5.1 in the directory specified on the notebook project page (which is what I used), and step (4) doesn't have a dash before "develop".

Rob



---

archive/issue_comments_072582.json:
```json
{
    "body": "Hi Rado and Kevin,\n\nBeen experimenting with this over the weekend - very, very nice.  I think I've learned enough about the pieces to be able to review this now.\n\nWere you going to\n\n(1) disable red edges?\n\n(2) turn-off auto-maximize?\n\nOne suggestion I have right now (without having done a 100% thorough review) is to perhaps check very early on to see if the input is even a graph?  Right now totally wrong input results in a traceback on getting the position dictionary (which is not very informative to the newbie).\n\nLet me know the status of this (ie will you be making more changes?) and I'll see about doing a careful review.  I've got some longer-term, broader comments that I'll post to sage-devel right now.\n\nRob",
    "created_at": "2010-03-28T22:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72582",
    "user": "@rbeezer"
}
```

Hi Rado and Kevin,

Been experimenting with this over the weekend - very, very nice.  I think I've learned enough about the pieces to be able to review this now.

Were you going to

(1) disable red edges?

(2) turn-off auto-maximize?

One suggestion I have right now (without having done a 100% thorough review) is to perhaps check very early on to see if the input is even a graph?  Right now totally wrong input results in a traceback on getting the position dictionary (which is not very informative to the newbie).

Let me know the status of this (ie will you be making more changes?) and I'll see about doing a careful review.  I've got some longer-term, broader comments that I'll post to sage-devel right now.

Rob



---

archive/issue_comments_072583.json:
```json
{
    "body": "The line defining graph_to_json is duplicate in graph_editor.py, that's all.",
    "created_at": "2010-03-31T12:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72583",
    "user": "pang"
}
```

The line defining graph_to_json is duplicate in graph_editor.py, that's all.



---

archive/issue_comments_072584.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-03T17:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72584",
    "user": "rkirov"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072585.json:
```json
{
    "body": "Attachment [8222-removed-duplicate-line.patch](tarball://root/attachments/some-uuid/ticket8222/8222-removed-duplicate-line.patch) by rkirov created at 2010-04-03 17:14:07\n\nHi Rob,\n\nI was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. You are right we should add some type checking.\n\nI wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? If nobody else, says something, I will just make final patch with:\n\n1) removed red-edges\n2) removed buttons for maximize and auto-maximize\n3) switch delete to keyboard 'd'\n\non the sage side:\n\n1) add type checking\n2) incorporate pang's patch (thanks for patch, that was very sloppy of me)\n\nThen Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.",
    "created_at": "2010-04-03T17:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72585",
    "user": "rkirov"
}
```

Attachment [8222-removed-duplicate-line.patch](tarball://root/attachments/some-uuid/ticket8222/8222-removed-duplicate-line.patch) by rkirov created at 2010-04-03 17:14:07

Hi Rob,

I was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. You are right we should add some type checking.

I wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? If nobody else, says something, I will just make final patch with:

1) removed red-edges
2) removed buttons for maximize and auto-maximize
3) switch delete to keyboard 'd'

on the sage side:

1) add type checking
2) incorporate pang's patch (thanks for patch, that was very sloppy of me)

Then Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.



---

archive/issue_comments_072586.json:
```json
{
    "body": "Replying to [comment:10 rkirov]:\n> Hi Rob,\n> \n> I was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. \n\nI'd suggest proceeding with changes and a review, and hope Kevin checks-in if he feels strongly.  If there is a change he's not happy with it, it could get reverted before being merged (or afterward).  I won't do a review immediately (but will do it soon), so he'll have a chance to weigh-in if he'd like.  \n\n> I wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? \n\nIt struck me that it was the source of a lot of wild behavior, without being crucial to proper functioning, so yes, I'd vote for leaving it out for right now.  It could come back later in a different form.\n\n> If nobody else, says something, I will just make final patch with:\n> \n> 1) removed red-edges\n> 2) removed buttons for maximize and auto-maximize\n> 3) switch delete to keyboard 'd'\n> \n> on the sage side:\n> \n> 1) add type checking\n> 2) incorporate pang's patch (thanks for patch, that was very sloppy of me)\n> \n> Then Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.\n\nSounds like a good plan.\n\nRob",
    "created_at": "2010-04-03T18:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72586",
    "user": "@rbeezer"
}
```

Replying to [comment:10 rkirov]:
> Hi Rob,
> 
> I was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. 

I'd suggest proceeding with changes and a review, and hope Kevin checks-in if he feels strongly.  If there is a change he's not happy with it, it could get reverted before being merged (or afterward).  I won't do a review immediately (but will do it soon), so he'll have a chance to weigh-in if he'd like.  

> I wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? 

It struck me that it was the source of a lot of wild behavior, without being crucial to proper functioning, so yes, I'd vote for leaving it out for right now.  It could come back later in a different form.

> If nobody else, says something, I will just make final patch with:
> 
> 1) removed red-edges
> 2) removed buttons for maximize and auto-maximize
> 3) switch delete to keyboard 'd'
> 
> on the sage side:
> 
> 1) add type checking
> 2) incorporate pang's patch (thanks for patch, that was very sloppy of me)
> 
> Then Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.

Sounds like a good plan.

Rob



---

archive/issue_comments_072587.json:
```json
{
    "body": "Attachment [8222-sage-2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sage-2.patch) by rkirov created at 2010-04-04 07:36:06\n\nrequires 8222-sage.patch contains type check and pang's patch",
    "created_at": "2010-04-04T07:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72587",
    "user": "rkirov"
}
```

Attachment [8222-sage-2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sage-2.patch) by rkirov created at 2010-04-04 07:36:06

requires 8222-sage.patch contains type check and pang's patch



---

archive/issue_comments_072588.json:
```json
{
    "body": "requires 8222-sagenb-mega.patch , has rob's suggested improvements",
    "created_at": "2010-04-04T07:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72588",
    "user": "rkirov"
}
```

requires 8222-sagenb-mega.patch , has rob's suggested improvements



---

archive/issue_comments_072589.json:
```json
{
    "body": "Attachment [8222-sagenb-2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb-2.patch) by rkirov created at 2010-04-04 07:41:30\n\nall ready for review",
    "created_at": "2010-04-04T07:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72589",
    "user": "rkirov"
}
```

Attachment [8222-sagenb-2.patch](tarball://root/attachments/some-uuid/ticket8222/8222-sagenb-2.patch) by rkirov created at 2010-04-04 07:41:30

all ready for review



---

archive/issue_comments_072590.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-04T07:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72590",
    "user": "rkirov"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072591.json:
```json
{
    "body": "Dialog string change",
    "created_at": "2010-04-15T05:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72591",
    "user": "@rbeezer"
}
```

Dialog string change



---

archive/issue_comments_072592.json:
```json
{
    "body": "Attachment [trac_8222-reviewer.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-reviewer.patch) by @rbeezer created at 2010-04-15 05:28:54\n\nAll-in-one patch for notebook code",
    "created_at": "2010-04-15T05:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72592",
    "user": "@rbeezer"
}
```

Attachment [trac_8222-reviewer.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-reviewer.patch) by @rbeezer created at 2010-04-15 05:28:54

All-in-one patch for notebook code



---

archive/issue_comments_072593.json:
```json
{
    "body": "Attachment [trac_8222-sagenb-graph-editor.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-sagenb-graph-editor.patch) by @rbeezer created at 2010-04-15 05:29:31\n\nAll-in-one patch for sage library",
    "created_at": "2010-04-15T05:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72593",
    "user": "@rbeezer"
}
```

Attachment [trac_8222-sagenb-graph-editor.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-sagenb-graph-editor.patch) by @rbeezer created at 2010-04-15 05:29:31

All-in-one patch for sage library



---

archive/issue_comments_072594.json:
```json
{
    "body": "Attachment [trac_8222-sage-graph-editor.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-sage-graph-editor.patch) by @rbeezer created at 2010-04-15 05:33:24\n\nGreat improvements!  The \"live\" layout works great, and I really like the way dragging a vertex against the edge makes it appear to bounce off the wall.  Turning off auto-maximize was a good idea, I think.\n\nTested with 4.3.4 and sagenb-0.7.5.1.  sagenb was updated with all patches available to date.\n\nPasses all tests in sage/graphs, HTML docs build without warnings.\n\nI have added a reviewer patch.  There was a misspelling on the dialog warning about the circular layout change and while I was there I made a little change to the tail end of the string.  the patch file is just to make it easy to see the change.\n\nThere are also two new comprehensive patches, wrapping everything up (including reviewer patch).  Apply `trac_8222-sagenb-graph-editor.patch` to the notebook code and apply `trac_8222-sage-graph-editor.patch` to the sage library repo.\n\nRado - This is all ready for a positive review, subject to approval of the reviewer patch.  Have a look at that, and if everything looks OK with the combined patches, please mark this as positive review and add yourself as an author.  Great work! - Rob",
    "created_at": "2010-04-15T05:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72594",
    "user": "@rbeezer"
}
```

Attachment [trac_8222-sage-graph-editor.patch](tarball://root/attachments/some-uuid/ticket8222/trac_8222-sage-graph-editor.patch) by @rbeezer created at 2010-04-15 05:33:24

Great improvements!  The "live" layout works great, and I really like the way dragging a vertex against the edge makes it appear to bounce off the wall.  Turning off auto-maximize was a good idea, I think.

Tested with 4.3.4 and sagenb-0.7.5.1.  sagenb was updated with all patches available to date.

Passes all tests in sage/graphs, HTML docs build without warnings.

I have added a reviewer patch.  There was a misspelling on the dialog warning about the circular layout change and while I was there I made a little change to the tail end of the string.  the patch file is just to make it easy to see the change.

There are also two new comprehensive patches, wrapping everything up (including reviewer patch).  Apply `trac_8222-sagenb-graph-editor.patch` to the notebook code and apply `trac_8222-sage-graph-editor.patch` to the sage library repo.

Rado - This is all ready for a positive review, subject to approval of the reviewer patch.  Have a look at that, and if everything looks OK with the combined patches, please mark this as positive review and add yourself as an author.  Great work! - Rob



---

archive/issue_comments_072595.json:
```json
{
    "body": "Thanks Rob, for catching the typos (i should have spellcheck on next time). Big thanks to Kevin for the spring-repel algo and the auto-max. The big final patches worked fine, everything is in place. It is ready to be merged.\n\nnext thing to tackle is the graph interact !!! I hope this gets merged soon so when working on the graph interact we all have the current graph_editor as base (no need to build on this).",
    "created_at": "2010-04-15T16:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72595",
    "user": "rkirov"
}
```

Thanks Rob, for catching the typos (i should have spellcheck on next time). Big thanks to Kevin for the spring-repel algo and the auto-max. The big final patches worked fine, everything is in place. It is ready to be merged.

next thing to tackle is the graph interact !!! I hope this gets merged soon so when working on the graph interact we all have the current graph_editor as base (no need to build on this).



---

archive/issue_comments_072596.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T16:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72596",
    "user": "rkirov"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072597.json:
```json
{
    "body": "Hi Rado,\n\nYes, I forgot to add that the next target is definitely the graph-control for interacts.  I'll try to get my experiment together as a patch and post it there.  Also, I have my sights on the graph/latex/tikz stuff.\n\nAnd yes again - Kevin's contributions here are great!\n\nThanks for getting this ready to merge so quickly.\n\nRob",
    "created_at": "2010-04-15T16:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72597",
    "user": "@rbeezer"
}
```

Hi Rado,

Yes, I forgot to add that the next target is definitely the graph-control for interacts.  I'll try to get my experiment together as a patch and post it there.  Also, I have my sights on the graph/latex/tikz stuff.

And yes again - Kevin's contributions here are great!

Thanks for getting this ready to merge so quickly.

Rob



---

archive/issue_comments_072598.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-24T19:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72598",
    "user": "@williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072599.json:
```json
{
    "body": "I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is \"a missing script\".  So, needs work.",
    "created_at": "2010-04-24T19:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72599",
    "user": "@williamstein"
}
```

I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is "a missing script".  So, needs work.



---

archive/issue_comments_072600.json:
```json
{
    "body": "Replying to [comment:17 was]:\n> I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is \"a missing script\".  So, needs work. \n\nhmm, weird, it is all working on my setup. I downloaded sagenb-0.8 from #8725, applied rob's all-in-one patch, ran setup.py develop and there was nothing broken.\n\nCan Tim send me some more info on how to reproduce that bug, so I can work on fixing it?",
    "created_at": "2010-04-24T19:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72600",
    "user": "rkirov"
}
```

Replying to [comment:17 was]:
> I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is "a missing script".  So, needs work. 

hmm, weird, it is all working on my setup. I downloaded sagenb-0.8 from #8725, applied rob's all-in-one patch, ran setup.py develop and there was nothing broken.

Can Tim send me some more info on how to reproduce that bug, so I can work on fixing it?



---

archive/issue_comments_072601.json:
```json
{
    "body": "Actually, I got it working on my machine already without touching anything. William's still having trouble though.",
    "created_at": "2010-04-24T22:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72601",
    "user": "@TimDumol"
}
```

Actually, I got it working on my machine already without touching anything. William's still having trouble though.



---

archive/issue_comments_072602.json:
```json
{
    "body": "Replying to [comment:19 timdumol]:\n> Actually, I got it working on my machine already without touching anything. William's still having trouble though.\n\nMaybe it was a caching issue. Also i have only tested it on Firefox and Chrome, so maybe there is some browser specific issue?",
    "created_at": "2010-04-25T00:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72602",
    "user": "rkirov"
}
```

Replying to [comment:19 timdumol]:
> Actually, I got it working on my machine already without touching anything. William's still having trouble though.

Maybe it was a caching issue. Also i have only tested it on Firefox and Chrome, so maybe there is some browser specific issue?



---

archive/issue_comments_072603.json:
```json
{
    "body": "Since this has been confirmed to work, can this be marked positive review now?",
    "created_at": "2010-04-27T06:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72603",
    "user": "@TimDumol"
}
```

Since this has been confirmed to work, can this be marked positive review now?



---

archive/issue_comments_072604.json:
```json
{
    "body": "This was not merged, as far as I can tell.  The Sage library patch definitely isn't in, and the end of [the upstream sagenb graph_editor.html](https://github.com/sagemath/sagenb/blob/master/sagenb/data/graph_editor/graph_editor.html) indicates it wasn't merged there either.",
    "created_at": "2012-06-29T15:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72604",
    "user": "@kcrisman"
}
```

This was not merged, as far as I can tell.  The Sage library patch definitely isn't in, and the end of [the upstream sagenb graph_editor.html](https://github.com/sagemath/sagenb/blob/master/sagenb/data/graph_editor/graph_editor.html) indicates it wasn't merged there either.



---

archive/issue_comments_072605.json:
```json
{
    "body": "Notice that the graph editor hasn't worked in a long time, but [this pull request](https://github.com/sagemath/sagenb/pull/104) fixes it!",
    "created_at": "2012-10-23T13:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72605",
    "user": "@kcrisman"
}
```

Notice that the graph editor hasn't worked in a long time, but [this pull request](https://github.com/sagemath/sagenb/pull/104) fixes it!



---

archive/issue_comments_072606.json:
```json
{
    "body": "Changing keywords from \"\" to \"graph editor\".",
    "created_at": "2014-07-25T12:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72606",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "graph editor".



---

archive/issue_comments_072607.json:
```json
{
    "body": "Changing component from graph theory to notebook.",
    "created_at": "2014-10-16T08:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72607",
    "user": "@jdemeyer"
}
```

Changing component from graph theory to notebook.



---

archive/issue_comments_072608.json:
```json
{
    "body": "See [this sagenb issue](https://github.com/sagemath/sagenb/issues/244), in case anyone ever wants to port this to the latest.",
    "created_at": "2014-10-16T13:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72608",
    "user": "@kcrisman"
}
```

See [this sagenb issue](https://github.com/sagemath/sagenb/issues/244), in case anyone ever wants to port this to the latest.



---

archive/issue_comments_072609.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72609",
    "user": "@mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_072610.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72610",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072611.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72611",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072612.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-10-26T11:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8222#issuecomment-72612",
    "user": "@fchapoton"
}
```

Resolution: invalid
