# Issue 2024: [with patch, needs review] univariate gcd over Z_N (N composite)

archive/issues_002024.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe attached patch implements GCDs for univariate polynomials over Z_N where N is composite by calling PARI.\n\n**EXAMPLE**\n\nA standard attack on textbook RSA due to Franklin and\nReiter: Consider that we are given two ciphertexts c<sub>1</sub>\nand c<sub>2</sub> and the knowledge that the matching plaintexts\nare related by m<sub>2</sub> = m<sub>1</sub> + 2<sup>10</sup>. We also know the public\nkey (N,e) and that e is rather small. Then we can\nrecover the plaintext using a GCD computation for two\nunivariate polynomials.\n\n```\nsage: N = 2157212598407\nsage: e = 3\nsage: c1 = 1429779991932\nsage: c2 =  655688908482\nsage: P.<x> = PolynomialRing(Zmod(N))\nsage: f1 = x^e - c1\nsage: f2 = (x+2^10)^e - c2\nsage: g = gcd(f1,f2); g\nx + 2155978030517\nsage: m = -g[0]; m\n1234567890\n            \nsage: m^e\n1429779991932\n```\n\n\nSurprisingly, MAGMA cannot perform this operation:\n\n\n```\nsage: f1._magma_().GCD(f2._magma_())\nException (click to the left for traceback):\n...\nRuntime error in 'GCD': Algorithm is not available for this kind of coefficient ring\n```\n\n\nThe example is from http://www.isg.rhul.ac.uk/~sdg/mt466/lecture12.pdf which also claims that Mathematica cannot perform this operation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2024\n\n",
    "created_at": "2008-02-01T11:51:40Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] univariate gcd over Z_N (N composite)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2024",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

The attached patch implements GCDs for univariate polynomials over Z_N where N is composite by calling PARI.

**EXAMPLE**

A standard attack on textbook RSA due to Franklin and
Reiter: Consider that we are given two ciphertexts c<sub>1</sub>
and c<sub>2</sub> and the knowledge that the matching plaintexts
are related by m<sub>2</sub> = m<sub>1</sub> + 2<sup>10</sup>. We also know the public
key (N,e) and that e is rather small. Then we can
recover the plaintext using a GCD computation for two
univariate polynomials.

```
sage: N = 2157212598407
sage: e = 3
sage: c1 = 1429779991932
sage: c2 =  655688908482
sage: P.<x> = PolynomialRing(Zmod(N))
sage: f1 = x^e - c1
sage: f2 = (x+2^10)^e - c2
sage: g = gcd(f1,f2); g
x + 2155978030517
sage: m = -g[0]; m
1234567890
            
sage: m^e
1429779991932
```


Surprisingly, MAGMA cannot perform this operation:


```
sage: f1._magma_().GCD(f2._magma_())
Exception (click to the left for traceback):
...
Runtime error in 'GCD': Algorithm is not available for this kind of coefficient ring
```


The example is from http://www.isg.rhul.ac.uk/~sdg/mt466/lecture12.pdf which also claims that Mathematica cannot perform this operation.

Issue created by migration from https://trac.sagemath.org/ticket/2024





---

archive/issue_comments_013052.json:
```json
{
    "body": "Attachment [trac_2024_gcd.patch](tarball://root/attachments/some-uuid/ticket2024/trac_2024_gcd.patch) by dmharvey created at 2008-02-01 23:55:10\n\nhuh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.",
    "created_at": "2008-02-01T23:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13052",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac_2024_gcd.patch](tarball://root/attachments/some-uuid/ticket2024/trac_2024_gcd.patch) by dmharvey created at 2008-02-01 23:55:10

huh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.



---

archive/issue_comments_013053.json:
```json
{
    "body": "Replying to [comment:1 dmharvey]:\n> huh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.\n\nI agree.  What is the gcd of `2 x` and `4 x` over `Z_8[x]`?  Should this return all divisors of largest degree?\n\nAs it stands, I think this patch should not be applied.",
    "created_at": "2008-02-02T00:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13053",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:1 dmharvey]:
> huh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.

I agree.  What is the gcd of `2 x` and `4 x` over `Z_8[x]`?  Should this return all divisors of largest degree?

As it stands, I think this patch should not be applied.



---

archive/issue_comments_013054.json:
```json
{
    "body": "I wrote `gcd(a,b)` for elements a,b in Z/NZ without further comment in an early version of my elementary number theory book, and when Brian Conrad saw that he went ballistic.  So I'm with you guys on now having this function unless its name is changed and the precise meaning of what is being computed is clarified.",
    "created_at": "2008-02-02T05:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13054",
    "user": "https://github.com/williamstein"
}
```

