# Issue 6342: notebook -- fix that the slideshow mode in the notebook utterly completely broken

archive/issues_006342.json:
```json
{
    "body": "Assignee: boothby\n\nThis patch turns slideshow mode into something actually pretty useful.  It is maybe uglier than it was 2 years ago.  It is maybe \"lame\"-ish, perhaps.  But it is usable!  Which is a million times better than the literally buggy situation now.  \n\nThe actual patch attached here tracks both the cell_list (the compute cells), and adds a new list allcell_list, which contains all the cells (not just the compute cells).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6342\n\n",
    "created_at": "2009-06-16T22:15:54Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "notebook -- fix that the slideshow mode in the notebook utterly completely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6342",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

This patch turns slideshow mode into something actually pretty useful.  It is maybe uglier than it was 2 years ago.  It is maybe "lame"-ish, perhaps.  But it is usable!  Which is a million times better than the literally buggy situation now.  

The actual patch attached here tracks both the cell_list (the compute cells), and adds a new list allcell_list, which contains all the cells (not just the compute cells).

Issue created by migration from https://trac.sagemath.org/ticket/6342





---

archive/issue_comments_050573.json:
```json
{
    "body": "Attachment [trac_6342.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342.patch) by boothby created at 2009-06-16 22:41:23\n\nUnder Ubuntu j & firefox, I can repeatably hit an infinite memory consumption:\n\n1. Switch into slideshow mode\n2. Shift-click to create an html cell above the first cell\n3. Enter the text, `This is some $foo$`\n4. Shift-enter to save the html cell\n5. Shift-click to edit the html cell just created\n6. Quickly kill firefox before it takes down your system.",
    "created_at": "2009-06-16T22:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50573",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_6342.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342.patch) by boothby created at 2009-06-16 22:41:23

Under Ubuntu j & firefox, I can repeatably hit an infinite memory consumption:

1. Switch into slideshow mode
2. Shift-click to create an html cell above the first cell
3. Enter the text, `This is some $foo$`
4. Shift-enter to save the html cell
5. Shift-click to edit the html cell just created
6. Quickly kill firefox before it takes down your system.



---

archive/issue_comments_050574.json:
```json
{
    "body": "notes on the above comment:\n\nStep 1 may be omitted, this bug is active in normal mode.  Step 5 should read, \"double-click\".",
    "created_at": "2009-06-16T22:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50574",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

notes on the above comment:

Step 1 may be omitted, this bug is active in normal mode.  Step 5 should read, "double-click".



---

archive/issue_comments_050575.json:
```json
{
    "body": "Attachment [trac_6342-part2.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part2.patch) by @williamstein created at 2009-06-17 10:28:59\n\na tiny little bugfix",
    "created_at": "2009-06-17T10:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50575",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6342-part2.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part2.patch) by @williamstein created at 2009-06-17 10:28:59

a tiny little bugfix



---

archive/issue_comments_050576.json:
```json
{
    "body": "Attachment [trac_6342-part3.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part3.patch) by @williamstein created at 2009-06-17 10:29:12",
    "created_at": "2009-06-17T10:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50576",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6342-part3.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part3.patch) by @williamstein created at 2009-06-17 10:29:12



---

archive/issue_comments_050577.json:
```json
{
    "body": "make it so slides delimited by text cells with <hr>'s; lighten up control css",
    "created_at": "2009-06-17T19:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50577",
    "user": "https://github.com/williamstein"
}
```

make it so slides delimited by text cells with <hr>'s; lighten up control css



---

archive/issue_comments_050578.json:
```json
{
    "body": "Attachment [trac_6342-part4.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part4.patch) by boothby created at 2009-06-17 20:39:58\n\nProblems:\n\n1. Shift-enter is broken in html cells\n2. Up & down buttons are completely broken (as are the pgup/pgdn keys):\n   a. Without any <hr> tags, nothing happens at all\n   b. With one <hr> tag, one can view either the first cell or just the text cell with the <hr> all by itself.\n \nComments:\n\n1. I liked the previous version which showed cells after the current one.\n2. It would be nice if you didn't have to have your mouse in a cell for the pgdn/pgup keys to work. (this would take some effort, as we have no global key handling right now -- so this should be handled in another ticket)",
    "created_at": "2009-06-17T20:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50578",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_6342-part4.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part4.patch) by boothby created at 2009-06-17 20:39:58

Problems:

1. Shift-enter is broken in html cells
2. Up & down buttons are completely broken (as are the pgup/pgdn keys):
   a. Without any <hr> tags, nothing happens at all
   b. With one <hr> tag, one can view either the first cell or just the text cell with the <hr> all by itself.
 
Comments:

1. I liked the previous version which showed cells after the current one.
2. It would be nice if you didn't have to have your mouse in a cell for the pgdn/pgup keys to work. (this would take some effort, as we have no global key handling right now -- so this should be handled in another ticket)



---

