# Issue 6204: make norms for degree 1 relative number fields work; add doctests

Issue created by migration from https://trac.sagemath.org/ticket/6204

Original creator: ncalexan

Original creation time: 2009-06-04 03:36:11

Assignee: was

CC:  craigcitro fwclarke

Keywords: degree 1 relative number field norm

This small patch makes norms for degree 1 relative number fields avoid pari, which fails (in our old version) in this case.  I also added a doctest or two.


---

Attachment


---

Comment by craigcitro created at 2009-06-04 23:17:48

This looks good. Points for adding doctests to a bunch of functions, not just the ones you happened to add code to.

On a related note, should we start a wiki page or something with all the workarounds we can remove once we update to a modern Pari?


---

Comment by davidloeffler created at 2009-06-08 10:50:48

This conflicts with my patch at #6188 (but only in a fairly harmless way). I have prepared a rebased patch, which also corrects a few minor indentation errors in the new docstrings, which I will upload once I've checked that the reference manual builds OK.


---

Comment by davidloeffler created at 2009-06-08 11:08:44

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

Comment by fwclarke created at 2009-06-11 07:28:03

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

Comment by fwclarke created at 2009-06-11 07:29:57

Replying to [ticket:6204 ncalexan]:
> ...  I also added a doctest or two.

The doctest for `is_principal` conflicts somewhat with changes in #5842.


---

Comment by davidloeffler created at 2009-07-21 08:20:40

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-21 08:20:40

Changing component from number theory to number fields.
