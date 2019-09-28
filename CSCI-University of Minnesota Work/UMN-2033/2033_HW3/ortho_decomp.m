function [c,v_perp] = ortho_decomp(U, v)
c = transpose(U) * v;
[m,n] = size(U);
vSum = zeros(m,1);
i = 1;
while i <= n
    vSum = vSum + (c(i)*U(:,i));
    i = i+1;
end

v_perp = v - vSum;
end



