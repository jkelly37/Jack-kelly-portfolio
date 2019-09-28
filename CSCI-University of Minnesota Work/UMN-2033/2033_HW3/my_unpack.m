function [M, t] = my_unpack(beta)
t = beta([5,6]);
M(1,1) = beta(1,1);
M(1,2) = beta(2,1);
M(2,1) = beta(3,1);
M(2,2) = beta(4,1);
end
