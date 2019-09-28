function [L, U, P] = my_lup(A)
%create U
n = size(A,2);
L = eye(n);
P = eye(n);
U = A;
i = 1;
while ((i >= 1) && (i<= n-1))
    [m , j] = max(U(:,i));
    [U, L, P] = interchange_lup(U, i, j, L, P);
    if (abs(U(i,i))) < (10e-12)
        U(i,i) = 0;
        return
    end
    k = n
    while (i+1)<=k && k<=n
        p = U(k,i) / U(i,i);
        [U, L] = replacement_lu(U, k ,i, p, L);
        k = k - 1;
    end
    i = i+1;
end 
end