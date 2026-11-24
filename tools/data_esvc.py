# -*- coding: utf-8 -*-
"""E-service definitions (rendered by assets/svc.js). Text tuples are (English, Korean, Traditional Chinese);
build.py localises every 3-tuple of strings. Currency: Baekhyeon Hwarang Dollar (BH$)."""

CUR = "BH$"

L = {
    "next": ("Next", "다음", "下一步"), "back": ("Back", "이전", "上一步"), "submit": ("Submit", "제출", "遞交"),
    "pay": ("Pay", "결제", "付款"), "print": ("Print", "인쇄", "列印"), "again": ("Start a new one", "새로 시작", "重新開始"),
    "processing": ("Processing…", "처리 중…", "處理中…"), "choose": ("-- Please select --", "-- 선택하세요 --", "-- 請選擇 --"),
    "errReq": ("This field is required.", "필수 입력 항목입니다.", "此欄必須填寫。"),
    "errAgree": ("Please tick the box to continue.", "계속하려면 확인란에 체크해 주세요.", "請剔選方格以繼續。"),
    "errEmail": ("Please enter a valid email address.", "올바른 이메일 주소를 입력하세요.", "請輸入有效的電郵地址。"),
    "errTel": ("Please enter a valid phone number.", "올바른 전화번호를 입력하세요.", "請輸入有效的電話號碼。"),
    "errId": ("Invalid identity card number. Example format: A123456(3).", "신분증 번호가 올바르지 않습니다. 형식 예: A123456(3)", "身份證號碼不正確。格式例子：A123456(3)。"),
    "errDate": ("Please enter a valid date (YYYY-MM-DD) that is not in the future.", "미래가 아닌 올바른 날짜(YYYY-MM-DD)를 입력하세요.", "請輸入有效而不是未來的日期（YYYY-MM-DD）。"),
    "errName": ("Use English letters, spaces, hyphens and apostrophes only.", "영문, 공백, 하이픈, 아포스트로피만 사용할 수 있습니다.", "只可使用英文字母、空格、連字號及撇號。"),
    "errCode": ("Please enter exactly 4 digits.", "숫자 4자리를 입력하세요.", "請輸入4位數字。"),
    "errPw": ("At least 8 characters with letters and numbers.", "영문과 숫자를 포함해 8자 이상이어야 합니다.", "密碼須至少8個字元，並包含英文字母及數字。"),
    "errMatch": ("The two entries do not match.", "두 입력값이 일치하지 않습니다.", "兩次輸入的內容不相符。"),
    "errCard": ("Please enter a valid card number.", "올바른 카드 번호를 입력하세요.", "請輸入有效的信用卡號碼。"),
    "errExp": ("Please enter a valid expiry date (MM/YY).", "올바른 유효기간(MM/YY)을 입력하세요.", "請輸入有效的到期日（MM/YY）。"),
    "errCvv": ("Please enter the 3 or 4 digit security code.", "3~4자리 보안코드를 입력하세요.", "請輸入3或4位數字的保安碼。"),
    "errNum": ("Please enter a number.", "숫자를 입력하세요.", "請輸入數字。"),
    "errRef": ("Please enter a valid reference number.", "올바른 접수번호를 입력하세요.", "請輸入有效的參考編號。"),
    "errPay": ("Please select a payment method.", "결제 수단을 선택하세요.", "請選擇付款方法。"),
    "errSlot": ("Please select an office, a date and a time.", "사무소, 날짜, 시간을 모두 선택하세요.", "請選擇辦事處、日期及時間。"),
    "errFileSize": ("The file is larger than 2MB.", "파일이 2MB를 초과합니다.", "檔案超過2MB。"),
    "errPhotoType": ("The photograph must be a JPEG image.", "사진은 JPEG 이미지여야 합니다.", "照片必須為JPEG圖像。"),
    "errPhotoSize": ("The photograph is larger than 5MB.", "사진이 5MB를 초과합니다.", "照片超過5MB。"),
    "errPhotoDim": ("The image must be at least 1200 x 1600 pixels.", "이미지는 최소 1200 x 1600픽셀이어야 합니다.", "圖像大小至少須為1200 x 1600像素。"),
    "errPhotoRatio": ("The image must have a width-to-height ratio of 40:50.", "이미지의 가로:세로 비율은 40:50이어야 합니다.", "圖像的闊高比例必須為40:50。"),
    "applicant": ("Applicant", "신청인", "申請人"), "idno": ("Identity card number", "신분증 번호", "身份證號碼"),
    "dob": ("Date of birth (YYYY-MM-DD)", "생년월일(YYYY-MM-DD)", "出生日期（YYYY-MM-DD）"),
    "office": ("Office", "사무소", "辦事處"), "date": ("Date", "날짜", "日期"), "time": ("Time", "시간", "時間"),
    "refNo": ("Reference number", "접수번호", "參考編號"), "when": ("Submitted at", "제출 일시", "遞交時間"),
    "trn": ("Transaction Reference Number (TRN)", "거래 참조번호(TRN)", "交易參考編號（TRN）"),
    "paid": ("Amount paid", "납부 금액", "已繳費用"), "total": ("Total", "합계", "總額"),
    "payMethod": ("Payment method", "결제 수단", "付款方法"),
    "payRedirect": ("You will be taken to the payment provider to complete the payment. Press Pay to continue.", "결제 대행사 화면에서 결제를 마치게 됩니다. 계속하려면 결제 버튼을 누르세요.", "你會被帶往付款服務供應商的頁面完成付款。請按「付款」繼續。"),
    "search": ("Search", "조회", "查詢"), "updated": ("Last updated", "최종 갱신", "最後更新"), "remark": ("Remarks", "비고", "備註"),
    "login": ("Login", "로그인", "登入"), "logout": ("Logout", "로그아웃", "登出"),
    "makeAppt": ("Make an appointment", "예약하기", "預約"), "findAppt": ("Change, cancel or enquire about an appointment", "예약 변경·취소·조회", "更改、取消或查詢預約"),
    "findIntro": ("Enter the reference number of your appointment and the 4-digit enquiry code you set.", "예약 접수번호와 직접 설정한 4자리 조회 코드를 입력하세요.", "請輸入預約的參考編號及你設定的4位數字查詢編號。"),
    "enqCode": ("Enquiry code (4 digits)", "조회 코드(4자리)", "查詢編號（4位數字）"),
    "notFound": ("No matching appointment was found in this browser.", "이 브라우저에서 일치하는 예약을 찾을 수 없습니다.", "在此瀏覽器內找不到相符的預約。"),
    "cancelAppt": ("Cancel this appointment", "이 예약 취소", "取消此預約"), "cancelled": ("The appointment has been cancelled.", "예약이 취소되었습니다.", "預約已取消。"),
    "pickOfficeDate": ("Select an office and a date to see the available time slots.", "사무소와 날짜를 선택하면 가능한 시간이 표시됩니다.", "請選擇辦事處及日期，以查看可預約的時段。"),
    "noSlots": ("No time slot is available on this date.", "이 날짜에는 예약 가능한 시간이 없습니다.", "此日期沒有可預約的時段。"),
    "dow": [("Sun", "일", "日"), ("Mon", "월", "一"), ("Tue", "화", "二"), ("Wed", "수", "三"), ("Thu", "목", "四"), ("Fri", "금", "五"), ("Sat", "토", "六")],
    "compute": ("Compute", "계산", "計算"),
    "stepFmt": ("Step {n}: {t}", "{n}단계: {t}", "步驟{n}：{t}"),
    "dlPassport": ("Download passport (PDF)", "여권 내려받기(PDF)", "下載護照（PDF）"),
    "generating": ("Generating PDF…", "PDF 만드는 중…", "正在產生PDF…"),
}

