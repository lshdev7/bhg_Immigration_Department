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
    "errId": ("Please enter the identity card number in the format A123456(7): 1 or 2 letters, 6 digits and a check digit (0-9 or A).", "신분증 번호를 A123456(7) 형식으로 입력하세요. 영문 1~2자, 숫자 6자리, 확인 문자(0~9 또는 A)입니다.", "請按A123456(7)格式輸入身份證號碼：1至2個英文字母、6位數字及1個核對數字（0至9或A）。"),
    "errDate": ("Please enter a valid date (YYYYMMDD) that is not in the future.", "미래가 아닌 올바른 날짜(YYYYMMDD)를 입력하세요.", "請輸入有效而不是未來的日期（YYYYMMDD）。"),
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
    "errPhotoType": ("The file must be an image (e.g. JPEG or PNG).", "이미지 파일(JPEG, PNG 등)이어야 합니다.", "檔案必須為圖像（例如JPEG或PNG）。"),
    "errPhotoSize": ("The photograph is larger than 5MB.", "사진이 5MB를 초과합니다.", "照片超過5MB。"),
    "errPhotoDim": ("The image must be at least 1200 x 1600 pixels.", "이미지는 최소 1200 x 1600픽셀이어야 합니다.", "圖像大小至少須為1200 x 1600像素。"),
    "errPhotoRatio": ("The image must have a width-to-height ratio of 40:50.", "이미지의 가로:세로 비율은 40:50이어야 합니다.", "圖像的闊高比例必須為40:50。"),
    "applicant": ("Applicant", "신청인", "申請人"), "idno": ("Identity card number", "신분증 번호", "身份證號碼"),
    "dob": ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"),
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
    "bhPlace": ("Baekhyeon Hwarang", "백현화랑", "柏峴화랑"),
    "dlPassport": ("Download passport (PDF)", "여권 내려받기(PDF)", "下載護照（PDF）"),
    "dlIdcard": ("Download identity card (PDF)", "신분증 내려받기(PDF)", "下載身份證（PDF）"),
    "errMMYY": ("Please enter the month and year as MMYY (e.g. 0696).", "월·년을 MMYY 형식으로 입력하세요(예: 0696).", "請以MMYY格式輸入月份及年份（例如0696）。"),
    "errAge11": ("Please enter a valid date of birth. Applicants must be aged 11 or above.", "올바른 생년월일을 입력하세요. 만 11세 이상만 신청할 수 있습니다.", "請輸入有效的出生日期。申請人須年滿11歲。"),
    "cropTitle": ("Adjust your photograph", "사진 맞추기", "調整照片"),
    "cropHint": ("Drag the photograph to move it and use the slider (or mouse wheel) to zoom, so that your face fits the oval guide. It will be saved as a 40 mm x 50 mm photograph (1280 x 1600 pixels).",
                 "사진을 끌어서 옮기고 슬라이더(또는 마우스 휠)로 확대해 얼굴이 타원 안내선 안에 들어오게 맞추세요. 40mm x 50mm 사진(1280 x 1600픽셀)으로 저장됩니다.",
                 "拖動照片以移動位置，並以滑桿（或滑鼠滾輪）縮放，使面部位於橢圓輔助線內。照片會以40毫米 x 50毫米（1280 x 1600像素）儲存。"),
    "zoom": ("Zoom", "확대", "縮放"), "rotate": ("Rotate 90°", "90° 회전", "旋轉90°"),
    "cropApply": ("Use this photograph", "이 사진 사용", "使用此照片"), "cropCancel": ("Cancel", "취소", "取消"), "cropAgain": ("Adjust again", "다시 맞추기", "重新調整"),
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
            F("dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD"),
            F("pob", ("Place of birth (country / territory)", "출생지(국가·지역)", "出生地點（國家／地區）"), "country", req=True),
            F("idno", ("Baekhyeon Hwarang identity card number", "백현화랑 신분증 번호", "柏峴화랑身份證號碼"), req=True, v="bhid", ph="A123456(3)", sens=True, h=("Example format: A123456(3)", "형식 예: A123456(3)", "格式例子：A123456(3)")),
            F("marital", ("Marital status", "혼인 여부", "婚姻狀況"), "select", req=True, o=MARITAL),
        ]},
        {"title": ("Contact Details", "연락처", "聯絡資料"), "fields": [
            F("mobile", ("Mobile phone number (to receive SMS)", "휴대전화 번호(SMS 수신용)", "流動電話號碼（接收短訊）"), "tel", req=True, v="tel", sens=True),
            F("email", ("Email address", "이메일 주소", "電郵地址"), "email", req=True, v="email", sens=True),
            F("addr", ("Residential address", "거주지 주소", "住址"), "textarea", req=True, full=True),
        ]},
        {"title": ("Photograph", "사진", "照片"), "intro": ("<p>Upload a recent colour photograph in plain white background. After choosing the file you can move, zoom and rotate it to fit the 40:50 frame; it will be saved as a JPEG of 1280 x 1600 pixels. See the photograph requirements for details.</p>",
                   "<p>흰색 배경의 최근 컬러 사진을 올려 주세요. 파일을 고른 뒤 40:50 비율 틀에 맞게 옮기고 확대·회전할 수 있으며, 1280 x 1600픽셀 JPEG로 저장됩니다. 자세한 내용은 사진 규격을 참고하세요.</p>",
                   "<p>請上載背景為白色的彩色近照。選擇檔案後，你可移動、縮放及旋轉照片以配合40:50的框架，照片會以1280 x 1600像素的JPEG格式儲存。詳情請參閱照片規格。</p>"),
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
        "ext": [["ext", ("Extension of stay", "체류 연장", "延期逗留")], ["chg", ("Change of employment / sponsorship", "고용·보증 변경", "轉換僱主／擔保")], ["evisa", ("Payment and collection of “e-Visa”", "\"e-Visa\" 결제 및 수령", "繳費及領取「電子簽證」")]],
    }[kind]
    title = {"ext": ("Appointment Booking for Submission of Application", "신청서 제출 예약", "預約遞交申請"), "td": ("Appointment Booking for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件"),
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
    "fields": [F("ref", ("Application reference number", "신청 접수번호", "申請參考編號"), req=True, v="ref"), F("dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD")],
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
            F("dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD")]},
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


