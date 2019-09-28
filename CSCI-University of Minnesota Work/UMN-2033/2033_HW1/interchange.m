function B = interchange(A, i ,j)
if i>= 1 && i<= size(A,1) && j>= 1 && j<= size(A,1)
    B = [];
    B = A;
    B(j,:)= A(i,:);
    B(i,:)= A(j,:);
    
else
    disp("error row index out of bounds")
    disp("returning original matrix...")
    B = A;
    
end
end

