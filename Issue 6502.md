# Issue 6502: [with Patch, needs review] Linear Program Solver and Mixed Integer Program Solver in SAGE

Issue created by migration from https://trac.sagemath.org/ticket/6502

Original creator: ncohen

Original creation time: 2009-07-09 16:34:48

Assignee: jkantor

CC:  schilly

Following this message on SAGE-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f

This is the class sage.numerical.mip which is meant to be the common interface between SAGE and 3 different LP solvers : GLPK, Coin-Or, and CPLEX.

For the moment, I only wrote the interface with Coin-Or, which I needed and which seems to work for simple problems. I will improve it over time, but it can already be used and I hope you will like it :-)


---

Comment by ncohen created at 2009-07-09 16:35:08

Class sage.numerical.mip


---

Attachment

If you want to try this code, you will find a short example there :

http://groups.google.com/group/sage-devel/browse_thread/thread/7c13a0a4ba3d87b6


---

Comment by carlohamalainen created at 2009-07-10 11:14:54

Compiles and installs successfully on Sage 4.0.1 on Ubuntu x86.

The methods in MIP should have doctests/docstrings. e.g. I should be able to type


```
sage: MIP.addBound?
```


and see a nice example for how to add a bound.


---

Comment by wdj created at 2009-07-10 11:49:42

I agree, this needs docstrings.

Installation of the spkg went fine on a macbook running 10.4.11. The patch seemed to apply okay. sage -testall on 4.1.rc1 passed except for failures in parallel/decorate (DeprecationWarning: os.popen2 is deprecated. ) and interfaces/sage0 (which could not be replicated).

The examples given in the sage-devel email (below) seemed to work okay, though I am not an expert on this stuff.


```
g=graphs.RandomGNP(10,.5)

p=MIP(max=True)

obj={}
for i in g.vertices():
   obj["V"+str(i)]=1
   p.setinteger("V"+str(i))
p.setobj(Constraint(obj,obj=True))
for (a,b,c) in g.edges():
   obj={}
   obj["V"+str(a)]=1
   obj["V"+str(b)]=1
   p.addconstraint(Constraint(obj,lt=1))
p.solve()
```



---

Comment by ncohen created at 2009-07-23 14:22:23

- solves LP using GLPK ( see http://trac.sagemath.org/sage_trac/ticket/6602 )
- the interface with the COIN solver has been moved to a SPKG whose link will be added here
- Doctstrings have been added
- small modifications everywhere

Patch numerical.mip-2.patch applies on top of 2428.patch

I hope you will like it !! I spent a lot of time on this LP for SAGE ! ;-)


---

Attachment


---

Comment by ncohen created at 2009-07-23 14:56:20

A small mistake in the detection of COIN -- fixed ! ;-)


---

Attachment

Once this ticket has positive review, the SPKG at #6602 should also be merged in the standard packages repository. So in a sense, that SPKG is dependent on this ticket.


---

Comment by wdj created at 2009-07-26 23:01:45

I got this problem:


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: OR2
sage: hg_sage.apply("/home/wdj/sagefiles/12428.patch")
cd "/home/wdj/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
/home/wdj/sagefiles/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 isdeprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/home/wdj/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg import   "/home/wdj/sagefiles/12428.patch"
applying /home/wdj/sagefiles/12428.patch
patching file module_list.py
Hunk #1 succeeded at 240 with fuzz 2 (offset 13 lines).
patching file sage/numerical/all.py
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/numerical/all.py.rej
abort: patch failed to apply
```

Any suggestions?


---

Comment by mvngu created at 2009-07-26 23:06:23

Replying to [comment:10 wdj]:
> I got this problem:
<SNIP>
> Any suggestions?
I suggest we wait until 4.1.1 is out.


---

Comment by ncohen created at 2009-07-30 22:50:02

New patch including all the previously announced features and probably a bit more. It encompasses the previous patches, so you need only apply this one and forget about the others ! ;-)


---

Attachment

This was applied to 4.1.1.a0 and the following test failed:


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -t  "devel/sage/sage/numerical/mip.pyx"
sage -t  "devel/sage/sage/numerical/mip.pyx"                
sh: line 1: kpsewhich: command not found
sh: line 1: kpsewhich: command not found
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 37:
    sage: p=MIP(sense=1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        p=MIP(sense=Integer(1))###line 37:
    sage: p=MIP(sense=1)
    NameError: name 'MIP' is not defined
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 39:
    sage: for i in g.vertices():
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1
         for i in g.vertices():###line 39:
    sage: for i in g.vertices():
                                                                             
    ^
     SyntaxError: unexpected EOF while parsing
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 40:
    sage:     obj[i]=1
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[6]>", line 1
         obj[i]=Integer(1)###line 40:
    sage:     obj[i]=1
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 41:
    sage:     p.setinteger(i)
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1
         p.setinteger(i)###line 41:
    sage:     p.setinteger(i)
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 42:
    sage: p.setobj(obj)
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        p.setobj(obj)###line 42:
    sage: p.setobj(obj)
    NameError: name 'p' is not defined
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 43:
    sage: for (a,b,c) in g.edges():
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1
         for (a,b,c) in g.edges():###line 43:
    sage: for (a,b,c) in g.edges():
                                                                                   
    ^
     SyntaxError: unexpected EOF while parsing
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 44:
    sage:     cons={}
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1
         cons={}###line 44:
    sage:     cons={}
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 45:
    sage:     cons[a]=1
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1
         cons[a]=Integer(1)###line 45:
    sage:     cons[a]=1
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 46:
    sage:     cons[b]=1
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1
         cons[b]=Integer(1)###line 46:
    sage:     cons[b]=1
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 47:
    sage:     p.addconstraint(cons,max=1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[13]>", line 1
         p.addconstraint(cons,max=Integer(1))###line 47:
    sage:     p.addconstraint(cons,max=1)
        ^
     IndentationError: unexpected indent
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/numerical/mip.pyx", line 48:
    sage: p.solve()
Exception raised:
    Traceback (most recent call last):
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[14]>", line 1, in <module>
        p.solve()###line 48:
    sage: p.solve()
    NameError: name 'p' is not defined
**********************************************************************
1 items had failures:
  11 of  15 in __main__.example_0
***Test Failed*** 11 failures.
For whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/tmp/.doctest_mip.py
         [4.9 s]
exit code: 1024
 
```


