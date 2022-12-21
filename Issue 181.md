# Issue 181: Recursive load makes symbol?? display the wrong File: information

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2006-12-11 18:58:16

Assignee: was

Keywords: recursive load source file

We use the example in examples/programming/recursive_load.

file1.sage defines a symbol foo.
file2.sage defines a symbol bar.

Each file loads the other recursively.

If we load file2.sage first, then the source code for foo is displayed correctly by foo?? but the File: information is wrong.  The File: should read file1.sage.


```
sage: load file2.sage
loaded file1.sage
I'm now defining s
loaded file1.sage

sage: foo??
Type:           function
Base Class:     <type 'function'>
String Form:    <function foo at 0x8fd6db0>
Namespace:      Interactive
File:           /Users/nalexand/Devel/sage-alpha8/examples/programming/recursive_load/file2.py
Definition:     foo(n)
Source:
def foo(n):
    print "foo"
    return n**Integer(2)
```



---

Comment by was created at 2007-01-22 05:00:58

Changing type from defect to enhancement.


---

Comment by was created at 2007-01-22 05:00:58

This isn't really a bug.  What happens is that from file2.sage the file file2.py
is created.  And file2.py is where the function foo is actually defined (it's the
preparsed version).  So the File field above is actually correct about where that
function is defined.  It's *confusing* though, because there is a non-preparsed
.sage function that is defined in file1.sage, and it would be very nice if the
File: field instead listed that.  The only reasonable way I can think of to do
that would be to add to the preparser code that embeds original file location
and line number info in the .py file after the definition of any function. 

So I'm going to change this to an enhancement request rather than a defect, 
as it's not even clear what the right design should be, and currently no invalid
output is actually being produced.


---

Comment by kcrisman created at 2013-01-29 20:34:58

Just pointing out to those looking at this that the examples directory no longer exists.  However, the request still makes sense.
