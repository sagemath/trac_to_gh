# Issue 1208: Faster _choose in matrix2.py

Issue created by migration from https://trac.sagemath.org/ticket/1208

Original creator: jsp

Original creation time: 2007-11-19 13:43:50

Assignee: was

This is in pure Python in a notebook running under VMWare during SD6:

choose_T is an implementation of the algorithm T from Knuth:
TAOC, a draft of section 7.2.1.3: Generating all combinations: p. 5
This is like algoritm L, but faster (Knuth)


```
choose
system:sage

{{{id=0|
def choose_T(n, t):
    x = []               # initialize T1
    c = range(t)
    if t == n:
        return c
    c.append(n)
    c.append(0)
    j = t-1


    while True:
        #print "T2 reached: c = ", c, "j = ", j
        x.append(c[:t])    # visit T2
        if j >= 0:
            c[j] = j+1
            j = j-1
            continue       # goto T2

        #print "T3 reached: c = ", c, "j = ", j
        if c[0]+1 < c[1]:  # T3 easy case!
            c[0] = c[0]+1
            continue
        else:
            j = 1

        #print "T4 reached: with j = ", j
        while True:
            c[j-1] = j-1      # T4 find j
            temp = c[j]+1
            if temp == c[j+1]:
                j = j+1
            else:
                break


        #print "T5 reached: with j = ", j
        if j >= t:
            break

        #print "T6 reached: with j = ", j, "increase c[j]"
        c[j] = temp
        j = j-1

    return x
}}}


choose is an implementation of algorithm L TAOC, draft of 7.2.1.3, p.4.

{{{
{{{id=1|
def choose(n,t):
    x = []
    c = range(t)
    c.append(n)
    c.append(0)
    j = 0

    while j < t:
        x.append(c[:t])
        j = 0
        while c[j]+1 == c[j+1]:
            c[j] = j
            j = j+1
        c[j] = c[j]+1

    return x
}}}


{{{
{{{id=2|
time l = choose(20,9)
///
CPU time: 3.94 s,  Wall time: 4.22 s
}}}



{{{
{{{id=3|
time k = choose_T(20,9)
///
CPU time: 2.28 s,  Wall time: 2.35 s
}}}

}}}


{{{
{{{id=5|
3.94/2.28
///
1.72807017543860
}}}

Seems to be faster. To do: implement in Cython and make a patch.








---

Comment by jsp created at 2007-11-27 19:23:04

There is an error in the algo (code fragment):
should be:


```
    if t == n:
        x.append(c)
        return x
```


For example _choose(1,1) should return

```
[[0]]
```



---

Comment by jsp created at 2007-11-27 20:01:10

Further comment: I can not reproduce the speed factor on Linux. But I believe Knuth:
it is faster :)!


---

Attachment

My test case is the infamous 'dance' program: since sage-2.8.3 we won:



```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.6, Release Date: 2007-09-06                     |
| Type notebook() for the GUI, and license() for information.        |

sage: attach '/home/jaap/pythonsrc/OEIS/dancing.sage'

sage: time dance(6)
h^6 - 9*h^5 + 60*h^4 - 225*h^3 + 555*h^2 - 774*h + 484
CPU times: user 5.15 s, sys: 0.15 s, total: 5.30 s
Wall time: 5.33

sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 44.50 s, sys: 1.18 s, total: 45.69 s
Wall time: 45.85


----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.14, Release Date: 2007-11-24                      |
| Type notebook() for the GUI, and license() for information.        |

sage: attach '/home/jaap/pythonsrc/OEIS/dancing.sage'

sage: time dance(6)
h^6 - 9*h^5 + 60*h^4 - 225*h^3 + 555*h^2 - 774*h + 484
CPU times: user 2.16 s, sys: 0.03 s, total: 2.19 s
Wall time: 2.19

sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 17.22 s, sys: 0.17 s, total: 17.39 s
Wall time: 17.66


```



---

Attachment


---

Comment by jsp created at 2007-11-29 15:47:10

I screwed up matrix2.pyx, I suppose. There is a new bundle in newchoose.hg


---

Comment by mhansen created at 2007-12-02 05:21:48

Works for me.


---

Comment by mabshoff created at 2007-12-02 06:01:40

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 06:01:40

Merged in 2.8.15.alpha2.