Does this make sense?


---

Comment by ncohen created at 2009-07-31 06:19:57

It seems Sage does not like something dealing with the indentation in the doctest of the class, as the example works when I am copying it manually... If you know the standard ( if there are any ) in this situation, please tell me because I am trying to fix this and changing the indentation ten thousand times hoping it will work is not my preferred way of debugging ^^;


---

Comment by ncohen created at 2009-07-31 06:52:04

Fixed in patch MIP-2.patch

As a sidenote, this ranks as the least interesting debugging I ever did, and I just achieved it because there was another example of a loop in a dosctring in Sage. Thanks to the brave developper of sage.combinat.dlx who conquered the docstrings ! ;-)


---

Attachment


---

Comment by wdj created at 2009-07-31 09:49:05

I usually debug by just running sage -t with the file open in an editor until it passes:-) 

Am I to apply MIP1 then MIP2? If so, there was a problem compiling (amd64, ubuntu 9.04):


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -b                                                             

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....       
Building modified file sage/numerical/mip.pyx.
python `which cython` --embed-positions --incref-local-binop -I/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage-OR -o sage/numerical/mip.cpp sage/numerical/mip.pyx                                                           
sage/numerical/mip.pyx --> /home/wdj/sagefiles/sage-4.1.1.alpha1/local//lib/python/site-packages//sage/numerical/mip.pyx                                                                                                      
Time to execute 1 commands: 0.891119003296 seconds                                                             
Finished compiling Cython code (time = 1.45167207718 seconds)                                                  
running install                                                                                                
running build                                                                                                  
running build_py                                                                                               
copying sage/numerical/all.py -> build/lib.linux-x86_64-2.6/sage/numerical                                     
running build_ext                                                                                              
building 'sage.numerical.mip' extension                                                                        
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -Ilocal/include/ -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local//include -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local//include/csage -I/home/wdj/sagefiles/sage-4.1.1.alpha1/devel//sage/sage/ext -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local/include/python2.6 -c sage/numerical/mip.cpp -o build/temp.linux-x86_64-2.6/sage/numerical/mip.o -w                         
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++            
sage/numerical/mip.cpp:132:38: error: ../../local/include/glpk.h: No such file or directory                    
sage/numerical/mip.cpp: In function ‘PyObject* __pyx_pf_4sage_9numerical_3mip_3MIP_solveGLPK(PyObject*, PyObject*, PyObject*)’:                                                                                               
sage/numerical/mip.cpp:2777: error: ‘glp_prob’ was not declared in this scope                                  
sage/numerical/mip.cpp:2777: error: ‘__pyx_v_lp’ was not declared in this scope                                
sage/numerical/mip.cpp:2787: error: ‘glp_iocp’ was not declared in this scope                                  
sage/numerical/mip.cpp:2787: error: ‘__pyx_v_iocp’ was not declared in this scope                              
sage/numerical/mip.cpp:2985: error: ‘glp_create_prob’ was not declared in this scope                           
sage/numerical/mip.cpp:2998: error: ‘glp_add_rows’ was not declared in this scope                              
sage/numerical/mip.cpp:3011: error: ‘glp_add_cols’ was not declared in this scope                              
sage/numerical/mip.cpp:3098: error: ‘glp_set_obj_coef’ was not declared in this scope                          
sage/numerical/mip.cpp:3241: error: ‘GLP_DB’ was not declared in this scope                                    
sage/numerical/mip.cpp:3241: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3330: error: ‘GLP_UP’ was not declared in this scope                                    
sage/numerical/mip.cpp:3330: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3419: error: ‘GLP_LO’ was not declared in this scope                                    
sage/numerical/mip.cpp:3419: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3450: error: ‘GLP_FR’ was not declared in this scope                                    
sage/numerical/mip.cpp:3450: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3764: error: ‘GLP_FX’ was not declared in this scope                                    
sage/numerical/mip.cpp:3764: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3791: error: ‘GLP_DB’ was not declared in this scope                                    
sage/numerical/mip.cpp:3791: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3846: error: ‘GLP_UP’ was not declared in this scope                                    
sage/numerical/mip.cpp:3846: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3899: error: ‘GLP_LO’ was not declared in this scope                                    
sage/numerical/mip.cpp:3899: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3912: error: ‘GLP_FR’ was not declared in this scope                                    
sage/numerical/mip.cpp:3912: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3957: error: ‘GLP_MIN’ was not declared in this scope                                   
sage/numerical/mip.cpp:3957: error: ‘glp_set_obj_dir’ was not declared in this scope                           
sage/numerical/mip.cpp:3969: error: ‘GLP_MAX’ was not declared in this scope                                   
sage/numerical/mip.cpp:3969: error: ‘glp_set_obj_dir’ was not declared in this scope                           
sage/numerical/mip.cpp:4059: error: ‘GLP_IV’ was not declared in this scope                                    
sage/numerical/mip.cpp:4059: error: ‘glp_set_col_kind’ was not declared in this scope                          
sage/numerical/mip.cpp:4108: error: ‘GLP_BV’ was not declared in this scope                                    
sage/numerical/mip.cpp:4108: error: ‘glp_set_col_kind’ was not declared in this scope                          
sage/numerical/mip.cpp:4136: error: ‘GLP_CV’ was not declared in this scope
sage/numerical/mip.cpp:4136: error: ‘glp_set_col_kind’ was not declared in this scope
sage/numerical/mip.cpp:4156: error: ‘glp_load_matrix’ was not declared in this scope
sage/numerical/mip.cpp:4165: error: expected type-specifier before ‘glp_iocp’
sage/numerical/mip.cpp:4165: error: expected `;' before ‘glp_iocp’
sage/numerical/mip.cpp:4174: error: ‘glp_init_iocp’ was not declared in this scope
sage/numerical/mip.cpp:4183: error: ‘GLP_ON’ was not declared in this scope
sage/numerical/mip.cpp:4205: error: ‘GLP_MSG_OFF’ was not declared in this scope
sage/numerical/mip.cpp:4229: error: ‘GLP_MSG_ERR’ was not declared in this scope
sage/numerical/mip.cpp:4253: error: ‘GLP_MSG_ON’ was not declared in this scope
sage/numerical/mip.cpp:4265: error: ‘GLP_MSG_ALL’ was not declared in this scope
sage/numerical/mip.cpp:4276: error: ‘glp_intopt’ was not declared in this scope
sage/numerical/mip.cpp:4285: error: ‘glp_mip_obj_val’ was not declared in this scope
sage/numerical/mip.cpp:4314: error: ‘glp_delete_prob’ was not declared in this scope
sage/numerical/mip.cpp:4408: error: ‘glp_mip_col_val’ was not declared in this scope
sage/numerical/mip.cpp:4422: error: ‘glp_delete_prob’ was not declared in this scope
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m3.367s
user    0m2.880s
sys     0m0.428s
```


