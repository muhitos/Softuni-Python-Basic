import math

price_video = int(input())
price_adapter = int(input())
price_el_video_day = float(input())
profit_vc_one_day = float(input())


video_cards = 13
adapters = 13
other_parts = 1000

obshto_cena_vc = price_video * video_cards
obshto_cena_adapters = price_adapter * adapters
obshto_poharcheno = obshto_cena_vc + obshto_cena_adapters + other_parts

profit_vc_one_day -= price_el_video_day

obshta_pechalba_vc_den = video_cards * profit_vc_one_day

dni_za_vrushtane = obshto_poharcheno / obshta_pechalba_vc_den

print(obshto_poharcheno)
print(math.ceil(dni_za_vrushtane))
