# Issue 6139: [with patch, needs review] Fix S-Box calling when m != n

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-05-27 12:20:18

Assignee: malb

CC:  mvngu

Keywords: crypto, mq, sbox

This should work:


```
sage: S = mq.SBox(3, 0, 1, 3, 1, 0, 2, 2)
sage: S(0)
3
sage: S([0,0,0])
[1, 1]
```


reported by Sajan.S on [sage-support] (27.5.09)


---

Attachment

Hi Minh, can I ask you to review this?


---

Comment by mvngu created at 2009-06-03 21:17:10

REFEREE REPORT



Patch applies OK against sage-4.0.1.alpha0, all tests pass even with `-long` option. Most of the patch deals with Sphinxifying the module `sage/crypto/mq/sbox.py`. But the main issue is to fix the bug reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/91ec1975d7bfc565/d6113194a8a6cc3f) thread. And the patch does exactly as claimed. Positive review. I've attached a reviewer patch that fixes some trivial formatting typos.


---

Attachment


---

Comment by malb created at 2009-06-03 22:10:55

The referee patch is fine too.


---

Comment by mhansen created at 2009-06-04 18:22:37

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 18:22:37

Merged both patches in 4.0.1.rc1.