OFFICES = [
    ["hq", ("Immigration Headquarters (Baekhyeon Maeul Complex 3)", "출입경사무처 본부(백현마을 3단지)", "入境事務處總部（柏峴마을3社區）")],
    ["b3", ("Baekhyeon Maeul Complex 3 Branch Office", "백현마을 3단지 지소", "柏峴마을3社區分區辦事處")],
    ["b4", ("Baekhyeon Maeul Complex 4 Branch Office", "백현마을 4단지 지소", "柏峴마을4社區分區辦事處")],
]

SEX = [["M", ("Male", "남", "男")], ["F", ("Female", "여", "女")]]
MARITAL = [["single", ("Single", "미혼", "未婚")], ["married", ("Married", "기혼", "已婚")], ["divorced", ("Divorced", "이혼", "離婚")], ["widowed", ("Widowed", "사별", "喪偶")]]


def F(n, l, t="text", **kw):
    d = {"n": n, "l": l, "t": t}
    d.update(kw)
    return d


# ----------------------------------------------------------------------------- passport application
PASSPORT = {
    "type": "wizard", "prefix": "PA",
    "title": ("Application through the Internet for Baekhyeon Hwarang SAR Passport", "인터넷 백현화랑 특별행정구 여권 신청", "透過互聯網申請柏峴화랑特別行政區護照"),
    "fee": {
        "base": [
            {"when": {"ageGroup": "18+", "pages": "32"}, "l": ("Passport fee (aged 16 or above, 32 pages)", "여권 수수료(만 16세 이상, 32쪽)", "護照費用（十六歲或以上，32頁）"), "amt": 430},
            {"when": {"ageGroup": "18+", "pages": "48"}, "l": ("Passport fee (aged 16 or above, 48 pages)", "여권 수수료(만 16세 이상, 48쪽)", "護照費用（十六歲或以上，48頁）"), "amt": 520},
            {"when": {"ageGroup": "16-17", "pages": "32"}, "l": ("Passport fee (aged 16 or above, 32 pages)", "여권 수수료(만 16세 이상, 32쪽)", "護照費用（十六歲或以上，32頁）"), "amt": 430},
            {"when": {"ageGroup": "16-17", "pages": "48"}, "l": ("Passport fee (aged 16 or above, 48 pages)", "여권 수수료(만 16세 이상, 48쪽)", "護照費用（十六歲或以上，48頁）"), "amt": 520},
            {"when": {"pages": "32"}, "l": ("Passport fee (aged under 16, 32 pages)", "여권 수수료(만 16세 미만, 32쪽)", "護照費用（十六歲以下，32頁）"), "amt": 215},
            {"when": {"pages": "48"}, "l": ("Passport fee (aged under 16, 48 pages)", "여권 수수료(만 16세 미만, 48쪽)", "護照費用（十六歲以下，48頁）"), "amt": 260},
        ],
        "extra": [
            {"when": {"office": "mission", "delivery": "reg"}, "l": ("Delivery by double registered air mail", "이중 등기 항공우편 배송", "以雙掛號航空郵件遞送"), "amt": 50},
            {"when": {"office": "mission", "delivery": "exp"}, "l": ("Delivery by express dispatch service (Asia-Pacific)", "특급 배송 서비스(아시아·태평양)", "以速遞服務遞送（亞太區）"), "amt": 210},
        ],
    },
    "steps": [
        {"title": ("Notes", "유의사항", "注意事項"),
         "intro": ("<p>If you are a Korean citizen, and a permanent resident of Baekhyeon Hwarang holding a valid Baekhyeon Hwarang permanent identity card, you may apply for a Baekhyeon Hwarang SAR Passport through the Internet. Please prepare your identity card, a recent colour photograph (JPEG, white background) and the supporting documents required for your age group.</p><p>Successful submission does not mean that your application is approved. An application without a standard photograph, full supporting documents or payment will not be processed.</p>",
                   "<p>대한민국 국민이면서 유효한 백현화랑 영구 신분증을 소지한 백현화랑 영주권자는 인터넷으로 백현화랑 특별행정구 여권을 신청할 수 있습니다. 신분증, 최근 컬러 사진(JPEG, 흰색 배경)과 연령대별 필요 증빙서류를 준비해 주세요.</p><p>제출에 성공했다고 해서 신청이 승인된 것은 아닙니다. 규격 사진, 전체 증빙서류 또는 수수료 납부가 없는 신청은 처리되지 않습니다.</p>",
                   "<p>若你是大韓民國國民，並且持有有效柏峴화랑永久性居民身份證的柏峴화랑永久性居民，你可透過互聯網申請柏峴화랑特別行政區護照。請預備你的身份證、背景為白色的彩色近照（JPEG格式），以及所屬年齡組別所需的證明文件。</p><p>成功遞交並不代表申請已獲批准。如沒有上載符合標準規格的照片、全部證明文件或繳付護照費用，本處將不受理該申請。</p>"),
         "fields": [F("agree", ("I have read and understood the above notes.", "위 유의사항을 읽고 이해했습니다.", "我已閱讀並明白上述注意事項。"), "checkbox", req=True)]},
        {"title": ("Application Type", "신청 유형", "申請類別"), "fields": [
            F("ageGroup", ("Age group of the applicant", "신청인의 연령대", "申請人的年齡組別"), "radio", req=True, o=[["18+", ("Aged 18 or above", "만 18세 이상", "十八歲或以上")], ["16-17", ("Aged 16 or 17", "만 16세 또는 17세", "十六或十七歲")], ["11-15", ("Child aged between 11 and 15", "만 11세~15세 아동", "十一至十五歲兒童")], ["u11", ("Child aged below 11", "만 11세 미만 아동", "十一歲以下兒童")]]),
            F("apptype", ("Type of application", "신청 종류", "申請種類"), "radio", req=True, o=[["first", ("First application", "최초 신청", "首次申請")], ["replace", ("Replacement of an existing passport", "기존 여권 교체", "換領現有護照")]]),
            F("pages", ("Number of pages", "쪽수", "頁數"), "radio", req=True, o=[["32", ("32 pages", "32쪽", "32頁")], ["48", ("48 pages", "48쪽", "48頁")]]),
        ]},
        {"title": ("Applicant's Particulars", "신청인 인적사항", "申請人資料"), "fields": [
            F("surname", ("Surname (in English)", "성(영문)", "姓氏（英文）"), req=True, v="enname", ph="SHIN", rl=("Surname", "성", "姓氏")),
            F("given", ("Given names (in English)", "이름(영문)", "名字（英文）"), req=True, v="enname", ph="JIHOO", rl=("Given names", "이름", "名字")),
            F("local", ("Name in Chinese / Korean characters (if any)", "한글·한자 성명(있는 경우)", "中文／韓文姓名（如有）")),
            F("sex", ("Sex", "성별", "性別"), "select", req=True, o=SEX),
            F("dob", ("Date of birth (YYYY-MM-DD)", "생년월일(YYYY-MM-DD)", "出生日期（YYYY-MM-DD）"), req=True, v="date", ph="YYYY-MM-DD"),
            F("pob", ("Place of birth", "출생지", "出生地點"), req=True),
            F("idno", ("Baekhyeon Hwarang identity card number", "백현화랑 신분증 번호", "柏峴화랑身份證號碼"), req=True, v="bhid", ph="A123456(3)", sens=True, h=("Example format: A123456(3)", "형식 예: A123456(3)", "格式例子：A123456(3)")),
            F("marital", ("Marital status", "혼인 여부", "婚姻狀況"), "select", req=True, o=MARITAL),
        ]},
        {"title": ("Contact Details", "연락처", "聯絡資料"), "fields": [
            F("mobile", ("Mobile phone number (to receive SMS)", "휴대전화 번호(SMS 수신용)", "流動電話號碼（接收短訊）"), "tel", req=True, v="tel", sens=True),
            F("email", ("Email address", "이메일 주소", "電郵地址"), "email", req=True, v="email", sens=True),
            F("addr", ("Residential address", "거주지 주소", "住址"), "textarea", req=True, full=True),
        ]},
        {"title": ("Photograph", "사진", "照片"), "intro": ("<p>Upload a recent colour photograph in plain white background (JPEG, 5MB or below, at least 1200 x 1600 pixels, width-to-height ratio 40:50). See the photograph requirements for details.</p>",
                                                       "<p>흰색 배경의 최근 컬러 사진을 업로드하세요(JPEG, 5MB 이하, 최소 1200 x 1600픽셀, 가로:세로 비율 40:50). 자세한 내용은 사진 규격을 참고하세요.</p>",
                                                       "<p>請上載背景為白色的彩色近照（JPEG格式，5MB或以下，最少1200 x 1600像素，闊高比例40:50）。詳情請參閱照片規格。</p>"),
         "fields": [F("photo", ("Photograph", "사진", "照片"), "photo", req=True, full=True)]},
        {"title": ("Supporting Documents", "증빙서류", "證明文件"), "showIf": {"n": "ageGroup", "ne": "18+"}, "fields": [
            F("pname", ("Name of consenting parent / legal guardian", "동의하는 부모·법정대리인 성명", "同意申請的父、母或合法監護人姓名"), req=True),
            F("pid", ("Parent / guardian's identity card number", "부모·법정대리인의 신분증 번호", "父、母或監護人的身份證號碼"), req=True, v="bhid", ph="A123456(3)", sens=True),
            F("prel", ("Relationship", "관계", "關係"), "select", req=True, o=[["father", ("Father", "부", "父")], ["mother", ("Mother", "모", "母")], ["guardian", ("Legal guardian", "법정대리인", "合法監護人")]]),
            F("fparent", ("Copy of the consenting parent / guardian's identity card or travel document", "동의하는 부모·법정대리인의 신분증 또는 여행증명서 사본", "同意申請的父、母或監護人的身份證或旅行證件副本"), "file", req=True, full=True),
            F("fbirth", ("Copy of birth certificate (not required if born in Baekhyeon Hwarang)", "출생증명서 사본(백현화랑에서 출생한 경우 불필요)", "出生證明書副本（如在柏峴화랑出生則無需提交）"), "file", full=True),
            F("fschool", ("Copy of school document bearing the child's photograph", "자녀 사진이 있는 학교 서류 사본", "附有兒童照片的學校證明文件副本"), "file", req=True, full=True, showIf={"n": "ageGroup", "eq": "u11"}),
        ]},
        {"title": ("Collection of Passport", "여권 수령", "領取護照"), "fields": [
            F("office", ("Place of collection", "수령 장소", "領取地點"), "select", req=True, o=OFFICES + [["mission", ("Korean Diplomatic and Consular Mission (outside Baekhyeon Hwarang)", "재외공관(백현화랑 밖)", "大韓民國駐外使領館（柏峴화랑以外地區）")]]),
            F("mission", ("Name of the Korean Diplomatic and Consular Mission", "재외공관 명칭", "大韓民國駐外使領館名稱"), req=True, showIf={"n": "office", "eq": "mission"}),
            F("delivery", ("Delivery method", "배송 방법", "遞送方式"), "select", req=True, showIf={"n": "office", "eq": "mission"}, o=[["reg", ("Double registered air mail", "이중 등기 항공우편", "雙掛號航空郵件")], ["exp", ("Express dispatch service", "특급 배송", "速遞服務")]]),
        ]},
        {"title": ("Review and Declaration", "확인 및 선서", "核對及聲明"), "type": "review"},
        {"title": ("Payment", "결제", "付款"), "type": "pay"},
        {"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"},
    ],
    "declare": F("declare", ("I declare that the information given in this application is true and correct, and I understand that the applicant will be required to make a further declaration upon collection of the passport.",
                             "이 신청서에 기재한 정보가 사실이며 정확함을 선서합니다. 여권을 수령할 때 다시 선서해야 함을 이해합니다.",
                             "本人聲明本申請所填報的資料全部屬實及正確，並明白申請人在領取護照時須再作出聲明。"), "checkbox", req=True),
    "pay": {"methods": [["card", ("Credit card (VISA, Mastercard and JCB only)", "신용카드(VISA, Mastercard, JCB만 가능)", "信用卡（只接受VISA、萬事達卡及JCB）")], ["ops", ("OPS (Online Payment Service)", "OPS(온라인 결제 서비스)", "網上繳費服務（OPS）")], ["fps", ("Instant bank transfer", "계좌 간편이체", "即時轉賬")], ["wallet", ("Mobile wallet", "모바일 지갑", "流動錢包")]],
            "fields": {
                "card": [F("cardname", ("Name on card", "카드 소유자 이름", "持卡人姓名"), req=True, sens=True), F("card", ("Card number", "카드 번호", "信用卡號碼"), req=True, v="cardnum", im="numeric", sens=True, max=23),
                         F("exp", ("Expiry date (MM/YY)", "유효기간(MM/YY)", "到期日（MM/YY）"), req=True, v="exp", ph="MM/YY", sens=True, max=7), F("cvv", ("Security code", "보안코드", "保安碼"), "password", req=True, v="cvv", im="numeric", sens=True, max=4)],
                "ops": [F("opsno", ("OPS account number", "OPS 계좌번호", "OPS帳戶號碼"), req=True, v="num", im="numeric", sens=True), F("opspw", ("OPS Internet password", "OPS 인터넷 비밀번호", "OPS互聯網密碼"), "password", req=True, sens=True)],
            }},
    "doneText": ("<strong>Your application has been submitted successfully.</strong> Successful submission does not mean that your application is approved. A Collection Notice specifying the period and office for collection will be sent to you after processing.",
                 "<strong>신청이 정상적으로 제출되었습니다.</strong> 제출에 성공했다고 해서 신청이 승인된 것은 아닙니다. 처리 후 수령 기간과 수령 사무소가 적힌 수령 통지서가 발송됩니다.",
                 "<strong>你的申請已成功遞交。</strong>成功遞交並不代表申請已獲批准。處理完畢後，本處會向你發出列明領證期限及辦事處的領證通知。"),
    "doneNote": ("Please print or keep this page. You may check the progress with the application reference number through the online status enquiry.", "이 페이지를 인쇄하거나 보관해 주세요. 접수번호로 신청 현황 온라인 조회에서 진행 상황을 확인할 수 있습니다.", "請列印或保存此頁。你可憑申請參考編號，透過網上查詢服務查閱申請進度。"),
    "doneRows": [{"n": "surname", "l": ("Surname", "성", "姓氏")}, {"n": "given", "l": ("Given names", "이름", "名字")}, {"n": "office", "l": ("Place of collection", "수령 장소", "領取地點"), "o": OFFICES + [["mission", ("Korean Diplomatic and Consular Mission", "재외공관", "大韓民國駐外使領館")]]}],
}

