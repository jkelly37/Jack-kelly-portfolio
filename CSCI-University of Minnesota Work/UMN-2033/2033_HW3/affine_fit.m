function [M, t] = affine_fit(P, P_tilde)
[m,n] = size(P);
i=1;
A=[];
while i<=n
    b = design_matrix(P(:,i));
    A = [A;b];
    i = i+1;
end
x = least_squares(A,P_tilde(:));
[M,t] = my_unpack(x);

end

