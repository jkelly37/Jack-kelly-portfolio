function [U_new, L_new, P_new] = interchange_lup(U, i, j, L, P)
%update U
U_new = U;
U_new(i,:) = U(j,:);
U_new(j,:) = U(i,:);

%update L 
L_new = L;
bounds = i - 1;
k = 1;
while k<= bounds
    L_new(i,k) = L(j,k);
    L_new(j,k) = L(i,k);
    k = k+1;
end
P_new = P;
P_new(j,:) = P(i,:);
P_new(i,:) = P(j,:);
end