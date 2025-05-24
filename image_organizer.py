import os
import shutil
from pathlib import Path
import re

def is_image_file(file_path):
    """이미지 파일인지 확인하는 함수"""
    image_extensions = {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
        '.webp', '.svg', '.ico', '.raw', '.cr2', '.nef', '.orf', '.sr2'
    }
    return file_path.suffix.lower() in image_extensions

def get_unique_filename(target_dir, filename):
    """중복 파일명이 있을 경우 고유한 파일명을 생성하는 함수"""
    target_path = target_dir / filename
    
    # 파일이 존재하지 않으면 원래 이름 그대로 반환
    if not target_path.exists():
        return filename
    
    # 파일명과 확장자 분리
    stem = target_path.stem  # 확장자 제외한 파일명
    suffix = target_path.suffix  # 확장자
    
    # 숫자 카운터로 고유한 파일명 찾기
    counter = 1
    while True:
        new_filename = f"{stem}-{counter:04d}{suffix}"
        new_path = target_dir / new_filename
        if not new_path.exists():
            return new_filename
        counter += 1

def organize_images(source_dir=None):
    """이미지 파일들을 images 폴더로 이동시키는 함수"""
    
    # 소스 디렉토리 설정 (기본값은 현재 디렉토리)
    if source_dir is None:
        source_dir = Path.cwd()
    else:
        source_dir = Path(source_dir)
    
    # 소스 디렉토리 존재 확인
    if not source_dir.exists():
        print(f"❌ 디렉토리를 찾을 수 없습니다: {source_dir}")
        return
    
    # 이미지 파일 찾기
    image_files = []
    
    print(f"\n🔍 {source_dir}에서 이미지 파일 검색 중...")
    
    for file_path in source_dir.iterdir():
        # 파일인지 확인 (디렉토리 제외)
        if not file_path.is_file():
            continue
        
        # images 폴더 내부의 파일은 제외
        if file_path.parent.name == "images":
            continue
            
        # 이미지 파일인지 확인
        if is_image_file(file_path):
            image_files.append(file_path)
    
    # 이미지 파일이 없으면 종료
    if not image_files:
        print("📭 이동할 이미지 파일이 없습니다.")
        return
    
    # 이미지 파일이 있으면 images 폴더 생성
    images_dir = source_dir / "images"
    images_dir.mkdir(exist_ok=True)
    print(f"📁 images 폴더 생성: {images_dir}")
    
    # 이미지 파일 이동
    moved_count = 0
    error_count = 0
    
    for file_path in image_files:
        try:
            # 고유한 파일명 생성
            unique_filename = get_unique_filename(images_dir, file_path.name)
            target_path = images_dir / unique_filename
            
            # 파일 이동
            shutil.move(str(file_path), str(target_path))
            
            # 결과 출력
            if unique_filename != file_path.name:
                print(f"📸 {file_path.name} → {unique_filename} (이름 변경됨)")
            else:
                print(f"📸 {file_path.name} → images/")
            
            moved_count += 1
            
        except Exception as e:
            print(f"❌ {file_path.name} 이동 실패: {e}")
            error_count += 1
    
    # 결과 요약
    print(f"\n✅ 작업 완료!")
    print(f"   📸 이동된 이미지: {moved_count}개")
    if error_count > 0:
        print(f"   ❌ 실패한 파일: {error_count}개")

def main():
    """메인 함수"""
    print("🖼️  이미지 파일 정리 프로그램")
    print("=" * 40)
    
    # 사용자 입력 받기
    user_input = input("정리할 폴더 경로를 입력하세요 (엔터: 현재 폴더): ").strip()
    
    if user_input:
        source_directory = user_input
    else:
        source_directory = None
    
    # 이미지 정리 실행
    organize_images(source_directory)
    
    input("\n아무 키나 누르면 종료합니다...")

if __name__ == "__main__":
    main()
