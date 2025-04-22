"""
Grafik çizimlerini yapan yardımcı modül.
"""

import matplotlib.pyplot as plt

def plot_turns(N1, N2):
    """
    Primer ve sekonder sarım sayılarını çubuk grafik olarak gösterir.
    """
    labels = ['Primer Sarım', 'Sekonder Sarım']
    values = [N1, N2]

    plt.figure()
    plt.bar(labels, values, color=['blue', 'orange'])
    plt.title('Primer ve Sekonder Sarım Sayıları')
    plt.ylabel('Sarım Sayısı')
    plt.grid(axis='y')
    plt.tight_layout()
    return plt

def plot_efficiency_graph(P_out_list, P_loss_list):
    """
    Çıkış gücüne göre verim yüzdesini çizer.
    """
    efficiency = [P_out / (P_out + P_loss) * 100 for P_out, P_loss in zip(P_out_list, P_loss_list)]

    plt.figure()
    plt.plot(P_out_list, efficiency, marker='o')
    plt.title('Çıkış Gücüne Göre Verim')
    plt.xlabel('Çıkış Gücü (W)')
    plt.ylabel('Verim (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return plt

