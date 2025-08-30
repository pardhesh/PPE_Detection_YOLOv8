# PPE Detection using YOLOv8

## 📌 Project Overview
This project implements a **Personal Protective Equipment (PPE) Detection System** using **YOLOv8**.  
It allows detection of safety equipment such as **helmets, vests, boots, gloves, and humans** from both **webcam (real-time)** and **uploaded images/videos** via a **Flask web application**.

---

## 🚀 Features
- Real-time webcam PPE detection.
- Image and video upload for detection.
- Results available for **viewing and downloading in MP4 format**.
- User-friendly web UI with Bootstrap styling.
- Model trained with **class-weighted loss** to handle class imbalance.

---

## 🧠 Model Details
- **Model Architecture**: YOLOv8s (Small)
- **Input Size**: 768x768
- **Training Epochs**: 100
- **Parameters**: ~11.1M
- **GFLOPs**: 28.4

### 📊 Validation Metrics (Train Split)
- **mAP@50**: 0.922  
- **mAP@50-95**: 0.773  
- **Precision**: 0.965  
- **Recall**: 0.834  

**Per-Class Performance (Validation)**:  
- Boots: mAP@50 = 0.978, mAP@50-95 = 0.777  
- Gloves: mAP@50 = 0.720, mAP@50-95 = 0.564  
- Helmet: mAP@50 = 0.974, mAP@50-95 = 0.785  
- Human: mAP@50 = 0.967, mAP@50-95 = 0.884  
- Vest: mAP@50 = 0.973, mAP@50-95 = 0.857  

### 📊 Test Metrics (Unseen Data)
- **mAP@50**: 0.977  
- **mAP@50-95**: 0.816  
- **Precision**: 0.956  
- **Recall**: 0.963  

**Per-Class Performance (Test)**:  
- Boots: mAP@50 = 0.995, mAP@50-95 = 0.794  
- Gloves: mAP@50 = 0.936, mAP@50-95 = 0.677  
- Helmet: mAP@50 = 0.975, mAP@50-95 = 0.779  
- Human: mAP@50 = 0.988, mAP@50-95 = 0.931  
- Vest: mAP@50 = 0.991, mAP@50-95 = 0.897  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ppe-detection.git
cd ppe-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Flask App
```bash
python app.py
```
Then open browser at: **http://127.0.0.1:5000/**

---

## 📂 Project Structure
```
PPE-Detection/
│── app.py                # Flask web app
│── requirements.txt      # Dependencies
│── static/
│   └── results/          # Processed outputs (images/videos)
│── templates/
│   ├── index.html        # Homepage UI
│   └── result.html       # Results UI
│── weights/
│   └── best.pt           # Trained YOLOv8 model weights
```

---

## 📌 Usage
1. Select **Webcam** for real-time detection.  
2. Upload an **image or video** for processing.  
3. View detection results on the results page.  
4. Download processed video in **MP4 format**.  

---

## ✅ Results & Insights
- Model performs well on **boots, helmet, human, and vest** classes with **mAP > 0.9**.  
- **Gloves detection is comparatively weaker** due to fewer training samples.  
- Class-weighted training improved detection of rare classes.  
- Real-time performance is achieved with **~14ms inference per image** on **Tesla T4 GPU**.

---

## 📢 Future Improvements
- Increase glove dataset size for better accuracy.  
- Deploy model on **edge devices** (Jetson Nano, Raspberry Pi).  
- Add **multi-camera support**.  
- Integrate with **alert systems** for safety monitoring.  

---

## 🧑‍💻 Author
Developed by **[Your Name]** 🚀  
For research, learning, and industrial safety monitoring applications.
