# Issue 8952: Odd Girth

archive/issues_008952.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rbeezer\n\nAdd a function to compute odd girth, and modify Graph.is_perfect accordingly\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8952\n\n",
    "created_at": "2010-05-12T00:24:22Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.6",
    "title": "Odd Girth",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8952",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  @rbeezer

Add a function to compute odd girth, and modify Graph.is_perfect accordingly

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8952





---

archive/issue_comments_082328.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82328",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_082329.json:
```json
{
    "body": "What needs work here exactly? There's no patch on this ticket.",
    "created_at": "2012-09-25T18:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82329",
    "user": "https://github.com/kini"
}
```

What needs work here exactly? There's no patch on this ticket.



---

archive/issue_comments_082330.json:
```json
{
    "body": "Well, nothing actually. I used to use the Trac server as my todo-list, a loooong time ago, so you will find many such tickets in this section `^^;`\n\nI am (desperately) looking for a flat in Paris right now, but I should stop sinking and start swimming in a couple of weeks. \n\nI hope that all is well on you side !! `:-)`\n\nNathann",
    "created_at": "2012-09-25T18:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82330",
    "user": "https://github.com/nathanncohen"
}
```

Well, nothing actually. I used to use the Trac server as my todo-list, a loooong time ago, so you will find many such tickets in this section `^^;`

I am (desperately) looking for a flat in Paris right now, but I should stop sinking and start swimming in a couple of weeks. 

I hope that all is well on you side !! `:-)`

Nathann



---

archive/issue_comments_082331.json:
```json
{
    "body": "Haha, OK :) I found this ticket because someone asked about it on IRC and wants to work on it. Good luck with your flat!",
    "created_at": "2012-09-25T18:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82331",
    "user": "https://github.com/kini"
}
```

Haha, OK :) I found this ticket because someone asked about it on IRC and wants to work on it. Good luck with your flat!



---

