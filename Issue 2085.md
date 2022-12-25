# Issue 2085: [with patch, needs review] bug in graph_isom and binary_code

archive/issues_002085.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nThis bug was only exposed by changing the refinement procedure to always return 0: although this slows the algorithm down, it should not change correctness, but errors were cropping up as low as three vertices for digraphs. Since the only way to expose the bug is to slow down the algorithm, there isn't a clear way to add a doctest for it. However, it is imperative that this typo fix get merged in...\n\nAlso, there is a new function included in the bundle, which plays the role of the refinement procedure, but also does some checks to make sure that the assumptions being made on the function are true. This is the first of several \"automatic debugging\" measures I will be taking, to solidify the isomorphism programs.\n\nNOTE: This bundle depends on tickets #1304 and #2082.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2085\n\n",
    "created_at": "2008-02-07T11:05:30Z",
    "labels": [
        "component: graph theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] bug in graph_isom and binary_code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2085",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  @jasongrout

This bug was only exposed by changing the refinement procedure to always return 0: although this slows the algorithm down, it should not change correctness, but errors were cropping up as low as three vertices for digraphs. Since the only way to expose the bug is to slow down the algorithm, there isn't a clear way to add a doctest for it. However, it is imperative that this typo fix get merged in...

Also, there is a new function included in the bundle, which plays the role of the refinement procedure, but also does some checks to make sure that the assumptions being made on the function are true. This is the first of several "automatic debugging" measures I will be taking, to solidify the isomorphism programs.

NOTE: This bundle depends on tickets #1304 and #2082.

Issue created by migration from https://trac.sagemath.org/ticket/2085





---

archive/issue_comments_013467.json:
```json
{
    "body": "Attachment [2085-auto_debug_and_bug_fix.hg](tarball://root/attachments/some-uuid/ticket2085/2085-auto_debug_and_bug_fix.hg) by @rlmill created at 2008-02-07 22:55:15",
    "created_at": "2008-02-07T22:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13467",
    "user": "https://github.com/rlmill"
}
```

Attachment [2085-auto_debug_and_bug_fix.hg](tarball://root/attachments/some-uuid/ticket2085/2085-auto_debug_and_bug_fix.hg) by @rlmill created at 2008-02-07 22:55:15



---

archive/issue_comments_013468.json:
```json
{
    "body": "positive review for the 8314 plotting loops patch.",
    "created_at": "2008-02-09T09:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13468",
    "user": "https://github.com/jasongrout"
}
```

positive review for the 8314 plotting loops patch.



---

archive/issue_comments_013469.json:
```json
{
    "body": "Attachment [2085-helper_fn_names.patch](tarball://root/attachments/some-uuid/ticket2085/2085-helper_fn_names.patch) by @rlmill created at 2008-02-16 20:08:21",
    "created_at": "2008-02-16T20:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13469",
    "user": "https://github.com/rlmill"
}
```

Attachment [2085-helper_fn_names.patch](tarball://root/attachments/some-uuid/ticket2085/2085-helper_fn_names.patch) by @rlmill created at 2008-02-16 20:08:21



---

archive/issue_comments_013470.json:
```json
{
    "body": "Looks good to me at this point in my graph isomorphism education.",
    "created_at": "2008-02-18T23:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13470",
    "user": "https://github.com/jasongrout"
}
```

Looks good to me at this point in my graph isomorphism education.



---

archive/issue_comments_013471.json:
```json
{
    "body": "``` \n[2:40pm] jason-: what's next?\n[2:41pm] rlm: ok, next is #2085, and you've already done the first two!\n[2:41pm] jason-: yay!\n[2:42pm] jason-: whoa, that's a big bundle.\n[2:43pm] rlm: the third patch in the bundle makes it look nicer when you print stuff\n[2:43pm] jason-: hang on, I'm separating it out into patches\n[2:43pm] jason-: and importing it into my queue.\n[2:44pm] rlm: it also makes it so that you can automatically sanity-check the refinement function\n[2:44pm] roed__ left the chat room. (Read error: 104 (Connection reset by peer))\n[2:45pm] roed_ joined the chat room.\n[2:47pm] jason-: the loop plotting patch has already been merged, right?\n[2:47pm] rlm: yes\n[2:47pm] rlm: that's 3 down, 3 to go\n[2:50pm] jason-: and I don't need to look at patches 1 and 2, right?\n[2:50pm] rlm: correct\n[2:51pm] jason-: huh, what does:\n[2:51pm] jason-: cdef int test_refine_by_square_matrix(self, int *alpha, int n, int **g, int dig) except? -1:\n[2:51pm] jason-: do?\n[2:52pm] jason-: (the \"except?\" ?)\n[2:52pm] rlm: it has the same signature as refine_by_square_matrix\n[2:52pm] rlm: it records the state before the function is called, and then after it calls it, and checks to make sure that the right thing is happening\n[2:52pm] jason-: what is \"it\"?\n[2:52pm] jason-: Cython?\n[2:53pm] rlm:  refine_by_square_matrix is the real function\n[2:53pm] rlm: test_etc just checks that  refine_by_square_matrix is doing the right thing!\n[2:53pm] rlm: it's automatic debugging\n[2:53pm] jason-: cool.  I was just wondering what the \"except? -1:\" syntax did.\n[2:53pm] rlm: \" except? -1\" allows the function to raise an error\n[2:54pm] rlm: which i do, if test_blahblahblah discovers a mistake\n[2:54pm] jason-: so it looks like most of the changes are the including k as an attribute thing.\n[2:55pm] jason-: the others are testing functions?\n[2:55pm] rlm: yep\n[2:56pm] jason-: okay.  Well, since nothing looks obviously wrong (but I'm not sure if I could spot something like that if it hit me upside the head at this point), I say to go ahead and merge it and that way I'll be looking at it when I go through the algorithm over the next little while.\n[2:56pm] jason-: Besides, the testing functions will make it easier to go through the algorithm \n[2:56pm] rlm: cool.\n[2:56pm] rlm: two patches left in this bundle\n[2:57pm] jason-: Did I tell you that you convinced me that this review and the whole-algorithm review need to be two separate things? \n[2:57pm] rlm: I gathered as much\n[2:57pm] jason-: okay, we already talked about the next one.\n[2:57pm] rlm: The second to last patch in that bundle is the bug i described to you at SD7\n[2:58pm] jason-: and I agreed it was good (at 3AM after a week with no sleep \n[2:58pm] rlm: haha\n[2:58pm] rlm: it\n[2:58pm] rlm: 's still good, since it eliminated that one bug\n[2:58pm] rlm: and the last patch was the idea was also talked about at SD7, namely providing the option to turn off the indicator function, in order to expose the bug to doctesting\n[2:58pm] rlm: \"was\" -> we\n[2:59pm] jason-: so \"uif\" is the indicator function switch?\n[2:59pm] rlm: yep\n[3:00pm] jason-: okay, I say it goes in for the same reasons as above.\n[3:00pm] rlm: cool, so that's the bundle\n```",
    "created_at": "2008-02-18T23:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13471",
    "user": "https://github.com/rlmill"
}
```

``` 
[2:40pm] jason-: what's next?
[2:41pm] rlm: ok, next is #2085, and you've already done the first two!
[2:41pm] jason-: yay!
[2:42pm] jason-: whoa, that's a big bundle.
[2:43pm] rlm: the third patch in the bundle makes it look nicer when you print stuff
[2:43pm] jason-: hang on, I'm separating it out into patches
[2:43pm] jason-: and importing it into my queue.
[2:44pm] rlm: it also makes it so that you can automatically sanity-check the refinement function
[2:44pm] roed__ left the chat room. (Read error: 104 (Connection reset by peer))
[2:45pm] roed_ joined the chat room.
[2:47pm] jason-: the loop plotting patch has already been merged, right?
[2:47pm] rlm: yes
[2:47pm] rlm: that's 3 down, 3 to go
[2:50pm] jason-: and I don't need to look at patches 1 and 2, right?
[2:50pm] rlm: correct
[2:51pm] jason-: huh, what does:
[2:51pm] jason-: cdef int test_refine_by_square_matrix(self, int *alpha, int n, int **g, int dig) except? -1:
[2:51pm] jason-: do?
[2:52pm] jason-: (the "except?" ?)
[2:52pm] rlm: it has the same signature as refine_by_square_matrix
[2:52pm] rlm: it records the state before the function is called, and then after it calls it, and checks to make sure that the right thing is happening
[2:52pm] jason-: what is "it"?
[2:52pm] jason-: Cython?
[2:53pm] rlm:  refine_by_square_matrix is the real function
[2:53pm] rlm: test_etc just checks that  refine_by_square_matrix is doing the right thing!
[2:53pm] rlm: it's automatic debugging
[2:53pm] jason-: cool.  I was just wondering what the "except? -1:" syntax did.
[2:53pm] rlm: " except? -1" allows the function to raise an error
[2:54pm] rlm: which i do, if test_blahblahblah discovers a mistake
[2:54pm] jason-: so it looks like most of the changes are the including k as an attribute thing.
[2:55pm] jason-: the others are testing functions?
[2:55pm] rlm: yep
[2:56pm] jason-: okay.  Well, since nothing looks obviously wrong (but I'm not sure if I could spot something like that if it hit me upside the head at this point), I say to go ahead and merge it and that way I'll be looking at it when I go through the algorithm over the next little while.
[2:56pm] jason-: Besides, the testing functions will make it easier to go through the algorithm 
[2:56pm] rlm: cool.
[2:56pm] rlm: two patches left in this bundle
[2:57pm] jason-: Did I tell you that you convinced me that this review and the whole-algorithm review need to be two separate things? 
[2:57pm] rlm: I gathered as much
[2:57pm] jason-: okay, we already talked about the next one.
[2:57pm] rlm: The second to last patch in that bundle is the bug i described to you at SD7
[2:58pm] jason-: and I agreed it was good (at 3AM after a week with no sleep 
[2:58pm] rlm: haha
[2:58pm] rlm: it
[2:58pm] rlm: 's still good, since it eliminated that one bug
[2:58pm] rlm: and the last patch was the idea was also talked about at SD7, namely providing the option to turn off the indicator function, in order to expose the bug to doctesting
[2:58pm] rlm: "was" -> we
[2:59pm] jason-: so "uif" is the indicator function switch?
[2:59pm] rlm: yep
[3:00pm] jason-: okay, I say it goes in for the same reasons as above.
[3:00pm] rlm: cool, so that's the bundle
```



---

archive/issue_comments_013472.json:
```json
{
    "body": "Attachment [2085-segfault-fix.patch](tarball://root/attachments/some-uuid/ticket2085/2085-segfault-fix.patch) by @rlmill created at 2008-02-19 00:50:38",
    "created_at": "2008-02-19T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13472",
    "user": "https://github.com/rlmill"
}
```

Attachment [2085-segfault-fix.patch](tarball://root/attachments/some-uuid/ticket2085/2085-segfault-fix.patch) by @rlmill created at 2008-02-19 00:50:38



---

archive/issue_comments_013473.json:
```json
{
    "body": "I had some rejects to fix while merging 2085-auto_debug_and_bug_fix.hg after applying #1304, so please verify that I did the right thing. If loads of doctests fail you now know why. \n\nWhile I am at it: Dead to bundles!\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T15:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I had some rejects to fix while merging 2085-auto_debug_and_bug_fix.hg after applying #1304, so please verify that I did the right thing. If loads of doctests fail you now know why. 

While I am at it: Dead to bundles!

Cheers,

Michael



---

archive/issue_events_004995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-19T15:21:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2085#event-4995"
}
```



---

archive/issue_comments_013474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T15:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013475.json:
```json
{
    "body": "Merged all three bundles & patches in Sage 2.10.2.alpha1",
    "created_at": "2008-02-19T15:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2085#issuecomment-13475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three bundles & patches in Sage 2.10.2.alpha1
