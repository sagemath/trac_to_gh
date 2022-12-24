# Issue 5371: change autosave defaults

archive/issues_005371.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: autosave interval, snapshot\n\nUntil the autosave becomes smarter, the default settings should be changed.  Otherwise the number of snapshots eats up too much space.  In the exchange below, Jan Groenewald likes an autosave interval of 2 hours, which might be a bit long since the fix that deletes redundant snapshots is in.  So I would suggest a max history length of 50, as Jan asked for, and an autosave interval of at least 5 minutes.\n\nOn Mon, Feb 23, 2009 at 12:00 AM, Jan Groenewald <j...`@`aims.ac.za> wrote: \n> PS. I will now be permanently patching user_conf.py to set autosave_interval higher\n> from 3*60 to 120*60 and and max_history_length lower from 500 to 50. It would be\n> great if the defaults here were reconsidered.\n\n+1  -- I would be very happy if that change were made officially.\nPlease submit a patch / ticket.\n\nWilliam\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5371\n\n",
    "created_at": "2009-02-25T13:01:07Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "change autosave defaults",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5371",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: autosave interval, snapshot

Until the autosave becomes smarter, the default settings should be changed.  Otherwise the number of snapshots eats up too much space.  In the exchange below, Jan Groenewald likes an autosave interval of 2 hours, which might be a bit long since the fix that deletes redundant snapshots is in.  So I would suggest a max history length of 50, as Jan asked for, and an autosave interval of at least 5 minutes.

On Mon, Feb 23, 2009 at 12:00 AM, Jan Groenewald <j...`@`aims.ac.za> wrote: 
> PS. I will now be permanently patching user_conf.py to set autosave_interval higher
> from 3*60 to 120*60 and and max_history_length lower from 500 to 50. It would be
> great if the defaults here were reconsidered.

+1  -- I would be very happy if that change were made officially.
Please submit a patch / ticket.

William


Issue created by migration from https://trac.sagemath.org/ticket/5371





---

archive/issue_comments_041364.json:
```json
{
    "body": "I like Marshall's suggestion of 5 minutes for autosave and a history of length say 100.   Decreasing the history length likely won't have much of an impact on space usage, since the history is 1-file per user.",
    "created_at": "2009-02-26T01:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41364",
    "user": "was"
}
```

I like Marshall's suggestion of 5 minutes for autosave and a history of length say 100.   Decreasing the history length likely won't have much of an impact on space usage, since the history is 1-file per user.



---

archive/issue_comments_041365.json:
```json
{
    "body": "Attachment [trac_5371_worsheet_save_time.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_worsheet_save_time.patch) by rbeezer created at 2009-03-07 20:01:10\n\nReplying to [comment:1 was]:\nSince I was working through this in my own setup, I've added a patch increasing default save time to 1 hour (William Stein's latest suggestion on sage-support) and taking history length down to 100.\n\nI've added documentation on how to change these values for an existing notebook.\n\nSee related #5291 and #5300",
    "created_at": "2009-03-07T20:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41365",
    "user": "rbeezer"
}
```

Attachment [trac_5371_worsheet_save_time.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_worsheet_save_time.patch) by rbeezer created at 2009-03-07 20:01:10

Replying to [comment:1 was]:
Since I was working through this in my own setup, I've added a patch increasing default save time to 1 hour (William Stein's latest suggestion on sage-support) and taking history length down to 100.

I've added documentation on how to change these values for an existing notebook.

See related #5291 and #5300



---