archive/issue_comments_082332.json:
```json
{
    "body": "Attachment [trac_8952_odd_girth.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth.patch) by azi created at 2012-09-25 22:20:08\n\nPatch performing the ticket request",
    "created_at": "2012-09-25T22:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82332",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Attachment [trac_8952_odd_girth.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth.patch) by azi created at 2012-09-25 22:20:08

Patch performing the ticket request



---

archive/issue_comments_082333.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-25T22:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82333",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082334.json:
```json
{
    "body": "Hello!\n\nAttached is the patch that should perform the required task. odd_girth() computes the odd girth of a graph using a property of the characteristic polynomial of the adjacency matrix. Its (theoretic) computational complexity is optimal.",
    "created_at": "2012-09-25T22:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82334",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Hello!

Attached is the patch that should perform the required task. odd_girth() computes the odd girth of a graph using a property of the characteristic polynomial of the adjacency matrix. Its (theoretic) computational complexity is optimal.



---

archive/issue_comments_082335.json:
```json
{
    "body": "Azi,\n\nI took a quick look and it looks promising, especially since characteristic polynomials are quite fast in Sage.  I can look closer when I have a bit more time.\n\nFor now, documentation needs some work.  For example:\n\n\n```\nAny complete graph on more than 2 vertices contains a triangle and has thus odd girth 3 \n\n\t            G = graphs.CompleteGraph(10) \n\t            sage: G.odd_girth() \n\t            3\n```\n\n\nneeds a double colon after the lead-in sentence (all 3 of your verbatim blocks need this).  And your line creating the complete graph needs a `sage:` preceding it.\n\nCurrent documentation style needs \"INPUT\" and \"OUTPUT\" blocks - look around for examples.  They will be pretty simple in this case.\n\nYou can catch some of these yourself:\n\n\n```\nsage -b\nsage -docbuild reference html\n```\n\n\nwill rebuild the documentation and you can view the html file for mess-ups with the doc string.\n\nAnd\n\n\n```\nsage -t <source file>\n```\n\n\nwill find broken tests.\n\nRob",
    "created_at": "2012-09-26T02:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82335",
    "user": "https://github.com/rbeezer"
}
```

Azi,

I took a quick look and it looks promising, especially since characteristic polynomials are quite fast in Sage.  I can look closer when I have a bit more time.

For now, documentation needs some work.  For example:


```
Any complete graph on more than 2 vertices contains a triangle and has thus odd girth 3 

	            G = graphs.CompleteGraph(10) 
	            sage: G.odd_girth() 
	            3
```


needs a double colon after the lead-in sentence (all 3 of your verbatim blocks need this).  And your line creating the complete graph needs a `sage:` preceding it.

Current documentation style needs "INPUT" and "OUTPUT" blocks - look around for examples.  They will be pretty simple in this case.

You can catch some of these yourself:


```
sage -b
sage -docbuild reference html
```


will rebuild the documentation and you can view the html file for mess-ups with the doc string.

And


```
sage -t <source file>
```


will find broken tests.

Rob



---

archive/issue_comments_082336.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-09-26T02:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82336",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082337.json:
```json
{
    "body": "Second patch implementing the requested comments",
    "created_at": "2012-09-26T16:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82337",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Second patch implementing the requested comments



---

archive/issue_comments_082338.json:
```json
{
    "body": "Attachment [trac_8952_odd_girth_second.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth_second.patch) by azi created at 2012-09-26 16:39:52\n\nI have added a patch (hopefully valid) with the commends you requested. There is still one missing warning in building the documentation (Literal block expected; none found.\" is likely an indentiation problem and/or a problem with a double-colon) which I was not able to spot.",
    "created_at": "2012-09-26T16:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82338",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Attachment [trac_8952_odd_girth_second.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth_second.patch) by azi created at 2012-09-26 16:39:52

I have added a patch (hopefully valid) with the commends you requested. There is still one missing warning in building the documentation (Literal block expected; none found." is likely an indentiation problem and/or a problem with a double-colon) which I was not able to spot.



---

archive/issue_comments_082339.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-26T16:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82339",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082340.json:
```json
{
    "body": "Dear Azi,\n\nYour \"literal block expected\" error is caused by a double-colon after \"EXAMPLES\".  It should be a single, just to be typeset as-is.  A double-colon says verbatim (literal) stuff comes next.\n\nThe patch looks severely messed-up to me.  ;-(  I am not all sure how you got it to that state, but I think I can fix it.  Are you using clones or Mercurial queues?  Queues are much easier to deal with, and easier for iterative changes like this.\n\nDon't try to fix the double-colon until I fix the patch (maybe later today).\n\nRob",
    "created_at": "2012-09-26T17:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82340",
    "user": "https://github.com/rbeezer"
}
```

Dear Azi,

Your "literal block expected" error is caused by a double-colon after "EXAMPLES".  It should be a single, just to be typeset as-is.  A double-colon says verbatim (literal) stuff comes next.

The patch looks severely messed-up to me.  ;-(  I am not all sure how you got it to that state, but I think I can fix it.  Are you using clones or Mercurial queues?  Queues are much easier to deal with, and easier for iterative changes like this.

Don't try to fix the double-colon until I fix the patch (maybe later today).

Rob



---

archive/issue_comments_082341.json:
```json
{
    "body": "The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change",
    "created_at": "2012-09-26T17:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82341",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change



---

archive/issue_comments_082342.json:
```json
{
    "body": "Replying to [comment:11 azi]:\n> The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change\n\nWell, I sort of hope not, since I wrote that guide.  ;-)  It looks like something wasn't done quite right.\n\nGuide discusses two approaches:  clones and queues.  I cannot even begin to help if I don't know which approach you are taking.  Let me know.\n\nRob",
    "created_at": "2012-09-26T19:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82342",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:11 azi]:
> The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change

Well, I sort of hope not, since I wrote that guide.  ;-)  It looks like something wasn't done quite right.

Guide discusses two approaches:  clones and queues.  I cannot even begin to help if I don't know which approach you are taking.  Let me know.

Rob



---

archive/issue_comments_082343.json:
```json
{
    "body": "\"consolidated\" patch has previous work in one (proper) patch - still has azi's name on it, too.\n\nSee new \"Apply\" section in ticket description.\n\nAzi -\n\n1.  Start with a clean Sage installation (even if it means installing from source).\n2.  Install a system version of Mercurial, or replace \"hg\" commands with \"sage -hg\"\n3.  hg import <URL-to-consolidated-patch> (get URL from tiny download icon, not web-view of patch)\n4.  hg qpush  (to apply patch)\n5.  Rebuild sage, edit source, make changes, etc, etc.\n6.  hg qrefresh -m \"<A possible new message for patch summary goes here>\"\n7.  hg export qtip > <file-name-for-revised-patch>\n8.  hg qpop (to move changes out of the way, and get back to original Sage, rebuild, etc)\n\nYou can use \"hg qnew <private-name-for-patch>\" to initiate a new project with no interference from previous one.  You can easily manage several activities with qpop/qpush, and \"hg qpush --move\" will allow applying patches out of order.  \"hg qapplied\", \"hg qunapplied\" are informative.  Hope this is helpful.\n\nRob",
    "created_at": "2012-09-30T19:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82343",
    "user": "https://github.com/rbeezer"
}
```

"consolidated" patch has previous work in one (proper) patch - still has azi's name on it, too.

See new "Apply" section in ticket description.

Azi -

1.  Start with a clean Sage installation (even if it means installing from source).
2.  Install a system version of Mercurial, or replace "hg" commands with "sage -hg"
3.  hg import <URL-to-consolidated-patch> (get URL from tiny download icon, not web-view of patch)
4.  hg qpush  (to apply patch)
5.  Rebuild sage, edit source, make changes, etc, etc.
6.  hg qrefresh -m "<A possible new message for patch summary goes here>"
7.  hg export qtip > <file-name-for-revised-patch>
8.  hg qpop (to move changes out of the way, and get back to original Sage, rebuild, etc)

You can use "hg qnew <private-name-for-patch>" to initiate a new project with no interference from previous one.  You can easily manage several activities with qpop/qpush, and "hg qpush --move" will allow applying patches out of order.  "hg qapplied", "hg qunapplied" are informative.  Hope this is helpful.

Rob



---

archive/issue_comments_082344.json:
```json
{
    "body": "(same patch with the max 80 characters per line that Minh taught me to respect in the Graph files, some links between odd_girth and girth, and some modifications in the doc so that Sphinx gets what it should)",
    "created_at": "2012-10-01T13:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82344",
    "user": "https://github.com/nathanncohen"
}
```

(same patch with the max 80 characters per line that Minh taught me to respect in the Graph files, some links between odd_girth and girth, and some modifications in the doc so that Sphinx gets what it should)



---

archive/issue_comments_082345.json:
```json
{
    "body": "Ahem...\n\n\n```\nsage: graphs.CycleGraph(5).odd_girth()\n+Infinity\n```\n\n\nWith this additional patch, the functions looks more similar to what page 45 of \"Algebraic Graph Theory\" seems to say `:-)`\n\nNathann",
    "created_at": "2012-10-01T15:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82345",
    "user": "https://github.com/nathanncohen"
}
```

Ahem...


```
sage: graphs.CycleGraph(5).odd_girth()
+Infinity
```


With this additional patch, the functions looks more similar to what page 45 of "Algebraic Graph Theory" seems to say `:-)`

Nathann



---

archive/issue_comments_082346.json:
```json
{
    "body": "Apply trac_8952_odd_girth_consolidated.patch trac_8952_odd_girth-bugfix.patch",
    "created_at": "2012-10-01T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82346",
    "user": "https://github.com/kini"
}
```

Apply trac_8952_odd_girth_consolidated.patch trac_8952_odd_girth-bugfix.patch



---

archive/issue_comments_082347.json:
```json
{
    "body": "Replying to [comment:16 ncohen]:\n> With this additional patch, the functions looks more similar to what page 45 of \"Algebraic Graph Theory\" seems to say `:-)`\n\nI'd been meaning to suggest stepping by -2, mostly for clarity, and less code.  I hadn't realized there was a problem, though!  Good catch.",
    "created_at": "2012-10-01T17:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82347",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:16 ncohen]:
> With this additional patch, the functions looks more similar to what page 45 of "Algebraic Graph Theory" seems to say `:-)`

I'd been meaning to suggest stepping by -2, mostly for clarity, and less code.  I hadn't realized there was a problem, though!  Good catch.



---

archive/issue_comments_082348.json:
```json
{
    "body": "There is always a problem when a book decides to write `\\sum_i c_{n-i} x^i` instead of `\\sum_i c_{i} x^i` `:-P`\n\nIn the end what do we do with this ticket ? 3 peoples modified the patch already `:-D`\n\nTo me it looks good as it is... \n\nNathann",
    "created_at": "2012-10-02T08:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82348",
    "user": "https://github.com/nathanncohen"
}
```

There is always a problem when a book decides to write `\sum_i c_{n-i} x^i` instead of `\sum_i c_{i} x^i` `:-P`

In the end what do we do with this ticket ? 3 peoples modified the patch already `:-D`

To me it looks good as it is... 

Nathann



---

archive/issue_comments_082349.json:
```json
{
    "body": "HMmmmmmmm.... I guess I shouldn't put a 's' at the end of \"people\". And I guess I should have said \"persons\" instead, by the way `:-)`\n\nNathann",
    "created_at": "2012-10-02T08:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82349",
    "user": "https://github.com/nathanncohen"
}
```

HMmmmmmmm.... I guess I shouldn't put a 's' at the end of "people". And I guess I should have said "persons" instead, by the way `:-)`

Nathann



---

archive/issue_comments_082350.json:
```json
{
    "body": "(just updated the patch so that is_odd_hole_free uses this function too !!!)",
    "created_at": "2012-10-02T13:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82350",
    "user": "https://github.com/nathanncohen"
}
```

(just updated the patch so that is_odd_hole_free uses this function too !!!)



---

archive/issue_comments_082351.json:
```json
{
    "body": "Attachment [trac_8952_odd_girth-bugfix.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth-bugfix.patch) by azi created at 2012-10-27 13:23:48\n\nThe patch looks good to me. Am I allowed to change the status of the ticket to reflect that?",
    "created_at": "2012-10-27T13:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82351",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Attachment [trac_8952_odd_girth-bugfix.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth-bugfix.patch) by azi created at 2012-10-27 13:23:48

The patch looks good to me. Am I allowed to change the status of the ticket to reflect that?



---

archive/issue_comments_082352.json:
```json
{
    "body": "Well I guess you can if you think the patch is ready `:-)`\n\nNathann",
    "created_at": "2012-10-27T22:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82352",
    "user": "https://github.com/nathanncohen"
}
```

Well I guess you can if you think the patch is ready `:-)`

Nathann



---

archive/issue_comments_082353.json:
```json
{
    "body": "Ahem. Does everybody here agree that this patch should be merged ?\n\nNathann",
    "created_at": "2012-11-05T15:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82353",
    "user": "https://github.com/nathanncohen"
}
```

Ahem. Does everybody here agree that this patch should be merged ?

Nathann



---

archive/issue_comments_082354.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2012-11-05T16:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82354",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Looks good to me!



---

archive/issue_comments_082355.json:
```json
{
    "body": "Ok, fine then... Could you set it to positive_review ? I'm the last one who added something to the ticket `:-)`\n\nNathann",
    "created_at": "2012-11-05T16:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82355",
    "user": "https://github.com/nathanncohen"
}
```

Ok, fine then... Could you set it to positive_review ? I'm the last one who added something to the ticket `:-)`

Nathann



---

archive/issue_comments_082356.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-11-17T16:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82356",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082357.json:
```json
{
    "body": "Okayyyyyyyyyyyyyyyyyy.................. `:-P`\n\nNathann",
    "created_at": "2012-11-17T16:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82357",
    "user": "https://github.com/nathanncohen"
}
```

Okayyyyyyyyyyyyyyyyyy.................. `:-P`