I wrote `gcd(a,b)` for elements a,b in Z/NZ without further comment in an early version of my elementary number theory book, and when Brian Conrad saw that he went ballistic.  So I'm with you guys on now having this function unless its name is changed and the precise meaning of what is being computed is clarified.



---

archive/issue_comments_013055.json:
```json
{
    "body": "replacement patch gcd -> common_divisor",
    "created_at": "2008-02-02T14:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13055",
    "user": "https://github.com/malb"
}
```

replacement patch gcd -> common_divisor



---

archive/issue_comments_013056.json:
```json
{
    "body": "Attachment [trac_2024_gcd.2.patch](tarball://root/attachments/some-uuid/ticket2024/trac_2024_gcd.2.patch) by @malb created at 2008-02-02 14:33:10\n\nThe attached patch renames `gcd` to `common_divisor` and adds some documentation. Also, some `_sig_on`/{{{_sig_off}}s were added to avoid zero divisions.",
    "created_at": "2008-02-02T14:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13056",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2024_gcd.2.patch](tarball://root/attachments/some-uuid/ticket2024/trac_2024_gcd.2.patch) by @malb created at 2008-02-02 14:33:10

The attached patch renames `gcd` to `common_divisor` and adds some documentation. Also, some `_sig_on`/{{{_sig_off}}s were added to avoid zero divisions.



---

archive/issue_comments_013057.json:
```json
{
    "body": "Sorry, this still doesn't make much sense to me.\n\nFrom the docstring:\n\n```\nPerform Euclid's algorithm and return a common divisor of \n\\code{self} and \\code{other} as a monic polynomial. This is \nsimilar to a GCD computation over a GCD domain.\n```\n\n\nProblems:\n\nFirst, what is Euclid's algorithm here? For Euclid's algorithm you need a division algorithm, but I don't know what the division algorithm would be for `Z_N[x]` (at least when the divisor is not monic).\n\nSecond, sometimes there is *no* monic polynomial dividing both inputs. For example if N = 4, then 2x+1 is not divisible by *any* monic polynomial.\n\nThird, what does the PARI documentation claim will happen when you call the gcd code over such a base ring? I'm too lazy to check. From memory, the NTL documentation specifically says that the modulus needs to be prime for any polynomial gcd routine. (I've had situations with a prime power modulus, where the gcd almost makes sense, but I still couldn't use the vanilla gcd routine, it would sometimes crash; I needed to write a p-adic gcd instead.)\n\nYou either need to specify precisely something that makes sense, or just bite the bullet and write in the docstring \"this will call PARI's gcd routine and if the modulus is not prime then we don't promise anything and good luck to you\". It seems that the reason you want to include this function at all is for the cryptographic application. That's fine (it's a nice application), but if we want this function in SAGE then it has to be something that mathematically make sense.",
    "created_at": "2008-02-02T22:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13057",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Sorry, this still doesn't make much sense to me.

From the docstring:

```
Perform Euclid's algorithm and return a common divisor of 
\code{self} and \code{other} as a monic polynomial. This is 
similar to a GCD computation over a GCD domain.
```


Problems:

First, what is Euclid's algorithm here? For Euclid's algorithm you need a division algorithm, but I don't know what the division algorithm would be for `Z_N[x]` (at least when the divisor is not monic).

Second, sometimes there is *no* monic polynomial dividing both inputs. For example if N = 4, then 2x+1 is not divisible by *any* monic polynomial.

Third, what does the PARI documentation claim will happen when you call the gcd code over such a base ring? I'm too lazy to check. From memory, the NTL documentation specifically says that the modulus needs to be prime for any polynomial gcd routine. (I've had situations with a prime power modulus, where the gcd almost makes sense, but I still couldn't use the vanilla gcd routine, it would sometimes crash; I needed to write a p-adic gcd instead.)

You either need to specify precisely something that makes sense, or just bite the bullet and write in the docstring "this will call PARI's gcd routine and if the modulus is not prime then we don't promise anything and good luck to you". It seems that the reason you want to include this function at all is for the cryptographic application. That's fine (it's a nice application), but if we want this function in SAGE then it has to be something that mathematically make sense.



---

