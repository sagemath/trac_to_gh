# Issue 99: Need to get rid of "Integer(0)"

Issue created by migration from https://trac.sagemath.org/ticket/99

Original creator: justin

Original creation time: 2006-09-30 02:57:51

Assignee: was

Keywords: Preparsing, sage integers

If I have, for example,

```
    print "F(%s,0)=%s"%(a,b)
```

the result appears as

```
    F(27,Integer(0))=359
```

which seems kind of sucky (to use the technical term).  The only workaround is something like

```
    zero = 0
    print "F(%s,%s)=%s"%(a,zero,b)
```

which is similarly sucky...



---

Comment by was created at 2006-10-01 12:39:12

I can't replicate this.  Can anybody?


---

Comment by was created at 2006-10-01 19:18:53


```
I think I asked this before at some point, and I don't recall if there was an answer.  Why does the preparser modify strings?  It doesn't always, which seems to be why I can't get a small example.
 
This might be a clue.
 
I have a function in a larger (~250 line-) file that has a print statement which looks roughly like
   print "(%s, 0) -> %s"%(blah)
This gets modified in preparsing to
   print "(%s, Integer(0)) -> %s"%(blah)
 
When I take this function and type it in by hand, or put it in a file, it behaves "correctly".  I have tried loading and attaching; same (correct) result.
 
In the case of the larger file, the changed line (above) shows up in the .py file.
 
This larger file has an "attach" line in it, and the attached file gets interpolated into the first file.  But I notice an oddity: in the resulting .py file, it appears as if the parser gets out of sync.
 
Below is a snippet of some parsed code from the .py file, the function that exhibits the bad behavior; notice that the '0' in the "range" expression is not "Integer()"ed.
 
This happens throughout the ~650-line .py file: some range statements with integer arguments have "Integer()" applied; some don't.
 
Is this expeected?
 
def Foo(i):
#    zero = 0   # Blech!
    L=DefaultTR(i,i)
    print "%s -> %s"%(L,GT(L))
    for j in range(0,i+1):
        rv = GT1(L,j)
        if rv != -1:
#            print " (%s,%s|%s) -> %s"%(i,zero,j,rv)
            print " (%s, Integer(0)|%s) -> %s"%(i,j,rv)
 
Justin
 
--
```



---

Comment by justin created at 2006-10-01 21:13:02

Replying to [comment:1 was]:
> I can't replicate this.  Can anybody?

Yup; it's repeatable.  So far, it isn't clear how to do it.  The file in which I initially saw the problem still shows the problem.

One possible connection: I 'attach' this file, and this file contains an 'attach' of a second file.

Looking at the resulting .py file, it shows the content of the second file inserted in the first file at the line where the 'attach' is.  Some distance into the .py file, things start going bad:

Until this point, the only integer constants that get wrapped (in "Integer()") are those in code.  Beginning with a specific function, several lines occur with this form:
   code... # comment

and the comments have wrapped integers.  Following these lines, *no* integer constants are wrapped (for ~200 lines), until some distance into the first file, when wrapping begins again.  From this point, only constants in strings (docstrings or print strings) appear to be wrapped.  Constants in code or comments are untouched.  Weird.


---

Comment by was created at 2006-10-03 04:29:21


```
I think, in preparse(), you are making invalid assumptions about quote marks.  This is a gnarly area, but I think it can be fixed.
 
The problem is that you assume that quotes appear in pairs, but I often use them by themselves (e.g, "# It's time to punt!").
 
The fix is to identify what you are working on when you encounter a character that means something:
  if in Quoted string:
     ignore everything until matching quote
     but note when quotes are "escaped", as in "\'"
 
A quoted string means "blah" or 'blah'.
 
Make sense?
 
Justin
 }}}


---

Comment by was created at 2006-10-15 17:19:56

To Justin:

I just decided to try to fix this, and discovered that I still don't have an actual
example file that exhibits the problem.  I tried making some examples based on what
you wrote above, but everything I tried worked fine.  Could you send me an actual
concrete example that illustrates the behavior you observed?


---

Comment by was created at 2006-11-06 06:24:22

Andrey Novoseltsev 
submitted a new bug report to me that had an example that actually illustrated the problem:


```
Dear William,
 
I believe that I found a bug - SAGE parser does not ignore comments.
 
I had the following code in .sage file
 
##########################
f.readline()    #v[d][i]: sum_j Incidence(i'th dim-d-face, j-th vertex) x 2^j
...
    if lseq[i+1][n-1-j]=='1':
...
f.readline()    #f[d][i]: sum_j Incidence(i'th dim-d-face, j-th facet) x 2^j
...
    if lseq[i+1][n-1-j]=='1':
##########################
 
and the corresponding lines in .py file look like
 
##########################
f.readline()    #v[d][i]: sum_j Incidence(i'th dim-d-face, j-th vertex) x 2^j
...
    if lseq[i+1][n-1-j]=='Integer(1)':
...
f.readline()    #f[d][i]: sum_j Incidence(i'th dim-d-face, j-th facet) x 
Integer(2)**j
...
    if lseq[i+Integer(1)][n-Integer(1)-j]=='1':
##########################
 
So because of the single  '  in the comment it changed my strings and two very 
similar pieces of code worked completely different.
 
I saved the complete files in my directory on sage.math (user novoselt) as 
bug.sage and bug.py.
 
Thank you,
Andrey 
```


I then fixed it in minutes.


```
sha:~ was$ more Desktop/1780.patch 
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1162773046 28800
# Node ID c5bbdfb6168859a83462b061784673d6e4f7e4cc
# Parent  9bd772e2980bd58f8025568f9451e75452b30b84
Fixed bug in preparser where it got confused by comments.

  This bug was reported by Justin Walker and Andrey Novoseltsev

diff -r 9bd772e2980b -r c5bbdfb61688 sage/misc/preparser.py
--- a/sage/misc/preparser.py    Sun Nov 05 10:34:40 2006 -0800
+++ b/sage/misc/preparser.py    Sun Nov 05 16:30:46 2006 -0800
@@ -311,6 +311,12 @@ def preparse(line, reset=True, do_time=F
                                           or line[i-1] == ')'))):
             in_number = True
             num_start = i
+            
+        # Decide if we hit a comment, so we're done.
+        if line[i] == '#' and not (in_single_quote or in_double_quote or in_triple_quote):
+            i = len(line)
+            break
+
         i += 1
```

 
     if in_number:


---

Comment by was created at 2006-11-06 06:24:22

Resolution: fixed
