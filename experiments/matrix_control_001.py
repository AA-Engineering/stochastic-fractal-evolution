import numpy as np, json
rng=np.random.default_rng(20261016)
n=20000; A=np.diag([.8,.6]); Q=np.diag([.04,.09]); x0=np.array([2.,-1.]); x=np.tile(x0,(n,1))
for t in range(12):
    x=x@A.T+rng.normal(size=(n,2))@np.linalg.cholesky(Q).T
mu=np.linalg.matrix_power(A,12)@x0
cov=sum((np.linalg.matrix_power(A,k)@Q@np.linalg.matrix_power(A,k).T for k in range(12)),np.zeros((2,2)))
result={'seed':20261016,'runs':n,'steps':12,'expected_mean':mu.tolist(),'observed_mean':x.mean(axis=0).tolist(),'expected_variance':np.diag(cov).tolist(),'observed_variance':x.var(axis=0,ddof=1).tolist(),'det_A':float(np.linalg.det(A)),'rank_A':int(np.linalg.matrix_rank(A))}
print(json.dumps(result,indent=2))
