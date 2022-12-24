# Issue 5850: add Creative Commons license to French tutorial

archive/issues_005850.json:
```json
{
    "body": "Assignee: tba\n\nThe French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.\n\nI could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)\n\nTicket #4809 is the English version of this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5850\n\n",
    "created_at": "2009-04-22T04:18:03Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "add Creative Commons license to French tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5850",
    "user": "@dandrake"
}
```
Assignee: tba

The French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.

I could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)

Ticket #4809 is the English version of this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/5850





---

archive/issue_comments_046159.json:
```json
{
    "body": "Attachment [sagetutfr.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr.patch) by @mezzarobba created at 2009-04-27 21:04:26",
    "created_at": "2009-04-27T21:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46159",
    "user": "@mezzarobba"
}
```

Attachment [sagetutfr.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr.patch) by @mezzarobba created at 2009-04-27 21:04:26



---

archive/issue_comments_046160.json:
```json
{
    "body": "Replying to [ticket:5850 ddrake]:\n> The French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.\n> \n> I could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)\n> \n> Ticket #4809 is the English version of this ticket.",
    "created_at": "2009-04-27T21:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46160",
    "user": "@mezzarobba"
}
```

Replying to [ticket:5850 ddrake]:
> The French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.
> 
> I could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)
> 
> Ticket #4809 is the English version of this ticket.



---

archive/issue_comments_046161.json:
```json
{
    "body": "Hi,\n\nI am one of the translators of the tutorial. I have just noticed that the French translation was added to the Sage repository by Mike Hansen... a few days before we put its proofread version on the wiki!\n\nSo I guess the best I can do now is to provide one single patch which updates the translation and fixes all the issues with it I am aware of, namely this ticket, #4318 and #5337. There had been a few changes (limited to the doctests and the build scripts) in the version of the French tutorial in the hg repository in the meantime; I have done my best to merge them with our work.\n\n-- Marc",
    "created_at": "2009-04-27T21:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46161",
    "user": "@mezzarobba"
}
```

Hi,

I am one of the translators of the tutorial. I have just noticed that the French translation was added to the Sage repository by Mike Hansen... a few days before we put its proofread version on the wiki!

So I guess the best I can do now is to provide one single patch which updates the translation and fixes all the issues with it I am aware of, namely this ticket, #4318 and #5337. There had been a few changes (limited to the doctests and the build scripts) in the version of the French tutorial in the hg repository in the meantime; I have done my best to merge them with our work.

-- Marc



---

archive/issue_comments_046162.json:
```json
{
    "body": "The patch did not quite apply to a 3.4.2.alpha0 (yes, that's a mistake above) tree, so I've uploaded a version which should apply cleanly. One problem was that now you can do ``\\QQ`` instead of something like ``\\mathbf{Q}``; I fixed all the occurrences I could find.\n\nI'm also assigning this ticket to mmezzarobba, since he did upload a patch.",
    "created_at": "2009-04-28T00:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46162",
    "user": "@dandrake"
}
```

The patch did not quite apply to a 3.4.2.alpha0 (yes, that's a mistake above) tree, so I've uploaded a version which should apply cleanly. One problem was that now you can do ``\QQ`` instead of something like ``\mathbf{Q}``; I fixed all the occurrences I could find.

I'm also assigning this ticket to mmezzarobba, since he did upload a patch.



---

archive/issue_comments_046163.json:
```json
{
    "body": "Changing assignee from tba to @mezzarobba.",
    "created_at": "2009-04-28T00:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46163",
    "user": "@dandrake"
}
```

Changing assignee from tba to @mezzarobba.



---

archive/issue_comments_046164.json:
```json
{
    "body": "patch rebased against 3.4.2.alpha0; \\QQ fixes; doctest fixes",
    "created_at": "2009-04-30T07:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46164",
    "user": "@dandrake"
}
```

patch rebased against 3.4.2.alpha0; \QQ fixes; doctest fixes



---

archive/issue_comments_046165.json:
```json
{
    "body": "Attachment [sagetutfr-updated.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr-updated.patch) by @dandrake created at 2009-04-30 07:42:13\n\nOops, I just found that the tutorial doesn't pass doctests...mostly because the doctest framework doesn't speak French, so if you have \"`# n\u00e9cessite le paquet facultatif database_gap`\", it doesn't understand that you mean \"`optional - database_gap`\". :)\n\nYou just need the magic (English) words, so you can still include explanation in French. Things like this work fine:\n\n```\nsome code # sortie plus ou moins al\u00e9atoire (random)\n\nmore code # n\u00e9cessite le paquet facultatif database_gap (optional)\n```\n\n\nI added the necessary English words to the doctests, and also added \"...\" to a Maxima doctest (at the end of tour_algebra.rst) that had random low order bits.",
    "created_at": "2009-04-30T07:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46165",
    "user": "@dandrake"
}
```

Attachment [sagetutfr-updated.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr-updated.patch) by @dandrake created at 2009-04-30 07:42:13

Oops, I just found that the tutorial doesn't pass doctests...mostly because the doctest framework doesn't speak French, so if you have "`# nécessite le paquet facultatif database_gap`", it doesn't understand that you mean "`optional - database_gap`". :)

You just need the magic (English) words, so you can still include explanation in French. Things like this work fine:

```
some code # sortie plus ou moins aléatoire (random)

more code # nécessite le paquet facultatif database_gap (optional)
```


I added the necessary English words to the doctests, and also added "..." to a Maxima doctest (at the end of tour_algebra.rst) that had random low order bits.



---

archive/issue_comments_046166.json:
```json
{
    "body": "Attachment [sagetutfr-review-nb.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr-review-nb.patch) by nborie created at 2009-06-21 23:20:10\n\n(some typo fixes)",
    "created_at": "2009-06-21T23:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46166",
    "user": "nborie"
}
```

Attachment [sagetutfr-review-nb.patch](tarball://root/attachments/some-uuid/ticket5850/sagetutfr-review-nb.patch) by nborie created at 2009-06-21 23:20:10

(some typo fixes)



---

archive/issue_comments_046167.json:
```json
{
    "body": "I added a very small patch which fix some typo in the sagetutfr-updated.patch\n\nThe patch is very good. I have learn some informations by reading it carefully. I give this patch a positive review. (First review for me...)\nBeing also French, I thank very much the authors.",
    "created_at": "2009-06-21T23:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46167",
    "user": "nborie"
}
```

I added a very small patch which fix some typo in the sagetutfr-updated.patch

The patch is very good. I have learn some informations by reading it carefully. I give this patch a positive review. (First review for me...)
Being also French, I thank very much the authors.



---

archive/issue_comments_046168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46168",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_046169.json:
```json
{
    "body": "Nicolas, thank you for your review!\n\nJust one remark: I do not know what the 'author' field is used for, but if it is meant to identify the authors of the change (as opposed to track the authors/submitters of the patches) then Bertrand Meyer should be added. Paul Zimmermann and Isma\u00ebl Bouya helped with proofreading and suggestions.",
    "created_at": "2009-06-24T19:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5850#issuecomment-46169",
    "user": "@mezzarobba"
}
```

Nicolas, thank you for your review!

Just one remark: I do not know what the 'author' field is used for, but if it is meant to identify the authors of the change (as opposed to track the authors/submitters of the patches) then Bertrand Meyer should be added. Paul Zimmermann and Ismaël Bouya helped with proofreading and suggestions.
