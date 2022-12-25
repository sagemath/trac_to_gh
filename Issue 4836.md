# Issue 4836: pari types getattr() function ugly and inefficient

archive/issues_004836.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jdemeyer\n\nthe pari interface relies on the function getattr(), e.g. as in\n\n```\nzk_basis = K.pari_nf().getattr('zk')\n```\n\nbut I *really* don't like this function!  Each of these dot-attributes\nin pari is a short-cut, in this case to `K.pari_nf()[6]`, as these are\neasier when running gp than remembering which field is which in the\nnf/bnf structures.  There are not very many of these (I started making\na list).  But what I do not like is the implementation of getattr() in\nSage:\n\n```\n   def getattr(self, attr):\n       t0GEN(str(self) + '.' + str(attr))\n       _sig_on\n       return self.new_gen(t0)\n```\n\nSo it converts the nf into a string (in my examples, that's a string\nof length 59604), adds \".zk\" to it, and reparses the input (using the\ngp parser).\n\nWe could instead implement the getattr function with a dictionary like\nthis for an nf:\n\n```\n{('pol',1), ('sign',2), ('r1',(2,1)), ('r2',(2,2)),\n```\n\netc   (where the numbers are indices into the array so should actually have 1 subtracted\nfrom them).\n\nThe only disadvantage I can see for this is that new versions of pari\nmight change the indices -- though I doubt that happens often, as you\ncan see from the existence of unused fields which are just there to\npad arrays to the expected length.  And in any case doctests would\nfind these.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4836\n\n",
    "created_at": "2008-12-20T12:08:49Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "pari types getattr() function ugly and inefficient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4836",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

CC:  @jdemeyer

the pari interface relies on the function getattr(), e.g. as in

```
zk_basis = K.pari_nf().getattr('zk')
```

but I *really* don't like this function!  Each of these dot-attributes
in pari is a short-cut, in this case to `K.pari_nf()[6]`, as these are
easier when running gp than remembering which field is which in the
nf/bnf structures.  There are not very many of these (I started making
a list).  But what I do not like is the implementation of getattr() in
Sage:

```
   def getattr(self, attr):
       t0GEN(str(self) + '.' + str(attr))
       _sig_on
       return self.new_gen(t0)
```

So it converts the nf into a string (in my examples, that's a string
of length 59604), adds ".zk" to it, and reparses the input (using the
gp parser).

We could instead implement the getattr function with a dictionary like
this for an nf:

```
{('pol',1), ('sign',2), ('r1',(2,1)), ('r2',(2,2)),
```

etc   (where the numbers are indices into the array so should actually have 1 subtracted
from them).

The only disadvantage I can see for this is that new versions of pari
might change the indices -- though I doubt that happens often, as you
can see from the existence of unused fields which are just there to
pad arrays to the expected length.  And in any case doctests would
find these.

Issue created by migration from https://trac.sagemath.org/ticket/4836





---

archive/issue_events_011107.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-20T14:07:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4836#event-11107"
}
```



---

archive/issue_comments_036576.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-07-11T11:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36576",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_comments_036577.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2009-07-11T11:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36577",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to interfaces.



---

archive/issue_events_011108.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-08-04T07:37:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4836#event-11108"
}
```



---

