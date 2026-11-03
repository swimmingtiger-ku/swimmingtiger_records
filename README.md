# 수호회 기록실

고려대학교 수영동아리 수호회의 기록 검색 사이트입니다. 동아리원 전용이라 기록 데이터는 동아리 비밀번호로 암호화되어 있습니다.

- 사이트: https://swimmingtiger-ku.github.io/swimmingtiger_records/
- 기록 원본: 수호회 '고려대 역대 기록 모음집' 구글 스프레드시트 (비공개)

## 기록 갱신 방법
1. 스프레드시트의 '2018~ 기록모음' 탭과 '고려대 기록(2018~)' 탭을 읽어 `data.json`을 만듭니다 (형식은 `tools/build_site.py` 설명 참고). `data.json`은 저장소에 올리지 않습니다.
2. `python3 tools/build_site.py --data data.json --password <동아리 비밀번호>` 로 `index.html`을 다시 만듭니다.
3. 커밋하고 푸시하면 1~2분 뒤 사이트에 반영됩니다.

비밀번호를 바꿀 때도 2~3단계만 다시 하면 됩니다.