archive/issue_comments_013058.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-03T00:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13058",
    "user": "https://github.com/malb"
}
```

Resolution: invalid



---

archive/issue_comments_013059.json:
```json
{
    "body": "> if we want this function in SAGE then it has to be something that mathematically\n> make sense.\n\nI agree. Because I cannot provide anything sensible due to time constraints and lack of background I withdraw the patch.",
    "created_at": "2008-02-03T00:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13059",
    "user": "https://github.com/malb"
}
```

> if we want this function in SAGE then it has to be something that mathematically
> make sense.

I agree. Because I cannot provide anything sensible due to time constraints and lack of background I withdraw the patch.



---

archive/issue_comments_013060.json:
```json
{
    "body": "What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?",
    "created_at": "2008-02-03T00:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13060",
    "user": "https://github.com/williamstein"
}
```

What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?



---

archive/issue_comments_013061.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?\n\nMhh, I realised that checking for `is_nilpotent` is not sufficient, so I wonder what exactly to check for, maybe: `any(not x.is_unit() for x in f)`? In any case `_sig_on`/`_sig_off`s need to be added somehow.",
    "created_at": "2008-02-03T00:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13061",
    "user": "https://github.com/malb"
}
```

Replying to [comment:8 was]:
> What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?

Mhh, I realised that checking for `is_nilpotent` is not sufficient, so I wonder what exactly to check for, maybe: `any(not x.is_unit() for x in f)`? In any case `_sig_on`/`_sig_off`s need to be added somehow.



---

archive/issue_comments_013062.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-03T01:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13062",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_013063.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-02-03T01:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13063",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_013064.json:
```json
{
    "body": "The pari documentation just says that gcd uses the subresultant algorithm in this case.  It certainly does not give a run-time error:\n\n\n```\n? f=x^20-1\n%8 = x^20 - 1\n? g=x^25-1\n%9 = x^25 - 1\n? gcd(f,g)\n%10 = x^5 - 1\n? gcd(f*Mod(1,15),g*Mod(1,15))\n%11 = Mod(1, 15)*x^5 + Mod(14, 15)\n? lift(%)\n%12 = x^5 + 14\n```\n\nBut I agree with earlier contributors that unless we can define what the output is then we should not include this function.",
    "created_at": "2008-02-16T20:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13064",
    "user": "https://github.com/JohnCremona"
}
```

The pari documentation just says that gcd uses the subresultant algorithm in this case.  It certainly does not give a run-time error:


```
? f=x^20-1
%8 = x^20 - 1
? g=x^25-1
%9 = x^25 - 1
? gcd(f,g)
%10 = x^5 - 1
? gcd(f*Mod(1,15),g*Mod(1,15))
%11 = Mod(1, 15)*x^5 + Mod(14, 15)
? lift(%)
%12 = x^5 + 14
```

But I agree with earlier contributors that unless we can define what the output is then we should not include this function.



---