Nathann



---

archive/issue_comments_082358.json:
```json
{
    "body": "I am sorry. I completely overlooked the \"set it to positive_review\" part.",
    "created_at": "2012-11-17T16:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82358",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

I am sorry. I completely overlooked the "set it to positive_review" part.



---

archive/issue_comments_082359.json:
```json
{
    "body": "No problem. Could you add your name to the list of reviewers/authors ? And if possible to the list in \"http://trac.sagemath.org/sage_trac/wiki\" too `:-)`\n\nNathann",
    "created_at": "2012-11-17T16:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82359",
    "user": "https://github.com/nathanncohen"
}
```

No problem. Could you add your name to the list of reviewers/authors ? And if possible to the list in "http://trac.sagemath.org/sage_trac/wiki" too `:-)`

Nathann



---

archive/issue_comments_082360.json:
```json
{
    "body": "OK. I have added myself to the wiki link. But I can't find the list of reviewers/authors. Do you happen to know where do I find that?",
    "created_at": "2012-11-17T18:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82360",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

OK. I have added myself to the wiki link. But I can't find the list of reviewers/authors. Do you happen to know where do I find that?



---

archive/issue_comments_082361.json:
```json
{
    "body": "Ahahaah. It's on this page, on the \"Modify Ticket\" section. When a ticket is positively reviewed, the list of authors and reviewers has to be filled. I often forget that myself `:-)`\n\nNathann",
    "created_at": "2012-11-17T18:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82361",
    "user": "https://github.com/nathanncohen"
}
```

