function B = scaling(A, i, s)
 if i>=1 && i<= size(A,1)
    l1 = 1;
    while l1<=size(A,2)
        A(i,l1) =A(i,l1)*s;
        l1= l1+1;
    B = A;    
    end
 else
    disp("error row index out of bounds")
    disp("returning original matrix...")
    B = A;   
 end  
end

