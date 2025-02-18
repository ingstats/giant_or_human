from tensorflow.keras.models import load_model

# 기존 .h5 모델 로드
model = load_model("keras_model.h5", compile=False)

# 모델을 SavedModel 형식으로 저장
model.save("saved_model", save_format="tf")

print("✅ 모델 변환 완료: 'saved_model' 폴더가 생성되었습니다.")