# Issue 9705: trouble with long lines in notebook magma mode

Issue created by migration from https://trac.sagemath.org/ticket/9705

Original creator: nbruin

Original creation time: 2010-08-07 20:53:05

Assignee: jason, was

The following are three cells in a magma-mode notebook worksheet, together with output (there should be none). Each is valid magma code, but the first one produces an error. The other two examples show that shortening the line by changing its content or by placing a line break make the error go away.

```
_<x>:=PolynomialRing(Rationals());
repeat
  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);
until Roots(g) ne [];
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_6.py", line 10, in <module>
    exec compile(u"print _support_.syseval(magma, u'_<x>:=PolynomialRing(Rationals());\\nrepeat\\n  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);\\nuntil Roots(g) ne [];', __SAGE_TMP_DIR__)" + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/usr/local/sage/4.4.4/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/support.py", line 473, in syseval
    return system.eval(cmd, sage_globals, locals = sage_globals)
  File "/usr/local/sage/4.4.4/local/lib/python2.6/site-packages/sage/interfaces/magma.py", line 523, in eval
    raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
RuntimeError: Error evaluating Magma code.
IN:_<x>:=PolynomialRing(Rationals());
repeat
  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);
until Roots(g) ne [];
OUT:

>> load "/home/nobody/.sage//temp/ella.cecm.sfu.ca/21960//interface//tmp21960"
   ^
User error: bad syntax

>> until Roots(g) ne [];
   ^
User error: bad syntax
```



```
_<x>:=PolynomialRing(Rationals());
repeat
  g:=x^3+b*x+c where b:=Random([-10..10]) where c:=Random([-10..10]);
until Roots(g) ne [];
///
```



```
_<x>:=PolynomialRing(Rationals());
repeat
  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2
     where b:=Random([-10..10]) where c:=Random([-10..10]);
until Roots(g) ne [];
///
```



---

Comment by klee created at 2010-08-08 22:00:42

If I remember correctly, my own investigation into this bug revealed that this is caused by Sage's use of temporary files for lengthy input, which causes truncations of input at wrong syntactical places. 

As you see in the first input, a temporary file is used for the first three lines, and the last line "until ..." is input separately. Both chunks of Magma codes are of course syntactically wrong. Thus Magma complains.


---

Comment by kedlaya created at 2011-02-28 03:25:15

Here's a similar but even stranger example. This valid Magma which should return nothing, but it returns an error when evaluated in a notebook cell:

```
MR:=MatrixRing(Rationals(),4); 
embed:=function(A); 
return MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); 
end function;
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_27.py", line 10, in <module>
    exec compile(u"print _support_.syseval(magma, u'MR:=MatrixRing(Rationals(),4); \\nembed:=function(A); \\nreturn MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); \\nend function;', __SAGE_TMP_DIR__)" + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/scratch/sage-x64/devel/sagenb-main/sagenb/misc/support.py", line 473, in syseval
    return system.eval(cmd, sage_globals, locals = sage_globals)
  File "/scratch/sage-x64/local/lib/python2.6/site-packages/sage/interfaces/magma.py", line 523, in eval
    raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
RuntimeError: Error evaluating Magma code.
IN:MR:=MatrixRing(Rationals(),4); 
embed:=function(A); 
return MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); 
end function;
OUT:

>> load "/home/r1/kedlaya/.sage//temp/dwork.mit.edu/32584//interface//tmp32588
   ^
User error: bad syntax

>> end function;
   ^
User error: bad syntax
```

Apparently the last line got separated from the rest by mistake. The same sort of thing happens if I concatenate the first two commands into one line and the other two into a second line. But if I make the line even longer by concatenating all four commands together, the error vanishes!

```
MR:=MatrixRing(Rationals(),4); embed:=function(A); return MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); end function;
///
```

I can also avoid the error by slightly shortening the third line in the original (e.g., by changing the last nonzero matrix entry to 0).

I suppose what's going on is that Sage never breaks up an individual line, but it does or does not concatenate multiple lines into the same temporary file based on length considerations. This clearly needs to be done more intelligently.


