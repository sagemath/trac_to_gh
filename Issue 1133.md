# Issue 1133: issue with gap and large permutations

Issue created by migration from https://trac.sagemath.org/ticket/1133

Original creator: was

Original creation time: 2007-11-09 07:25:38

Assignee: was


```

Hi,

Is there a limit on the size of permutations with the Gap interface? I
managed to get an error today which seems to be due to Gap putting
"(...)" at the end of a line. Here's the error:

<type 'exceptions.TypeError'>: Gap produced error output
Syntax error: expression expected in /home/carlo/.sage//temp/t40/13158//interf\
ace//tmp line 1
$sage3:=(1,2,8,30,43,13,3)(4,18,56,140,145,59,19)(5,23,69,162,167,72,24)(6,11,\
33,86,114,46,16)(7,12,34,87,115,47,17)(9,35,96,208,146,61,21)(10,38,103,220,16\
8,74,27)(14,22,58,141,252,124,48)(15,26,71,163,264,131,51)(20,62,150,284,288,1\
53,63)(25,75,172,306,310,175,76)(28,41,94,190,234,122,54)(29,42,95,191,235,123\
,55)(31,88,192,281,149,67,37)(32,91,199,303,171,81,40)(36,98,211,237,241,213,9\
9)(39,105,223,244,248,225,106)(44,50,68,144,277,236,116)(45,53,80,166,299,243,\
119)(49,126,255,197,193,258,127)(52,133,267,204,200,270,134)(57,142,278,232,28\
9,155,65)(60,66,152,285,185,282,147)(64,156,292,319,333,295,157)(70,164,300,23\
3,311,177,79)(73,78,174,307,188,304,169)(77,178,314,322,336,315,179)(82,110,20\
6,298,280,250,138)(83,111,207,276,302,251,139)(...);;
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                                                             \
                                               ^

  executing Read("/home/carlo/.sage//temp/t40/13158//interface//tmp");



Here's the code to reproduce it:

def p3Group(p):
   assert is_prime(p)

   F = gap.new("FreeGroup(3)")

   a = F.gen(1)
   b = F.gen(2)
   c = F.gen(3)

   rels = []
   rels.append( a**Integer(p) )
   rels.append( b**Integer(p) )
   rels.append( c**Integer(p) )
   rels.append( a*b*((b*a*c)**Integer(-1)) )
   rels.append( c*a*((a*c)**Integer(-1)) )
   rels.append( c*b*((b*c)**Integer(-1)) )

   N = gap.NormalClosure(F, gap.Subgroup(F, rels))
   niso = gap.NaturalHomomorphismByNormalSubgroupNC(F, N)

   a = PermutationGroupElement(gap.Image(niso, a))

# This works:
p3Group(5)

# This blows up:
p3Group(7)
```



---

Comment by was created at 2007-11-10 12:22:37

Solution-ish:

```
---------- Forwarded message ----------
From: Steve Linton <sal@cs.st-and.ac.uk>
Date: Nov 9, 2007 3:49 AM
Subject: Re: Fwd: [sage-support] Issue with interface to Gap in 2.8.12
To: David Joyner <wdjoyner@gmail.com>


Distinction between Print and View is the issue here. Viw truncates, Print
does not.

Try

gap> PermList([1000,999..1]);

and compare

gap> Print(PermList([1000,999..1]),"\n");

       Steve

```



---

Comment by robertwb created at 2007-11-28 05:48:28

See the last patch of #1296


---

Comment by mabshoff created at 2007-12-29 21:03:16

This issue was fixed by Robert Bradshaw's patch referred above and merged in 2.9.0. It works in Sage 2.9.1.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.1.1, Release Date: 2007-12-25                     |
| Type notebook() for the GUI, and license() for information.        |
sage: def p3Group(p):
....:        assert is_prime(p)
....:    F = gap.new("FreeGroup(3)")
....:    a = F.gen(1)
....:    b = F.gen(2)
....:    c = F.gen(3)
....:    rels = []
....:    rels.append( a**Integer(p) )
....:    rels.append( b**Integer(p) )
....:    rels.append( c**Integer(p) )
....:    rels.append( a*b*((b*a*c)**Integer(-1)) )
....:    rels.append( c*a*((a*c)**Integer(-1)) )
....:    rels.append( c*b*((b*c)**Integer(-1)) )
....:    N = gap.NormalClosure(F, gap.Subgroup(F, rels))
....:    niso = gap.NaturalHomomorphismByNormalSubgroupNC(F, N)
....:    a = PermutationGroupElement(gap.Image(niso, a))
....:
sage: p3Group(5)
sage: p3Group(7)
sage:
```

But we still might need to use `View` in a the GAP interface. Can somebody confirm that it is no longer needed since Robert's patch probably eliminated that code? But it might just be that the same problem exists in other places in the GAP interface.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 17:47:26

This works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11, Release Date: 2008-03-30                        |
| Type notebook() for the GUI, and license() for information.        |
sage: attach foo.sage
sage: p3Group
p3Group
sage: p3Group?
Type:           function
Base Class:     <type 'function'>
String Form:    <function p3Group at 0x2b14f4d08938>
Namespace:      Interactive
File:           /home/mabshoff/.sage/temp/sage/16347/_scratch_mabshoff_release_cycle_sage_3_0_alpha0_foo_sage_0.py
Definition:     p3Group(p)
Docstring:
    x.__init__(...) initializes x; see x.__class__.__doc__ for signature

sage: p3Group(3)
sage: p3Group(5)
sage: p3Group(7)
sage: p3Group(11)
sage: p3Group(17)
sage:
Exiting SAGE (CPU time 0m1.25s, Wall time 1m4.75s).
Exiting spawned Gap process.
```



---

Comment by mabshoff created at 2008-04-01 20:25:24

Resolution: fixed


---

Comment by mabshoff created at 2008-04-01 20:25:24


```
[21:45] <mabshoff> wstein: could you check #1133 and conform that we can close it.
[21:48] <wstein> I confirm that 1133 looks fixed.
```


Cheers,

Michael
