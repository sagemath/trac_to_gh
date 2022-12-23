# Issue 8792: clean up documentation of logic/booleval.py

Issue created by migration from https://trac.sagemath.org/ticket/8792

Original creator: mvngu

Original creation time: 2010-04-28 06:49:40

Assignee: mvngu

CC:  leif

As the subject says.


---

Comment by mvngu created at 2010-05-03 04:04:32

Changing status from new to needs_review.


---

Attachment

Changes in the patch include:

 * Add `sage/logic/booleval.py` to the reference manual.
 * Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/).
 * Avoid using the name `vars` of a built-in function for a variable name.


---

Comment by ncohen created at 2010-05-19 20:12:40

If I'm not mistaken, this patch does not apply against the brand new 4.4.2 with #8796 ^^;

Nathann


---

Comment by ncohen created at 2010-05-19 20:12:40

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-05-20 08:52:34

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-05-20 08:52:34

Replying to [comment:3 ncohen]:
> If I'm not mistaken, this patch does not apply against the brand new 4.4.2 with #8796 ^^;

Could you try again? Here is how I applied the relevant patches:


```sh
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sandbox/sage-4.4.2-8792-booleval/devel/sage-main
[mvngu@sage sage-main]$ hg tip
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8796/trac_8796-propcalc-clean-ups.patch && hg qpush 
adding trac_8796-propcalc-clean-ups.patch to series file
applying trac_8796-propcalc-clean-ups.patch
now at: trac_8796-propcalc-clean-ups.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8792/trac_8792-booleval-clean-ups.patch && hg qpush 
adding trac_8792-booleval-clean-ups.patch to series file
applying trac_8792-booleval-clean-ups.patch
now at: trac_8792-booleval-clean-ups.patch
[mvngu@sage sage-main]$ hg tip
changeset:   14323:a91966275ff3
tag:         qtip
tag:         trac_8792-booleval-clean-ups.patch
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Sun May 02 20:59:37 2010 -0700
summary:     #8792: clean up documentation of logic/booleval.py
```



---

Comment by ncohen created at 2010-05-20 18:21:47

Hmmmm... I'm really sorry but ... 

```
~/.Sage/devel/sage-doc$ pwd
/home/ncohen/.Sage/devel/sage-doc
~/.Sage/devel/sage-doc$ hg tip
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

~/.Sage/devel/sage-doc$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8796/trac_8796-propcalc-clean-ups.patch && hg qpush
adding trac_8796-propcalc-clean-ups.patch to series file
applying trac_8796-propcalc-clean-ups.patch
now at: trac_8796-propcalc-clean-ups.patch
~/.Sage/devel/sage-doc$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8792/trac_8792-booleval-clean-ups.patch && hg qpush
adding trac_8792-booleval-clean-ups.patch to series file
applying trac_8792-booleval-clean-ups.patch
patching file sage/logic/booleval.py
Hunk #6 FAILED at 111
1 out of 6 hunks FAILED -- saving rejects to file sage/logic/booleval.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8792-booleval-clean-ups.patch
~/.Sage/devel/sage-doc$ hg tip
changeset:   14323:fd8399a20ce0
tag:         qtip
tag:         trac_8792-booleval-clean-ups.patch
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Sun May 02 20:59:37 2010 -0700
summary:     #8792: clean up documentation of logic/booleval.py
```


is there anything I am doing wrong ? O_o


---

Comment by ncohen created at 2010-05-20 18:23:42

The rejects are all the fixes (a==b) => a == b at the end of your patch O_o

Nathann


---

Comment by jthurber created at 2010-11-03 04:29:32

Replying to [comment:6 ncohen]:
> The rejects are all the fixes (a==b) => a == b at the end of your patch O_o
> 
> Nathann


Hi,

I'm new to development and thought this patch looked like a good place to start. I got the same error message as Nathann. Is this patch still receiving attention?

John


---

Comment by leif created at 2010-11-03 05:06:03

Replying to [comment:8 jthurber]:
> I'm new to development and thought this patch looked like a good place to start. I got the same error message as Nathann. Is this patch still receiving attention?

By commenting on the ticket, it does. ;-)

Though I personally currently have no time for it. Feel free to review it / upload a reviewer patch and we'll see...

P.S.: If the current patch doesn't apply cleanly, the ticket's status should be set to "needs work" until the patch has been rebased.


---

Comment by leif created at 2010-11-03 05:27:42


```sh
$ hg import -v ~/Sage/patches/trac_8792-booleval-clean-ups.patch 
applying /home/leif/Sage/patches/trac_8792-booleval-clean-ups.patch
patching file doc/en/reference/logic.rst
patching file sage/logic/booleval.py
doc/en/reference/logic.rst
sage/logic/booleval.py
```


(This is with Sage 4.6. Documentation apparently builds ok, too, doctests pass.)


---

Comment by was created at 2010-11-03 19:57:05

It also works for me with sage-4.6.


---

Comment by jthurber created at 2010-11-05 14:44:39


```
07:26:25johnthurber~/sage/sage-4.6/devel/sage-test$ hg qimport ~/sage/patches/trac_8792-booleval-clean-ups-2.patch 
adding trac_8792-booleval-clean-ups-2.patch to series file
07:34:56johnthurber~/sage/sage-4.6/devel/sage-test$ hg qpush
applying trac_8792-booleval-clean-ups-2.patch
patching file sage/logic/booleval.py
Hunk #6 FAILED at 111
1 out of 6 hunks FAILED -- saving rejects to file sage/logic/booleval.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8792-booleval-clean-ups-2.patch
```


I wondered if it was my download technique, but I've tried it a couple of ways, including 


```
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8792/trac_8792-booleval-clean-ups.patch
```


so, unless someone has another suggestion, I will go ahead and suggest this needs to be rebased.


---

Comment by was created at 2010-11-09 01:06:40

Hi,

I figured it out.  jthurber is using hg version 1.6, whereas Sage uses hg version 1.3.  With 1.6 the algorithm for accepting hunks has been tightened (surely a good thing!) and the patch fails to apply, whereas it does apply with hg version 1.3.


---

Comment by jthurber created at 2010-11-10 18:07:46

Changing status from needs_review to positive_review.


---

Comment by jthurber created at 2010-11-10 18:07:46

Positive review, though there was one test timeout failure which passed when isolated from --testall.

--testall --long led to 


```
sage -t  --long -force_lib "devel/sage/sage/modular/ssmod/ssmod.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
```


I isolated this test, it passed:


```
07:36:53johnthurber~/sage/sage-4.6$ sage -t  --long -force_lib "devel/sage/sage/modular/ssmod/ssmod.py"
sage -t --long -force_lib "devel/sage/sage/modular/ssmod/ssmod.py"
	 [276.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 276.0 seconds
}}


---

Comment by jdemeyer created at 2010-11-11 13:39:21

jthurber: Please add your real name as "Reviewer" and also on [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames)


---

Comment by jdemeyer created at 2010-11-11 19:37:16

Resolution: fixed
