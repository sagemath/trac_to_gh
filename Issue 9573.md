# Issue 9573: Error building the PDF reference manual

archive/issues_009573.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  novoselt vbraun davidloeffler\n\nBuilding the PDF reference manual for the forthcoming Sage 4.5.2.alpha0 on sage.math, I get\n\n```\n[4610] [4611]\nUnderfull \\hbox (badness 10000) in paragraph at lines 373276--373277\n\n[4612] [4613] [4614] [4615] [4616] [4617] [4618]\n(/usr/share/texmf-texlive/tex/latex/ucs/data/uni-4.def)\n! Undefined control sequence.\n\\u-default-1065 #1->\\CYRSHCH\n\nl.373945 ...@PYGaB[\"]@PYGaB[\u0429@_45]@PYGaB[\"]@rb[])\n\n?\n```\n\nThe problem *may* be in `schemes/generic/toric_variety.py` (cf. #8988).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9573\n\n",
    "created_at": "2010-07-22T04:52:45Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "Error building the PDF reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9573",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  novoselt vbraun davidloeffler

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

archive/issue_comments_092452.json:
```json
{
    "body": "[Here](http://sage.math.washington.edu/home/mpatel/trac/9573/reference.log) is the full pdflatex log.",
    "created_at": "2010-07-22T04:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92452",
    "user": "mpatel"
}
```

[Here](http://sage.math.washington.edu/home/mpatel/trac/9573/reference.log) is the full pdflatex log.



---

archive/issue_comments_092453.json:
```json
{
    "body": "Changing assignee from mvngu to novoselt.",
    "created_at": "2010-07-22T04:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92453",
    "user": "novoselt"
}
```

Changing assignee from mvngu to novoselt.



---

archive/issue_comments_092454.json:
```json
{
    "body": "I'll fix this. It is a cool non-alphanumeric symbol \"\u0429\" that cannot be used as a variable name...",
    "created_at": "2010-07-22T04:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92454",
    "user": "novoselt"
}
```

I'll fix this. It is a cool non-alphanumeric symbol "Щ" that cannot be used as a variable name...



---

archive/issue_comments_092455.json:
```json
{
    "body": "Out of curiosity: Does it help to replace `r\"\"\"` with `ur\"\"\"` for the relevant docstring?",
    "created_at": "2010-07-22T05:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92455",
    "user": "mpatel"
}
```

Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?



---

archive/issue_comments_092456.json:
```json
{
    "body": "Attachment [trac_9573_fix_cyrillic_character_in_docstring_problem.patch](tarball://root/attachments/some-uuid/ticket9573/trac_9573_fix_cyrillic_character_in_docstring_problem.patch) by novoselt created at 2010-07-22 05:25:39\n\nReplying to [comment:3 mpatel]:\n> Out of curiosity: Does it help to replace `r\"\"\"` with `ur\"\"\"` for the relevant docstring?\n\nI don't know, but I think using \"`@`\" here as an example of an unacceptable character is more robust and appropriate.\n\nI apologize for the caused problem.",
    "created_at": "2010-07-22T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92456",
    "user": "novoselt"
}
```

Attachment [trac_9573_fix_cyrillic_character_in_docstring_problem.patch](tarball://root/attachments/some-uuid/ticket9573/trac_9573_fix_cyrillic_character_in_docstring_problem.patch) by novoselt created at 2010-07-22 05:25:39

Replying to [comment:3 mpatel]:
> Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?

I don't know, but I think using "`@`" here as an example of an unacceptable character is more robust and appropriate.

I apologize for the caused problem.



---

archive/issue_comments_092457.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92457",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092458.json:
```json
{
    "body": "No need to apologize!",
    "created_at": "2010-07-22T05:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92458",
    "user": "mpatel"
}
```

No need to apologize!



---

archive/issue_comments_092459.json:
```json
{
    "body": "I am still getting an error, although a different one. I am not sure if it is related since I didn't have a pdf version before. Working...",
    "created_at": "2010-07-22T06:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92459",
    "user": "novoselt"
}
```

I am still getting an error, although a different one. I am not sure if it is related since I didn't have a pdf version before. Working...



---

archive/issue_comments_092460.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-22T06:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92460",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092461.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-22T07:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92461",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092462.json:
```json
{
    "body": "OK, looks like a false alarm. I have done the following:\n\n* Removed doc/output in a sage-4.5.1 installation.\n* Built PDF-documentation without any patches applied.\n* Applied all merged toric patches and the patch on this ticket.\n* Build PDF-documentation again. Is seems to be OK in the sense that I got back to the shell prompt, there is a big PDF file in output, and I can see the modified example there just fine.\n\nPlease test it with 4.5.2.alpha0.",
    "created_at": "2010-07-22T07:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92462",
    "user": "novoselt"
}
```

OK, looks like a false alarm. I have done the following:

* Removed doc/output in a sage-4.5.1 installation.
* Built PDF-documentation without any patches applied.
* Applied all merged toric patches and the patch on this ticket.
* Build PDF-documentation again. Is seems to be OK in the sense that I got back to the shell prompt, there is a big PDF file in output, and I can see the modified example there just fine.

Please test it with 4.5.2.alpha0.



---

archive/issue_comments_092463.json:
```json
{
    "body": "Looks good to me.  PDF builds successfully, output looks fine.",
    "created_at": "2010-07-23T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92463",
    "user": "jhpalmieri"
}
```

Looks good to me.  PDF builds successfully, output looks fine.



---

archive/issue_comments_092464.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92464",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T02:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9573#issuecomment-92465",
    "user": "ddrake"
}
```

Resolution: fixed
