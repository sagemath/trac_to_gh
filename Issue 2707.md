# Issue 2707: [with patch, needs review] clean and better document is_totally_real(), add is_totally_imaginary() to NumberField_generic

archive/issues_002707.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan\n\nKeywords: number field totally real imaginary\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2707\n\n",
    "created_at": "2008-03-28T20:21:09Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] clean and better document is_totally_real(), add is_totally_imaginary() to NumberField_generic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2707",
    "user": "ncalexan"
}
```
Assignee: was

CC:  ncalexan

Keywords: number field totally real imaginary



Issue created by migration from https://trac.sagemath.org/ticket/2707





---

archive/issue_comments_018671.json:
```json
{
    "body": "Attachment\n\nThis looks good, but I would like to see three things changed:\n\n* There's an extra 's' in the documentation for `is_totally_real` -- specifically on line 900. \n\n* Personally, I'd like to see some newlines between `is_totally_imaginary`, `is_totally_complex`, and `complex_embeddings`.\n\n* I think that `is_totally_complex` should be given a full function definition, not just declared as `is_totaly_complex = is_totally_imaginary`. Here's the reason: as I understand it, if you inherit from `NumberField_generic`, and override `is_totally_imaginary`, this will **not** change `is_totally_complex` in the subclass. While this might not be deeply relevant in this case (since it's such a trivial function), I think this means it's a bad habit to be in in general, so we should avoid doing it. I know this means writing an extra docstring, which seems silly, but I think it's worth it.",
    "created_at": "2008-03-28T20:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2707#issuecomment-18671",
    "user": "craigcitro"
}
```

Attachment

This looks good, but I would like to see three things changed:

* There's an extra 's' in the documentation for `is_totally_real` -- specifically on line 900. 

* Personally, I'd like to see some newlines between `is_totally_imaginary`, `is_totally_complex`, and `complex_embeddings`.

* I think that `is_totally_complex` should be given a full function definition, not just declared as `is_totaly_complex = is_totally_imaginary`. Here's the reason: as I understand it, if you inherit from `NumberField_generic`, and override `is_totally_imaginary`, this will **not** change `is_totally_complex` in the subclass. While this might not be deeply relevant in this case (since it's such a trivial function), I think this means it's a bad habit to be in in general, so we should avoid doing it. I know this means writing an extra docstring, which seems silly, but I think it's worth it.



---

archive/issue_comments_018672.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-28T20:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2707#issuecomment-18672",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_018673.json:
```json
{
    "body": "Apply both patches.  Second addresses referee's comments.",
    "created_at": "2008-03-28T20:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2707#issuecomment-18673",
    "user": "ncalexan"
}
```

Apply both patches.  Second addresses referee's comments.



---

archive/issue_comments_018674.json:
```json
{
    "body": "Merged both patches in Sage 2.11.alpha2",
    "created_at": "2008-03-28T20:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2707#issuecomment-18674",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.11.alpha2



---

archive/issue_comments_018675.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T20:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2707#issuecomment-18675",
    "user": "mabshoff"
}
```

Resolution: fixed
