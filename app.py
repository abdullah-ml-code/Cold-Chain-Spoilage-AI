
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="AI Spoilage Predictor", page_icon="vix")

# تحميل الموديل اللي دربناه
model = joblib.load('spoilage_model.pkl')

st.title(" نظام التنبؤ الذكي بمخاطر تلف الشحنات")
st.markdown("أدخل ظروف الشحنة الحالية للحصول على توقع دقيق لمستوى الخطر.")

# تقسيم الصفحة لأعمدة
col1, col2 = st.columns(2)

with col1:
    temp = st.slider("درجة حرارة التخزين (C)", -5.0, 15.0, 4.0)
    excursion = st.number_input("ساعات تجاوز الحرارة (Hours)", 0.0, 24.0, 2.0)
    humidity = st.slider("الرطوبة (%)", 0, 100, 75)
    duration = st.number_input("مدة الرحلة (Hours)", 1.0, 72.0, 12.0)

with col2:
    distance = st.number_input("المسافة (KM)", 10, 2000, 500)
    pkg_quality = st.slider("جودة التغليف (1-10)", 1, 10, 8)
    doors = st.selectbox("عدد مرات فتح الأبواب", [0, 1, 2, 3, 5, 10])
    ambient_temp = st.slider("حرارة الجو الخارجية (C)", 10, 50, 35)

# زر التوقع
if st.button("احسب نسبة المخاطرة"):
    # تجهيز البيانات بنفس ترتيب الموديل
    # ملحوظة: لازم الترتيب يكون مطابق للأعمدة في ملف الـ CSV الأصلي
    features = np.array([[temp, excursion, humidity, duration, distance, pkg_quality, 80.0, doors, 1.0, ambient_temp, 90.0, 50.0]])
    prediction = model.predict(features)[0]
    
    st.divider()
    if prediction > 15:
        st.error(f" تحذير: نسبة خطر التلف مرتفعة جداً: {prediction:.2f}%")
    else:
        st.success(f" الشحنة في حالة جيدة. نسبة الخطر: {prediction:.2f}%")