# Issue 2514: additions to coding modules

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-03-13 23:51:40

Assignee: rlm

I have a number of changes to the modules in coding. With permission of Robert Miller, it is rather large ("code bomb"). However, most are guava wrappers, rewritten as pure Python/SAGE functions. 


---

Comment by wdj created at 2008-03-14 18:21:21

New patch added to address comments by referee. I think you have to apply the first patch and then the second patch to 2.10.3.


---

Comment by wdj created at 2008-03-14 18:34:39

Forgot to add: the patch 8866+8867 passes sage -testall.


---

Comment by wdj created at 2008-03-15 14:36:50

Added one more patch to address problems noticed by the referee. When running sage -testall,
I noticed another problem. One of the functions requires an internet connection (it goes to codetables.de and fetches data). At this moment, that site is down, so the test failed.
I added the comment "## requires internet, long time" since timing out raises a socket.error.
This is the content of the last patch.
8866+8867+8868+8869 get applied to 2.10.3. Please let me know if it is 
preferable to make a patch for 2.10.4.alpha0 instead.


---

Comment by rlm created at 2008-03-15 18:10:58

For doctests that require internet, "optional" instead of "long time" is the usual flag used. As observed by Mike Hansen, this apparently the standard, as you find when doing `search_src('internet')`.  This is the only remaining issue for this ticket. I have not tried testall with the patches in this ticket, but I have tested `sage/coding`. If the author fixes the doctest comment, and does testall with all of the patches on a fresh 2.10.4.alpha0, then that's a positive review from me.

Very good work here.


---

Comment by rlm created at 2008-03-15 23:25:38

Oops,

```
sage: C = LinearCode(Matrix(GF(2),[This is the Trac macro *0,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,1-macro)))
sage: C.permutation_automorphism_group()
*BOOM*
```

This is probably just not checking for trivial generators or something. I don't think these patches introduced this, but it's very closely related...


---

Comment by rlm created at 2008-03-15 23:38:32

In fact, the problem above is caused by exactly that: in this case, `gens` is an empty list, and `PermutationGroup`s don't like those.


---

Comment by wdj created at 2008-03-16 01:11:54

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

Comment by rlm created at 2008-03-16 03:23:32

Regarding the `QuasiQuadraticResidueCode`, see #2541.


---

Comment by rlm created at 2008-03-16 03:45:42

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

Comment by wdj created at 2008-03-16 12:42:59

I have tried to create a patch incorporating 8866+8867+8868+8869, but based on 2.10.4.alpha0, as requested by the referee. Passes sage -testalll, except for a dsage failure,
devel/sage-coding1/sage/dsage/tests/testdoc.py, which I think is unrelated to this patch.

Regarding the problem with permutation_automorphism_group, the plan of course is to drop that function and use Robert Miller's code instead. So 
(a) I'm not sure what the problem is since I can't figure out from the traceback above what paramaters were useb ("just call this on random binary codes, it comes up pretty quickly" isn't very
specific). 
(b) Since it will be deprecated ASAP, maybe this can be left until the next patch?


---

Comment by wdj created at 2008-03-16 13:35:40

I have found an example where permutation_automorphism_group mysteriously crashes. (In fact, the docstring there mentions that there is at least one such example already known.) Since this is a problem, I'm in the process of creating another patch which removes this code. I have no idea why the code crashes. It may have something to do with GAP variables being over-written but, unfortunately, I don't see a way to revise it in a GAP-friendlier way.


---

Comment by rlm created at 2008-03-16 17:34:25

I do not support removing the `permutation_automorphism_group` function.

I see two reasons not to deprecate the other version. For one, it
seems to work on non-binary codes, and further my version only runs on
very small codes. Second, I am still debugging my version, and it is
good to have another version to run examples on, to check for a
difference in output. It was while I was looking for such examples
that the weird traceback I got occurred.

It isn't generally the philosophy of Sage to delete a function because it has bugs. ;)


---

Comment by rlm created at 2008-03-16 17:35:48

Sorry if "other version" doesn't make sense in the above (this is opposed to `sage/coding/binary_code.pyx`, and was taken out of context- originally in an email discussion between David and me).


---

Comment by rlm created at 2008-03-16 17:43:03

Also, the instructions "apply 8916+8917 to 2.10.4.alpha0" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the "flattened" patches...


---

Comment by mabshoff created at 2008-03-16 18:06:00

Replying to [comment:14 rlm]:
> Also, the instructions "apply 8916+8917 to 2.10.4.alpha0" omit that you also need to apply 8868.patch, or else Sage will not even start up properly! sd_codes was not added to the "flattened" patches...

