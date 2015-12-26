(* The try catch does not yet work as desired *)

resubst:=proc(sol, polys) 
  map(u -> simplify(subs(u,polys)),sol) end proc;

myBenchmarkFunction:=proc(u) local exmpl,vars,polys,sol,tt;
  exmpl:=subs(u,theExample);
  vars:=subs(u,theVars);
  polys:=subs(u,thePolys);
  printf("Solve: %s\n",exmpl);
  try 
    tt:=time();
    sol:=timelimit(2,solve(polys,vars));
    tt:=time()-tt;
  catch "FAIL": 
    printf("Interrupted %a\n",sol); 
    return([exmpl,0,FALSE])
  end try;
  printf("Elapsed time: %2.5f\n",tt);
  printf("Result: %a\n",sol);
  printf("Resubstitution: %a\n",resubst(sol,polys));
  return([exmpl,tt,TRUE]);
end proc:


