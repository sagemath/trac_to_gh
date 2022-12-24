# Issue 6186: two probably-easy-to-fix scope bugs

archive/issues_006186.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  roed\n\n\n```\nsage: version()\n'Sage Version 4.0, Release Date: 2009-05-29'\n\nsage: G =  Algebras(CC); G.category()\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call\nlast)\n\n/Users/jeromelefebvre/.sage/temp/Jerome.local/57209/\n_Users_jeromelefebvre__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/categories/\ncategory.pyc in category(self)\n   172\n   173     def category(self):\n--> 174         return Objects()\n   175\n   176 def is_Category(x):\n\nNameError: global name 'Objects' is not defined\n\n\nAn other;\n\nsage: k = Qp(13);f.<a> = k.extension(x^2+1)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call\nlast)\n\n/Users/jeromelefebvre/.sage/temp/Jerome.local/57209/\n_Users_jeromelefebvre__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/\npadic_generic.pyc in extension(self, modulus, prec, names, print_mode,\nhalt, **kwds)\n   463                     else:\n   464                         print_mode[option] = self._printer.dict\n()[option]\n--> 465         return ExtensionFactory(base=self, premodulus=modulus,\nprec=prec, halt=halt, names=names, check = True, **print_mode)\n   466\n   467 def local_print_mode(obj, print_options, pos = None, ram_name\n# None):\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/structure/\nfactory.so in sage.structure.factory.UniqueFactory.__call__ (sage/\nstructure/factory.c:761)()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/\nfactory.pyc in create_key_and_extra_args(self, base, premodulus, prec,\nprint_mode, halt, names, var_name, res_name, unram_name, ram_name,\nprint_pos, print_sep, print_alphabet, print_max_ram_terms,\nprint_max_unram_terms, print_max_terse_terms, check, unram)\n  2261             key = (polytype, base, premodulus, modulus, names,\nprec, halt, print_mode, print_pos, print_sep, tuple(print_alphabet),\nprint_max_ram_terms, print_max_unram_terms, print_max_terse_terms)\n  2262         else:\n-> 2263             upoly, epoly, prec = split(modulus, prec)\n  2264             key = (polytype, base, premodulus, upoly, epoly,\nnames, prec, halt, print_mode, print_pos, print_sep, tuple\n(print_alphabet), print_max_ram_terms, print_max_unram_terms,\nprint_max_terse_terms)\n  2265         return key, {'shift_seed': shift_seed}\n\nNameError: global name 'split' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6186\n\n",
    "created_at": "2009-06-02T15:18:50Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "two probably-easy-to-fix scope bugs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6186",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/6186





---

archive/issue_comments_049386.json:
```json
{
    "body": "The first one is readily fixed by the category patches #5891. Please don't fix it separately so as not to create a conflict!",
    "created_at": "2009-06-15T08:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49386",
    "user": "nthiery"
}
```

The first one is readily fixed by the category patches #5891. Please don't fix it separately so as not to create a conflict!



---

archive/issue_comments_049387.json:
```json
{
    "body": "> Please don't fix it separately so as not to create a conflict! \n\nI really hope categories gets in ASAP.  Last time you told me not to fix something because it would conflict with that patch, was almost two months ago (I'm glad I didn't listen).  This time I will listen though...\n\nWilliam",
    "created_at": "2009-06-15T13:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49387",
    "user": "was"
}
```

> Please don't fix it separately so as not to create a conflict! 

I really hope categories gets in ASAP.  Last time you told me not to fix something because it would conflict with that patch, was almost two months ago (I'm glad I didn't listen).  This time I will listen though...

William



---

archive/issue_comments_049388.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-14T02:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49388",
    "user": "craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049389.json:
```json
{
    "body": "I'm attaching a fix for the second error above -- the `split` function was in the file, but commented out. I confirmed with David Roe that it should, indeed, be uncommented still (because we still don't have an implementation of Round4 in Sage). \n\nAmusingly, this was debugged during our Math 480 class -- successfully, though saying \"oh, it's going to raise a different error\" was probably a little unsatisfying.\n\nThe other error in the description is indeed fixed.",
    "created_at": "2010-05-14T02:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49389",
    "user": "craigcitro"
}
```

I'm attaching a fix for the second error above -- the `split` function was in the file, but commented out. I confirmed with David Roe that it should, indeed, be uncommented still (because we still don't have an implementation of Round4 in Sage). 

Amusingly, this was debugged during our Math 480 class -- successfully, though saying "oh, it's going to raise a different error" was probably a little unsatisfying.

The other error in the description is indeed fixed.



---

archive/issue_comments_049390.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-11T00:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49390",
    "user": "cwitty"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049391.json:
```json
{
    "body": "Attachment [trac-6186.patch](tarball://root/attachments/some-uuid/ticket6186/trac-6186.patch) by cwitty created at 2010-07-11 00:40:55\n\nPositive review.  Patch applies, doctests pass.\n\nNote that this ticket has two separate bug reports; the first bug was already fixed (presumably, as nthiery promised, by the category patches).  trac-6186.patch fixes the second.",
    "created_at": "2010-07-11T00:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49391",
    "user": "cwitty"
}
```

Attachment [trac-6186.patch](tarball://root/attachments/some-uuid/ticket6186/trac-6186.patch) by cwitty created at 2010-07-11 00:40:55

Positive review.  Patch applies, doctests pass.

Note that this ticket has two separate bug reports; the first bug was already fixed (presumably, as nthiery promised, by the category patches).  trac-6186.patch fixes the second.



---

archive/issue_comments_049392.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6186#issuecomment-49392",
    "user": "ddrake"
}
```

Resolution: fixed