archive/issue_events_011109.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-08-04T07:37:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4836#event-11109"
}
```



---

archive/issue_comments_036578.json:
```json
{
    "body": "This can be dealt with after #9343 has been merged.  PARI 2.4 has functions like nf_get_zk() which do exactly that.",
    "created_at": "2010-08-04T07:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36578",
    "user": "https://github.com/jdemeyer"
}
```

This can be dealt with after #9343 has been merged.  PARI 2.4 has functions like nf_get_zk() which do exactly that.



---

archive/issue_comments_036579.json:
```json
{
    "body": "As a reference, I grepped such occurances:\n\n\n```\nsage/rings/number_field/number_field_element.pyx:296:                Zbasis = self.number_field().pari_nf().getattr('zk')\nsage/rings/number_field/number_field_ideal_rel.py:118:            self.__pari_rhnf = rnf.rnfidealabstorel(nf.getattr('zk')*L_hnf)\nsage/rings/number_field/number_field.py:2614:        cycle_structure = eval(str(k.getattr('clgp.cyc')))\nsage/rings/number_field/number_field.py:2617:        gens = k.getattr('clgp.gen')\nsage/rings/number_field/number_field.py:3207:            diff = self.pari_nf().getattr('diff')\nsage/rings/number_field/number_field.py:3208:            zk_basis = self.pari_nf().getattr('zk')\nsage/rings/number_field/number_field.py:4190:            s = str(k.getattr('reg'))\nsage/rings/number_field/number_field.py:4274:        r1, r2 = self.pari_nf().getattr('sign')\nsage/rings/number_field/number_field_ideal.py:92:    return field.pari_nf().getattr('zk') * hnf\nsage/rings/number_field/number_field_ideal.py:119:    alpha = field( field.pari_nf().getattr('zk') * ideal[2] )\nsage/rings/number_field/number_field_ideal.py:643:            gens = [ K(a), K(nf.getattr('zk')*alpha) ]\nsage/rings/number_field/number_field_ideal.py:842:                g = K(bnf.getattr('zk') * v[1])\nsage/rings/number_field/number_field_ideal.py:1024:            self.__smallest_integer = ZZ(self._pari_prime.getattr('p'))\nsage/rings/number_field/number_field_ideal.py:1335:            zk_basis = K.pari_nf().getattr('zk')\nsage/rings/number_field/number_field_ideal.py:1337:                prime, alpha = p.getattr('gen')\nsage/rings/number_field/number_field_ideal.py:1478:            return ZZ(self._pari_prime.getattr('e'))\nsage/rings/number_field/number_field_ideal.py:2008:            sage: bid.getattr('clgp')\nsage/rings/number_field/number_field_ideal.py:2013:            if flag==2 and len(bid.getattr('clgp'))<3:\nsage/rings/number_field/number_field_ideal.py:2069:        inv = eval(str(G.getattr('cyc')))\nsage/rings/number_field/number_field_ideal.py:2074:            g = G.getattr('gen')\nsage/rings/number_field/number_field_ideal.py:2188:        return K(bnf.getattr('zk')*r)\nsage/rings/number_field/number_field_ideal.py:2529:            return ZZ(self._pari_prime.getattr('f'))\n```\n",
    "created_at": "2010-08-15T12:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36579",
    "user": "https://github.com/jdemeyer"
}
```

As a reference, I grepped such occurances:


```
sage/rings/number_field/number_field_element.pyx:296:                Zbasis = self.number_field().pari_nf().getattr('zk')
sage/rings/number_field/number_field_ideal_rel.py:118:            self.__pari_rhnf = rnf.rnfidealabstorel(nf.getattr('zk')*L_hnf)
sage/rings/number_field/number_field.py:2614:        cycle_structure = eval(str(k.getattr('clgp.cyc')))
sage/rings/number_field/number_field.py:2617:        gens = k.getattr('clgp.gen')
sage/rings/number_field/number_field.py:3207:            diff = self.pari_nf().getattr('diff')
sage/rings/number_field/number_field.py:3208:            zk_basis = self.pari_nf().getattr('zk')
sage/rings/number_field/number_field.py:4190:            s = str(k.getattr('reg'))
sage/rings/number_field/number_field.py:4274:        r1, r2 = self.pari_nf().getattr('sign')
sage/rings/number_field/number_field_ideal.py:92:    return field.pari_nf().getattr('zk') * hnf
sage/rings/number_field/number_field_ideal.py:119:    alpha = field( field.pari_nf().getattr('zk') * ideal[2] )
sage/rings/number_field/number_field_ideal.py:643:            gens = [ K(a), K(nf.getattr('zk')*alpha) ]
sage/rings/number_field/number_field_ideal.py:842:                g = K(bnf.getattr('zk') * v[1])
sage/rings/number_field/number_field_ideal.py:1024:            self.__smallest_integer = ZZ(self._pari_prime.getattr('p'))
sage/rings/number_field/number_field_ideal.py:1335:            zk_basis = K.pari_nf().getattr('zk')
sage/rings/number_field/number_field_ideal.py:1337:                prime, alpha = p.getattr('gen')
sage/rings/number_field/number_field_ideal.py:1478:            return ZZ(self._pari_prime.getattr('e'))
sage/rings/number_field/number_field_ideal.py:2008:            sage: bid.getattr('clgp')
sage/rings/number_field/number_field_ideal.py:2013:            if flag==2 and len(bid.getattr('clgp'))<3:
sage/rings/number_field/number_field_ideal.py:2069:        inv = eval(str(G.getattr('cyc')))
sage/rings/number_field/number_field_ideal.py:2074:            g = G.getattr('gen')
sage/rings/number_field/number_field_ideal.py:2188:        return K(bnf.getattr('zk')*r)
sage/rings/number_field/number_field_ideal.py:2529:            return ZZ(self._pari_prime.getattr('f'))
```




---

archive/issue_comments_036580.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari gp getattr\".",
    "created_at": "2010-09-19T20:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36580",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "pari gp getattr".



---

archive/issue_comments_036581.json:
```json
{
    "body": "Still needs some polishing but the essence of this patch is done.",
    "created_at": "2010-09-19T20:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36581",
    "user": "https://github.com/jdemeyer"
}
```

Still needs some polishing but the essence of this patch is done.



---

archive/issue_comments_036582.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-09-19T20:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36582",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_036583.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T21:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36583",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036584.json:
```json
{
    "body": "I just realized I have not yet done any tests on a 32-bit system.  I will do a `make testlong` on a 32-bit OS X 10.4 PPC system.",
    "created_at": "2010-09-25T15:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36584",
    "user": "https://github.com/jdemeyer"
}
```

I just realized I have not yet done any tests on a 32-bit system.  I will do a `make testlong` on a 32-bit OS X 10.4 PPC system.



---

archive/issue_comments_036585.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n\nI'm about to test on a 32-bit machine as well.",
    "created_at": "2010-09-25T16:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36585",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:11 jdemeyer]:

I'm about to test on a 32-bit machine as well.



---

archive/issue_comments_036586.json:
```json
{
    "body": "Patch applies fine to 4.6.alpha1 +  #9898 + #9753.\n\nTests all pass on a 32-bit machine.\n\nIn the patch:  \n\n1. Is the first line of docstring of ideallist() a typo:   \"Vector of vectors `L` of all idealstar of all ideals of `norm <= bound`. \" ?  Or are you using \"idealstar\" in a PARI-technical sense of \"ideal structure with extra data?\n2. Can you explain the quotes in the patch to maps.py (e.g. \"'x\") \n3. I would not have minded if you had removed my old smallest_integer code instead of commenting it out!\n\nPositive review!  Thanks for doing this.  (Did you deal with all occurrences of getattr()?)",
    "created_at": "2010-09-26T14:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36586",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.6.alpha1 +  #9898 + #9753.

Tests all pass on a 32-bit machine.

In the patch:  

1. Is the first line of docstring of ideallist() a typo:   "Vector of vectors `L` of all idealstar of all ideals of `norm <= bound`. " ?  Or are you using "idealstar" in a PARI-technical sense of "ideal structure with extra data?
2. Can you explain the quotes in the patch to maps.py (e.g. "'x") 
3. I would not have minded if you had removed my old smallest_integer code instead of commenting it out!

Positive review!  Thanks for doing this.  (Did you deal with all occurrences of getattr()?)



---

archive/issue_comments_036587.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-26T14:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36587",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036588.json:
```json
{
    "body": "Replying to [comment:14 cremona]:\n> Patch applies fine to 4.6.alpha1 +  #9898 + #9753.\n> \n> Tests all pass on a 32-bit machine.\n> \n> In the patch:  \n> \n>     1. Is the first line of docstring of ideallist() a typo:   \"Vector of vectors `L` of all idealstar of all ideals of `norm <= bound`. \" ?  Or are you using \"idealstar\" in a PARI-technical sense of \"ideal structure with extra data?\nYes, it is meant in that sense.  That help is copied from the PARI help.\n\n>     2. Can you explain the quotes in the patch to maps.py (e.g. \"'x\")\nIt means the actual *variables* `x` and `y`, even if `x` and `y` have been assigned to something.  For example, try the following in `gp`:\n\n```\ngp> x = 10\n%1 = 10\ngp> x\n%2 = 10\ngp> 'x\n%3 = x\n```\n\n\n>     3. I would not have minded if you had removed my old smallest_integer code instead of commenting it out!\nWell, it doesn't hurt to leave to code for now, in case something breaks.",
    "created_at": "2010-09-27T10:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36588",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 cremona]:
