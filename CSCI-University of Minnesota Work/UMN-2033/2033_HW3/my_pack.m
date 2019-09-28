function beta = my_pack(M, t)
%construct M as vector
M = transpose(M)
beta = [M(:);t]
end