Do you know what this means?


---

Comment by ncohen created at 2009-07-31 09:54:24

Yes, this time I know !!! ;-)

The first error is : sage/numerical/mip.cpp:132:38: error: ../../local/include/glpk.h: No such file or directory

And this is because you did not install GLPK ( http://trac.sagemath.org/sage_trac/ticket/6602 ) which is to be a standanrd package. And MIP-2 applies on top of MIP-1 !

Sorry for these details I may have forgotten ! ;-)


---

Comment by wdj created at 2009-07-31 13:07:24

These patches applies to an amd64 ubuntu 9.04 machine passes sage -testall (except for the already reported errors for sage 4.1.1.a1). 

Things are improving but there are some remaining issues:

1. There is a possible typo in the docstring for MIP:


```
        For example linear function 3 * x - 2 * y + 3 * z
        where x,y, and z are objects is represented as { x : 3, y : -2, z : -3 }
```


might have a sign error and should I think be 


```
        For example linear function 3 * x - 2 * y + 3 * z
        where x,y, and z are objects is represented as { x : 3, y : -2, z : 3 }
```


2. There is no example in the docstring for MIP.solve. There should be at least one 
(fairly simple and well-commented) and preferably more. Please check other 
docstrings for missing examples. They are *required* as part of the code 
inclusion process. Please read:
http://www.sagemath.org/doc/developer/conventions.html#documentation-strings


---

Comment by ncohen created at 2009-07-31 16:18:34

You were right about the typo. And I hope you will find in MIP-3.patch all the docstrings you need ;-)


---

Attachment

Replying to [comment:9 mvngu]:
> Once this ticket has positive review, the SPKG at #6602 should also be merged in the standard packages repository. 
*Correction:* Once this ticket has positive review, the SPKG at #6602 should also be merged in the *optional* packages repository.


