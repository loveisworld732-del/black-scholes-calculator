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
현재_주가 = float(input("📈 1. Underling Asset Price (S): "))
행사_가격 = float(input("🎯 2. Strike Price (K): "))
남은_시간 = float(input("⏳ 3. Time to Maturity in Years (T): "))
기본_금리 = float(input("🏦 4. Risk-Free Interest Rate (r): "))
주가_변동성 = float(input("⚡ 5. Asset Volatility (sigma): "))

콜옵션_가격, 풋옵션_가격 = black_scholes_calculator(현재_주가, 행사_가격, 남은_시간, 기본_금리, 주가_변동성)

print("\n==================================================")
print("✨ [Compilation Success - Execution Output] ✨")
print("==================================================")
print(f"💵 Call Option Value: {콜옵션_가격:.2f} 원")
print(f"💵 Put Option Value: {풋옵션_가격:.2f} 원")
print("==================================================")
