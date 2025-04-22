# app.py

import streamlit as st
from calculations import calculate_turns, calculate_flux, calculate_reluctance, estimate_loss, estimate_efficiency, calculate_dynamic_mu
from materials import get_material_properties, core_materials
from utils import plot_turns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Transformatör Simülatörü", layout="wide")
st.title("Transformatör Tasarımı Simülatörü")
st.write("Bu uygulama, elektrik makineleri dersinde kullanılan transformatörlerin temel parametrelerini hesaplar ve görselleştirir.")

# Giriş Alanları
st.sidebar.header("Giriş Verileri")
V1 = st.sidebar.number_input("Primer Gerilim (V)", value=220)
V2 = st.sidebar.number_input("Sekonder Gerilim (V)", value=12)
freq = st.sidebar.number_input("Frekans (Hz)", value=50)
A_core = st.sidebar.number_input("Nüve Kesit Alanı (cm²)", value=1.0, format="%.2f") * 1e-4
core_length = st.sidebar.number_input("Nüve Uzunluğu (cm)", value=10.0, format="%.2f") / 100
material = st.sidebar.selectbox("Nüve Malzemesi", list(core_materials.keys()))

# Hesapla Butonu
if st.button("Hesapla"):
    mat_props = get_material_properties(material)
    mu_r = mat_props['mu_r'] if mat_props else 1000

    N1, N2 = calculate_turns(V1, V2)
    phi = calculate_flux(V1, freq, N1, A_core)
    B = phi / A_core

    if mat_props and "bh_curve" in mat_props:
        mu_dynamic = calculate_dynamic_mu(B, mat_props["bh_curve"])
        if mu_dynamic:
            mu_r = mu_dynamic

    R = calculate_reluctance(mu_r, A_core, core_length)
    P_loss = estimate_loss()
    eta = estimate_efficiency(P_out=90, P_loss=P_loss)

    st.subheader("Sonuçlar")
    st.markdown(f"**Seçilen Malzeme:** {material} - _{mat_props['description']}_")
    st.markdown(f"**Primer Sarım Sayısı:** `{N1}`")
    st.markdown(f"**Sekonder Sarım Sayısı:** `{N2}`")
    st.markdown(f"**Manyetik Akı (Φ):** `{phi:.5f} Wb`")
    st.markdown(f"**Akı Yoğunluğu (B):** `{B:.3f} T`")
    st.markdown(f"**Etkin Bağıl Geçirgenlik (μᵣ):** `{mu_r:.1f}`")
    st.markdown(f"**Relüktans (R):** `{R:.2e} A/Wb`")
    st.markdown(f"**Toplam Kayıp:** `{P_loss:.2f} W`")
    st.markdown(f"**Verim:** `{eta*100:.2f} %`")

    st.subheader("Grafikler")
    st.pyplot(plot_turns(N1, N2))

    # Dinamik verim grafiği çizimi
    P_out_list = list(range(60, 161, 10))  
    dynamic_efficiency_list = []

    st.subheader("Dinamik Hesaplar (Her güç seviyesi için)")

    for P_out in P_out_list:
        phi = calculate_flux(V1, freq, N1, A_core)
        B = phi / A_core

        if mat_props and "bh_curve" in mat_props:
            mu_dynamic = calculate_dynamic_mu(B, mat_props["bh_curve"])
            mu_eff = mu_dynamic if mu_dynamic else mat_props['mu_r']
        else:
            mu_eff = mat_props['mu_r']

        R = calculate_reluctance(mu_eff, A_core, core_length)
        P_loss = estimate_loss(core_loss=(1.0 / mu_eff) * 20)
        eta = estimate_efficiency(P_out, P_loss)
        dynamic_efficiency_list.append(eta * 100)

        #st.write(f"P_out: {P_out} W, B: {B:.3f} T, μᵣ: {mu_eff:.1f}, P_loss: {P_loss:.2f} W, Verim: {eta*100:.2f}%")

    plt.figure(figsize=(10, 5))
    plt.plot(P_out_list, dynamic_efficiency_list, marker='o')
    plt.title('Çıkış Gücüne Göre Verim')
    plt.xlabel('Çıkış Gücü (W)')
    plt.ylabel('Verim (%)')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

else:
    st.info("Sol panelden değerleri girin ve 'Hesapla' butonuna basın.")