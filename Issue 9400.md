# Issue 9400: modify the NumberField constructor to pass in optional integer B such that all the internal pari routines will replace the discriminant by its gcd with B, making some things massively faster.

archive/issues_009400.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  jdemeyer\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9400\n\n",
    "created_at": "2010-07-01T03:43:21Z",
    "labels": [
        "number fields",
        "major",
        "enhancement"
    ],
    "title": "modify the NumberField constructor to pass in optional integer B such that all the internal pari routines will replace the discriminant by its gcd with B, making some things massively faster.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9400",
    "user": "was"
}
```
Assignee: davidloeffler

CC:  jdemeyer



Issue created by migration from https://trac.sagemath.org/ticket/9400





---

archive/issue_comments_089529.json:
```json
{
    "body": "Example of what this makes possible:\n\n```\n~wstein/bin/sagedb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x> = QQ[]\nsage: f = (x^20 - 3*x^19 - 29*x^18 + 91*x^17 + 338*x^16 - 1130*x^15 -\n2023*x^14 +\n....: 7432*x^13 + 6558*x^12 - 28021*x^11 - 10909*x^10 + 61267*x^9 + 6954*x^8 -\n....: 74752*x^7 + 1407*x^6 + 46330*x^5 - 1087*x^4 - 12558*x^3 - 942*x^2 +\n....: 960*x + 148)\nsage: K.<a> = NumberField(f^2+2, maximize_at_primes=[2])\nsage: K.degree()\n40\nsage: time z = K.factor(2)\nCPU times: user 0.59 s, sys: 0.01 s, total: 0.60 s\nWall time: 0.60 s\nsage: time k = z[0][0].residue_field()\nCPU times: user 1.68 s, sys: 0.03 s, total: 1.71 s\nWall time: 1.98 s\nsage: time k(a^3+3)\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\nabar^3 + 1\n```\n",
    "created_at": "2010-07-01T06:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89529",
    "user": "was"
}
```

Example of what this makes possible:

```
~wstein/bin/sagedb
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = QQ[]
sage: f = (x^20 - 3*x^19 - 29*x^18 + 91*x^17 + 338*x^16 - 1130*x^15 -
2023*x^14 +
....: 7432*x^13 + 6558*x^12 - 28021*x^11 - 10909*x^10 + 61267*x^9 + 6954*x^8 -
....: 74752*x^7 + 1407*x^6 + 46330*x^5 - 1087*x^4 - 12558*x^3 - 942*x^2 +
....: 960*x + 148)
sage: K.<a> = NumberField(f^2+2, maximize_at_primes=[2])
sage: K.degree()
40
sage: time z = K.factor(2)
CPU times: user 0.59 s, sys: 0.01 s, total: 0.60 s
Wall time: 0.60 s
sage: time k = z[0][0].residue_field()
CPU times: user 1.68 s, sys: 0.03 s, total: 1.71 s
Wall time: 1.98 s
sage: time k(a^3+3)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
abar^3 + 1
```




---

archive/issue_comments_089530.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-11T22:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89530",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089531.json:
```json
{
    "body": "It is clear from a very first look at the patch that this will massively conflict with #9343 (why did nobody point this out to me earlier???).  Personally, I would prefer to postpone the last two points of the description, i.e.\n\n* implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster \n\n* make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.\n\nand do them after #9343 is merged (I also want to change the hashing of PARI objects, see #9667).  Also, I'm personally not completely convinced about the best way to print NumberFieldIdeals (see also my post at sage-devel).",
    "created_at": "2010-08-12T06:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89531",
    "user": "jdemeyer"
}
```

It is clear from a very first look at the patch that this will massively conflict with #9343 (why did nobody point this out to me earlier???).  Personally, I would prefer to postpone the last two points of the description, i.e.

* implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster 

* make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.

and do them after #9343 is merged (I also want to change the hashing of PARI objects, see #9667).  Also, I'm personally not completely convinced about the best way to print NumberFieldIdeals (see also my post at sage-devel).



---

archive/issue_comments_089532.json:
```json
{
    "body": "> It is clear from a very first look at the patch that this will massively conflict with #9343 (why \n\nI'm sure this will be easy to merge with #9343.  It's probably best to get 9343 in first, since it is much more difficult, then rebase the current patch against it.\n\n> I would prefer to postpone:  hashing, printing\n\nThe current hashing and printing setup is complete and total crap, and needs to be removed ASAP.  It renders number fields completely useless for any nontrivial applications that involve prime ideals. \n\n> Also, I'm personally not completely convinced about the best way to print \n\nI saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be). Print in reduced form only in small trivial cases (by default), but allow the user to easily up the cutoff if they want, for some reason.",
    "created_at": "2010-08-12T11:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89532",
    "user": "was"
}
```

> It is clear from a very first look at the patch that this will massively conflict with #9343 (why 

I'm sure this will be easy to merge with #9343.  It's probably best to get 9343 in first, since it is much more difficult, then rebase the current patch against it.

> I would prefer to postpone:  hashing, printing

The current hashing and printing setup is complete and total crap, and needs to be removed ASAP.  It renders number fields completely useless for any nontrivial applications that involve prime ideals. 

> Also, I'm personally not completely convinced about the best way to print 

I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be). Print in reduced form only in small trivial cases (by default), but allow the user to easily up the cutoff if they want, for some reason.



---

archive/issue_comments_089533.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).\n\nWhy not hash based on the HNF representation, as I propsed in #9666?  I think this is more canonical than gens() and it is the native PARI format.",
    "created_at": "2010-08-12T17:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89533",
    "user": "jdemeyer"
}
```