# ----------------------------------------------------------------------------- appointment booking
def booking(kind):
    docs = {
        "td": [["passport", ("Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照")], ["reentry", ("Re-entry Permit", "재입경 허가증", "回港證")], ["docid", ("Document of Identity for Visa Purposes", "비자용 신분증명서", "簽證身份書")], ["seaman", ("Seaman's Identity Book", "선원 신분증", "海員身份證")]],
        "id": [["idnew", ("Application for Baekhyeon Hwarang Smart Identity Card", "백현화랑 스마트 신분증 신청", "申領柏峴화랑智能身份證")], ["idrepl", ("Replacement of Smart Identity Card", "스마트 신분증 재발급", "換領智能身份證")], ["idcoll", ("Collection of Smart Identity Card", "스마트 신분증 수령", "領取智能身份證")]],
    }[kind]
    title = {"td": ("Appointment Booking for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件"),
             "id": ("Appointment Booking for Smart Identity Card", "스마트 신분증 신청 예약", "預約申領智能身份證")}[kind]
    return {
        "type": "booking", "title": title, "offices": OFFICES,
        "steps": [
            {"title": ("Input Appointment Details", "예약 정보 입력", "輸入預約資料"), "gen": "applicants",
             "intro": ("<p>You can make advance booking within 24 working days (Monday to Saturday, except General Holidays). For a child without an identity card, enter the identity card number of the applying parent / guardian and the child's date of birth. Set a 4-digit enquiry code for later change, cancel or enquiry.</p>",
                       "<p>24근무일(월~토요일, 일반 공휴일 제외) 이내로 미리 예약할 수 있습니다. 신분증이 없는 자녀는 신청 부모·보호자의 신분증 번호와 자녀의 생년월일을 입력하세요. 이후 변경·취소·조회에 사용할 4자리 조회 코드를 설정하세요.</p>",
                       "<p>你可預約其後24個工作天（星期一至星期六，公眾假期除外）內的時段。未持有身份證的兒童，請輸入申請的父、母或監護人的身份證號碼及該兒童的出生日期。請設定一個4位數字的查詢編號，以便日後更改、取消或查詢預約。</p>"),
             "fields": [F("doc1", ("Service", "서비스", "服務"), "select", req=True, o=docs), F("doc2", ("Second service (optional)", "두 번째 서비스(선택)", "第二項服務（可選）"), "select", o=docs),
                        F("count", ("Number of applicants", "신청 인원", "申請人數目"), "select", req=True, o=[[str(n), str(n)] for n in (1, 2, 3, 4)])],
             "extra": [F("code", ("Enquiry code (4 digits)", "조회 코드(4자리)", "查詢編號（4位數字）"), "password", req=True, v="digits4", max=4, im="numeric", sens=True),
                       F("code2", ("Confirm enquiry code", "조회 코드 확인", "確認查詢編號"), "password", req=True, v="match", of="code", max=4, im="numeric", sens=True)]},
            {"title": ("Select Office and Appointment Date", "사무소 및 예약 날짜 선택", "選擇辦事處及預約日期"), "fields": [F("slot_od", ("Office and date", "사무소·날짜", "辦事處及日期"), "slot", part="od", full=True)]},
            {"title": ("Select Time and Appointment Reminder", "시간 및 예약 알림 선택", "選擇時間及預約提示"), "fields": [
                F("slot_t", ("Time", "시간", "時間"), "slot", part="time", full=True),
                F("email", ("Email address for reminder (optional)", "알림 받을 이메일(선택)", "接收提示的電郵地址（可選）"), "email", v="email", sens=True),
                F("remind", ("Send me an appointment reminder 2 days before the appointment", "예약 2일 전에 알림을 보내 주세요", "請在預約日期前2日向我發出預約提示"), "checkbox")]},
            {"title": ("Confirmation", "확인", "確認"), "type": "review"},
            {"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"},
        ],
        "doneText": ("<strong>Your appointment has been made.</strong> Please bring your identity card and the required supporting documents, and arrive at the office at least 10 minutes before the appointment time.",
                     "<strong>예약이 완료되었습니다.</strong> 신분증과 필요한 증빙서류를 지참하고 예약 시간 최소 10분 전에 사무소에 도착해 주세요.",
                     "<strong>你的預約已完成。</strong>請攜帶身份證及所需的證明文件，並最少於預約時間前10分鐘到達辦事處。"),
        "doneNote": ("Keep the reference number and your 4-digit enquiry code. You may change or cancel the appointment at least 1 day before the appointment date.", "접수번호와 4자리 조회 코드를 보관하세요. 예약일 1일 전까지 예약을 변경하거나 취소할 수 있습니다.", "請保存參考編號及4位數字查詢編號。你可於預約日期前至少1日更改或取消預約。"),
    }