---

Comment by wdj created at 2009-08-01 03:07:00

The 3 patches applied fione to 4.1.1.a1. But on an ubuntu 9.04 machine, I got the following failures:


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -t  "devel/sage/sage/numerical/mip.pyx"            
sage -t  "devel/sage/sage/numerical/mip.pyx"                                                      
**********************************************************************                            
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 280:         
    sage: p.show()                                                                                
Exception raised:                                                                                 
    Traceback (most recent call last):                                                            
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                  
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_10[5]>", line 1, in <module>                                       
        p.show()###line 280:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 303:                
    sage: p.addbound("x",min=3,max=8)                                                                    
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_11[4]>", line 1, in <module>                                       
        p.addbound("x",min=Integer(3),max=Integer(8))###line 303:                                        
    sage: p.addbound("x",min=3,max=8)                                                                    
    AttributeError: MIP instance has no attribute 'addbound'                                             
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 304:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_11[5]>", line 1, in <module>                                       
        p.show()###line 304:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 372:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 374:                
    sage: p.solve(objective_only=True)                                                                   
Expected:                                                                                                
    4.0                                                                                                  
Got:                                                                                                     
    2.6666666666666665                                                                                   
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 102:                
    sage: print p.export(format="text")                                                                  
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_3[4]>", line 1, in <module>                                        
        print p.export(format="text")###line 102:                                                        
    sage: print p.export(format="text")                                                                  
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 126:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_4[5]>", line 1, in <module>                                        
        p.show()###line 126:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 159:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 195:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 214:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_7[5]>", line 1, in <module>                                        
        p.show()###line 214:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 231:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_8[5]>", line 1, in <module>                                        
        p.show()###line 231:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 248:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_9[5]>", line 1, in <module>                                        
        p.show()###line 248:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************
10 items had failures:
   1 of   6 in __main__.example_10
   2 of   6 in __main__.example_11
   2 of  15 in __main__.example_12
   1 of   5 in __main__.example_3
   1 of   6 in __main__.example_4
   1 of   7 in __main__.example_5
   1 of   7 in __main__.example_6
   1 of   6 in __main__.example_7
   1 of   6 in __main__.example_8
   1 of   6 in __main__.example_9
