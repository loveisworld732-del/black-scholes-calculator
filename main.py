import sys
import io

# Force terminal output to UTF-8 to prevent emoji errors (터미널 출력을 UTF-8로 강제 설정하여 이모지 에러 방지)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

import math
from scipy.stats import norm

def black_scholes_calculator(S, K, T, r, sigma):
    """
    Calculate Black-Scholes Option Pricing for Call and Put Options (콜옵션과 풋옵션의 블랙-숄즈 옵션 가격을 계산합니다).
    Includes exception handling for Zero Division (sigma or T is 0) (시그마나 만기가 0일 때 발생하는 영분할 예외 처리를 포함합니다).
    """
    # Check if sigma or T is less than or equal to 0 (시그마나 만기가 0 이하인지 확인합니다)
    if sigma <= 0 or T <= 0:
        return 0.0, 0.0

    # Calculate the numerator and denominator for d1 (d1의 분자와 분모를 계산합니다)
    numerator = math.log(S / K) + (r + 0.5 * (sigma ** 2)) * T
    denominator = sigma * math.sqrt(T)

    # Calculate d1 and d2 values (d1과 d2 값을 계산합니다)
    d1 = numerator / denominator
    d2 = d1 - denominator

    # Calculate call and put option prices (콜옵션과 풋옵션 가격을 계산합니다)
    call_price = (S * norm.cdf(d1)) - (K * math.exp(-r * T) * norm.cdf(d2))
    put_price = (K * math.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))

    return call_price, put_price

print("==================================================")
print("💰 [Option Pricing Engine - CLI v1.0.0] 💰")
print("==================================================")
current_stock_price = float(input("📈 1. Underlying Asset Price (S) (현재 주가): "))
strike_price = float(input("🎯 2. Strike Price (K) (행사 가격): "))
time_to_maturity = float(input("⏳ 3. Time to Maturity in Years (T) (남은 만기 시간/년): "))
risk_free_rate = float(input("🏦 4. Risk-Free Interest Rate (r) (무위험 이자율): "))
asset_volatility = float(input("⚡ 5. Asset Volatility (sigma) (주가 변동성): "))

call_option_price, put_option_price = black_scholes_calculator(
    current_stock_price, strike_price, time_to_maturity, risk_free_rate, asset_volatility
)

print("\n==================================================")
print("✨ [Compilation Success - Execution Output] ✨")
print("==================================================")
print(f"💵 Call Option Value (콜옵션 가격): {call_option_price:.2f} KRW(원)")
print(f"💵 Put Option Value (풋옵션 가격): {put_option_price:.2f} KRW(원)")
print("==================================================")
