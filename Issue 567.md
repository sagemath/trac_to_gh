# Issue 567: ode_solver: display a user-friendly error message if the jacobian is not provided for the bsimp algorithm

Issue created by migration from https://trac.sagemath.org/ticket/567

Original creator: pdenapo

Original creation time: 2007-09-02 01:02:31

Assignee: was

When using ode_solve with the algorithm 'bsimp' that requires the jacobian to be provided, 
an error  of type ValueError with the message 'error solving'. It would be more user-friendly to
check if the jacobian has been provided, and display a more specific error message.

Example:

sage: f= lambda t,y :[y[1],-y[0]]
sage: T=ode_solver()
sage: T.function=f
sage: T.algorithm='bsimp'
sage: T.ode_solve(y_
0=[1,0],t_span=[0,2*pi],num_points=100)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/<ipython console> in <module>()

/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/ode.pyx in ode.ode_solver.ode_solve()

<type 'exceptions.ValueError'>: error solving


I'm submiting a patch for this.




---

Attachment


---

Comment by was created at 2007-09-05 05:02:08

Resolution: fixed
