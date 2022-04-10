n_kilometers = int(input())
time_when = input()
# Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
taxi_starts_price = 0.70
taxi_day_price_per_km = 0.79
taxi_night_price_per_km = 0.90
bus_tariff = 0.09
train_tariff = 0.06

bus_price = bus_tariff * n_kilometers
train_price = train_tariff * n_kilometers

if time_when == "day":
    taxi_price = taxi_day_price_per_km * n_kilometers + taxi_starts_price
else:
    taxi_price = taxi_night_price_per_km * n_kilometers + taxi_starts_price

if n_kilometers < 20:
    cheapest_transport = taxi_price
elif n_kilometers < 100:
    cheapest_transport = min(bus_price, taxi_price)
else:
    cheapest_transport = min(train_price, bus_price, taxi_price)
print(f"{cheapest_transport:.2f}")