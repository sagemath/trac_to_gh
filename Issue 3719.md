# Issue 3719: bug in group cohomology

Issue created by migration from https://trac.sagemath.org/ticket/3719

Original creator: wdj

Original creation time: 2008-07-24 11:16:49

Assignee: tbd

CC:  alexghitza

As reported by Ursula Whitcher


```
sage: G = SymmetricGroup(4)
sage: G.cohomology(1,2)
```

yields an error. The problem is a bug in the current version of the GAP package HAP, version 1.8.5. The latest version 1.8.7 but there the bug still exists


```
gap> G := SymmetricGroup(4);
Sym( [ 1 .. 4 ] )
gap> GroupCohomology(G,1); ## an improvement over 1.8.5
[  ]
gap> GroupCohomology(G,1,2);
List Element: <position> must be a positive integer (not a integer) at
if IsInt( C!.fpIntHom[n] )  then
...
```




---

Comment by wdj created at 2008-08-03 02:35:14

I posted a new gap_packages archive to
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_6.spkg


---

Comment by wdj created at 2008-08-03 02:38:32

Sorry, meant to add that this passes sage -testall on amd64 hardy heron and includes hap1.8.8 which fixes the problem reported above.


```
sage: gap.eval('LoadPackage("hap")')
'true'
sage: G = SymmetricGroup(4)
sage: G.cohomology(1,2)
Multiplicative Abelian Group isomorphic to C2
```



---

Comment by mabshoff created at 2008-08-03 08:13:34

David,

please also add an optional doctest that verifies that the issue has been fixed.

Cheers,

Michael


---

Comment by wdj created at 2008-08-03 12:13:28

Michael:
You mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?


---

Comment by mabshoff created at 2008-08-03 13:51:02

Replying to [comment:5 wdj]:
> Michael:
> You mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?

Yes, it should be an optional doctest. I am somewhat concerned that the author of the GAP package just rereleased the package with the bug fix instead of incrementing the release number. Since various packaging efforts are under way I could imagine something like this not getting fixed upstream in other distributions, so the doctest when run with optional flags would show that the problem remains unfixed. 

It is still my plan to used optional testing in the future at least for the build on sage.math per default.

Cheers,

Michael


---

Comment by wdj created at 2008-08-03 14:48:09

docstring addition patch based on 3.1.alpha0


---

Attachment

Okay, I just attached the patch you requested to this ticket. (I wasn't sure if it needed a new ticket or not.) It passes sage -t but it dawned on me afterwards that sage -t would not test for optional docstring additions. Anyway, hope this is what you were looking for.

BTW, I am one of the webmasters for GAP (hence involved wityh package updates) and you can be sure that hap 1.8.8 will definitely get applied upstream, probably in the next week or so.


---

Comment by was created at 2008-08-03 17:48:28

> Okay, I just attached the patch you requested to this ticket. (I wasn't sure
>  if it needed a new ticket or not.) It passes sage -t but it dawned on 
> me afterwards that sage -t would not test for optional docstring additions. 

Use

```

  sage -t --optional 

```



---

Attachment

based on 3.1.alpha0 and probably the previous patch


---

Comment by wdj created at 2008-08-04 04:08:31

Okay, the attached passes sage -t --optional
I had to make some changes to the code. For some reason, it seems gap packages were not loading for me properly (eg, gap.eval('LoadPackage("hap")') gave a traceback the first time but loaded it the second time...). That was fixed with some try/except trickery which seems harmless even if packages do load as they should. Also, GAP's RequirePackage is actually being deprecated, so I replaced them with the preferred LoadPackage. Finally, Molien series do not require an optional package, so I removed some comments in the docstring for that method.
Hope this is okay now.


---

Comment by AlexGhitza created at 2008-08-27 06:44:47

Looks good.  The new spkg fixes the problem that was reported, and the few things that broke in the upgrade are fixed by the two patches.


---

Comment by mabshoff created at 2008-08-27 08:08:18

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 08:08:18

Merged both patches in Sage 3.1.2.alpha1.

David,

I added an hg repo to the spkg (but kept the p6 patchlevel). Please base future spkgs on the spkg

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/gap_packages-4.4.10_6.spkg

Cheers,

Michael
