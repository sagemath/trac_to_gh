# Issue 7124: affine cipher and its cryptanalysis

archive/issues_007124.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  rbeezer\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7124\n\n",
    "created_at": "2009-10-05T16:13:43Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "affine cipher and its cryptanalysis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7124",
    "user": "mvngu"
}
```
Assignee: somebody

CC:  rbeezer



Issue created by migration from https://trac.sagemath.org/ticket/7124





---

archive/issue_comments_059075.json:
```json
{
    "body": "Changing keywords from \"\" to \"affine cipher\".",
    "created_at": "2009-10-10T00:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59075",
    "user": "mvngu"
}
```

Changing keywords from "" to "affine cipher".



---

archive/issue_comments_059076.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-10T00:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59076",
    "user": "mvngu"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_059077.json:
```json
{
    "body": "The patch `trac_7124-affine.patch` implements the affine cryptosystem.",
    "created_at": "2009-10-10T00:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59077",
    "user": "mvngu"
}
```

The patch `trac_7124-affine.patch` implements the affine cryptosystem.



---

archive/issue_comments_059078.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-13T01:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59078",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059079.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-15T00:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59079",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059080.json:
```json
{
    "body": "In light of rbeezer's comments at #7123, I need to update the patches on this ticket since they depend on #7123. Also, I would like to add some more stuff to the patches for the affine cipher.",
    "created_at": "2009-10-15T00:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59080",
    "user": "mvngu"
}
```

In light of rbeezer's comments at #7123, I need to update the patches on this ticket since they depend on #7123. Also, I would like to add some more stuff to the patches for the affine cipher.



---

archive/issue_comments_059081.json:
```json
{
    "body": "Attachment [trac_7124_brute_force_output.txt](tarball://root/attachments/some-uuid/ticket7124/trac_7124_brute_force_output.txt) by rbeezer created at 2009-10-15 01:07:11\n\nSample output for odd behavior of `brute_force()`",
    "created_at": "2009-10-15T01:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59081",
    "user": "rbeezer"
}
```

Attachment [trac_7124_brute_force_output.txt](tarball://root/attachments/some-uuid/ticket7124/trac_7124_brute_force_output.txt) by rbeezer created at 2009-10-15 01:07:11

Sample output for odd behavior of `brute_force()`



---

archive/issue_comments_059082.json:
```json
{
    "body": "Minh,\n\nOutput of plain `brute_force()` looks suspicious, and when a ranking is suggested, errors are raised.  Tests are failing as well.  See attached.\n\nInside `brute_force()` method, should the `L` list be so empty?\n\nRob",
    "created_at": "2009-10-15T01:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59082",
    "user": "rbeezer"
}
```

Minh,

Output of plain `brute_force()` looks suspicious, and when a ranking is suggested, errors are raised.  Tests are failing as well.  See attached.

Inside `brute_force()` method, should the `L` list be so empty?

Rob



---

archive/issue_comments_059083.json:
```json
{
    "body": "Please try the latest patches based on Sage 4.1.2.rc2.",
    "created_at": "2009-10-15T01:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59083",
    "user": "mvngu"
}
```

Please try the latest patches based on Sage 4.1.2.rc2.



---

archive/issue_comments_059084.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-15T01:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59084",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059085.json:
```json
{
    "body": "\n```\n18:13 < mvngu> rbeezer: The output of brute_force() is all the 312 possible\n               dicipherments.\n18:14 < mvngu> rbeezer: It uses a list of list for an indexing scheme that's\n               meant for readability.\n18:14 < rbeezer> but I'm not getting the keys that achieves them\n18:14 < rbeezer> the L list is a list of empty lists??\n18:14 < mvngu> rbeezer: Let me upload my recent patches....\n18:14 < rbeezer> aah, that'd help  ;-) ;-)\n18:18 < mvngu> rbeezer: Uploaded patches.\n18:18 < mvngu> rbeezer: Note the ticket dependency.\n18:19 < rbeezer> thanks - do they include whatever prompted you to take the \n                 ticket back to \"needs work\"\n18:19 < mvngu> rbeezer: yes\n18:19 < rbeezer> In other words, should I attempt a full review in the next 6 \n                 hours, or no?\n18:19 < mvngu> rbeezer: I fixed some documentation typos, add an example on the \n               decimation cipher.\n18:20 < mvngu> rbeezer: And yes, I think it's ready for a full review.\n18:20 < mvngu> rbeezer: Thank you very much for spending time on these crypto \n               stuff!\n```\n",
    "created_at": "2009-10-15T01:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59085",
    "user": "mvngu"
}
```


```
18:13 < mvngu> rbeezer: The output of brute_force() is all the 312 possible
               dicipherments.
