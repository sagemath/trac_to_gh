# Issue 8370: Add tour_functions to the French tutorial (cf. #5463)

archive/issues_008370.json:
```json
{
    "body": "Assignee: @mezzarobba\n\nCC:  abmasse\n\ntour_functions.rst (added by #5463) is missing from the French translation of the tutorial\n\nIssue created by migration from https://trac.sagemath.org/ticket/8370\n\n",
    "created_at": "2010-02-25T23:00:17Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Add tour_functions to the French tutorial (cf. #5463)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8370",
    "user": "@mezzarobba"
}
```
Assignee: @mezzarobba

CC:  abmasse

tour_functions.rst (added by #5463) is missing from the French translation of the tutorial

Issue created by migration from https://trac.sagemath.org/ticket/8370





---

archive/issue_comments_074815.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T09:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74815",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074816.json:
```json
{
    "body": "Attachment [trac_8370_tour_functions_french.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_tour_functions_french.patch) by @mezzarobba created at 2010-02-27 09:20:38",
    "created_at": "2010-02-27T09:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74816",
    "user": "@mezzarobba"
}
```

Attachment [trac_8370_tour_functions_french.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_tour_functions_french.patch) by @mezzarobba created at 2010-02-27 09:20:38



---

archive/issue_comments_074817.json:
```json
{
    "body": "Hello, Marc !\n\nThis is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?\n\nI'll start looking at your patch today.",
    "created_at": "2010-03-06T09:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74817",
    "user": "abmasse"
}
```

Hello, Marc !

This is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?

I'll start looking at your patch today.



---

archive/issue_comments_074818.json:
```json
{
    "body": "A very stupid question : how can I generate the French documentation ? I'll try to find out, but if you read this message before I find out, don't hesitate to enlighten me !\n\nThank you.",
    "created_at": "2010-03-06T10:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74818",
    "user": "abmasse"
}
```

A very stupid question : how can I generate the French documentation ? I'll try to find out, but if you read this message before I find out, don't hesitate to enlighten me !

Thank you.



---

archive/issue_comments_074819.json:
```json
{
    "body": "Never mind, I just found out.\n\n\n```\nsage -docbuild fr/tutorial html\n```\n",
    "created_at": "2010-03-06T10:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74819",
    "user": "abmasse"
}
```

Never mind, I just found out.


```
sage -docbuild fr/tutorial html
```




---

archive/issue_comments_074820.json:
```json
{
    "body": "Minor rephrasing and doc syntax fixes -- apply on top of the other patch",
    "created_at": "2010-03-06T12:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74820",
    "user": "abmasse"
}
```

Minor rephrasing and doc syntax fixes -- apply on top of the other patch



---

archive/issue_comments_074821.json:
```json
{
    "body": "Attachment [trac_8370_review-abm.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_review-abm.patch) by abmasse created at 2010-03-06 12:24:08\n\nHello again Marc !\nI reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.\n\n1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.\n\n2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.\n\n3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.\n\n4. You forgot to put the word \"plot\" between backticks in one place. I corrected that.\n\nThat's pretty much it. As soon as you confirm my changes, I'll be ready to set this ticket to positive review.",
    "created_at": "2010-03-06T12:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74821",
    "user": "abmasse"
}
```

Attachment [trac_8370_review-abm.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_review-abm.patch) by abmasse created at 2010-03-06 12:24:08

Hello again Marc !
I reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.

1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.

2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.

3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.

4. You forgot to put the word "plot" between backticks in one place. I corrected that.

That's pretty much it. As soon as you confirm my changes, I'll be ready to set this ticket to positive review.



---

archive/issue_comments_074822.json:
```json
{
    "body": "Sorry for the delay.\n\nReplying to [comment:2 abmasse]:\n> This is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?\n\nIndeed.\n\nReplying to [comment:5 abmasse]:\n> I reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.\n> \n> 1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.\n\nHere I just stuck to the style of the English version.  But you are right that (most?) other sections of the original tutorial use four spaces.\n\n> 2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.\n\nSame here, except that the format with `::` on its own line seems to be used consistently in the tutorial (in both languages).  I don't think it's a big deal anyway.\n\nHowever, in some cases, you put a space between the `::` and the preceding word, so that there is no colon (and no period either) in the output.  Was that deliberate?  \n\n> 3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.\n> \n> 4. You forgot to put the word \"plot\" between backticks in one place. I corrected that.\n\nSeems fine to me. Btw, I also checked that the our patches apply correctly on top of 4.3.4 + patches from #8242.",
    "created_at": "2010-03-26T21:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74822",
    "user": "@mezzarobba"
}
```

Sorry for the delay.

Replying to [comment:2 abmasse]:
> This is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?

Indeed.

Replying to [comment:5 abmasse]:
> I reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.
> 
> 1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.

Here I just stuck to the style of the English version.  But you are right that (most?) other sections of the original tutorial use four spaces.

> 2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.

Same here, except that the format with `::` on its own line seems to be used consistently in the tutorial (in both languages).  I don't think it's a big deal anyway.

However, in some cases, you put a space between the `::` and the preceding word, so that there is no colon (and no period either) in the output.  Was that deliberate?  

> 3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.
> 
> 4. You forgot to put the word "plot" between backticks in one place. I corrected that.

Seems fine to me. Btw, I also checked that the our patches apply correctly on top of 4.3.4 + patches from #8242.



---

archive/issue_comments_074823.json:
```json
{
    "body": "Hello !!! This new patch is a concatenation of the two previous given, plus two unimportant fixes for a broken doctest :-)\n\nDo you agree to set it to positive review ? It applied fine, it is indeed french and everything is nicely formatted !!\n\nNathann",
    "created_at": "2010-04-04T15:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74823",
    "user": "@nathanncohen"
}
```

Hello !!! This new patch is a concatenation of the two previous given, plus two unimportant fixes for a broken doctest :-)

