# Issue 3542: [with patch, needs review] multimodular algorithm for Bernoulli numbers

archive/issues_003542.json:
```json
{
    "body": "Assignee: somebody\n\nThis patch implements the algorithm in my preprint \"A multimodular algorithm for computing Bernoulli numbers\".\n\nhttp://math.harvard.edu/~dmharvey/bernmm/\n\nIt adds a few files into a new bernmm directory, a cython wrapper (bernmm.pyx), modifies setup.py to build those files, removes the old implementation of `bernoulli_mod_p_single`, and adds a new algorithm option and a `num_threads` option to the global `bernoulli()` function.\n\nMy main concern from a build point of view is whether pthreads is supported on all of our target platforms. If not, it will be necessary to modify setup.py to conditionally remove the -lpthreads option and also to #define `USE_THREADS` appropriately.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3542\n\n",
    "created_at": "2008-07-02T19:22:20Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] multimodular algorithm for Bernoulli numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3542",
    "user": "dmharvey"
}
```
Assignee: somebody

This patch implements the algorithm in my preprint "A multimodular algorithm for computing Bernoulli numbers".

http://math.harvard.edu/~dmharvey/bernmm/

It adds a few files into a new bernmm directory, a cython wrapper (bernmm.pyx), modifies setup.py to build those files, removes the old implementation of `bernoulli_mod_p_single`, and adds a new algorithm option and a `num_threads` option to the global `bernoulli()` function.

My main concern from a build point of view is whether pthreads is supported on all of our target platforms. If not, it will be necessary to modify setup.py to conditionally remove the -lpthreads option and also to #define `USE_THREADS` appropriately.


Issue created by migration from https://trac.sagemath.org/ticket/3542





---

archive/issue_comments_025045.json:
```json
{
    "body": "Attachment [bernmm.patch](tarball://root/attachments/some-uuid/ticket3542/bernmm.patch) by dmharvey created at 2008-07-02 19:23:34",
    "created_at": "2008-07-02T19:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25045",
    "user": "dmharvey"
}
```

