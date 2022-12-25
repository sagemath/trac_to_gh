# Issue 7746: Blum-Goldwasser probabilistic encryption

archive/issues_007746.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @wdjoyner\n\nKeywords: Blum-Goldwasser, probabilistic encryption\n\nThe Blum-Goldwasser probabilistic public-key encryption scheme. This scheme was originally described by (Blum and Goldwasser 1985). See also section 8.7.2 of (Menezes et al. 1996) and the [Wikipedia article](http://en.wikipedia.org/wiki/Blum-Goldwasser_cryptosystem) on this scheme.\n\n* (Blum and Goldwasser 1985) M. Blum and S. Goldwasser. An Efficient Probabilistic Public-Key Encryption Scheme Which Hides All Partial Information. In Proceedings of CRYPTO 84 on Advances in Cryptology, pp. 289\u2013299, Springer, 1985.\n\n* (Menezes et al. 1996) A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone. Handbook of Applied Cryptography. CRC Press, 1996.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7746\n\n",
    "created_at": "2009-12-21T03:37:12Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Blum-Goldwasser probabilistic encryption",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @wdjoyner

Keywords: Blum-Goldwasser, probabilistic encryption

The Blum-Goldwasser probabilistic public-key encryption scheme. This scheme was originally described by (Blum and Goldwasser 1985). See also section 8.7.2 of (Menezes et al. 1996) and the [Wikipedia article](http://en.wikipedia.org/wiki/Blum-Goldwasser_cryptosystem) on this scheme.

* (Blum and Goldwasser 1985) M. Blum and S. Goldwasser. An Efficient Probabilistic Public-Key Encryption Scheme Which Hides All Partial Information. In Proceedings of CRYPTO 84 on Advances in Cryptology, pp. 289–299, Springer, 1985.

* (Menezes et al. 1996) A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone. Handbook of Applied Cryptography. CRC Press, 1996.

Issue created by migration from https://trac.sagemath.org/ticket/7746





---

archive/issue_comments_066558.json:
```json
{
    "body": "public domain version by Mike Hogan and David Joyner",
    "created_at": "2009-12-21T04:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

public domain version by Mike Hogan and David Joyner



---

archive/issue_comments_066559.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-21T04:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066560.json:
```json
{
    "body": "Attachment [BGcrypto2.sage](tarball://root/attachments/some-uuid/ticket7746/BGcrypto2.sage) by mvngu created at 2009-12-21 04:02:37\n\nThe patch `trac_7746-blum-goldwasser.patch` introduces two new files:\n\n* `sage/crypto/public_key/blum_goldwasser.py` --- A class implementing the Blum-Goldwasser probabilistic public-key encryption scheme. This is a complete rewrite of the version by Mike Hogan and David Joyner, which was originally released as public domain software. The rewrite is licensed under GPLv2+. For reference, I have also attached the original public domain version.\n \n* `sage/crypto/util.py` --- A module containing miscellaneous functions for cryptographic purposes. The Blum-Goldwasser implementation makes use of various functions in this module.",
    "created_at": "2009-12-21T04:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [BGcrypto2.sage](tarball://root/attachments/some-uuid/ticket7746/BGcrypto2.sage) by mvngu created at 2009-12-21 04:02:37

The patch `trac_7746-blum-goldwasser.patch` introduces two new files:

* `sage/crypto/public_key/blum_goldwasser.py` --- A class implementing the Blum-Goldwasser probabilistic public-key encryption scheme. This is a complete rewrite of the version by Mike Hogan and David Joyner, which was originally released as public domain software. The rewrite is licensed under GPLv2+. For reference, I have also attached the original public domain version.
 
* `sage/crypto/util.py` --- A module containing miscellaneous functions for cryptographic purposes. The Blum-Goldwasser implementation makes use of various functions in this module.



---

archive/issue_comments_066561.json:
```json
{
    "body": "This applies and tests fine (modulo the usual failures) on sage-4.3.rc0 on a mac running 10.6.2.\n\nThis is definitely a complete reimplementation (as stated in the docstring) of Hogan's module, since we actually did a hybrid of the HAC version and the Wikipedia version of the algorithm.\n\nI am not crazy about this:\n\n\n```\n\n \t289\t    However, if there are no primes between the lower and upper bounds, \n \t290\t    this function could hang forever. For instance, a lower bound of 24 and \n \t291\t    an upper bound of 28 would trigger an infinite loop. \n```\n\n\nIt seems to violate the \"defensive programming\" (or \"assume all people are stupid\") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.\n\nOther than this, the patch looks very well documented, gives good references and examples. I've forgotten how to compile the docs to see if the html comes out okay. Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in \n\n\n```\nsage-4.3.rc0/devel/sage-BG-7746/doc/output/html/en/reference/sage/crypto/cryptosystem.html\n```\n\n\nFinally, some general more-or-less stylistic questions.\n\nIs SageObject the best superclass for this? \n\nIs the best place for blum_blum_shub in util or in a stream cipher module?",
    "created_at": "2009-12-21T13:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66561",
    "user": "https://github.com/wdjoyner"
}
```

This applies and tests fine (modulo the usual failures) on sage-4.3.rc0 on a mac running 10.6.2.

This is definitely a complete reimplementation (as stated in the docstring) of Hogan's module, since we actually did a hybrid of the HAC version and the Wikipedia version of the algorithm.

I am not crazy about this:


```

 	289	    However, if there are no primes between the lower and upper bounds, 
 	290	    this function could hang forever. For instance, a lower bound of 24 and 
 	291	    an upper bound of 28 would trigger an infinite loop. 
```


It seems to violate the "defensive programming" (or "assume all people are stupid") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.

Other than this, the patch looks very well documented, gives good references and examples. I've forgotten how to compile the docs to see if the html comes out okay. Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in 


```
sage-4.3.rc0/devel/sage-BG-7746/doc/output/html/en/reference/sage/crypto/cryptosystem.html
```


Finally, some general more-or-less stylistic questions.

Is SageObject the best superclass for this? 

Is the best place for blum_blum_shub in util or in a stream cipher module?



---

archive/issue_comments_066562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-21T14:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066563.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> It seems to violate the \"defensive programming\" (or \"assume all people are stupid\") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.\n\nIt looks to me that there needs to be a function called, say, \"has_blum_prime(lbound, ubound)\" in the module `sage/crypto/util.py`. This function checks to see if there is a Blum prime within the specified lower and upper bounds. One could then use `has_blum_prime()` to first check for the presence of a Blum prime within a specified interval, prior to actually computing a random Blum prime.\n\n\n\n\n\n> Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in \n\nAfter you have applied the patch and rebuilt your branch, you could use the following command to rebuild the HTML version of the reference manual:\n\n```\n./sage -docbuild reference html\n```\n\n\n\n\n\n> Is SageObject the best superclass for this? \n\nNo, not really. Ideally, the best parent class for the class `BlumGoldwasser` is `sage.crypto.cryptosystem.PublicKeyCryptosystem`. I'll see what I can do to make `sage.crypto.cryptosystem.PublicKeyCryptosystem` the parent class of `BlumGoldwasser`.\n\n\n\n\n\n> Is the best place for blum_blum_shub in util or in a stream cipher module? \n\nI think the best place for the function `blum_blum_shub()` is in a module for pseudorandom number generators. The module that comes to mind is `sage/misc/prandom.py`. But all functions in that module are exported to the global name space, so those functions are available upon starting Sage, without having to explicitly import them. Adding more functions to the global name space is not a good idea. One wants to minimize Sage's loading time, but also to have a default set of common useful functions. Adding `blum_blum_shub()` to `sage/misc/prandom.py` and polluting the global name space is not my intention. The Blum-Blum-Shub pseudorandom bit generator is not as commonly used as, say, `random()` and `randint()`. For now, `blum_blum_shub()` fits OK in `sage/crypto/util.py`. Functions in that module are not exported by default, which is why you see lots of import statements throughout examples in that module.",
    "created_at": "2009-12-21T14:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 wdj]:
> It seems to violate the "defensive programming" (or "assume all people are stupid") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.

It looks to me that there needs to be a function called, say, "has_blum_prime(lbound, ubound)" in the module `sage/crypto/util.py`. This function checks to see if there is a Blum prime within the specified lower and upper bounds. One could then use `has_blum_prime()` to first check for the presence of a Blum prime within a specified interval, prior to actually computing a random Blum prime.





> Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in 

After you have applied the patch and rebuilt your branch, you could use the following command to rebuild the HTML version of the reference manual:

```
./sage -docbuild reference html
```





> Is SageObject the best superclass for this? 

No, not really. Ideally, the best parent class for the class `BlumGoldwasser` is `sage.crypto.cryptosystem.PublicKeyCryptosystem`. I'll see what I can do to make `sage.crypto.cryptosystem.PublicKeyCryptosystem` the parent class of `BlumGoldwasser`.





> Is the best place for blum_blum_shub in util or in a stream cipher module? 

I think the best place for the function `blum_blum_shub()` is in a module for pseudorandom number generators. The module that comes to mind is `sage/misc/prandom.py`. But all functions in that module are exported to the global name space, so those functions are available upon starting Sage, without having to explicitly import them. Adding more functions to the global name space is not a good idea. One wants to minimize Sage's loading time, but also to have a default set of common useful functions. Adding `blum_blum_shub()` to `sage/misc/prandom.py` and polluting the global name space is not my intention. The Blum-Blum-Shub pseudorandom bit generator is not as commonly used as, say, `random()` and `randint()`. For now, `blum_blum_shub()` fits OK in `sage/crypto/util.py`. Functions in that module are not exported by default, which is why you see lots of import statements throughout examples in that module.



---

archive/issue_comments_066564.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Replying to [comment:2 wdj]:\n\n\n> It looks to me that there needs to be a function called, say, \n> \"has_blum_prime(lbound, ubound)\" in the module `sage/crypto/util.py`. \n> This function checks to see if there is a Blum prime within the \n> specified lower and upper bounds. \n\n\nSounds good.\n\n\n> use the following command to rebuild the HTML version of the reference manual:\n> {{{\n> ./sage -docbuild reference html\n> }}}\n> \n\n> \n\n\nThanks. Docs compile fine and look great.\n\n\n\n> \n> \n> > Is the best place for blum_blum_shub in util or in a stream cipher module? \n> \n> I think the best place for the function `blum_blum_shub()` is in a module \n> for pseudorandom number generators. The module that comes to mind \n> is `sage/misc/prandom.py`. But all functions in that module are exported to the \n\nWhy not \n\n\n```\nsage/crypto/stream_cipher.py\n```\n\ninstead?",
    "created_at": "2009-12-22T03:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66564",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 mvngu]:
> Replying to [comment:2 wdj]:


> It looks to me that there needs to be a function called, say, 
> "has_blum_prime(lbound, ubound)" in the module `sage/crypto/util.py`. 
> This function checks to see if there is a Blum prime within the 
> specified lower and upper bounds. 


Sounds good.


> use the following command to rebuild the HTML version of the reference manual:
> {{{
> ./sage -docbuild reference html
> }}}
> 

> 


Thanks. Docs compile fine and look great.



> 
> 
> > Is the best place for blum_blum_shub in util or in a stream cipher module? 
> 
> I think the best place for the function `blum_blum_shub()` is in a module 
> for pseudorandom number generators. The module that comes to mind 
> is `sage/misc/prandom.py`. But all functions in that module are exported to the 

Why not 


```
sage/crypto/stream_cipher.py
```

instead?



---

archive/issue_comments_066565.json:
```json
{
    "body": "based on Sage 4.3.2",
    "created_at": "2010-02-12T05:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.3.2



---

archive/issue_comments_066566.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-12T05:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66566",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066567.json:
```json
{
    "body": "Attachment [trac_7746-blum-goldwasser.patch](tarball://root/attachments/some-uuid/ticket7746/trac_7746-blum-goldwasser.patch) by mvngu created at 2010-02-12 05:36:43\n\nReplying to [comment:4 wdj]:\n> Sounds good.\n\nI have attached an updated patch which also implements the function `has_blum_prime()`.\n\n\n\n\n\n> Why not \n> \n\n```\nsage/crypto/stream_cipher.py\n```\n\n> instead?\n\nThe module `sage/crypto/stream_cipher.py` acts as a back-end for `sage/crypto/stream.py`. I believe a more appropriate place is to put `blum_blum_shub()` in  `sage/crypto/stream.py`. The latest version of the patch does this.",
    "created_at": "2010-02-12T05:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66567",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7746-blum-goldwasser.patch](tarball://root/attachments/some-uuid/ticket7746/trac_7746-blum-goldwasser.patch) by mvngu created at 2010-02-12 05:36:43

Replying to [comment:4 wdj]:
> Sounds good.

I have attached an updated patch which also implements the function `has_blum_prime()`.





> Why not 
> 

```
sage/crypto/stream_cipher.py
```

> instead?

The module `sage/crypto/stream_cipher.py` acts as a back-end for `sage/crypto/stream.py`. I believe a more appropriate place is to put `blum_blum_shub()` in  `sage/crypto/stream.py`. The latest version of the patch does this.



---

archive/issue_comments_066568.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-13T13:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66568",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066569.json:
```json
{
    "body": "Applied fine to 4.3.3.a0 and passes sage -testall. Reference manual looks good too.\n\nPositive review.\n\nThank you very much Minh!",
    "created_at": "2010-02-13T13:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66569",
    "user": "https://github.com/wdjoyner"
}
```

Applied fine to 4.3.3.a0 and passes sage -testall. Reference manual looks good too.

Positive review.

Thank you very much Minh!



---

archive/issue_comments_066570.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-15T03:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7746#issuecomment-66570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007958.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-15T03:42:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7746",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7746#event-7958"
}
```
