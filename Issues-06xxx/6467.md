# Issue 6467: [with patch, needs work] all primitive roots modulo n

archive/issues_006467.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nKeywords: primitive roots, generators mod n\n\nFor a fixed positive integer n, compute a list of all the primitive roots modulo n. Sage currently can compute one primitive root modulo n, but not all of them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6467\n\n",
    "created_at": "2009-07-05T18:11:29Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs work] all primitive roots modulo n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @williamstein

CC:  @kcrisman

Keywords: primitive roots, generators mod n

For a fixed positive integer n, compute a list of all the primitive roots modulo n. Sage currently can compute one primitive root modulo n, but not all of them.

Issue created by migration from https://trac.sagemath.org/ticket/6467





---

archive/issue_events_015257.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-05T18:24:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15257"
}
```



---

archive/issue_comments_052187.json:
```json
{
    "body": "The patch `trac_6467.patch` adds two functions to `sage/rings/arith.py` for calculating all the primitive roots modulo a fixed integer n:\n1. `primitive_roots()` --- Return all the generators for the multiplicative group of integers modulo a positive integer n. Where n is a positive composite integer, the function uses a naive method that is inefficient, since I do not know of a better method. If n is a positive prime integer, then use the function `primitive_roots_prime()`.\n2. `primitive_roots_prime()` --- Return all the generators for the multiplicative group of integers modulo a positive prime p. Again, this uses an inefficient method since I'm not aware of a better way.",
    "created_at": "2009-07-05T18:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6467#issuecomment-52187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6467.patch` adds two functions to `sage/rings/arith.py` for calculating all the primitive roots modulo a fixed integer n:
1. `primitive_roots()` --- Return all the generators for the multiplicative group of integers modulo a positive integer n. Where n is a positive composite integer, the function uses a naive method that is inefficient, since I do not know of a better method. If n is a positive prime integer, then use the function `primitive_roots_prime()`.
2. `primitive_roots_prime()` --- Return all the generators for the multiplicative group of integers modulo a positive prime p. Again, this uses an inefficient method since I'm not aware of a better way.



---

archive/issue_comments_052188.json:
```json
{
    "body": "based on Sage 4.1.rc0",
    "created_at": "2009-07-05T18:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6467#issuecomment-52188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.rc0



---

archive/issue_comments_052189.json:
```json
{
    "body": "Attachment [trac_6467.patch](tarball://root/attachments/some-uuid/ticket6467/trac_6467.patch) by @loefflerd created at 2009-07-14 10:42:33\n\nI'm not totally convinced by this. \n\n- The function `primitive_roots_prime` shouldn't be exported to the global namespace. At present *everything* in sage/rings/arith is exported, which (to me) suggests moving the innards of this function to methods of the IntegerModRing class.\n\n- There is already a method `IntegerRing_class.multiplicative_group_is_cyclic()` which you can use to find out if a primitive root exists -- I fixed a bug in it not long back. Asking for a primitive root and then catching the exception if one isn't found is a bit ugly, besides being much slower.\n\n- For a prime modulus p, you take a primitive root g, then compute g<sup>k</sup> for each k in 1...phi(p). It would be more efficient to have a variable that is initialised to 1 and then multiplied by g (mod p) each time, avoiding the separate power_mod call. \n\n- The algorithm in the composite case can be *massively* improved using two simple observations: (1) there are no primitive roots mod n unless n is < 8, an odd prime power, or twice an odd prime power; and (2) if n is an odd prime power then g is a primitive root mod p<sup>k</sup> if and only if it's a primitive root mod p (and g is a primitive root mod 2 * p<sup>k</sup> iff g is a primitive root mod p and g is odd).\n\n(At a rough guess your current algorithm is running in time about N^{3/2} times a power of log; this observation will speed it up to N * power of log.)\n\nDavid",
    "created_at": "2009-07-14T10:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6467#issuecomment-52189",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6467.patch](tarball://root/attachments/some-uuid/ticket6467/trac_6467.patch) by @loefflerd created at 2009-07-14 10:42:33

I'm not totally convinced by this. 

- The function `primitive_roots_prime` shouldn't be exported to the global namespace. At present *everything* in sage/rings/arith is exported, which (to me) suggests moving the innards of this function to methods of the IntegerModRing class.

- There is already a method `IntegerRing_class.multiplicative_group_is_cyclic()` which you can use to find out if a primitive root exists -- I fixed a bug in it not long back. Asking for a primitive root and then catching the exception if one isn't found is a bit ugly, besides being much slower.

- For a prime modulus p, you take a primitive root g, then compute g<sup>k</sup> for each k in 1...phi(p). It would be more efficient to have a variable that is initialised to 1 and then multiplied by g (mod p) each time, avoiding the separate power_mod call. 

- The algorithm in the composite case can be *massively* improved using two simple observations: (1) there are no primitive roots mod n unless n is < 8, an odd prime power, or twice an odd prime power; and (2) if n is an odd prime power then g is a primitive root mod p<sup>k</sup> if and only if it's a primitive root mod p (and g is a primitive root mod 2 * p<sup>k</sup> iff g is a primitive root mod p and g is odd).

(At a rough guess your current algorithm is running in time about N^{3/2} times a power of log; this observation will speed it up to N * power of log.)

David



---

archive/issue_comments_052190.json:
```json
{
    "body": "Oops, by `IntegerRing_class.multiplicative_group_is_cyclic()` I meant `IntegerModRing_generic.multiplicative_group_is_cyclic()`, in `sage.rings.integer_mod_ring`. Sorry.",
    "created_at": "2009-07-14T10:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6467#issuecomment-52190",
    "user": "https://github.com/loefflerd"
}
```

Oops, by `IntegerRing_class.multiplicative_group_is_cyclic()` I meant `IntegerModRing_generic.multiplicative_group_is_cyclic()`, in `sage.rings.integer_mod_ring`. Sorry.



---

archive/issue_events_015258.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15258"
}
```



---

archive/issue_events_015259.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15259"
}
```



---

archive/issue_events_015260.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15260"
}
```



---

archive/issue_events_015261.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15261"
}
```



---

archive/issue_events_015262.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15262"
}
```



---

archive/issue_events_015263.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15263"
}
```



---

archive/issue_events_015264.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15264"
}
```



---

archive/issue_events_015265.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6467",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6467#event-15265"
}
```