18:14 < mvngu> rbeezer: It uses a list of list for an indexing scheme that's
               meant for readability.
18:14 < rbeezer> but I'm not getting the keys that achieves them
18:14 < rbeezer> the L list is a list of empty lists??
18:14 < mvngu> rbeezer: Let me upload my recent patches....
18:14 < rbeezer> aah, that'd help  ;-) ;-)
18:18 < mvngu> rbeezer: Uploaded patches.
18:18 < mvngu> rbeezer: Note the ticket dependency.
18:19 < rbeezer> thanks - do they include whatever prompted you to take the 
                 ticket back to "needs work"
18:19 < mvngu> rbeezer: yes
18:19 < rbeezer> In other words, should I attempt a full review in the next 6 
                 hours, or no?
18:19 < mvngu> rbeezer: I fixed some documentation typos, add an example on the 
               decimation cipher.
18:20 < mvngu> rbeezer: And yes, I think it's ready for a full review.
18:20 < mvngu> rbeezer: Thank you very much for spending time on these crypto 
               stuff!
```




---

archive/issue_comments_059086.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-15T01:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59086",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059087.json:
```json
{
    "body": "At present, here's what happening with the method `brute_force()`: it returns a list of lists `L` that contains all the possible decipherments. And that's it, not even the key that results in a candidate decipherment. If you think the present behaviour is confusing, yes, I agree with that. Here's a sample session.\n\n```\nsage: A = AffineCryptosystem(AlphabeticStrings())\nsage: cipher = A(11, 4)\nsage: P = A.encoding(\"Have a nice day at the seashore.\")\nsage: C = cipher(P); C\nDEBWEROAWLEIEFFDWUWEUDCJW\nsage: candidates = A.brute_force(C)\nsage: candidates[1]\n\n[DEBWEROAWLEIEFFDWUWEUDCJW,\n CDAVDQNZVKDHDEECVTVDTCBIV,\n BCZUCPMYUJCGCDDBUSUCSBAHU,\n ABYTBOLXTIBFBCCATRTBRAZGT,\n ZAXSANKWSHAEABBZSQSAQZYFS,\n YZWRZMJVRGZDZAAYRPRZPYXER,\n XYVQYLIUQFYCYZZXQOQYOXWDQ,\n WXUPXKHTPEXBXYYWPNPXNWVCP,\n VWTOWJGSODWAWXXVOMOWMVUBO,\n UVSNVIFRNCVZVWWUNLNVLUTAN,\n TURMUHEQMBUYUVVTMKMUKTSZM,\n STQLTGDPLATXTUUSLJLTJSRYL,\n RSPKSFCOKZSWSTTRKIKSIRQXK,\n QROJREBNJYRVRSSQJHJRHQPWJ,\n PQNIQDAMIXQUQRRPIGIQGPOVI,\n OPMHPCZLHWPTPQQOHFHPFONUH,\n NOLGOBYKGVOSOPPNGEGOENMTG,\n MNKFNAXJFUNRNOOMFDFNDMLSF,\n LMJEMZWIETMQMNNLECEMCLKRE,\n KLIDLYVHDSLPLMMKDBDLBKJQD,\n JKHCKXUGCRKOKLLJCACKAJIPC,\n IJGBJWTFBQJNJKKIBZBJZIHOB,\n HIFAIVSEAPIMIJJHAYAIYHGNA,\n GHEZHURDZOHLHIIGZXZHXGFMZ,\n FGDYGTQCYNGKGHHFYWYGWFELY,\n EFCXFSPBXMFJFGGEXVXFVEDKX]\n```\n\nI think this is perhaps why you said the output of `brute_force()` is odd. In the method `brute_force()` of the shift cipher from #7123, it provides both the key together with the corresponding candidate decipherment. In the current affine cipher implementation, I forgot about the output of the brute force method in #7123. OK, move to \"needs work\" again.",
    "created_at": "2009-10-15T01:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59087",
    "user": "mvngu"
}
```

At present, here's what happening with the method `brute_force()`: it returns a list of lists `L` that contains all the possible decipherments. And that's it, not even the key that results in a candidate decipherment. If you think the present behaviour is confusing, yes, I agree with that. Here's a sample session.

```
sage: A = AffineCryptosystem(AlphabeticStrings())
sage: cipher = A(11, 4)
sage: P = A.encoding("Have a nice day at the seashore.")
sage: C = cipher(P); C
DEBWEROAWLEIEFFDWUWEUDCJW
sage: candidates = A.brute_force(C)
sage: candidates[1]

