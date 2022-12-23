# Issue 9729: Moving the discrete fourier interact from wiki into the library.

Issue created by migration from https://trac.sagemath.org/ticket/9729

Original creator: punchagan

Original creation time: 2010-08-11 21:38:23

Assignee: itolkov, jason

CC:  mhampton

Moving the discrete Fourier interact from the wiki into the library. 


---

Attachment


---

Comment by punchagan created at 2010-08-12 04:44:51

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-21 20:05:31

This apparently depends on #9728.


---

Attachment


---

Attachment

The data from the FFT seems very difficult to read, in my opinion. From the documentation of Fourier.fft:

```
    The packing of the result is "standard": If A = fft(a, n), then A[0]
    contains the zero-frequency term, A[1:n/2+1] contains the
    positive-frequency terms, and A[n/2+1:] contains the negative-frequency
    terms, in order of decreasingly negative frequency. So for an 8-point
    transform, the frequencies of the result are [ 0, 1, 2, 3, 4, -3, -2, -1]
```


This suggests that the second half of the array should go before the first half. Also, for many common examples all but a few Fourier coefficients are zero, and it could help visualize them if we plot only the non-zero ones. 

The labels on the x axis do not correspond to the coefficients, but this can be fixed.

Also, I think a bar plot is more adequate than a line plot. You can compare the result of the original code and the proposed changes in the attached png files.

Last but not least, abs(myfft[j])==abs(my_fft[-j]) for all real functions, so if only real functions are going to be used, we should only plot one half: what was the intention? 

I suggest something along the lines of:


```
def plot_bars(ls, lenght = 1):
    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),
                           (x+lenght/2,y),(x-lenght/2,y)])
               for x,y in ls) +
           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),
                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], 
                      rgbcolor=(0,0,0))
               for x,y in ls))

import scipy.fftpack as Fourier
var('x')
@interact
def discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), 
                     treshold = slider(0,0.1,0.01,0.01)):
    pbegin = -float(pi)
    pend = float(pi)
    html("<h3>Function plot and its discrete Fourier transform</h3>")
    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])
    f_vals = [f(ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]
    my_fft = Fourier.fft(f_vals)
    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])
    M = max(v for j,v in ls)
    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)
    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)
    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])

```


Note: "scale" no longer works, but if you like the suggestions, it shouldn't be hard to recover.


---

Comment by pang created at 2010-11-18 11:50:03

Replying to [comment:3 pang]:
Sorry, forgot to copyandpaste some details

```
def plot_bars(ls, lenght = 1):
    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),
                           (x+lenght/2,y),(x-lenght/2,y)])
               for x,y in ls) +
           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),
                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], 
                      rgbcolor=(0,0,0))
               for x,y in ls))

import scipy.fftpack as Fourier
var('x')
@interact
def discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), 
                     treshold = slider(0,0.1,0.01,0.01)):
    pbegin = -float(pi)
    pend = float(pi)
    html("<h3>Function plot and its discrete Fourier transform</h3>")
    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])
    f_vals = [f(x=ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]
    my_fft = Fourier.fft(f_vals)
    L = len(my_fft)
    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])
    M = max(v for j,v in ls)
    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)
    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)
    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])
    


```



---

Comment by kcrisman created at 2011-06-13 18:13:38

Based on pang's comments, looks like maybe this is 'needs work'.


---

Comment by kcrisman created at 2011-06-13 18:13:38

Changing status from needs_review to needs_work.
