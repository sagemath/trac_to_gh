# Issue 9573: Error building the PDF reference manual

archive/issues_009573.json:
```json
{
    "body": "Assignee: @novoselt\n\nCC:  @novoselt @vbraun @loefflerd\n\nBuilding the PDF reference manual for the forthcoming Sage 4.5.2.alpha0 on sage.math, I get\n\n```\n[4610] [4611]\nUnderfull \\hbox (badness 10000) in paragraph at lines 373276--373277\n\n[4612] [4613] [4614] [4615] [4616] [4617] [4618]\n(/usr/share/texmf-texlive/tex/latex/ucs/data/uni-4.def)\n! Undefined control sequence.\n\\u-default-1065 #1->\\CYRSHCH\n\nl.373945 ...@PYGaB[\"]@PYGaB[\u0429@_45]@PYGaB[\"]@rb[])\n\n?\n```\nThe problem *may* be in `schemes/generic/toric_variety.py` (cf. #8988).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9573\n\n",
    "closed_at": "2010-07-23T02:22:44Z",
    "created_at": "2010-07-22T04:52:45Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Error building the PDF reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9573",
    "user": "https://github.com/qed777"
}
```
Assignee: @novoselt

CC:  @novoselt @vbraun @loefflerd

Building the PDF reference manual for the forthcoming Sage 4.5.2.alpha0 on sage.math, I get

```
[4610] [4611]
Underfull \hbox (badness 10000) in paragraph at lines 373276--373277

[4612] [4613] [4614] [4615] [4616] [4617] [4618]
(/usr/share/texmf-texlive/tex/latex/ucs/data/uni-4.def)
! Undefined control sequence.
\u-default-1065 #1->\CYRSHCH

l.373945 ...@PYGaB["]@PYGaB[Щ@_45]@PYGaB["]@rb[])

?
```
The problem *may* be in `schemes/generic/toric_variety.py` (cf. #8988).

Issue created by migration from https://trac.sagemath.org/ticket/9573





---

archive/issue_comments_092298.json:
```json
{
    "body": "[Here](http://sage.math.washington.edu/home/mpatel/trac/9573/reference.log) is the full pdflatex log.",
    "created_at": "2010-07-22T04:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92298",
    "user": "https://github.com/qed777"
}
```

[Here](http://sage.math.washington.edu/home/mpatel/trac/9573/reference.log) is the full pdflatex log.



---

archive/issue_comments_092299.json:
```json
{
    "body": "Changing assignee from mvngu to @novoselt.",
    "created_at": "2010-07-22T04:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92299",
    "user": "https://github.com/novoselt"
}
```

Changing assignee from mvngu to @novoselt.



---

archive/issue_comments_092300.json:
```json
{
    "body": "I'll fix this. It is a cool non-alphanumeric symbol \"\u0429\" that cannot be used as a variable name...",
    "created_at": "2010-07-22T04:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92300",
    "user": "https://github.com/novoselt"
}
```

I'll fix this. It is a cool non-alphanumeric symbol "Щ" that cannot be used as a variable name...



---

archive/issue_comments_092301.json:
```json
{
    "body": "Out of curiosity: Does it help to replace `r\"\"\"` with `ur\"\"\"` for the relevant docstring?",
    "created_at": "2010-07-22T05:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92301",
    "user": "https://github.com/qed777"
}
```

Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?



---

archive/issue_comments_092302.json:
```json
{
    "body": "Attachment [trac_9573_fix_cyrillic_character_in_docstring_problem.patch](tarball://root/attachments/some-uuid/ticket9573/trac_9573_fix_cyrillic_character_in_docstring_problem.patch) by @novoselt created at 2010-07-22 05:25:39\n\nReplying to [comment:3 mpatel]:\n> Out of curiosity: Does it help to replace `r\"\"\"` with `ur\"\"\"` for the relevant docstring?\n\n\nI don't know, but I think using \"`@`\" here as an example of an unacceptable character is more robust and appropriate.\n\nI apologize for the caused problem.",
    "created_at": "2010-07-22T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92302",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9573_fix_cyrillic_character_in_docstring_problem.patch](tarball://root/attachments/some-uuid/ticket9573/trac_9573_fix_cyrillic_character_in_docstring_problem.patch) by @novoselt created at 2010-07-22 05:25:39

Replying to [comment:3 mpatel]:
> Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?


I don't know, but I think using "`@`" here as an example of an unacceptable character is more robust and appropriate.

I apologize for the caused problem.



---

archive/issue_comments_092303.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92303",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092304.json:
```json
{
    "body": "No need to apologize!",
    "created_at": "2010-07-22T05:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92304",
    "user": "https://github.com/qed777"
}
```

No need to apologize!



---

archive/issue_comments_092305.json:
```json
{
    "body": "I am still getting an error, although a different one. I am not sure if it is related since I didn't have a pdf version before. Working...",
    "created_at": "2010-07-22T06:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92305",
    "user": "https://github.com/novoselt"
}
```

I am still getting an error, although a different one. I am not sure if it is related since I didn't have a pdf version before. Working...



---

archive/issue_comments_092306.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-22T06:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92306",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092307.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-22T07:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92307",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092308.json:
```json
{
    "body": "OK, looks like a false alarm. I have done the following:\n\n* Removed doc/output in a sage-4.5.1 installation.\n* Built PDF-documentation without any patches applied.\n* Applied all merged toric patches and the patch on this ticket.\n* Build PDF-documentation again. Is seems to be OK in the sense that I got back to the shell prompt, there is a big PDF file in output, and I can see the modified example there just fine.\n\nPlease test it with 4.5.2.alpha0.",
    "created_at": "2010-07-22T07:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92308",
    "user": "https://github.com/novoselt"
}
```

OK, looks like a false alarm. I have done the following:

* Removed doc/output in a sage-4.5.1 installation.
* Built PDF-documentation without any patches applied.
* Applied all merged toric patches and the patch on this ticket.
* Build PDF-documentation again. Is seems to be OK in the sense that I got back to the shell prompt, there is a big PDF file in output, and I can see the modified example there just fine.

Please test it with 4.5.2.alpha0.



---

archive/issue_comments_092309.json:
```json
{
    "body": "Looks good to me.  PDF builds successfully, output looks fine.",
    "created_at": "2010-07-23T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92309",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  PDF builds successfully, output looks fine.



---

archive/issue_comments_092310.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92310",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T02:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92311",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_events_023831.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-23T02:22:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9573#event-23831"
}
```
