# Issue 2514: additions to coding modules

archive/issues_002514.json:
```json
{
    "body": "Assignee: @rlmill\n\nI have a number of changes to the modules in coding. With permission of Robert Miller, it is rather large (\"code bomb\"). However, most are guava wrappers, rewritten as pure Python/SAGE functions. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2514\n\n",
    "created_at": "2008-03-13T23:51:40Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "additions to coding modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2514",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @rlmill

I have a number of changes to the modules in coding. With permission of Robert Miller, it is rather large ("code bomb"). However, most are guava wrappers, rewritten as pure Python/SAGE functions. 

Issue created by migration from https://trac.sagemath.org/ticket/2514





---

archive/issue_comments_017009.json:
```json
{
    "body": "New patch added to address comments by referee. I think you have to apply the first patch and then the second patch to 2.10.3.",
    "created_at": "2008-03-14T18:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17009",
    "user": "https://github.com/wdjoyner"
}
```

New patch added to address comments by referee. I think you have to apply the first patch and then the second patch to 2.10.3.



---

archive/issue_comments_017010.json:
```json
{
    "body": "Forgot to add: the patch 8866+8867 passes sage -testall.",
    "created_at": "2008-03-14T18:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17010",
    "user": "https://github.com/wdjoyner"
}
```

Forgot to add: the patch 8866+8867 passes sage -testall.



---

archive/issue_comments_017011.json:
```json
{
    "body": "Added one more patch to address problems noticed by the referee. When running sage -testall,\nI noticed another problem. One of the functions requires an internet connection (it goes to codetables.de and fetches data). At this moment, that site is down, so the test failed.\nI added the comment \"## requires internet, long time\" since timing out raises a socket.error.\nThis is the content of the last patch.\n8866+8867+8868+8869 get applied to 2.10.3. Please let me know if it is \npreferable to make a patch for 2.10.4.alpha0 instead.",
    "created_at": "2008-03-15T14:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17011",
    "user": "https://github.com/wdjoyner"
}
```

Added one more patch to address problems noticed by the referee. When running sage -testall,
I noticed another problem. One of the functions requires an internet connection (it goes to codetables.de and fetches data). At this moment, that site is down, so the test failed.
I added the comment "## requires internet, long time" since timing out raises a socket.error.
This is the content of the last patch.
8866+8867+8868+8869 get applied to 2.10.3. Please let me know if it is 
preferable to make a patch for 2.10.4.alpha0 instead.



---

archive/issue_comments_017012.json:
```json
{
    "body": "For doctests that require internet, \"optional\" instead of \"long time\" is the usual flag used. As observed by Mike Hansen, this apparently the standard, as you find when doing `search_src('internet')`.  This is the only remaining issue for this ticket. I have not tried testall with the patches in this ticket, but I have tested `sage/coding`. If the author fixes the doctest comment, and does testall with all of the patches on a fresh 2.10.4.alpha0, then that's a positive review from me.\n\nVery good work here.",
    "created_at": "2008-03-15T18:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17012",
    "user": "https://github.com/rlmill"
}
```

For doctests that require internet, "optional" instead of "long time" is the usual flag used. As observed by Mike Hansen, this apparently the standard, as you find when doing `search_src('internet')`.  This is the only remaining issue for this ticket. I have not tried testall with the patches in this ticket, but I have tested `sage/coding`. If the author fixes the doctest comment, and does testall with all of the patches on a fresh 2.10.4.alpha0, then that's a positive review from me.

Very good work here.



---

archive/issue_comments_017013.json:
```json
{
    "body": "Oops,\n\n```\nsage: C = LinearCode(Matrix(GF(2),[[0,1]]))\nsage: C.permutation_automorphism_group()\n*BOOM*\n```\n\nThis is probably just not checking for trivial generators or something. I don't think these patches introduced this, but it's very closely related...",
    "created_at": "2008-03-15T23:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17013",
    "user": "https://github.com/rlmill"
}
```

Oops,

```
sage: C = LinearCode(Matrix(GF(2),[[0,1]]))
sage: C.permutation_automorphism_group()
*BOOM*
```

This is probably just not checking for trivial generators or something. I don't think these patches introduced this, but it's very closely related...



---

archive/issue_comments_017014.json:
```json
{
    "body": "In fact, the problem above is caused by exactly that: in this case, `gens` is an empty list, and `PermutationGroup`s don't like those.",
    "created_at": "2008-03-15T23:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17014",
    "user": "https://github.com/rlmill"
}
```

In fact, the problem above is caused by exactly that: in this case, `gens` is an empty list, and `PermutationGroup`s don't like those.



---

archive/issue_comments_017015.json:
```json
{
    "body": "Thank you very much for finding this! I can fix this easily. \n\nThere still is the problem of the example\n\n\n```\nsage: C = QuasiQuadraticResidueCode(11)\nsage: C.automorphism_group_binary_code()\n\n\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nI am forced to \"kill -9\" the entire process in this example.\nThe group is not trivial:\n\n\n```\nsage: C = QuasiQuadraticResidueCode(11)\nsage: C\nLinear code of length 22, dimension 11 over Finite Field of size 2\nsage: C.is_self_dual()\nTrue\nsage: C.permutation_automorphism_group()\nPermutation Group with generators [(6,9)(8,17)(10,19)(11,16)(12,20)(13,22)(14,15), (5,8)(7,16)(9,18)(10,15)(12,21)(13,14)(19,22), (4,6)(7,14)(9,18)(10,12)(11,20)(13,16)(15,21)(19,22), (4,7)(6,14)(9,15)(10,19)(11,16)(12,22)(13,20)(18,21), (3,4)(5,7)(8,16)(10,19)(11,17)(13,14)(15,22), (2,3)(7,21)(10,13)(11,20)(12,16)(14,15)(19,22), (1,2)(6,12)(8,17)(9,20)(11,16)(13,15)(14,22)(18,21)]\n```\n",
    "created_at": "2008-03-16T01:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17015",
    "user": "https://github.com/wdjoyner"
}
```

Thank you very much for finding this! I can fix this easily. 

There still is the problem of the example


```
sage: C = QuasiQuadraticResidueCode(11)
sage: C.automorphism_group_binary_code()


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