***Test Failed*** 12 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.1.1.alpha1/tmp/.doctest_mip.py
         [3.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/numerical/mip.pyx"
Total time for all tests: 3.5 seconds
```



---

Comment by wdj created at 2009-08-01 03:09:42

There was also this compiling error:


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -b  

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....       
Building sage/numerical/mip.pyx because it depends on ../../local/include/glpk.h.
python `which cython` --embed-positions --incref-local-binop -I/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage-OR2 -o sage/numerical/mip.cpp sage/numerical/mip.pyx                                                          
sage/numerical/mip.pyx --> /home/wdj/sagefiles/sage-4.1.1.alpha1/local//lib/python/site-packages//sage/numerical/mip.pyx                                                                                                      
Time to execute 1 commands: 1.12334299088 seconds                                                              
Finished compiling Cython code (time = 2.04412698746 seconds)                                                  
running install                                                                                                
running build                                                                                                  
running build_py                                                                                               
running build_ext                                                                                              
building 'sage.numerical.mip' extension                                                                        
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -Ilocal/include/ -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local//include -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local//include/csage -I/home/wdj/sagefiles/sage-4.1.1.alpha1/devel//sage/sage/ext -I/home/wdj/sagefiles/sage-4.1.1.alpha1/local/include/python2.6 -c sage/numerical/mip.cpp -o build/temp.linux-x86_64-2.6/sage/numerical/mip.o -w                         
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++            
sage/numerical/mip.cpp: In function ‘PyObject* __pyx_pf_4sage_9numerical_3mip_3MIP_solveGLPK(PyObject*, PyObject*, PyObject*)’:                                                                                               
sage/numerical/mip.cpp:2785: error: ‘glp_prob’ was not declared in this scope                                  
sage/numerical/mip.cpp:2785: error: ‘__pyx_v_lp’ was not declared in this scope                                
sage/numerical/mip.cpp:2795: error: ‘glp_iocp’ was not declared in this scope                                  
sage/numerical/mip.cpp:2795: error: ‘__pyx_v_iocp’ was not declared in this scope                              
sage/numerical/mip.cpp:2993: error: ‘glp_create_prob’ was not declared in this scope                           
sage/numerical/mip.cpp:3006: error: ‘glp_add_rows’ was not declared in this scope                              
sage/numerical/mip.cpp:3019: error: ‘glp_add_cols’ was not declared in this scope                              
sage/numerical/mip.cpp:3106: error: ‘glp_set_obj_coef’ was not declared in this scope                          
sage/numerical/mip.cpp:3249: error: ‘GLP_DB’ was not declared in this scope                                    
sage/numerical/mip.cpp:3249: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3338: error: ‘GLP_UP’ was not declared in this scope                                    
sage/numerical/mip.cpp:3338: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3427: error: ‘GLP_LO’ was not declared in this scope                                    
sage/numerical/mip.cpp:3427: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3458: error: ‘GLP_FR’ was not declared in this scope                                    
sage/numerical/mip.cpp:3458: error: ‘glp_set_col_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3772: error: ‘GLP_FX’ was not declared in this scope                                    
sage/numerical/mip.cpp:3772: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3799: error: ‘GLP_DB’ was not declared in this scope                                    
sage/numerical/mip.cpp:3799: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3854: error: ‘GLP_UP’ was not declared in this scope                                    
sage/numerical/mip.cpp:3854: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3907: error: ‘GLP_LO’ was not declared in this scope                                    
sage/numerical/mip.cpp:3907: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3920: error: ‘GLP_FR’ was not declared in this scope                                    
sage/numerical/mip.cpp:3920: error: ‘glp_set_row_bnds’ was not declared in this scope                          
sage/numerical/mip.cpp:3965: error: ‘GLP_MIN’ was not declared in this scope                                   
sage/numerical/mip.cpp:3965: error: ‘glp_set_obj_dir’ was not declared in this scope                           
sage/numerical/mip.cpp:3977: error: ‘GLP_MAX’ was not declared in this scope                                   
sage/numerical/mip.cpp:3977: error: ‘glp_set_obj_dir’ was not declared in this scope                           
sage/numerical/mip.cpp:4067: error: ‘GLP_IV’ was not declared in this scope                                    
sage/numerical/mip.cpp:4067: error: ‘glp_set_col_kind’ was not declared in this scope                          
sage/numerical/mip.cpp:4116: error: ‘GLP_BV’ was not declared in this scope                                    
sage/numerical/mip.cpp:4116: error: ‘glp_set_col_kind’ was not declared in this scope                          
sage/numerical/mip.cpp:4144: error: ‘GLP_CV’ was not declared in this scope
sage/numerical/mip.cpp:4144: error: ‘glp_set_col_kind’ was not declared in this scope
sage/numerical/mip.cpp:4164: error: ‘glp_load_matrix’ was not declared in this scope
sage/numerical/mip.cpp:4173: error: expected type-specifier before ‘glp_iocp’
sage/numerical/mip.cpp:4173: error: expected `;' before ‘glp_iocp’
sage/numerical/mip.cpp:4182: error: ‘glp_init_iocp’ was not declared in this scope
sage/numerical/mip.cpp:4191: error: ‘GLP_ON’ was not declared in this scope
sage/numerical/mip.cpp:4213: error: ‘GLP_MSG_OFF’ was not declared in this scope
sage/numerical/mip.cpp:4237: error: ‘GLP_MSG_ERR’ was not declared in this scope
sage/numerical/mip.cpp:4261: error: ‘GLP_MSG_ON’ was not declared in this scope
sage/numerical/mip.cpp:4273: error: ‘GLP_MSG_ALL’ was not declared in this scope
sage/numerical/mip.cpp:4284: error: ‘glp_intopt’ was not declared in this scope
sage/numerical/mip.cpp:4293: error: ‘glp_mip_obj_val’ was not declared in this scope
sage/numerical/mip.cpp:4322: error: ‘glp_delete_prob’ was not declared in this scope
sage/numerical/mip.cpp:4416: error: ‘glp_mip_col_val’ was not declared in this scope
sage/numerical/mip.cpp:4430: error: ‘glp_delete_prob’ was not declared in this scope
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m6.324s
user    0m3.516s
sys     0m0.604s
```



---

Comment by wdj created at 2009-08-01 03:17:15

Ignore the last 2 errors. I think I know what happened. the experimental package 4ti2 on sage.math seems to be over-writing the glpk package. I need to start over ...


---

Comment by wdj created at 2009-08-01 03:21:49

I reinstalled glpk and rebuilt the clone which had MIP1, MIP2, MIP3 applied. This time, it compiled fine:-)

Hopwever the was the following error:


```

wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -t  "devel/sage/sage/numerical/mip.pyx"
sage -t  "devel/sage/sage/numerical/mip.pyx"                                          
**********************************************************************                
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 280:
    sage: p.show()                                                                       
Exception raised:                                                                        
    Traceback (most recent call last):                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                  
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_10[5]>", line 1, in <module>                                       
        p.show()###line 280:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 303:                
    sage: p.addbound("x",min=3,max=8)                                                                    
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_11[4]>", line 1, in <module>                                       
        p.addbound("x",min=Integer(3),max=Integer(8))###line 303:                                        
    sage: p.addbound("x",min=3,max=8)                                                                    
    AttributeError: MIP instance has no attribute 'addbound'                                             
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 304:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_11[5]>", line 1, in <module>                                       
        p.show()###line 304:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 372:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 374:                
    sage: p.solve(objective_only=True)                                                                   
Expected:                                                                                                
    4.0                                                                                                  
Got:                                                                                                     
    2.6666666666666665                                                                                   
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 102:                
    sage: print p.export(format="text")                                                                  
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_3[4]>", line 1, in <module>                                        
        print p.export(format="text")###line 102:                                                        
    sage: print p.export(format="text")                                                                  
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 126:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_4[5]>", line 1, in <module>                                        
        p.show()###line 126:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 159:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 195:                
    sage: p.solve()                                                                                      
Expected:                                                                                                
    [4.0, {'x': 2.0, 'y': 0.0}]                                                                          
Got:                                                                                                     
    [2.6666666666666665, {'y': 1.3333333333333333, 'x': 0.0}]                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 214:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_7[5]>", line 1, in <module>                                        
        p.show()###line 214:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 231:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)                                      
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example 
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs                                                                   
      File "<doctest __main__.example_8[5]>", line 1, in <module>                                        
        p.show()###line 231:                                                                             
    sage: p.show()                                                                                       
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)             
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)           
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)  
    AttributeError: 'NoneType' object has no attribute 'copy'                                            
