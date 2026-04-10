# 🩺 Diabetes Prediction API

API dự đoán nguy cơ mắc bệnh tiểu đường sử dụng Machine Learning (Scikit-learn) và FastAPI.

---

## 🚀 1. Giới thiệu

Dự án này cung cấp một REST API cho phép:

* Gửi dữ liệu sức khỏe bệnh nhân
* Nhận dự đoán (có/không mắc tiểu đường)
* Trả về xác suất (probability)

---

## 🧠 2. Công nghệ sử dụng

* Python 3.11
* FastAPI
* Scikit-learn
* Pandas
* Uvicorn
* Docker

---

## 📦 3. Cài đặt & chạy project

### 🔹 Cách 1: Chạy local

#### Bước 1: Cài thư viện

```bash
pip install -r requirements.txt
```

#### Bước 2: Chạy API

```bash
uvicorn diabetes_fastapi:app --reload
```

#### Bước 3: Truy cập

* Swagger UI: http://localhost:8000/docs

---

### 🔹 Cách 2: Chạy bằng Docker

#### Bước 1: Build image

```bash
docker build -t diabetes-api .
```

#### Bước 2: Run container

```bash
docker run -p 8000:8000 diabetes-api
```

#### Bước 3: Truy cập

* http://localhost:8000/docs

---

## 📊 4. Input dữ liệu

API nhận JSON với các trường sau:

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

---

## 🔥 5. API Endpoints

### 🟢 1. Health Check

**GET /**

```bash
GET /
```

**Response**

```json
{
  "message": "Diabetes Prediction API is running"
}
```

---

### 🟢 2. Predict

**POST /predict**

#### Request:

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 25.0,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

#### Response:

```json
{
  "prediction": 1,
  "probability": 0.87
}
```

### 🧠 Giải thích:

* `prediction = 1` → Có nguy cơ mắc tiểu đường
* `prediction = 0` → Không mắc
* `probability` → Xác suất dự đoán

---

## ⚙️ 6. Cách hoạt động

1. Nhận dữ liệu từ request
2. Tiền xử lý (scaler, imputer nếu có)
3. Load model `.pkl`
4. Dự đoán bằng `predict()` và `predict_proba()`
5. Trả kết quả JSON

---

## 📁 7. Cấu trúc project

```
.
├── diabetes_fastapi.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚠️ 8. Lưu ý

* Đảm bảo file `model.pkl` nằm đúng path
* Feature input phải đúng thứ tự khi train model
* Không dùng `--reload` khi deploy production

---

## 💡 9. Hướng phát triển

* Thêm authentication (JWT)
* Deploy lên cloud (Render, AWS, GCP)
* Kết nối database
* Logging & monitoring

---

## 👨‍💻 10. Tác giả

* Anh Tuấn

---

## ⭐ 11. Demo

Sau khi chạy:
👉 http://localhost:8000/docs

Bạn có thể test trực tiếp API tại đây.