archive/issue_comments_041366.json:
```json
{
    "body": "4 doctests fail after applying this patch and running \"sage -t\" on the server directory.\n\n\n```\n^[[Awstein@sage:~/build/sage-3.4.1.rc2-ref2$ ./sage -tp 30 devel/sage/sage/server\nGlobal iterations: 1\nFile iterations: 1\nUsing cached timings to run longest doctests first.\nDoctesting 24 files doing 30 jobs in parallel\nsage -t  devel/sage/sage/server/notebook/compress/BaseConvert.py\n         [0.1 s]\nsage -t  devel/sage/sage/server/notebook/compress/SourceMap.py\n         [0.1 s]\nsage -t  devel/sage/sage/server/notebook/compress/JavaScriptCompressor.py\n         [0.1 s]\nsage -t  devel/sage/sage/server/misc.py\n         [2.0 s]\nsage -t  devel/sage/sage/server/introspect.py\n         [2.0 s]\nsage -t  devel/sage/sage/server/trac/trac.py\n         [2.0 s]\nsage -t  devel/sage/sage/server/notebook/sage_email.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/sagetex.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/user.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/user.py\", line 86:\n    sage: config['max_history_length']\nExpected:\n    500\nGot:\n    100\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/user.py\", line 90:\n    sage: config['autosave_interval']\nExpected:\n    180\nGot:\n    3600\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_1\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_user.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/user_conf.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/keyboards.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/gnutls_socket_ssl.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/docHTMLProcessor.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/wiki/moin.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/template.py\n         [2.1 s]\nsage -t  devel/sage/sage/server/notebook/avatars.py\n         [2.2 s]\nsage -t  devel/sage/sage/server/notebook/jquery.py\n         [2.2 s]\nsage -t  devel/sage/sage/server/notebook/applet.py\n         [2.3 s]\nsage -t  devel/sage/sage/server/notebook/notebook.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/notebook.py\", line 561:\n    sage: config['max_history_length']\nExpected:\n    500\nGot:\n    100\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/notebook.py\", line 565:\n    sage: config['autosave_interval']\nExpected:\n    180\nGot:\n    3600\n**********************************************************************\n1 items had failures:\n   2 of   9 in __main__.example_19\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_notebook.py\n         [2.4 s]\nsage -t  devel/sage/sage/server/support.py\n         [2.6 s]\nsage -t  devel/sage/sage/server/notebook/interact.py\n         [3.1 s]\nsage -t  devel/sage/sage/server/notebook/twist.py\n         [3.5 s]\nsage -t  devel/sage/sage/server/notebook/worksheet.py\n         [5.3 s]\nsage -t  devel/sage/sage/server/notebook/cell.py\n         [8.1 s]\n \n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/server/notebook/user.py # 2 doctests failed\n        sage -t  devel/sage/sage/server/notebook/notebook.py # 2 doctests failed\n```\n",
    "created_at": "2009-04-12T08:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41366",
    "user": "was"
}
```

4 doctests fail after applying this patch and running "sage -t" on the server directory.


```
^[[Awstein@sage:~/build/sage-3.4.1.rc2-ref2$ ./sage -tp 30 devel/sage/sage/server
Global iterations: 1
File iterations: 1
Using cached timings to run longest doctests first.
Doctesting 24 files doing 30 jobs in parallel
sage -t  devel/sage/sage/server/notebook/compress/BaseConvert.py
         [0.1 s]
sage -t  devel/sage/sage/server/notebook/compress/SourceMap.py
         [0.1 s]
sage -t  devel/sage/sage/server/notebook/compress/JavaScriptCompressor.py
         [0.1 s]
sage -t  devel/sage/sage/server/misc.py
         [2.0 s]
sage -t  devel/sage/sage/server/introspect.py
         [2.0 s]
sage -t  devel/sage/sage/server/trac/trac.py
         [2.0 s]
sage -t  devel/sage/sage/server/notebook/sage_email.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/sagetex.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/user.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/user.py", line 86:
    sage: config['max_history_length']
Expected:
    500
Got:
    100
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/user.py", line 90:
    sage: config['autosave_interval']
Expected:
    180
Got:
    3600
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_1
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_user.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/user_conf.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/keyboards.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/gnutls_socket_ssl.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/docHTMLProcessor.py
         [2.1 s]
sage -t  devel/sage/sage/server/wiki/moin.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/template.py
         [2.1 s]
sage -t  devel/sage/sage/server/notebook/avatars.py
         [2.2 s]
sage -t  devel/sage/sage/server/notebook/jquery.py
         [2.2 s]
sage -t  devel/sage/sage/server/notebook/applet.py
         [2.3 s]
sage -t  devel/sage/sage/server/notebook/notebook.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/notebook.py", line 561:
    sage: config['max_history_length']
Expected:
    500
Got:
    100
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/server/notebook/notebook.py", line 565:
    sage: config['autosave_interval']
Expected:
    180
Got:
    3600
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_19
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_notebook.py
         [2.4 s]
sage -t  devel/sage/sage/server/support.py
         [2.6 s]
sage -t  devel/sage/sage/server/notebook/interact.py
         [3.1 s]
sage -t  devel/sage/sage/server/notebook/twist.py
         [3.5 s]
sage -t  devel/sage/sage/server/notebook/worksheet.py
         [5.3 s]
sage -t  devel/sage/sage/server/notebook/cell.py
         [8.1 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/server/notebook/user.py # 2 doctests failed
        sage -t  devel/sage/sage/server/notebook/notebook.py # 2 doctests failed
```




---

archive/issue_comments_041367.json:
```json
{
    "body": "Well, these are trivial doctest failures since the defaults have been changed, patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41367",
    "user": "mabshoff"
}
```

Well, these are trivial doctest failures since the defaults have been changed, patch coming up.

Cheers,

Michael



---

archive/issue_comments_041368.json:
```json
{
    "body": "Fix doctests",
    "created_at": "2009-04-13T04:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41368",
    "user": "mabshoff"
}
```

Fix doctests



---

archive/issue_comments_041369.json:
```json
{
    "body": "Attachment [trac_5371_reviewer-2.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_reviewer-2.patch) by mabshoff created at 2009-04-13 04:56:46\n\nAdd a doctest, slightly rewrite the example",
    "created_at": "2009-04-13T04:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41369",
    "user": "mabshoff"
}
```

Attachment [trac_5371_reviewer-2.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_reviewer-2.patch) by mabshoff created at 2009-04-13 04:56:46

Add a doctest, slightly rewrite the example



---

archive/issue_comments_041370.json:
```json
{
    "body": "Bouncing this since no one seems to be working on this.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T22:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41370",
    "user": "mabshoff"
}
```

Bouncing this since no one seems to be working on this.

Cheers,

Michael



---

archive/issue_comments_041371.json:
```json
{
    "body": "That second reviewer patch fails for me since I don't have a directory \"/home/mabshoff/\".  I think that's why the original patch didn't have sage: lines there.  What do you think, mabshoff?",
    "created_at": "2009-04-22T10:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41371",
    "user": "jason"
}
```

That second reviewer patch fails for me since I don't have a directory "/home/mabshoff/".  I think that's why the original patch didn't have sage: lines there.  What do you think, mabshoff?



---

archive/issue_comments_041372.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> That second reviewer patch fails for me since I don't have a directory \"/home/mabshoff/\".  I think that's why the original patch didn't have sage: lines there.  What do you think, mabshoff?\n\nWell, the fix would be to use $DOT_SAGE instead even though I am afraid that people who changed the custom settings already would see failed doctests. And the doctest might even change the default settings, etc. \n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T16:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41372",
    "user": "mabshoff"
}
```

Replying to [comment:7 jason]:
> That second reviewer patch fails for me since I don't have a directory "/home/mabshoff/".  I think that's why the original patch didn't have sage: lines there.  What do you think, mabshoff?

Well, the fix would be to use $DOT_SAGE instead even though I am afraid that people who changed the custom settings already would see failed doctests. And the doctest might even change the default settings, etc. 

Thoughts?

Cheers,

Michael



---

archive/issue_comments_041373.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> Well, the fix would be to use $DOT_SAGE instead even though I am afraid that people who changed the custom settings already would see failed doctests. And the doctest might even change the default settings, etc. \n\nIt appears to me that employing these commands with $DOT_SAGE will\n\n(a) mess with users' changes\n\n(b) fail for those who have changed the defaults.\n\nI'm reasonably confident this would be the case on my own setup, since I don't have my DOT_SAGE directory isolated from where I do testing.  Of course, the doctests could save state, run a test, then restore the state.\n\nHowever, I never really meant the documentation to be doctests.  The patch was meant to be stop-gap, and not a complete solution to the problem of excessive saves.  I was included a sample command-line session as a way to show users how to change the defaults without editing the source.  So if somebody had tracked the problem this far (like kcrisman today), then they might get some help for a quick fix.\n\nI'd prefer this whole ticket to not even be necessary.  But I think converting the sample command-line session to doctests is more trouble than it is worth.  So I'd suggest not including the second reviewer patch.  Sorry I didn't look at this sooner - I misunderstood what was happening with the doctest failures and the added doctest.\n\nI'm going to post some more general comments about all this on sage-support.",
    "created_at": "2009-04-22T20:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41373",
    "user": "rbeezer"
}
```

Replying to [comment:8 mabshoff]:
> Well, the fix would be to use $DOT_SAGE instead even though I am afraid that people who changed the custom settings already would see failed doctests. And the doctest might even change the default settings, etc. 

It appears to me that employing these commands with $DOT_SAGE will

(a) mess with users' changes

(b) fail for those who have changed the defaults.

I'm reasonably confident this would be the case on my own setup, since I don't have my DOT_SAGE directory isolated from where I do testing.  Of course, the doctests could save state, run a test, then restore the state.

However, I never really meant the documentation to be doctests.  The patch was meant to be stop-gap, and not a complete solution to the problem of excessive saves.  I was included a sample command-line session as a way to show users how to change the defaults without editing the source.  So if somebody had tracked the problem this far (like kcrisman today), then they might get some help for a quick fix.

I'd prefer this whole ticket to not even be necessary.  But I think converting the sample command-line session to doctests is more trouble than it is worth.  So I'd suggest not including the second reviewer patch.  Sorry I didn't look at this sooner - I misunderstood what was happening with the doctest failures and the added doctest.

I'm going to post some more general comments about all this on sage-support.



---

archive/issue_comments_041374.json:
```json
{
    "body": "I was looking at this because I've been having problems with the notebook lately due to excessive creation of snapshots. I applied the original patch and the first reviewer patch against 4.0.rc2. They look fine, pass doctests in sage/server, and perform as expected. Positive review for them. \n\nI didn't apply the second reviewer patch, and I agree with Rob's argument that it isn't necessary. I should add that I did find the docstring extremely helpful in clearing up a problem with my existing notebook server, so I'd like that to stay in.",
    "created_at": "2009-05-31T01:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41374",
    "user": "kedlaya"
}
```

I was looking at this because I've been having problems with the notebook lately due to excessive creation of snapshots. I applied the original patch and the first reviewer patch against 4.0.rc2. They look fine, pass doctests in sage/server, and perform as expected. Positive review for them. 

I didn't apply the second reviewer patch, and I agree with Rob's argument that it isn't necessary. I should add that I did find the docstring extremely helpful in clearing up a problem with my existing notebook server, so I'd like that to stay in.



---

archive/issue_comments_041375.json:
```json
{
    "body": "I think the initial \"doctest\" at the beginning of the file should be removed.  As it is, none of the patches have valid rest markup.\n\nSo, just remove the bit at the beginning of the first patch and I'll merge it along with the patch that has the simple doctest fixes.",
    "created_at": "2009-06-04T18:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41375",
    "user": "mhansen"
}
```

I think the initial "doctest" at the beginning of the file should be removed.  As it is, none of the patches have valid rest markup.

So, just remove the bit at the beginning of the first patch and I'll merge it along with the patch that has the simple doctest fixes.



---

archive/issue_comments_041376.json:
```json
{
    "body": "Replaces very first patch",
    "created_at": "2009-06-05T04:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41376",
    "user": "rbeezer"
}
```

Replaces very first patch



---

archive/issue_comments_041377.json:
```json
{
    "body": "Attachment [trac_5371_worksheet_save_time_version2.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_worksheet_save_time_version2.patch) by rbeezer created at 2009-06-05 04:10:17\n\nFourth patch is identical to first, but with docstring removed, so it only changes default values for a newly created notebook.\n\nPresumably this will all get sorted out with a notebook overhaul.  If not, the content of that docstring should probably go somewhere (the wiki?) where folks can find it, since it gives instructions for a fix that cannot be enacted to existing servers through a patch.",
    "created_at": "2009-06-05T04:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41377",
    "user": "rbeezer"
}
```

Attachment [trac_5371_worksheet_save_time_version2.patch](tarball://root/attachments/some-uuid/ticket5371/trac_5371_worksheet_save_time_version2.patch) by rbeezer created at 2009-06-05 04:10:17

Fourth patch is identical to first, but with docstring removed, so it only changes default values for a newly created notebook.

Presumably this will all get sorted out with a notebook overhaul.  If not, the content of that docstring should probably go somewhere (the wiki?) where folks can find it, since it gives instructions for a fix that cannot be enacted to existing servers through a patch.



---

archive/issue_comments_041378.json:
```json
{
    "body": "I applied\n\n```\nhttp://trac.sagemath.org/sage_trac/raw-attachment/ticket/5371/trac_5371_worksheet_save_time_version2.patch\nhttp://trac.sagemath.org/sage_trac/raw-attachment/ticket/5371/trac_5371_reviewer.patch\n```\n\n\nand fixed the following doctests:\n\n\n```\nsage -t  sage/server/notebook/notebook.py\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/sage/server/notebook/notebook.py\", line 561:\n    sage: config['max_history_length']\nExpected:\n    100\nGot:\n    1000\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_19\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/ncalexan/sage-4.0.2.alpha1/tmp/.doctest_notebook.py\n         [2.0 s]\nsage -t  sage/server/notebook/template.py\n         [1.3 s]\nsage -t  sage/server/notebook/sagetex.py\n         [1.4 s]\nsage -t  sage/server/notebook/user.py\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/sage/server/notebook/user.py\", line 86:\n    sage: config['max_history_length']\nExpected:\n    100\nGot:\n    1000\n```\n",
    "created_at": "2009-06-13T23:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41378",
    "user": "ncalexan"
}
```

I applied

```
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5371/trac_5371_worksheet_save_time_version2.patch
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5371/trac_5371_reviewer.patch
```


and fixed the following doctests:


```
sage -t  sage/server/notebook/notebook.py
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/sage/server/notebook/notebook.py", line 561:
    sage: config['max_history_length']
Expected:
    100
Got:
    1000
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_19
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/ncalexan/sage-4.0.2.alpha1/tmp/.doctest_notebook.py
         [2.0 s]
sage -t  sage/server/notebook/template.py
         [1.3 s]
sage -t  sage/server/notebook/sagetex.py
         [1.4 s]
sage -t  sage/server/notebook/user.py
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/sage/server/notebook/user.py", line 86:
    sage: config['max_history_length']
Expected:
    100
Got:
    1000
```




---

archive/issue_comments_041379.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T23:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5371#issuecomment-41379",
    "user": "ncalexan"
}
```

Resolution: fixed
