function p = gps3d(a, b, c, d, ra, rb, rc, rd)
r1 = (rb^2) - (ra^2)
r2 = (rc^2) - (rb^2)
r3 = (rd^2) - (rc^2)
m11 = 2*(a(1)-b(1))
m12 = 2*(a(2)-b(2))
m13 = 2*(a(3)-b(3))
m21 = 2*(b(1)-c(1))
m22 = 2*(b(2)-c(2))
m23 = 2*(b(3)-c(3))
m31 = 2*(c(1)-d(1))
m32 = 2*(c(2)-d(2))
m33 = 2*(c(3)-d(3))

v1 = -(a(1)^2)-(a(2)^2)-(a(3)^2)+(b(1)^2)+(b(2)^2)+(b(3)^2)
v2 = -(b(1)^2)-(b(2)^2)-(b(3)^2)+(c(1)^2)+(c(2)^2)+(c(3)^2)
v3 = -(c(1)^2)-(c(2)^2)-(c(3)^2)+(d(1)^2)+(d(2)^2)+(d(3)^2)

v = [r1-v1;r2-v2;r3-v3;]
m = [m11,m12,m13;m21,m22,m23;m31,m32,m33]
p = solve(m,v)
end