[DEBWEROAWLEIEFFDWUWEUDCJW,
 CDAVDQNZVKDHDEECVTVDTCBIV,
 BCZUCPMYUJCGCDDBUSUCSBAHU,
 ABYTBOLXTIBFBCCATRTBRAZGT,
 ZAXSANKWSHAEABBZSQSAQZYFS,
 YZWRZMJVRGZDZAAYRPRZPYXER,
 XYVQYLIUQFYCYZZXQOQYOXWDQ,
 WXUPXKHTPEXBXYYWPNPXNWVCP,
 VWTOWJGSODWAWXXVOMOWMVUBO,
 UVSNVIFRNCVZVWWUNLNVLUTAN,
 TURMUHEQMBUYUVVTMKMUKTSZM,
 STQLTGDPLATXTUUSLJLTJSRYL,
 RSPKSFCOKZSWSTTRKIKSIRQXK,
 QROJREBNJYRVRSSQJHJRHQPWJ,
 PQNIQDAMIXQUQRRPIGIQGPOVI,
 OPMHPCZLHWPTPQQOHFHPFONUH,
 NOLGOBYKGVOSOPPNGEGOENMTG,
 MNKFNAXJFUNRNOOMFDFNDMLSF,
 LMJEMZWIETMQMNNLECEMCLKRE,
 KLIDLYVHDSLPLMMKDBDLBKJQD,
 JKHCKXUGCRKOKLLJCACKAJIPC,
 IJGBJWTFBQJNJKKIBZBJZIHOB,
 HIFAIVSEAPIMIJJHAYAIYHGNA,
 GHEZHURDZOHLHIIGZXZHXGFMZ,
 FGDYGTQCYNGKGHHFYWYGWFELY,
 EFCXFSPBXMFJFGGEXVXFVEDKX]
