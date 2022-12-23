# Issue 6186: two probably-easy-to-fix scope bugs

Issue created by migration from https://trac.sagemath.org/ticket/6186

Original creator: was

Original creation time: 2009-06-02 15:18:50

Assignee: cwitty

CC:  roed


```
sage: version()
'Sage Version 4.0, Release Date: 2009-05-29'

sage: G =  Algebras(CC); G.category()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call
last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/57209/
_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/categories/
category.pyc in category(self)
   172
   173     def category(self):
--> 174         return Objects()
   175
   176 def is_Category(x):

NameError: global name 'Objects' is not defined


An other;

sage: k = Qp(13);f.<a> = k.extension(x^2+1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call
last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/57209/
_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/
padic_generic.pyc in extension(self, modulus, prec, names, print_mode,
halt, **kwds)
   463                     else:
   464                         print_mode[option] = self._printer.dict
()[option]
--> 465         return ExtensionFactory(base=self, premodulus=modulus,
prec=prec, halt=halt, names=names, check = True, **print_mode)
   466
   467 def local_print_mode(obj, print_options, pos = None, ram_name
# None):

/Applications/sage/local/lib/python2.5/site-packages/sage/structure/
factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/
structure/factory.c:761)()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/
factory.pyc in create_key_and_extra_args(self, base, premodulus, prec,
print_mode, halt, names, var_name, res_name, unram_name, ram_name,
print_pos, print_sep, print_alphabet, print_max_ram_terms,
print_max_unram_terms, print_max_terse_terms, check, unram)
  2261             key = (polytype, base, premodulus, modulus, names,
prec, halt, print_mode, print_pos, print_sep, tuple(print_alphabet),
print_max_ram_terms, print_max_unram_terms, print_max_terse_terms)
  2262         else:
-> 2263             upoly, epoly, prec = split(modulus, prec)
  2264             key = (polytype, base, premodulus, upoly, epoly,
names, prec, halt, print_mode, print_pos, print_sep, tuple
(print_alphabet), print_max_ram_terms, print_max_unram_terms,
print_max_terse_terms)
  2265         return key, {'shift_seed': shift_seed}

NameError: global name 'split' is not defined
```



---

Comment by nthiery created at 2009-06-15 08:26:51

The first one is readily fixed by the category patches #5891. Please don't fix it separately so as not to create a conflict!


---

Comment by was created at 2009-06-15 13:23:41

> Please don't fix it separately so as not to create a conflict! 

I really hope categories gets in ASAP.  Last time you told me not to fix something because it would conflict with that patch, was almost two months ago (I'm glad I didn't listen).  This time I will listen though...

William


---

Comment by craigcitro created at 2010-05-14 02:54:38

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-05-14 02:54:38

I'm attaching a fix for the second error above -- the `split` function was in the file, but commented out. I confirmed with David Roe that it should, indeed, be uncommented still (because we still don't have an implementation of Round4 in Sage). 

Amusingly, this was debugged during our Math 480 class -- successfully, though saying "oh, it's going to raise a different error" was probably a little unsatisfying.

The other error in the description is indeed fixed.


---

Comment by cwitty created at 2010-07-11 00:40:55

Changing status from needs_review to positive_review.


---

Attachment

Positive review.  Patch applies, doctests pass.

Note that this ticket has two separate bug reports; the first bug was already fixed (presumably, as nthiery promised, by the category patches).  trac-6186.patch fixes the second.


---

Comment by ddrake created at 2010-07-22 07:34:41

Resolution: fixed
