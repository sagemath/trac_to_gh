# Issue 6204: [with patch, needs work] make norms for degree 1 relative number fields work; add doctests

archive/issues_006204.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @craigcitro fwclarke\n\nKeywords: degree 1 relative number field norm\n\nThis small patch makes norms for degree 1 relative number fields avoid pari, which fails (in our old version) in this case.  I also added a doctest or two.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6204\n\n",
    "created_at": "2009-06-04T03:36:11Z",
    "labels": [
        "component: number fields"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs work] make norms for degree 1 relative number fields work; add doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6204",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @loefflerd

CC:  @craigcitro fwclarke

Keywords: degree 1 relative number field norm

This small patch makes norms for degree 1 relative number fields avoid pari, which fails (in our old version) in this case.  I also added a doctest or two.

Issue created by migration from https://trac.sagemath.org/ticket/6204





---

archive/issue_comments_049472.json:
```json
{
    "body": "Attachment [trac_6204-degree-1-relative-norms.patch](tarball://root/attachments/some-uuid/ticket6204/trac_6204-degree-1-relative-norms.patch) by @ncalexan created at 2009-06-04 03:38:03",
    "created_at": "2009-06-04T03:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49472",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6204-degree-1-relative-norms.patch](tarball://root/attachments/some-uuid/ticket6204/trac_6204-degree-1-relative-norms.patch) by @ncalexan created at 2009-06-04 03:38:03



---

archive/issue_comments_049473.json:
```json
{
    "body": "This looks good. Points for adding doctests to a bunch of functions, not just the ones you happened to add code to.\n\nOn a related note, should we start a wiki page or something with all the workarounds we can remove once we update to a modern Pari?",
    "created_at": "2009-06-04T23:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49473",
    "user": "https://github.com/craigcitro"
}
```

This looks good. Points for adding doctests to a bunch of functions, not just the ones you happened to add code to.

On a related note, should we start a wiki page or something with all the workarounds we can remove once we update to a modern Pari?



---

archive/issue_comments_049474.json:
```json
{
    "body": "This conflicts with my patch at #6188 (but only in a fairly harmless way). I have prepared a rebased patch, which also corrects a few minor indentation errors in the new docstrings, which I will upload once I've checked that the reference manual builds OK.",
    "created_at": "2009-06-08T10:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49474",
    "user": "https://github.com/loefflerd"
}
```

This conflicts with my patch at #6188 (but only in a fairly harmless way). I have prepared a rebased patch, which also corrects a few minor indentation errors in the new docstrings, which I will upload once I've checked that the reference manual builds OK.



---

archive/issue_comments_049475.json:
```json
{
    "body": "Hold it, this fails doctests under 4.0.1:\n\n```\ndavid@groke:~/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field> sage -t number_field_ideal_rel.py\nsage -t  \"devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py\"                           \n**********************************************************************                                    \nFile \"/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py\", line 361:\n    sage: L.ideal(b).relative_norm()                                                                             \nException raised:                                                                                                \n    Traceback (most recent call last):                                                                           \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1231, in run_one_test                            \n        self.run_one_example(test, example, filename, compileflags)                                              \n      File \"/home/david/sage-4.0/local/bin/sagedoctest.py\", line 38, in run_one_example                          \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                           \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1172, in run_one_example                         \n        compileflags, 1) in test.globs                                                                           \n      File \"<doctest __main__.example_11[19]>\", line 1, in <module>                                              \n        L.ideal(b).relative_norm()###line 361:                                                                   \n    sage: L.ideal(b).relative_norm()                                                                             \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py\", line 370, in relative_norm                                                                                   \n        return K.ideal(map(K, self.gens()))                                                                          \n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           \n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  \n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 941, in _element_constructor_                                                                                     \n        return self._coerce_from_other_number_field(x)                                                               \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4317, in _coerce_from_other_number_field                                                                          \n        raise TypeError, \"Cannot coerce element into this number field\"                                              \n    TypeError: Cannot coerce element into this number field                                                          \n**********************************************************************                                               \nFile \"/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py\", line 480:    \n    sage: L.ideal(b).ideal_below()                                                                                   \nException raised:                                                                                                    \n    Traceback (most recent call last):                                                                               \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1231, in run_one_test                                \n        self.run_one_example(test, example, filename, compileflags)                                                  \n      File \"/home/david/sage-4.0/local/bin/sagedoctest.py\", line 38, in run_one_example                              \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                               \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1172, in run_one_example                             \n        compileflags, 1) in test.globs                                                                               \n      File \"<doctest __main__.example_13[50]>\", line 1, in <module>                                                  \n        L.ideal(b).ideal_below()###line 480:                                                                         \n    sage: L.ideal(b).ideal_below()                                                                                   \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py\", line 489, in ideal_below                                                                                     \n        return K.ideal(map(K, self.gens()))                                                                          \n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           \n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  \n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 941, in _element_constructor_                                                                                     \n        return self._coerce_from_other_number_field(x)                                                               \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4317, in _coerce_from_other_number_field                                                                          \n        raise TypeError, \"Cannot coerce element into this number field\"                                              \n    TypeError: Cannot coerce element into this number field                                                          \n**********************************************************************                                               \nFile \"/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py\", line 482:    \n    sage: L.ideal(b^2 + 2).ideal_below()                                                                             \nException raised:                                                                                                    \n    Traceback (most recent call last):                                                                               \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1231, in run_one_test                                \n        self.run_one_example(test, example, filename, compileflags)                                                  \n      File \"/home/david/sage-4.0/local/bin/sagedoctest.py\", line 38, in run_one_example                              \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                               \n      File \"/home/david/sage-4.0/local/bin/ncadoctest.py\", line 1172, in run_one_example                             \n        compileflags, 1) in test.globs                                                                               \n      File \"<doctest __main__.example_13[51]>\", line 1, in <module>                                                  \n        L.ideal(b**Integer(2) + Integer(2)).ideal_below()###line 482:                                                \n    sage: L.ideal(b^2 + 2).ideal_below()                                                                             \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py\", line 489, in ideal_below                                                                                     \n        return K.ideal(map(K, self.gens()))                                                                          \n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           \n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  \n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 941, in _element_constructor_                                                                                     \n        return self._coerce_from_other_number_field(x)                                                               \n      File \"/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4317, in _coerce_from_other_number_field                                                                          \n        raise TypeError, \"Cannot coerce element into this number field\"                                              \n    TypeError: Cannot coerce element into this number field                                                          \n**********************************************************************                                               \n2 items had failures:                                                                                                \n   1 of  21 in __main__.example_11                                                                                   \n   2 of  52 in __main__.example_13                                                                                   \n***Test Failed*** 3 failures.                                                                                        \nFor whitespace errors, see the file /home/david/sage-4.0.1.rc2/tmp/.doctest_number_field_ideal_rel.py                \n         [6.2 s]                                                                                                     \nexit code: 1024                                                                                                      \n                                                                                                                     \n----------------------------------------------------------------------                                               \nThe following tests failed:                                                                                          \n\n\n        sage -t  \"devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py\"\nTotal time for all tests: 6.2 seconds                                                  \n```\n\nI'm changing this back to \"needs work\". The problem seems to be that we need to work around a pari bug in \"gens_reduced\" as well as in \"relative_norm\".",
    "created_at": "2009-06-08T11:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49475",
    "user": "https://github.com/loefflerd"
}
```

Hold it, this fails doctests under 4.0.1:

```
david@groke:~/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field> sage -t number_field_ideal_rel.py
sage -t  "devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py"                           
**********************************************************************                                    
File "/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py", line 361:
    sage: L.ideal(b).relative_norm()                                                                             