I am forced to "kill -9" the entire process in this example.
The group is not trivial:


```
sage: C = QuasiQuadraticResidueCode(11)
sage: C
Linear code of length 22, dimension 11 over Finite Field of size 2
sage: C.is_self_dual()
True
sage: C.permutation_automorphism_group()
Permutation Group with generators [(6,9)(8,17)(10,19)(11,16)(12,20)(13,22)(14,15), (5,8)(7,16)(9,18)(10,15)(12,21)(13,14)(19,22), (4,6)(7,14)(9,18)(10,12)(11,20)(13,16)(15,21)(19,22), (4,7)(6,14)(9,15)(10,19)(11,16)(12,22)(13,20)(18,21), (3,4)(5,7)(8,16)(10,19)(11,17)(13,14)(15,22), (2,3)(7,21)(10,13)(11,20)(12,16)(14,15)(19,22), (1,2)(6,12)(8,17)(9,20)(11,16)(13,15)(14,22)(18,21)]
```




---

archive/issue_comments_017016.json:
```json
{
    "body": "Regarding the `QuasiQuadraticResidueCode`, see #2541.",
    "created_at": "2008-03-16T03:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17016",
    "user": "https://github.com/rlmill"
}
```

Regarding the `QuasiQuadraticResidueCode`, see #2541.



---

archive/issue_comments_017017.json:
```json
{
    "body": "Michael Abshoff also noticed that this code is not very consistent. There are further issues with the `permutation_automorphism_group` function, but I'm not sure what's going on. Here is the traceback (if you just call this on random binary codes, it comes up pretty quickly):\n\n```\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/Users/rlmill/sage-2.10.3/<ipython console> in <module>()\n\n/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in permutation_automorphism_group(self, mode)\n   1447           gap.eval(\"Cwt:=Filtered(eltsC,c->WeightCodeword(c)=%s)\"%wt)   ## bottleneck 2 (repeated \n   1448           gap.eval(\"matCwt:=List(Cwt,c->VectorCodeword(c))\")            ##        for each i until stop = 1) \n-> 1449           gap.eval(\"A:=MatrixAutomorphisms(matCwt); GG:=Intersection(Gp,A)\")    ## bottleneck 3\n   1450           #print i,\" = i \\n\",gap.eval(\"matCwt\"),\" = matCwt\\n\"\n   1451           #print gap.eval(\"A\"),\" = A \\n\",gap.eval(\"GG\"),\" = GG\\n\\n\"\n\n/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)\n    307         if len(x) == 0 or x[len(x) - 1] != ';':\n    308             x += ';'\n--> 309         s = Expect.eval(self, x)\n    310         if newlines:\n    311             return s\n\n/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)\n    705         try:\n    706             with gc_disabled():\n--> 707                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    708         except KeyboardInterrupt:\n    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    508                         return ''\n    509                 else:\n--> 510                     raise RuntimeError, message\n    511 \n    512         except KeyboardInterrupt:\n\n<type 'exceptions.RuntimeError'>: Gap produced error output\nLists Assignment: <list> must be a mutable list\n\n   executing A:=MatrixAutomorphisms(matCwt); GG:=Intersection(Gp,A);\n```\n",
    "created_at": "2008-03-16T03:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17017",
    "user": "https://github.com/rlmill"
}
```

Michael Abshoff also noticed that this code is not very consistent. There are further issues with the `permutation_automorphism_group` function, but I'm not sure what's going on. Here is the traceback (if you just call this on random binary codes, it comes up pretty quickly):

```
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/rlmill/sage-2.10.3/<ipython console> in <module>()

