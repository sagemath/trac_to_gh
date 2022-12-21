# Issue 4362: Bug fixes in tableaux latex output [with patches at #4355. Needs review.]

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-10-24 11:34:13

Assignee: mhansen

CC:  sage-combinat

The latex output of tableaux is a broke, which affects the latex output in CrystalOfTableaux. Patches that fix this were attached to #4355 but I should have created a new ticket for these since that ticket really proposes something different.

See #4355 for the patches.

See http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en for discussion. But in a nutshell try 


```
latex(Tableau([[1,2,3],[2,2],[3,4],[4]])) 
latex(Tableau([[1,1,2,3,4],[2,2,2],[3]])) 
latex(Tableau([[1],[2],[3],[4]])) 
latex(Tableau([This is the Trac macro *1,2,3,4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,3,4-macro))) 
latex(Tableau([[1,2,3,4],[5,6,7,8]])) 
latex(Tableau([[1,2,3,4],[5,6,7,8],[9]])) 
latex(Tableau([[1,2,],[5,6],[7,9]])) 
latex(Tableau([[1,2,],[5,6],[7,9],[9]])) 
latex(Tableau([[1,2,3,4,5,],[6]])) 
latex(Tableau([[1,2,3,4,5,],[6],[7],[8],[9]])) 
```


etc or 


```
CrystalOfTableaux("A2",shape=[3,1]).latex_file("/home/bump/tmp/test.tex")
```


to see the defect.




---

Attachment

First of Dan's patches from #4355


---

Attachment

Second of Dan's patches from #4355


---

Comment by mabshoff created at 2008-10-24 11:42:08

Dan, 

I have moved the patches from #4355 over here and will delete them on the other ticket. Having patches from another ticket applied via this ticket will only make things more complicated than they need to be.

Cheers,

Michael


---

Comment by mhansen created at 2008-11-06 22:25:57

I tested this out on all the examples, and it looks good to me.


---

Attachment

Nicolas suggested that the tests should reflect the problem. As it turns out the existing tests all have square tableaux (in tensor_product.py, tableau.py and output.py) which is a rare case that is not broke for the original code.

http://groups.google.com/group/sage-combinat-devel/msg/cd0de81b0e2f0ae5?hl=en

Nicolas posted this before Mike reviewed the patch. In view of Nicolas' comment I'm uploading
a third patch tableaux_output2.patch that makes the tests non-rectangular tableaux
for which the original code was broke.


---

Comment by mabshoff created at 2008-11-07 16:13:23

Resolution: fixed


---

Comment by mabshoff created at 2008-11-07 16:13:23

Merged all three patches in Sage 3.2.rc0. 

Dan: Please make sure that you post patches and not diffs. I did apply and commit the patches above in your name, so no need to update anything here.

Cheers,

Michael
