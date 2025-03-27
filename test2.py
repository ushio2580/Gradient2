import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(page_title="Gradient and Line Search", layout="centered")

# Tabs
example1_tab, example2_tab = st.tabs(["🧮 Example 1: Gradient and Hessian", "📈 Example 2: Line Search"])

# =====================
# Example 1: Gradient and Hessian
# =====================
with example1_tab:
    st.header("🧮 Example 1: Gradient and Hessian")

    st.markdown("""
    ## 🎯 Goal:

    Enter a function of two variables `x1` and `x2` below to compute its gradient and Hessian:
    """)

    # Define symbols
    x1, x2 = sp.symbols('x1 x2')
    user_input = st.text_input("✍️ Enter your function f(x1, x2):", "1/2*(x2 - x1**2)**2 + (1 - x1)**2")

    try:
        f_expr = sp.sympify(user_input)

        st.latex(r"f(x_1, x_2) = " + sp.latex(f_expr))

        st.markdown("---")
        st.subheader("🔧 Step 1: Partial Derivative with respect to x1")
        grad_x1 = sp.diff(f_expr, x1)
        st.latex(r"\frac{\partial f}{\partial x_1} = " + sp.latex(grad_x1))

        st.markdown("---")
        st.subheader("🔧 Step 2: Partial Derivative with respect to x2")
        grad_x2 = sp.diff(f_expr, x2)
        st.latex(r"\frac{\partial f}{\partial x_2} = " + sp.latex(grad_x2))

        st.markdown("---")
        st.subheader("✅ Step 3: Full Gradient")
        grad_vector = sp.Matrix([grad_x1, grad_x2])
        st.latex(r"\nabla f(x_1, x_2) = " + sp.latex(grad_vector))

        st.markdown("---")
        st.subheader("🔧 Step 4: Compute the Hessian")
        hessian = sp.hessian(f_expr, (x1, x2))
        for i in range(2):
            for j in range(2):
                st.latex(r"\frac{\partial^2 f}{\partial x_%d \partial x_%d} = %s" % (i+1, j+1, sp.latex(hessian[i,j])))

        st.markdown("---")
        st.subheader("✅ Step 5: Hessian Matrix")
        st.latex(r"\nabla^2 f(x_1, x_2) = " + sp.latex(hessian))

        st.markdown("---")
        st.subheader("📊 Step 6: 3D and Contour Plots")
        f_lambdified = sp.lambdify((x1, x2), f_expr, modules="numpy")
        x_vals = np.linspace(-2, 2, 100)
        y_vals = np.linspace(-1, 3, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        with np.errstate(all='ignore'):
            Z = f_lambdified(X, Y)
            Z = np.nan_to_num(Z, nan=0, posinf=0, neginf=0)

        # Create figure with two subplots
        fig = plt.figure(figsize=(16, 6))

        # 3D Surface Plot
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
        ax1.set_title(r"3D Surface of $f(x_1, x_2)$")
        ax1.set_xlabel(r"$x_1$")
        ax1.set_ylabel(r"$x_2$")
        ax1.set_zlabel(r"$f(x_1, x_2)$")

        # Contour Plot
        ax2 = fig.add_subplot(122)
        contour = ax2.contour(X, Y, Z, levels=20, cmap='viridis')
        ax2.set_title(r"Contour Plot of $f(x_1, x_2)$")
        ax2.set_xlabel(r"$x_1$")
        ax2.set_ylabel(r"$x_2$")
        plt.colorbar(contour, label='Function Value')

        # Display the figure in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error processing the function: {e}")

# =====================
# Example 2: Line Search
# =====================
with example2_tab:
    st.header("📈 Example 2: Line Search")

    st.markdown("""
    ## 🎯 Goal:
    
    Given the function:
    """)
    st.latex(r"f(x_1, x_2) = x_1^2 + x_2^2 + x_1 x_2 + 4x_1 - x_2 + 1")

    st.markdown("""
    Starting from the point:
    """)
    st.latex(r"\vec{x}_0 = \begin{bmatrix} 2 \\ -1 \end{bmatrix}, \quad \vec{p} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}")

    st.markdown("""
    Perform a line search and verify that:
    """)
    st.latex(r"\nabla f(\vec{z})^T \vec{p} = 0")

    # Define symbols and function
    x1, x2, t = sp.symbols('x1 x2 t')
    f = x1**2 + x2**2 + x1*x2 + 4*x1 - x2 + 1
    x0 = sp.Matrix([2, -1])
    p = sp.Matrix([-1, 1])
    x_t = x0 + t * p

    st.markdown("---")
    st.subheader("🔧 Step 1: Define the Path")
    st.latex(r"\vec{x}(t) = \vec{x}_0 + t \vec{p} = " + sp.latex(x_t))

    st.markdown("---")
    st.subheader("🔧 Step 2: Substitute into f")
    x1_t, x2_t = x_t[0], x_t[1]
    f_t = f.subs({x1: x1_t, x2: x2_t})
    st.latex(r"f(t) = " + sp.latex(f_t))

    st.markdown("---")
    st.subheader("🔧 Step 3: Derivative and Optimal t")
    f_t_deriv = sp.diff(f_t, t)
    t_star = sp.solve(f_t_deriv, t)[0]
    st.latex(r"f'(t) = " + sp.latex(f_t_deriv))
    st.latex(r"t^* = " + sp.latex(t_star))

    st.markdown("---")
    st.subheader("✅ Step 4: Evaluate Minimum Point")
    z = x_t.subs(t, t_star)
    st.latex(r"\vec{z} = " + sp.latex(z))

    st.markdown("---")
    st.subheader("🔍 Step 5: Verify Gradient Condition")
    grad_f = sp.Matrix([sp.diff(f, x1), sp.diff(f, x2)])
    grad_at_z = grad_f.subs({x1: z[0], x2: z[1]})
    dot_product = (grad_at_z.T * p)[0]
    st.latex(r"\nabla f(\vec{z}) = " + sp.latex(grad_at_z))
    st.latex(r"\nabla f(\vec{z})^T \vec{p} = " + sp.latex(dot_product))

    if dot_product == 0:
        st.success("✅ Verified: The directional derivative is zero. Minimum found along the direction.")
    else:
        st.warning("⚠️ Warning: Dot product not zero. May not be a true minimum.")

    st.markdown("---")
    st.subheader("📊 Step 6: Visualization of Line Search")

    # Lambdify functions
    f_num = sp.lambdify((x1, x2), f, 'numpy')
    f_t_num = sp.lambdify(t, f_t, 'numpy')

    # Generate grid
    x_vals = np.linspace(-3, 3, 50)
    y_vals = np.linspace(-2, 4, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    with np.errstate(all='ignore'):
        Z = f_num(X, Y)
        Z = np.nan_to_num(Z, nan=0, posinf=0, neginf=0)

    # Path coordinates
    t_vals = np.linspace(-1, 2, 50)
    path_x = [float(x_t[0].subs(t, val)) for val in t_vals]
    path_y = [float(x_t[1].subs(t, val)) for val in t_vals]
    path_z = f_t_num(t_vals)

    # Optimal point
    z0 = float(z[0])
    z1 = float(z[1])
    optimal_z = f_num(z0, z1)

    # Starting point
    start_x = float(x0[0])
    start_y = float(x0[1])
    start_z = f_num(start_x, start_y)

    # Create figure with subplots
    fig = plt.figure(figsize=(16, 6))

    # 3D Surface Plot
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='plasma', alpha=0.7)
    ax1.plot(path_x, path_y, path_z, 'r-', lw=2, label='Search Path')
    ax1.scatter([start_x], [start_y], [start_z], c='g', s=100, label='Start')
    ax1.scatter([z0], [z1], [optimal_z], c='b', s=100, label='Optimal')
    ax1.set_title("3D Surface with Search Path")
    ax1.set_xlabel("x1")
    ax1.set_ylabel("x2")
    ax1.set_zlabel("f(x1, x2)")
    ax1.legend()

    # Contour Plot
    ax2 = fig.add_subplot(132)
    ax2.contour(X, Y, Z, levels=15, cmap='plasma')
    ax2.plot(path_x, path_y, 'r-', lw=2)
    ax2.scatter([start_x], [start_y], c='g', s=100)
    ax2.scatter([z0], [z1], c='b', s=100)
    ax2.set_title("Contour Plot with Search Path")
    ax2.set_xlabel("x1")
    ax2.set_ylabel("x2")

    # Function Along Path
    ax3 = fig.add_subplot(133)
    ax3.plot(t_vals, path_z, 'b-')
    ax3.scatter(float(t_star), f_t_num(float(t_star)), c='r', s=100)
    ax3.set_title("Function Value Along Path")
    ax3.set_xlabel("Parameter t")
    ax3.set_ylabel("f(t)")
    ax3.grid(True)

    plt.tight_layout()
    st.pyplot(fig)