# ----------------------------------------------------------------------------- status enquiries
TD_STATUS = {
    "type": "status", "title": ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度"),
    "intro": ("<p>Enter your application reference number and the day and year of your birth.</p>", "<p>신청 접수번호와 생일(일), 출생 연도를 입력하세요.</p>", "<p>請輸入申請的參考編號，以及你出生的日及年。</p>"),
    "statusLabel": ("Application status", "신청 상태", "申請進度"),
    "fields": [F("ref", ("Application reference number", "신청 접수번호", "申請參考編號"), req=True, v="ref"), F("dobDay", ("Day of birth (1-31)", "생일(1~31)", "出生日（1-31）"), req=True, v="num", im="numeric", max=2), F("dobYear", ("Year of birth (YYYY)", "출생 연도(YYYY)", "出生年份（YYYY）"), req=True, v="num", im="numeric", max=4)],
    "results": [
        [("Application received", "신청 접수", "已收到申請"), ("Your application has been received. It will be processed after all documents and payment are received.", "신청이 접수되었습니다. 모든 서류와 결제가 확인되면 처리가 시작됩니다.", "本處已收到你的申請，待收妥所有文件及款項後便會處理。")],
        [("Under processing", "처리 중", "處理中"), ("Your application is being processed. The normal processing time is 5 working days.", "신청을 처리하고 있습니다. 통상 처리 기간은 5근무일입니다.", "你的申請正在處理中，一般處理時間為5個工作天。")],
        [("Approved – ready for collection", "승인 – 수령 가능", "已獲批准 – 可領取"), ("Your new travel document is ready. Please collect it at the selected office within the period stated in the Collection Notice.", "새 여행증명서가 준비되었습니다. 수령 통지서에 적힌 기간 내에 선택한 사무소에서 수령하세요.", "你的新旅行證件已準備好，請在領證通知所列的期限內到所選定的辦事處領取。")],
        [("Further documents required", "추가 서류 필요", "須補交文件"), ("Please submit the additional documents requested in the notice sent to you.", "발송된 통지서에 안내된 추가 서류를 제출해 주세요.", "請補交本處發出的通知所要求的文件。")],
    ],
}
VISA_STATUS = {
    "type": "status", "title": ("Online Application Status Enquiry", "신청 현황 온라인 조회", "網上查詢申請進度"),
    "intro": ("<p>Enter the application reference number and your date of birth.</p>", "<p>신청 접수번호와 생년월일을 입력하세요.</p>", "<p>請輸入申請的參考編號及你的出生日期。</p>"),
    "statusLabel": ("Application status", "신청 상태", "申請進度"),
    "fields": [F("ref", ("Application reference number", "신청 접수번호", "申請參考編號"), req=True, v="ref"), F("dob", ("Date of birth (YYYY-MM-DD)", "생년월일(YYYY-MM-DD)", "出生日期（YYYY-MM-DD）"), req=True, v="date", ph="YYYY-MM-DD")],
    "results": [
        [("Application received", "신청 접수", "已收到申請"), ("Your application has been received and is waiting to be processed.", "신청이 접수되어 처리 대기 중입니다.", "本處已收到你的申請，正等候處理。")],
        [("Under processing", "처리 중", "處理中"), ("Your application is being processed. You will be notified of the outcome.", "신청을 처리하고 있습니다. 결과는 별도로 통지됩니다.", "你的申請正在處理中，本處會通知你結果。")],
        [("Approved", "승인", "已獲批准"), ("Your application has been approved. Please follow the instructions in the notice sent to you.", "신청이 승인되었습니다. 발송된 통지서의 안내에 따라 주세요.", "你的申請已獲批准，請按本處所發通知內的指示辦理。")],
        [("Closed", "종결", "已結案"), ("Your application has been finalised. Records are kept for 1 month after closure.", "신청이 종결되었습니다. 종결 후 1개월간 기록이 보관됩니다.", "你的申請已處理完畢，紀錄在結案後保留1個月。")],
    ],
}

