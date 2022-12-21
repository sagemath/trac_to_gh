# Issue 1948: K.factor_integer needs a name change, since now it does much more

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-27 15:33:16

Assignee: was

For K a number field, K.factor_integer slices, dices, and also factors rationals, elements of the number field, etc.:


```
sage: K.<a> = NumberField(x^2 + 1)
sage: K.factor_integer(1/3)
Fractional ideal (3)^-1
sage: K.factor_integer(1+a)
Fractional ideal (a + 1)
sage: K.factor_integer(1+a/5)
(Fractional ideal (-3*a - 2)) * (Fractional ideal (a + 1)) * (Fractional ideal (-a - 2))^-1 * (Fractional ideal (2*a + 1))^-1
sage: 
```


So it needs to be named something else.  Suggestions welcome.  


---

Comment by AlexGhitza created at 2008-02-17 02:18:22

How about just calling it K.factor()?


---

Attachment


---

Comment by cremona created at 2008-04-05 14:28:06

The patch (based on 3.0.alpha0) follows Alex's suggestion.  It is a simple text replacement of all factor_integer -> factor in the source code.

I wondered about keeping factor_integer as an alias but decided against.


---

Comment by AlexGhitza created at 2008-04-13 00:51:43

Looks good to me.


---

Attachment

apply after trac1948.patch


---

Comment by AlexGhitza created at 2008-04-13 01:00:25

I just realized that it is a good idea to document the fact that factor() does more than factor integral elements, so I added a small patch that puts in William's examples as doctests.


---

Comment by mabshoff created at 2008-04-13 02:20:02

Merged both patches in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-13 02:20:02

Resolution: fixed


---

Attachment


---

Comment by AlexGhitza created at 2008-04-13 14:47:59

While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.

BTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)


---

Comment by AlexGhitza created at 2008-04-13 14:47:59

Resolution changed from fixed to 


---

Comment by AlexGhitza created at 2008-04-13 14:47:59

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-04-13 15:01:01

Resolution: fixed


---

Comment by mabshoff created at 2008-04-13 15:01:01

Replying to [comment:7 AlexGhitza]:
> While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.
> 
> BTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)
> 

Hi Alex,

those factor_integer instances do no longer exist in alpha4 [I assume John has rewritten that code in some other patch]:

```
sage-3.0.alpha4/devel/sage$ grep -r factor_integer *
sage-3.0.alpha4/devel/sage$     
```

I did run `-t -long` on the tree after applying the inital two patches. So I am closing this again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 15:56:01

Ahh, the irony: The problem is introduced by the two patches at #2880. I get doctest failures related to factor_interger and after applying the latest patch they get fixed.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-04-13 15:57:43

That makes sense, because I ran into this while reviewing #2880.

All is well that ends well.


---

Comment by mabshoff created at 2008-04-13 16:03:02

Merged trac1948-ell_finite_field.patch in Sage 3.0.alpha5 after merging #2880.

Cheers,

Michael
