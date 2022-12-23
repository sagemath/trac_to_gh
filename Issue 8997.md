# Issue 8997: riemann_roch_basis is implemented incorrectly in sage

Issue created by migration from https://trac.sagemath.org/ticket/8997

Original creator: was

Original creation time: 2010-05-20 00:19:02

Assignee: AlexGhitza

CC:  rkirov minz oleksandrmotsak

See the file schemes/plane_curves/projective_curve.py, where it says

```

        The following example illustrates that the Riemann-Roch space
        function in Singular doesn't *not* work correctly.
        
        ::
        
            sage: R.<x,y,z> = GF(5)[]
            sage: f = x^7 + y^7 + z^7
            sage: C = Curve(f); pts = C.rational_points()
            sage: D = C.divisor([ (3, pts[0]), (-1,pts[1]), (10, pts[5]) ])
            sage: C.riemann_roch_basis(D)    # output is random (!!!!)
            [x/(y + x), (z + y)/(y + x)]
        
        The answer has dimension 2 (confirmed via Magma). But it varies
        between 1 and quite large with Singular.
```


The problem can be solved by learning how the relevant code in Singular works then correctly wrapping it.


---

Comment by was created at 2010-05-20 00:19:12

Changing component from algebra to algebraic geometry.


---

Comment by wdj created at 2010-05-21 16:41:30

Replying to [ticket:8997 was]:

> 
> The problem can be solved by learning how the relevant code in Singular works then correctly wrapping it. 

Are there any more details on this available?


---

Comment by was created at 2010-05-25 07:22:22

For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153


---

Comment by wdj created at 2010-05-25 11:13:14

Replying to [comment:3 was]:
> For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153

Thanks. This suggests that all one needs to do is to add the singular command 

```
system("random", mySeedAsAnInt);
```

at the top of the function code.


---

Comment by wdj created at 2010-05-26 18:53:34

apply to 4.4.2


---

Attachment

The attached patch seems to fix the problem. When applied to 4.4.2 on a 10.6.3 mac, it passes sage -testall except for an unrelated docstring failure (in interfaces/r.py).

I'm leaving it as needs work for now since I want to test it on more machines. I'm posting it in case others want to test it too.


---

Comment by wdj created at 2010-05-26 18:56:52

Changing status from new to needs_work.


---

Comment by wdj created at 2010-05-27 17:39:42

This patch does not work. My guess is that


```
system("random", mySeedAsAnInt);
```

does not really set the random seed for all commands, but I could easily be wrong. In any case, it seems that the command now does return the dimension in a consistent way for different machines. That is progress, since the old version was much worse. However, the basis (ie, the list of functions spanning the RR space) is not deterministic. I'm not sure how to fix that.


---

Comment by minz created at 2010-07-19 09:47:23

My impression is that the problem lies with Singular. I adapted the example in the description above and typed directly into Singular the following:


```
kill s, C, Ctemp, temp, G, R, LG;

LIB "brnoeth.lib";
int plevel=printlevel;
printlevel=-1;
system("random", 1);

ring s=5,(x,y),lp;
list C=Adj_div(x7+y7+1);
C=NSplaces(1,C);
def R=C[1][2];

# I want to look at the points to be able to define
# the same divisor each time, see below
def Ctemp=extcurve(1,C);
def temp=Ctemp[1][5];
setring temp;
print(POINTS);

setring R;

# adapt the line below according to the ordering of the points
# i always chose the divisor 3(0,-1,1)-1(1,2,1)+10(2,1,1)
intvec G = ;

list LG=BrillNoether(G,C);
LG;

printlevel=plevel;
```


Not only did the bases vary each time I ran this code (even though I fixed the random seed in the sixth line), the resulting bases also had different cardinality (either 0 or 2).

(I also tried to post this on the Singular trac server, but failed to do so. Maybe someone else is able to update the Singular ticket?)


---

Comment by OleksandrMotsak created at 2010-10-14 16:09:02

Changing status from needs_work to needs_info.


---

Comment by OleksandrMotsak created at 2010-10-14 16:09:02

Dear minz,

1. what do you mean with "intvec G = ;" in the Singular code?
2. could you please answer to the comment by Jose Ignacio Farran at
http://www.singular.uni-kl.de:8002/trac/ticket/153#comment:7 ?


---

Comment by minz created at 2010-11-21 12:39:17

apply to 4.6


---

Attachment

Following Jose's explanations on the Singular trac server, the modified Sage wrapper should now work with the new patch. What the unmodified wrapper did wrong was how it defined the divisor in Singular. There's actually two lists that are important: The divisor needs to be defined relative to the list of points C[3] (in the above example), but to know which point the k-th entry of this list actually refers to, one has to parse the list POINTS of the rings C[5][d][1], where d is the degree of the point. -- The patch also modifies the documentation to illustrate this with an example.


---

Comment by minz created at 2010-11-21 12:50:44

Changing status from needs_info to needs_review.


---

Comment by wdj created at 2010-11-29 00:27:44

Replying to [comment:12 minz]:
> Following Jose's explanations on the Singular trac server, the modified Sage wrapper 

...

Thank you! 

I'll look at this carefully when classes end this semester, which will be in a few weeks.


---

Comment by wdj created at 2010-12-20 03:36:41

This looks good. It applies fine to sage 4.6 on an ubuntu linux machine and passes sage -testall. I have fixed the code and docstrings in agcode.py so that it runs too. I guess this should be a separate ticket?

Again, thanks *very* much!


---

Comment by wdj created at 2010-12-20 03:36:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-18 13:57:29

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2011-01-18 13:57:29

This needs some clarifications:
 * which patch(es) need to be applied?
 * who are the authors/reviewers? (please fill in the real names in the Author and Reviewer fields on this ticket)


---

Comment by wdj created at 2011-01-18 20:55:08

Replying to [comment:16 jdemeyer]:
> This needs some clarifications:
>  * which patch(es) need to be applied?
>  * who are the authors/reviewers? (please fill in the real names in 
> the Author and Reviewer fields on this ticket)

Done. Others helped, such as William Stein and Jose Farran.

Many thanks to everyone who helped with fixing this issue!

Can this be changed back to positive review now?


---

Comment by jdemeyer created at 2011-01-19 01:30:03

Replying to [comment:17 wdj]:
> Replying to [comment:16 jdemeyer]:
> > This needs some clarifications:
> >  * which patch(es) need to be applied?
You didn't answer this question...


---

Comment by wdj created at 2011-01-19 01:43:55

Replying to [comment:18 jdemeyer]:
> Replying to [comment:17 wdj]:
> > Replying to [comment:16 jdemeyer]:
> > > This needs some clarifications:
> > >  * which patch(es) need to be applied?
> You didn't answer this question...

Sorry! Just trac_8997_fix_rr_basis_and_doc.patch


---

Comment by jdemeyer created at 2011-01-19 01:51:44

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2011-01-19 01:52:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:19:54

Resolution: fixed