Ahahaah. It's on this page, on the "Modify Ticket" section. When a ticket is positively reviewed, the list of authors and reviewers has to be filled. I often forget that myself `:-)`

Nathann



---

archive/issue_comments_082362.json:
```json
{
    "body": "Oooh ok! I suppose you will add yourself to the list right?",
    "created_at": "2012-11-17T18:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82362",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Oooh ok! I suppose you will add yourself to the list right?



---

archive/issue_comments_082363.json:
```json
{
    "body": "Well, I'm not really an author of this ticket, and Rob did some of it too `:-)`\n\nNathann",
    "created_at": "2012-11-17T19:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82363",
    "user": "https://github.com/nathanncohen"
}
```

Well, I'm not really an author of this ticket, and Rob did some of it too `:-)`

Nathann



---

archive/issue_comments_082364.json:
```json
{
    "body": "If azi is the only author, then he cannot be a reviewer...",
    "created_at": "2012-11-17T19:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82364",
    "user": "https://github.com/kini"
}
```

If azi is the only author, then he cannot be a reviewer...



---

archive/issue_comments_082365.json:
```json
{
    "body": "AHahah. If that's the law, then...`:-)`\n\nNathann",
    "created_at": "2012-11-17T19:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82365",
    "user": "https://github.com/nathanncohen"
}
```

AHahah. If that's the law, then...`:-)`

Nathann



---

archive/issue_comments_082366.json:
```json
{
    "body": "Attachment [trac_8952_odd_girth_consolidated.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth_consolidated.patch) by @jdemeyer created at 2012-12-16 15:35:44",
    "created_at": "2012-12-16T15:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82366",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_8952_odd_girth_consolidated.patch](tarball://root/attachments/some-uuid/ticket8952/trac_8952_odd_girth_consolidated.patch) by @jdemeyer created at 2012-12-16 15:35:44



---

archive/issue_comments_082367.json:
```json
{
    "body": "Rebased to sage-5.5.rc0.",
    "created_at": "2012-12-16T15:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82367",
    "user": "https://github.com/jdemeyer"
}
```

Rebased to sage-5.5.rc0.



---

archive/issue_events_009105.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-12-18T11:14:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8952#event-9105"
}
```



---

archive/issue_comments_082368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-12-18T11:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8952#issuecomment-82368",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
