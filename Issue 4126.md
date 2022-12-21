# Issue 4126: [with patch; not ready for review] improve sage <--> magma interface for number fields

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-15 03:56:49

Assignee: was




---

Attachment

add sage number field --> magma number field conversion


---

Attachment

The part 3 patch that I applied does some re-architect-ing of the sage --> magma conversion system so now one can define either _magma_init_ in the very simple case when a pure string is enough or _magma_coerce_ when one wants to do arbitrarily complicated stuff but doesn't want to have to worry about caching. 

 Caching turns out to be extremely important, e.g., coercing the same number field twice into magma without caching would result in two separate copies of that number field in Magma with no coercion maps, which would cause lots of problems for other things.  This re-architecting will surely be needed all over the place as the Magma / Sage interface gets steadily improved.

It's possible that the choices of names is not optimal.  Using _magma_coerce_ was better than anything else I could think of (e.g., _magma_not_cached_, _magma_impl_, etc.).


---

Attachment


---

Comment by robertwb created at 2008-09-25 00:39:03

Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. 

In terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine.


---

Comment by mabshoff created at 2008-09-25 00:41:56

Replying to [comment:3 robertwb]:
> Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. 
> 
> In terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine. 

So the rename would turn this into a positive review?

Cheers,

Michael


---

Comment by robertwb created at 2008-09-25 00:46:48

The comment that magma -> sage is not implemented rather than unintentionally broken, and a comment on the name change (doesn't have to change, just looks like William was looking for ideas).


---

Attachment

respond to referee remark


---

Comment by was created at 2008-09-25 18:16:34

I've posted a patch that makes the change robert suggests, which I like. 

And indeed, this was definitely not meant to be feature complete, but a first self-contained step before I do a lot more that uses the same architecture.


---

Comment by robertwb created at 2008-09-25 19:03:27

I'm happy with the code.


---

Attachment

The following two hunks

```
`@``@` -5300,6 +5301,14 `@``@`
         return NumberField_cyclotomic_v1, (self.__n, self.variable_name())

     def _magma_init_(self):
+        # TODO: I really don't like this on multiple levels.
+        # (1) it kills a global symbol self.gen()
+        # (2) it abuses how conversion works and throws in an extra define.
+        # (3) a cyclo field in a funny generator wouldn't get converted to
+        #     one with the right name via this.
+        # (4) One should define _magma_coerce_ instead of _magma_init_
+        #     in this case, probably.
+        #    -- William
         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)

     def _repr_(self):
```

and

```
`@``@` -5306,7 +5306,7 `@``@`
         # (2) it abuses how conversion works and throws in an extra define.
         # (3) a cyclo field in a funny generator wouldn't get converted to
         #     one with the right name via this.
-        # (4) One should define _magma_coerce_ instead of _magma_init_
+        # (4) One should define _magma_convert_ instead of _magma_init_
         #     in this case, probably.
         #    -- William
         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)
```

did not apply cleanly against my merge tree, so I committed them manually. Patch is attached.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 05:06:14

Merged all five patches in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-26 05:06:14

Resolution: fixed
