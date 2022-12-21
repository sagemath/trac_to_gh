# Issue 1646: 'matrix in group' test doesn't work

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2007-12-31 17:18:19

Assignee: was

The code 



```
G = SL(2,ZZ)                 
M = matrix([[1,0],[0,1]])    
M in G            
```



runs possibly forever inside GAP. same for

```
M = matrix(ZZ,[[1,0],[0,1]])
```



---

Comment by mabshoff created at 2008-01-24 09:18:19

Changing priority from major to critical.


---

Comment by mhansen created at 2008-01-24 18:04:30

This is due to GAP.  Unless we get GAP to fix this, then the best solution would be for SL to override the __contains__ method.


---

Comment by wdj created at 2008-01-24 20:20:09

Changing assignee from was to joyner.


---

Comment by wdj created at 2008-01-24 20:20:09

Changing component from linear algebra to group_theory.


---

Comment by wdj created at 2008-01-24 20:20:09

I've reported this to GAP support.


---

Comment by wdj created at 2008-01-24 23:06:26

from	Laurent Bartholdi <laurent.bartholdi`@`gmail.com>
to	David Joyner <wdjoyner`@`gmail.com>,
cc	GAP Support <support`@`gap-system.org>,
date	Jan 24, 2008 5:36 PM
subject	Re: [GAP Support] membership in SL(2,Z)
mailed-by	gmail.com
	
hide details 5:36 PM (27 minutes ago)
	
	
	
Reply
	
	
It's not intentional, and should be fixed. Here's a quick solution:

InstallMethod(\in,[IsMatrix,IsSpecialLinearGroup],
 function(g,G)
   return Length(g)=Length(One(G)) and
             ForAll(g,row->Length(row)=Length(One(g)) and
             IsOne(DeterminantMat(g));
 end);

needless to say, there must be lots of other missing methods; e.g. for
general, symplectic etc. linear groups.
- Hide quoted text -

On Jan 24, 2008 9:16 PM, David Joyner <wdjoyner`@`gmail.com> wrote:
> Hi:
>
> I wonder if the behavior of
>
> gap> G := SL(2,Integers);
> SL(2,Integers)
> gap> g := [[1,0],[0,1]];
> [ [ 1, 0 ], [ 0, 1 ] ]
> gap> g in G;
> user interrupt at ....
>
> is intentional: it just hangs, as far as I can tell.
> Unless I'm doing something wrong, I wonder if
> an error message should be returned? Perhaps "method not
> implemented" or something?
>
> - David Joyner
>
> _______________________________________________
> Support mailing list
> Support`@`gap-system.org
> http://mail.gap-system.org/mailman/listinfo/support
>



--
Laurent Bartholdi          \  laurent.bartholdi<at>gmail<dot>com
EPFL SB SMA IMB MAD         \    Téléphone: +41 21-6935458
Station 8                    \ Secrétaire: +41 21-6935471
CH-1015 Lausanne, Switzerland \      Fax: +41 21-6930339
Home address: http://f34.com/68


---

Comment by AlexGhitza created at 2008-09-06 22:52:04

This is a duplicate of #1834, which has been fixed and merged in 3.1.2.alpha4.


---

Comment by mabshoff created at 2008-09-06 22:54:29

Resolution: duplicate


---

Comment by mabshoff created at 2008-09-06 22:54:29

Alex,

Thanks for finding the dupe. Closed as duplicate.

Cheers,

Michael
