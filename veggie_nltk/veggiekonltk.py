from konlpy.tag import Okt, Hannanum
from nltk import pos_tag, Freq
from nltk.corpus import stopwords
from collections import Counter
twitter = Okt()
hannanum = Hannanum()


korean_sentence = "리듬엔'은 고객사의 브랜드를 이해하고 브랜드의 가치를 온라인에 담애는 글로벌 브랜드 파트너입니다. 리듬엔은 크리에이티브로 뭉친 사람들이 모여있는 곳으로 감각있고 창의적인 전문가들이 브랜드 플랫폼 서비스를 개발합니다.\n\n\n주요업무\n• HTML·퍼블리싱·UI개발\n• UI·UX, 자바스크립트\n\n자격요건\n• 성별무관\n• 만 23세 이상 33세 이하\n• 초대졸이상\n• 크로스브라우징/웹표준 준수 가능자\n• 웹 접근성/반응형 가능자\n• Javascript/Jauery 가능자\n• Mobile/App 가능자\n\n우대사항\n• 경력 1년 이상\n• 컴퓨터 관련 전공\n• 워드프레스/부트스트랩 가능\n• 고도몰/카페24가능자\n• 모바일앱 UI가이드 제작 경험자\n• 에이전시 경력자\n\n혜택 및 복지\n• 장기근속자 포상제\n• 이 달의 우수사원 포상\n• 킹갓제너럴능력자 재택근무 가능\n• 통신비 지원\n• 맥북 지원\n• 점심, 간식비 제공\n• 프로젝트 완료 후 리프레쉬 휴가 (휴가비 지원)\n• 불금 조기퇴근\n• 피곤한 월요일 1시간 늦게 출근\n\n• 연금·보험 국민연금, 고용보험, 산재보험, 건강보험\n• 휴무·휴가·행사 주5일근무, 연차, 월차, Refresh휴가, 워크샵/MT\n• 보상·수당·지원 스톡옵션, 각종 경조금 지원, 인센티브제, 자기계발비 지원, \n• 도서구입비 지원, 휴가비 지원"

tokens = hannanum.morphs(korean_sentence)
stop_words = set(stopwords.words('english'))
stop_words.add(',')
stop_words.add('.')
filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
filtered_sentence = [word for word in filtered_sentence if len(word) > 1]
filtered_sentence = [word for word in filtered_sentence if not word.isnumeric()]
filtered_sentence

pos = twitter.pos(korean_sentence, norm=True, stem=True)
pos
Counter(filtered_sentence)
Counter(pos)
print(pos)