Exception raised:                                                                                                
    Traceback (most recent call last):                                                                           
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test                            
        self.run_one_example(test, example, filename, compileflags)                                              
      File "/home/david/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example                          
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                           
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example                         
        compileflags, 1) in test.globs                                                                           
      File "<doctest __main__.example_11[19]>", line 1, in <module>                                              
        L.ideal(b).relative_norm()###line 361:                                                                   
    sage: L.ideal(b).relative_norm()                                                                             
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py", line 370, in relative_norm                                                                                   
        return K.ideal(map(K, self.gens()))                                                                          
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 941, in _element_constructor_                                                                                     
        return self._coerce_from_other_number_field(x)                                                               
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4317, in _coerce_from_other_number_field                                                                          
        raise TypeError, "Cannot coerce element into this number field"                                              
    TypeError: Cannot coerce element into this number field                                                          
**********************************************************************                                               
File "/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py", line 480:    
    sage: L.ideal(b).ideal_below()                                                                                   
Exception raised:                                                                                                    
    Traceback (most recent call last):                                                                               
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test                                
        self.run_one_example(test, example, filename, compileflags)                                                  
      File "/home/david/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example                              
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                               
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example                             
        compileflags, 1) in test.globs                                                                               
      File "<doctest __main__.example_13[50]>", line 1, in <module>                                                  
        L.ideal(b).ideal_below()###line 480:                                                                         
    sage: L.ideal(b).ideal_below()                                                                                   
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py", line 489, in ideal_below                                                                                     
        return K.ideal(map(K, self.gens()))                                                                          
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 941, in _element_constructor_                                                                                     
        return self._coerce_from_other_number_field(x)                                                               
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4317, in _coerce_from_other_number_field                                                                          
        raise TypeError, "Cannot coerce element into this number field"                                              
    TypeError: Cannot coerce element into this number field                                                          
**********************************************************************                                               
File "/home/david/sage-4.0.1.rc2/devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py", line 482:    
    sage: L.ideal(b^2 + 2).ideal_below()                                                                             
