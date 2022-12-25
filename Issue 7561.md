# Issue 7561: Replaces InfinitePolynomialRing in MixedIntegerLinearProgram by 'var'

archive/issues_007561.json:
```json
{
    "body": "Assignee: jkantor\n\nInfinitePolynomialRing was responsible for some bugs and extreme slowness in the utilisation of MixedINtegerLinearProgram for LP containing more than 1000 variables.\n\nBy replacing this polynomial ring by 'var', this is settled and waaaaayyyy mroe efficient !!\n\nThis patch depends on #7270\n\nIssue created by migration from https://trac.sagemath.org/ticket/7561\n\n",
    "created_at": "2009-11-30T17:40:24Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Replaces InfinitePolynomialRing in MixedIntegerLinearProgram by 'var'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7561",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

InfinitePolynomialRing was responsible for some bugs and extreme slowness in the utilisation of MixedINtegerLinearProgram for LP containing more than 1000 variables.

By replacing this polynomial ring by 'var', this is settled and waaaaayyyy mroe efficient !!

This patch depends on #7270

Issue created by migration from https://trac.sagemath.org/ticket/7561





---

archive/issue_comments_064209.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-01T08:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64209",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064210.json:
```json
{
    "body": "Patch looks good and indeed speeds up everything considerably for me. Some small issues:\n* id should not be used as a variable name\n* The documentation says `# Returns the optimal value of x[3]` but you are asking for y[2][9]\n* min/max should not be used as variable names",
    "created_at": "2009-12-02T14:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64210",
    "user": "https://github.com/malb"
}
```

Patch looks good and indeed speeds up everything considerably for me. Some small issues:
* id should not be used as a variable name
* The documentation says `# Returns the optimal value of x[3]` but you are asking for y[2][9]
* min/max should not be used as variable names



---

archive/issue_comments_064211.json:
```json
{
    "body": "Hello !!! It seems there are no \"id\" anymore in the file, and I corrected the x[3]..\n\nThe min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)\n\nNathann",
    "created_at": "2009-12-02T18:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64211",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!! It seems there are no "id" anymore in the file, and I corrected the x[3]..

The min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)

Nathann



---

archive/issue_comments_064212.json:
```json
{
    "body": "Still around ??? :-)\n\nIt would be good if this patch was merged into next release ! :-)",
    "created_at": "2009-12-05T14:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64212",
    "user": "https://github.com/nathanncohen"
}
```

Still around ??? :-)

It would be good if this patch was merged into next release ! :-)



---

archive/issue_comments_064213.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Hello !!! It seems there are no \"id\" anymore in the file, and I corrected the x[3]..\n\nHi, it seems you didn't upload your new patch.\n \n> The min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)\n\nHow about `minimum` & `maximum`? I'll leave it to you to change it or to keep min/max.",
    "created_at": "2009-12-05T14:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64213",
    "user": "https://github.com/malb"
}
```

Replying to [comment:3 ncohen]:
> Hello !!! It seems there are no "id" anymore in the file, and I corrected the x[3]..

Hi, it seems you didn't upload your new patch.
 
> The min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)

How about `minimum` & `maximum`? I'll leave it to you to change it or to keep min/max.



---

archive/issue_comments_064214.json:
```json
{
    "body": "I forgot to uploaded it and erased it since... I'll upload a new one in a few seconds ! :-)",
    "created_at": "2009-12-05T14:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64214",
    "user": "https://github.com/nathanncohen"
}
```

I forgot to uploaded it and erased it since... I'll upload a new one in a few seconds ! :-)



---

archive/issue_comments_064215.json:
```json
{
    "body": "Here it is ! I only corrected the x[3] and let the min/max be... The function in which they appear is very short, and longer version would mean updating manymany patches (currently under review) and having longer aliases when it does not hurt that much. ( though I understand how you felt about them, I did not realized it when I first used them ).\n\nWe will be able to change them later if needed anyway :-)\n\nNathann",
    "created_at": "2009-12-05T14:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64215",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! I only corrected the x[3] and let the min/max be... The function in which they appear is very short, and longer version would mean updating manymany patches (currently under review) and having longer aliases when it does not hurt that much. ( though I understand how you felt about them, I did not realized it when I first used them ).

We will be able to change them later if needed anyway :-)

Nathann



---

archive/issue_comments_064216.json:
```json
{
    "body": "Attachment [trac_7561.patch](tarball://root/attachments/some-uuid/ticket7561/trac_7561.patch) by @malb created at 2009-12-05 14:59:46\n\nThis should go into 4.3, it opens a whole new world for MIP problems.",
    "created_at": "2009-12-05T14:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64216",
    "user": "https://github.com/malb"
}
```

Attachment [trac_7561.patch](tarball://root/attachments/some-uuid/ticket7561/trac_7561.patch) by @malb created at 2009-12-05 14:59:46

This should go into 4.3, it opens a whole new world for MIP problems.



---

archive/issue_comments_064217.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-05T14:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64217",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064218.json:
```json
{
    "body": "Thankssssssssssssss :-)",
    "created_at": "2009-12-05T15:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64218",
    "user": "https://github.com/nathanncohen"
}
```

Thankssssssssssssss :-)



---

archive/issue_comments_064219.json:
```json
{
    "body": "Attachment [trac_7561-review.patch](tarball://root/attachments/some-uuid/ticket7561/trac_7561-review.patch) by @mwhansen created at 2009-12-06 08:51:22",
    "created_at": "2009-12-06T08:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64219",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7561-review.patch](tarball://root/attachments/some-uuid/ticket7561/trac_7561-review.patch) by @mwhansen created at 2009-12-06 08:51:22



---

archive/issue_events_007790.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-06T08:51:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7561#event-7790"
}
```



---

archive/issue_comments_064220.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7561#issuecomment-64220",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