# ----------------------------------------------------------------------------- eTAX
def etax_login(link):
    return {
        "type": "login", "title": ("eTAX – Individual Tax Portal (ITP) Login", "eTAX – 개인 납세 포털(ITP) 로그인", "稅務易 – 個人稅務入門網站（ITP）登入"),
        "intro": ("<p>ITP is the gateway to the Inland Revenue Department's electronic services.</p>", "<p>ITP는 국세청(IRD) 전자서비스로 들어가는 관문입니다.</p>", "<p>ITP是通往稅務局電子服務的入口。</p>"),
        "fields": [F("acct", ("ITP Account Number / identity card number", "ITP 계정 번호 / 신분증 번호", "ITP帳戶號碼／身份證號碼"), req=True, sens=True), F("pass", ("ITP Password", "ITP 비밀번호", "ITP密碼"), "password", req=True, sens=True)],
        "links": [[("Open ITP Account", "ITP 계정 만들기", "開立ITP帳戶"), link("eservices/etax-register")], [("Forgot password", "비밀번호 찾기", "忘記密碼"), link("misc/itpforgot")]],
        "portalTitle": ("My ITP Account", "나의 ITP 계정", "我的ITP帳戶"),
        "welcome": ("Welcome, account", "환영합니다. 계정", "歡迎，帳戶"),
        "taxPos": ("Tax Position", "납세 현황", "稅務狀況"),
        "taxCols": [("Year of assessment", "과세연도", "課稅年度"), ("Tax payable", "납부할 세액", "應繳稅款"), ("Paid", "납부 완료", "已繳"), ("Balance", "잔액", "結餘")],
        "msgTitle": ("Messages", "메시지", "訊息"),
        "messages": [("e-Alert: the due date for filing the 2026/27 salaries tax return is approaching.", "e-알림: 2026/27 근로소득세 신고 마감일이 다가오고 있습니다.", "電子提示：2026/27年度薪俸稅報稅表的截止日期快將屆滿。"), ("Your notice of assessment is available in your electronic mailbox.", "납세고지서가 전자 우편함에 도착했습니다.", "你的評稅通知書已存放於電子信箱。")],
        "svcTitle": ("Services", "서비스", "服務"),
        "services": [[("File Tax Return", "세금 신고", "報稅"), link("misc/itpfile")], [("Pay Tax", "세금 납부", "繳稅"), link("eservices/tax-payment")], [("Calculate tax liability", "납부 세액 계산", "計算稅款"), link("residents/taxes/etax/taxcalc")], [("Know more about my Entitlement to Allowance", "공제·감면 자격 알아보기", "了解我享有的免稅額"), link("residents/taxes/etax/allowance")]],
    }


