# Issue 5808: [with patch, needs review] fix most warnings when building the reference manual

archive/issues_005808.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nAlong with #5541, this patch fixes most of the warnings when building the reference manual in 3.4.1.rc3.  I still get these:\n\n```\nchecking consistency... WARNING: /Applications/sage_builds/sage-3.4.1.rc3/devel/sage-test/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree\ndone\npreparing documents... WARNING: html_favicon is not an .ico file\n```\n\nbut that's it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5808\n\n",
    "created_at": "2009-04-17T06:04:42Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] fix most warnings when building the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5808",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Along with #5541, this patch fixes most of the warnings when building the reference manual in 3.4.1.rc3.  I still get these:

```
checking consistency... WARNING: /Applications/sage_builds/sage-3.4.1.rc3/devel/sage-test/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree
done
preparing documents... WARNING: html_favicon is not an .ico file
```

but that's it.



Issue created by migration from https://trac.sagemath.org/ticket/5808





---

archive/issue_comments_045611.json:
```json
{
    "body": "John,\n\nI just uploaded a patch at #4933 which fixes some of the same things for ell_rational_field and ell_generic.  We might have difficulties merging these.  I am about to test yours and hope to give a positive review shortly...\n\nPS I would like to add \\AA and \\PP to the \"blackboard bold\" list (for affine and projective space).  I read your clear instructions on how to do that, but have not done so as I thought you were probably touching that file.",
    "created_at": "2009-04-17T14:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45611",
    "user": "cremona"
}
```

John,

I just uploaded a patch at #4933 which fixes some of the same things for ell_rational_field and ell_generic.  We might have difficulties merging these.  I am about to test yours and hope to give a positive review shortly...

PS I would like to add \AA and \PP to the "blackboard bold" list (for affine and projective space).  I read your clear instructions on how to do that, but have not done so as I thought you were probably touching that file.



---

archive/issue_comments_045612.json:
```json
{
    "body": "Apply after the first patch",
    "created_at": "2009-04-17T14:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45612",
    "user": "cremona"
}
```

Apply after the first patch



---

archive/issue_comments_045613.json:
```json
{
    "body": "Attachment [trac_5808-review.patch](tarball://root/attachments/some-uuid/ticket5808/trac_5808-review.patch) by cremona created at 2009-04-17 14:47:31\n\nApplies fine to 3.4.1.rc3.  When I did \"sage -docbuild all html\" I got lots of warnings in the tutrial (ok, not dealt with here) and a couple in algebras/quatalg/quaternion_algebra.py.\n\nSo I added some edits to that file, as in the second patch attached.\n\nMy positive review applies to the first patch.  If John likes the second one, that's good.",
    "created_at": "2009-04-17T14:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45613",
    "user": "cremona"
}
```

Attachment [trac_5808-review.patch](tarball://root/attachments/some-uuid/ticket5808/trac_5808-review.patch) by cremona created at 2009-04-17 14:47:31

Applies fine to 3.4.1.rc3.  When I did "sage -docbuild all html" I got lots of warnings in the tutrial (ok, not dealt with here) and a couple in algebras/quatalg/quaternion_algebra.py.

So I added some edits to that file, as in the second patch attached.

My positive review applies to the first patch.  If John likes the second one, that's good.



---

archive/issue_comments_045614.json:
```json
{
    "body": "Hi John,\n\nI think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.",
    "created_at": "2009-04-17T15:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45614",
    "user": "jhpalmieri"
}
```

Hi John,

I think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.



---

archive/issue_comments_045615.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> Hi John,\n> \n> I think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.\n\nOK, kill that patch, I should not have wasted my time!\n\nI'm about to add a patch doing what you suggested for mwrank.  Which will make 4933 even harder to merge...so on second thoughts I will not post it here but will rebase my #4933 patch on this one and include the mwrank changes there.\n\nUPSHOT:   Positive review for ref-warnings.patch;  ignore the seond one.",
    "created_at": "2009-04-17T15:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45615",
    "user": "cremona"
}
```

Replying to [comment:3 jhpalmieri]:
> Hi John,
> 
> I think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.

OK, kill that patch, I should not have wasted my time!

I'm about to add a patch doing what you suggested for mwrank.  Which will make 4933 even harder to merge...so on second thoughts I will not post it here but will rebase my #4933 patch on this one and include the mwrank changes there.

UPSHOT:   Positive review for ref-warnings.patch;  ignore the seond one.



---

archive/issue_comments_045616.json:
```json
{
    "body": "Okay, thanks, and sorry for the extra work you'll have to do rebasing.",
    "created_at": "2009-04-17T15:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45616",
    "user": "jhpalmieri"
}
```

Okay, thanks, and sorry for the extra work you'll have to do rebasing.



---

archive/issue_comments_045617.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> Okay, thanks, and sorry for the extra work you'll have to do rebasing.\nNo problem -- done!",
    "created_at": "2009-04-17T15:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45617",
    "user": "cremona"
}
```

Replying to [comment:5 jhpalmieri]:
> Okay, thanks, and sorry for the extra work you'll have to do rebasing.
No problem -- done!



---

archive/issue_comments_045618.json:
```json
{
    "body": "Attachment [ref-warnings.patch](tarball://root/attachments/some-uuid/ticket5808/ref-warnings.patch) by jhpalmieri created at 2009-04-17 22:52:12\n\napply only this patch",
    "created_at": "2009-04-17T22:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45618",
    "user": "jhpalmieri"
}
```

Attachment [ref-warnings.patch](tarball://root/attachments/some-uuid/ticket5808/ref-warnings.patch) by jhpalmieri created at 2009-04-17 22:52:12

apply only this patch



---

archive/issue_comments_045619.json:
```json
{
    "body": "This version removes the \"..link::\" directives from sudoku.py; otherwise, it's identical to the previous patch.",
    "created_at": "2009-04-17T22:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45619",
    "user": "jhpalmieri"
}
```

This version removes the "..link::" directives from sudoku.py; otherwise, it's identical to the previous patch.



---

archive/issue_comments_045620.json:
```json
{
    "body": "mabshoff: the only issue with the latest patch is whether it passes doctests. I think it does; if you agree, I think you can re-issue the positive review.",
    "created_at": "2009-04-17T22:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45620",
    "user": "jhpalmieri"
}
```

mabshoff: the only issue with the latest patch is whether it passes doctests. I think it does; if you agree, I think you can re-issue the positive review.



---

archive/issue_comments_045621.json:
```json
{
    "body": "With only ref-warnings.patch applied doctests do pass. So I am reinstating the positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T01:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45621",
    "user": "mabshoff"
}
```

With only ref-warnings.patch applied doctests do pass. So I am reinstating the positive review.

Cheers,

Michael



---

archive/issue_comments_045622.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T01:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45622",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc4.

Cheers,

Michael



---

archive/issue_comments_045623.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T01:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5808#issuecomment-45623",
    "user": "mabshoff"
}
```

Resolution: fixed
