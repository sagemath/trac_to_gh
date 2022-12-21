# Issue 6647: Permutation Group improvements

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2009-07-28 12:10:21

Assignee: nborie

CC:  sage-combinat

Keywords: permutationgroup, orbit, stabilizer, transversal

Add transversal, orbit, stabilizer to PermutationGroup sage object.


---

Attachment


---

Comment by wdj created at 2009-07-28 14:06:09

This is a nice addition. I have a question though.

In the docstring for a transversal, you have `Return a list of representatives of the orbit of the given integer in the group.` The usual definition (as one finds for example in wikipedia) is `... given a subgroup H of a group G, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H.`. I'm just wondering if this docstring is a bit confusing?


---

Comment by nborie created at 2009-07-28 14:20:59

Hello wdj,

This is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...

My English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.

The reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.


---

Comment by wdj created at 2009-07-28 18:55:10

Replying to [comment:5 nborie]:
> Hello wdj,
> 
> This is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...
> 
> My English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.
> 
> The reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.


I would replace `Return a list of representatives of the orbit of the given integer in the group` by 
`If G is a permutation group acting on the set X = {1, 2, ...., n} and H is the stabilizer subgroup of <integer>, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H. This method returns a right transversal of G by H.`

However, if this is to be reviewed by applying 6620 and then this patch, I can tell you that I had a problem 
doing that.


---

Comment by nborie created at 2009-08-12 14:05:34

Changing keywords from "permutationgroup, orbit, stabilizer, transversal" to "permutationgroup, orbit, stabilizer, transversal, strong generating system".


---

Comment by nborie created at 2009-08-12 14:05:34

Add a strong generating system method.

I really need this method and so, this first implementation is not very good. The data structure (list of list) is dense and perhaps not very adapted (the python list begin at zero and the structure should be in correlation with positions and integer...(Dictionary? , family?, ...) ). This is really not optimized (I am waiting for LinGap...). If it goes in Sage as a first version, one could easily improve it...  
 
Comments, corrections, suggestions welcome!

Wdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...


---

Comment by wdj created at 2009-08-12 14:10:17

Replying to [comment:8 nborie]:
> Add a strong generating system method.
> 
...
> 
> Wdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...

I've forgotten now the exact problem. I guess hg_sage.apply did not work for me. What does "the sage-combinat queue" mean? Does sage-combinat have their own trac system?


---

Comment by nborie created at 2009-08-12 14:28:15

We just work with in special branch with a special mercurial queue I think... (the system is so complicated...)


```
nicolas`@`Lancelot:/opt/sage/devel/sage-combinat$ hg qtop
trac_6647_permutationgroup_improvement.patch
nicolas`@`Lancelot:/opt/sage/devel/sage-combinat$ hg qpop
Now at: trac_6620.patch
nicolas`@`Lancelot:/opt/sage/devel/sage-combinat$ hg qpush
applying trac_6647_permutationgroup_improvement.patch
Now at: trac_6647_permutationgroup_improvement.patch
nicolas`@`Lancelot:/opt/sage/devel/sage-combinat$ sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.28746032715e-05 seconds
Finished compiling Cython code (time = 0.407410144806 seconds)
running install
running build
running build_py
copying sage/groups/perm_gps/permgroup.py -> build/lib.linux-i686-2.6/sage/groups/perm_gps
running build_ext
Total time spent compiling C/C++ extensions:  0.0105719566345 seconds.
running install_lib
copying build/lib.linux-i686-2.6/sage/groups/perm_gps/permgroup.py -> /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps
byte-compiling /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup.py to permgroup.pyc
running install_egg_info
Removing /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.391s
user	0m1.132s
sys	0m0.252s
nicolas`@`Lancelot:/opt/sage/devel/sage-combinat$ 
```


hg = hg_sage in my shell

I never use hg apply in fact as I work every times with the shared combinat branch and repository...
--> http://combinat.sagemath.org/patches/


