# Issue 4485: notebook -- implicit multiplication is broken in the notebook but works on the command line (sage-3.1.4)

Issue created by migration from https://trac.sagemath.org/ticket/4485

Original creator: was

Original creation time: 2008-11-09 23:06:57

Assignee: boothby

On the command line in sage-3.1.4:

```
sage: implicit_multiplication(True)
sage: 3x
3*x
```


In the Sage notebook using exactly the same version of Sage (in fact, on sagenb.org):

```
sage: implicit_multiplication(True)
sage: 3 x
 line 4
    _sage_const_3  x
                   ^
SyntaxError: invalid syntax
```



---

Comment by was created at 2008-11-09 23:36:29


```
OK, I've thought about it, and see now that there is no way
that implicit multiplication was ever even *implemented*
for the notebook!    Just to illustrate what is going on, note
that if in the notebook you type 

   implicit_multiplication(True)
   preparse('3x')

you get as output

   'Integer(3)*x'

which illustrates that the implicit_multiplication command works fine in the actual Sage worksheet process.   The problem is that the preparsing of the input for each cell of the notebook is *not* done in that subprocess!  It's done by the worksheet server process itself, before the input is ever sent to the subprocess. 

There are some approaches to fixing this and I'm not happy really about any of them:

  1. Make it so the whole notebook server has an implicit_multiplication mode.  This is absurd since some users might want it and some not.  Alternatively, make it so the notebook server has a mode flag for each worksheet.  That's bad too since that mode can't be set via user input (by typing in cells) unless we fully parse all input before passing it on for evaluation -- i.e., that's a stupid idea which will result in great pain.  The other option, would be to have some GUI checkbox or something, and just give an error if one types in the input box "implicit_multiplication".  This would be inconsistent and maybe busy, but would probably work.  The inconsistency would be huge, since, e.g., if somebody writes a 30 line script like this:
  ...
  implicit_multiplication(True)
  ... 
  3x + 1
  ...
and just *pastes* it into the notebook, it will suddenly not work.  Which will be really annoying. 

  2. Change how the Sage notebook evaluates code blocks.  Instead of preparsing input before sending it off to be evaluated by the worksheet subprocess, somehow send a chunck of non-preparsed code off, and a command that says "preparse this then evaluate it". 

  3. Make sage query the subprocess for its implicit_multiplication state before every single evaluation -- this would be idiotic and slow down the server a lot.  Not an option. 

I think 2 is the best option, but it will not be easy to implement, and making this change scares me. It feels like the sort of change that could introduce numerous subtle bugs, and result in nontrivial degredation in functionality -- for example, maybe source code ?? inspection of user-defined functions in the notebook might no longer work. 

Incidentally, here is a workaround to make it so you can input an expression using implicit multiplication in the notebook. 

implicit_multiplication(True)
sage_eval('3x^3 + 4/5 x + 1', globals())
3*x^3 + 4*x/5 + 1

I'm not going to do anything further on this without some feedback
from Robert Bradshaw (who implemented implicit multiplication)
and/or Mike Hansen who I think knows the relevant part of the
notebook code well enough to have a comment about what
I wrote above.  

 -- William
```



---

Comment by was created at 2008-11-11 00:51:54

Robert Bradshaw and I talked about this and think the best thing to implement
is checkboxes in the notebook with an error message when the implicit_multiplication command is used there.  Also, he claimed that the preparse command should decide on whether or not to use implicit multiplication via an option to that command (I'm not so sure I agree with that).

I think *this* ticket should *only* be to change the implicit_multiplication command to check if it is being run in the notebook (EMBEDDED_MODE, just like the graphics commands use), and if so, give a useful NotImplementedError message.  Then later adding a checkbox will be an enhancement. I've made that enhancement trac #4490.


---

Comment by robertwb created at 2008-11-11 01:31:19

With patch?


---

Attachment


---

Comment by mabshoff created at 2008-11-14 03:31:05

Resolution: fixed


---

Comment by mabshoff created at 2008-11-14 03:31:05

Merged in Sage 3.2.rc1
