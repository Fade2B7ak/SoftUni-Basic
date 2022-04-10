procesorr_price_in_usd = float(input())
video_card_price_in_usd = float(input())
ram_price_in_usd = float(input())
count_of_rams = int(input())
discount = float(input())

usd_to_bgn = 1.57

processor_price = procesorr_price_in_usd * usd_to_bgn
video_card_price = video_card_price_in_usd * usd_to_bgn
ram_price = ram_price_in_usd * usd_to_bgn * count_of_rams
processor_discount = processor_price - (processor_price * discount)
video_card_discount = video_card_price - (video_card_price * discount)
total_cost = processor_discount + video_card_discount + ram_price
print(f'Money needed - {total_cost:.2f} leva.')
