# Issue 1544: Rich Morin's SAGE Tutorial nits #2

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-17 03:22:35

Assignee: tba


```

http://sagemath.org/doc/html/tut/node9.html

  SAGE uses = for assignment and ==,<=,>=,<,> for comparison:
  ---
  SAGE uses = for assignment.  It uses ==, <=, >=, <, and >
  for comparison:


  ... after the list of variables names.
                        variable


  You can specify multiple inputs,
  and optional defaults for the inputs.
  ---
  You can specify multiple inputs,
  each of which may have a default value.


  In Python  blocks of code are ...
     Python,


  ... because the return          statement is not ...
                  <tt>return</tt>


  If you fix the indentation, then the function works:
  ---
  If you fix the indentation, the function works:


  ... on one line separate   by semicolons:
             line, separated


  ... multiple lines, use               backslash:
                          a terminating


  In SAGE  you count ...
     SAGE,


  ... is like (for(i=1;i<6;i+=2).
               for(i=1;i<6;i+=2).


  ... is to use string formating.
                       formatting.


  Below  we create three columns ...
  Below,


  ... except      it can be ...
             that


  ... is a powerful techniques that can ...
                    technique


  Below  we define a class ...
  Below,


  ... when it is created, and the ...
  ---
  ... when it is created; the ...


  ... of numbers  use the list function:
         numbers,


  ... is considered       in ...
                    to be

  ... the following doesn't, since ...
  ---
  ... the following doesn't work, since ...


  ... on the mailing      for further details.
                     list
```



---

Comment by wdj created at 2007-12-27 04:53:12

Dear Matthew,

Thanks for your bug report!

Dear David Joyner (cc: sage-devel):

This is in some latex that you wrote.  Any ideas?

I've made this trac #1602:
   http://trac.sagemath.org/sage_trac/ticket/1602


---------- Forwarded message ----------
From: Matthew Moelter <>
Date: Dec 26, 2007 4:24 PM
Subject: typo in sage tutorial
To: wstein`@`gmail.com


on this page

http://www.sagemath.org/doc/html/tut/node24.html

in the table there is what appears to be raw latex rather than
typeset material.
this appears "&vellip#vdots;"

Matt



Matthew Moelter, Assoc Prof
Department of Physics
Calif. Polytechnic State Univ.
San Luis Obispo, CA 93407


---

Comment by wdj created at 2007-12-27 04:53:58

Fixed and patch posted to 
http://sage.math.washington.edu/home/wdj/patches/tut20071226.hg
Passes sage -t.


---

Comment by wdj created at 2007-12-27 14:11:27

From an email of Haydn Huntley:

....
One small thing is that "axes" was misspelled as "ases" at the top of page 32.
....


---

Comment by wdj created at 2007-12-28 00:40:10

Fixed and new patch posted to http://sage.math.washington.edu/home/wdj/patches/tut20071227.hg Passes sage -t. Also, the new version of tut.tex is at
http://sage.math.washington.edu/home/wdj/patches/tut.tex


---

Comment by mabshoff created at 2008-01-07 17:16:51

Changes look good to me. Merged in Sage 2.10.alpha0.


---

Comment by mabshoff created at 2008-01-07 17:16:51

Resolution: fixed