> Patch applies fine to 4.6.alpha1 +  #9898 + #9753.
> 
> Tests all pass on a 32-bit machine.
> 
> In the patch:  
> 
>     1. Is the first line of docstring of ideallist() a typo:   "Vector of vectors `L` of all idealstar of all ideals of `norm <= bound`. " ?  Or are you using "idealstar" in a PARI-technical sense of "ideal structure with extra data?
Yes, it is meant in that sense.  That help is copied from the PARI help.

>     2. Can you explain the quotes in the patch to maps.py (e.g. "'x")
It means the actual *variables* `x` and `y`, even if `x` and `y` have been assigned to something.  For example, try the following in `gp`:

```
gp> x = 10
%1 = 10
gp> x
%2 = 10
gp> 'x
%3 = x
```


>     3. I would not have minded if you had removed my old smallest_integer code instead of commenting it out!
Well, it doesn't hurt to leave to code for now, in case something breaks.



---

archive/issue_comments_036589.json:
```json
{
    "body": "OK -- good to have these explanations on the ticket, even though they do not affect the positive review.",
    "created_at": "2010-09-27T10:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36589",
    "user": "https://github.com/JohnCremona"
}
```

OK -- good to have these explanations on the ticket, even though they do not affect the positive review.



---

archive/issue_comments_036590.json:
```json
{
    "body": "Could someone fix this docbuild warning\n\n```\ndocstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\\\ntart-string without end-string.\n```\n\n?",
    "created_at": "2010-09-28T10:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36590",
    "user": "https://github.com/qed777"
}
```

Could someone fix this docbuild warning

```
docstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\
tart-string without end-string.
```

?



---

archive/issue_comments_036591.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T10:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36591",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_036592.json:
```json
{
    "body": "Attachment [4836_pari_getattr.patch](tarball://root/attachments/some-uuid/ticket4836/4836_pari_getattr.patch) by @jdemeyer created at 2010-09-28 10:56:15",
    "created_at": "2010-09-28T10:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36592",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [4836_pari_getattr.patch](tarball://root/attachments/some-uuid/ticket4836/4836_pari_getattr.patch) by @jdemeyer created at 2010-09-28 10:56:15



---

archive/issue_comments_036593.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T10:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36593",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_036594.json:
```json
{
    "body": "Replying to [comment:17 mpatel]:\n> Could someone fix this docbuild warning\n> {{{\n> docstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\\\n> tart-string without end-string.\n> }}}\n> ?\n\nDone.",
    "created_at": "2010-09-28T10:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36594",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:17 mpatel]:
> Could someone fix this docbuild warning
> {{{
> docstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\
> tart-string without end-string.
> }}}
> ?

Done.



---

archive/issue_comments_036595.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T11:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4836#issuecomment-36595",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_011110.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T11:05:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4836",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4836#event-11110"
}
```
