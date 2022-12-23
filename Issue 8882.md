# Issue 8882: Cleanup Combinatorial Free module

Issue created by migration from https://trac.sagemath.org/ticket/8882

Original creator: hivert

Original creation time: 2010-05-05 02:41:20

Assignee: sage-combinat

Keywords: Free module

`CombinatorialFreeModules` need some cleanup

 1 - merge `CombinatorialFreeModules` with `CombinatorialFreeModulesInterface`

 2 - make its `classcall` private

 3 - `if isinstance(basis_keys, list)` in `__init__` should be removed.


---

Comment by hivert created at 2010-05-05 02:59:18

Changing status from new to needs_review.


---

Comment by saliola created at 2010-05-05 12:43:04

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2010-05-05 12:43:04

Hello Florent.

You do exactly what is said in the description. But I noticed a few things that you might want to clean up in *sage/combinat/free_module.py*::

    * line 824: change 'depend' to 'depends'
    * line 844 mentions 'the argument cc', but there is no argument called 'cc'
    * line 847: can you use `isinstance(args[1], (list,tuple))` instead here?
    * line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)
    * line 893: there is a 'cc' in the comment
    * line 902: it seems that the comment `#_prefix = ""` is not necessary


---

Attachment


---

Comment by hivert created at 2010-05-05 14:24:39

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-05-05 14:24:39

>     * line 824: change 'depend' to 'depends'
>     * line 844 mentions 'the argument cc', but there is no argument called 'cc'
>     * line 847: can you use `isinstance(args[1], (list,tuple))` instead here?
>     * line 862: there are some formatting issues (indentation; using `:` instead of `::` and missing a blank line afterwards)
>     * line 893: there is a 'cc' in the comment
>     * line 902: it seems that the comment `#_prefix = ""` is not necessary

All those comment should be addressed in the new patch. I also corrected some more doc issues.
Please review.


---

Comment by saliola created at 2010-05-05 15:02:42

Changing status from needs_review to needs_info.


---

Comment by saliola created at 2010-05-05 15:02:42

It seems that you mistakenly uploaded a patch for #8832 instead.


---

Comment by hivert created at 2010-05-05 15:05:27

Replying to [comment:4 saliola]:
> It seems that you mistakenly uploaded a patch for #8832 instead.

Oops !!!


---

Comment by saliola created at 2010-05-05 15:13:29

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

Attachment


---

Comment by saliola created at 2010-05-05 15:39:12

Thanks for addressing these concerns, Florent.

*Release manager: only apply attachment:trac_8882-freemod_interface_cleanup-fh.patch.*


---

Comment by saliola created at 2010-05-05 15:39:12

Changing status from needs_info to needs_review.


---

Comment by saliola created at 2010-05-05 15:43:58

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:42:04

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 21:42:04

Merged [trac_8882-freemod_interface_cleanup-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8882/trac_8882-freemod_interface_cleanup-fh.patch).