The patches at this ticket seem to become very messy. rlm: Can you delete patches that are no longer valid?

Cheers,

Michael


---

Comment by rlm created at 2008-03-16 18:39:58

Done. Also, I'm removing my email from the cc field since I'm getting two copies for every change...


---

Comment by wdj created at 2008-03-17 00:36:01

Aded a pacth to fix the problem mentioned by Michael concerning permutation_automorphism_group.
Passes sage -testall, except for the dsage file mentioned above.
The function permutation_automorphism_group is still rather ugly, but at least this puts some lipstick on the pig and it doesn't barf on you half the time:-)


---

Comment by rlm created at 2008-03-17 03:01:54

OK, now that all this has been done, I'm trying to apply everything to sage 2.10.4.rc0. Hunks are failing all over the place. My suggestion is to rebase everything against 2.10.4 when it comes out, and we'll try again.


---

Comment by wdj created at 2008-03-18 00:01:53

The rebased patch is attached, as requested.


---

Comment by wdj created at 2008-03-18 00:02:24

Forgot to mention - it passes sage -testall.


---

Comment by rlm created at 2008-03-18 00:19:37

David,

Your stand alone patch *still* does not include `sd_codes.py`.  Please provide one flattened patch, on top of sage-2.10.4, which includes this file.


---

Comment by wdj created at 2008-03-18 03:32:43

The last patch was missing sd_codes.py. This corrected rebased patch (attached) should work (I hope).


---

Comment by rlm created at 2008-03-18 07:06:21

Ok, this last patch passes the bare minimum test: it applies cleanly to sage-2.10.4 and passes tests. I've deleted the rest of the noise.


---

Attachment


---

Comment by rlm created at 2008-03-20 00:35:26

I have replaced the patch with one in which all new comments use only one # instead of the highly annoying ##. In the future, patches with ## will be automatically rejected. I think mabshoff has a bigger problem with these than I do, but I don't want to go through it again.

Also, I notice that in this new patch, `permutation_automorphism_group` is once again commented out. I thought we agreed not to do that...

In `sd_codes.py`, you have a function to return the codes of a certain length, yet when the function is called, the data for *all* lengths is prepared, before the data of the specified length is returned (and the rest thrown away). Why doesn't this style of coding bother you!?

Any docstring containing LaTeX should be a raw string ( i.e. `r"""` ). I have added a patch which does this.


---

Attachment

PS- Please post the suggested changes in a single patch on top of sage-2.10.4 plus the two patches here.


---

Comment by wdj created at 2008-03-20 01:26:58

Arrgghh. We not only agreed that I put perm_aut_gp back in - I actually worked hard to patch that
program up so it worked correctly. I'm obviously not doing a good job with creating patches.
I'll try again...


---

Comment by wdj created at 2008-03-20 10:48:55

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

Attachment

apply 8962coding.patch+2514-docs.patch+this to 2.10.4.


---

Comment by rlm created at 2008-03-20 12:42:28

David,

Apologies, I haven't slept much this week :-). I misread the code- I thought one big dict was getting built. I guess the real thing is that the code is very hard to read. There are several databases included with Sage, and they are not source-code databases. That is a very strange choice to me.

Some of your doctests have `<BLANKLINE>`'s after the commands. Things look better, and you'll be more consistent with the rest of the source code in Sage, if you simply remove these lines. The doctests should still pass the same. It's a little jarring for someone reading the docs.

Why are the minimum distance bound functions commented out?

The rest of the code looks pretty good. As I've indicated, I give this patch a positive review, modulo the few issues mentioned, but you're going to need to get a second opinion from someone else.


---

Comment by wdj created at 2008-03-20 14:21:10

apply all 4 (in order) to 2.10.4


---

Attachment

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

Comment by rlm created at 2008-03-20 19:25:54


```
Sorry, I misunderstood again. When I asked you if you
objected to a "code bomb", I was assuming that you were
the only referee. Since you said no, you didn't mind, I
submitted it.
```


This isn't *that* much of a code bomb-- the problem is really that my judgment has kind of fuzzed over, due to exhaustion. I give things as they are a positive review, so all you need is another set of eyes to go over the code and make sure there aren't any blatant issues I might have missed.


---

Comment by mabshoff created at 2008-03-21 05:31:02

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

Comment by mabshoff created at 2008-03-21 05:32:46

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 05:32:46

Merged all four patches in Sage 2.11.alpha1. If anybody has issues with this patch please open another ticket as a follow up since this ticket as is is messy enough.