**********************************************************************                                   
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/numerical/mip.pyx", line 248:                
    sage: p.show()                                                                                       
Exception raised:                                                                                        
    Traceback (most recent call last):                                                                   
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test   
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wdj/sagefiles/sage-4.1.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[5]>", line 1, in <module>
        p.show()###line 248:
    sage: p.show()
      File "mip.pyx", line 130, in sage.numerical.mip.MIP.show (sage/numerical/mip.cpp:1335)
      File "mip.pyx", line 108, in sage.numerical.mip.MIP.export (sage/numerical/mip.cpp:1047)
      File "mip.pyx", line 604, in sage.numerical.mip.Constraint.__init__ (sage/numerical/mip.cpp:5791)
    AttributeError: 'NoneType' object has no attribute 'copy'
**********************************************************************
10 items had failures:
   1 of   6 in __main__.example_10
   2 of   6 in __main__.example_11
   2 of  15 in __main__.example_12
   1 of   5 in __main__.example_3
   1 of   6 in __main__.example_4
   1 of   7 in __main__.example_5
   1 of   7 in __main__.example_6
   1 of   6 in __main__.example_7
   1 of   6 in __main__.example_8
   1 of   6 in __main__.example_9
***Test Failed*** 12 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.1.1.alpha1/tmp/.doctest_mip.py
         [3.3 s]
exit code: 1024

