edin_gram_maznini = 9
edin_gram_protein = 4
edin_gram_vuglehidrati = 4



procent_mass = int(input())
procent_protein = int(input())
procent_vuglehidrat = int(input())
obsht_broi_kalorii = int(input())
procent_sud_voda = int(input())


obshiti_gramove_maznini = (procent_mass * obsht_broi_kalorii) / edin_gram_maznini /100
obshiti_gramove_proteini = (procent_protein * obsht_broi_kalorii) / edin_gram_protein / 100
obshiti_gramove_vuglehidrat = (procent_vuglehidrat * obsht_broi_kalorii) / edin_gram_vuglehidrati / 100

tegloto_na_hranata = obshiti_gramove_maznini + obshiti_gramove_proteini + obshiti_gramove_vuglehidrat
kalorii_za_edin_gram_hrana = obsht_broi_kalorii / tegloto_na_hranata


diff = abs(100 - procent_sud_voda)

print(f"{diff * kalorii_za_edin_gram_hrana / 100:.4f}")

