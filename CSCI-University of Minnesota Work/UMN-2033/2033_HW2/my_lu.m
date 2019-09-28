function [L, U] = my_lu(A)
%create U
n = size(A,2)
L = eye(n);
U = A;
i = 1;
while ((i >= 1) && (i<= n-1))
    i
    if (abs(U(i,i))) < (10e-12)
        U(i,i) = 0;
        return
    end
    k = n
    while (i+1)<=k && k<=n
        
        p = U(k,i) / U(i,i);
        [U, L] = replacement_lu(U, k ,i, p, L);
        k = k - 1; 
        %U = new(1);
        %L = new(2);
       
    end
    i = i+1;
end 
end