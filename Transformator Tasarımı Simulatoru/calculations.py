# calculations.py

def calculate_turns(V1, V2, N2_desired=None):
    """
    Primer tarafın sarım sayısı varsayılan olarak 220 yapıldı.
    Sekonder tarafın sarım sayısı isteğe bırakılmıştır.
    V1: Primer gerilim (Volt)
    V2: Sekonder gerilim (Volt)
    N2_desired: Sekonder sarımı sabit verirse ona göre hesap yapar (opsiyonel)
    """
    if N2_desired:
        N1 = round((V1 / V2) * N2_desired)
        N2 = N2_desired
    else:
        N1 = 220  # varsayılan primer sarım
        N2 = round((V2 / V1) * N1)
    return N1, N2

def calculate_flux(V, f, N, A):
    """
    Manyetik akı Φ (Weber) hesaplar.
    V: Gerilim (Volt)
    f: Frekans (Hz)
    N: Sarım sayısı
    A: Nüve kesit alanı (m^2)
    """
    return V / (4.44 * f * N * A)

def calculate_dynamic_mu(B_target, bh_curve):
    """
    B-H eğrisine göre etkin bağıl geçirgenliği hesaplar.
    B_target: Hesaplanan akı yoğunluğu (T)
    bh_curve: Malzemeye ait B-H verileri (liste halinde)
    """
    for i in range(len(bh_curve) - 1):
        H1, B1 = bh_curve[i]
        H2, B2 = bh_curve[i + 1]
        if B1 <= B_target <= B2:
            # Lineer interpolasyonla H değeri bulunur
            H = H1 + ((B_target - B1) * (H2 - H1)) / (B2 - B1)
            return B_target / H if H != 0 else None
    return None  # B, eğrinin dışındaysa

def calculate_reluctance(mu_r, A, l):
    """
    Relüktans hesaplar.
    mu_r: Bağıl geçirgenlik
    A: Alan (m^2)
    l: Manyetik yol uzunluğu (m)
    """
    mu_0 = 4 * 3.1416e-7  # boşluğun manyetik geçirgenliği (H/m)
    return l / (mu_0 * mu_r * A)

def estimate_efficiency(P_out, P_loss):
    """
    Verim hesaplama fonksiyonu
    η = P_out / (P_out + P_loss)
    """
    return P_out / (P_out + P_loss)

def estimate_loss(core_loss=2.0, copper_loss=3.0):
    """
    Sabit kayıpları döner (basit model)
    """
    return core_loss + copper_loss