Attachment [bernmm.patch](tarball://root/attachments/some-uuid/ticket3542/bernmm.patch) by dmharvey created at 2008-07-02 19:23:34



---

archive/issue_comments_025046.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-07-02T19:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25046",
    "user": "dmharvey"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_025047.json:
```json
{
    "body": "OMFG! W00t!!",
    "created_at": "2008-07-02T20:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25047",
    "user": "was"
}
```

OMFG! W00t!!



---

archive/issue_comments_025048.json:
```json
{
    "body": "REFEREE REPORT:\n\n* Patch applies and works fine. Doctests pass.\n\n* You need r\"\"\" instead of \"\"\" for some of the docstrings where you use backslashes.\n\n```\n \t75\tdef bernmm_bern_modp(long p, long k): \n \t76\t    \"\"\" \n \t77\t    Computes $B_k \\mod p$, where $B_k$ is the k-th Bernoulli number. \n```\n\n\n* You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?\n\n* I would prefer if there were an algorithm=\"default\" or algorithm=\"heuristic\" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.\n\n* I found bugs in either PARI or your new code!  This happens also with num_threads=1.\n\n```\nsage: for k in range(1,10000):\n....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k\n....:     \n2932\n2957\n3443\n3962\n3973\n...\n```\n\nThis is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). \n\n* What does this do?  Just curious.  Maybe you could document it.\n\n``` \nNTL_CLIENT; \n```\n\n\n* Wow, this patch has a really large amount of interesting C++ code, all well documented.  This must have been quite a lot of work -- it's of course the best in the world and multithreaded.  Amazing.",
    "created_at": "2008-08-01T02:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25048",
    "user": "was"
}
```

REFEREE REPORT:

* Patch applies and works fine. Doctests pass.

* You need r""" instead of """ for some of the docstrings where you use backslashes.

```
 	75	def bernmm_bern_modp(long p, long k): 
 	76	    """ 
 	77	    Computes $B_k \mod p$, where $B_k$ is the k-th Bernoulli number. 
```


* You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?

* I would prefer if there were an algorithm="default" or algorithm="heuristic" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.

* I found bugs in either PARI or your new code!  This happens also with num_threads=1.

```
sage: for k in range(1,10000):
....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k
....:     
2932
2957
3443
3962
3973
...
```

This is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). 

* What does this do?  Just curious.  Maybe you could document it.

``` 
NTL_CLIENT; 
```


* Wow, this patch has a really large amount of interesting C++ code, all well documented.  This must have been quite a lot of work -- it's of course the best in the world and multithreaded.  Amazing.



---

archive/issue_comments_025049.json:
```json
{
    "body": "Replying to [comment:3 was]:\n>  * You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?\n\nNo, I don't understand what you mean. I thought all the function documentation was automatically included in the reference manual?\n\n\n>  * I would prefer if there were an algorithm=\"default\" or algorithm=\"heuristic\" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.\n\nOkay.\n\n\n>  * I found bugs in either PARI or your new code!  This happens also with num_threads=1.\n> {{{\n> sage: for k in range(1,10000):\n> ....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k\n> ....:     \n> 2932\n> 2957\n> 3443\n> 3962\n> 3973\n> ...\n> }}}\n> This is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). \n\nNasty. Thanks for picking that up. I've found the bug and I should have a fix tomorrow. That's quite annoying, because I actually do have a test suite which I ran on a 32-bit machine, and it was specifically designed to pick up that kind of crap, and I still missed it. (The first failure occurs when the largest prime modulus is just below `2^15`, which was a good clue :-))\n\n\n>  * What does this do?  Just curious.  Maybe you could document it.\n> {{{ \n> NTL_CLIENT; \n> }}}\n\nThis is a standard NTL macro that Shoup recommends putting at the top of any file that uses NTL. It does something to do with namespaces. See\n\nhttp://www.shoup.net/ntl/doc/tour-ex1.html",
    "created_at": "2008-08-01T03:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25049",
    "user": "dmharvey"
}
```

Replying to [comment:3 was]:
>  * You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?

No, I don't understand what you mean. I thought all the function documentation was automatically included in the reference manual?


>  * I would prefer if there were an algorithm="default" or algorithm="heuristic" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.

Okay.


>  * I found bugs in either PARI or your new code!  This happens also with num_threads=1.
> {{{
> sage: for k in range(1,10000):
> ....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k
> ....:     
> 2932
> 2957
> 3443
> 3962
> 3973
> ...
> }}}
> This is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). 

Nasty. Thanks for picking that up. I've found the bug and I should have a fix tomorrow. That's quite annoying, because I actually do have a test suite which I ran on a 32-bit machine, and it was specifically designed to pick up that kind of crap, and I still missed it. (The first failure occurs when the largest prime modulus is just below `2^15`, which was a good clue :-))


>  * What does this do?  Just curious.  Maybe you could document it.
> {{{ 
> NTL_CLIENT; 
> }}}

This is a standard NTL macro that Shoup recommends putting at the top of any file that uses NTL. It does something to do with namespaces. See

http://www.shoup.net/ntl/doc/tour-ex1.html



---

archive/issue_comments_025050.json:
```json
{
    "body": ">     * You may want to post a patch to add the docs to the reference manual. Do you know how to do that?\n\n> No, I don't understand what you mean. I thought all the function documentation was automatically\n> included in the reference manual? \n\nThe layout and choice contents of the reference manual are done by hand.  If you read the instructions in SAGE_ROOT/devel/doc/ref/README.txt hopefully that will explain what you need to do.",
    "created_at": "2008-08-01T12:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25050",
    "user": "was"
}
```

>     * You may want to post a patch to add the docs to the reference manual. Do you know how to do that?

> No, I don't understand what you mean. I thought all the function documentation was automatically
> included in the reference manual? 

The layout and choice contents of the reference manual are done by hand.  If you read the instructions in SAGE_ROOT/devel/doc/ref/README.txt hopefully that will explain what you need to do.



---

archive/issue_comments_025051.json:
```json
{
    "body": "Attachment [bernmm.2.patch](tarball://root/attachments/some-uuid/ticket3542/bernmm.2.patch) by dmharvey created at 2008-08-01 14:35:33\n\nI've addressed all issues raised by reviewer (see attached patch), except for the reference manual thing.\n\nThe bernoulli number function itself is already in the reference manual, in\n\nhttp://www.sagemath.org/doc/ref/module-sage.rings.arith.html\n\nAre you talking about adding the bernmm.pyx wrapper to the manual? It's not at all clear to me where in the manual it would belong. I already don't really understand why bernoulli() is in rings.arith, that seems pretty random.",
    "created_at": "2008-08-01T14:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25051",
    "user": "dmharvey"
}
```

Attachment [bernmm.2.patch](tarball://root/attachments/some-uuid/ticket3542/bernmm.2.patch) by dmharvey created at 2008-08-01 14:35:33

I've addressed all issues raised by reviewer (see attached patch), except for the reference manual thing.

The bernoulli number function itself is already in the reference manual, in

http://www.sagemath.org/doc/ref/module-sage.rings.arith.html

Are you talking about adding the bernmm.pyx wrapper to the manual? It's not at all clear to me where in the manual it would belong. I already don't really understand why bernoulli() is in rings.arith, that seems pretty random.



---

archive/issue_comments_025052.json:
```json
{
    "body": "Attachment [3542-dharvey-bernoulli-numbers-multimodular.patch](tarball://root/attachments/some-uuid/ticket3542/3542-dharvey-bernoulli-numbers-multimodular.patch) by ncalexan created at 2008-08-10 19:59:10\n\nI think this looks good.  I added a few doctests that verify that your code agrees with the pari code, for a few of the cases that William found did not agree.\n\nApply only `3542-dharvey-bernoulli-numbers-multimodular.patch`.",
    "created_at": "2008-08-10T19:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25052",
    "user": "ncalexan"
}
```

Attachment [3542-dharvey-bernoulli-numbers-multimodular.patch](tarball://root/attachments/some-uuid/ticket3542/3542-dharvey-bernoulli-numbers-multimodular.patch) by ncalexan created at 2008-08-10 19:59:10

I think this looks good.  I added a few doctests that verify that your code agrees with the pari code, for a few of the cases that William found did not agree.

Apply only `3542-dharvey-bernoulli-numbers-multimodular.patch`.



---

archive/issue_comments_025053.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T01:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25053",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_025054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T01:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3542#issuecomment-25054",
    "user": "mabshoff"
}
```

Resolution: fixed
