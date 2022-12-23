# Issue 8200: ElementWrapper: doctests improvements to not abuse ZZ invariants

Issue created by migration from https://trac.sagemath.org/ticket/8200

Original creator: nthiery

Original creation time: 2010-02-06 12:03:24

Assignee: nthiery

CC:  sage-combinat

Keywords: ElementWrapper

The attached patch updates the doctests of ElementWrapper to use a custom dummy parent, rather than abusing from ZZ. This abuse could trigger a segfault (see #8177).


---

Comment by nthiery created at 2010-02-06 12:07:44

Changing status from new to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-02-06 12:07:44

Changing priority from major to blocker.


---

Comment by wdj created at 2010-02-06 13:19:11

This applied fine and passed 


```
./sage -t  "devel/sage/sage/structure/element_wrapper.py" 
```

for 4.3.2.rc0 on a mac 10.6.2. Running sage -testall now.


---

Comment by wdj created at 2010-02-06 16:42:26

This passed sage -testall on a mac 10.6.2 applied to 4.3.2.rc0. However, am not competent to judge the patch. Hopefully someone else can read it over and give a positive review.


---

Comment by was created at 2010-02-06 16:56:01

Changing assignee from nthiery to was.


---

Comment by was created at 2010-02-06 16:56:01

This patch itself looks fine and passes tests.  

However, it's critical that a patch to address this problem at least include a comment that completely explains the problem.   As it is, this patch just hides a problem that will certainly cause similar great confusion and pain later. 
  
So another patch that includes a statement of the problem is needed.   A trivial way to do this, would be to just link to *this* trac ticket, and post something here.  I'll add a 1-line addition to the patch above.  

And here's a good description of the full problem from emails:

```
Using ZZ as a parent for something which isn't of class
sage.rings.integer.Integer is what was causing the segfault here.
There's actually a bit more to the story -- in particular, one should
wonder why it only segfaulted on OSX. I'll make some comments about
what was going on below; more importantly, though, is what we should
do about fixing it. In general, there are a lot of parents that assume
that elements with that parent are of some fixed type; breaking this
rule would be bad on two counts: (1) we'd pay the price by having to
do a bunch of typechecks everywhere, which is no good, and (2) the
logic that depends on this isn't clearly defined -- it's just an
*implicit* assumption in lots of code all over the place.

So how should we fix it? Robert Bradshaw pointed out that there should
probably be a corresponding ParentWrapper, that one could use to
create wrapped parents for the wrapped elements. In fact, I think we
should go one step further -- I don't see why you should be able to
end up with an ElementWrapper without the corresponding ParentWrapper.
So passing parent=P should probably just create a wrapper out of P, if
it isn't one already. In general, being able to just choose your
parent out of the blue is a dangerous thing ... this might be a
reasonably controlled way to do so.

In the short term, someone needs to change up the docstrings in
element_wrapper.py, and at the very least, put a big warning in about
the dangers of getting to choose your parents. (There's surely a good
joke I'm missing here.) Nicolas, it might make the most sense for you
to modify the docstrings, if you have time ...

Now for the interesting part: what was going on? Well, the example on
the ticket creates an integer wrapper object, and then calls into the
integer comparison code with it. Since the two have identical parents,
the code lets it in, and passes it off to a function that implicitly
assumes both inputs are of type sage.rings.integer.Integer. Once that
code (_cmp_c_impl) gets its hands on them, it calls off to the gmp
mpz_cmp function to do a comparison on the two underlying mpz_ts.
However, the second argument was some other random Python object --
so, on OS X, it ends up taking some random chunk of the object, and
dereferencing it ... boom.

But why only on OSX? The sage.rings.integer.Integer object stores just
a bit of information and an mpz_t; the mpz_t is the number of
allocated limbs, the number of used limbs, and a pointer to the limbs.
I just ended up printing out the relevant bytes on my laptop and
sage.math ... on my laptop, both of the first two entries were just
large numbers. However, on sage.math, it happens that in the same
situation, the second entry happened to be all zeros. That means that
when mpz_cmp looks at the number, it decides that it's just zero, and
does the comparison without ever trying to actually access the limbs
-- so it works, except that it pretends the number is 0. (Indeed, 0 ==
a will return True on sage.math, for a as in the description on
#8177.) I just chatted with Robert Bradshaw, and at least in one
example on my laptop, creating a weakref will "fix" the problem -- no
more segfault. But then, you've still got a nonsense value it found
elsewhere in memory. (Interestingly, on his machine, he has the
opposite behavior -- a acts like 0 before the weakref, and segfaults
once it's there.)

For the curious, on my machine (little-endian 32-bit):

sage: hex(id(ZZ))
'0x191e6c0'

sage: hexdump(Integer(3))
000: 04 00 00 00
004: 00 34 4d 03
008: a0 b1 4e 03
012: c0 e6 91 01           <--  parent (=ZZ)
016: 0a 00 00 00           <-- mpz_t._alloc
020: 01 00 00 00           <-- mpz_t._size
024: 00 98 33 0a           <-- mpz_t._d

sage: b = ElementWrapper(3, ZZ)
sage: hex(id(b.__dict__))
'0xb84b810'

sage: hexdump(ElementWrapper(b, ZZ))
000: 03 00 00 00
004: 00 0d a9 01
008: a0 31 d2 01
012: c0 e6 91 01         <-- parent (=ZZ)
016: 60 46 85 0b         <-- __dict__
020: 00 00 00 00         <-- __weakref__ (=NULL)
                                      <-- shorter struct

# acts like Integer(0) as the NULL __weakref__ is interpreted as mpz_t._size = 0
sage: 5 + b
5
sage: 0 == b
True

sage: f = weakref.ref(b)
sage: hex(id(b.__weakref__))
'0xb86fe70'

sage: hexdump(b)
000: 04 00 00 00
004: 00 0d a9 01
008: a0 31 d2 01
012: c0 e6 91 01
016: 10 b8 84 0b
020: 70 fe 86 0b      <-- __weakref__ (garbage used for mpz_t._size, dereference off the end of the struct)

sage: 5 + b # BOOM
```



---

Comment by was created at 2010-02-06 16:57:04

I realized the comments in element_wrapper.py *still* refer to Integer, so that is wrong in your patch.


---

Comment by was created at 2010-02-06 16:59:24

Actually, the above comment is wrong.  Never mind about that.


---

Comment by was created at 2010-02-06 17:02:14

apply after the other patch.


---

Comment by was created at 2010-02-06 17:02:30

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by nthiery created at 2010-02-06 17:25:52

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2010-02-06 17:25:52

Replying to [comment:5 was]:
> This patch itself looks fine and passes tests.  

Thanks for the review.
 
> However, it's critical that a patch to address this problem at least include a comment that completely explains the problem.   As it is, this patch just hides a problem that will certainly cause similar great confusion and pain later. 


I fully agree that the issue with ZZ/Integer should not be left hidden, which is precisely why I forked this ticket in two.

But sorry, I don't accept the reviewer's patch. Integer/ZZ is broken. That's the purpose of #8177. Abusing ElementWrapper with ZZ as parent was broken. That's the purpose of this ticket. But ElementWrapper in itself is *not* broken (well at least in this context). Any other Sage element class that accepts a parent as input (that is most of them) would trigger the exact same issue when abused the same way.

I don't want people to be scared away of ElementWrapper because of an issue elsewhere.


---

Comment by nthiery created at 2010-02-06 17:26:15

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-02-06 18:08:42

Merged into sagenb-4.3.2 (wstein version -- post minh).


---

Comment by was created at 2010-02-06 18:08:42

Resolution: fixed
