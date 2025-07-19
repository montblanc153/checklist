import csv
import os

# CSV 파일을 읽어서 Excel 호환 형식으로 변환
def create_excel_compatible_csv():
    # 원본 CSV 파일 읽기
    with open('이랜드건설_정확한체크리스트.csv', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Excel에서 한글이 제대로 보이도록 BOM 추가
    with open('이랜드건설_정확한체크리스트_Excel용.csv', 'w', encoding='utf-8-sig') as file:
        file.write(content)
    
    print("Excel 호환 CSV 파일이 생성되었습니다: 이랜드건설_정확한체크리스트_Excel용.csv")
    print("이 파일을 Excel에서 열면 한글이 제대로 보입니다.")

if __name__ == "__main__":
    create_excel_compatible_csv() 