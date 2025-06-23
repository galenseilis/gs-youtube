import sympy as sp

# Define symbols
x, y, u, v = sp.symbols('x y u v')

# Original joint PDF: standard bivariate normal
f_xy = (1 / (2 * sp.pi)) * sp.exp(-0.5 * (x**2 + y**2))

# Change of variables
u_def = x + y
v_def = x - y

# Solve for x, y in terms of u, v
sol = sp.solve([u - x - y, v - x + y], (x, y))
x_uv = sol[x]
y_uv = sol[y]

# Substitute into the original density
f_uv_expr = f_xy.subs({x: x_uv, y: y_uv}).simplify()

# Compute Jacobian matrix of the inverse transformation
J = sp.Matrix([[sp.diff(x_uv, u), sp.diff(x_uv, v)],
               [sp.diff(y_uv, u), sp.diff(y_uv, v)]])

# Compute absolute value of determinant of the Jacobian
Jacobian_det = sp.Abs(J.det())

# Final transformed density
f_uv = (f_uv_expr * Jacobian_det).simplify()

# Display result
print(f_uv)