---

Comment by nborie created at 2009-08-13 10:52:43

I fix a problem : any stabilizer must have the same degree of the permgroup in argument. I hardcoded that because I don't know how to do that in a better way...


---

Comment by wdj created at 2009-08-13 10:57:32

I wonder if this patch was been submitted to the wrong trac system. I guess what the author is saying in some comments above is that the patch is to be applied to the sage-combinat version of sage, not the "standard" version. If that is correct, then either the patch should be submitted t the sage-combinat trac or rebased for the "standard" version. If that is not correct, then a better explanation of why it does not apply to the "standard" sage could be helpful.


---

Comment by nborie created at 2009-08-13 11:08:04

I am very sorry for all the misunderstanding I produce... I think there is only one trac and only one sage. Franco or Nicolas (Thiéry) could say that better than me but i think we work with a special repository but we try to say the closer we can to the real sage version. I think that is my fault and and should try to work with different version of sage on my computer. I really should based that for the standard version... I really think there is only one way to go in sage (the trac, the only...).

Sorry and thank for your comments. I continue my formation on sage...


---

Comment by nborie created at 2009-08-13 15:10:12

I installed a new sage 4.1 and applyed only #6620 and #6647... It seems to work for me.

```
nicolas`@`Lancelot:~/sage_standard$ ./sage -t devel/sage-main/sage/groups/perm_gps/permgroup.py
sage -t  "devel/sage-main/sage/groups/perm_gps/permgroup.py"
	 [5.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.0 seconds
nicolas`@`Lancelot:~/sage_standard$ 
```

I must disturb the combinat guys too because the combinat wiki don't say how to interface from combinat patches to trac patches. If someone can tell me how it would normally work...


---

Comment by wdj created at 2009-08-14 00:49:20

This still doesn't work for me. I don't understand the problem. On 4.1.alpha3, I ran


```
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/trac_6620.patch")
```

This worked fine. Then I ran


```
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/trac_6647_permutationgroup_improvement_2.patch")
```

but this did not apply and instead opened up vi. I aborted the patch, since I didn't know what else to do.


---

Attachment


---

Comment by nborie created at 2009-08-16 15:53:06

I hope it will be Ok now. Jason Bandlow noticed that hg informations was missing in my patches. Beginner mystake : I did not export my patches (hg export) but just upload the files from .hg/patches to the trac. Sorry for that...


---

Comment by wdj created at 2009-08-18 19:31:00

This (and the dependency #6620) applied fine to 4.1.1.rc2, on an intel macbook running 10.4.11. Although sage -testall gave


```
The following tests failed:


        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

I think these are unrelated (and known) failures.

Docstrings look good. Positive review from me. Are there other tests (eg, other platforms) needed to run before changing :needs" to "positive"?


---

Attachment

reviewer patch; fix ReST formatting typos


---

Comment by mvngu created at 2009-08-25 02:05:46

The patch `trac_6647-reviewer.patch` fixes some ReST formatting typos found in `trac_6647_permutationgroup_improvement_2.patch`. Such typos result in warnings when building the reference manual. If people are happy with the changes in `trac_6647-reviewer.patch`, then patches should be merged in this order:

 1. `trac_6647_permutationgroup_improvement_2.patch`
 1. `trac_6647-reviewer.patch`


---

Comment by nborie created at 2009-08-25 12:11:58

The reviewer ReST fixes seems good to me. Thanks for fix it. As I don't manage the trac when review over review appear, I leave another people change the status to positive...


---

Comment by mvngu created at 2009-08-25 17:47:53

Resolution: fixed


---

Comment by mvngu created at 2009-08-25 17:47:53

Merged patches in this order:

 1. `trac_6647_permutationgroup_improvement_2.patch`
 1. `trac_6647-reviewer.patch`


---

Comment by ddrake created at 2009-10-14 03:07:35

This may have caused a doctest failure -- see #7206.
