
"""
Bu modül, farklı nüve malzemelerinin bağıl geçirgenlik (mu_r) ve açıklama bilgilerini içerir.
"""

core_materials = {
    "Silicon Steel": {
        "mu_r": 4000,
        "description": "Düşük kayıplı, manyetik nüvelerde yaygın kullanılan malzeme.",
        "bh_curve": [
        [0, 0],
        [50, 0.2],
        [100, 0.5],
        [200, 1.0],
        [300, 1.25],
        [400, 1.4],
        [500, 1.45],
        [600, 1.48],  # Doyma bu noktada baslıyor.
        [700, 1.49],
        [800, 1.495]
    ]
    },
    "Ferrite": {
        "mu_r": 1500,
        "description": "Yüksek frekansta tercih edilen, düşük akı yoğunluklu nüve malzemesi.",
         "bh_curve": [
        [0, 0.0],
        [25, 0.2],
        [50, 0.4],
        [100, 0.6],
        [150, 0.8],
        [200, 0.9],
        [250, 0.91],
        [300, 0.915],
        [350, 0.916]
    ]
    },
    "Amorphous Metal": {
        "mu_r": 20000,
        "description": "Yüksek geçirgenlik ve düşük kayıpla çalışan ileri düzey nüve malzemesi.",
        "bh_curve": [
    [0, 0.0],
    [10, 0.2],
    [20, 0.4],
    [40, 0.7],
    [60, 0.9],
    [80, 1.05],
    [100, 1.15],
    [120, 1.2],
    [140, 1.22],
    [160, 1.23]
]
    },
    "Air": {
        "mu_r": 1,
        "description": "Manyetik alanın geçişine direnç gösteren, referans ortam.",
        "bh_curve": [
    [0, 0.0],
    [100, 0.0001],
    [200, 0.0002],
    [300, 0.0003],
    [400, 0.0004],
    [500, 0.0005],
    [600, 0.0006],
    [700, 0.0007],
    [800, 0.0008],
    [900, 0.0009]
]
    }
}

def get_material_properties(material_name):
    """
    Malzeme ismine göre bağıl geçirgenlik ve açıklamasını döner.
    """
    return core_materials.get(material_name, None)