archive/issue_comments_050579.json:
```json
{
    "body": "I just read the new entry in the tutorial.  According to the specified behavior (which I don't like), the up&down buttons are almost working -- however,\n\n1. Deleting a cell in a 'frame' jumps back to the previous frame, even if it wasn't the first cell in the frame.\n2. The first frame shows up fine, but the second and subsequent frames don't show any code cells -- it's just the HTML cells, and there's no way to view the code cells.  Interestingly, if you add a few cells to the frame, they don't show up -- but after 10 or 20, they start appearing.  However, if you switch out of and back into the frame, it's back to not showing any code cells.\n3. The counter / progress meter shows the number of cells, not the number of frames.  This is counterintuitive.\n\nReasons I don't like the specified behavior:\n\n1. The resulting code is more complex.\n2. Using <hr>'s, while documented, is not intuitive.  I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap.\n\nBy contrast, the version before part-2.patch was clean, simple and intuitive.",
    "created_at": "2009-06-17T21:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50579",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I just read the new entry in the tutorial.  According to the specified behavior (which I don't like), the up&down buttons are almost working -- however,

1. Deleting a cell in a 'frame' jumps back to the previous frame, even if it wasn't the first cell in the frame.
2. The first frame shows up fine, but the second and subsequent frames don't show any code cells -- it's just the HTML cells, and there's no way to view the code cells.  Interestingly, if you add a few cells to the frame, they don't show up -- but after 10 or 20, they start appearing.  However, if you switch out of and back into the frame, it's back to not showing any code cells.
3. The counter / progress meter shows the number of cells, not the number of frames.  This is counterintuitive.

Reasons I don't like the specified behavior:

1. The resulting code is more complex.
2. Using <hr>'s, while documented, is not intuitive.  I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap.

By contrast, the version before part-2.patch was clean, simple and intuitive.



---

archive/issue_comments_050580.json:
```json
{
    "body": "> The first frame shows up fine, but the second and subsequent frames don't show any code cells \n\nThis is an unintended bug which I'm fixing. \n\n> Reasons I don't like the specified behavior:\n>   1. The resulting code is more complex.\n>   2. Using <hr>'s, while documented, is not intuitive. I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap. \n> By contrast, the version before part-2.patch was clean, simple and intuitive. \n\nI'm trying to give an *actual* talk, and in preparing it, I learned that the version before part-2.patch was actually totally broken crap for actual use.  In contrast, what I've just written is really awesome for actual use.   There is a huge difference between imagining maybe giving a talk and actually writing a talk you're going to give in front of a 130 people.  It is absolutely essential to have slides that are given by a marker.  <hr> is a very reasonable choice for a marker.\n\n> 3. The counter / progress meter shows the number of cells, not the number of frames. This is counterintuitive. \n\nIt's going to be a lot more work to implement the counter to show the frames, and I decided not to implement that in the interest of iterative development.",
    "created_at": "2009-06-17T22:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50580",
    "user": "https://github.com/williamstein"
}
```

> The first frame shows up fine, but the second and subsequent frames don't show any code cells 

This is an unintended bug which I'm fixing. 

> Reasons I don't like the specified behavior:
>   1. The resulting code is more complex.
>   2. Using <hr>'s, while documented, is not intuitive. I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap. 
> By contrast, the version before part-2.patch was clean, simple and intuitive. 

I'm trying to give an *actual* talk, and in preparing it, I learned that the version before part-2.patch was actually totally broken crap for actual use.  In contrast, what I've just written is really awesome for actual use.   There is a huge difference between imagining maybe giving a talk and actually writing a talk you're going to give in front of a 130 people.  It is absolutely essential to have slides that are given by a marker.  <hr> is a very reasonable choice for a marker.

> 3. The counter / progress meter shows the number of cells, not the number of frames. This is counterintuitive. 

It's going to be a lot more work to implement the counter to show the frames, and I decided not to implement that in the interest of iterative development.



---

archive/issue_comments_050581.json:
```json
{
    "body": "Attachment [trac_6342-part5.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part5.patch) by boothby created at 2009-06-17 23:46:01\n\nSlideshow mode now works, shift-enter on HTML cells is still broken.",
    "created_at": "2009-06-17T23:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50581",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_6342-part5.patch](tarball://root/attachments/some-uuid/ticket6342/trac_6342-part5.patch) by boothby created at 2009-06-17 23:46:01

Slideshow mode now works, shift-enter on HTML cells is still broken.



---

archive/issue_comments_050582.json:
```json
{
    "body": "Oops, the \"bottom\" button now jumps to the last cell instead of the last frame.",
    "created_at": "2009-06-17T23:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50582",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Oops, the "bottom" button now jumps to the last cell instead of the last frame.



---

archive/issue_comments_050583.json:
```json
{
    "body": "It would be nice if there were some way to\n\n1. indicate which hr's delimit slide breaks, and which don't, i.e. if you want to use an hr in the middle of a slide, and\n\n2. allow for slides which don't contain any cells.\n\nRegarding 1, we could even use something like <sage_slide_break> instead",
    "created_at": "2009-06-23T09:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50583",
    "user": "https://github.com/rlmill"
}
```

It would be nice if there were some way to

1. indicate which hr's delimit slide breaks, and which don't, i.e. if you want to use an hr in the middle of a slide, and

2. allow for slides which don't contain any cells.

Regarding 1, we could even use something like <sage_slide_break> instead



---

archive/issue_comments_050584.json:
```json
{
    "body": "I think also if there is a newline at the end of an html block, it cuts the slide after the next cell.",
    "created_at": "2009-06-23T10:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50584",
    "user": "https://github.com/rlmill"
}
```

I think also if there is a newline at the end of an html block, it cuts the slide after the next cell.



---

archive/issue_comments_050585.json:
```json
{
    "body": "Adding a cell to the end of a slide is also problematic.",
    "created_at": "2009-06-23T10:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50585",
    "user": "https://github.com/rlmill"
}
```

Adding a cell to the end of a slide is also problematic.



---

archive/issue_comments_050586.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50586",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_050587.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6342#issuecomment-50587",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid



---

archive/issue_events_006586.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2020-03-29T02:12:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6342",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6342#event-6586"
}
```
