# Issue 4836: pari types getattr() function ugly and inefficient

Issue created by migration from https://trac.sagemath.org/ticket/4836

Original creator: cremona

Original creation time: 2008-12-20 12:08:49

Assignee: tbd

CC:  jdemeyer

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


---

Comment by AlexGhitza created at 2009-07-11 11:15:46

Changing assignee from tbd to was.


---

Comment by AlexGhitza created at 2009-07-11 11:15:46

Changing component from algebra to interfaces.


---

Comment by jdemeyer created at 2010-08-04 07:37:13

This can be dealt with after #9343 has been merged.  PARI 2.4 has functions like nf_get_zk() which do exactly that.


---

Comment by jdemeyer created at 2010-08-15 12:19:14

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

Comment by jdemeyer created at 2010-09-19 20:30:55

Changing keywords from "" to "pari gp getattr".


---

Comment by jdemeyer created at 2010-09-19 20:41:19

Still needs some polishing but the essence of this patch is done.


---

Comment by jdemeyer created at 2010-09-19 20:41:19

Changing status from new to needs_work.


---

Comment by jdemeyer created at 2010-09-24 21:07:41

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-25 15:45:57

I just realized I have not yet done any tests on a 32-bit system.  I will do a `make testlong` on a 32-bit OS X 10.4 PPC system.


---

Comment by cremona created at 2010-09-25 16:05:12

Replying to [comment:11 jdemeyer]:

I'm about to test on a 32-bit machine as well.


---

Comment by cremona created at 2010-09-26 14:16:02

Patch applies fine to 4.6.alpha1 +  #9898 + #9753.

Tests all pass on a 32-bit machine.

In the patch:  

    1. Is the first line of docstring of ideallist() a typo:   "Vector of vectors `L` of all idealstar of all ideals of `norm <= bound`. " ?  Or are you using "idealstar" in a PARI-technical sense of "ideal structure with extra data?
    2. Can you explain the quotes in the patch to maps.py (e.g. "'x") 
    3. I would not have minded if you had removed my old smallest_integer code instead of commenting it out!

Positive review!  Thanks for doing this.  (Did you deal with all occurrences of getattr()?)


---

Comment by cremona created at 2010-09-26 14:16:02

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-27 10:07:30

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

Comment by cremona created at 2010-09-27 10:40:11

OK -- good to have these explanations on the ticket, even though they do not affect the positive review.


---

Comment by mpatel created at 2010-09-28 10:14:02

Could someone fix this docbuild warning

```
docstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\
tart-string without end-string.
```

?


---

Comment by mpatel created at 2010-09-28 10:14:02

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2010-09-28 10:56:55

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-09-28 10:56:55

Replying to [comment:17 mpatel]:
> Could someone fix this docbuild warning
> {{{
> docstring of sage.libs.pari.gen.gen.nf_get_sign:1: (WARNING/2) Inline literal s\
> tart-string without end-string.
> }}}
> ?

Done.


---

Comment by mpatel created at 2010-09-28 11:05:18

Resolution: fixed
