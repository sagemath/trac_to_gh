# Issue 536: off by one in NZL::vec_ZZ::SetLength(long) (from modular/dirichlet.py)

archive/issues_000536.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom Sage 2.8.3rc3:\n\n```\n==25034==  Address 0x24DB2020 is 8 bytes before a block of size 64 alloc'd\n==25034==    by 0x97D3C09: NTL::vec_ZZ::SetLength(long) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libntl.so)\n==25034==    by 0x972D78F: NTL::PlainPseudoDivRem(NTL::ZZX&, NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sag\ne-2.8.3.rc3/local/lib/libntl.so)\n==25034==    by 0x972D9E6: NTL::PlainPseudoRem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/lo\ncal/lib/libntl.so)\n==25034==    by 0x9732BA2: NTL::rem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/lib\nntl.so)\n==25034==    by 0x9732E1C: NTL::MulMod(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8\n.3.rc3/local/lib/libntl.so)\n==25034==    by 0x1B790919: __pyx_f_20number_field_element_18NumberFieldElement__mul_c_impl(__pyx_obj_20number_field_element\n_NumberFieldElement*, __pyx_obj_4sage_9structure_7element_RingElement*) (number_field_element.cpp:4198)\n==25034==    by 0xE3C999D: __pyx_f_7element_11RingElement__mul_c (element.c:8340)\n==25034==    by 0xE3BD3E4: __pyx_f_7element_11RingElement___mul__ (element.c:7922)\n==25034==    by 0x41596C: binary_op1 (abstract.c:398)\n==25034==    by 0x418EC3: PyNumber_InPlaceMultiply (abstract.c:744)\n==25034==    by 0x481053: PyEval_EvalFrameEx (ceval.c:1274)\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/536\n\n",
    "created_at": "2007-08-30T18:54:24Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "off by one in NZL::vec_ZZ::SetLength(long) (from modular/dirichlet.py)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

From Sage 2.8.3rc3:

```
==25034==  Address 0x24DB2020 is 8 bytes before a block of size 64 alloc'd
==25034==    by 0x97D3C09: NTL::vec_ZZ::SetLength(long) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x972D78F: NTL::PlainPseudoDivRem(NTL::ZZX&, NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sag
e-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x972D9E6: NTL::PlainPseudoRem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/lo
cal/lib/libntl.so)
==25034==    by 0x9732BA2: NTL::rem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/lib
ntl.so)
==25034==    by 0x9732E1C: NTL::MulMod(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8
.3.rc3/local/lib/libntl.so)
==25034==    by 0x1B790919: __pyx_f_20number_field_element_18NumberFieldElement__mul_c_impl(__pyx_obj_20number_field_element
_NumberFieldElement*, __pyx_obj_4sage_9structure_7element_RingElement*) (number_field_element.cpp:4198)
==25034==    by 0xE3C999D: __pyx_f_7element_11RingElement__mul_c (element.c:8340)
==25034==    by 0xE3BD3E4: __pyx_f_7element_11RingElement___mul__ (element.c:7922)
==25034==    by 0x41596C: binary_op1 (abstract.c:398)
==25034==    by 0x418EC3: PyNumber_InPlaceMultiply (abstract.c:744)
==25034==    by 0x481053: PyEval_EvalFrameEx (ceval.c:1274)
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/536





---

archive/issue_comments_002719.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-30T18:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/536#issuecomment-2719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_001399.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-01T22:47:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1399"
}
```



---

archive/issue_events_001400.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:47:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1400"
}
```



---

archive/issue_events_001401.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:47:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1401"
}
```



---

archive/issue_events_001402.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:19:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1402"
}
```



---

archive/issue_events_001403.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:19:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1403"
}
```



---

archive/issue_events_001404.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:21:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1404"
}
```



---

archive/issue_events_001405.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:21:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1405"
}
```



---

archive/issue_comments_002720.json:
```json
{
    "body": "I'm closing this as wontfix -- we don't know which doctest caused this, and it's old enough that the guilty code could well be gone anyway (for instance, all the arithmetic code was reworked with the coercion switch). Plus, this might actually be an issue in NTL. I'd be happy to look at this again if we had a way to reproduce it, but as it stands, it's not worth trying to hunt this down. (I guess I could rebuild 2.8.3, but that seems excessive ...)",
    "created_at": "2010-01-17T22:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/536#issuecomment-2720",
    "user": "https://github.com/craigcitro"
}
```

I'm closing this as wontfix -- we don't know which doctest caused this, and it's old enough that the guilty code could well be gone anyway (for instance, all the arithmetic code was reworked with the coercion switch). Plus, this might actually be an issue in NTL. I'd be happy to look at this again if we had a way to reproduce it, but as it stands, it's not worth trying to hunt this down. (I guess I could rebuild 2.8.3, but that seems excessive ...)



---

archive/issue_events_001406.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2010-01-17T22:48:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1406"
}
```



---

archive/issue_comments_002721.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-17T22:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/536#issuecomment-2721",
    "user": "https://github.com/craigcitro"
}
```

Resolution: wontfix



---

archive/issue_events_001407.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-18T02:04:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1407"
}
```



---

archive/issue_events_001408.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-18T02:04:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/536",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/536#event-1408"
}
```