# ----------------------------------------------------------------------------- Smart identity card (online application)
IDCARD = {
    "type": "wizard", "prefix": "ID", "idcardPdf": True,
    "title": ("Online Application for Baekhyeon Hwarang Smart Identity Card", "백현화랑 스마트 신분증 온라인 신청", "網上申領柏峴화랑智能身份證"),
    "fee": {
        "base": [
            {"when": {"idtype": "lost"}, "l": ("Replacement of identity card (lost)", "신분증 재발급(분실)", "補領身份證（遺失）"), "amt": 370},
            {"when": {"idtype": "damaged"}, "l": ("Replacement of identity card (damaged / defaced)", "신분증 재발급(훼손·오손)", "補領身份證（損毀／污損）"), "amt": 370},
        ],
    },
    "steps": [
        {"title": ("Application Type", "신청 유형", "申請類別"), "fields": [
            F("idtype", ("Type of application", "신청 종류", "申請種類"), "radio", req=True, o=[
                ["first", ("First registration", "최초 등록", "首次登記")],
                ["lost", ("Replacement due to loss", "분실에 따른 재발급", "因遺失而補領")],
                ["damaged", ("Replacement due to damage / defacement", "훼손·오손에 따른 재발급", "因損毀／污損而補領")],
                ["change", ("Replacement due to change of particulars", "인적사항 변경에 따른 재발급", "因更改個人資料而換領")]]),
            F("oldid", ("Existing identity card number", "기존 신분증 번호", "現有身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True, showIf={"n": "idtype", "ne": "first"}),
            F("firstreg", ("Month and year of first registration (MMYY)", "최초 등록 월·년(MMYY)", "首次登記月份及年份（MMYY）"), req=True, v="mmyy", ph="MMYY", showIf={"n": "idtype", "ne": "first"}),
            F("status", ("Residence status", "거주 자격", "居留身份"), "radio", req=True, o=[
                ["A", ("Permanent resident with the right of abode", "거주권이 있는 영주권자", "擁有居留權的永久性居民")],
                ["R", ("Resident with the right to land", "입경권이 있는 주민", "擁有入境權的居民")],
                ["U", ("Non-permanent resident – no conditions of stay", "비영주 주민 – 체류 조건 없음", "非永久性居民 – 沒有逗留條件")],
                ["C", ("Non-permanent resident – stay limited by conditions", "비영주 주민 – 체류 조건 있음", "非永久性居民 – 逗留受條件限制")]]),
            F("kornat", ("Nationality", "국적", "國籍"), "radio", req=True, o=[["KOR", ("Korean", "대한민국", "大韓民國")], ["OTH", ("Other", "기타", "其他")]]),
        ]},
        {"title": ("Personal Particulars", "인적사항", "個人資料"), "fields": [
            F("surname", ("Surname (in English)", "성(영문)", "姓氏（英文）"), req=True, v="enname", ph="CHOI", rl=("Surname", "성", "姓氏")),
            F("given", ("Given names (in English)", "이름(영문)", "名字（英文）"), req=True, v="enname", ph="Yu Na", rl=("Given names", "이름", "名字")),
            F("local", ("Name in Chinese / Korean characters (if any)", "한글·한자 성명(있는 경우)", "中文／韓文姓名（如有）")),
            F("sex", ("Sex", "성별", "性別"), "select", req=True, o=SEX),
            F("dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="age11", ph="YYYYMMDD", h=("Applicants must be aged 11 or above.", "만 11세 이상만 신청할 수 있습니다.", "申請人須年滿11歲。")),
            F("pob", ("Place of birth (country / territory)", "출생지(국가·지역)", "出生地點（國家／地區）"), "country", req=True),
            F("chgbirth", ("Has your date or place of birth been changed since first registration?", "최초 등록 이후 생년월일이나 출생지가 변경되었습니까?", "首次登記後，你的出生日期或出生地點有否更改？"), "radio", req=True, o=[["Y", ("Yes", "예", "有")], ["N", ("No", "아니요", "沒有")]]),
            F("chgname", ("Has your name been changed, or a Chinese / Korean name added, since first registration?", "최초 등록 이후 이름이 바뀌었거나 한글·한자 이름이 추가되었습니까?", "首次登記後，你的姓名有否更改或加入中文／韓文姓名？"), "radio", req=True, o=[["Y", ("Yes", "예", "有")], ["N", ("No", "아니요", "沒有")]]),
            F("dobproof", ("Will you produce a birth certificate or passport to confirm your date of birth?", "생년월일 확인을 위해 출생증명서나 여권을 제출합니까?", "你會否出示出生證明書或護照以確認出生日期？"), "radio", req=True, o=[["Y", ("Yes", "예", "會")], ["N", ("No", "아니요", "不會")]]),
            F("mobile", ("Mobile phone number", "휴대전화 번호", "流動電話號碼"), "tel", req=True, v="tel", sens=True),
            F("email", ("Email address", "이메일 주소", "電郵地址"), "email", req=True, v="email", sens=True),
            F("addr", ("Residential address", "거주지 주소", "住址"), "textarea", req=True, full=True),
        ]},
        {"title": ("Attach Photograph", "사진 첨부", "附加照片"),
         "intro": ("<p>Upload a recent colour photograph in plain white background. After choosing the file you can move, zoom and rotate it to fit the frame.</p>",
                   "<p>흰색 배경의 최근 컬러 사진을 올려 주세요. 파일을 고른 뒤 틀에 맞게 옮기고 확대·회전할 수 있습니다.</p>",
                   "<p>請上載背景為白色的彩色近照。選擇檔案後，你可移動、縮放及旋轉照片以配合框架。</p>"),
         "fields": [F("photo", ("Photograph", "사진", "照片"), "photo", req=True, full=True)]},
        {"title": ("Collection Means", "수령 방법", "領取方式"), "fields": [F("office", ("Office for collection", "수령 사무소", "領取辦事處"), "select", req=True, o=OFFICES)]},
        {"title": ("Confirmation, Declaration and Submission", "확인·선서·제출", "確認、聲明及遞交"), "type": "review"},
        {"title": ("Online Payment", "온라인 결제", "網上付款"), "type": "pay", "showIf": {"n": "idtype", "in": ["lost", "damaged"]}},
        {"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"},
    ],
    "declare": F("declare", ("I declare that the information given in this application is true and correct.", "이 신청서에 기재한 정보가 사실이며 정확함을 선서합니다.", "本人聲明本申請所填報的資料全部屬實及正確。"), "checkbox", req=True),
    "pay": PASSPORT["pay"],
    "doneText": ("<strong>Your application has been submitted successfully.</strong> Please collect your new identity card at the selected office with the acknowledgement.",
                 "<strong>신청이 정상적으로 제출되었습니다.</strong> 접수 확인서를 지참하고 선택한 사무소에서 새 신분증을 수령하세요.",
                 "<strong>你的申請已成功遞交。</strong>請攜同確認通知到所選定的辦事處領取新身份證。"),
    "doneRows": [{"n": "surname", "l": ("Surname", "성", "姓氏")}, {"n": "given", "l": ("Given names", "이름", "名字")}, {"n": "office", "l": ("Office for collection", "수령 사무소", "領取辦事處"), "o": OFFICES}],
}


# ============================================================================= Visas / Entry Permits e-services (built from data_visa)
import data_visa as V

L.update({
    "dependant": ("Dependant", "부양가족", "受養人"),
    "dlEvisa": ("Download “e-Visa” (PDF)", "\"e-Visa\" 내려받기(PDF)", "下載「電子簽證」（PDF）"),
    "errFdate": ("Please enter a valid future date (YYYYMMDD).", "오늘 이후의 올바른 날짜(YYYYMMDD)를 입력하세요.", "請輸入有效的未來日期（YYYYMMDD）。"),
    "errAnyDate": ("Please enter a valid date (YYYYMMDD).", "올바른 날짜(YYYYMMDD)를 입력하세요.", "請輸入有效的日期（YYYYMMDD）。"),
    "errEvref": ("Please enter the application reference number shown on the acknowledgement or “e-Visa” (e.g. TTEN-1234567-26(5)).", "접수 확인서나 \"e-Visa\"에 적힌 신청 접수번호를 입력하세요(예: TTEN-1234567-26(5)).", "請輸入確認通知或「電子簽證」上的申請參考編號（例如TTEN-1234567-26(5)）。"),
    "evRef": ("Application reference number", "신청 접수번호", "申請參考編號"),
    "evDob": ("Date of birth of the applicant (YYYYMMDD)", "신청인의 생년월일(YYYYMMDD)", "申請人的出生日期（YYYYMMDD）"),
    "evNotFound": ("No “e-Visa” record matches the information entered. Please check the application reference number and the date of birth.", "입력한 정보와 일치하는 \"e-Visa\" 기록이 없습니다. 신청 접수번호와 생년월일을 확인하세요.", "找不到與所輸入資料相符的「電子簽證」紀錄。請檢查申請參考編號及出生日期。"),
    "evName": ("Name", "성명", "姓名"), "evType": ("Type", "종류", "類別"), "evScheme": ("Scheme / arrangement", "제도·절차", "計劃／安排"),
    "evIssue": ("Date of issue", "발급일", "簽發日期"), "evValid": ("Valid for presentation on or before", "제시 유효기한", "須於此日期或之前使用"),
    "evStay": ("Limit of stay", "체류 기한", "逗留期限"), "evStatus": ("Status", "상태", "狀況"), "evOk": ("Valid", "유효", "有效"),
    "evEntry": ("Notification Slip for Entry Visa / Permit", "입경 비자·허가 통지서", "入境簽證／進入許可通知書"),
    "evExt": ("Notification Slip for Conditions of Stay", "체류 조건 통지서", "逗留條件通知書"),
    "evPaid": ("The fee for this “e-Visa” has been paid. You may download the “e-Visa” now.", "이 \"e-Visa\"의 수수료는 이미 납부되었습니다. 지금 \"e-Visa\"를 내려받을 수 있습니다.", "此「電子簽證」的費用已經繳付。你現可下載「電子簽證」。"),
    "evNoFee": ("No payment is required for this application.", "이 신청은 납부할 수수료가 없습니다.", "此申請無須付款。"),
    "evPar": ("Notification Slip for Pre-arrival Registration", "사전 입경 등록 통지서", "預辦入境登記通知書"),
    "evFdh2": ("Foreign Domestic Helper – Notification Slip for Extension of Stay and Entry Visa", "외국인 가사도우미 – 체류 연장 및 입경 비자 통지서", "外籍家庭傭工 – 延期逗留及入境簽證通知書"),
    "evOver": ("The validity period or the limit of stay of this “e-Visa” has expired. It cannot be downloaded.", "이 \"e-Visa\"는 유효기한이나 체류 기한이 지나 내려받을 수 없습니다.", "此「電子簽證」的有效期或逗留期限已過，不能下載。"),
    "evExpired": ("Expired", "기한 만료", "已過期"), "evRe": ("Re-entry employment till", "재입경 후 취업 기한", "再入境僱傭工作至"), "evEmp": ("Employer / institution", "고용주·기관", "僱主／院校"),
    "evMake": ("The “e-Visa” is being prepared…", "\"e-Visa\"를 만드는 중입니다…", "正在準備「電子簽證」……"),
    "evMakeErr": ("The “e-Visa” could not be prepared. Please try again later.", "\"e-Visa\"를 만들지 못했습니다. 잠시 후 다시 시도하세요.", "未能準備「電子簽證」。請稍後再試。"),
    "evM1": ("Scan the QR code", "QR 코드 스캔", "掃描二維碼"), "evM2": ("Import the “e-Visa” file", "\"e-Visa\" 파일 불러오기", "匯入「電子簽證」檔案"), "evM3": ("Input the “e-Visa” information", "\"e-Visa\" 정보 입력", "輸入「電子簽證」資料"),
    "evM1p": ("Point the camera at the encrypted QR code on the “e-Visa”.", "\"e-Visa\"에 있는 암호화된 QR 코드를 카메라에 비추세요.", "請把鏡頭對準「電子簽證」上的加密二維碼。"),
    "evM2p": ("Choose the “e-Visa” file (PDF, JPEG, GIF or PNG).", "\"e-Visa\" 파일(PDF, JPEG, GIF, PNG)을 선택하세요.", "請選擇「電子簽證」檔案（PDF、JPEG、GIF或PNG格式）。"),
    "evCamOn": ("Start the camera", "카메라 켜기", "開啟鏡頭"), "evCamErr": ("The camera cannot be used. Please import the “e-Visa” file or input the information.", "카메라를 사용할 수 없습니다. 파일을 불러오거나 정보를 입력하세요.", "未能使用鏡頭。請匯入「電子簽證」檔案或輸入資料。"),
    "evQrNone": ("No QR code was found in the file.", "파일에서 QR 코드를 찾지 못했습니다.", "在檔案中找不到二維碼。"),
    "evQrBad": ("This QR code was not issued by the Immigration Department.", "출입경사무처가 발급한 QR 코드가 아닙니다.", "此二維碼並非由入境事務處發出。"),
    "evQrOk": ("The QR code is authentic. The “e-Visa” was issued by the Immigration Department.", "진본 QR 코드입니다. 출입경사무처가 발급한 \"e-Visa\"입니다.", "二維碼核實無誤，此「電子簽證」由入境事務處發出。"),
    "search": ("Search", "조회", "查詢"),
    "months": ("months", "개월", "個月"), "days": ("days", "일", "日"),
})

_TD_TYPES = [["passport", ("Passport", "여권", "護照")], ["other", ("Other travel document", "기타 여행증명서", "其他旅行證件")]]
_REL = [["spouse", ("Spouse / partner", "배우자·동반자", "配偶／伴侶")], ["child", ("Child under 18", "만 18세 미만 자녀", "18歲以下子女")]]


def _personal(ext):
    out = [
        F("surname", ("Surname (in English)", "성(영문)", "姓氏（英文）"), req=True, v="enname", ph="CHOI", rl=("Surname", "성", "姓氏")),
        F("given", ("Given names (in English)", "이름(영문)", "名字（英文）"), req=True, v="enname", ph="Yu Na", rl=("Given names", "이름", "名字")),
        F("local", ("Name in Chinese / Korean characters (if any)", "한글·한자 성명(있는 경우)", "中文／韓文姓名（如有）")),
        F("sex", ("Sex", "성별", "性別"), "select", req=True, o=SEX),
        F("dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD"),
        F("pob", ("Place of birth (country / territory)", "출생지(국가·지역)", "出生地點（國家／地區）"), "country", req=True),
        F("nat", ("Nationality (country / territory)", "국적(국가·지역)", "國籍（國家／地區）"), "country", req=True),
        F("marital", ("Marital status", "혼인 여부", "婚姻狀況"), "select", req=True, o=MARITAL),
        F("tdtype", ("Type of travel document", "여행증명서 종류", "旅行證件類別"), "select", req=True, o=_TD_TYPES),
        F("tdno", ("Travel document number", "여행증명서 번호", "旅行證件號碼"), req=True, sens=True),
        F("tdexp", ("Date of expiry of travel document (YYYYMMDD)", "여행증명서 만료일(YYYYMMDD)", "旅行證件屆滿日期（YYYYMMDD）"), req=True, v="fdate", ph="YYYYMMDD"),
        F("mobile", ("Mobile phone number", "휴대전화 번호", "流動電話號碼"), "tel", req=True, v="tel", sens=True),
        F("email", ("Email address", "이메일 주소", "電郵地址"), "email", req=True, v="email", sens=True),
        F("addr", ("Residential address", "거주지 주소", "住址"), "textarea", req=True, full=True),
    ]
    return out


def _dep_fields():
    return [F("d{k}_surname", ("Surname (in English)", "성(영문)", "姓氏（英文）"), req=True, v="enname"),
            F("d{k}_given", ("Given names (in English)", "이름(영문)", "名字（英文）"), req=True, v="enname"),
            F("d{k}_sex", ("Sex", "성별", "性別"), "select", req=True, o=SEX),
            F("d{k}_dob", ("Date of birth (YYYYMMDD)", "생년월일(YYYYMMDD)", "出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD"),
            F("d{k}_rel", ("Relationship with the applicant", "신청인과의 관계", "與申請人的關係"), "select", req=True, o=_REL),
            F("d{k}_nat", ("Nationality", "국적", "國籍"), "country", req=True),
            F("d{k}_tdno", ("Travel document number", "여행증명서 번호", "旅行證件號碼"), req=True, sens=True),
            F("d{k}_photo", ("Photograph", "사진", "照片"), "file", req=True, full=True)]


def _fee(s, ext):
    lines = []
    if s["spec"]:
        lines.append({"when": {}, "l": ("Application fee", "신청 수수료", "申請費"), "amt": 600})
        long_ = (s.get("months") or 0) > 6 or (s.get("days") or 0) > 180
        lines.append({"when": {}, "l": ("Visa issuance fee", "비자 발급 수수료", "簽證簽發費"), "amt": 1300 if long_ else 600})
    elif s["k"] == "apec":
        lines.append({"when": {}, "l": ("Card fee", "카드 발급 수수료", "旅遊證費用"), "amt": 440})
    elif s["k"] in ("pri", "prt"):
        return None
    else:
        lines.append({"when": {}, "l": (("Extension of stay fee", "체류 연장 수수료", "延期逗留費") if ext else ("Visa issuance fee", "비자 발급 수수료", "簽證簽發費")), "amt": 230})
    fee = {"base": [], "extra": lines}
    if s["deps"]:
        fee["mult"] = "deps"
    return fee


def _ref_code(s, ext):
    letters = "".join(c for c in s["abbr"].upper() if c.isalpha())[:2] or s["k"][:2].upper()
    return letters + ("XR" if ext else "EN")


def visa_service(key):
    ext = key.startswith("ext-")
    s = V.SCHEME[key.split("-", 1)[1]]
    title = V.GOVT["extT" if ext else "entryT"]
    if ext and s.get("fdhsub"):
        title = V.GOVT["fdhExtT"]
    title = tuple(x.replace("{s}", y) for x, y in zip(title, s["t"]))
    if not ext and s["entry"] in V.GOV_TITLE:
        title = V.GOV_TITLE[s["entry"]]
    docs = s["ext_docs"] if ext else s["docs"]
    intro_p = (s["ext_intro"] or s["intro"]) if ext else s["intro"]
    lis = lambda i: "".join("<li>%s</li>" % d[i] for d in docs)
    notes = tuple("<p>%s</p><p><strong>%s</strong></p><ul>%s</ul><p>%s</p>" % (intro_p[0][i], V.H["docs"][i], lis(i), V.GOVT["fmtP"][i]) for i in range(3))
    info = [F("where", ("Where are you now?", "현재 위치", "你現時身在何處？"), "radio", req=True, o=[["in", ("In Baekhyeon Hwarang", "백현화랑 안", "在柏峴화랑")], ["out", ("Outside Baekhyeon Hwarang", "백현화랑 밖", "在柏峴화랑以外地區")]])]
    if ext:
        info = [F("idno", ("Baekhyeon Hwarang identity card number", "백현화랑 신분증 번호", "柏峴화랑身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
                F("lse", ("Expiry date of current limit of stay (YYYYMMDD)", "현재 체류 기한 만료일(YYYYMMDD)", "現時逗留期限屆滿日期（YYYYMMDD）"), req=True, v="fdate", ph="YYYYMMDD")]
    if s["deps"]:
        info.append(F("deps", ("Number of accompanying dependants applying together (group submission)", "함께 신청하는 동반 부양가족 수(그룹 제출)", "一併申請的隨行受養人數目（以組別方式遞交）"), "select", req=True, o=[[str(n), str(n)] for n in range(0, 9)], h=("Maximum nine applications in each group (including the principal applicant).", "그룹당 주 신청인을 포함해 최대 9건입니다.", "每組最多九宗申請（包括主申請人）。")))
    uploads = [F("photo", V.D_PHOTO, "photo", req=True, full=True)]
    n = 0
    for d in docs:
        if d is V.D_PHOTO:
            continue
        n += 1
        uploads.append(F("doc%d" % n, d, "file", req=V.mandatory(d), full=True))
    steps = [
        {"title": ("Important Notes", "유의사항", "注意事項"), "intro": notes,
         "fields": [F("agree", ("I have read and understood the above notes and prepared the required documents.", "위 유의사항을 읽고 이해했으며 필요한 서류를 준비했습니다.", "我已閱讀並明白上述注意事項，並已準備所需文件。"), "checkbox", req=True, full=True)]},
        {"title": ("Application Information", "신청 정보", "申請資料"), "fields": info},
        {"title": ("Personal Particulars of Applicant", "신청인 인적사항", "申請人個人資料"), "fields": _personal(ext)},
    ]
    if s["fields"]:
        steps.append({"title": (("Details of Application", "신청 세부 사항", "申請詳情")), "fields": s["fields"]})
    if s["deps"]:
        steps.append({"title": ("Particulars of Accompanying Dependants", "동반 부양가족 인적사항", "隨行受養人資料"), "gen": "deps", "showIf": {"n": "deps", "pos": True}, "fields": []})
    steps.append({"title": ("Upload Documents", "서류 업로드", "上載文件"), "intro": (V.GOVT["fmtP"][0], V.GOVT["fmtP"][1], V.GOVT["fmtP"][2]), "fields": uploads})
    steps.append({"title": ("Confirmation, Declaration and Submission", "확인·선서·제출", "確認、聲明及遞交"), "type": "review"})
    fee = _fee(s, ext)
    if fee:
        steps.append({"title": ("Online Payment", "온라인 결제", "網上付款"), "type": "pay"})
    steps.append({"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"})
    emp = None
    for f in s["fields"]:
        if f["n"] in ("employer", "school", "trainer", "emname", "bizname", "company", "sname"):
            emp = f["n"]
            break
    cfg = {
        "type": "wizard", "prefix": "EV", "refCode": _ref_code(s, ext), "title": title, "steps": steps, "depFields": _dep_fields(),
        "declare": F("declare", ("I declare that the information given in this application, including that of my accompanying dependants, is true, complete and correct, and that I understand that making false statements to an immigration officer is an offence.", "이 신청서(동반 부양가족 정보 포함)에 기재한 정보가 사실이고 완전하며 정확함을 선서하며, 출입경 공무원에게 허위 진술을 하는 것이 범죄임을 이해합니다.", "本人聲明本申請（包括隨行受養人的資料）所填報的資料全部屬實、完整及正確，並明白向入境事務主任作出虛假陳述即屬違法。"), "checkbox", req=True),
        "pay": PASSPORT["pay"],
        "doneText": ("<strong>Your application has been submitted and approved.</strong> The “e-Visa” has been issued. Please download and keep it, and present it with your valid travel document upon arrival clearance.",
                     "<strong>신청이 제출되어 승인되었습니다.</strong> \"e-Visa\"가 발급되었습니다. 내려받아 보관하고, 입경 심사 때 유효한 여행증명서와 함께 제시하세요.",
                     "<strong>你的申請已遞交並獲批准。</strong>「電子簽證」已經發出。請下載並妥為保存，並在辦理入境檢查時連同有效旅行證件一併出示。") if s["evisa"] else
                    ("<strong>Your application has been submitted successfully.</strong> You will be notified of the result by email.", "<strong>신청이 정상적으로 제출되었습니다.</strong> 결과는 이메일로 알려 드립니다.", "<strong>你的申請已成功遞交。</strong>本處會以電郵通知你申請結果。"),
        "doneNote": ("You may re-download the “e-Visa” at any time through the Download “e-Visa” service with the application reference number and your date of birth.", "신청 접수번호와 생년월일로 \"e-Visa\" 내려받기 서비스에서 언제든 \"e-Visa\"를 다시 받을 수 있습니다.", "你可隨時憑申請參考編號及出生日期，透過「下載電子簽證」服務重新下載「電子簽證」。") if s["evisa"] else None,
        "doneRows": [{"n": "surname", "l": ("Surname", "성", "姓氏")}, {"n": "given", "l": ("Given names", "이름", "名字")}],
    }
    if fee:
        cfg["fee"] = fee
    if s["evisa"]:
        cfg["evisa"] = {"k": s["k"], "mode": "ext" if ext else "entry", "zh": s["t"][2], "en": s["t"][0], "slip": list(s["slip"]), "months": s.get("months") or 0,
                        "days": s.get("days") or 0, "multi": s["multi"], "emp": emp, "employ": s["slip"][1] in ("EMPLOYMENT", "IMPORTED LABOUR", "FOREIGN DOMESTIC HELPER", "TECHNICAL PROFESSIONALS STREAM")}
    return cfg


def _lookup(mode, title):
    return {"type": "evisa", "mode": mode, "title": title,
            "intro": ("Please enter the application reference number and the date of birth of the applicant.", "신청 접수번호와 신청인의 생년월일을 입력하세요.", "請輸入申請參考編號及申請人的出生日期。"),
            "fields": [F("ref", ("Application reference number", "신청 접수번호", "申請參考編號"), req=True, v="evref", ph="TTEN-1234567-26(5)"),
                       F("dob", ("Date of birth of the applicant (YYYYMMDD)", "신청인의 생년월일(YYYYMMDD)", "申請人的出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD")]}


def _simple(title, fields, done, fee=None, prefix="VS"):
    steps = [{"title": ("Application Details", "신청 내용", "申請資料"), "fields": fields},
             {"title": ("Confirmation and Declaration", "확인 및 선서", "確認及聲明"), "type": "review"}]
    if fee:
        steps.append({"title": ("Online Payment", "온라인 결제", "網上付款"), "type": "pay"})
    steps.append({"title": ("Acknowledgement", "접수 확인", "確認"), "type": "done"})
    cfg = {"type": "wizard", "prefix": prefix, "title": title, "steps": steps, "pay": PASSPORT["pay"], "doneText": done,
           "declare": F("declare", ("I declare that the information given is true and correct.", "기재한 정보가 사실이며 정확함을 선서합니다.", "本人聲明所填報的資料全部屬實及正確。"), "checkbox", req=True),
           "doneRows": []}
    if fee:
        cfg["fee"] = {"base": [], "extra": [fee]}
    return cfg


_DONE = ("<strong>Your submission has been received.</strong> The Immigration Department will process it and contact you if necessary.", "<strong>제출이 접수되었습니다.</strong> 출입경사무처가 처리하고 필요하면 연락드립니다.", "<strong>本處已收到你的遞交。</strong>入境事務處會進行處理，並在有需要時與你聯絡。")
_ID = F("idno", ("Baekhyeon Hwarang identity card number", "백현화랑 신분증 번호", "柏峴화랑身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True)


def common_service(key):
    title = [c[2] for c in V.COMMON if c[0] == key][0]
    if key in ("evisa-payment", "evisa-download", "evisa-enquiry"):
        return _lookup(key.split("-")[1], title)
    if key == "extension-booking":
        b = booking("ext")
        b["title"] = title
        return b
    if key == "supplementary-documents":
        return _simple(title, [F("ref", ("Application reference number", "신청 접수번호", "申請參考編號"), req=True, v="evref", ph="TTEN-1234567-26(5)"),
                               F("dob", ("Date of birth of the applicant (YYYYMMDD)", "신청인의 생년월일(YYYYMMDD)", "申請人的出生日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD"),
                               F("letter", ("Reference number on the notification letter", "통지서 번호", "通知信上的參考編號"), req=True),
                               F("s1", ("Supplementary document 1", "추가 서류 1", "補充文件1"), "file", req=True, full=True),
                               F("s2", ("Supplementary document 2 (optional)", "추가 서류 2(선택)", "補充文件2（可選）"), "file", full=True),
                               F("s3", ("Supplementary document 3 (optional)", "추가 서류 3(선택)", "補充文件3（可選）"), "file", full=True)], _DONE, prefix="SD")
    if key == "change-sponsorship":
        return _simple(title, [_ID, F("ctype", ("Type of change", "변경 종류", "轉換類別"), "radio", req=True, o=[["emp", ("Change of employment", "고용 변경", "轉換僱主")], ["inv", ("Change of investment", "투자 변경", "更改投資")], ["edu", ("Change of educational institution", "교육기관 변경", "轉換教育院校")]]),
                               F("neworg", ("Name of new employer / business / institution", "새 고용주·사업체·교육기관 이름", "新僱主／業務／院校名稱"), req=True, full=True),
                               F("post", ("Post / programme", "직위·과정", "職位／課程"), req=True), F("salary", ("Monthly salary (BH$)", "월 급여(BH$)", "每月薪金（柏峴화랑元）"), v="num", im="numeric", req=True, showIf={"n": "ctype", "eq": "emp"}),
                               F("cstart", ("Intended commencement date (YYYYMMDD)", "시작 예정일(YYYYMMDD)", "預計開始日期（YYYYMMDD）"), req=True, v="anydate", ph="YYYYMMDD"),
                               F("cdoc", ("Employment contract / admission letter / business proof", "고용계약서·입학허가서·사업 증빙", "僱傭合約／取錄通知書／業務證明"), "file", req=True, full=True)], _DONE,
                       fee={"when": {}, "l": ("Change of condition of stay fee", "체류 조건 변경 수수료", "更改逗留條件費"), "amt": 230}, prefix="CS")
    if key == "fdh-termination":
        return _simple(title, [F("by", ("Notification made by", "통보자", "通知人"), "radio", req=True, o=[["employer", ("Employer", "고용주", "僱主")], ["helper", ("Foreign domestic helper", "외국인 가사도우미", "外籍家庭傭工")]]),
                               F("emname", ("Name of employer", "고용주 성명", "僱主姓名"), req=True), F("emid", ("Employer’s identity card number", "고용주 신분증 번호", "僱主身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
                               F("hname", ("Name of helper", "가사도우미 성명", "傭工姓名"), req=True), F("hid", ("Helper’s identity card number", "가사도우미 신분증 번호", "傭工身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
                               F("tdate", ("Date of termination (YYYYMMDD)", "해지일(YYYYMMDD)", "終止日期（YYYYMMDD）"), req=True, v="date", ph="YYYYMMDD"),
                               F("reason", ("Reason for termination", "해지 사유", "終止原因"), "textarea", req=True, full=True)], _DONE, prefix="FT")
    if key == "id407g":
        return _simple(title, [F("emname", ("Name of employer", "고용주 성명", "僱主姓名"), req=True), F("emid", ("Employer’s identity card number", "고용주 신분증 번호", "僱主身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
                               F("hname", ("Name of helper", "가사도우미 성명", "傭工姓名"), req=True), F("flat", ("Size of flat (square metres)", "주택 면적(㎡)", "住所面積（平方米）"), req=True, v="num", im="numeric"),
                               F("room", ("Accommodation arrangement for the helper", "가사도우미 숙소 형태", "為傭工提供的住宿安排"), "select", req=True, o=[["own", ("Separate room", "독립된 방", "獨立房間")], ["share", ("Sharing a room with a child", "아동과 방 공유", "與兒童同房")], ["other", ("Other arrangement", "기타", "其他安排")]]),
                               F("duties", ("Revised domestic duties", "변경된 가사 업무", "經修訂的家務"), "textarea", req=True, full=True),
                               F("g", ("Signed revised Schedule (ID 407G)", "서명한 변경 명세서(ID 407G)", "已簽署的經修訂安排表（ID 407G）"), "file", req=True, full=True)], _DONE, prefix="AG")
    raise KeyError(key)
