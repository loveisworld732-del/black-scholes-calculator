import math
from scipy.stats import norm

def black_scholes_calculator(S, K, T, r, sigma):
    """
    Calculate Black-Scholes Option Pricing for Call and Put Options.
    Includes exception handling for Zero Division (sigma or T is 0).
    """
    if sigma <= 0 or T <= 0:
        return 0.0, 0.0

    numerator = math.log(S / K) + (r + 0.5 * (sigma ** 2)) * T
    denominator = sigma * math.sqrt(T)

    d1 = numerator / denominator
    d2 = d1 - denominator

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
print(f"💵 Call Option Value (콜옵션 가격): {call_option_price:.2f} KRW")
print(f"💵 Put Option Value (풋옵션 가격): {put_option_price:.2f} KRW")
print("==================================================")