ETAX_REGISTER = {
    "type": "wizard", "prefix": "ITP", "title": ("Open eTAX ITP Account", "eTAX ITP 계정 만들기", "開立稅務易ITP帳戶"),
    "steps": [
        {"title": ("Identity", "본인 확인", "身份核對"), "fields": [
            F("name", ("Full name (in English)", "성명(영문)", "姓名（英文）"), req=True, v="enname"), F("idno", ("Baekhyeon Hwarang identity card number", "백현화랑 신분증 번호", "柏峴화랑身份證號碼"), req=True, v="bhid", ph="A123456(3)", sens=True),
            F("dob", ("Date of birth (YYYY-MM-DD)", "생년월일(YYYY-MM-DD)", "出生日期（YYYY-MM-DD）"), req=True, v="date", ph="YYYY-MM-DD")]},
        {"title": ("Contact", "연락처", "聯絡資料"), "fields": [F("email", ("Email address", "이메일 주소", "電郵地址"), "email", req=True, v="email", sens=True), F("mobile", ("Mobile phone number", "휴대전화 번호", "流動電話號碼"), "tel", req=True, v="tel", sens=True)]},
        {"title": ("Set Password", "비밀번호 설정", "設定密碼"), "fields": [F("pw", ("ITP Password", "ITP 비밀번호", "ITP密碼"), "password", req=True, v="pw", sens=True, h=("At least 8 characters with letters and numbers.", "영문과 숫자를 포함해 8자 이상.", "至少8個字元，並包含英文字母及數字。")), F("pw2", ("Confirm password", "비밀번호 확인", "確認密碼"), "password", req=True, v="match", of="pw", sens=True)]},
        {"title": ("Review", "확인", "核對"), "type": "review"},
        {"title": ("Account Opened", "계정 개설 완료", "帳戶已開立"), "type": "done"},
    ],
    "declare": F("declare", ("I declare that the information given is true and correct.", "기재한 정보가 사실이며 정확함을 선서합니다.", "本人聲明所填報的資料全部屬實及正確。"), "checkbox", req=True),
    "doneText": ("<strong>Your ITP Account has been opened.</strong> Your account number is shown below. You can now login to ITP.", "<strong>ITP 계정이 개설되었습니다.</strong> 계정 번호는 아래와 같습니다. 이제 ITP에 로그인할 수 있습니다.", "<strong>你的ITP帳戶已開立。</strong>帳戶號碼如下，你現可登入ITP。"),
    "doneRows": [{"n": "name", "l": ("Name", "성명", "姓名")}],
}

