function A = build_matrix()
I = eye(8);
i = 1; 
blank = zeros(8)
while i<= size(I,2)
    blank(:,i)= get_forces(I(:,i)); 
    i = i+1;
end
A = blank
end
%for each col call get force


