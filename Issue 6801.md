# Issue 6801: weird bug in magma.eval

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-22 10:22:58

Assignee: was

This gives a weird magma error:

```
magma.eval("""
function t()
    a:=1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7;
end function;
""")
```


The same thing with a shorter line starting "a:=" does not fail. 


---

Comment by klee created at 2009-08-26 07:44:13

The weird error occurs because Sage try to use a file to input the second line "a:=..." 
when Magma is waiting for the remaining part of "function t()". Look at the following pexpect log.


```
function t()
>>>load "/Users/Kwankyu/.sage//temp/athena.local/72436//interface//tmp72436";
load "/Users/Kwankyu/.sage//temp/athena.local/72436//interface//tmp72436";

>> load "/Users/Kwankyu/.sage//temp/athena.local/72436//interface//tmp72436";
   ^
User error: bad syntax
>>>end function;
end function;

>> end function;
   ^
User error: bad syntax
>>>
```


I don't understand why the parameter "allow_use_file" is defaulted to True, in 
"sage/interfaces/expect.py(631)_eval_line()". See


```
def _eval_line(self, line, allow_use_file=True, wait_for_prompt=True):
```



---

Comment by klee created at 2009-08-26 07:48:45

I see... A file is used if the input line is longer than self._eval_using_file_cutoff, which is 100 in my case.


---

Comment by klee created at 2009-08-26 08:22:16

In "sage/interfaces/magma.py(278)", the default value 100 for the parameter "eval_using_file_cutoff" is set. 


```
        Expect.__init__(self,
                        name = "magma",
                        prompt = ">>SAGE>>",
                        command = command,
                        maxread = maxread,
                        server = server, 
                        server_tmpdir = server_tmpdir,
                        script_subdirectory = script_subdirectory,
                        restart_on_ctrlc = False,
                        logfile = logfile,
                        eval_using_file_cutoff=100)      
```


I think 100 is too small. Many of my own Magma codes have lines exceeding 100. Should we simply set the value to a larger value, e.g., 300? This may be a solution, though not elegant.... Is there a smarter solution? One solution is to provide a method like

magma.SetDefaultFileCutoffLength(file_cutoff=300)

so that users can adjust it for their convenience.


---

Comment by mariah created at 2011-05-25 19:21:02

This problem no longer seems to exist with sage-4.7.rc4 and magma-2.17-7.  I suggest that this ticket be closed.


---

Comment by mariah created at 2011-05-25 19:21:02

Changing status from new to needs_review.


---

Comment by kedlaya created at 2011-06-18 05:41:04

Changing status from needs_review to positive_review.


---

Comment by kedlaya created at 2011-06-18 05:41:04

I think this can now be regarded as a duplicate of #9705 and thus closed.


---

Comment by jdemeyer created at 2011-06-20 18:54:53

Resolution: duplicate
