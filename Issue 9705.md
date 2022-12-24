# Issue 9705: trouble with long lines in notebook magma mode

archive/issues_009705.json:
```json
{
    "body": "Assignee: jason, was\n\nThe following are three cells in a magma-mode notebook worksheet, together with output (there should be none). Each is valid magma code, but the first one produces an error. The other two examples show that shortening the line by changing its content or by placing a line break make the error go away.\n\n```\n_<x>:=PolynomialRing(Rationals());\nrepeat\n  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);\nuntil Roots(g) ne [];\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_6.py\", line 10, in <module>\n    exec compile(u\"print _support_.syseval(magma, u'_<x>:=PolynomialRing(Rationals());\\\\nrepeat\\\\n  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);\\\\nuntil Roots(g) ne [];', __SAGE_TMP_DIR__)\" + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/usr/local/sage/4.4.4/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/support.py\", line 473, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\n  File \"/usr/local/sage/4.4.4/local/lib/python2.6/site-packages/sage/interfaces/magma.py\", line 523, in eval\n    raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\nRuntimeError: Error evaluating Magma code.\nIN:_<x>:=PolynomialRing(Rationals());\nrepeat\n  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);\nuntil Roots(g) ne [];\nOUT:\n\n>> load \"/home/nobody/.sage//temp/ella.cecm.sfu.ca/21960//interface//tmp21960\"\n   ^\nUser error: bad syntax\n\n>> until Roots(g) ne [];\n   ^\nUser error: bad syntax\n```\n\n\n\n```\n_<x>:=PolynomialRing(Rationals());\nrepeat\n  g:=x^3+b*x+c where b:=Random([-10..10]) where c:=Random([-10..10]);\nuntil Roots(g) ne [];\n///\n```\n\n\n\n```\n_<x>:=PolynomialRing(Rationals());\nrepeat\n  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2\n     where b:=Random([-10..10]) where c:=Random([-10..10]);\nuntil Roots(g) ne [];\n///\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9705\n\n",
    "created_at": "2010-08-07T20:53:05Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "trouble with long lines in notebook magma mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9705",
    "user": "nbruin"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/9705





---

archive/issue_comments_094432.json:
```json
{
    "body": "If I remember correctly, my own investigation into this bug revealed that this is caused by Sage's use of temporary files for lengthy input, which causes truncations of input at wrong syntactical places. \n\nAs you see in the first input, a temporary file is used for the first three lines, and the last line \"until ...\" is input separately. Both chunks of Magma codes are of course syntactically wrong. Thus Magma complains.",
    "created_at": "2010-08-08T22:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94432",
    "user": "klee"
}
```

If I remember correctly, my own investigation into this bug revealed that this is caused by Sage's use of temporary files for lengthy input, which causes truncations of input at wrong syntactical places. 

As you see in the first input, a temporary file is used for the first three lines, and the last line "until ..." is input separately. Both chunks of Magma codes are of course syntactically wrong. Thus Magma complains.



---

