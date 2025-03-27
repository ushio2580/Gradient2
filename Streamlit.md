
---

## Requirements

### To run this application, you need the following Python libraries:

- `streamlit` - For the interactive web interface.
- `sympy` - For symbolic mathematics (e.g., derivatives, Hessian).
- `numpy` - For numerical computations.
- `matplotlib` - For creating 3D and contour plots.

**Python Version**: Requires Python 3.7 or higher.

---

## How to Run

Follow these steps to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ushio2580/Gradient2.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Gradient2
   ```

3. **Install Dependencies**:
   Run the following command to install the required libraries:
   ```bash
   pip install streamlit sympy numpy matplotlib
   ```

4. **Launch the Application**:
   Run the Streamlit app with:
   ```bash
   streamlit run test2.py
   ```
   This will start a local server and open the application in your default web browser (typically at `http://localhost:8501`).

---

## Usage

Once the application is running, you’ll see two tabs:

### 🧮 Example 1: Gradient and Hessian
- **Input**: Enter a function of two variables using `x1` and `x2` (e.g., `1/2*(x2 - x1**2)**2 + (1 - x1)**2`).
- **Outputs**:
  - Partial derivatives: \(\frac{\partial f}{\partial x_1}\) and \(\frac{\partial f}{\partial x_2}\).
  - Gradient vector: \(\nabla f(x_1, x_2)\).
  - Second-order derivatives and Hessian matrix: \(\nabla^2 f(x_1, x_2)\).
  - Visualizations:
    - **3D Surface Plot**: Shows the function’s surface.
    - **Contour Plot**: Displays level curves of the function.

### 📈 Example 2: Line Search
- **Setup**: Uses the function \( f(x_1, x_2) = x_1^2 + x_2^2 + x_1 x_2 + 4x_1 - x_2 + 1 \), starting at \(\vec{x}_0 = [2, -1]^T\), with direction \(\vec{p} = [-1, 1]^T\).
- **Process**:
  - Defines the parametric path: \(\vec{x}(t) = \vec{x}_0 + t \vec{p}\).
  - Computes the optimal step size \(t^*\) where the directional derivative is zero.
  - Verifies the minimum condition: \(\nabla f(\vec{z})^T \vec{p} = 0\).
- **Visualizations**:
  - **3D Surface with Path**: Plots the function surface with the search path.
  - **Contour Plot with Path**: Shows the path on the function’s contours.
  - **Function Value Along Path**: Graphs \(f(t)\) with the optimal point marked.

---

## Troubleshooting

- **Error Processing Function**: Ensure your function input is valid (e.g., uses `x1` and `x2`, avoids undefined operations).
- **Plots Not Displaying**: Verify that `matplotlib` is installed correctly.
- **Streamlit Not Running**: Check that you’re in the correct directory and that `test2.py` exists.

---

## Contributing

Feel free to fork the repository and submit pull requests with enhancements, such as additional features, improved visualizations, or more example functions.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

This application is an excellent tool for learning about gradients, Hessians, and line search methods in optimization. Enjoy experimenting!
```

---