```


Do you know what these mean?

This was with sage 4.1.1.a1 and on an amd64 ubuntu 9.04 machine.


---

Comment by ncohen created at 2009-08-01 08:32:36

I do !!

It means first that I sent another patch without testing it in the end again ( for which I am sorry ), and also that I forgot some of the algorithms in the solvers were randomized, which explains for some results being different from time to time. I "corrected" this by picking examples for which the solutions are unique ;-)

Patch MIP-4 available ;-)


---

Attachment


---

Comment by wdj created at 2009-08-01 16:05:46

This passed and the docstrings look good.

Positive review from me as an optional package.

Great job Nathann and thanks for creating this very useful package!


---

Comment by ncohen created at 2009-08-02 08:24:19

MIP-5.patch is available !

Two lines' worth of modifications to print different messages when wrong solvers are selected.. And I don't think I will have anything to add to that for the moment ;-)

And as soon as this patch is accepted into Sage, I post the new graph functions ;-)

Thank you so much again !!!


---

Attachment


---

Comment by wdj created at 2009-08-03 02:24:14

This passed test as well.


---

Comment by ncohen created at 2009-08-03 07:15:33

is there anything left to do for this patch, now ? ;-)


---

Comment by wdj created at 2009-08-03 15:00:45

Once someone posts it and your other packages to sagemath.org, you probably should post another email to sage-devel (and maybe sage-edu) to ask people to try it out. If you have looked at pygklp already then you can also comment on how your package compares to it.


---

Comment by ncohen created at 2009-08-03 16:17:18

And how is it possible for me to check on whether the patch have already been included in Sage ? Is there any page I can consult on which I could read when it is possible for the users to use this patch using sage -upgrade ? 

Thank you for your help ! :-)

Nathann


---

Comment by wdj created at 2009-08-03 16:50:02

Replying to [comment:31 ncohen]:
> And how is it possible for me to check on whether the patch have already been included in Sage ? 

It will go here:
http://www.sagemath.org/packages/optional/


> Is there any page I can consult on which I could read when it is possible for the 
> users to use this patch using sage -upgrade ? 


They will use sage -i <spkg-name>, not sage -upgrade, on the bash command line.
Also, install_package('<spkg-name>') should work from the Sage command line or 
the notebook.

Of course, anyone can use 
sage -i http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg
to install glpk right now (or
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg
to force a reinstall).


> 
> Thank you for your help ! :-)
> 
> Nathann


---

Comment by ncohen created at 2009-08-03 16:53:01

They will use sage -upgrade to download the spkg, but what about this very patch ? Will there be any other way to install it than by meddling with hg_sage ? ;-)


---

Comment by wdj created at 2009-08-03 17:12:11

Replying to [comment:33 ncohen]:
> They will use sage -upgrade to download the spkg, 

sage -i, not sage -upgrade.

> but what about this very patch ? Will there be any other way to install it than by meddling with hg_sage ? ;-)

Once Minh or William posts a comment to this trac ticket saying "applied to sage x.y.z" and "status => closed" (or something like that) then it will be part of the next release of Sage. Until then, yes, a user should create a new clone and then apply your patches using hg_sage.


---

Comment by ncohen created at 2009-08-03 17:15:21

sage -i, sorry ^^;

Thanks for these explanations ! ;-)


---

Comment by mvngu created at 2009-08-04 09:25:40

One can use the following command in order to install glpk:

```
sage -f http://www.sagemath.org/packages/optional/glpk-4.38.spkg
```



---

Comment by wdj created at 2009-08-04 10:15:24

Replying to [comment:36 mvngu]:
> One can use the following command in order to install glpk:
> {{{
> sage -f http://www.sagemath.org/packages/optional/glpk-4.38.spkg
> }}}

I don't see it listed on http://www.sagemath.org/packages/optional/.
Am I missing something?


---

Comment by mvngu created at 2009-08-04 10:20:55

Replying to [comment:37 wdj]:
> Replying to [comment:36 mvngu]:
> > One can use the following command in order to install glpk:
> > {{{
> > sage -f http://www.sagemath.org/packages/optional/glpk-4.38.spkg
> > }}}
> 
> I don't see it listed on http://www.sagemath.org/packages/optional/.
> Am I missing something?
The Python script that is used for regenerating the packages HTML pages is not working for me at the moment. So I can't successfully run it in order to update any of the HTML pages that lists all known packages. But the good news is that you can be sure that the package `glpk-4.38.spkg ` is up on the optional packages repository. If you can't download that package from the link

http://www.sagemath.org/packages/optional/glpk-4.38.spkg

please tell me.


---

Comment by ncohen created at 2009-08-06 18:53:27

All patches up to MIP-5


---

Attachment


---

Comment by mvngu created at 2009-08-14 11:27:22

Hi Nathann. The timing of these patches is unfortunate :-(  I'm about to release Sage 4.1.1 in a couple of hours. The release has been delayed far too long.


---

Comment by mvngu created at 2009-08-14 11:47:26

I got the following error after merging the patch `AllMIP.patch` and rebuilding the modified library files. I was merging it on top of Sage 4.1.1.rc2.

```
<SNIP>
sage/numerical/mip.cpp:4051: error: ‘GLP_MIN’ was not declared in this scope
sage/numerical/mip.cpp:4051: error: ‘glp_set_obj_dir’ was not declared in this scope
sage/numerical/mip.cpp:4063: error: ‘GLP_MAX’ was not declared in this scope
sage/numerical/mip.cpp:4063: error: ‘glp_set_obj_dir’ was not declared in this scope
sage/numerical/mip.cpp:4153: error: ‘GLP_IV’ was not declared in this scope
sage/numerical/mip.cpp:4153: error: ‘glp_set_col_kind’ was not declared in this scope
sage/numerical/mip.cpp:4202: error: ‘GLP_BV’ was not declared in this scope
sage/numerical/mip.cpp:4202: error: ‘glp_set_col_kind’ was not declared in this scope
sage/numerical/mip.cpp:4230: error: ‘GLP_CV’ was not declared in this scope
sage/numerical/mip.cpp:4230: error: ‘glp_set_col_kind’ was not declared in this scope
sage/numerical/mip.cpp:4250: error: ‘glp_load_matrix’ was not declared in this scope
sage/numerical/mip.cpp:4259: error: expected type-specifier before ‘glp_iocp’
sage/numerical/mip.cpp:4259: error: expected `;' before ‘glp_iocp’
sage/numerical/mip.cpp:4268: error: ‘glp_init_iocp’ was not declared in this scope
sage/numerical/mip.cpp:4277: error: ‘GLP_ON’ was not declared in this scope
sage/numerical/mip.cpp:4299: error: ‘GLP_MSG_OFF’ was not declared in this scope
sage/numerical/mip.cpp:4323: error: ‘GLP_MSG_ERR’ was not declared in this scope
sage/numerical/mip.cpp:4347: error: ‘GLP_MSG_ON’ was not declared in this scope
sage/numerical/mip.cpp:4359: error: ‘GLP_MSG_ALL’ was not declared in this scope
sage/numerical/mip.cpp:4370: error: ‘glp_intopt’ was not declared in this scope
sage/numerical/mip.cpp:4379: error: ‘glp_mip_obj_val’ was not declared in this scope
sage/numerical/mip.cpp:4408: error: ‘glp_delete_prob’ was not declared in this scope
sage/numerical/mip.cpp:4502: error: ‘glp_mip_col_val’ was not declared in this scope
sage/numerical/mip.cpp:4516: error: ‘glp_delete_prob’ was not declared in this scope
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```



---

Comment by mvngu created at 2009-08-14 12:24:43