Replying to [comment:6 was]:
> I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).

Why not hash based on the HNF representation, as I propsed in #9666?  I think this is more canonical than gens() and it is the native PARI format.



---

archive/issue_comments_089534.json:
```json
{
    "body": "Replying to [comment:7 jdemeyer]:\n> Replying to [comment:6 was]:\n> > I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).\n> \n> Why not hash based on the HNF representation, as I propsed in #9666?  \n> I think this is more canonical than gens() and it is the native PARI format.\n\nCONS:\nI think number fields will frequently be relative extensions, and we'll also consider ideals both in the maximal order and in suborders.  Pari will likely have almost nothing to do with our general relative extensions (it's only currently used for relative extensions as a miserable crutch), and HNF doesn't apply for ideals in orders.\n\nPROS:\nWhen it works, hashing based on the HNF has the property that if I==J then hash(I) == hash(J).  That's a very good property to have.   With hashing of gens that fails. \n\nThus taken together, I'm OK with your proposal with the caveat that at some future time it has to be revisited for *relative* extensions.",
    "created_at": "2010-08-14T00:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89534",
    "user": "was"
}
```

Replying to [comment:7 jdemeyer]:
> Replying to [comment:6 was]:
> > I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).
> 
> Why not hash based on the HNF representation, as I propsed in #9666?  
> I think this is more canonical than gens() and it is the native PARI format.

CONS:
I think number fields will frequently be relative extensions, and we'll also consider ideals both in the maximal order and in suborders.  Pari will likely have almost nothing to do with our general relative extensions (it's only currently used for relative extensions as a miserable crutch), and HNF doesn't apply for ideals in orders.

PROS:
When it works, hashing based on the HNF has the property that if I==J then hash(I) == hash(J).  That's a very good property to have.   With hashing of gens that fails. 

Thus taken together, I'm OK with your proposal with the caveat that at some future time it has to be revisited for *relative* extensions.



---

archive/issue_comments_089535.json:
```json
{
    "body": "apply only this patch (which also addresses the referees issue with __hash__)",
    "created_at": "2010-08-14T00:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89535",
    "user": "was"
}
```

apply only this patch (which also addresses the referees issue with __hash__)



---

archive/issue_comments_089536.json:
```json
{
    "body": "Attachment\n\nOK, new patch up that changes __hash__.  It passes all doctests on sage.math.",
    "created_at": "2010-08-14T00:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89536",
    "user": "was"
}
```

Attachment

OK, new patch up that changes __hash__.  It passes all doctests on sage.math.



