# Sound Source Localization and Speech Translation for Earthquake Victims
GCC-PHAT based sound source localization with an 8-microphone array. Supported by NVIDIA and BTF.

**Supported by:**  
🟩 [NVIDIA Academic Hardware Grant Program](https://developer.nvidia.com/academic-hardware)  
🟦 [Bridge to Türkiye Fund – Scientific Research Support Program](https://bridgetoturkiye.org/)

This repository contains an implementation of **GCC-PHAT (Generalized Cross-Correlation with Phase Transform)** for **sound source localization** using a custom-built 8-microphone array. The project was conducted at the Department of Computer Engineering, Yıldız Technical University, under the coordination of **Assoc. Prof. Ali Can Karaca**, and supported by the generous contributions of **NVIDIA** and **Bridge to Türkiye Fund (BTF)**.
---

## 🔧 Project Scope and System Summary

This project addresses the problem of detecting and localizing sound sources, specifically in disaster scenarios such as **earthquake search and rescue**. A number of miniature systems with 2 and 4 microphones were initially designed, but due to hardware limitations, the final system was built using the following professional components:

- **8 SE Electronics SE8 condenser microphones**  
- **Focusrite Scarlett 18i20 audio interface**  
- **Circular microphone array mounted on a tripod**  
- **Jetson Nano 2GB** for embedded real-time processing  
- **7” Waveshare Touchscreen** for GUI visualization
The system captures multichannel audio, applies GCC-PHAT to compute the time differences between microphones, and estimates the **azimuth and elevation angles** of the sound source. It was trained and tested using a dataset collected in both indoor and semi-open environments, and achieved **average localization errors under 3 degrees** with traditional methods.

Due to its low power consumption, mobility, and cost-effectiveness, **Jetson Nano** was selected as the main embedded deployment platform.

---

## 💻 Code & Implementation

This repository provides a simple and clear implementation of the **GCC-PHAT algorithm** for two or more microphones. The following is included:

- 🟩 `main_NVIDIA.py`: Core implementation of GCC-PHAT and visualization


📚 Related Theses
Several undergraduate and graduate theses were completed within the scope of this project. You can access the PDF versions below:

🧑‍🎓 Abdullah Y. & Ayşe K. (2024)
"GCC-PHAT Tabanlı İki Mikrofonla Ses Konum Tespiti Sistemi"
📄 Download PDF

🧑‍🎓 Mücahit D. & Ömer T. (2024)
"Dört Mikrofonla Ses Açısı Tespiti ve Geometrik Hesaplama Yöntemleri"
📄 Download PDF

🎓 Umut K. & Mehmet S. (2024)
"GCC Özellikleriyle Derin Öğrenmeye Dayalı Ses Yönü Tahmini"
📄 Download PDF

🙏 Acknowledgments
We would like to sincerely thank both NVIDIA and the Bridge to Türkiye Fund for their support and generosity. Their contribution not only enabled the acquisition of critical hardware (Jetson Nano kits, microphones, and audio interfaces) but also empowered a team of students to gain hands-on experience in cutting-edge embedded audio research.
