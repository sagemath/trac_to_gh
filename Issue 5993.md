# Issue 5993: rewrite numerical_approx (the n function) to use interval arithmetic

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-06 06:30:59

Assignee: burcin

This email snippet pretty much describes the issue:

```


On Tue, May 5, 2009 at 11:16 PM, Henryk Trappmann <bo198214`@`googlemail.com> wrote:
>
> Ah now I see, you mean though it displays 1/384 it is internally still
> the above sum, which is computed when evaluated with n.

True.  In Sage right now the internal form of the expression (not the simplified form) is used by the "n" command.  This will change when Sage switches from using maxima-based symbolics to Pynac. 

By the way, you can use the real interval field to get a floating point approximation to any symbolic expression to a given number of digits of precision.  Every digit is definitely right except the one right before the question mark:

sage: a = 1/(48*sqrt(1)) - 7/(96*1**(3/2)) + 3/(32*1**(5/2)) - 5/ (128*1**(7/2))
sage: RealIntervalField(100)(a)             # increase 100 for more digits
0.002604166666666666666666666667?

I think the n function (numerical_approx) for symbolics should be changed to using interval arithmetic.  This will be a huge improvement.  Notice, e.g., that interval arithmetic very nicely gives the right answer for the infamous sin(10^50):

sage: a = sin(10^50)
sage: a.n(53)
-0.480500143493759
sage: a.n(100)
0.60974154556722786199645650055
sage: RealIntervalField(100)(a)
0.?
sage: RealIntervalField(1000)(a)
-0.7896724934293100827102895399174077539600834046214027191457808736221899969800609898633436757589688470442999273506152178357769064871103469499564331175635613221319397479785737324994506546860108913238488404198306006819757685879489185272089985858148036954222175628785469474395231359019098600625732453528693?
sage: RealIntervalField(2000)(a)
-0.78967249342931008271028953991740775396008340462140271914578087362218999698006098986334367575896884704429992735061521783577690648711034694995643311756356132213193974797857373249945065468601089132384884041983060068197576858794891852720899858581480369542221756287854694743952313590190986006257324535286926640214204183176856658976160340849634781130568053474154330242776565926107540133198976420887112928640131582614537425282391078909233424580311555104358881651194953182665408243214532152322603956371555619997139323527489307648072219268176687894373677502675114853503742816202001868587837402822439060931321957?

```





---

Comment by kcrisman created at 2011-03-16 15:54:52

Disagree, primarily because it's been this way for quite a while now, and because a lot of users would be _really_ confused by the question mark.  We certainly could update the documentation to make it clear how to get much more accurate answers using RIF.


---

Comment by kcrisman created at 2011-03-16 15:54:52

Changing priority from major to minor.


---

Comment by rws created at 2015-02-01 15:53:54

Changing assignee from burcin to mvngu.


---

Comment by rws created at 2015-02-01 15:53:54

Changing component from calculus to documentation.
