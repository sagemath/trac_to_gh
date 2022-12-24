# Issue 9395: new doctest for french book about Sage

archive/issues_009395.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  was cremona ylchapuy\n\nThe attached patch includes a new doctest for a book (in french) some\npeople are writing about Sage (see the README file for the list of\nauthors).\n\nThis book will be available under a CC-by-sa license.\n\nThis patch contains only the doctests for one chapter (about number\ntheory). Some more doctests will follow, one per chapter, but we\nalready submit that one to see if some things need to be fixed.\n\nThis doctest was tested successfully with Sage 4.4.2 under Fedora 12.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9395\n\n",
    "created_at": "2010-06-30T13:14:12Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "new doctest for french book about Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9395",
    "user": "zimmerma"
}
```
Assignee: mvngu

CC:  was cremona ylchapuy

The attached patch includes a new doctest for a book (in french) some
people are writing about Sage (see the README file for the list of
authors).

This book will be available under a CC-by-sa license.

This patch contains only the doctests for one chapter (about number
theory). Some more doctests will follow, one per chapter, but we
already submit that one to see if some things need to be fixed.

This doctest was tested successfully with Sage 4.4.2 under Fedora 12.

Issue created by migration from https://trac.sagemath.org/ticket/9395





---

archive/issue_comments_089440.json:
```json
{
    "body": "I found no way so that the `%timeit ...` or `time ...` lines are tested, thus I've added\n`# not tested`. If somebody knows how to do so that in `%timeit a = b + c` at least the\ninstruction `a = b + c` is performed, please tell me.",
    "created_at": "2010-06-30T13:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89440",
    "user": "zimmerma"
}
```

I found no way so that the `%timeit ...` or `time ...` lines are tested, thus I've added
`# not tested`. If somebody knows how to do so that in `%timeit a = b + c` at least the
instruction `a = b + c` is performed, please tell me.



---

archive/issue_comments_089441.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-30T13:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89441",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089442.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-30T13:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89442",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089443.json:
```json
{
    "body": "You don't need to put your doctests inside a function. I think it's much simpler to put your doctests inside a docstring. See the files under tests/ in the Sage library for examples. You should also consider giving your book's directory name a more descriptive name. Something like \"number_theory_zimmermann\", not just \"sagebook\". Or do you envision the directory \"sagebook\" to contain doctests of books that leverage the Sage doctesting framework? In that case, see [this script](http://www.bitbucket.org/mvngu/textract) for a proof of concept for automatic extraction of Sage code and doctesting the extracted code. That script has been tested on this [Sage book](http://code.google.com/p/factor-book/).",
    "created_at": "2010-06-30T13:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89443",
    "user": "mvngu"
}
```

You don't need to put your doctests inside a function. I think it's much simpler to put your doctests inside a docstring. See the files under tests/ in the Sage library for examples. You should also consider giving your book's directory name a more descriptive name. Something like "number_theory_zimmermann", not just "sagebook". Or do you envision the directory "sagebook" to contain doctests of books that leverage the Sage doctesting framework? In that case, see [this script](http://www.bitbucket.org/mvngu/textract) for a proof of concept for automatic extraction of Sage code and doctesting the extracted code. That script has been tested on this [Sage book](http://code.google.com/p/factor-book/).



---

archive/issue_comments_089444.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n\nthe new patch addresses your remarks.\n\nPaul",
    "created_at": "2010-06-30T14:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89444",
    "user": "zimmerma"
}
```

Replying to [comment:3 mvngu]:

the new patch addresses your remarks.

Paul



---

archive/issue_comments_089445.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T14:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89445",
    "user": "zimmerma"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089446.json:
```json
{
    "body": "Attachment [intro.pdf](tarball://root/attachments/some-uuid/ticket9395/intro.pdf) by zimmerma created at 2010-07-01 08:48:54\n\ntable of contents of the book",
    "created_at": "2010-07-01T08:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89446",
    "user": "zimmerma"
}
```

Attachment [intro.pdf](tarball://root/attachments/some-uuid/ticket9395/intro.pdf) by zimmerma created at 2010-07-01 08:48:54

table of contents of the book



---

archive/issue_comments_089447.json:
```json
{
    "body": "current version of chapter on number theory",
    "created_at": "2010-07-01T08:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89447",
    "user": "zimmerma"
}
```

current version of chapter on number theory



---

archive/issue_comments_089448.json:
```json
{
    "body": "Attachment [numbertheory.pdf](tarball://root/attachments/some-uuid/ticket9395/numbertheory.pdf) by zimmerma created at 2010-07-09 11:00:47\n\nThe version 1.0 of the book has now appeared, and is available from\nhttp://www.loria.fr/~zimmerma/sagebook.html. Any feedback is most welcome!",
    "created_at": "2010-07-09T11:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89448",
    "user": "zimmerma"
}
```

Attachment [numbertheory.pdf](tarball://root/attachments/some-uuid/ticket9395/numbertheory.pdf) by zimmerma created at 2010-07-09 11:00:47

The version 1.0 of the book has now appeared, and is available from
http://www.loria.fr/~zimmerma/sagebook.html. Any feedback is most welcome!



---

archive/issue_comments_089449.json:
```json
{
    "body": "Yann, please could you review this? What you have to do (William please correct me if needed):\n\n1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write \"optional\" since this should be our (the authors of the book) responsability.\n\n2) check the new doctests pass with the latest Sage version (we used 4.4.4)\n\nPaul",
    "created_at": "2010-07-12T11:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89449",
    "user": "zimmerma"
}
```

Yann, please could you review this? What you have to do (William please correct me if needed):

1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write "optional" since this should be our (the authors of the book) responsability.

2) check the new doctests pass with the latest Sage version (we used 4.4.4)

Paul



---

archive/issue_comments_089450.json:
```json
{
    "body": "Replying to [comment:6 zimmerma]:\n> Yann, please could you review this? What you have to do (William please correct me if needed):\n\nSounds good to me. \n\nI've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).",
    "created_at": "2010-07-12T20:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89450",
    "user": "was"
}
```

Replying to [comment:6 zimmerma]:
> Yann, please could you review this? What you have to do (William please correct me if needed):

Sounds good to me. 

I've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).



---

archive/issue_comments_089451.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> I've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).\nthanks, some people of my lab who were at Euroscipy indeed told me today that they heard of our book there!\nPaul",
    "created_at": "2010-07-12T21:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89451",
    "user": "zimmerma"
}
```

