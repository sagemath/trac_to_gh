# Issue 6263: Add __cmp__ method to ClassFunctions (group characters)

Issue created by migration from https://trac.sagemath.org/ticket/6263

Original creator: saliola

Original creation time: 2009-06-11 20:28:36

Assignee: joyner

The loads/dumps test for ClassFunction fails because `__cmp__` is not defined.

```
sage: chi = ClassFunction(CyclicPermutationGroup(4), [1,-1,1,-1])
sage: loads(dumps(chi)) == chi
False
```



---

Attachment


---

Comment by wdj created at 2009-06-11 21:48:23

I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?


---

Comment by jlefebvre created at 2009-06-11 22:05:09

Aside from wdj comments, the patch fixes the problem I was having with the characters of finite groups.
Does the  <  a shortcut for "does this character of G restrict to this character of H, where H is a subgroup of G"?


---

Comment by saliola created at 2009-06-11 22:17:08

Replying to [comment:2 wdj]:
> I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?

The GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:

```
So two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. 
```

So this is partly replicated here, except that the patch actually tests the groups as well as the values.

If you think it would be better, we can just ask GAP and return the answer it gives.


---

Comment by saliola created at 2009-06-11 22:20:14

Replying to [comment:3 jlefebvre]:
> Does the  <  a shortcut for "does this character of G restrict to this character of H, where H is a subgroup of G"?

No, it just does a comparison of the list of values. This is what GAP does (see my previous method for more information).


---

Comment by wdj created at 2009-06-11 22:30:49

Replying to [comment:4 saliola]:
> Replying to [comment:2 wdj]:
> > I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?
> 
> The GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:
> {{{
> So two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. 
> }}}

Okay, it seems as though at least you are improving the situation over what GAP has!



> So this is partly replicated here, except that the patch actually tests the groups as well as the values.
> 
> If you think it would be better, we can just ask GAP and return the answer it gives.


---

Comment by jlefebvre created at 2009-06-12 05:12:36

It looks good to me, I'm not quite sure of gaps justification of having less than comparison, but seems there's nothing wrong in following it. So, marking it with positive review.


---

Comment by ncalexan created at 2009-06-13 21:13:58

Resolution: fixed
