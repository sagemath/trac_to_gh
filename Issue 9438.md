# Issue 9438: IntegerMod_int.log has side-effect in Pari

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-07-06 15:34:02

Assignee: AlexGhitza

Keywords: log finite field pari

Motivated by a bug hunt for #2420, I found:

```
sage: R.<a, b> = QQ[]
sage: b._pari_()
b
sage: GF(7)(5).log()
5
sage: b._pari_()
Mod(3, 7)
```


The reason is that in the `log` method, the string

```
'b=Mod(%s,%s); if(znorder(b)!=eulerphi(%s),-1,znlog(%s,b))'%(b, self.__modulus.sageInteger,
                                                                           self.__modulus.sageInteger, self)
```

is evaluated in `pari`, so that afterwards `pari('b')` isn't doing what it should.

Since this bug is triggered whenever a GAP representation of a finite field element is created, I mark this ticket "critical". I hope "basic arithmetic" is the right component.


---

Comment by SimonKing created at 2010-07-06 17:00:18

The patch seems to fix the bug. The string that is evaluated by PARI defines a variable 'b' and uses it exactly twice. The definition of 'b' is not so long: It is `b=Mod(m,n)`. OK, m and n can be large numbers. But still, I think the cleanest solution is to expand the definition and insert `Mod(m,n)` twice in the string.

sage -t "devel/sage/sage/rings/finite_rings/integer_mod.pyx" passes, I now do sage -testall

Of course, I added a doctest against the bug.


---

Comment by SimonKing created at 2010-07-06 17:00:18

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-07-06 18:35:35

`sage -testall` passes!


---

Comment by davidloeffler created at 2010-07-06 19:36:18

This modifies exactly the same code as #9205 (which already has a positive review). Sadly I didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK on top of #9205, and if not, rebase it?

David


---

Attachment

Fixes a side effect of log on PARI


---

Comment by SimonKing created at 2010-07-07 11:50:43

Replying to [comment:3 davidloeffler]:
> This modifies exactly the same code as #9205 (which already has a positive review). Sadly I 
> didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK 
> on top of #9205, and if not, rebase it?

It did not apply on top of #9205. So, I replaced the original patch by one that is to be applied after the two patches from #9205.

Cheers,

Simon


---

Comment by davidloeffler created at 2010-07-07 15:10:18

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:17:28

Resolution: fixed
