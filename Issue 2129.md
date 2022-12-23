# Issue 2129: implement "sage -t" for .pyx files

Issue created by migration from https://trac.sagemath.org/ticket/2129

Original creator: was

Original creation time: 2008-02-09 19:33:42

Assignee: failure


```
'm having some trouble doctesting non sage files. The only things I
could find in the Programming Guide were:

 4.3.1 Testing .py, .pyx and .sage Files

    Run sage -t <filename.py> to test that all code examples in
    filename.py. Similar remarks apply to .sage and
    .pyx files.

and

 5.3.8 Doctests

    If x.pyx is a Cython file, then you can do

     sage -t x.pyx

    to test all the examples in the documentation strings in x.pyx.

But this does not seem to be sufficient. One question: what about
.spyx files? Here is an experiment done on version 2.10.1 that shows
that some clarification (if not some coding) is desirable:

Create a file hello.py with contents:

 def hello():
     """
     Return a friendly string.

     EXAMPLES:
     sage: hello()
     Goodbye!
     """
     return 'Hello!'

Make copies of the file called

 hello.sage
 hello.pyx
 hello.spyx

and then run the commands

 $ sage -t hello.sage  # reports correctly that 'Hello' is not
'Goodbye'
 $ sage -t hello.py    # NameError: name 'hello' is not defined
 $ sage -t hello.pyx   # NameError: name 'hello' is not defined
 $ sage -t hello.spyx  # blithely reports incorrectly that all tests
pass

Following a hint in the Programming Guide, in the case of hello.py,
after changing the EXAMPLES section so it reads

 EXAMPLES:
 sage: from hello import *
 sage: hello()
 Goodbye!

the correct behaviour is recovered. Applying the same change to
hello.pyx is not the right thing to do, since the import will grab the
function out of the module hello.py. However, after changing the name
of the file to hello2.pyx and the function to hello2, we encounter
the same NameError.

 -- Kate Minola
```



---

Comment by malb created at 2009-01-22 23:05:52

Changing type from defect to enhancement.


---

Attachment


---

Comment by rhinton created at 2009-03-12 00:16:12

Note that one of the originally reported problems is still not solved -- doctesting .pyx files outside the tree.  I'm not sure how to fix this, but it would be nice.

I manually updated the patch for 3.4 and added trac_2129-scripts-v3_4.patch, but I need someone to check that I did it correctly.  Specifically, I am not sure the patch applies cleanly.  With these changes, I am able to doctest .spyx files outside the Sage tree, a valuable tool for me right now.


---

Attachment


---

Attachment

.spyx file with a doctest that fails (since previous doctesting blithely reported all tests pass)


---

Comment by jason created at 2009-03-13 15:59:06

This applies cleanly to my sage-3.4 build, so positive review on the rebase.

I also tested it with the spyx file rhinton uploaded, and everything seems to work correctly.


---

Comment by mabshoff created at 2009-03-25 08:26:36

Merged trac_2129-scripts-v3_4.patch in Sage 3.4.1.alpha0. 

Ryan: You posted only a diff, I committed the patch in your name. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 08:26:36

Resolution: fixed
