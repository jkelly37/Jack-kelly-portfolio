function [Q,R] = my_qr(A)
[m,n] = size(A);
Q = zeros(m,n);
i=1;
while i<=n 
    if i == 1
        sum = 0;
        j=1;
        while j <= m
            sum = (A(j,i)^2) + sum;
            j=j+1;
        end
        sum = sum^0.5;
        if sum == 0
            Q(:,i) = 0;
        else    
        Q(:,i) = A(:,i)/sum;
        end
    else
        [c, v_perp] = ortho_decomp(Q,A(:,i));
        sum = 0;
        j=1;
        while j <= size(v_perp,1)
            sum = (v_perp(j,1)^2) + sum;
            j=j+1;
        end
        sum = sum^0.5;
        if sum == 0
            Q(:,i) = 0;
        else    
        Q(:,i) = (v_perp/sum);
        end
        
    end
    i = i+1;
end
R = (transpose(Q)) * A;
R(abs(R)<1e-12) = 0;
end