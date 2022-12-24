# Issue 8882: Cleanup Combinatorial Free module

archive/issues_008882.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: Free module\n\n`CombinatorialFreeModules` need some cleanup\n\n 1 - merge `CombinatorialFreeModules` with `CombinatorialFreeModulesInterface`\n\n 2 - make its `classcall` private\n\n 3 - `if isinstance(basis_keys, list)` in `__init__` should be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8882\n\n",
    "created_at": "2010-05-05T02:41:20Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Cleanup Combinatorial Free module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8882",
    "user": "hivert"
}
```
Assignee: sage-combinat

Keywords: Free module

`CombinatorialFreeModules` need some cleanup

 1 - merge `CombinatorialFreeModules` with `CombinatorialFreeModulesInterface`

 2 - make its `classcall` private

 3 - `if isinstance(basis_keys, list)` in `__init__` should be removed.

Issue created by migration from https://trac.sagemath.org/ticket/8882





---

archive/issue_comments_081635.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T02:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81635",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081636.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-05T12:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81636",
    "user": "saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081637.json:
```json
{
    "body": "Hello Florent.\n\nYou do exactly what is said in the description. But I noticed a few things that you might want to clean up in **sage/combinat/free_module.py**::\n\n* line 824: change 'depend' to 'depends'\n* line 844 mentions 'the argument cc', but there is no argument called 'cc'\n* line 847: can you use `isinstance(args[1], (list,tuple))` instead here?\n* line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)\n* line 893: there is a 'cc' in the comment\n* line 902: it seems that the comment `#_prefix = \"\"` is not necessary",
    "created_at": "2010-05-05T12:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81637",
    "user": "saliola"
}
```

Hello Florent.

You do exactly what is said in the description. But I noticed a few things that you might want to clean up in **sage/combinat/free_module.py**::

* line 824: change 'depend' to 'depends'
* line 844 mentions 'the argument cc', but there is no argument called 'cc'
* line 847: can you use `isinstance(args[1], (list,tuple))` instead here?
* line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)
* line 893: there is a 'cc' in the comment
* line 902: it seems that the comment `#_prefix = ""` is not necessary



---

archive/issue_comments_081638.json:
```json
{
    "body": "Attachment [trac_8832-free_module_coerce-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8832-free_module_coerce-fh.patch) by hivert created at 2010-05-05 14:23:21",
    "created_at": "2010-05-05T14:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81638",
    "user": "hivert"
}
```

Attachment [trac_8832-free_module_coerce-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8832-free_module_coerce-fh.patch) by hivert created at 2010-05-05 14:23:21



---

archive/issue_comments_081639.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-05T14:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81639",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081640.json:
```json
{
    "body": ">     * line 824: change 'depend' to 'depends'\n>     * line 844 mentions 'the argument cc', but there is no argument called 'cc'\n>     * line 847: can you use `isinstance(args[1], (list,tuple))` instead here?\n>     * line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)\n>     * line 893: there is a 'cc' in the comment\n>     * line 902: it seems that the comment `#_prefix = \"\"` is not necessary\n\nAll those comment should be addressed in the new patch. I also corrected some more doc issues.\nPlease review.",
    "created_at": "2010-05-05T14:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81640",
    "user": "hivert"
}
```

>     * line 824: change 'depend' to 'depends'
>     * line 844 mentions 'the argument cc', but there is no argument called 'cc'
>     * line 847: can you use `isinstance(args[1], (list,tuple))` instead here?
>     * line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)
>     * line 893: there is a 'cc' in the comment
>     * line 902: it seems that the comment `#_prefix = ""` is not necessary

All those comment should be addressed in the new patch. I also corrected some more doc issues.
Please review.



---

archive/issue_comments_081641.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-05T15:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81641",
    "user": "saliola"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_081642.json:
```json
{
    "body": "It seems that you mistakenly uploaded a patch for #8832 instead.",
    "created_at": "2010-05-05T15:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81642",
    "user": "saliola"
}
```

It seems that you mistakenly uploaded a patch for #8832 instead.



---

archive/issue_comments_081643.json:
```json
{
    "body": "Replying to [comment:4 saliola]:\n> It seems that you mistakenly uploaded a patch for #8832 instead.\n\nOops !!!",
    "created_at": "2010-05-05T15:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81643",
    "user": "hivert"
}
```

Replying to [comment:4 saliola]:
> It seems that you mistakenly uploaded a patch for #8832 instead.

Oops !!!



---

archive/issue_comments_081644.json:
```json
{
    "body": "Everything looks good except for one thing. I realize it is not your patch that created the problem, but since you are poking around in this code, I figure you might be able to correct it quickly.\n\nIn this block of code:\n\n```\n822\t        # convert the argument args[2] into a tuple if it is a list. \n823\t        # note: if args is too short, we still propagate it down \n824\t        # to __init__ to let it handle proper exception raising. \n825\t        if len(args) >= 2 and isinstance(args[1], (list, tuple)): \n826\t            args = (args[0], FiniteEnumeratedSet(args[1])) + args[2:] \n827\t        return super(CombinatorialFreeModule, cls).__classcall__(cls, *args, **keywords) \n```\n\nthe comment says that `args[2]` will be converted into a tuple, but I don't actually see it happening. Is this a problem, or just a comment that needs to be deleted?",
    "created_at": "2010-05-05T15:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81644",
    "user": "saliola"
}
```

Everything looks good except for one thing. I realize it is not your patch that created the problem, but since you are poking around in this code, I figure you might be able to correct it quickly.

In this block of code:

```
822	        # convert the argument args[2] into a tuple if it is a list. 
823	        # note: if args is too short, we still propagate it down 
824	        # to __init__ to let it handle proper exception raising. 
825	        if len(args) >= 2 and isinstance(args[1], (list, tuple)): 
826	            args = (args[0], FiniteEnumeratedSet(args[1])) + args[2:] 
827	        return super(CombinatorialFreeModule, cls).__classcall__(cls, *args, **keywords) 
```

the comment says that `args[2]` will be converted into a tuple, but I don't actually see it happening. Is this a problem, or just a comment that needs to be deleted?



---

archive/issue_comments_081645.json:
```json
{
    "body": "Attachment [trac_8882-freemod_interface_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8882-freemod_interface_cleanup-fh.patch) by hivert created at 2010-05-05 15:22:45",
    "created_at": "2010-05-05T15:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81645",
    "user": "hivert"
}
```

Attachment [trac_8882-freemod_interface_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8882-freemod_interface_cleanup-fh.patch) by hivert created at 2010-05-05 15:22:45



---

archive/issue_comments_081646.json:
```json
{
    "body": "Thanks for addressing these concerns, Florent.\n\n**Release manager: only apply attachment:trac_8882-freemod_interface_cleanup-fh.patch.**",
    "created_at": "2010-05-05T15:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81646",
    "user": "saliola"
}
```

Thanks for addressing these concerns, Florent.

**Release manager: only apply attachment:trac_8882-freemod_interface_cleanup-fh.patch.**



---

archive/issue_comments_081647.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-05T15:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81647",
    "user": "saliola"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_081648.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-05T15:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81648",
    "user": "saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81649",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_081650.json:
```json
{
    "body": "Merged [trac_8882-freemod_interface_cleanup-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8882/trac_8882-freemod_interface_cleanup-fh.patch).",
    "created_at": "2010-05-08T21:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81650",
    "user": "mvngu"
}
```

Merged [trac_8882-freemod_interface_cleanup-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8882/trac_8882-freemod_interface_cleanup-fh.patch).
