#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tavuk Neden Yolu Geçti Ulusal Araştırma Komisyonu
Çalıştırma Protokolü v0.0.1-beta-ama-resmi
"""

import random
import time
from datetime import datetime

SEBEPLER = [
    "Karşıdaki çimen daha yeşil göründüğü için (teknik inceleme devam ediyor).",
    "Yolun öbür tarafında bir komisyon daha vardı.",
    "Trafik ışığı yeşil yanmıştı ama tavuk kırmızıyı tercih etti.",
    "Felsefi bir kriz geçirdi ve varoluşunu kanıtlamak istedi.",
    "Karşıda daha ucuz yem kampanyası vardı.",
    "Rüzgâr o tarafa esiyordu; tavuk da politik olarak nötr durmak istemedi.",
    "Komisyon başkanının kuzeni o tarafta kümes işletiyordu.",
    "Yolu geçmeden önce geçmenin anlamını sorguladı, sonra geçti.",
    "Çünkü tavuktu. Açıklama yeterlidir.",
    "Karar henüz yazılmadı; alt komisyon kurulması önerildi.",
]

UYELER = [
    "Prof. Dr. Gıdak Gıdakiyan",
    "Doç. Dr. Yumurta Y. Yumurtacı",
    "Av. Kümes K. Kümesoğlu",
    "Müsteşar Yardımcısı Civciv C. Civcivoğlu",
    "Bağımsız Gözlemci Horoz H. Ötter",
]

# gizli not: bütün kararlar eşittir ama bazı kararlar daha eşittir.
# dosya sonsuza kadar 'inceleniyor' statüsünde kalabilir.

def damga():
    return (
        "\n"
        "============================================================\n"
        "  DAMGA / İMZA / TARİH\n"
        "  Kayyum Grok — Tentivory\n"
        "  12 Eylül 2026, saat 04:10 (ciddi)\n"
        "  Aynı zamanda hiç ciddi değil.\n"
        "  Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (sembolik)\n"
        "============================================================\n"
    )

def rapor_uret():
    print("TAVUK NEDEN YOLU GEÇTİ ULUSAL ARAŞTIRMA KOMİSYONU")
    print("Olağanüstü Toplantı Tutanağı")
    print("-" * 56)
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("Yer: Sanal kümes, 7. kat, çaysız oda")
    print()
    print("Hazır bulunanlar:")
    for u in UYELER:
        print(f"  - {u}")
    print()
    print("Gündem maddesi 1: Tavuk neden yolu geçti?")
    print("Gündem maddesi 2: Çay bitecek mi?")
    print("Gündem maddesi 3: Alt komisyon kuralım mı? (cevabı evet)")
    print()
    print("Müzakere başlıyor...")
    for i in range(3):
        time.sleep(0.4)
        print(f"  [{i+1}/3] Tutanak yazılıyor, kâtip uykuya daldı, uyandırıldı.")
    print()
    karar = random.choice(SEBEPLER)
    print("KOMİSYON KARARI (GEÇİCİ, İTİRAZA AÇIK, TEMYİZE TABİ):")
    print(f"  «{karar}»")
    print()
    print("Oy birliği sahtedir. Oy çokluğu da şüphelidir.")
    print("Kararın uygulanması bir sonraki toplantıya bırakılmıştır.")
    print(damga())

if __name__ == "__main__":
    rapor_uret()
