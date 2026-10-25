# Welcome to the Black-Scholes-Calculator

This project is a Python-based implementation of the famous Black-Scholes-Merton model, used to estimate the theoretical price of European-style options. 

This project was developed by exploring financial engineering concepts and refactoring the codebase in collaboration with AI to ensure clean, efficient, and robust execution.

## ⭐ Key Features
* **Robust Exception Handling:** Includes advanced edge-case handling, such as preventing **division-by-zero errors**
* **AI-Collaborative Refactoring:** Optimized code structure for high readability and performance.
* **Theoretical Grounding:** Implements the core financial engineering formula for Call and Put options.

## 🔬 Mathematical Background
This calculator dynamically computes options pricing using the classic Black-Scholes formula:

$$ d_1 = \frac{\ln(S/K) + \left(r + \frac{\sigma^2}{2}\right)t}{\sigma\sqrt{t}} $$

$$ d_2 = d_1 - \sigma\sqrt{t} $$

### 📝 Parameter Guide:
* $S$ : Current stock price (현재 주가)
* $K$ : Strike price of the option (행사 가격)
* $r$ : Risk-free interest rate (무위험 이자율)
* $\sigma$ : Volatility of the stock (주가 변동성)
* $t$ : Time to expiration in years (만기까지 남은 시간)

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
