# Welcome to the Black-Scholes-Calculator

This project is a Python-based implementation of the famous Black-Scholes-Merton model, used to estimate the theoretical price of European-style options. 

This project was developed by exploring financial engineering concepts and refactoring the codebase in collaboration with AI to ensure clean, efficient, and robust execution.

## Key Features
* **Robust Exception Handling:** Includes advanced edge-case handling, such as preventing **division-by-zero errors**
* **AI-Collaborative Refactoring:** Optimized code structure for high readability and performance.
* **Theoretical Grounding:** Implements the core financial engineering formula for Call and Put options.

## 🔬 Mathematical Background
This calculator dynamically computes options pricing using the classic formula:

$$ d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)t}{\sigma\sqrt{t}} $$

$$ d_2 = d_1 - \sigma\sqrt{t} $$

## 🛠️ Built With
* Python 3.x
* Math & SciPy libraries (for precise cumulative distribution function calculations)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---
🎈 *This project was built with deep curiosity by a 14-year-old student passionate about Financial Engineering and AI. If you find this codebase helpful or interesting, please review it and leave a ⭐ Star! Thank you!*
