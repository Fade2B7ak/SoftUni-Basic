pens_pack = 5.80
marker_pack = 7.20
cleaner = 1.20

count_pens_packs = int(input())
count_marker_packs = int(input())
count_cleaner_litters = int(input())
discount = int(input())

markers_pack_price = marker_pack * count_marker_packs
pens_pack_price = pens_pack * count_pens_packs
cleaner_pack_price = cleaner * count_cleaner_litters
price_sum = markers_pack_price + pens_pack_price + cleaner_pack_price

prince_with_discount = price_sum - (price_sum * (discount /100))
print(prince_with_discount)