Replying to [comment:7 was]:
> I've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).
thanks, some people of my lab who were at Euroscipy indeed told me today that they heard of our book there!
Paul



---

archive/issue_comments_089452.json:
```json
{
    "body": "Replying to [comment:6 zimmerma]:\n> Yann, please could you review this? What you have to do (William please correct me if needed):\n> \n> 1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write \"optional\" since this should be our (the authors of the book) responsability.\n> \n> 2) check the new doctests pass with the latest Sage version (we used 4.4.4)\n> \n> Paul\n\nSorry for the delay.\nAll tests passed with Sage 4.5.2.\n\nRegarding the `timeit` issue, you could change \n\n```\n    sage: %timeit (a^e) # not tested\n```\n\nfor\n\n```\n    sage: timeit('a^e') # random\n```\n\n\n(and also `# long` for some of them).\n\nI put it to `need info` for now, but feel free either to change this and ask me for a review (I'll be faster this time) or don't change anything and give a positive review.\n\n Yann",
    "created_at": "2010-08-15T21:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89452",
    "user": "ylchapuy"
}
```

Replying to [comment:6 zimmerma]:
> Yann, please could you review this? What you have to do (William please correct me if needed):
> 
> 1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write "optional" since this should be our (the authors of the book) responsability.
> 
> 2) check the new doctests pass with the latest Sage version (we used 4.4.4)
> 
> Paul

Sorry for the delay.
All tests passed with Sage 4.5.2.

Regarding the `timeit` issue, you could change 

```
    sage: %timeit (a^e) # not tested
```

for

```
    sage: timeit('a^e') # random
```


(and also `# long` for some of them).

