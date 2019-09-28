function p = gps2d(a, b, c, ra, rb, rc)
disp(a(1))
r1 = (rb^2) - (ra^2)
r2 = (rc^2) - (rb^2)
m11 = 2*(a(1)-b(1))
m12 = 2*(a(2)-b(2))
v1 = -(a(1)^2)-(a(2)^2)+(b(1)^2)+(b(2)^2)

m21 = 2*(b(1)-c(1))
m22 = 2*(b(2)-c(2))
v2 = -(b(1)^2)-(b(2)^2)+(c(1)^2)+(c(2)^2)
m  = [m11,m12; m21,m22]
v = [r1-v1;r2-v2]
p = solve(v,m)

end