TAX_PAYMENT = {
    "type": "wizard", "prefix": "TX", "title": ("Pay Tax", "세금 납부", "繳稅"),
    "fee": {"amountField": "amount", "amountLabel": ("Tax payment", "세금 납부액", "繳稅金額")},
    "steps": [
        {"title": ("Payment Details", "납부 내용", "付款資料"), "fields": [
            F("taxtype", ("Type of tax", "세금 종류", "稅項"), "select", req=True, o=[["sal", ("Salaries Tax / Personal Assessment", "근로소득세 / 개인 과세", "薪俸稅／個人入息課稅")], ["prop", ("Property Tax", "재산세", "物業稅")], ["prof", ("Profits Tax", "법인이윤세", "利得稅")]]),
            F("fileno", ("Tax file / notice reference number", "세무 파일·고지서 참조번호", "稅務檔案／通知書參考編號"), req=True, v="ref"),
            F("amount", ("Amount to pay (BH$)", "납부 금액(BH$)", "繳款金額（BH$）"), req=True, v="num", im="decimal")]},
        {"title": ("Payment", "결제", "付款"), "type": "pay"},
        {"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"},
    ],
    "pay": PASSPORT["pay"],
    "doneText": ("<strong>Your payment has been received.</strong> Please print this acknowledgement for your records.", "<strong>납부가 접수되었습니다.</strong> 이 확인서를 인쇄해 보관하세요.", "<strong>本處已收到你的付款。</strong>請列印此確認頁作紀錄。"),
    "doneRows": [{"n": "fileno", "l": ("Tax file / notice reference number", "세무 파일·고지서 참조번호", "稅務檔案／通知書參考編號")}],
}


# ----------------------------------------------------------------------------- tax calculator
def _num(n, l, **kw):
    return F(n, l, v="num", im="decimal", **kw)


def _cnt(n, l, mx):
    return F(n, l, "select", o=[[str(k), str(k)] for k in range(0, mx + 1)])