---

archive/issue_comments_089537.json:
```json
{
    "body": "The patch introduces an inconsistency:\n\n\n```\nsage: K.<a> = NumberField(x^3-7)\nsage: K.ideal(12*a + 5).factor()\n(Fractional ideal (101, a - 8)) * (Fractional ideal (11, a + 5))^2\n```\n\n\n\n```\nsage: K.<b> = NumberField(x^3-10001)\nsage: L.ideal(b+1).factor()\n(Fractional ideal (b + 1, 1667)) * (Fractional ideal (b + 1, 2)) * (Fractional ideal (b + 1, 3))\n```\n\n\nNote how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?",
    "created_at": "2010-08-14T22:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89537",
    "user": "jdemeyer"
}
```

The patch introduces an inconsistency:


```
sage: K.<a> = NumberField(x^3-7)
sage: K.ideal(12*a + 5).factor()
(Fractional ideal (101, a - 8)) * (Fractional ideal (11, a + 5))^2
```



```
sage: K.<b> = NumberField(x^3-10001)
sage: L.ideal(b+1).factor()
(Fractional ideal (b + 1, 1667)) * (Fractional ideal (b + 1, 2)) * (Fractional ideal (b + 1, 3))
```


Note how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?



---

archive/issue_comments_089538.json:
```json
{
    "body": "> Note how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?\n\nWould that make any difference?  The difference above is that in one case the number field has a very small discriminant (-1323), and in the other it doesn't (-2700540027).   When the discriminant is small, then reduced generators are used for printing.   A solution could be to apply the sorting and \"uniquing\" in both cases before printing -- right now it is only applied in the case of large discriminant.",
    "created_at": "2010-08-15T17:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89538",
    "user": "was"
}
```

> Note how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?

Would that make any difference?  The difference above is that in one case the number field has a very small discriminant (-1323), and in the other it doesn't (-2700540027).   When the discriminant is small, then reduced generators are used for printing.   A solution could be to apply the sorting and "uniquing" in both cases before printing -- right now it is only applied in the case of large discriminant.



---

archive/issue_comments_089539.json:
```json
{
    "body": "Hi,\n\nI retract my comment.  The issue may be that sorting of elements of number fields is now useless.  Observe:\n\n```\nsage: L.<b> = NumberField(x^3-10001)\nsage: b+1 < L(1667)\nFalse\nsage: L(1667) < b + 1\nFalse\n```\n\nThus it doesn't matter *what* you do with sorting and uniquing the gens before or after -- there's no sensible ordering that will come out of this, unless elements of number fields get a total (non-algebraic) ordering.  I thought they had one. \n\nOh, now I remember -- there is a *major bug* in the way elements of number fields are ordered.  You can see this by looking at the code (I think Joel Mohler) wrote in number_field_element.pyx.  I fixed this a few weeks ago as part of the patch bomb #9541.   \n\nSo my advice is to not worry about sorting issues as part of *this* patch, but keep in mind that it is has to be fixed later.  I've opened ticket #9752 to fix this.",
    "created_at": "2010-08-15T17:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89539",
    "user": "was"
}
```

Hi,

I retract my comment.  The issue may be that sorting of elements of number fields is now useless.  Observe:

```
sage: L.<b> = NumberField(x^3-10001)
sage: b+1 < L(1667)
False
sage: L(1667) < b + 1
False
```

Thus it doesn't matter *what* you do with sorting and uniquing the gens before or after -- there's no sensible ordering that will come out of this, unless elements of number fields get a total (non-algebraic) ordering.  I thought they had one. 

Oh, now I remember -- there is a *major bug* in the way elements of number fields are ordered.  You can see this by looking at the code (I think Joel Mohler) wrote in number_field_element.pyx.  I fixed this a few weeks ago as part of the patch bomb #9541.   

So my advice is to not worry about sorting issues as part of *this* patch, but keep in mind that it is has to be fixed later.  I've opened ticket #9752 to fix this.



---