```

I think this is perhaps why you said the output of `brute_force()` is odd. In the method `brute_force()` of the shift cipher from #7123, it provides both the key together with the corresponding candidate decipherment. In the current affine cipher implementation, I forgot about the output of the brute force method in #7123. OK, move to "needs work" again.



---

archive/issue_comments_059088.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-15T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59088",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059089.json:
```json
{
    "body": "rbeezer --- I think I have addressed your comment about the output of `brute_force()` being odd. Please use the latest version of the patches.",
    "created_at": "2009-10-15T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59089",
    "user": "mvngu"
}
```

rbeezer --- I think I have addressed your comment about the output of `brute_force()` being odd. Please use the latest version of the patches.



---

archive/issue_comments_059090.json:
```json
{
    "body": "Hi Minh,\n\nTwo comments:\n\n1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run\n\n`x=S.random_key(); print x, S.inverse_key(*x)` \n\nrepeatedly.\n\nThis shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).\n\nMaybe you just need subtraction someplace where you have a addition, or...\n\n2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem?  Then you could skip some of the gcd-stuff.  For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing.  Or when checking validity for a new key, you could just test on the list.  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.\n\nRob",
    "created_at": "2009-10-16T05:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59090",
    "user": "rbeezer"
}
```

Hi Minh,

Two comments:

1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run

`x=S.random_key(); print x, S.inverse_key(*x)` 

repeatedly.

This shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).

Maybe you just need subtraction someplace where you have a addition, or...

2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem?  Then you could skip some of the gcd-stuff.  For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing.  Or when checking validity for a new key, you could just test on the list.  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.

Rob



---

archive/issue_comments_059091.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-16T05:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59091",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059092.json:
```json
{
    "body": "Replying to [comment:11 rbeezer]:\n> 1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run\n\n```\nx=S.random_key(); print x, S.inverse_key(*x)\n```\n\n> repeatedly. This shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).\n\nI may be misunderstanding your comment here, so please tell me if that's the case. Any key `(a,b) in ZZ/nZZ x ZZ/nZZ` of the affine cipher is such that `gcd(a,n) = 1`. So you're saying that the inverse key corresponding to `(a, b)` is `(a^{-1}, -b)` where `a^{-1}` is the multiplicative inverse of `a` modulo `n`? If that is the case, then the current implementation of `inverse_key()` is clearly broken:\n\n```\n        try:\n            from copy import copy\n            from sage.rings.arith import inverse_mod\n            n = self.alphabet_size()\n            return (inverse_mod(a, n), copy(b))\n        except:\n            raise ValueError(\"(a, b) = (%s, %s) is outside the range of acceptable values for a key of this affine cipher.\" % (a, b))\n```\n\n\nHow then would one use the above defined inverse key to decrypt a ciphertext? The current implementation of the method `deciphering()` follows this Wikipedia description of the encryption and decryption functions of the affine cipher:\n\nhttp://en.wikipedia.org/wiki/Affine_cipher\n\nThis agrees with the following text that I have access to:\n\n* Doug Stinson. \"Cryptography: Theory and Practice\" 3rd edition.\n* Wade Trappe and Lawrence C. Washington. \"Introduction to Cryptography with Coding Theory\"\n\n\n\n\n\n> Maybe you just need subtraction someplace where you have a addition, or...\n\nI don't quite understand this comment. Can you please explain it?\n\n\n\n\n\n> 2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem? \n\nYes it does make sense to do so, and I have implemented this in response to your suggestion. The resulting code of the affine crypto module looks less \"ugly\" from my point of view. Thank you, Rob. Please see the latest version of the patches.\n\n\n\n\n\n> Then you could skip some of the gcd-stuff.\n\nAnd I have skipped some of the GCD computation with the above implementation of a list of invertible elements in the multiplicative group of `ZZ/nZZ`.\n\n\n\n\n\n> For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing. \n\nDone according to your suggestion.\n\n\n\n\n\n> Or when checking validity for a new key, you could just test on the list. \n\nDone according to your suggestion.\n\n\n\n\n\n>  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.\n\nI can see in my mind how to implement this based on the implementation of generating invertible elements in the multiplicative group of `ZZ/nZZ`. I think this would entail changing the implementation of the class(es) that implement say, the hexadecimal monoid. Getting the affine cipher to support the hexadecimal and radix-64 monoids should be another ticket in itself.",
    "created_at": "2009-10-16T20:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59092",
    "user": "mvngu"
}
```

Replying to [comment:11 rbeezer]:
> 1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run

```
x=S.random_key(); print x, S.inverse_key(*x)
```

> repeatedly. This shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).

I may be misunderstanding your comment here, so please tell me if that's the case. Any key `(a,b) in ZZ/nZZ x ZZ/nZZ` of the affine cipher is such that `gcd(a,n) = 1`. So you're saying that the inverse key corresponding to `(a, b)` is `(a^{-1}, -b)` where `a^{-1}` is the multiplicative inverse of `a` modulo `n`? If that is the case, then the current implementation of `inverse_key()` is clearly broken:

```
        try:
            from copy import copy
            from sage.rings.arith import inverse_mod
            n = self.alphabet_size()
            return (inverse_mod(a, n), copy(b))
        except:
            raise ValueError("(a, b) = (%s, %s) is outside the range of acceptable values for a key of this affine cipher." % (a, b))