I put it to `need info` for now, but feel free either to change this and ask me for a review (I'll be faster this time) or don't change anything and give a positive review.

 Yann



---

archive/issue_comments_089453.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-08-15T21:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89453",
    "user": "ylchapuy"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_089454.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-01T16:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89454",
    "user": "zimmerma"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_089455.json:
```json
{
    "body": "thank you Yann for your comments. I attach a new patch taking them into account. I left the\nlast `time r=...` as `not tested` since I do not know how to make it work, without\nchanging `time` into `timeit`, which would be not coherent with the book.\n\nPaul",
    "created_at": "2010-09-01T16:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89455",
    "user": "zimmerma"
}
```

thank you Yann for your comments. I attach a new patch taking them into account. I left the
last `time r=...` as `not tested` since I do not know how to make it work, without
changing `time` into `timeit`, which would be not coherent with the book.

Paul



---

archive/issue_comments_089456.json:
```json
{
    "body": "Attachment [trac_9395.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395.patch) by zimmerma created at 2010-09-01 16:09:55",
    "created_at": "2010-09-01T16:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89456",
    "user": "zimmerma"
}
```

Attachment [trac_9395.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395.patch) by zimmerma created at 2010-09-01 16:09:55



---

archive/issue_comments_089457.json:
```json
{
    "body": "apply on top of trac_9395.patch",
    "created_at": "2010-09-01T17:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89457",
    "user": "ylchapuy"
}
```

apply on top of trac_9395.patch



---

archive/issue_comments_089458.json:
```json
{
    "body": "Attachment [trac_9395_review.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395_review.patch) by ylchapuy created at 2010-09-01 17:33:34\n\nEverything is still ok for me. I added 'long time' to the longest tests, this reduces the time for normal testing to 12 seconds on my computer compared to 67 for the long version.\n\nPaul, if you agree with my reviewer's patch, you can give this ticket a positive review.\n\n       Yann",
    "created_at": "2010-09-01T17:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89458",
    "user": "ylchapuy"
}
```

Attachment [trac_9395_review.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395_review.patch) by ylchapuy created at 2010-09-01 17:33:34

Everything is still ok for me. I added 'long time' to the longest tests, this reduces the time for normal testing to 12 seconds on my computer compared to 67 for the long version.

Paul, if you agree with my reviewer's patch, you can give this ticket a positive review.

       Yann



---

archive/issue_comments_089459.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-01T19:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89459",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089460.json:
```json
{
    "body": "> Paul, if you agree with my reviewer's patch, you can give this ticket a positive review. \n\nyes I agree.\nPaul",
    "created_at": "2010-09-01T19:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89460",
    "user": "zimmerma"
}
```

> Paul, if you agree with my reviewer's patch, you can give this ticket a positive review. 

yes I agree.
Paul



---

archive/issue_comments_089461.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-05T03:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89461",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_089462.json:
```json
{
    "body": "Could someone please update both patches with more descriptive commit strings (and change the status back to \"positive review\")?",
    "created_at": "2010-09-05T03:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89462",
    "user": "mpatel"
}
```

Could someone please update both patches with more descriptive commit strings (and change the status back to "positive review")?



---

archive/issue_comments_089463.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Could someone please update both patches with more descriptive commit strings (and change the status back to \"positive review\")?\n\ndone with a combined patch (apply only that one). Is that what you wanted?\n\nPaul",
    "created_at": "2010-09-06T18:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89463",
    "user": "zimmerma"
}
```

Replying to [comment:13 mpatel]:
> Could someone please update both patches with more descriptive commit strings (and change the status back to "positive review")?

done with a combined patch (apply only that one). Is that what you wanted?

Paul



---

archive/issue_comments_089464.json:
```json
{
    "body": "I apologize for not being clearer.  The first line of the commit string for each patch to be merged should start with the ticket number and contain a short description of what the patch does.  This line should be < 80 characters in length.\n\nFor example: `#9395: Number theory doctests for French book about Sage` and `#9395: Reviewer patch: tag longest tests as long`.\n\nThe reason for these policies is so that `hg log` and `hg log filename.py` tell us what a changeset did and which Sage trac ticket we can consult for background.\n\nOf course, extra lines are welcome and may help to explain details to a reviewer or someone who uses `hg log -p`.\n\nCould you update the just first line of the combined patch?",
    "created_at": "2010-09-06T21:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89464",
    "user": "mpatel"
}
```

I apologize for not being clearer.  The first line of the commit string for each patch to be merged should start with the ticket number and contain a short description of what the patch does.  This line should be < 80 characters in length.

For example: `#9395: Number theory doctests for French book about Sage` and `#9395: Reviewer patch: tag longest tests as long`.

The reason for these policies is so that `hg log` and `hg log filename.py` tell us what a changeset did and which Sage trac ticket we can consult for background.

Of course, extra lines are welcome and may help to explain details to a reviewer or someone who uses `hg log -p`.

Could you update the just first line of the combined patch?



---

archive/issue_comments_089465.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-09-07T08:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89465",
    "user": "zimmerma"
}
```

apply only this patch



---

archive/issue_comments_089466.json:
```json
{
    "body": "Attachment [trac_9395_combined.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395_combined.patch) by zimmerma created at 2010-09-07 08:14:04\n\n> Could you update the just first line of the combined patch? \n\ndone.\nPaul",
    "created_at": "2010-09-07T08:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89466",
    "user": "zimmerma"
}
```

Attachment [trac_9395_combined.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395_combined.patch) by zimmerma created at 2010-09-07 08:14:04

> Could you update the just first line of the combined patch? 

done.
Paul



---

archive/issue_comments_089467.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-07T08:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89467",
    "user": "zimmerma"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_089468.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89468",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_089469.json:
```json
{
    "body": "Attachment [trac_9395-manifest_and_setup.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395-manifest_and_setup.patch) by mpatel created at 2010-09-17 02:58:09\n\nUpdate `MANIFEST.in` and `setup.py` with new file and directory",
    "created_at": "2010-09-17T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89469",
    "user": "mpatel"
}
```

Attachment [trac_9395-manifest_and_setup.patch](tarball://root/attachments/some-uuid/ticket9395/trac_9395-manifest_and_setup.patch) by mpatel created at 2010-09-17 02:58:09

Update `MANIFEST.in` and `setup.py` with new file and directory



---

archive/issue_comments_089470.json:
```json
{
    "body": "I've added a release manager's patch that ensures the files added here are included in a new Sage source distribution.",
    "created_at": "2010-09-17T02:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89470",
    "user": "mpatel"
}
```

I've added a release manager's patch that ensures the files added here are included in a new Sage source distribution.



---

archive/issue_comments_089471.json:
```json
{
    "body": "Ticket #9951, about a missing `__init__.py` file, follows up on this ticket.",
    "created_at": "2010-09-19T21:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9395#issuecomment-89471",
    "user": "mpatel"
}
```

Ticket #9951, about a missing `__init__.py` file, follows up on this ticket.