---

Comment by was created at 2011-03-21 22:08:34

Changing assignee from jason, was to was.


---

Comment by was created at 2011-03-21 22:44:47

Hi,

I'm attaching a patch that fixes this issue.  It's hard to test because of other issues with the sage/magma interface being broken.  

The idea of the fix is simply that for Magma we just evaluate the input block as one big block instead of splitting things up into separate lines.      I implemented this by adding an option to the base class in expect.py.    Obviously, this same sort of bug could happen with some other interfaces, and I'm not addressing that problem in this ticket.


---

Attachment


---

Comment by was created at 2011-03-21 22:48:58

Changing status from new to needs_review.


---

Comment by mraum created at 2011-03-22 22:53:25

Changing status from needs_review to positive_review.


---

Comment by mraum created at 2011-03-22 22:53:25

This looks good for; Tests are OK.


---

Comment by jdemeyer created at 2011-03-27 20:57:19

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-03-27 20:57:19

Problems while building the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma.Magma.eval:33: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma:33: (ERROR/3) Unexpected indentation.
```



---

Comment by mraum created at 2011-03-29 06:20:29

Changing status from needs_work to positive_review.


---

Attachment

I reformated the old part of the function's documentation, that was incorrect. Now everything builds fine with the right output.

Sorry for this trouble!


---

Comment by jdemeyer created at 2011-04-04 14:19:13

I still have the same problems, even with the new patch.  Are you sure your documentation built fine?  Do `make doc-html` and look for WARNING or ERROR in the output.


---

Comment by jdemeyer created at 2011-04-04 14:19:13

Changing status from positive_review to needs_work.


---

Comment by mraum created at 2011-04-04 18:03:32

Jeroen, there really isn't anything like this on my computer (based on 4.7alpha1). I just have checked once more. If possible could you post the output?

William, if you have time to have a look at this, please do so. I somewhat have no clue why this should happen.


---

Comment by jdemeyer created at 2011-04-04 18:14:46

I will have a second look.


---

Comment by jdemeyer created at 2011-04-04 18:27:21

When applying your patches, I get:

```
$ ./sage -b
[...]
$ make doc-html
[...]
sphinx-build -b html -d /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/doctrees/en/reference    /usr/local/src/sage-4.7.alpha2/devel/sage/doc/en/reference /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/html/en/reference
Running Sphinx v1.0.4
loading pickled environment... done
building [html]: targets for 2 source files that are out of date
updating environment: 0 added, 2 changed, 0 removed
reading sources... [ 50%] sage/interfaces/expect
reading sources... [100%] sage/interfaces/magma

/usr/local/src/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma.Magma.eval:33: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/usr/local/src/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma:33: (ERROR/3) Unexpected indentation.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [ 25%] index
writing output... [ 50%] interfaces
writing output... [ 75%] sage/interfaces/expect
writing output... [100%] sage/interfaces/magma

writing additional files... genindex py-modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 2 warnings.
Build finished.  The built documents can be found in /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/html/en/reference
[...]
```

I will have a look to fix this.


---

Comment by jdemeyer created at 2011-04-04 20:30:58

This one is more involved than I guessed: the problem seems to be the "\n" symbol in the magma command.  I don't know what to do with this.  Is there a way to rewrite the test such that no "\n" is needed?  Otherwise I would suggest to ask `sage-devel`.


---

Comment by mraum created at 2011-04-05 16:18:20

Indeed, the \n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.


---

Comment by jdemeyer created at 2011-04-07 14:02:11

Replying to [comment:14 mraum]:
> Indeed, the \n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.

You better do it as I don't know nor have Magma.


---

Attachment

I removed the linebreaks an the tests pass. The document builds without warnings, but this should be checked by others.


---

Comment by mraum created at 2011-04-08 17:11:11

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-04-11 09:00:33

I will check that the documentation works.


---

Comment by jdemeyer created at 2011-04-11 19:16:01

Resolution: fixed