archive/issue_comments_013065.json:
```json
{
    "body": "Closing this ticket, per IRC discussion with malb (see also #2497):\n\n\n```\n[2:20pm] dmharvey: ok I'm looking at the 2nd patch file\n[2:20pm] dmharvey: basically consists of:\n[2:20pm] dmharvey: (1) removing commented-out crud\n[2:20pm] dmharvey: (2) adding a _sig_on/_sig_off somewhere\n[2:20pm] dmharvey: (3) adding common_divisor which I don't know if I believe in\n[2:20pm] dmharvey: (4) some right.is_nilpotent() tests\n[2:20pm] malb: (3) is out\n[2:20pm] dmharvey: ok\n[2:21pm] dmharvey: so that's basically the guts of the ticket\n[2:21pm] malb: I think (4) is not sufficient\n[2:21pm] dmharvey: ok just hang on a second\n[2:21pm] dmharvey: so do we agree the ticket is essentially invalid?\n[2:21pm] malb: yes\n[2:21pm] dmharvey: ok\n[2:21pm] malb: I closed it before\n[2:21pm] dmharvey: for (4), I don't understand what you're trying to do there\n[2:22pm] malb: don't crash\n[2:22pm] malb: that's all\n[2:22pm] dmharvey: ah\n[2:22pm] dmharvey: so ZZ_pX_DivRem can crash/.\n[2:22pm] dmharvey: hmmm\n[2:22pm] dmharvey: perhaps that should be a separate ticket anyway.\n[2:22pm] malb: yep\n[2:22pm] dmharvey: do you know how to make it crash?\n[2:23pm] malb: so this one is invalid but we open another one for the crashes\n[2:23pm] dmharvey: given how expensive ZZ_pX_DivRem is compared to setting up the signal handler, I'd be inclined to just call sig_on universally\n[2:24pm] malb: sage: N = 35\n[2:24pm] malb: sage: P.<x> = PolynomialRing(Zmod(N))\n[2:24pm] malb: sage: 7*x//(5*x)\n[2:24pm] malb: InvMod: inverse undefined\n[2:24pm] malb: /usr/local/sage-2.11/local/bin/sage-sage: line 214: 30395 Aborted                sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n[2:24pm] malb: okay, I have no idea how expensive it is\n[2:24pm] dmharvey: well, how expensive is _sig_on?\n[2:24pm] malb: it is a system call\n[2:25pm] malb: the siglongjmp\n[2:25pm] dmharvey: and 5*x is not nilpotent :-)\n[2:26pm] dmharvey: the Right Way to deal with this is to make NTL return error codes more nicely\n[2:26pm] dmharvey: instead of aborting\n[2:27pm] malb: yep\n[2:28pm] malb: but that requires changing NTL\n[2:28pm] dmharvey: malb: okay, I think the rest of the patch is probably not worth resurrecting. I will report that crash as a separate ticket (I have a feeling I've seen it before already?), and close #2024, does that sound ok?\n[2:28pm] malb: yes\n[2:28pm] dmharvey: yeah I think it's already #2497\n[2:28pm] malb: ack\n[2:29pm] dmharvey: ok I will do that\n```\n",
    "created_at": "2008-04-05T18:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13065",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Closing this ticket, per IRC discussion with malb (see also #2497):


```
[2:20pm] dmharvey: ok I'm looking at the 2nd patch file
[2:20pm] dmharvey: basically consists of:
[2:20pm] dmharvey: (1) removing commented-out crud
[2:20pm] dmharvey: (2) adding a _sig_on/_sig_off somewhere
[2:20pm] dmharvey: (3) adding common_divisor which I don't know if I believe in
[2:20pm] dmharvey: (4) some right.is_nilpotent() tests
[2:20pm] malb: (3) is out
[2:20pm] dmharvey: ok
[2:21pm] dmharvey: so that's basically the guts of the ticket
[2:21pm] malb: I think (4) is not sufficient
[2:21pm] dmharvey: ok just hang on a second
[2:21pm] dmharvey: so do we agree the ticket is essentially invalid?
[2:21pm] malb: yes
[2:21pm] dmharvey: ok
[2:21pm] malb: I closed it before
[2:21pm] dmharvey: for (4), I don't understand what you're trying to do there
[2:22pm] malb: don't crash
[2:22pm] malb: that's all
[2:22pm] dmharvey: ah
[2:22pm] dmharvey: so ZZ_pX_DivRem can crash/.
[2:22pm] dmharvey: hmmm
[2:22pm] dmharvey: perhaps that should be a separate ticket anyway.
[2:22pm] malb: yep
[2:22pm] dmharvey: do you know how to make it crash?
[2:23pm] malb: so this one is invalid but we open another one for the crashes
[2:23pm] dmharvey: given how expensive ZZ_pX_DivRem is compared to setting up the signal handler, I'd be inclined to just call sig_on universally
[2:24pm] malb: sage: N = 35
[2:24pm] malb: sage: P.<x> = PolynomialRing(Zmod(N))
[2:24pm] malb: sage: 7*x//(5*x)
[2:24pm] malb: InvMod: inverse undefined
[2:24pm] malb: /usr/local/sage-2.11/local/bin/sage-sage: line 214: 30395 Aborted                sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
[2:24pm] malb: okay, I have no idea how expensive it is
[2:24pm] dmharvey: well, how expensive is _sig_on?
[2:24pm] malb: it is a system call
[2:25pm] malb: the siglongjmp
[2:25pm] dmharvey: and 5*x is not nilpotent :-)
[2:26pm] dmharvey: the Right Way to deal with this is to make NTL return error codes more nicely
[2:26pm] dmharvey: instead of aborting
[2:27pm] malb: yep
[2:28pm] malb: but that requires changing NTL
[2:28pm] dmharvey: malb: okay, I think the rest of the patch is probably not worth resurrecting. I will report that crash as a separate ticket (I have a feeling I've seen it before already?), and close #2024, does that sound ok?
[2:28pm] malb: yes
[2:28pm] dmharvey: yeah I think it's already #2497
[2:28pm] malb: ack
[2:29pm] dmharvey: ok I will do that
```




---

archive/issue_comments_013066.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-04-05T18:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2024#issuecomment-13066",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: invalid
