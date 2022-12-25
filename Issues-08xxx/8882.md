# Issue 8882: Cleanup Combinatorial Free module

archive/issues_008882.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: Free module\n\n`CombinatorialFreeModules` need some cleanup\n\n 1 - merge `CombinatorialFreeModules` with `CombinatorialFreeModulesInterface`\n\n 2 - make its `classcall` private\n\n 3 - `if isinstance(basis_keys, list)` in `__init__` should be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8882\n\n",
    "closed_at": "2010-05-08T21:42:04Z",
    "created_at": "2010-05-05T02:41:20Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Cleanup Combinatorial Free module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8882",
    "user": "https://github.com/hivert"
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

archive/issue_events_021679.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2010-05-05T02:59:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "milestone": "sage-4.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8882#event-21679"
}
```



---

archive/issue_comments_081501.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T02:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81501",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081502.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-05T12:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81502",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081503.json:
```json
{
    "body": "Hello Florent.\n\nYou do exactly what is said in the description. But I noticed a few things that you might want to clean up in **sage/combinat/free_module.py**::\n\n* line 824: change 'depend' to 'depends'\n* line 844 mentions 'the argument cc', but there is no argument called 'cc'\n* line 847: can you use `isinstance(args[1], (list,tuple))` instead here?\n* line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)\n* line 893: there is a 'cc' in the comment\n* line 902: it seems that the comment `#_prefix = \"\"` is not necessary",
    "created_at": "2010-05-05T12:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81503",
    "user": "https://github.com/saliola"
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

archive/issue_comments_081504.json:
```json
{
    "body": "Attachment [trac_8832-free_module_coerce-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8832-free_module_coerce-fh.patch) by @hivert created at 2010-05-05 14:23:21",
    "created_at": "2010-05-05T14:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81504",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8832-free_module_coerce-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8832-free_module_coerce-fh.patch) by @hivert created at 2010-05-05 14:23:21



---

archive/issue_comments_081505.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-05T14:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81505",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081506.json:
```json
{
    "body": ">     * line 824: change 'depend' to 'depends'\n>     * line 844 mentions 'the argument cc', but there is no argument called 'cc'\n>     * line 847: can you use `isinstance(args[1], (list,tuple))` instead here?\n>     * line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)\n>     * line 893: there is a 'cc' in the comment\n>     * line 902: it seems that the comment `#_prefix = \"\"` is not necessary\n\n\nAll those comment should be addressed in the new patch. I also corrected some more doc issues.\nPlease review.",
    "created_at": "2010-05-05T14:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81506",
    "user": "https://github.com/hivert"
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

archive/issue_comments_081507.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-05T15:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81507",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_081508.json:
```json
{
    "body": "It seems that you mistakenly uploaded a patch for #8832 instead.",
    "created_at": "2010-05-05T15:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81508",
    "user": "https://github.com/saliola"
}
```

It seems that you mistakenly uploaded a patch for #8832 instead.



---

archive/issue_comments_081509.json:
```json
{
    "body": "Replying to [comment:4 saliola]:\n> It seems that you mistakenly uploaded a patch for #8832 instead.\n\n\nOops !!!",
    "created_at": "2010-05-05T15:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81509",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 saliola]:
> It seems that you mistakenly uploaded a patch for #8832 instead.


Oops !!!



---

archive/issue_comments_081510.json:
```json
{
    "body": "Everything looks good except for one thing. I realize it is not your patch that created the problem, but since you are poking around in this code, I figure you might be able to correct it quickly.\n\nIn this block of code:\n\n```\n822\t        # convert the argument args[2] into a tuple if it is a list. \n823\t        # note: if args is too short, we still propagate it down \n824\t        # to __init__ to let it handle proper exception raising. \n825\t        if len(args) >= 2 and isinstance(args[1], (list, tuple)): \n826\t            args = (args[0], FiniteEnumeratedSet(args[1])) + args[2:] \n827\t        return super(CombinatorialFreeModule, cls).__classcall__(cls, *args, **keywords) \n```\nthe comment says that `args[2]` will be converted into a tuple, but I don't actually see it happening. Is this a problem, or just a comment that needs to be deleted?",
    "created_at": "2010-05-05T15:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81510",
    "user": "https://github.com/saliola"
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

archive/issue_comments_081511.json:
```json
{
    "body": "Attachment [trac_8882-freemod_interface_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8882-freemod_interface_cleanup-fh.patch) by @hivert created at 2010-05-05 15:22:45",
    "created_at": "2010-05-05T15:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81511",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8882-freemod_interface_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket8882/trac_8882-freemod_interface_cleanup-fh.patch) by @hivert created at 2010-05-05 15:22:45



---

archive/issue_comments_081512.json:
```json
{
    "body": "Thanks for addressing these concerns, Florent.\n\n**Release manager: only apply attachment:trac_8882-freemod_interface_cleanup-fh.patch.**",
    "created_at": "2010-05-05T15:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81512",
    "user": "https://github.com/saliola"
}
```

Thanks for addressing these concerns, Florent.

**Release manager: only apply attachment:trac_8882-freemod_interface_cleanup-fh.patch.**



---

archive/issue_comments_081513.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-05T15:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81513",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_081514.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-05T15:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81514",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_081516.json:
```json
{
    "body": "Merged [trac_8882-freemod_interface_cleanup-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8882/trac_8882-freemod_interface_cleanup-fh.patch).",
    "created_at": "2010-05-08T21:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8882#issuecomment-81516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8882-freemod_interface_cleanup-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8882/trac_8882-freemod_interface_cleanup-fh.patch).



---

archive/issue_events_021680.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T21:42:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8882",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8882#event-21680"
}
```
