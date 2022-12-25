# Issue 6093: [with patch, needs review] module to read ext_rep format of combinatorial designs

archive/issues_006093.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nAdds documentation and doctests to the pydesign module ext_rep for reading combinatorial designs from http://designtheory.org/database/\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6093\n\n",
    "created_at": "2009-05-20T08:16:47Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] module to read ext_rep format of combinatorial designs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6093",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```
Assignee: @wdjoyner

Adds documentation and doctests to the pydesign module ext_rep for reading combinatorial designs from http://designtheory.org/database/


Issue created by migration from https://trac.sagemath.org/ticket/6093





---

archive/issue_comments_048454.json:
```json
{
    "body": "In at least 2 of the docstrings there are comments after an example which state \"# not tested\".\nCan you explain what this means? Do you mean \" # optional - requires internet\"?",
    "created_at": "2009-06-01T02:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48454",
    "user": "https://github.com/wdjoyner"
}
```

In at least 2 of the docstrings there are comments after an example which state "# not tested".
Can you explain what this means? Do you mean " # optional - requires internet"?



---

archive/issue_comments_048455.json:
```json
{
    "body": "Attachment [extrep.patch](tarball://root/attachments/some-uuid/ticket6093/extrep.patch) by carlohamalainen created at 2009-06-01 08:09:23",
    "created_at": "2009-06-01T08:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48455",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```

Attachment [extrep.patch](tarball://root/attachments/some-uuid/ticket6093/extrep.patch) by carlohamalainen created at 2009-06-01 08:09:23



---

archive/issue_comments_048456.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> In at least 2 of the docstrings there are comments after an example which state \"# not tested\".\n> Can you explain what this means? Do you mean \" # optional - requires internet\"?\n\nI did mean \"optional - requires internet\". I've updated the patch.",
    "created_at": "2009-06-01T08:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48456",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```

Replying to [comment:2 wdj]:
> In at least 2 of the docstrings there are comments after an example which state "# not tested".
> Can you explain what this means? Do you mean " # optional - requires internet"?

I did mean "optional - requires internet". I've updated the patch.



---

archive/issue_comments_048457.json:
```json
{
    "body": "Also, I get the following test failure:\n\n\n```\nwdj@hera:~/sagefiles/sage-4.0.rc1$ ./sage -t  \"devel/sage/sage/combinat/designs/ext_rep.py\"                                                                                       \nsage -t  \"devel/sage/sage/combinat/designs/ext_rep.py\"                                   \n**********************************************************************                   \nFile \"/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py\", line 464:                                                                                    \n    sage: file_loc = dump_to_tmpfile(\"boo\")                                              \nException raised:                                                                        \n    Traceback (most recent call last):                                                   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test                                                                                 \n        self.run_one_example(test, example, filename, compileflags)                      \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example                                                                               \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example                                                                              \n        compileflags, 1) in test.globs                                                   \n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>                        \n        file_loc = dump_to_tmpfile(\"boo\")###line 464:                                    \n    sage: file_loc = dump_to_tmpfile(\"boo\")                                              \n    NameError: name 'dump_to_tmpfile' is not defined                                     \n**********************************************************************                   \nFile \"/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py\", line 465:                                                                                    \n    sage: os.remove(file_loc)                                                            \nException raised:                                                                        \n    Traceback (most recent call last):                                                   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test                                                                                 \n        self.run_one_example(test, example, filename, compileflags)                      \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example                                                                               \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example                                                                              \n        compileflags, 1) in test.globs                                                   \n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>                        \n        os.remove(file_loc)###line 465:                                                  \n    sage: os.remove(file_loc)                                                            \n    NameError: name 'file_loc' is not defined                                            \n**********************************************************************                   \nFile \"/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py\", line 481:                                                                                    \n    sage: check_dtrs_protocols('source', '2.0')                                          \nException raised:                                                                        \n    Traceback (most recent call last):                                                   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test                                                                                 \n        self.run_one_example(test, example, filename, compileflags)                      \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example                                                                               \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example                                                                              \n        compileflags, 1) in test.globs                                                   \n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>                        \n        check_dtrs_protocols('source', '2.0')###line 481:                                \n    sage: check_dtrs_protocols('source', '2.0')                                          \n    NameError: name 'check_dtrs_protocols' is not defined                                \n**********************************************************************                   \nFile \"/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/sage/combinat/designs/ext_rep.py\", line 482:                                                                                    \n    sage: check_dtrs_protocols('source', '3.0')                                          \nExpected:                                                                                \n    Traceback (most recent call last):                                                   \n    ...                                                                                  \n    RuntimeError: Incompatible dtrs_protocols: program: 2.0 source: 3.0                  \nGot:                                                                                     \n    Traceback (most recent call last):                                                   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test                                                                                 \n        self.run_one_example(test, example, filename, compileflags)                      \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example                                                                               \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)   \n      File \"/home/wdj/sagefiles/sage-4.0.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example                                                                              \n        compileflags, 1) in test.globs                                                   \n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        check_dtrs_protocols('source', '3.0')###line 482:\n    sage: check_dtrs_protocols('source', '3.0')\n    NameError: name 'check_dtrs_protocols' is not defined\n**********************************************************************\n2 items had failures:\n   2 of   4 in __main__.example_2\n   2 of   4 in __main__.example_3\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/wdj/sagefiles/sage-4.0.rc1/tmp/.doctest_ext_rep.py\n         [2.5 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/combinat/designs/ext_rep.py\"\nTotal time for all tests: 2.5 seconds\n\n```\n\nDoes your new patch fix this too?",
    "created_at": "2009-06-01T10:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48457",
    "user": "https://github.com/wdjoyner"
}
```

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

archive/issue_comments_048458.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> Also, I get the following test failure:\n> ...\n> Does your new patch fix this too?\n\nYes, all doctests now pass.",
    "created_at": "2009-06-02T09:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48458",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```

Replying to [comment:4 wdj]:
> Also, I get the following test failure:
> ...
> Does your new patch fix this too?

Yes, all doctests now pass.



---

archive/issue_comments_048459.json:
```json
{
    "body": "This patch applies cleanly to 4.0.1.a0, passes sage -testall (the only error is that in html.py already reported by Marshall Hampton), and sage -docbuild reference html produces no errors. Also, it adds useful functionality (IMHO) and more-or-less completes the \"porting\" of pydesign's functionality to Sage.",
    "created_at": "2009-06-02T23:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48459",
    "user": "https://github.com/wdjoyner"
}
```

This patch applies cleanly to 4.0.1.a0, passes sage -testall (the only error is that in html.py already reported by Marshall Hampton), and sage -docbuild reference html produces no errors. Also, it adds useful functionality (IMHO) and more-or-less completes the "porting" of pydesign's functionality to Sage.



---

archive/issue_comments_048460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T20:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48460",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006345.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-03T20:28:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6093#event-6345"
}
```



---

archive/issue_comments_048461.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T20:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48461",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc0.



---

archive/issue_comments_048462.json:
```json
{
    "body": "Bad ReST formatting in the patch. This should be addressed in #6239.",
    "created_at": "2009-06-07T06:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6093#issuecomment-48462",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Bad ReST formatting in the patch. This should be addressed in #6239.
