# Issue 2138: bugs in word_problem for AbelianGroupElement

Issue created by migration from https://trac.sagemath.org/ticket/2138

Original creator: wdj

Original creation time: 2008-02-11 00:42:10

Assignee: joyner

sage: G = AbelianGroup(2,[2,3], names="xy")
sage: x,y = G.gens()
sage: x.word_problem([x,y],display=False)
[This is the Trac macro *x, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x, 1-macro)
sage: x.word_problem([x,y],display=True)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-2.9.alpha4/<ipython console> in <module>()

/home/wdj/wdj/sagefiles/sage-2.9.alpha4/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group_element.py in word_problem(self, words, display)
    341         #print LL1,LL2
    342         if display:
--> 343             s = str(g)+" = "+add(["("+str(words[LL2[i]-1])+")^"+str(LL1[i])+"*" for i in range(nn)])
    344             m = len(s)
    345             #print "      ",s[:m-1]

<type 'exceptions.NameError'>: global name 'add' is not defined


This is obviously a problem. Also, the docstring should be written better. The first
example is hard to understand.


---

Comment by was created at 2008-02-11 01:03:15

> Also, the docstring should be written better. The first example is hard to understand.

Whoever fixes this (maybe me) please keep in mind trac #1849 and the attached patch.  

William


---

Comment by wdj created at 2008-04-09 11:47:58

I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?


---

Comment by mabshoff created at 2008-04-09 15:20:00

Resolution: fixed


---

Comment by mabshoff created at 2008-04-09 15:20:00

Replying to [comment:3 wdj]:
> I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?

Yes. I can confirm that the `display` property is gone. Closed as fixed.

Cheers,

Michael
