# Transformatör Tasarımı Simülatörü

Bu proje, elektrik makineleri dersi kapsamında geliştirilen bir transformatör simülasyonudur. 
Python + Streamlit kullanılarak interaktif bir arayüzle çalışır. 
Kullanıcıdan alınan transformatör verileriyle temel elektromanyetik hesaplamalar yapar ve görsel grafikler sunar.

## Özellikler

- Primer ve sekonder gerilim değerine göre sarım sayısı hesaplar  
- Nüve kesit alanı ve uzunluğuna göre manyetik akı ve akı yoğunluğu (B) hesaplar  
- Farklı nüve malzemelerine göre bağıl geçirgenlik (`μᵣ`) kullanır  
- Relüktans (`R`) ve verim (`η`) gibi parametreleri çıkartır  
- Farklı çıkış güçleri için dinamik verim grafiği çizer  
- Doygunluk etkisini `B-H` eğrileri üzerinden modellemeye çalışır  
- Kullanıcı dostu arayüz: Streamlit ile interaktif kullanım

## Doygunluk Modellemesi

Projede, malzemelerin `B-H` eğrileri tanımlanmıştır. Bu eğriler üzerinden `μᵣ` değeri dinamik olarak hesaplanır ve doygunluk bölgesine girildikçe `μᵣ` düşer. Bu düşüş, relüktansı artırır ve verime yansır.

> **Not:** Doygunluk etkisi teorik olarak modellenmiş olsa da, `B-H` eğrilerindeki geçişin yumuşaklığı nedeniyle grafikte *gözle görülür dramatik bir kırılma* elde edilememiştir.
Gelecekte daha agresif eğrilerle veya deneysel ölçümlerle model güçlendirilebilir.



![Arayüz Görseli](https://github.com/KRMALC/Transformator-Tasarim--Simulasyonu/blob/fd045cc43536d7b97753ca36e514282e800723d3/1.png)
![Arayüz Görseli](https://github.com/KRMALC/Transformator-Tasarim--Simulasyonu/blob/fd045cc43536d7b97753ca36e514282e800723d3/2.png)
![Arayüz Görseli](https://github.com/KRMALC/Transformator-Tasarim--Simulasyonu/blob/fd045cc43536d7b97753ca36e514282e800723d3/3.png)