archive/issue_comments_094433.json:
```json
{
    "body": "Here's a similar but even stranger example. This valid Magma which should return nothing, but it returns an error when evaluated in a notebook cell:\n\n```\nMR:=MatrixRing(Rationals(),4); \nembed:=function(A); \nreturn MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); \nend function;\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_27.py\", line 10, in <module>\n    exec compile(u\"print _support_.syseval(magma, u'MR:=MatrixRing(Rationals(),4); \\\\nembed:=function(A); \\\\nreturn MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); \\\\nend function;', __SAGE_TMP_DIR__)\" + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/scratch/sage-x64/devel/sagenb-main/sagenb/misc/support.py\", line 473, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\n  File \"/scratch/sage-x64/local/lib/python2.6/site-packages/sage/interfaces/magma.py\", line 523, in eval\n    raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\nRuntimeError: Error evaluating Magma code.\nIN:MR:=MatrixRing(Rationals(),4); \nembed:=function(A); \nreturn MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); \nend function;\nOUT:\n\n>> load \"/home/r1/kedlaya/.sage//temp/dwork.mit.edu/32584//interface//tmp32588\n   ^\nUser error: bad syntax\n\n>> end function;\n   ^\nUser error: bad syntax\n```\n\nApparently the last line got separated from the rest by mistake. The same sort of thing happens if I concatenate the first two commands into one line and the other two into a second line. But if I make the line even longer by concatenating all four commands together, the error vanishes!\n\n```\nMR:=MatrixRing(Rationals(),4); embed:=function(A); return MR!Matrix([[A[1][1],A[1][2],0,0],[A[2][1],A[2][2],0,0],[0,0,A[1][1],A[1][2]],[0,0,0,A[2][2]]]); end function;\n///\n```\n\nI can also avoid the error by slightly shortening the third line in the original (e.g., by changing the last nonzero matrix entry to 0).\n\nI suppose what's going on is that Sage never breaks up an individual line, but it does or does not concatenate multiple lines into the same temporary file based on length considerations. This clearly needs to be done more intelligently.",
    "created_at": "2011-02-28T03:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94433",
    "user": "kedlaya"
}
```

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

archive/issue_comments_094434.json:
```json
{
    "body": "Changing assignee from jason, was to was.",
    "created_at": "2011-03-21T22:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94434",
    "user": "was"
}
```

Changing assignee from jason, was to was.



---

archive/issue_comments_094435.json:
```json
{
    "body": "Hi,\n\nI'm attaching a patch that fixes this issue.  It's hard to test because of other issues with the sage/magma interface being broken.  \n\nThe idea of the fix is simply that for Magma we just evaluate the input block as one big block instead of splitting things up into separate lines.      I implemented this by adding an option to the base class in expect.py.    Obviously, this same sort of bug could happen with some other interfaces, and I'm not addressing that problem in this ticket.",
    "created_at": "2011-03-21T22:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94435",
    "user": "was"
}
```

Hi,

I'm attaching a patch that fixes this issue.  It's hard to test because of other issues with the sage/magma interface being broken.  

The idea of the fix is simply that for Magma we just evaluate the input block as one big block instead of splitting things up into separate lines.      I implemented this by adding an option to the base class in expect.py.    Obviously, this same sort of bug could happen with some other interfaces, and I'm not addressing that problem in this ticket.



---

archive/issue_comments_094436.json:
```json
{
    "body": "Attachment [trac_9705.patch](tarball://root/attachments/some-uuid/ticket9705/trac_9705.patch) by was created at 2011-03-21 22:47:08",
    "created_at": "2011-03-21T22:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94436",
    "user": "was"
}
```

Attachment [trac_9705.patch](tarball://root/attachments/some-uuid/ticket9705/trac_9705.patch) by was created at 2011-03-21 22:47:08



---

archive/issue_comments_094437.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-21T22:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94437",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-22T22:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94438",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094439.json:
```json
{
    "body": "This looks good for; Tests are OK.",
    "created_at": "2011-03-22T22:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94439",
    "user": "mraum"
}
```

This looks good for; Tests are OK.



---

archive/issue_comments_094440.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-03-27T20:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94440",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094441.json:
```json
{
    "body": "Problems while building the documentation:\n\n```\ndochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma.Magma.eval:33: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\ndochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma:33: (ERROR/3) Unexpected indentation.\n```\n",
    "created_at": "2011-03-27T20:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94441",
    "user": "jdemeyer"
}
```

Problems while building the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma.Magma.eval:33: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma:33: (ERROR/3) Unexpected indentation.
```




---

archive/issue_comments_094442.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-03-29T06:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94442",
    "user": "mraum"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094443.json:
```json
{
    "body": "Attachment [trac-9705-magma_block_evaluation-doc.patch](tarball://root/attachments/some-uuid/ticket9705/trac-9705-magma_block_evaluation-doc.patch) by mraum created at 2011-03-29 06:20:29\n\nI reformated the old part of the function's documentation, that was incorrect. Now everything builds fine with the right output.\n\nSorry for this trouble!",
    "created_at": "2011-03-29T06:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94443",
    "user": "mraum"
}
```