I got the above compilation errors because I didn't install the optional package glpk. So that spkg should be installed first, then apply the patch `AllMIP.patch`. I'm putting this back to positive review. My bad :-(


---

Comment by mvngu created at 2009-08-23 12:16:21

GLPK is an optional spkg. So any doctests that use GLPK must be flagged as "# optional". Also, it looks like #6765 depends on this ticket.


---

Comment by mvngu created at 2009-08-23 12:17:18

I'm marking this ticket as "needs work" until the doctests that use GLPK or CBC, etc., are marked as "# optional".


---

Comment by mvngu created at 2009-08-23 12:52:00

The patches and GLPK should be wrapped up into an spkg. The patch `AllMIP.patch` if applied as is would fail to compile. You can rectify that by first installing the optional spkg GLPK. But the patch `AllMIP.patch` is to be applied to the Sage library, and when applied and shipping Sage, Sage would fail to compile because we don't ship optional spkg's. So put everything (the patches plus GLPK) into a self-contained spkg.


---

Comment by ncohen created at 2009-08-24 09:47:06

New patch AllMIP-2 available.

All the calls to solve() are flagged optional. *This class should now compile even without the libraries glpk* ( which have been removed from module_list ) : all is left in this class except the call to solveGlpk, which is now a function defined in the new version of the spkg ( see #6817 ).

It is a bit better this way, as this was already the case with package CBC ( now, the code is "symmetric" between Glpk and Cbc, as both are optional packages )

In the end :
* To test this code aply patch AllMIP-2
* To install the new version of Glpk which is to make this code useful, type 

```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg
```


This spkg being currently reviewed at #6817 ( it should be pretty quick, there is nothing new in this patch except a function which had already been reviewed here ! )


---

Attachment

Now **without** solveGlpk !


---

Comment by ncohen created at 2009-08-24 11:08:19

Lets make it :

```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.p0.spkg
```



---

Comment by wdj created at 2009-08-25 17:53:02

I can only test this with glpk installed (having build problems...). Is that okay?


---

Comment by mvngu created at 2009-08-25 18:04:14

Replying to [comment:50 wdj]:
> I can only test this with glpk installed (having build problems...). Is that okay?
That is fine by me. But note that since the patch `AllMIP-2.patch` depends on an optional package, its doctests should be marked with "# optional" so that running doctests with something like "./sage -t -long  /path/to/script.py" would skip over doctests that require optional spkg's. At the moment, most of the doctests in `AllMIP-2.patch` require that the optional package GLPK be installed, but those doctests that require this package are not flagged with "# optional". See for example, this doctest:

```
 	39	         sage: ### Computation of a maximum stable set in Petersen's graph ### 
 	40	         sage: g=graphs.PetersenGraph() 
 	41	         sage: p=MIP(sense=1) 
 	42	         sage: obj={} 
 	43	         sage: for i in g.vertices(): 
 	44	         ...       obj[i]=1  
 	45	         ...       p.setinteger(i)  
 	46	         sage: p.setobj(obj) 
 	47	         sage: for (a,b,c) in g.edges(): 
 	48	         ...       cons={}  
 	49	         ...       cons[a]=1  
 	50	         ...       cons[b]=1  
 	51	         ...       p.addconstraint(cons,max=1)  
 	52	         sage: p.solve(objective_only=True) 
 	53	         4.0
```

The line

```
 	41	         sage: p=MIP(sense=1) 
```

requires GLPK and some other patches. But it should be written like this:

```
 	41	         sage: p=MIP(sense=1)  # optional
```

to flag it as requiring an optional package. Any other tests that require the functionalities of an optional spkg must be flagged as such. When testing these, one would do something along this line:

```
./sage -t -long -optional /path/to/script.py
```



---

Comment by wdj created at 2009-08-25 18:09:44

Okay, because of this comment, I'm changing it back to needs work.


---

Comment by ncohen created at 2009-08-25 18:48:57

Hmmm... There's something I do not understand here ^^;

At first I thought I had made a mistake by not uploading the last version of my patch, in which I added the required "optional" flags, but in the end it seems there are included already... You can see they are by looking (Ctrl - f) for the word "optional" on the page http://trac.sagemath.org/sage_trac/attachment/ticket/6502/AllMIP-2.patch

I just installed this patch on a brand new install without GLPK, it compiled fine and there were no warnings during the test ( without the -optional flag, obiously)

Could you please check that you downloaded the last version and did not apply a cached file ??

Just to be sure, I upload a flattened version of patch named AllMIP-2-flattened.patch


---

Attachment

BTW, the ALLMIP2 patch applied fine for me, as before, and passes sage -testall (mod the known unrelated failures already described). So, positive review from me, but I am testing on a clone of Sage which has glpk installed.


---

Comment by ncohen created at 2009-08-25 22:14:06

I tested it on a copy of Sage without GLPK... But as I posted this patch I guess it does not count ^^;


---

Comment by ncohen created at 2009-08-31 15:54:44

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-02 17:39:43

This ticket should be deleted. A new ticket has been created #6869 with a new version of the class, now using symbolics !

Nathann


---

Comment by mvngu created at 2009-09-02 17:44:51

Resolution: wontfix
