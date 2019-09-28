function Ai = design_matrix(pi)
[m,n] = size(pi);
Ai = zeros(m,6);
Ai(1,1) = pi(1,1);
Ai(1,2) = pi(2,1);
Ai(1,5) = 1;
Ai(2,3) = pi(1,1);
Ai(2,4) = pi(2,1);
Ai(2,6) = 1;
end