function x = least_squares(A, b)
[m,n] = size(A);
x = zeros(m,1);
[q,r] = my_qr(A);
x = back_sub(r,(transpose(q)*b));  
end