Do you agree to set it to positive review ? It applied fine, it is indeed french and everything is nicely formatted !!

Nathann



---

archive/issue_comments_074824.json:
```json
{
    "body": "Attachment [trac_8370_merged+doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_merged+doctest_fixes.patch) by abmasse created at 2010-04-06 19:10:21\n\nHello, Marc and Nathann ! Sorry for the delay...\n\nNathann, I can't see what changes you made with the merged patch. Could you please add a patch that contains only your changes and that applies on top of the two patches Marc and I have attached so far ? This way, it'll be easier to review.\n\nThank you !",
    "created_at": "2010-04-06T19:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74824",
    "user": "abmasse"
}
```

Attachment [trac_8370_merged+doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_merged+doctest_fixes.patch) by abmasse created at 2010-04-06 19:10:21

Hello, Marc and Nathann ! Sorry for the delay...

Nathann, I can't see what changes you made with the merged patch. Could you please add a patch that contains only your changes and that applies on top of the two patches Marc and I have attached so far ? This way, it'll be easier to review.

Thank you !



---

archive/issue_comments_074825.json:
```json
{
    "body": "Here it is ! :-)\n\nNathann",
    "created_at": "2010-04-08T11:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74825",
    "user": "@nathanncohen"
}
```

Here it is ! :-)

Nathann



---

archive/issue_comments_074826.json:
```json
{
    "body": "Attachment [trac_8370_fixes.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_fixes.patch) by abmasse created at 2010-04-15 20:38:22\n\nHello, everyone !\n\nI'm very sorry for the delay... I just moved back to Montreal and haven't had much time lately to work on Sage patches. I looked once again at the three patches, applied them, checked the documentation generated by Sage and run `sage -t` on the `tour_functions.rst` file. Everything looked fine and all tests passed. Therefore, I give this patch a positive review.\n\nFor the release manager, please apply the patches in the following order\n\n\n```\ntrac_8370_tour_functions_french.patch\ntrac_8370_review-abm.patch\ntrac_8370_fixes.patch\n```\n\n\nand disregard `trac_8370_merged+doctest_fixes.patch`.\n\nThank you for your patience!",
    "created_at": "2010-04-15T20:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74826",
    "user": "abmasse"
}
```

Attachment [trac_8370_fixes.patch](tarball://root/attachments/some-uuid/ticket8370/trac_8370_fixes.patch) by abmasse created at 2010-04-15 20:38:22

Hello, everyone !

I'm very sorry for the delay... I just moved back to Montreal and haven't had much time lately to work on Sage patches. I looked once again at the three patches, applied them, checked the documentation generated by Sage and run `sage -t` on the `tour_functions.rst` file. Everything looked fine and all tests passed. Therefore, I give this patch a positive review.

For the release manager, please apply the patches in the following order


```
trac_8370_tour_functions_french.patch
trac_8370_review-abm.patch
trac_8370_fixes.patch
```


and disregard `trac_8370_merged+doctest_fixes.patch`.

Thank you for your patience!



---

archive/issue_comments_074827.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T20:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74827",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074828.json:
```json
{
    "body": "Excellent ! I'll be in Montreal in the early days of may, btw ;-)\n\nNathann",
    "created_at": "2010-04-15T20:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74828",
    "user": "@nathanncohen"
}
```

Excellent ! I'll be in Montreal in the early days of may, btw ;-)

Nathann



---

archive/issue_comments_074829.json:
```json
{
    "body": "Nice! See you then!\n\nBy the way, I forgot to mention that I tested the three patches on sage-4.3.5.",
    "created_at": "2010-04-15T21:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74829",
    "user": "abmasse"
}
```

Nice! See you then!

By the way, I forgot to mention that I tested the three patches on sage-4.3.5.



---

archive/issue_comments_074830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8370#issuecomment-74830",
    "user": "@williamstein"
}
```

Resolution: fixed
