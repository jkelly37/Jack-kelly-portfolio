function R = my_rref(A)
k=1; 
l=1;
m = size(A,1);
while (1<=k) && (k<=m) && (1<=l)&&(l<=size(A,2))
    k1 = k;
    while k1<m
        if abs(A(k1,l))<abs(A(k1+1,l))
            bigRow = k1+1;
            A=interchange(A,bigRow,k);
        end
        k1 = k1+1;
    end
    if A(k,l) == 0
        l = l+1;          
    else
        A(k,:) = A(k,:)/A(k,l);
        i = 1;
        for i = 1:m
            if i~=k
                A = replacement(A,i,k,-A(i,l))
            end
        end
        if (abs(A(k,l))) <= 10e-12
            A(k,l) = 0;
        end
        k = k+1;
        l = l+1;
    end
end    
R = A    
end

