# 📸 Image Organizer

스크린샷 정리를 위한 이미지 파일 자동 분류 프로그램

## 🎯 프로그램 목적

업무 중 스크린샷을 촬영하면 다운로드 폴더에 자동으로 저장되는데, 작업이 끝나면 수많은 이미지 파일들로 인해 폴더가 지저분해집니다. 이 프로그램은 그런 이미지 파일들을 `images` 폴더로 자동으로 이동시켜 한 번에 삭제하기 편하게 만들어 줍니다.

## ✨ 주요 기능

- 🔍 **자동 이미지 파일 감지** - 웬만한 이미지 포맷 모두 지원 (jpg, png, gif, webp, raw 등)
- 📁 **자동 폴더 생성** - `images` 폴더를 자동으로 생성 (이미지가 있을 때만)
- 🔢 **중복 파일명 처리** - 같은 이름의 파일이 있으면 `-0001`, `-0002` 형태로 자동 넘버링
- 🛡️ **안전한 이동** - 기존 `images` 폴더 내부 파일은 건드리지 않음
- 📊 **진행상황 표시** - 이동된 파일 수와 실패한 파일 수를 실시간으로 표시

## 🚀 사용법

### Python으로 실행
```bash
python image_organizer.py
```

### 실행파일로 사용 (Windows)
1. `image_organizer.exe` 다운로드
2. 정리하고 싶은 폴더에 복사
3. 더블클릭으로 실행

## 📋 지원하는 이미지 포맷

- **일반 포맷**: jpg, jpeg, png, gif, bmp, tiff, tif
- **웹 포맷**: webp, svg, ico
- **RAW 포맷**: raw, cr2, nef, orf, sr2

## 💻 개발 환경

- Python 3.6+
- 외부 라이브러리 의존성 없음 (표준 라이브러리만 사용)

## 🔧 개발자용

### 실행파일 빌드
```bash
pip install pyinstaller
pyinstaller --onefile --console image_organizer.py
```

### 프로젝트 구조
```
image-organizer/
├── image_organizer.py    # 메인 프로그램
├── README.md            # 프로젝트 설명
└── releases/            # 실행파일 보관
    └── image_organizer.exe
```

## 📝 라이선스

MIT License

## 👤 개발자

개발자: 해삼씨  
목적: 업무용 스크린샷 정리 자동화