TAXCALC = {
    "type": "taxcalc", "title": ("Tax Calculator – Salaries Tax and Personal Assessment", "세액 계산기 – 근로소득세 및 개인 과세", "稅款計算機 – 薪俸稅及個人入息課稅"),
    "intro": ("<p>Salaries Tax payable is calculated at progressive rates on your net chargeable income or at standard rate on your net income, whichever is lower. All amounts are in Baekhyeon Hwarang Dollars (BH$).</p>",
              "<p>근로소득세는 순과세소득에 누진세율을 적용한 금액과 순소득에 표준세율을 적용한 금액 중 낮은 쪽으로 산정합니다. 모든 금액은 백현화랑달러(BH$)입니다.</p>",
              "<p>薪俸稅按你的應課稅入息實額以累進稅率計算，或按入息淨額以標準稅率計算，以較低者為準。所有金額均以柏峴화랑元（BH$）計算。</p>"),
    "years": ["2026/27", "2025/26", "2024/25", "2023/24", "2022/23", "2021/22", "2020/21"],
    "params": {"bands": [[50000, 0.02], [50000, 0.06], [50000, 0.10], [50000, 0.14]], "top": 0.17, "stdCap": 5000000, "stdLow": 0.15, "stdHigh": 0.16,
               "basic": 132000, "married": 264000, "singleParent": 132000, "child": 130000, "par60": 50000, "par55": 25000, "sib": 37500, "disabled": 75000,
               "mpfMax": 18000, "rentMax": 100000, "loanMax": 100000, "elderMax": 100000, "eduMax": 100000, "redPct": 1.0, "redCap": 1500,
               "redByYear": {"2026/27": 1500, "2025/26": 1500, "2024/25": 3000, "2023/24": 3000, "2022/23": 6000, "2021/22": 10000, "2020/21": 10000}},
    "fields": [
        F("year", ("Year of assessment", "과세연도", "課稅年度"), "select", o=[[y, y] for y in ["2026/27", "2025/26", "2024/25", "2023/24", "2022/23", "2021/22", "2020/21"]]),
        F("marital", ("Marital status", "혼인 여부", "婚姻狀況"), "select", req=True, o=[["single", ("Single", "미혼", "未婚")], ["married", ("Married", "기혼", "已婚")], ["single_parent", ("Single parent", "한부모", "單親")]]),
        _num("income", ("Total income (BH$)", "총소득(BH$)", "總入息（BH$）"), req=True),
        _num("mpf", ("Mandatory provident fund contributions (BH$)", "강제적립기금 납입액(BH$)", "強制性供款（BH$）")),
        _num("rent", ("Domestic rent (BH$)", "주거 임차료(BH$)", "居所租金（BH$）")),
        _num("loan", ("Home loan interest (BH$)", "주택대출 이자(BH$)", "居所貸款利息（BH$）")),
        _num("elder", ("Elderly residential care expenses (BH$)", "노인 요양시설 비용(BH$)", "長者住宿照顧開支（BH$）")),
        _num("edu", ("Self-education expenses (BH$)", "자기계발 교육비(BH$)", "個人進修開支（BH$）")),
        _num("donation", ("Charitable donations (BH$)", "기부금(BH$)", "慈善捐款（BH$）")),
        _num("spIncome", ("Spouse's total income (BH$) – if married", "배우자 총소득(BH$) – 기혼인 경우", "配偶的總入息（BH$）– 如已婚")),
        _num("spMpf", ("Spouse's mandatory contributions (BH$)", "배우자 강제적립기금 납입액(BH$)", "配偶的強制性供款（BH$）")),
        _cnt("kids", ("Number of dependent children", "부양 자녀 수", "受養子女數目"), 9), _cnt("kidsNew", ("Children born during the year (additional allowance)", "해당 연도 출생 자녀 수(추가 공제)", "該年度出生的子女數目（額外免稅額）"), 4),
        _cnt("par60", ("Dependent parents / grandparents aged 60 or above", "부양 부모·조부모(만 60세 이상) 수", "受養的60歲或以上父母／祖父母數目"), 4),
        _cnt("par55", ("Dependent parents / grandparents aged 55 to 59", "부양 부모·조부모(만 55~59세) 수", "受養的55至59歲父母／祖父母數目"), 4),
        _cnt("sib", ("Dependent brothers / sisters", "부양 형제·자매 수", "受養兄弟姊妹數目"), 4), _cnt("dis", ("Dependants with disability", "장애 부양가족 수", "受養的殘疾人士數目"), 4),
        F("selfDis", ("Taxpayer has a disability", "납세자 본인 장애 여부", "納稅人是否殘疾"), "select", o=[["no", ("No", "아니요", "否")], ["yes", ("Yes", "예", "是")]]),
    ],
    "out": {
        "title": ("Estimated tax liability", "예상 납부 세액", "估計稅款"), "income": ("Total income", "총소득", "總入息"), "ded": ("Deductions", "공제액", "扣除額"),
        "net": ("Net income", "순소득", "入息淨額"), "allow": ("Allowances", "인적 공제", "免稅額"), "ncid": ("Net chargeable income", "순과세소득", "應課稅入息實額"),
        "prog": ("Tax at progressive rates", "누진세율 적용 세액", "按累進稅率計算的稅款"), "std": ("Tax at standard rate", "표준세율 적용 세액", "按標準稅率計算的稅款"),
        "red": ("Tax reduction", "세액 감면", "稅款寬減"), "tax": ("Tax payable (the lower amount)", "납부할 세액(낮은 쪽)", "應繳稅款（以較低者為準）"),
        "jointBetter": ("Joint assessment with your spouse would be to your advantage", "배우자와의 합산 과세가 더 유리합니다", "與配偶選擇合併評稅對你有利"), "jointWorse": ("Joint assessment with your spouse would not be to your advantage", "배우자와의 합산 과세는 유리하지 않습니다", "與配偶選擇合併評稅對你並不有利"),
        "note": ("The tax payable figure produced by the Tax Calculator is for your information only. Its correctness depends on whether you have entered the correct income figure, deductions, your marital status and the number of your dependants. The Inland Revenue Department accepts no liability whatsoever for any loss or damage which may be incurred by its use.",
                 "세액 계산기가 산출한 납부 세액은 참고용입니다. 정확성은 소득, 공제, 혼인 여부, 부양가족 수를 올바르게 입력했는지에 달려 있습니다. 국세청은 이 계산기 사용으로 발생할 수 있는 어떠한 손실이나 손해에 대해서도 책임지지 않습니다.",
                 "稅款計算機所得出的應繳稅款數字只供參考，其準確程度取決於你所輸入的入息、扣除額、婚姻狀況及受養人數目是否正確。稅務局對使用本計算機可能引致的任何損失或損害概不負責。"),
    },
}


# Re-arrange the passport wizard into the eight steps of the Immigration Department's service demo.
def _merge(a, b, title):
    out = dict(a)
    out["fields"] = list(a["fields"]) + list(b["fields"])
    out["title"] = title
    return out


_s = PASSPORT["steps"]   # 0 notes, 1 type, 2 particulars, 3 contact, 4 photo, 5 documents, 6 collection, 7 review, 8 pay, 9 done
_type = dict(_s[1])
_type["title"] = ("Application Type", "신청 유형", "申請類別")
_type["fields"] = [dict(f) for f in _type["fields"]]
for _f in _type["fields"]:
    if _f["n"] == "apptype":
        _f["o"] = [["first", ("First application", "최초 신청", "首次申請")], ["replace", ("Normal replacement due to expiry of the passport", "여권 만료에 따른 일반 교체", "因護照到期而正常換領")]]
PASSPORT["steps"] = [
    _type,
    _merge(_s[2], _s[3], ("Personal Particulars", "인적사항", "個人資料")),
    dict(_s[4], title=("Attach Photograph", "사진 첨부", "附加照片")),
    dict(_s[5], title=("Attach Supporting Document", "증빙서류 첨부", "附加證明文件")),
    dict(_s[6], title=("Collection Means", "수령 방법", "領取方式")),
    dict(_s[7], title=("Confirmation, Declaration and Submission", "확인·선서·제출", "確認、聲明及遞交")),
    dict(_s[8], title=("Online Payment", "온라인 결제", "網上付款")),
    dict(_s[9], title=("Acknowledgement", "접수 확인", "確認")),
]