archive/issue_comments_089540.json:
```json
{
    "body": "Always using `gens()` for printing is also silly, because for larger degrees you can get something like:\n\n\n```\nsage: x=polygen(QQ); K.<a> = NumberField(x^8+x-1);\nsage: J1 = K.ideal(a+1); J2 = K.ideal(a+2); J = J1.intersection(J2)\nsage: J\nFractional ideal (a^2 + 249, -a^7 + 125, a + 2, a^3 + 8, a^4 + 237, -a^7 - a^6 + 189, a^7 + a^6 + a^5 + 96, 253)\n```\n\n\nIn my opinion, the best way would be to use `idealtwoelt()` for large discriminants instead of simply printing all generators (or alternatively: reduce the generators using `idealtwoelt()` in `__init__`).",
    "created_at": "2010-08-16T20:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89540",
    "user": "jdemeyer"
}
```

Always using `gens()` for printing is also silly, because for larger degrees you can get something like:


```
sage: x=polygen(QQ); K.<a> = NumberField(x^8+x-1);
sage: J1 = K.ideal(a+1); J2 = K.ideal(a+2); J = J1.intersection(J2)
sage: J
Fractional ideal (a^2 + 249, -a^7 + 125, a + 2, a^3 + 8, a^4 + 237, -a^7 - a^6 + 189, a^7 + a^6 + a^5 + 96, 253)
```


In my opinion, the best way would be to use `idealtwoelt()` for large discriminants instead of simply printing all generators (or alternatively: reduce the generators using `idealtwoelt()` in `__init__`).



---

archive/issue_comments_089541.json:
```json
{
    "body": "\n```\nOn Tue, Aug 17, 2010 at 5:03 PM, Chan-Ho Kim <chanho.math> wrote:\n> Dear William,\n> I think that there is a bug on trac 9400 patch.\n> My current SAGE is (SAGE 4.5.2 + trac 9400 patch only) in VM.\n> When I use `maximize_at_prime,'\n>\n> K.<a> = NumberField(x^6 + 9*x^5 - 8410*x^4 - 88580*x^3 + 18705368*x^2 +\n> 99820416*x - 12230355456, maximize_at_primes=[3]) ; K.primes_above(3)\n> this decomposition in K works as you mentioned.\n>\n> However, in this ``small'' number field\n>\n> F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[3]) ;\n> F.primes_above(3)\n> the low precision error occurs if I add `maximize_at_primes=[3].'\n\nThat's not a bug in maximize_at_primes or finding the primes above 3.   But it *is* an issue with *printing* the ideals out that it finds over 3.   Evidently, when printing is_principal is called on each ideal currently, and this leads to a problem.  This is not surprising, given that deciding whether or not an ideal is principal requires knowing the class group in general, and the equation order of F that you define above is not only deficient at 3.  You need to also maximize at 2.   See:\n\nsage: F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[2,3]) \nsage: F.primes_above(3)\n[Fractional ideal (-1/2*a^2 - 3/2*a + 5), Fractional ideal (-1/2*a^2 + 5/2*a - 1)]\n\nSo in short, this is not a bug.  If you try to compute with number fields and pass in the maximize_at_primes option, certain things can't possibly work.\n\nThat said, I'm not a big fan of how ideals print.  Maybe Jereon's suggestion -- just *always* print with the PARI 2-element representation -- is the way to go.  That might get around this problem. \n\n\n> BTW, I also have one more question:\n> Can I add `maximize_at_prime=[p]' in `hecke_eigenvalue_field()'?\n\nYou'll have to dive in and start hacking at the source code of Sage to do that....\n\n -- William\n```\n",
    "created_at": "2010-08-18T00:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89541",
    "user": "was"
}
```


```
On Tue, Aug 17, 2010 at 5:03 PM, Chan-Ho Kim <chanho.math> wrote:
> Dear William,
> I think that there is a bug on trac 9400 patch.
> My current SAGE is (SAGE 4.5.2 + trac 9400 patch only) in VM.
> When I use `maximize_at_prime,'
>
> K.<a> = NumberField(x^6 + 9*x^5 - 8410*x^4 - 88580*x^3 + 18705368*x^2 +
> 99820416*x - 12230355456, maximize_at_primes=[3]) ; K.primes_above(3)
> this decomposition in K works as you mentioned.
>
> However, in this ``small'' number field
>
> F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[3]) ;
> F.primes_above(3)
> the low precision error occurs if I add `maximize_at_primes=[3].'