Attachment [trac-9705-magma_block_evaluation-doc.patch](tarball://root/attachments/some-uuid/ticket9705/trac-9705-magma_block_evaluation-doc.patch) by mraum created at 2011-03-29 06:20:29

I reformated the old part of the function's documentation, that was incorrect. Now everything builds fine with the right output.

Sorry for this trouble!



---

archive/issue_comments_094444.json:
```json
{
    "body": "I still have the same problems, even with the new patch.  Are you sure your documentation built fine?  Do `make doc-html` and look for WARNING or ERROR in the output.",
    "created_at": "2011-04-04T14:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94444",
    "user": "jdemeyer"
}
```

I still have the same problems, even with the new patch.  Are you sure your documentation built fine?  Do `make doc-html` and look for WARNING or ERROR in the output.



---

archive/issue_comments_094445.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-04T14:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94445",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094446.json:
```json
{
    "body": "Jeroen, there really isn't anything like this on my computer (based on 4.7alpha1). I just have checked once more. If possible could you post the output?\n\nWilliam, if you have time to have a look at this, please do so. I somewhat have no clue why this should happen.",
    "created_at": "2011-04-04T18:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94446",
    "user": "mraum"
}
```

Jeroen, there really isn't anything like this on my computer (based on 4.7alpha1). I just have checked once more. If possible could you post the output?

William, if you have time to have a look at this, please do so. I somewhat have no clue why this should happen.



---

archive/issue_comments_094447.json:
```json
{
    "body": "I will have a second look.",
    "created_at": "2011-04-04T18:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94447",
    "user": "jdemeyer"
}
```

I will have a second look.



---

archive/issue_comments_094448.json:
```json
{
    "body": "When applying your patches, I get:\n\n```\n$ ./sage -b\n[...]\n$ make doc-html\n[...]\nsphinx-build -b html -d /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/doctrees/en/reference    /usr/local/src/sage-4.7.alpha2/devel/sage/doc/en/reference /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/html/en/reference\nRunning Sphinx v1.0.4\nloading pickled environment... done\nbuilding [html]: targets for 2 source files that are out of date\nupdating environment: 0 added, 2 changed, 0 removed\nreading sources... [ 50%] sage/interfaces/expect\nreading sources... [100%] sage/interfaces/magma\n\n/usr/local/src/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma.Magma.eval:33: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/usr/local/src/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/interfaces/magma.py:docstring of sage.interfaces.magma:33: (ERROR/3) Unexpected indentation.\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [ 25%] index\nwriting output... [ 50%] interfaces\nwriting output... [ 75%] sage/interfaces/expect\nwriting output... [100%] sage/interfaces/magma\n\nwriting additional files... genindex py-modindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 2 warnings.\nBuild finished.  The built documents can be found in /usr/local/src/sage-4.7.alpha2/devel/sage/doc/output/html/en/reference\n[...]\n```\n\nI will have a look to fix this.",
    "created_at": "2011-04-04T18:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94448",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_094449.json:
```json
{
    "body": "This one is more involved than I guessed: the problem seems to be the \"\\n\" symbol in the magma command.  I don't know what to do with this.  Is there a way to rewrite the test such that no \"\\n\" is needed?  Otherwise I would suggest to ask `sage-devel`.",
    "created_at": "2011-04-04T20:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94449",
    "user": "jdemeyer"
}
```

This one is more involved than I guessed: the problem seems to be the "\n" symbol in the magma command.  I don't know what to do with this.  Is there a way to rewrite the test such that no "\n" is needed?  Otherwise I would suggest to ask `sage-devel`.



---

archive/issue_comments_094450.json:
```json
{
    "body": "Indeed, the \\n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.",
    "created_at": "2011-04-05T16:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94450",
    "user": "mraum"
}
```

Indeed, the \n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.



---

archive/issue_comments_094451.json:
```json
{
    "body": "Replying to [comment:14 mraum]:\n> Indeed, the \\n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.\n\nYou better do it as I don't know nor have Magma.",
    "created_at": "2011-04-07T14:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94451",
    "user": "jdemeyer"
}
```

Replying to [comment:14 mraum]:
> Indeed, the \n are not necessary as they are replaced by '' anyway. The point of the patch was, that before it was split again later. You might already have a patch for this. If not, let me know, and I will prepare one.

You better do it as I don't know nor have Magma.



---

archive/issue_comments_094452.json:
```json
{
    "body": "Attachment [trac-9705-magma_block_evaluation-linebreak.patch](tarball://root/attachments/some-uuid/ticket9705/trac-9705-magma_block_evaluation-linebreak.patch) by mraum created at 2011-04-08 17:11:11\n\nI removed the linebreaks an the tests pass. The document builds without warnings, but this should be checked by others.",
    "created_at": "2011-04-08T17:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94452",
    "user": "mraum"
}
```

Attachment [trac-9705-magma_block_evaluation-linebreak.patch](tarball://root/attachments/some-uuid/ticket9705/trac-9705-magma_block_evaluation-linebreak.patch) by mraum created at 2011-04-08 17:11:11

I removed the linebreaks an the tests pass. The document builds without warnings, but this should be checked by others.



---

archive/issue_comments_094453.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-08T17:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94453",
    "user": "mraum"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094454.json:
```json
{
    "body": "I will check that the documentation works.",
    "created_at": "2011-04-11T09:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94454",
    "user": "jdemeyer"
}
```

I will check that the documentation works.



---

archive/issue_comments_094455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-11T19:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9705#issuecomment-94455",
    "user": "jdemeyer"
}
```

Resolution: fixed
