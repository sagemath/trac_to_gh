# Issue 8649: to_tableau method broken for crystals of type B

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2010-04-03 15:56:10

Assignee: sage-combinat

CC:  sage-combinat

Keywords: crystals

- For type B_n the to_tableau method in crystals is wrong: 00 in the list should give a column and not a row

- Changed __call__ function in both TensorProductOfCrystals and CrystalOfTableau x to _element_constructor_ to make automatic tests pass (before element constructor was not an idempotent)

- Fixed subsequent bug of empty tableau in CrystalOfTableau and empty highest weight crystal



---

Attachment


---

Comment by aschilling created at 2010-04-03 17:29:40

Changing status from new to needs_review.


---

Comment by bump created at 2010-04-18 15:41:38

Changing status from needs_review to positive_review.


---

Comment by bump created at 2010-04-18 15:41:38

Before the patch, the to_tableau method of crystals of tableaux could return a tableau with the wrong shape. I did a lot of testing of the fix. I found that there were problems with type B crystals, but also for type G2. (Crystal of letters, and hence crystals of tableaux are implemented for Type G2 even though this method of producing crystals may not be appropriate for other exceptional types.)

After the patch I found no problems after testing a lot of crystals of various Cartan types. In order to test a crystal, I simply verified that all elements v have the same `v.to_tableau().shape()`.

I also ran sage -testall and all tests pass.

The `__call__` method is also changed to `_element_constructor_` for the reason given in the patch description. This does not seem to break anything.

My conclusion is that the patch is correct and fixes a bad book. It should be merged.


---

Comment by nthiery created at 2010-04-18 15:47:03

Ah, we did a simultaneous review :-) Well, for the record, here were my comments:

All test pass on 4.3.5, and the changes are technically good (crystals are far more coercion friendly now). Thanks Anne for handling this!

I am just not very comfortable with the special casing with 0 to handle type B, which sounds more like a workaround than a mathematically meaningful rule.

Dan: what do you think? If that's fine with you, please set a positive review.


---

Comment by bump created at 2010-04-18 16:07:24

I wrote:

> My conclusion is that the patch is correct and fixes a bad book. It should be merged.

I meant a bad *bug*.

Replying to Nicolas:

It was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.
I don't understand this as a mathematical point, but I did enough testing that I am sure
the patch is right.


---

Comment by aschilling created at 2010-04-18 16:30:11

Dear Dan and Nicolas,

Thank you for the review. The mathematical reason why in type B the 0 is special,
is that it sits in a string of length 2:

1 -> 2 -> 0 -> -2 -> -1

Hence a column of height 2 for example can become

2      0      0      0
1 -2-> 1 -1-> 2 -2-> 0

since in the tensor product always the rightmost unbracketed element is changed.
For similar reasons, in the row case there cannot be two 0s.

So this is really due to the string of length 2 which the other crystal of letters
do not have. Nicolas, how else should the code be written to detect this?
The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
case specific.

Best wishes,

Anne  

Replying to [comment:4 bump]:
> I wrote:
> 
> > My conclusion is that the patch is correct and fixes a bad book. It should be merged.
> 
> I meant a bad *bug*.
> 
> Replying to Nicolas:
> 
> It was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.
> I don't understand this as a mathematical point, but I did enough testing that I am sure
> the patch is right.
>


---

Comment by nthiery created at 2010-04-18 17:28:40

Replying to [comment:5 aschilling]:
> Thank you for the review. The mathematical reason why in type B the 0 is special,
> is that it sits in a string of length 2:
> 
> 1 -> 2 -> 0 -> -2 -> -1
> 
> Hence a column of height 2 for example can become
> 
> 2      0      0      0
> 1 -2-> 1 -1-> 2 -2-> 0
> 
> since in the tensor product always the rightmost unbracketed element is changed.
> For similar reasons, in the row case there cannot be two 0s.
> 
> So this is really due to the string of length 2 which the other crystal of letters
> do not have. Nicolas, how else should the code be written to detect this?
> The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
> case specific.

In a perfect world, a crystal of letter would have a method which
would take two letters a and b, and say whether b can be above a in a
column. There would be a default implementation (returning a<b in the
crystal of letters), and the type B crystal of letter would override
this default implementation appropriately.