That's not a bug in maximize_at_primes or finding the primes above 3.   But it *is* an issue with *printing* the ideals out that it finds over 3.   Evidently, when printing is_principal is called on each ideal currently, and this leads to a problem.  This is not surprising, given that deciding whether or not an ideal is principal requires knowing the class group in general, and the equation order of F that you define above is not only deficient at 3.  You need to also maximize at 2.   See:

sage: F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[2,3]) 
sage: F.primes_above(3)
[Fractional ideal (-1/2*a^2 - 3/2*a + 5), Fractional ideal (-1/2*a^2 + 5/2*a - 1)]

So in short, this is not a bug.  If you try to compute with number fields and pass in the maximize_at_primes option, certain things can't possibly work.

That said, I'm not a big fan of how ideals print.  Maybe Jereon's suggestion -- just *always* print with the PARI 2-element representation -- is the way to go.  That might get around this problem. 


> BTW, I also have one more question:
> Can I add `maximize_at_prime=[p]' in `hecke_eigenvalue_field()'?

You'll have to dive in and start hacking at the source code of Sage to do that....

 -- William
```




---

archive/issue_comments_089542.json:
```json
{
    "body": "I am not familiar with `_pari_` and `_pari_init_`, but why does NumberField need `_pari_init_`?  Can't we add instead a `_pari_` method which returns `pari_nf()`?",
    "created_at": "2010-08-18T21:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89542",
    "user": "jdemeyer"
}
```

I am not familiar with `_pari_` and `_pari_init_`, but why does NumberField need `_pari_init_`?  Can't we add instead a `_pari_` method which returns `pari_nf()`?



---

archive/issue_comments_089543.json:
```json
{
    "body": "Rebasing to #9343 will be easier if we seperate the \"maximize_at_primes part\" from the \"printing and hashing of ideals\" part.  So I will cut this patch in two pieces.",
    "created_at": "2010-08-18T21:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89543",
    "user": "jdemeyer"
}
```

Rebasing to #9343 will be easier if we seperate the "maximize_at_primes part" from the "printing and hashing of ideals" part.  So I will cut this patch in two pieces.



---

archive/issue_comments_089544.json:
```json
{
    "body": "Patch for the \"maximize at primes\" part, rebased to sage-4.6.prealpha1 (see #9343)",
    "created_at": "2010-08-18T22:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89544",
    "user": "jdemeyer"
}
```

Patch for the "maximize at primes" part, rebased to sage-4.6.prealpha1 (see #9343)



---

archive/issue_comments_089545.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-18T22:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89545",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_089546.json:
```json
{
    "body": "I attached a big reviewer patch (to be applied on top of 9400_maximize_at_primes.patch) changing:\n* the PARI functions `nfbasis()` and `nfinit()`: document and fix implementation.\n* change `pari_nf()` to always use `integral_basis()` (this means that all the `maximize_at_primes` code can be moved out of `pari_nf()`).\n* rename `_compute_integral_basis` to `_pari_integral_basis` and don't convert from PARI to Sage.\n* make the code for CyclotomicField more analogous to NumberField_generic (such that only `_pari_integral_basis` needs to be specialized, not `integral_basis()`.\n\nSince the purpose of `_pari_init_()` is very unclear to me, I'm not sure what to do with that.",
    "created_at": "2010-08-20T15:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89546",
    "user": "jdemeyer"
}
```

I attached a big reviewer patch (to be applied on top of 9400_maximize_at_primes.patch) changing:
* the PARI functions `nfbasis()` and `nfinit()`: document and fix implementation.
* change `pari_nf()` to always use `integral_basis()` (this means that all the `maximize_at_primes` code can be moved out of `pari_nf()`).
* rename `_compute_integral_basis` to `_pari_integral_basis` and don't convert from PARI to Sage.
* make the code for CyclotomicField more analogous to NumberField_generic (such that only `_pari_integral_basis` needs to be specialized, not `integral_basis()`.

Since the purpose of `_pari_init_()` is very unclear to me, I'm not sure what to do with that.



---

archive/issue_comments_089547.json:
```json
{
    "body": "Apply on top of 9400_maximize_at_primes.patc",
    "created_at": "2010-08-21T10:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89547",
    "user": "jdemeyer"
}
```

Apply on top of 9400_maximize_at_primes.patc



---

archive/issue_comments_089548.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-24T19:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89548",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_089549.json:
```json
{
    "body": "Changing assignee from davidloeffler to jdemeyer.",
    "created_at": "2010-08-24T19:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89549",
    "user": "jdemeyer"
}
```

Changing assignee from davidloeffler to jdemeyer.



---

archive/issue_comments_089550.json:
```json
{
    "body": "Changing keywords from \"\" to \"PARI number field\".",
    "created_at": "2010-08-24T19:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89550",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "PARI number field".



---

archive/issue_comments_089551.json:
```json
{
    "body": "Since this ismarked \"needs review\" could the authors clarify which patches are up for review?  I assume it is \n\n```\n9400_maximize_at_primes.patch \nPatch for the \"maximize at primes\" part, rebased to sage-4.6.prealpha1 (see #9343)\n```\n\nand\n\n```\n9400_jd_review.patch \nApply on top of 9400_maximize_at_primes.patch\n```\n\nand not the first one.\n\nSecondly, since these patches have been merged into 4.6.prealpha3 which I have successfully built and tested, I reckon that the only (!) remaining task as a reviewer is to look at the code in the patch, with the additional explanations on the ticket, and approve (or otherwise, maybe) of it?\n\nI will try to do this before I go away on Friday for a week.  No promises...",
    "created_at": "2010-08-30T16:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89551",
    "user": "cremona"
}
```

Since this ismarked "needs review" could the authors clarify which patches are up for review?  I assume it is 

```
9400_maximize_at_primes.patch 
Patch for the "maximize at primes" part, rebased to sage-4.6.prealpha1 (see #9343)
```

and

```
9400_jd_review.patch 
Apply on top of 9400_maximize_at_primes.patch
```

and not the first one.

Secondly, since these patches have been merged into 4.6.prealpha3 which I have successfully built and tested, I reckon that the only (!) remaining task as a reviewer is to look at the code in the patch, with the additional explanations on the ticket, and approve (or otherwise, maybe) of it?

I will try to do this before I go away on Friday for a week.  No promises...



---

archive/issue_comments_089552.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-30T16:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89552",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089553.json:
```json
{
    "body": "Looking at the 2nd and 3rd patches (separately) it looks very good to me.  For the benefit of others reading this, the essence of these patches (apart from some ReSTification) is to expose some additional functionality from the pari library to Sage, so that some computations can be mande very much faster (a *lot* faster!).\n\nI spotted a few minor issues in docstrings (numbers refer to the ones I see in the third patch):\n\n\n6451: second 'it' --> 'the'\n\n6466: should have a preceding #, or replace \":\" by \"::\" and insert a blank line after and change the preceding \"TESTS::\" to \"TESTS:\"\n\n6592: change \"TESTS::\" to \"TESTS:\"\n\nand also when I rebuilt the docs after \"sage -ba\"  (using 4.6.prealpha3) I got these ReST warnings:\n\n\n```\ndocstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.\n```\n\n\n```\ndocstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n```\n\n\n```\ndocstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.\n```\n\n\nModulo these, a positive review is on offer.  Hence \"needs work\", but it is only trivial work.",
    "created_at": "2010-08-30T16:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89553",
    "user": "cremona"
}
```

Looking at the 2nd and 3rd patches (separately) it looks very good to me.  For the benefit of others reading this, the essence of these patches (apart from some ReSTification) is to expose some additional functionality from the pari library to Sage, so that some computations can be mande very much faster (a *lot* faster!).

I spotted a few minor issues in docstrings (numbers refer to the ones I see in the third patch):


6451: second 'it' --> 'the'

6466: should have a preceding #, or replace ":" by "::" and insert a blank line after and change the preceding "TESTS::" to "TESTS:"

6592: change "TESTS::" to "TESTS:"

and also when I rebuilt the docs after "sage -ba"  (using 4.6.prealpha3) I got these ReST warnings:


```
docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
```


```
docstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```


```
docstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.
```


Modulo these, a positive review is on offer.  Hence "needs work", but it is only trivial work.



---

archive/issue_comments_089554.json:
```json
{
    "body": "Thanks John, I will take care of these issues when I have time.",
    "created_at": "2010-08-30T21:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89554",
    "user": "jdemeyer"
}
```

Thanks John, I will take care of these issues when I have time.



---

archive/issue_comments_089555.json:
```json
{
    "body": "Attachment\n\nApply on top of previous 2 patches, small documentation fixes",
    "created_at": "2010-09-05T12:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89555",
    "user": "jdemeyer"
}
```

Attachment

Apply on top of previous 2 patches, small documentation fixes



---

archive/issue_comments_089556.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-05T13:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89556",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089557.json:
```json
{
    "body": "Attachment\n\nAll 3 patches combined (apply only this patch)",
    "created_at": "2010-09-05T16:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89557",
    "user": "jdemeyer"
}
```

Attachment

All 3 patches combined (apply only this patch)



---

archive/issue_comments_089558.json:
```json
{
    "body": "I did all the changes requested by the reviewer.\n\nReplying to [comment:22 cremona]:\n> {{{\n> docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.\n> }}}\nThis belongs to #9636 and is fixed there.  The other warnings are fixed here.",
    "created_at": "2010-09-05T18:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89558",
    "user": "jdemeyer"
}
```

I did all the changes requested by the reviewer.

Replying to [comment:22 cremona]:
> {{{
> docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
> }}}
This belongs to #9636 and is fixed there.  The other warnings are fixed here.



---

archive/issue_comments_089559.json:
```json
{
    "body": "Hi,\n\nI tried to apply my patch to 4.5.2.rc0 and it works fine:\n\n\n```\nadding trac_9400.patch to series file\napplying trac_9400.patch\nnow at: trac_9400.patch\n```\n\n\nI tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:\n\n```\nadding 9400_combined.patch to series file\napplying 9400_combined.patch\npatching file sage/libs/pari/gen.pyx\nHunk #1 succeeded at 6408 with fuzz 2 (offset -32 lines).\nHunk #4 FAILED at 6964\nHunk #5 FAILED at 6991\n2 out of 7 hunks FAILED -- saving rejects to file sage/libs/pari/gen.pyx.rej\npatching file sage/rings/number_field/number_field.py\nHunk #13 FAILED at 2870\nHunk #16 FAILED at 3727\n2 out of 25 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field.py.rej\npatching file sage/rings/number_field/number_field_ideal_rel.py\nHunk #2 FAILED at 592\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field_ideal_rel.py.rej\npatching file sage/rings/polynomial/polynomial_quotient_ring.py\nHunk #1 FAILED at 688\nHunk #2 FAILED at 1068\n2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_quotient_ring.py.rej\npatching file sage/rings/residue_field.pyx\nHunk #17 succeeded at 427 with fuzz 2 (offset 0 lines).\nHunk #18 succeeded at 444 with fuzz 2 (offset 0 lines).\nHunk #19 FAILED at 463\nHunk #26 succeeded at 572 with fuzz 1 (offset -1 lines).\nHunk #27 FAILED at 589\n2 out of 48 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 9400_combined.patch\n```\n",
    "created_at": "2010-09-07T16:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89559",
    "user": "was"
}
```

Hi,

I tried to apply my patch to 4.5.2.rc0 and it works fine:


```
adding trac_9400.patch to series file
applying trac_9400.patch
now at: trac_9400.patch
```


I tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:

```
adding 9400_combined.patch to series file
applying 9400_combined.patch
patching file sage/libs/pari/gen.pyx
Hunk #1 succeeded at 6408 with fuzz 2 (offset -32 lines).
Hunk #4 FAILED at 6964
Hunk #5 FAILED at 6991
2 out of 7 hunks FAILED -- saving rejects to file sage/libs/pari/gen.pyx.rej
patching file sage/rings/number_field/number_field.py
Hunk #13 FAILED at 2870
Hunk #16 FAILED at 3727
2 out of 25 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field.py.rej
patching file sage/rings/number_field/number_field_ideal_rel.py
Hunk #2 FAILED at 592
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field_ideal_rel.py.rej
patching file sage/rings/polynomial/polynomial_quotient_ring.py
Hunk #1 FAILED at 688
Hunk #2 FAILED at 1068
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_quotient_ring.py.rej
patching file sage/rings/residue_field.pyx
Hunk #17 succeeded at 427 with fuzz 2 (offset 0 lines).
Hunk #18 succeeded at 444 with fuzz 2 (offset 0 lines).
Hunk #19 FAILED at 463
Hunk #26 succeeded at 572 with fuzz 1 (offset -1 lines).
Hunk #27 FAILED at 589
2 out of 48 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9400_combined.patch
```




---

archive/issue_comments_089560.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-07T16:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89560",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089561.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-07T16:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89561",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089562.json:
```json
{
    "body": "Replying to [comment:28 was]:\n> I tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:\n\nIt is meant to be applied after #9343, then it works fine.",
    "created_at": "2010-09-07T16:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89562",
    "user": "jdemeyer"
}
```

Replying to [comment:28 was]:
> I tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:

It is meant to be applied after #9343, then it works fine.



---

archive/issue_comments_089563.json:
```json
{
    "body": "John, do Jeroen's most recent changes look good to you?",
    "created_at": "2010-09-09T11:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89563",
    "user": "mpatel"
}
```

John, do Jeroen's most recent changes look good to you?



---

archive/issue_comments_089564.json:
```json
{
    "body": "Replying to [comment:30 mpatel]:\n> John, do Jeroen's most recent changes look good to you?\n\nSorry for delay -- Jeroen has nudged me on this and I'll look at it as soon as I can, but I'm at a conference this week...",
    "created_at": "2010-09-09T14:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89564",
    "user": "cremona"
}
```

Replying to [comment:30 mpatel]:
> John, do Jeroen's most recent changes look good to you?

Sorry for delay -- Jeroen has nudged me on this and I'll look at it as soon as I can, but I'm at a conference this week...



---

archive/issue_comments_089565.json:
```json
{
    "body": "Replying to [comment:30 mpatel]:\n> John, do Jeroen's most recent changes look good to you?\n\nThe new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.",
    "created_at": "2010-09-11T16:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89565",
    "user": "cremona"
}
```

Replying to [comment:30 mpatel]:
> John, do Jeroen's most recent changes look good to you?

The new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.



---

archive/issue_comments_089566.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T16:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89566",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089567.json:
```json
{
    "body": "Replying to [comment:32 cremona]:\n> Replying to [comment:30 mpatel]:\n> > John, do Jeroen's most recent changes look good to you?\n> \n> The new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.\n\nAll (long) tests pass -- positive review.",
    "created_at": "2010-09-11T16:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89567",
    "user": "cremona"
}
```

Replying to [comment:32 cremona]:
> Replying to [comment:30 mpatel]:
> > John, do Jeroen's most recent changes look good to you?
> 
> The new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.

All (long) tests pass -- positive review.



---

archive/issue_comments_089568.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89568",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_089569.json:
```json
{
    "body": "Replying to [comment:34 mpatel]:\n\nNote that I mentioned  in this ticket (and on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff993da70fc9f7ac)) that I do not understand `_pari_init_()`. I don't know if the reviewers do, so I'm a little bit worried about this.",
    "created_at": "2010-09-19T10:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9400#issuecomment-89569",
    "user": "jdemeyer"
}
```

Replying to [comment:34 mpatel]:

Note that I mentioned  in this ticket (and on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff993da70fc9f7ac)) that I do not understand `_pari_init_()`. I don't know if the reviewers do, so I'm a little bit worried about this.
