function B = replacement(A, i, j, s)
if i>= 1 && i<= size(A,1) && j>= 1 && j<= size(A,1)
    l1 = 1;
    while l1<= size(A,2)
        A(i,l1) = A(i,l1) + (A(j,l1)*s);
        l1 = l1+1;
        
    end
    B = A;
    
else 
    disp("error row index out of bounds")
    disp("returning original matrix...")
    B = A;
end
end