If we are sure that no crystal of letter (or more generally crystal
that we want to use as letter in a tableau) will ever have a letter
called `0`, except for type `B`, or if we are willing to take the
risk, then I guess we can be lazy, and just leave things as they are.


---

Comment by aschilling created at 2010-04-18 19:14:34

Replying to [comment:6 nthiery]:
> Replying to [comment:5 aschilling]:
> > Thank you for the review. The mathematical reason why in type B the 0 is special,
> > is that it sits in a string of length 2:
> > 
> > 1 -> 2 -> 0 -> -2 -> -1
> > 
> > Hence a column of height 2 for example can become
> > 
> > 2      0      0      0
> > 1 -2-> 1 -1-> 2 -2-> 0
> > 
> > since in the tensor product always the rightmost unbracketed element is changed.
> > For similar reasons, in the row case there cannot be two 0s.
> > 
> > So this is really due to the string of length 2 which the other crystal of letters
> > do not have. Nicolas, how else should the code be written to detect this?
> > The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
> > case specific.
> 
> In a perfect world, a crystal of letter would have a method which
> would take two letters a and b, and say whether b can be above a in a
> column. There would be a default implementation (returning a<b in the
> crystal of letters), and the type B crystal of letter would override
> this default implementation appropriately.
> 
> If we are sure that no crystal of letter (or more generally crystal
> that we want to use as letter in a tableau) will ever have a letter
> called `0`, except for type `B`, or if we are willing to take the
> risk, then I guess we can be lazy, and just leave things as they are.

For the classical types ABCD, only type B has a 0. My plan was to implement the exceptional types in a generic way at some point using Littelmann paths or the alcove model and then possibly the HighestWeightCrystal environment. The tableaux method is rather type specific. 

For type D, one can have columns of the form n-bar n n-bar n .... since they are not comparable, so I think a<b for columns might not be the right point of view.  Rather not(a>=b) with the exception of a=b=0. But in any case, one has to distinguish cases. Right now the tableaux method for crystals is only supposed to work for type ABCD.


---

Comment by bump created at 2010-04-18 19:32:07

> Right now the tableaux method for crystals is only supposed to work for type ABCD.

The tableaux method does work with Sage for G2. This *may* be an accident
in that this would not be a good approach for other exceptional groups. Or
maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
patch, crystals of tableaux for G2 produce correct tableaux output.

I tend to think this is *not* an accident and take it as evidence that 0 is
really special. I guess the case where things might break in a worse way  is F4.

> If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.

I think the positive review should stand. It's not just a matter of laziness, unless
we have an alternative approach.


---

Comment by nthiery created at 2010-04-18 19:40:03

Replying to [comment:8 bump]:
> The tableaux method does work with Sage for G2. This *may* be an accident
> in that this would not be a good approach for other exceptional groups. Or
> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
> patch, crystals of tableaux for G2 produce correct tableaux output.
> 
> I tend to think this is *not* an accident and take it as evidence that 0 is
> really special. I guess the case where things might break in a worse way  is F4.

That's an interesting point!

> > If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.
> 
> I think the positive review should stand. It's not just a matter of laziness, unless
> we have an alternative approach.

I still think it is laziness until we have a proof that 0 is special in all types. But I agree that the positive review should stand.


---

Comment by aschilling created at 2010-04-19 05:20:27

Replying to [comment:8 bump]:
> > Right now the tableaux method for crystals is only supposed to work for type ABCD.
> 
> The tableaux method does work with Sage for G2. This *may* be an accident
> in that this would not be a good approach for other exceptional groups. Or
> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
> patch, crystals of tableaux for G2 produce correct tableaux output.
> 
> I tend to think this is *not* an accident and take it as evidence that 0 is
> really special. I guess the case where things might break in a worse way  is F4.

Hi Dan,

Thank you for this comment! Yes, for G_2 0 is again the only letter that sits
in a string of length 2. I suppose the letter 0 is chosen in crystal of letters since the weight is zero (and hence the element sits in the middle of a string).
Perhaps Nicolas accepts this as "proof" that 0 is special?

Anne


---

Comment by jhpalmieri created at 2010-04-19 05:21:37

Merged "trac_8649_crystal-as.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:21:37

Resolution: fixed
