# Issue 4401: Sage 3.1.4: magma related optional doctest failure in sage/crypto/mq/mpolynomialsystem.py

Issue created by migration from https://trac.sagemath.org/ticket/4401

Original creator: mabshoff

Original creation time: 2008-10-30 17:33:04

Assignee: was


```
sage -t -long -optional devel/sage/sage/crypto/mq/mpolynomialsystem.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/mpolynomialsystem.py", line 851:
    sage: F._magma_() # optional, requires MAGMA
Expected nothing
Got:
    Ideal of Polynomial ring of rank 20 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003, k000, k001, k002, k003
    Basis:
    [
    w100 + k000 + 1,
    w101 + k001,
    w102 + k002 + 1,
    w103 + k003 + 1,
    k000^2 + k000,
    k001^2 + k001,
    k002^2 + k002,
    k003^2 + k003,
    k100 + x100 + x102 + x103 + 1,
    k101 + x100 + x101 + x103,
    k102 + x100 + x101 + x102 + 1,
    k103 + x101 + x102 + x103,
    x100*w100 + x103*w100 + x102*w101 + x101*w102 + x100*w103,
    x100*w100 + x101*w100 + x100*w101 + x103*w101 + x102*w102 + x101*w103,
    x101*w100 + x102*w100 + x100*w101 + x101*w101 + x100*w102 + x103*w102 + x102*w103,
    x102*w100 + x101*w101 + x100*w102 + x103*w103 + 1,
    x100*w100 + x101*w100 + x103*w100 + x101*w101 + x100*w102 + x102*w102 + x100*w103 + x100,
    x102*w100 + x100*w101 + x101*w101 + x103*w101 + x101*w102 + x100*w103 + x102*w103 + x101,
    x100*w100 + x101*w100 + x102*w100 + x102*w101 + x100*w102 + x101*w102 + x103*w102 + x101*w103 + x102,
    x101*w100 + x100*w101 + x102*w101 + x100*w102 + x101*w103 + x103*w103 + x103,
    x100*w100 + x102*w100 + x103*w100 + x100*w101 + x101*w101 + x102*w102 + x100*w103 + w100,
    x101*w100 + x103*w100 + x101*w101 + x102*w101 + x100*w102 + x103*w102 + x101*w103 + w101,
    x100*w100 + x102*w100 + x100*w101 + x102*w101 + x103*w101 + x100*w102 + x101*w102 + x102*w103 + w102,
    x101*w100 + x102*w100 + x100*w101 + x103*w101 + x101*w102 + x103*w103 + w103,
    x100^2 + x100,
    x101^2 + x101,
    x102^2 + x102,
    x103^2 + x103,
    w100^2 + w100,
    w101^2 + w101,
    w102^2 + w102,
    w103^2 + w103,
    k100 + s000 + s002 + s003,
    k101 + s000 + s001 + s003 + 1,
    k102 + s000 + s001 + s002 + 1,
    k103 + s001 + s002 + s003 + 1,
    k100^2 + k100,
    k101^2 + k101,
    k102^2 + k102,
    k103^2 + k103,
    s000^2 + s000,
    s001^2 + s001,
    s002^2 + s002,
    s003^2 + s003,
    s000*k000 + s003*k000 + s002*k001 + s001*k002 + s000*k003,
    s000*k000 + s001*k000 + s000*k001 + s003*k001 + s002*k002 + s001*k003,
    s001*k000 + s002*k000 + s000*k001 + s001*k001 + s000*k002 + s003*k002 + s002*k003,
    s002*k000 + s001*k001 + s000*k002 + s003*k003 + 1,
    s000*k000 + s002*k000 + s003*k000 + s000*k001 + s001*k001 + s002*k002 + s000*k003 + k000,
    s001*k000 + s003*k000 + s001*k001 + s002*k001 + s000*k002 + s003*k002 + s001*k003 + k001,
    s000*k000 + s002*k000 + s000*k001 + s002*k001 + s003*k001 + s000*k002 + s001*k002 + s002*k003 + k002,
    s001*k000 + s002*k000 + s000*k001 + s003*k001 + s001*k002 + s003*k003 + k003,
    s000*k000 + s001*k000 + s003*k000 + s001*k001 + s000*k002 + s002*k002 + s000*k003 + s000,
    s002*k000 + s000*k001 + s001*k001 + s003*k001 + s001*k002 + s000*k003 + s002*k003 + s001,
    s000*k000 + s001*k000 + s002*k000 + s002*k001 + s000*k002 + s001*k002 + s003*k002 + s001*k003 + s002,
    s001*k000 + s000*k001 + s002*k001 + s000*k002 + s001*k003 + s003*k003 + s003
    ]
**********************************************************************
```



---

Comment by mabshoff created at 2008-11-24 22:54:06

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 22:54:06

Resolution: fixed
