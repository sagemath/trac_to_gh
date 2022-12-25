# Issue 8200: ElementWrapper: doctests improvements to not abuse ZZ invariants

archive/issues_008200.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: ElementWrapper\n\nThe attached patch updates the doctests of ElementWrapper to use a custom dummy parent, rather than abusing from ZZ. This abuse could trigger a segfault (see #8177).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8200\n\n",
    "created_at": "2010-02-06T12:03:24Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "ElementWrapper: doctests improvements to not abuse ZZ invariants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8200",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: ElementWrapper

The attached patch updates the doctests of ElementWrapper to use a custom dummy parent, rather than abusing from ZZ. This abuse could trigger a segfault (see #8177).

Issue created by migration from https://trac.sagemath.org/ticket/8200





---

archive/issue_comments_072190.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-06T12:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72190",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072191.json:
```json
{
    "body": "Attachment [trac_8200-element_wrapper_doctests-nt.patch](tarball://root/attachments/some-uuid/ticket8200/trac_8200-element_wrapper_doctests-nt.patch) by @nthiery created at 2010-02-06 12:07:44",
    "created_at": "2010-02-06T12:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72191",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8200-element_wrapper_doctests-nt.patch](tarball://root/attachments/some-uuid/ticket8200/trac_8200-element_wrapper_doctests-nt.patch) by @nthiery created at 2010-02-06 12:07:44



---

archive/issue_comments_072192.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-06T12:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72192",
    "user": "https://github.com/nthiery"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_072193.json:
```json
{
    "body": "This applied fine and passed \n\n\n```\n./sage -t  \"devel/sage/sage/structure/element_wrapper.py\" \n```\n\nfor 4.3.2.rc0 on a mac 10.6.2. Running sage -testall now.",
    "created_at": "2010-02-06T13:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72193",
    "user": "https://github.com/wdjoyner"
}
```

This applied fine and passed 


```
./sage -t  "devel/sage/sage/structure/element_wrapper.py" 
```

for 4.3.2.rc0 on a mac 10.6.2. Running sage -testall now.



---

archive/issue_comments_072194.json:
```json
{
    "body": "This passed sage -testall on a mac 10.6.2 applied to 4.3.2.rc0. However, am not competent to judge the patch. Hopefully someone else can read it over and give a positive review.",
    "created_at": "2010-02-06T16:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72194",
    "user": "https://github.com/wdjoyner"
}
```

This passed sage -testall on a mac 10.6.2 applied to 4.3.2.rc0. However, am not competent to judge the patch. Hopefully someone else can read it over and give a positive review.



---

archive/issue_comments_072195.json:
```json
{
    "body": "Changing assignee from @nthiery to @williamstein.",
    "created_at": "2010-02-06T16:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72195",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @nthiery to @williamstein.



---

archive/issue_comments_072196.json:
```json
{
    "body": "This patch itself looks fine and passes tests.  \n\nHowever, it's critical that a patch to address this problem at least include a comment that completely explains the problem.   As it is, this patch just hides a problem that will certainly cause similar great confusion and pain later. \n  \nSo another patch that includes a statement of the problem is needed.   A trivial way to do this, would be to just link to *this* trac ticket, and post something here.  I'll add a 1-line addition to the patch above.  \n\nAnd here's a good description of the full problem from emails:\n\n```\nUsing ZZ as a parent for something which isn't of class\nsage.rings.integer.Integer is what was causing the segfault here.\nThere's actually a bit more to the story -- in particular, one should\nwonder why it only segfaulted on OSX. I'll make some comments about\nwhat was going on below; more importantly, though, is what we should\ndo about fixing it. In general, there are a lot of parents that assume\nthat elements with that parent are of some fixed type; breaking this\nrule would be bad on two counts: (1) we'd pay the price by having to\ndo a bunch of typechecks everywhere, which is no good, and (2) the\nlogic that depends on this isn't clearly defined -- it's just an\n*implicit* assumption in lots of code all over the place.\n\nSo how should we fix it? Robert Bradshaw pointed out that there should\nprobably be a corresponding ParentWrapper, that one could use to\ncreate wrapped parents for the wrapped elements. In fact, I think we\nshould go one step further -- I don't see why you should be able to\nend up with an ElementWrapper without the corresponding ParentWrapper.\nSo passing parent=P should probably just create a wrapper out of P, if\nit isn't one already. In general, being able to just choose your\nparent out of the blue is a dangerous thing ... this might be a\nreasonably controlled way to do so.\n\nIn the short term, someone needs to change up the docstrings in\nelement_wrapper.py, and at the very least, put a big warning in about\nthe dangers of getting to choose your parents. (There's surely a good\njoke I'm missing here.) Nicolas, it might make the most sense for you\nto modify the docstrings, if you have time ...\n\nNow for the interesting part: what was going on? Well, the example on\nthe ticket creates an integer wrapper object, and then calls into the\ninteger comparison code with it. Since the two have identical parents,\nthe code lets it in, and passes it off to a function that implicitly\nassumes both inputs are of type sage.rings.integer.Integer. Once that\ncode (_cmp_c_impl) gets its hands on them, it calls off to the gmp\nmpz_cmp function to do a comparison on the two underlying mpz_ts.\nHowever, the second argument was some other random Python object --\nso, on OS X, it ends up taking some random chunk of the object, and\ndereferencing it ... boom.\n\nBut why only on OSX? The sage.rings.integer.Integer object stores just\na bit of information and an mpz_t; the mpz_t is the number of\nallocated limbs, the number of used limbs, and a pointer to the limbs.\nI just ended up printing out the relevant bytes on my laptop and\nsage.math ... on my laptop, both of the first two entries were just\nlarge numbers. However, on sage.math, it happens that in the same\nsituation, the second entry happened to be all zeros. That means that\nwhen mpz_cmp looks at the number, it decides that it's just zero, and\ndoes the comparison without ever trying to actually access the limbs\n-- so it works, except that it pretends the number is 0. (Indeed, 0 ==\na will return True on sage.math, for a as in the description on\n#8177.) I just chatted with Robert Bradshaw, and at least in one\nexample on my laptop, creating a weakref will \"fix\" the problem -- no\nmore segfault. But then, you've still got a nonsense value it found\nelsewhere in memory. (Interestingly, on his machine, he has the\nopposite behavior -- a acts like 0 before the weakref, and segfaults\nonce it's there.)\n\nFor the curious, on my machine (little-endian 32-bit):\n\nsage: hex(id(ZZ))\n'0x191e6c0'\n\nsage: hexdump(Integer(3))\n000: 04 00 00 00\n004: 00 34 4d 03\n008: a0 b1 4e 03\n012: c0 e6 91 01           <--  parent (=ZZ)\n016: 0a 00 00 00           <-- mpz_t._alloc\n020: 01 00 00 00           <-- mpz_t._size\n024: 00 98 33 0a           <-- mpz_t._d\n\nsage: b = ElementWrapper(3, ZZ)\nsage: hex(id(b.__dict__))\n'0xb84b810'\n\nsage: hexdump(ElementWrapper(b, ZZ))\n000: 03 00 00 00\n004: 00 0d a9 01\n008: a0 31 d2 01\n012: c0 e6 91 01         <-- parent (=ZZ)\n016: 60 46 85 0b         <-- __dict__\n020: 00 00 00 00         <-- __weakref__ (=NULL)\n                                      <-- shorter struct\n\n# acts like Integer(0) as the NULL __weakref__ is interpreted as mpz_t._size = 0\nsage: 5 + b\n5\nsage: 0 == b\nTrue\n\nsage: f = weakref.ref(b)\nsage: hex(id(b.__weakref__))\n'0xb86fe70'\n\nsage: hexdump(b)\n000: 04 00 00 00\n004: 00 0d a9 01\n008: a0 31 d2 01\n012: c0 e6 91 01\n016: 10 b8 84 0b\n020: 70 fe 86 0b      <-- __weakref__ (garbage used for mpz_t._size, dereference off the end of the struct)\n\nsage: 5 + b # BOOM\n```\n",
    "created_at": "2010-02-06T16:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72196",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_072197.json:
```json
{
    "body": "I realized the comments in element_wrapper.py *still* refer to Integer, so that is wrong in your patch.",
    "created_at": "2010-02-06T16:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72197",
    "user": "https://github.com/williamstein"
}
```

I realized the comments in element_wrapper.py *still* refer to Integer, so that is wrong in your patch.



---

archive/issue_comments_072198.json:
```json
{
    "body": "Actually, the above comment is wrong.  Never mind about that.",
    "created_at": "2010-02-06T16:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72198",
    "user": "https://github.com/williamstein"
}
```

Actually, the above comment is wrong.  Never mind about that.



---

archive/issue_comments_072199.json:
```json
{
    "body": "apply after the other patch.",
    "created_at": "2010-02-06T17:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72199",
    "user": "https://github.com/williamstein"
}
```

apply after the other patch.



---

archive/issue_comments_072200.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-06T17:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72200",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072201.json:
```json
{
    "body": "Attachment [trac-8200-part2-referee.patch](tarball://root/attachments/some-uuid/ticket8200/trac-8200-part2-referee.patch) by @williamstein created at 2010-02-06 17:02:30",
    "created_at": "2010-02-06T17:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72201",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-8200-part2-referee.patch](tarball://root/attachments/some-uuid/ticket8200/trac-8200-part2-referee.patch) by @williamstein created at 2010-02-06 17:02:30



---

archive/issue_comments_072202.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-06T17:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72202",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072203.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> This patch itself looks fine and passes tests.  \n\nThanks for the review.\n \n> However, it's critical that a patch to address this problem at least include a comment that completely explains the problem.   As it is, this patch just hides a problem that will certainly cause similar great confusion and pain later. \n\n\nI fully agree that the issue with ZZ/Integer should not be left hidden, which is precisely why I forked this ticket in two.\n\nBut sorry, I don't accept the reviewer's patch. Integer/ZZ is broken. That's the purpose of #8177. Abusing ElementWrapper with ZZ as parent was broken. That's the purpose of this ticket. But ElementWrapper in itself is *not* broken (well at least in this context). Any other Sage element class that accepts a parent as input (that is most of them) would trigger the exact same issue when abused the same way.\n\nI don't want people to be scared away of ElementWrapper because of an issue elsewhere.",
    "created_at": "2010-02-06T17:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72203",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 was]:
> This patch itself looks fine and passes tests.  

Thanks for the review.
 
> However, it's critical that a patch to address this problem at least include a comment that completely explains the problem.   As it is, this patch just hides a problem that will certainly cause similar great confusion and pain later. 


I fully agree that the issue with ZZ/Integer should not be left hidden, which is precisely why I forked this ticket in two.

But sorry, I don't accept the reviewer's patch. Integer/ZZ is broken. That's the purpose of #8177. Abusing ElementWrapper with ZZ as parent was broken. That's the purpose of this ticket. But ElementWrapper in itself is *not* broken (well at least in this context). Any other Sage element class that accepts a parent as input (that is most of them) would trigger the exact same issue when abused the same way.

I don't want people to be scared away of ElementWrapper because of an issue elsewhere.



---

archive/issue_comments_072204.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-06T17:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72204",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072205.json:
```json
{
    "body": "Merged into sagenb-4.3.2 (wstein version -- post minh).",
    "created_at": "2010-02-06T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72205",
    "user": "https://github.com/williamstein"
}
```

Merged into sagenb-4.3.2 (wstein version -- post minh).



---

archive/issue_comments_072206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-06T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8200#issuecomment-72206",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008402.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-02-06T18:08:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8200",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8200#event-8402"
}
```
