# Releases

이 폴더에는 빌드된 실행파일들이 저장됩니다.

## 최신 버전

- `image_organizer.exe` - Windows용 실행파일

## 빌드 방법

```bash
pip install pyinstaller
pyinstaller --onefile --console image_organizer.py
```

빌드 후 `dist/` 폴더에서 실행파일을 이 폴더로 복사하세요.
