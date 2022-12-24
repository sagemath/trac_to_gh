# Issue 7973: Documentation for submitting a patch is overly confusing

archive/issues_007973.json:
```json
{
    "body": "Assignee: mvngu\n\n\"Producing patches with Mercurial\" is overly informative and thus hides the basic info.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7973\n\n",
    "created_at": "2010-01-18T07:06:59Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Documentation for submitting a patch is overly confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7973",
    "user": "gaer"
}
```
Assignee: mvngu

"Producing patches with Mercurial" is overly informative and thus hides the basic info.

Issue created by migration from https://trac.sagemath.org/ticket/7973





---

archive/issue_comments_069546.json:
```json
{
    "body": "Is this a duplicate of #6987?",
    "created_at": "2010-01-18T07:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69546",
    "user": "mvngu"
}
```

Is this a duplicate of #6987?



---

archive/issue_comments_069547.json:
```json
{
    "body": "Attachment [13639.patch](tarball://root/attachments/some-uuid/ticket7973/13639.patch) by gaer created at 2010-01-18 07:52:15\n\nMercurial documentation simplifications/patches",
    "created_at": "2010-01-18T07:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69547",
    "user": "gaer"
}
```

Attachment [13639.patch](tarball://root/attachments/some-uuid/ticket7973/13639.patch) by gaer created at 2010-01-18 07:52:15

Mercurial documentation simplifications/patches



---

archive/issue_comments_069548.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T07:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69548",
    "user": "gaer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069549.json:
```json
{
    "body": "This is not the same as 6987 which suggests moving the entire section to a different location in the manual.  That might be a good idea, but this is a revision of the actual content, not a change in the location.  \n\nAnd one probably shouldn't perform the location changes requested in 6987 without first applying the above patch to the actual text.",
    "created_at": "2010-01-18T07:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69549",
    "user": "gaer"
}
```

This is not the same as 6987 which suggests moving the entire section to a different location in the manual.  That might be a good idea, but this is a revision of the actual content, not a change in the location.  

And one probably shouldn't perform the location changes requested in 6987 without first applying the above patch to the actual text.



---

archive/issue_comments_069550.json:
```json
{
    "body": "Attachment [13639_01.patch](tarball://root/attachments/some-uuid/ticket7973/13639_01.patch) by mvngu created at 2010-01-18 08:11:34\n\nfor reference only; don't apply",
    "created_at": "2010-01-18T08:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69550",
    "user": "mvngu"
}
```

Attachment [13639_01.patch](tarball://root/attachments/some-uuid/ticket7973/13639_01.patch) by mvngu created at 2010-01-18 08:11:34

for reference only; don't apply



---

archive/issue_comments_069551.json:
```json
{
    "body": "for reference only; don't apply",
    "created_at": "2010-01-18T08:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69551",
    "user": "mvngu"
}
```

for reference only; don't apply



---

archive/issue_comments_069552.json:
```json
{
    "body": "Attachment [13639_02.patch](tarball://root/attachments/some-uuid/ticket7973/13639_02.patch) by mvngu created at 2010-01-18 08:12:09\n\nfor reference only; don't apply",
    "created_at": "2010-01-18T08:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69552",
    "user": "mvngu"
}
```

Attachment [13639_02.patch](tarball://root/attachments/some-uuid/ticket7973/13639_02.patch) by mvngu created at 2010-01-18 08:12:09

for reference only; don't apply



---

archive/issue_comments_069553.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-18T08:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69553",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069554.json:
```json
{
    "body": "Attachment [13639_03.patch](tarball://root/attachments/some-uuid/ticket7973/13639_03.patch) by mvngu created at 2010-01-18 08:17:05\n\nYou're concatenating three different patches into one file. That would result in failures when applying the resulting one file (with the three patches):\n\n```\n[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7973/13639.patch && hg qpush\nadding 13639.patch to series file\napplying 13639.patch\npatching file doc/en/developer/producing_patches.rst\nHunk #1 FAILED at 21\nHunk #2 FAILED at 58\n2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej\npatching file doc/en/developer/producing_patches.rst\nHunk #1 FAILED at 21\nHunk #2 FAILED at 58\n2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 13639.patch\n```\n\nLooking at the attachment [13639.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.patch) more closely, I see that the three patches only touch the file\n\n```\ndoc/en/developer/producing_patches.rst\n```\n\nI have split the three different patches into three different files and attached them to this ticket for reference. Applying any one of them individually is OK. But if I then first apply one and then any of the other two, I'd get hunk failures. So of all the changes in your original attachment, which set of changes did you intend to submit for review? Also, one minor nit-pick: please reference the ticket number in your commit message. The general format of a commit message should be:\n\n```\ntrac xxxx: <your-commit-message-here>\n```\n\nwhere \"xxxx\" is the ticket number.",
    "created_at": "2010-01-18T08:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69554",
    "user": "mvngu"
}
```

Attachment [13639_03.patch](tarball://root/attachments/some-uuid/ticket7973/13639_03.patch) by mvngu created at 2010-01-18 08:17:05

You're concatenating three different patches into one file. That would result in failures when applying the resulting one file (with the three patches):

```
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7973/13639.patch && hg qpush
adding 13639.patch to series file
applying 13639.patch
patching file doc/en/developer/producing_patches.rst
Hunk #1 FAILED at 21
Hunk #2 FAILED at 58
2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej
patching file doc/en/developer/producing_patches.rst
Hunk #1 FAILED at 21
Hunk #2 FAILED at 58
2 out of 2 hunks FAILED -- saving rejects to file doc/en/developer/producing_patches.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 13639.patch
```

Looking at the attachment [13639.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.patch) more closely, I see that the three patches only touch the file

```
doc/en/developer/producing_patches.rst
```

I have split the three different patches into three different files and attached them to this ticket for reference. Applying any one of them individually is OK. But if I then first apply one and then any of the other two, I'd get hunk failures. So of all the changes in your original attachment, which set of changes did you intend to submit for review? Also, one minor nit-pick: please reference the ticket number in your commit message. The general format of a commit message should be:

```
trac xxxx: <your-commit-message-here>
```

where "xxxx" is the ticket number.



---

archive/issue_comments_069555.json:
```json
{
    "body": "Attachment [13639.2.patch](tarball://root/attachments/some-uuid/ticket7973/13639.2.patch) by gaer created at 2010-01-18 09:01:41\n\nRevised patching doc patch",
    "created_at": "2010-01-18T09:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69555",
    "user": "gaer"
}
```

Attachment [13639.2.patch](tarball://root/attachments/some-uuid/ticket7973/13639.2.patch) by gaer created at 2010-01-18 09:01:41

Revised patching doc patch



---

archive/issue_comments_069556.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T09:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69556",
    "user": "gaer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069557.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2010-01-18T09:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69557",
    "user": "mvngu"
}
```

reviewer patch



---

archive/issue_comments_069558.json:
```json
{
    "body": "Attachment [trac_7973-reviewer.patch](tarball://root/attachments/some-uuid/ticket7973/trac_7973-reviewer.patch) by mvngu created at 2010-01-18 10:01:38\n\nI'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.",
    "created_at": "2010-01-18T10:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69558",
    "user": "mvngu"
}
```

Attachment [trac_7973-reviewer.patch](tarball://root/attachments/some-uuid/ticket7973/trac_7973-reviewer.patch) by mvngu created at 2010-01-18 10:01:38

I'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.



---

archive/issue_comments_069559.json:
```json
{
    "body": "Now wait, what's wrong with \"Cardinal Fang\"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), \n\n```\nMaking references to Monty Python skits in documentation is not only allowed, it is encouraged!\n```\n\nSince Sage is written in Python, \"Cardinal Fang\" seems completely appropriate. :)",
    "created_at": "2010-01-18T15:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69559",
    "user": "jhpalmieri"
}
```

Now wait, what's wrong with "Cardinal Fang"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), 

```
Making references to Monty Python skits in documentation is not only allowed, it is encouraged!
```

Since Sage is written in Python, "Cardinal Fang" seems completely appropriate. :)



---

archive/issue_comments_069560.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n> Now wait, what's wrong with \"Cardinal Fang\"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), \n> {{{\n> Making references to Monty Python skits in documentation is not only allowed, it is encouraged!\n> }}}\n> Since Sage is written in Python, \"Cardinal Fang\" seems completely appropriate. :)\n> \n\nThat change was a direct request from wstein, who is, apparently, the anti-Python(Monty). :-)",
    "created_at": "2010-01-18T20:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69560",
    "user": "gaer"
}
```

Replying to [comment:6 jhpalmieri]:
> Now wait, what's wrong with "Cardinal Fang"?  According to [the Python documentation](http://docs.python.org/tutorial/appetite.html), 
> {{{
> Making references to Monty Python skits in documentation is not only allowed, it is encouraged!
> }}}
> Since Sage is written in Python, "Cardinal Fang" seems completely appropriate. :)
> 

That change was a direct request from wstein, who is, apparently, the anti-Python(Monty). :-)



---

archive/issue_comments_069561.json:
```json
{
    "body": "Replying to [comment:5 mvngu]:\n> I'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.\n\nAll those reviewer changes are spot on.  Thanks!  It's good to go for me.",
    "created_at": "2010-01-18T20:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69561",
    "user": "gaer"
}
```

Replying to [comment:5 mvngu]:
> I'm OK with the proposed changes in [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch). I have attached a reviewer patch [trac_7973-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/trac_7973-reviewer.patch), which fixes some typos. The attachment [13639.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7973/13639.2.patch) contains some tab characters, which don't look good when you view the HTML version of the Developer's Guide, i.e. only the corresponding section in the Developer's Guide. Try to avoid tabs as much as possible in patches. If you're OK with the reviewer patch, then the whole ticket gets a positive review.

All those reviewer changes are spot on.  Thanks!  It's good to go for me.



---

archive/issue_comments_069562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T20:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69562",
    "user": "gaer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069563.json:
```json
{
    "body": "Sage isn't Python, and I think it's funner in math software to have references to math-related items.  The vast majority of potential Sage users and developers will have no clue about these Python in jokes, and I don't want to confuse them.",
    "created_at": "2010-01-18T22:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69563",
    "user": "was"
}
```

Sage isn't Python, and I think it's funner in math software to have references to math-related items.  The vast majority of potential Sage users and developers will have no clue about these Python in jokes, and I don't want to confuse them.



---

archive/issue_comments_069564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7973#issuecomment-69564",
    "user": "rlm"
}
```

Resolution: fixed