/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in permutation_automorphism_group(self, mode)
   1447           gap.eval("Cwt:=Filtered(eltsC,c->WeightCodeword(c)=%s)"%wt)   ## bottleneck 2 (repeated 
   1448           gap.eval("matCwt:=List(Cwt,c->VectorCodeword(c))")            ##        for each i until stop = 1) 
-> 1449           gap.eval("A:=MatrixAutomorphisms(matCwt); GG:=Intersection(Gp,A)")    ## bottleneck 3
   1450           #print i," = i \n",gap.eval("matCwt")," = matCwt\n"
   1451           #print gap.eval("A")," = A \n",gap.eval("GG")," = GG\n\n"

/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)
    307         if len(x) == 0 or x[len(x) - 1] != ';':
    308             x += ';'
--> 309         s = Expect.eval(self, x)
    310         if newlines:
    311             return s

/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/rlmill/sage-2.10.3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    508                         return ''
    509                 else:
--> 510                     raise RuntimeError, message
    511 
    512         except KeyboardInterrupt:

<type 'exceptions.RuntimeError'>: Gap produced error output
Lists Assignment: <list> must be a mutable list

   executing A:=MatrixAutomorphisms(matCwt); GG:=Intersection(Gp,A);
```




---

archive/issue_comments_017018.json:
```json
{
    "body": "I have tried to create a patch incorporating 8866+8867+8868+8869, but based on 2.10.4.alpha0, as requested by the referee. Passes sage -testalll, except for a dsage failure,\ndevel/sage-coding1/sage/dsage/tests/testdoc.py, which I think is unrelated to this patch.\n\nRegarding the problem with permutation_automorphism_group, the plan of course is to drop that function and use Robert Miller's code instead. So \n(a) I'm not sure what the problem is since I can't figure out from the traceback above what paramaters were useb (\"just call this on random binary codes, it comes up pretty quickly\" isn't very\nspecific). \n(b) Since it will be deprecated ASAP, maybe this can be left until the next patch?",
    "created_at": "2008-03-16T12:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17018",
    "user": "https://github.com/wdjoyner"
}
```

I have tried to create a patch incorporating 8866+8867+8868+8869, but based on 2.10.4.alpha0, as requested by the referee. Passes sage -testalll, except for a dsage failure,
devel/sage-coding1/sage/dsage/tests/testdoc.py, which I think is unrelated to this patch.

Regarding the problem with permutation_automorphism_group, the plan of course is to drop that function and use Robert Miller's code instead. So 
(a) I'm not sure what the problem is since I can't figure out from the traceback above what paramaters were useb ("just call this on random binary codes, it comes up pretty quickly" isn't very
specific). 
(b) Since it will be deprecated ASAP, maybe this can be left until the next patch?



---

archive/issue_comments_017019.json:
```json
{
    "body": "I have found an example where permutation_automorphism_group mysteriously crashes. (In fact, the docstring there mentions that there is at least one such example already known.) Since this is a problem, I'm in the process of creating another patch which removes this code. I have no idea why the code crashes. It may have something to do with GAP variables being over-written but, unfortunately, I don't see a way to revise it in a GAP-friendlier way.",
    "created_at": "2008-03-16T13:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17019",
    "user": "https://github.com/wdjoyner"
}
```

I have found an example where permutation_automorphism_group mysteriously crashes. (In fact, the docstring there mentions that there is at least one such example already known.) Since this is a problem, I'm in the process of creating another patch which removes this code. I have no idea why the code crashes. It may have something to do with GAP variables being over-written but, unfortunately, I don't see a way to revise it in a GAP-friendlier way.



---

archive/issue_comments_017020.json:
```json
{
    "body": "I do not support removing the `permutation_automorphism_group` function.\n\nI see two reasons not to deprecate the other version. For one, it\nseems to work on non-binary codes, and further my version only runs on\nvery small codes. Second, I am still debugging my version, and it is\ngood to have another version to run examples on, to check for a\ndifference in output. It was while I was looking for such examples\nthat the weird traceback I got occurred.\n\nIt isn't generally the philosophy of Sage to delete a function because it has bugs. ;)",
    "created_at": "2008-03-16T17:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17020",
    "user": "https://github.com/rlmill"
}
```

I do not support removing the `permutation_automorphism_group` function.

I see two reasons not to deprecate the other version. For one, it
seems to work on non-binary codes, and further my version only runs on
very small codes. Second, I am still debugging my version, and it is
good to have another version to run examples on, to check for a
difference in output. It was while I was looking for such examples
that the weird traceback I got occurred.

It isn't generally the philosophy of Sage to delete a function because it has bugs. ;)



---

archive/issue_comments_017021.json:
```json
{
    "body": "Sorry if \"other version\" doesn't make sense in the above (this is opposed to `sage/coding/binary_code.pyx`, and was taken out of context- originally in an email discussion between David and me).",
    "created_at": "2008-03-16T17:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17021",
    "user": "https://github.com/rlmill"
}
```

Sorry if "other version" doesn't make sense in the above (this is opposed to `sage/coding/binary_code.pyx`, and was taken out of context- originally in an email discussion between David and me).



---

archive/issue_comments_017022.json:
```json
{
    "body": "Also, the instructions \"apply 8916+8917 to 2.10.4.alpha0\" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the \"flattened\" patches...",
    "created_at": "2008-03-16T17:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17022",
    "user": "https://github.com/rlmill"
}
```

Also, the instructions "apply 8916+8917 to 2.10.4.alpha0" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the "flattened" patches...



---

archive/issue_comments_017023.json:
```json
{
    "body": "Replying to [comment:14 rlm]:\n> Also, the instructions \"apply 8916+8917 to 2.10.4.alpha0\" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the \"flattened\" patches...\n\nThe patches at this ticket seem to become very messy. rlm: Can you delete patches that are no longer valid?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T18:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:14 rlm]:
> Also, the instructions "apply 8916+8917 to 2.10.4.alpha0" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the "flattened" patches...

The patches at this ticket seem to become very messy. rlm: Can you delete patches that are no longer valid?

Cheers,

Michael



---

archive/issue_comments_017024.json:
```json
{
    "body": "Done. Also, I'm removing my email from the cc field since I'm getting two copies for every change...",
    "created_at": "2008-03-16T18:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17024",
    "user": "https://github.com/rlmill"
}
```

Done. Also, I'm removing my email from the cc field since I'm getting two copies for every change...



---

archive/issue_comments_017025.json:
```json
{
    "body": "Aded a pacth to fix the problem mentioned by Michael concerning permutation_automorphism_group.\nPasses sage -testall, except for the dsage file mentioned above.\nThe function permutation_automorphism_group is still rather ugly, but at least this puts some lipstick on the pig and it doesn't barf on you half the time:-)",
    "created_at": "2008-03-17T00:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17025",
    "user": "https://github.com/wdjoyner"
}
```

Aded a pacth to fix the problem mentioned by Michael concerning permutation_automorphism_group.
Passes sage -testall, except for the dsage file mentioned above.
The function permutation_automorphism_group is still rather ugly, but at least this puts some lipstick on the pig and it doesn't barf on you half the time:-)



---

archive/issue_comments_017026.json:
```json
{
    "body": "OK, now that all this has been done, I'm trying to apply everything to sage 2.10.4.rc0. Hunks are failing all over the place. My suggestion is to rebase everything against 2.10.4 when it comes out, and we'll try again.",
    "created_at": "2008-03-17T03:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17026",
    "user": "https://github.com/rlmill"
}
```

OK, now that all this has been done, I'm trying to apply everything to sage 2.10.4.rc0. Hunks are failing all over the place. My suggestion is to rebase everything against 2.10.4 when it comes out, and we'll try again.



---

archive/issue_comments_017027.json:
```json
{
    "body": "The rebased patch is attached, as requested.",
    "created_at": "2008-03-18T00:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17027",
    "user": "https://github.com/wdjoyner"
}
```

The rebased patch is attached, as requested.



---

archive/issue_comments_017028.json:
```json
{
    "body": "Forgot to mention - it passes sage -testall.",
    "created_at": "2008-03-18T00:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17028",
    "user": "https://github.com/wdjoyner"
}
```

Forgot to mention - it passes sage -testall.



---

archive/issue_comments_017029.json:
```json
{
    "body": "David,\n\nYour stand alone patch *still* does not include `sd_codes.py`.  Please provide one flattened patch, on top of sage-2.10.4, which includes this file.",
    "created_at": "2008-03-18T00:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17029",
    "user": "https://github.com/rlmill"
}
```

David,

Your stand alone patch *still* does not include `sd_codes.py`.  Please provide one flattened patch, on top of sage-2.10.4, which includes this file.



---

archive/issue_comments_017030.json:
```json
{
    "body": "The last patch was missing sd_codes.py. This corrected rebased patch (attached) should work (I hope).",
    "created_at": "2008-03-18T03:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17030",
    "user": "https://github.com/wdjoyner"
}
```

The last patch was missing sd_codes.py. This corrected rebased patch (attached) should work (I hope).



---

archive/issue_comments_017031.json:
```json
{
    "body": "Ok, this last patch passes the bare minimum test: it applies cleanly to sage-2.10.4 and passes tests. I've deleted the rest of the noise.",
    "created_at": "2008-03-18T07:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17031",
    "user": "https://github.com/rlmill"
}
```

Ok, this last patch passes the bare minimum test: it applies cleanly to sage-2.10.4 and passes tests. I've deleted the rest of the noise.



---

archive/issue_comments_017032.json:
```json
{
    "body": "Attachment [8962coding.patch](tarball://root/attachments/some-uuid/ticket2514/8962coding.patch) by @rlmill created at 2008-03-20 00:15:07",
    "created_at": "2008-03-20T00:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17032",
    "user": "https://github.com/rlmill"
}
```

Attachment [8962coding.patch](tarball://root/attachments/some-uuid/ticket2514/8962coding.patch) by @rlmill created at 2008-03-20 00:15:07



---

archive/issue_comments_017033.json:
```json
{
    "body": "I have replaced the patch with one in which all new comments use only one # instead of the highly annoying ##. In the future, patches with ## will be automatically rejected. I think mabshoff has a bigger problem with these than I do, but I don't want to go through it again.\n\nAlso, I notice that in this new patch, `permutation_automorphism_group` is once again commented out. I thought we agreed not to do that...\n\nIn `sd_codes.py`, you have a function to return the codes of a certain length, yet when the function is called, the data for *all* lengths is prepared, before the data of the specified length is returned (and the rest thrown away). Why doesn't this style of coding bother you!?\n\nAny docstring containing LaTeX should be a raw string ( i.e. `r\"\"\"` ). I have added a patch which does this.",
    "created_at": "2008-03-20T00:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17033",
    "user": "https://github.com/rlmill"
}
```

I have replaced the patch with one in which all new comments use only one # instead of the highly annoying ##. In the future, patches with ## will be automatically rejected. I think mabshoff has a bigger problem with these than I do, but I don't want to go through it again.

Also, I notice that in this new patch, `permutation_automorphism_group` is once again commented out. I thought we agreed not to do that...

In `sd_codes.py`, you have a function to return the codes of a certain length, yet when the function is called, the data for *all* lengths is prepared, before the data of the specified length is returned (and the rest thrown away). Why doesn't this style of coding bother you!?

Any docstring containing LaTeX should be a raw string ( i.e. `r"""` ). I have added a patch which does this.



---

archive/issue_comments_017034.json:
```json
{
    "body": "Attachment [2514-docs.patch](tarball://root/attachments/some-uuid/ticket2514/2514-docs.patch) by @rlmill created at 2008-03-20 00:36:54\n\nPS- Please post the suggested changes in a single patch on top of sage-2.10.4 plus the two patches here.",
    "created_at": "2008-03-20T00:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17034",
    "user": "https://github.com/rlmill"
}
```

Attachment [2514-docs.patch](tarball://root/attachments/some-uuid/ticket2514/2514-docs.patch) by @rlmill created at 2008-03-20 00:36:54

PS- Please post the suggested changes in a single patch on top of sage-2.10.4 plus the two patches here.



---

archive/issue_comments_017035.json:
```json
{
    "body": "Arrgghh. We not only agreed that I put perm_aut_gp back in - I actually worked hard to patch that\nprogram up so it worked correctly. I'm obviously not doing a good job with creating patches.\nI'll try again...",
    "created_at": "2008-03-20T01:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17035",
    "user": "https://github.com/wdjoyner"
}
```

Arrgghh. We not only agreed that I put perm_aut_gp back in - I actually worked hard to patch that
program up so it worked correctly. I'm obviously not doing a good job with creating patches.
I'll try again...



---

archive/issue_comments_017036.json:
```json
{
    "body": "The attached patch I think does what you want.\n\n(a) It passes sage -testall on sage-2.10.4+your two patches above,\n(b) all \"## blah\" and \"#blah\" were replaced by \"# blah\",\n(c) it contains the fixed version of perm_aut_gp - for example\n\n\n```\nsage: for i in range(100):\n....:     C = RandomLinearCode( 20, 10, GF(2) )\n....:     print i, \", G= \", C.permutation_automorphism_group()\n....:\n0 , G=  Permutation Group with generators [()]\n1 , G=  Permutation Group with generators [()]\n2 , G=  Permutation Group with generators [()]\n3 , G=  Permutation Group with generators [(12,15), (2,12)]\n...\n```\n\nruns without crashing,\n(d) regarding your comment:\n\n\n```\nIn sd_codes.py, you have a function to return the codes of a certain length, yet when the function is called, the data for *all* lengths is prepared, before the data of the specified length is returned (and the rest thrown away). Why doesn't this style of coding bother you!?\n```\n\nI need further explanation. I wrote that file with the following goals in mind:\n(i) the file should be human readable,\n(ii)the entries should contain enough information to determine the sd codes uniquely\n(iii) the entries should contain all the \"expensive\" computations (eg, spectrum, aut gp order)\n(iv) a new entry should be easy to add by *someone else*.\nSo, that is the (subjective) basis for the data structures. If I understand your comment correctly, you are implying that\n\n```\nsage: C = self_dual_codes_binary(10)\n```\n\ncomputes information for (as an example) the sd codes of length n=8 and throws that out before returning the output. I simply do not understand how that is correct. The program is simply a case-by-case program which, in this example, reads off n as 10 and then proceeds to construct the dictionary of inequivalent self-dual binary codes of length 10 (and only 10). At least, unless I'm misunderstanding how Python works, that is what I think it does.\n\nHope this works this time!",
    "created_at": "2008-03-20T10:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17036",
    "user": "https://github.com/wdjoyner"
}
```

The attached patch I think does what you want.

(a) It passes sage -testall on sage-2.10.4+your two patches above,
(b) all "## blah" and "#blah" were replaced by "# blah",
(c) it contains the fixed version of perm_aut_gp - for example


```
sage: for i in range(100):
....:     C = RandomLinearCode( 20, 10, GF(2) )
....:     print i, ", G= ", C.permutation_automorphism_group()
....:
0 , G=  Permutation Group with generators [()]
1 , G=  Permutation Group with generators [()]
2 , G=  Permutation Group with generators [()]
3 , G=  Permutation Group with generators [(12,15), (2,12)]
...
```

runs without crashing,
(d) regarding your comment:


```
In sd_codes.py, you have a function to return the codes of a certain length, yet when the function is called, the data for *all* lengths is prepared, before the data of the specified length is returned (and the rest thrown away). Why doesn't this style of coding bother you!?
```

I need further explanation. I wrote that file with the following goals in mind:
(i) the file should be human readable,
(ii)the entries should contain enough information to determine the sd codes uniquely
(iii) the entries should contain all the "expensive" computations (eg, spectrum, aut gp order)
(iv) a new entry should be easy to add by *someone else*.
So, that is the (subjective) basis for the data structures. If I understand your comment correctly, you are implying that

```
sage: C = self_dual_codes_binary(10)
```

computes information for (as an example) the sd codes of length n=8 and throws that out before returning the output. I simply do not understand how that is correct. The program is simply a case-by-case program which, in this example, reads off n as 10 and then proceeds to construct the dictionary of inequivalent self-dual binary codes of length 10 (and only 10). At least, unless I'm misunderstanding how Python works, that is what I think it does.

Hope this works this time!



---

archive/issue_comments_017037.json:
```json
{
    "body": "Attachment [8964.patch](tarball://root/attachments/some-uuid/ticket2514/8964.patch) by @wdjoyner created at 2008-03-20 10:50:31\n\napply 8962coding.patch+2514-docs.patch+this to 2.10.4.",
    "created_at": "2008-03-20T10:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17037",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [8964.patch](tarball://root/attachments/some-uuid/ticket2514/8964.patch) by @wdjoyner created at 2008-03-20 10:50:31

apply 8962coding.patch+2514-docs.patch+this to 2.10.4.



---

archive/issue_comments_017038.json:
```json
{
    "body": "David,\n\nApologies, I haven't slept much this week :-). I misread the code- I thought one big dict was getting built. I guess the real thing is that the code is very hard to read. There are several databases included with Sage, and they are not source-code databases. That is a very strange choice to me.\n\nSome of your doctests have `<BLANKLINE>`'s after the commands. Things look better, and you'll be more consistent with the rest of the source code in Sage, if you simply remove these lines. The doctests should still pass the same. It's a little jarring for someone reading the docs.\n\nWhy are the minimum distance bound functions commented out?\n\nThe rest of the code looks pretty good. As I've indicated, I give this patch a positive review, modulo the few issues mentioned, but you're going to need to get a second opinion from someone else.",
    "created_at": "2008-03-20T12:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17038",
    "user": "https://github.com/rlmill"
}
```

David,

Apologies, I haven't slept much this week :-). I misread the code- I thought one big dict was getting built. I guess the real thing is that the code is very hard to read. There are several databases included with Sage, and they are not source-code databases. That is a very strange choice to me.

Some of your doctests have `<BLANKLINE>`'s after the commands. Things look better, and you'll be more consistent with the rest of the source code in Sage, if you simply remove these lines. The doctests should still pass the same. It's a little jarring for someone reading the docs.

Why are the minimum distance bound functions commented out?

The rest of the code looks pretty good. As I've indicated, I give this patch a positive review, modulo the few issues mentioned, but you're going to need to get a second opinion from someone else.



---

archive/issue_comments_017039.json:
```json
{
    "body": "apply all 4 (in order) to 2.10.4",
    "created_at": "2008-03-20T14:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17039",
    "user": "https://github.com/wdjoyner"
}
```

apply all 4 (in order) to 2.10.4



---

archive/issue_comments_017040.json:
```json
{
    "body": "Attachment [8965.patch](tarball://root/attachments/some-uuid/ticket2514/8965.patch) by @wdjoyner created at 2008-03-20 14:28:16\n\nrlm:\n\n```\nI guess the real thing is that the code is very hard to read. There are several databases included with Sage, and they are not source-code databases. That is a very strange choice to me.\n```\n\nwdj:\nI wanted it human-readable (maybe I can get a student to work on it, if I'm lucky) since it is so incomplete. I needed a table of data to test certain conjectures against. This fit the bill. When it is more complete, another format might be more suitable.\n\nrlm:\n\n```\nSome of your doctests have <BLANKLINE>'s after the commands. Things look better, and you'll be more consistent with the rest of the source code in Sage, if you simply remove these lines. The doctests should still pass the same. It's a little jarring for someone reading the docs.\n\nWhy are the minimum distance bound functions commented out? \n```\n\nwdj:\nThe BLANKLINES are all removed and the patch has been retested (and passes). I removed the\ncommented out minimum distance bound functions several versions ago. (I think someone else commented them out when Brouwer's tables went down some time ago. I never bothered to delete them until recently.)\n\nrlm:\n\n```\nThe rest of the code looks pretty good. As I've indicated, I give this patch a positive review, modulo the few issues mentioned, but you're going to need to get a second opinion from someone else.\n```\n\nwdj:\nSorry, I misunderstood again. When I asked you if you objected to a \"code bomb\", I was assuming that you were the only referee. Since you said no, you didn't mind, I submitted it.",
    "created_at": "2008-03-20T14:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17040",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [8965.patch](tarball://root/attachments/some-uuid/ticket2514/8965.patch) by @wdjoyner created at 2008-03-20 14:28:16

rlm:

```
I guess the real thing is that the code is very hard to read. There are several databases included with Sage, and they are not source-code databases. That is a very strange choice to me.
```

wdj:
I wanted it human-readable (maybe I can get a student to work on it, if I'm lucky) since it is so incomplete. I needed a table of data to test certain conjectures against. This fit the bill. When it is more complete, another format might be more suitable.

rlm:

```
Some of your doctests have <BLANKLINE>'s after the commands. Things look better, and you'll be more consistent with the rest of the source code in Sage, if you simply remove these lines. The doctests should still pass the same. It's a little jarring for someone reading the docs.

Why are the minimum distance bound functions commented out? 
```

wdj:
The BLANKLINES are all removed and the patch has been retested (and passes). I removed the
commented out minimum distance bound functions several versions ago. (I think someone else commented them out when Brouwer's tables went down some time ago. I never bothered to delete them until recently.)

rlm:

```
The rest of the code looks pretty good. As I've indicated, I give this patch a positive review, modulo the few issues mentioned, but you're going to need to get a second opinion from someone else.
```

wdj:
Sorry, I misunderstood again. When I asked you if you objected to a "code bomb", I was assuming that you were the only referee. Since you said no, you didn't mind, I submitted it.



---

archive/issue_comments_017041.json:
```json
{
    "body": "\n```\nSorry, I misunderstood again. When I asked you if you\nobjected to a \"code bomb\", I was assuming that you were\nthe only referee. Since you said no, you didn't mind, I\nsubmitted it.\n```\n\n\nThis isn't *that* much of a code bomb-- the problem is really that my judgment has kind of fuzzed over, due to exhaustion. I give things as they are a positive review, so all you need is another set of eyes to go over the code and make sure there aren't any blatant issues I might have missed.",
    "created_at": "2008-03-20T19:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17041",
    "user": "https://github.com/rlmill"
}
```


```
Sorry, I misunderstood again. When I asked you if you
objected to a "code bomb", I was assuming that you were
the only referee. Since you said no, you didn't mind, I
submitted it.
```


This isn't *that* much of a code bomb-- the problem is really that my judgment has kind of fuzzed over, due to exhaustion. I give things as they are a positive review, so all you need is another set of eyes to go over the code and make sure there aren't any blatant issues I might have missed.



---

archive/issue_comments_017042.json:
```json
{
    "body": "Hi David,\n\nI did mention some of my concern with this patch to rlm in IRC (the \"##\" issue, the missing raw docstrings and the less than elegant form of sage/coding/sd_codes.py) and since those have been taken care of I am satisfied. I did look around some more in the docstring and while a bunch of TeX markers are missing and there probably will be TeX problems once we build the documentation I am still giving this a positive review. I also assume that the doctests are correct, I didn't check with Guava to verify any of them.\n\nWhat is needed in the future:\n\n* somebody ought to take a general design of the this subsystem. Not that I am aware of any deficiancies\n* we need somebody else how intensively uses the subsystem to shake out bugs\n* please submit incremental, small patches instead of monster patches in the future. It makes review and integration much easier\n\nAs you wrote above \"The function permutation_automorphism_group is still rather ugly, but at least this puts some lipstick on the pig and it doesn't barf on you half the time\" I see this as a chance to get the code in shape :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T05:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17042",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi David,

I did mention some of my concern with this patch to rlm in IRC (the "##" issue, the missing raw docstrings and the less than elegant form of sage/coding/sd_codes.py) and since those have been taken care of I am satisfied. I did look around some more in the docstring and while a bunch of TeX markers are missing and there probably will be TeX problems once we build the documentation I am still giving this a positive review. I also assume that the doctests are correct, I didn't check with Guava to verify any of them.

What is needed in the future:

* somebody ought to take a general design of the this subsystem. Not that I am aware of any deficiancies
* we need somebody else how intensively uses the subsystem to shake out bugs
* please submit incremental, small patches instead of monster patches in the future. It makes review and integration much easier

As you wrote above "The function permutation_automorphism_group is still rather ugly, but at least this puts some lipstick on the pig and it doesn't barf on you half the time" I see this as a chance to get the code in shape :)

Cheers,

Michael



---

archive/issue_comments_017043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T05:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017044.json:
```json
{
    "body": "Merged all four patches in Sage 2.11.alpha1. If anybody has issues with this patch please open another ticket as a follow up since this ticket as is is messy enough.",
    "created_at": "2008-03-21T05:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2514#issuecomment-17044",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 2.11.alpha1. If anybody has issues with this patch please open another ticket as a follow up since this ticket as is is messy enough.