```


How then would one use the above defined inverse key to decrypt a ciphertext? The current implementation of the method `deciphering()` follows this Wikipedia description of the encryption and decryption functions of the affine cipher:

http://en.wikipedia.org/wiki/Affine_cipher

This agrees with the following text that I have access to:

* Doug Stinson. "Cryptography: Theory and Practice" 3rd edition.
* Wade Trappe and Lawrence C. Washington. "Introduction to Cryptography with Coding Theory"





> Maybe you just need subtraction someplace where you have a addition, or...

I don't quite understand this comment. Can you please explain it?





> 2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem? 

Yes it does make sense to do so, and I have implemented this in response to your suggestion. The resulting code of the affine crypto module looks less "ugly" from my point of view. Thank you, Rob. Please see the latest version of the patches.





> Then you could skip some of the gcd-stuff.

And I have skipped some of the GCD computation with the above implementation of a list of invertible elements in the multiplicative group of `ZZ/nZZ`.





> For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing. 

Done according to your suggestion.





> Or when checking validity for a new key, you could just test on the list. 

Done according to your suggestion.





>  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.

I can see in my mind how to implement this based on the implementation of generating invertible elements in the multiplicative group of `ZZ/nZZ`. I think this would entail changing the implementation of the class(es) that implement say, the hexadecimal monoid. Getting the affine cipher to support the hexadecimal and radix-64 monoids should be another ticket in itself.



---

archive/issue_comments_059093.json:
```json
{
    "body": "Replying to [comment:12 mvngu]:\n\nWell, I didn't really say exactly what `inverse_key()` should be on purpose - figuring it was your thesis and I shouldn't have all the fun.\n\nWikipedia is right on this one and it's what you have implemented in the deciphering routine.\n\nIf enciphering is accomplished by  x -> ax+b  (ie key is (a,b)) then \n\ndeciphering is accomplished by  `x -> a^{-1}(x-b) = a^{-1}x - a^{-1}b`\n\nso the inverse key would be the pair `(a^{-1}, -a^{-1}b)`\n\nNote the constant term.  In other words, the inverse key should be what you use for the same algorithm (linear function mod 26) to reverse the process, ie create the inverse function.\n\nTry the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.\n\n1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.\n\n2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.",
    "created_at": "2009-10-16T23:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59093",
    "user": "rbeezer"
}
```

Replying to [comment:12 mvngu]:

Well, I didn't really say exactly what `inverse_key()` should be on purpose - figuring it was your thesis and I shouldn't have all the fun.

Wikipedia is right on this one and it's what you have implemented in the deciphering routine.

If enciphering is accomplished by  x -> ax+b  (ie key is (a,b)) then 

deciphering is accomplished by  `x -> a^{-1}(x-b) = a^{-1}x - a^{-1}b`

so the inverse key would be the pair `(a^{-1}, -a^{-1}b)`

Note the constant term.  In other words, the inverse key should be what you use for the same algorithm (linear function mod 26) to reverse the process, ie create the inverse function.

Try the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.

1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.

2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.



---

archive/issue_comments_059094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-17T02:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59094",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059095.json:
```json
{
    "body": "Replying to [comment:13 rbeezer]:\n> Try the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.\n\nI have added this doctest.\n\n\n\n\n\n> 1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.\n\nDone.\n\n\n\n\n\n> 2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.\n\nIt can be generalized to other non-empty alphabets with more than 2 elements. An alphabet with 2 elements is not interesting enough to use for studying the affine cipher. In fact, I think that with the current implementation of the affine cipher, one can extend it to support alphabets such as the octal and hexadecimal number systems, radix-64 alphabet, and even the ASCII alphabet itself. It's just that doing so is tedious work for which I don't currently have time for. The same can be said for the shift cipher as well.",
    "created_at": "2009-10-17T02:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59095",
    "user": "mvngu"
}
```

Replying to [comment:13 rbeezer]:
> Try the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.

I have added this doctest.





> 1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.

Done.





> 2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.

It can be generalized to other non-empty alphabets with more than 2 elements. An alphabet with 2 elements is not interesting enough to use for studying the affine cipher. In fact, I think that with the current implementation of the affine cipher, one can extend it to support alphabets such as the octal and hexadecimal number systems, radix-64 alphabet, and even the ASCII alphabet itself. It's just that doing so is tedious work for which I don't currently have time for. The same can be said for the shift cipher as well.



---

archive/issue_comments_059096.json:
```json
{
    "body": "Minh,\n\nSome specific comments:\n\n1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.\n\n2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.\n\n3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.\n\nRob",
    "created_at": "2009-10-17T05:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59096",
    "user": "rbeezer"
}
```

Minh,

Some specific comments:

1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.

2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.

3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.

Rob



---

archive/issue_comments_059097.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-17T05:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59097",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059098.json:
```json
{
    "body": "based on Sage 4.1.2.rc2 and #7123",
    "created_at": "2009-10-17T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59098",
    "user": "mvngu"
}
```

based on Sage 4.1.2.rc2 and #7123



---

archive/issue_comments_059099.json:
```json
{
    "body": "Attachment [trac_7124-affine.patch](tarball://root/attachments/some-uuid/ticket7124/trac_7124-affine.patch) by mvngu created at 2009-10-17 06:31:45\n\napply on top of previous",
    "created_at": "2009-10-17T06:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59099",
    "user": "mvngu"
}
```

Attachment [trac_7124-affine.patch](tarball://root/attachments/some-uuid/ticket7124/trac_7124-affine.patch) by mvngu created at 2009-10-17 06:31:45

apply on top of previous



---

archive/issue_comments_059100.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-17T06:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59100",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059101.json:
```json
{
    "body": "Attachment [trac_7124-cryptanalysis.patch](tarball://root/attachments/some-uuid/ticket7124/trac_7124-cryptanalysis.patch) by mvngu created at 2009-10-17 06:36:45\n\nReplying to [comment:15 rbeezer]:\n> 1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.\n\nFixed.\n\n\n\n\n\n> 2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.\n\nI have removed the test. In its place, I added some comments explaining why we don't need to test that each `a` is coprime to `n`, the alphabet size.\n\n\n\n\n\n> 3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.\n\nThat doctest is meant to explain what sort of values that `a` can take on if `(a,b)` is to be a secret key. I have rewritten the doctest to explain this.",
    "created_at": "2009-10-17T06:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59101",
    "user": "mvngu"
}
```

Attachment [trac_7124-cryptanalysis.patch](tarball://root/attachments/some-uuid/ticket7124/trac_7124-cryptanalysis.patch) by mvngu created at 2009-10-17 06:36:45

Replying to [comment:15 rbeezer]:
> 1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.

Fixed.





> 2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.

I have removed the test. In its place, I added some comments explaining why we don't need to test that each `a` is coprime to `n`, the alphabet size.





> 3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.

That doctest is meant to explain what sort of values that `a` can take on if `(a,b)` is to be a secret key. I have rewritten the doctest to explain this.



---

archive/issue_comments_059102.json:
```json
{
    "body": "This should be pretty much read to go now, but I've got a six errors being raised in the doctests.  They all seem to be due to lines 2912 and 3158 of  classical.py  which are identical\n\n`OM.setdefault(e, 0.0)`\n\nThe error is\n\n`AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`",
    "created_at": "2009-10-19T02:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59102",
    "user": "rbeezer"
}
```

This should be pretty much read to go now, but I've got a six errors being raised in the doctests.  They all seem to be due to lines 2912 and 3158 of  classical.py  which are identical

`OM.setdefault(e, 0.0)`

The error is

`AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`



---

archive/issue_comments_059103.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-19T02:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59103",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059104.json:
```json
{
    "body": "Replying to [comment:17 rbeezer]:\n> The error is\n> \n> `AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`\n\nI took Sage 4.2 and successfully applied the attached two patches. The reference manual rebuilt successfully. Doctesting the whole Sage library didn't show up the error you reported. Can you please try using Sage 4.2? Please tell me if I've misunderstood your comments.",
    "created_at": "2009-10-28T12:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59104",
    "user": "mvngu"
}
```

Replying to [comment:17 rbeezer]:
> The error is
> 
> `AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`

I took Sage 4.2 and successfully applied the attached two patches. The reference manual rebuilt successfully. Doctesting the whole Sage library didn't show up the error you reported. Can you please try using Sage 4.2? Please tell me if I've misunderstood your comments.



---

archive/issue_comments_059105.json:
```json
{
    "body": "Alright, against 4.2 there are no doctest errors in sage/crypto, so this is done.\n\nPositive review.\n\nRelease manager: apply two patches - first \"affine\" then \"cryptanalysis.\"",
    "created_at": "2009-10-30T04:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59105",
    "user": "rbeezer"
}
```

Alright, against 4.2 there are no doctest errors in sage/crypto, so this is done.

Positive review.

Release manager: apply two patches - first "affine" then "cryptanalysis."



---

archive/issue_comments_059106.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-30T04:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59106",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059107.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-30T04:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59107",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7124#issuecomment-59108",
    "user": "mhansen"
}
```

Resolution: fixed