Exception raised:                                                                                                    
    Traceback (most recent call last):                                                                               
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test                                
        self.run_one_example(test, example, filename, compileflags)                                                  
      File "/home/david/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example                              
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                               
      File "/home/david/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example                             
        compileflags, 1) in test.globs                                                                               
      File "<doctest __main__.example_13[51]>", line 1, in <module>                                                  
        L.ideal(b**Integer(2) + Integer(2)).ideal_below()###line 482:                                                
    sage: L.ideal(b^2 + 2).ideal_below()                                                                             
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py", line 489, in ideal_below                                                                                     
        return K.ideal(map(K, self.gens()))                                                                          
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)           
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)                                                                                                  
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)      
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 941, in _element_constructor_                                                                                     
        return self._coerce_from_other_number_field(x)                                                               
      File "/home/david/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4317, in _coerce_from_other_number_field                                                                          
        raise TypeError, "Cannot coerce element into this number field"                                              
    TypeError: Cannot coerce element into this number field                                                          
**********************************************************************                                               
2 items had failures:                                                                                                
   1 of  21 in __main__.example_11                                                                                   
   2 of  52 in __main__.example_13                                                                                   
***Test Failed*** 3 failures.                                                                                        
For whitespace errors, see the file /home/david/sage-4.0.1.rc2/tmp/.doctest_number_field_ideal_rel.py                
         [6.2 s]                                                                                                     
exit code: 1024                                                                                                      
                                                                                                                     
----------------------------------------------------------------------                                               
The following tests failed:                                                                                          


        sage -t  "devel/sage-nfstuff/sage/rings/number_field/number_field_ideal_rel.py"
Total time for all tests: 6.2 seconds                                                  
```

I'm changing this back to "needs work". The problem seems to be that we need to work around a pari bug in "gens_reduced" as well as in "relative_norm".



---

archive/issue_comments_049476.json:
```json
{
    "body": "Replying to [comment:3 davidloeffler]:\n> Hold it, this fails doctests under 4.0.1:\n> ... The problem seems to be that we need to work around a pari bug in \"gens_reduced\" as well as in \"relative_norm\".\n\n\nI don't think there's anything wrong with `gens_reduced`.  \n\nIt seems to be a coercion/conversion problem, caused, or at least not helped, by the behaviour of `relativize`:\n\n```\nsage: K.<a> = NumberField(x^4 + 2*x^2 + 7)\nsage: L.<b, c> = K.relativize(a + 1); L \nNumber Field in b with defining polynomial x - c + 1 over its base field\nsage: L_base = L.base_field()\nsage: L_base(b)\nTraceback (most recent call last)\n...\nTypeError: Cannot coerce element into this number field\nsage: L_base(c)\nTraceback (most recent call last)\n...\nTypeError: Cannot coerce element into this number field\nsage: parent(b) == L\nTrue\nsage: parent(c) == L\nTrue\nsage: parent(c) == L_base\nFalse\n```",
    "created_at": "2009-06-11T07:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49476",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:3 davidloeffler]:
> Hold it, this fails doctests under 4.0.1:
> ... The problem seems to be that we need to work around a pari bug in "gens_reduced" as well as in "relative_norm".


I don't think there's anything wrong with `gens_reduced`.  

It seems to be a coercion/conversion problem, caused, or at least not helped, by the behaviour of `relativize`:

```
sage: K.<a> = NumberField(x^4 + 2*x^2 + 7)
sage: L.<b, c> = K.relativize(a + 1); L 
Number Field in b with defining polynomial x - c + 1 over its base field
sage: L_base = L.base_field()
sage: L_base(b)
Traceback (most recent call last)
...
TypeError: Cannot coerce element into this number field
sage: L_base(c)
Traceback (most recent call last)
...
TypeError: Cannot coerce element into this number field
sage: parent(b) == L
True
sage: parent(c) == L
True
sage: parent(c) == L_base
False
```



---

archive/issue_comments_049477.json:
```json
{
    "body": "Replying to [ticket:6204 ncalexan]:\n> ...  I also added a doctest or two.\n\n\nThe doctest for `is_principal` conflicts somewhat with changes in #5842.",
    "created_at": "2009-06-11T07:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49477",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [ticket:6204 ncalexan]:
> ...  I also added a doctest or two.


The doctest for `is_principal` conflicts somewhat with changes in #5842.



---

archive/issue_comments_049478.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49478",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_049479.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6204#issuecomment-49479",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_events_014552.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14552"
}
```



---

archive/issue_events_014553.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14553"
}
```



---

archive/issue_events_014554.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14554"
}
```



---

archive/issue_events_014555.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14555"
}
```



---

archive/issue_events_014556.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14556"
}
```



---

archive/issue_events_014557.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14557"
}
```



---

archive/issue_events_014558.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6204",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6204#event-14558"
}
```
