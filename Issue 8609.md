# Issue 8609: Switch AmbientSpace and Scheme to Parent

archive/issues_008609.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe patch switches AmbientSpace and Scheme to inherit from Parent rather than old-style classes. I used to get random segfaults in \"sage -testall\" with this patch applied, but with 4.3.3 it seems to be smooth and in anyway the patch is very simple and should not introduce new bugs.\n\nTo \"fix\" broken doctests because of the missing list() method I have just removed them, since they were in functions not directly related to list() anyway.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8609\n\n",
    "created_at": "2010-03-25T22:39:30Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Switch AmbientSpace and Scheme to Parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8609",
    "user": "novoselt"
}
```
Assignee: AlexGhitza

The patch switches AmbientSpace and Scheme to inherit from Parent rather than old-style classes. I used to get random segfaults in "sage -testall" with this patch applied, but with 4.3.3 it seems to be smooth and in anyway the patch is very simple and should not introduce new bugs.

To "fix" broken doctests because of the missing list() method I have just removed them, since they were in functions not directly related to list() anyway.

Issue created by migration from https://trac.sagemath.org/ticket/8609





---

archive/issue_comments_077989.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-25T22:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77989",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077990.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-25T22:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77990",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_077991.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-02T15:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77991",
    "user": "cremona"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_077992.json:
```json
{
    "body": "Patch applies fine to 4.3.5.  Testing all and will report back....\n\nAndrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!",
    "created_at": "2010-04-02T15:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77992",
    "user": "cremona"
}
```

Patch applies fine to 4.3.5.  Testing all and will report back....

Andrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!



---

archive/issue_comments_077993.json:
```json
{
    "body": "All tests pass.  I'll give this a positive review as soon as I know the reason for it!",
    "created_at": "2010-04-02T15:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77993",
    "user": "cremona"
}
```

All tests pass.  I'll give this a positive review as soon as I know the reason for it!



---

archive/issue_comments_077994.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-04-02T15:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77994",
    "user": "novoselt"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_077995.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> Patch applies fine to 4.3.5.  Testing all and will report back....\n> \n> Andrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!\n\nYeah, I should have probably explained it better. I am working on support for (Fano) toric varieties and Calabi-Yau hypersurfaces/complete intersections inside (with a hope to finish by this summer). So when I was going over schemes/general to figure out what is already there and what do I need to do to fit nicely into existing framework, I got this question:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/ddb9f2c592082c02/4120466d01cacae0#4120466d01cacae0\nand wrote the patch. It took me a while to post it due to those Segfaults that ALWAYS were appearing with the patch during non-parallel testing, although in different/unrelated places. Now I did manage to get at least one clean run and think that it should go in. After all, as I understand it, if this patch causes problems, it is because it exposes some deeper bugs in Sage and it actually can be nice if they become more visible...\n\nI also wanted to make the following change (I don't have a ready-to-review patch for this one, but can make one quickly), but nobody got interested in discussing it and I don't think such changes should happen silently:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/1279e373341da951/e0efa737426d5b19#e0efa737426d5b19\n\nThank you!",
    "created_at": "2010-04-02T15:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77995",
    "user": "novoselt"
}
```

Replying to [comment:2 cremona]:
> Patch applies fine to 4.3.5.  Testing all and will report back....
> 
> Andrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!

Yeah, I should have probably explained it better. I am working on support for (Fano) toric varieties and Calabi-Yau hypersurfaces/complete intersections inside (with a hope to finish by this summer). So when I was going over schemes/general to figure out what is already there and what do I need to do to fit nicely into existing framework, I got this question:
http://groups.google.com/group/sage-devel/browse_thread/thread/ddb9f2c592082c02/4120466d01cacae0#4120466d01cacae0
and wrote the patch. It took me a while to post it due to those Segfaults that ALWAYS were appearing with the patch during non-parallel testing, although in different/unrelated places. Now I did manage to get at least one clean run and think that it should go in. After all, as I understand it, if this patch causes problems, it is because it exposes some deeper bugs in Sage and it actually can be nice if they become more visible...

I also wanted to make the following change (I don't have a ready-to-review patch for this one, but can make one quickly), but nobody got interested in discussing it and I don't think such changes should happen silently:
http://groups.google.com/group/sage-devel/browse_thread/thread/1279e373341da951/e0efa737426d5b19#e0efa737426d5b19

Thank you!



---

archive/issue_comments_077996.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T15:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77996",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077997.json:
```json
{
    "body": "Thanks for the explanation -- and sorry for delay, I did not get a message from trac to say that you had replied.  Anyway -- positive review.",
    "created_at": "2010-04-05T15:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77997",
    "user": "cremona"
}
```

Thanks for the explanation -- and sorry for delay, I did not get a message from trac to say that you had replied.  Anyway -- positive review.



---

archive/issue_comments_077998.json:
```json
{
    "body": "Merged \"trac_8609_switch_ambient_space_and_scheme_to_parent.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77998",
    "user": "jhpalmieri"
}
```

Merged "trac_8609_switch_ambient_space_and_scheme_to_parent.patch" in 4.4.alpha0



---

archive/issue_comments_077999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8609#issuecomment-77999",
    "user": "jhpalmieri"
}
```

Resolution: fixed
