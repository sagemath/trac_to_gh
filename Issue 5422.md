# Issue 5422: [with patch, needs review] Quadratic forms polynomial

Issue created by migration from https://trac.sagemath.org/ticket/5422

Original creator: aly.deines

Original creation time: 2009-03-02 19:25:09

Assignee: justin

Keywords: quadratic forms

Given a quadratic form Q over the ring R of dimension n, this returns the polynomial form in n variables over R.  


---

Comment by aly.deines created at 2009-03-02 19:25:44

polynomial of a quadratic form patch


---

Attachment

REFEREE REPORT:


 * change it to 

```
  EXAMPLES::
  
      sage: stuff
```

for the new ReST format.

 * Don't hardcode only x, i.e., change this:

```
polynomial(self):
```

to 

```
polynomial(self, names='x'):
```


Yes, "names" sounds funny, but is traditional in sage for this.

 * Change "Input:" and "Output:" to be all caps and on their own line, like in the rest of sage. 

 * This is silly code `[R.gens()[i] for i in range(n)]` because `R.gens()` is almost the same thing.  If you really need a list do `list(R.gens())`.

 * This worries me: `(M*V).dot_product(V) `.  Should it be `(V*M).dot_product(V)`?


---

Comment by aly.deines created at 2010-11-04 21:16:04

Changing status from needs_work to needs_review.


---

Comment by spice created at 2010-11-05 16:22:28

Two things:
You need to list 'names' under the input section of the docstring.
Secondly, you forgot a period in your error message.

Otherwise good :-)


---

Comment by spice created at 2010-11-05 16:22:28

Changing status from needs_review to needs_work.


---

Comment by spice created at 2010-11-05 16:40:17

Replaces previous patch.


---

Attachment

Done the docstring updating. A review and we should be good to go.


---

Comment by spice created at 2010-11-05 16:42:46

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2010-11-05 18:38:59

After the error message had the grammer fixed (a period was added) the doctest needed that as well.  This is fixed in the current patch.


---

Comment by spice created at 2010-11-05 21:41:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-07 10:19:41

Please change the commit message of the third patch.  Currently it says "added a period to the doc test", but that applies only to the last changes made, not the whole patch.  If a patch _replaces_ previous patches, the commit message should be clear by itself.


---

Comment by jdemeyer created at 2010-11-07 10:19:41

Changing status from positive_review to needs_work.


---

Comment by aly.deines created at 2010-11-10 06:31:10

I changed the commit message to apply the the whole patch.


---

Comment by aly.deines created at 2010-11-10 06:31:10

Changing status from needs_work to needs_review.


---

Attachment

Replaces previous patch.


---

Comment by aly.deines created at 2010-11-10 17:57:26

I have fixed the comment to apply to the whole patch.


---

Comment by spice created at 2010-11-10 18:08:42

Changing status from needs_review to positive_review.


---

Comment by spice created at 2010-11-10 18:08:42

This latest version looks good to me.


---

Comment by jdemeyer created at 2010-11-11 13:01:38

Resolution: fixed


---

Comment by was created at 2010-11-22 23:39:19

I have some issues with this patch, which I hope will get fixed in a followup patch:

1. The ReST formatting is wrong for the list of inputs:

```
        1125	            -'self' - a quadratic form over a commatitive ring. 
 	1126	            -'names' - the name of the variables. Digits will be appended to the name for each different canonical 
 	1127	            variable e.g x1, x2, x3 etc. 
```

but it should be

```
        1125	            - 'self' - a quadratic form over a commatitive ring. 
 	1126	            - 'names' - the name of the variables. Digits will be appended to the name for each different canonical 
 	1127	              variable e.g x1, x2, x3 etc. 
```


Note the space after dash and the matching indention right before "variable".

2. I do not like this naked except, and think except: should almost never be used in Python:

```
        1160	        try: 
 	1161	            R = PolynomialRing(self.base_ring(),names,n) 
 	1162	        except: 
 	1163	            raise ValueError, 'Can only create polynomial rings over commutative rings.' 
```

How do you know that the error in creating the polynomial ring was due to poly ring not working because the ring is not commutative?   I would actually recommend just changing the above to:

```
                    R = PolynomialRing(self.base_ring(),names,n)
```

and completely get rid of the exception.     A proper exception will get raised by the PolynomialRing function itself.
