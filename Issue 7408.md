# Issue 7408: Improve the speed of RSK

Issue created by migration from https://trac.sagemath.org/ticket/7408

Original creator: mhansen

Original creation time: 2009-11-07 19:43:20

Assignee: mhansen

CC:  hivert

The implementation of RSK in Sage has a number of inefficiencies which add up when dealing with large permutations.  The main improvement comes from using a binary search to figure out where to insert the number.


---

Comment by mhansen created at 2009-11-07 19:44:26

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-07 20:14:06

I like this commentary of yours:

```
                #Swtich x and y
```

You should have called you variables `t` and `i` :-)


Florent


---

Comment by ylchapuy created at 2009-11-07 23:12:26

A last slight improvement would be to avoid the burden of keeping maxes and lenths.

A row version would then be:


```
    def robinson_schensted(self):
        from bisect import bisect
        p = []       #the "left" tableau
        q = []       #the "recording" tableau

        #For each x in self, insert x into the tableau p.
        for i,x in enumerate(self):
            row_counter = 0
            for r in p:
                if r[-1] > x:
                    y_pos = bisect(r, x)
                    x, r[y_pos] = r[y_pos], x
                    row_counter += 1
                else:
                    break
            if row_counter == len(p):
                p.append([x])
                q.append([i+1])
            else:
                r.append(x)
                q[row_counter].append(i+1)

        return [tableau.Tableau(p),tableau.Tableau(q)]
```


This gives me something like a 15% speedup.


---

Comment by mhansen created at 2009-11-08 07:09:22

I've put up a new patch which incorporates Yann's ideas as well as gets rid of the row_counter bookkeeping.


---

Attachment


---

Comment by hivert created at 2009-11-08 11:18:11

Changing keywords from "" to "Robinson-Schensted".


---

Comment by hivert created at 2009-11-08 11:18:11

This patch greatly improve the speed of RSK even for small permutations:

```
sage: p4 = Permutations(4).list()
sage: timeit("map(attrcall('robinson_schensted'), p4)")
625 loops, best of 3: 1.22 ms per loop
sage: p = Permutations(1000).random_element()
sage: timeit("p.robinson_schensted()")
25 loops, best of 3: 19.5 ms per loop
```

whereas we had:

```
sage: timeit("map(attrcall('robinson_schensted'), p4)")
625 loops, best of 3: 1.34 ms per loop
sage: p = Permutations(1000).random_element()
sage: timeit("p.robinson_schensted()")
5 loops, best of 3: 265 ms per loop
```

However, I was not sure that bisect cut the thing correctly in case of repeated letters so I had to write another test. I'd rather see it integrated into sage.
Please review this minor change. 

Otherwise you can put a postive review. 

Cheers,

Florent


---

Attachment

I give it a positive review.


---

Comment by ylchapuy created at 2009-11-08 14:06:10

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:28:33

Resolution: fixed
