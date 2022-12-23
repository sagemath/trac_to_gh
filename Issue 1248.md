# Issue 1248: mwrank wrapper defect

Issue created by migration from https://trac.sagemath.org/ticket/1248

Original creator: zimmerma

Original creation time: 2007-11-23 16:32:03

Assignee: was

The mwrank wrapper crashes for curves requiring a large precision:

```
sage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])
sage: F.gens()
...
Mwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
```

The workaround is to enlarge the precision, but this does not seem to work:

```
sage: mwrank_set_precision(40)
sage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])
sage: F.gens()
...
Mwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
```

In comparison, the mwrank console works:

```
pasta% sage -mwrank -p40
...
Enter curve: [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
...
Rank = 2
...
Generator 1 is [-64279912864146869343830:9890032513326436827332346415:5023053676376]; height 19.3576595783878252695113978299426894052
Generator 2 is [15973785170:1448063200169915:1]; height 4.540177201347877276441819514533365581727
```

This proves that the defect is in the mwrank wrapper, not in mwrank itself.



---

Comment by mabshoff created at 2007-12-05 19:01:37

John Cremona wrote:

```
This was Paul Z's observation and seems to be a wrapper problem, so
"anyone" could try to track that down.
]]]

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:00:38

Since William is rewriting the mwrank wrapper he might take care of this. The crash does happen with Sage 2.10.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 21:23:50

Hmmm, since William told be that the mwrank wrapper rewrite is practically done it would be nice to get this into Sage and hopefully resolve this issue, too.

Cheers,

Michael


---

Comment by cwitty created at 2008-08-23 19:14:38

Resolution: fixed


---

Comment by cwitty created at 2008-08-23 19:14:38

This works for me in Sage 3.1.1 on 32-bit and 64-bit x86; maybe the "mwrank wrapper rewrite" referred to above did fix the problem?
