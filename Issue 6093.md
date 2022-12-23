# Issue 6093: [with patch, needs review] module to read ext_rep format of combinatorial designs

Issue created by migration from https://trac.sagemath.org/ticket/6093

Original creator: carlohamalainen

Original creation time: 2009-05-20 08:16:47

Assignee: wdj

Adds documentation and doctests to the pydesign module ext_rep for reading combinatorial designs from http://designtheory.org/database/



---

Comment by wdj created at 2009-06-01 02:29:19

In at least 2 of the docstrings there are comments after an example which state "# not tested".
Can you explain what this means? Do you mean " # optional - requires internet"?


---

Attachment


---

Comment by carlohamalainen created at 2009-06-01 08:10:30

Replying to [comment:2 wdj]:
> In at least 2 of the docstrings there are comments after an example which state "# not tested".
> Can you explain what this means? Do you mean " # optional - requires internet"?

I did mean "optional - requires internet". I've updated the patch.


---

Comment by wdj created at 2009-06-01 10:51:15

Also, I get the following test failure:


```
wdj@hera:~/sagefiles/sage-4.0.rc1$ ./sage -t  "devel/sage/sage/combinat/designs/ext_rep.py"                                                                                       
sage -t  "devel/sage/sage/combinat/designs/ext_rep.py"                                   
**********************************************************************                   
File "/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py", line 464:                                                                                    
    sage: file_loc = dump_to_tmpfile("boo")                                              
Exception raised:                                                                        
    Traceback (most recent call last):                                                   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test                                                                                 
        self.run_one_example(test, example, filename, compileflags)                      
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py", line 38, in run_one_example                                                                               
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example                                                                              
        compileflags, 1) in test.globs                                                   
      File "<doctest __main__.example_2[2]>", line 1, in <module>                        
        file_loc = dump_to_tmpfile("boo")###line 464:                                    
    sage: file_loc = dump_to_tmpfile("boo")                                              
    NameError: name 'dump_to_tmpfile' is not defined                                     
**********************************************************************                   
File "/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py", line 465:                                                                                    
    sage: os.remove(file_loc)                                                            
Exception raised:                                                                        
    Traceback (most recent call last):                                                   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test                                                                                 
        self.run_one_example(test, example, filename, compileflags)                      
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py", line 38, in run_one_example                                                                               
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example                                                                              
        compileflags, 1) in test.globs                                                   
      File "<doctest __main__.example_2[3]>", line 1, in <module>                        
        os.remove(file_loc)###line 465:                                                  
    sage: os.remove(file_loc)                                                            
    NameError: name 'file_loc' is not defined                                            
**********************************************************************                   
File "/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py", line 481:                                                                                    
    sage: check_dtrs_protocols('source', '2.0')                                          
Exception raised:                                                                        
    Traceback (most recent call last):                                                   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test                                                                                 
        self.run_one_example(test, example, filename, compileflags)                      
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py", line 38, in run_one_example                                                                               
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example                                                                              
        compileflags, 1) in test.globs                                                   
      File "<doctest __main__.example_3[2]>", line 1, in <module>                        
        check_dtrs_protocols('source', '2.0')###line 481:                                
    sage: check_dtrs_protocols('source', '2.0')                                          
    NameError: name 'check_dtrs_protocols' is not defined                                
**********************************************************************                   
File "/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py", line 482:                                                                                    
    sage: check_dtrs_protocols('source', '3.0')                                          
Expected:                                                                                
    Traceback (most recent call last):                                                   
    ...                                                                                  
    RuntimeError: Incompatible dtrs_protocols: program: 2.0 source: 3.0                  
Got:                                                                                     
    Traceback (most recent call last):                                                   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test                                                                                 
        self.run_one_example(test, example, filename, compileflags)                      
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py", line 38, in run_one_example                                                                               
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   
      File "/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example                                                                              
        compileflags, 1) in test.globs                                                   
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        check_dtrs_protocols('source', '3.0')###line 482:
    sage: check_dtrs_protocols('source', '3.0')
    NameError: name 'check_dtrs_protocols' is not defined
**********************************************************************
2 items had failures:
   2 of   4 in __main__.example_2
   2 of   4 in __main__.example_3
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.0.rc1/tmp/.doctest_ext_rep.py
         [2.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/combinat/designs/ext_rep.py"
Total time for all tests: 2.5 seconds

```

Does your new patch fix this too?


---

Comment by carlohamalainen created at 2009-06-02 09:06:18

Replying to [comment:4 wdj]:
> Also, I get the following test failure:
> ...
> Does your new patch fix this too?

Yes, all doctests now pass.


---

Comment by wdj created at 2009-06-02 23:58:31

This patch applies cleanly to 4.0.1.a0, passes sage -testall (the only error is that in html.py already reported by Marshall Hampton), and sage -docbuild reference html produces no errors. Also, it adds useful functionality (IMHO) and more-or-less completes the "porting" of pydesign's functionality to Sage.


---

Comment by mhansen created at 2009-06-03 20:28:12

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 20:28:12

Merged in 4.0.1.rc0.


---

Comment by mvngu created at 2009-06-07 06:12:47

Bad ReST formatting in the patch. This should be addressed in #6239.
