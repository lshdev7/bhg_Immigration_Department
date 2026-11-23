# -*- coding: utf-8 -*-
"""Immigration Department of the Baekhyeon Hwarang Special Administrative Region - site content.
Tuples are (English, Korean, Traditional Chinese); Simplified Chinese is derived at build time."""

GOV_BASE = "https://lshdev7.github.io/BHG/"        # GovBHG one-stop portal

UI = {
    "dept": ("Immigration Department", "출입경사무처", "入境事務處"),
    "govline": ("The Government of the Baekhyeon Hwarang Special Administrative Region", "백현화랑 특별행정구 정부", "柏峴화랑特別行政區政府"),
    "other_lang": ("Other Languages", "다른 언어", "其他語言"),
    "text_size": ("Text Size", "글자 크기", "字體大小"),
    "search_ph": ("Enter search keyword(s)", "검색어를 입력하세요", "輸入搜尋關鍵字"),
    "home": ("Home", "홈", "首頁"),
    "skip": ("Skip to main content", "본문 바로가기", "跳至主要內容"),
    "faq_tab": ("FAQ", "자주 묻는 질문", "常見問題"),
    "enq_tab": ("Enquiry", "문의", "查詢"),
    "expand_all": ("Expand All", "모두 펼치기", "全部展開"),
    "collapse_all": ("Collapse All", "모두 접기", "全部收合"),
    "stub": ("Information on this topic is being prepared.", "이 주제의 정보는 준비 중입니다.", "此主題的資料現正準備中。"),
    "related": ("Related topics", "관련 주제", "相關主題"),
    "govhk": ("About GovBHG", "정부포털 BHG 소개", "關於BHG政府一站通"),
    "copyright": ("Copyright Notice", "저작권 안내", "版權公告"),
    "privacy": ("Privacy Policy", "개인정보 처리방침", "私隱政策"),
    "disclaimer": ("Disclaimer", "면책 고지", "免責聲明"),
    "exit": ("Exit", "나가기", "離開"),
    "hq": ("Immigration Headquarters", "출입경사무처 본부", "入境事務處總部"),
    "hq_addr": ("Baekhyeon Maeul Complex 3, Baekhyeon Hwarang Special Administrative Region", "백현화랑 특별행정구 백현마을 3단지", "柏峴화랑特別行政區柏峴마을3社區"),
    "addr_link": ("Address and Working Hours of Offices", "사무소 주소 및 근무 시간", "辦事處地址及辦公時間"),
    "enq_form": ("Online Enquiry Form", "온라인 문의 양식", "網上查詢表格"),
    "follow": ("Follow Us", "소셜 미디어", "追蹤我們"),
    "last_rev": ("Last revision date: ", "최종 수정일: ", "修訂日期："),
    "rev_val": ("November 2026", "2026년 11월", "2026年11月"),
}

NAV = [  # slug, title
    ("about-us", ("About Us", "출입경사무처 소개", "關於我們")),
    ("services", ("Our Services", "서비스 안내", "服務")),
    ("online-services", ("Online Services", "온라인 서비스", "網上服務")),
    ("forms", ("Forms", "서식", "表格")),
    ("publications", ("Publications & Press Releases", "간행물·보도자료", "刊物及新聞公報")),
    ("useful-information", ("Useful Information & Statistics", "유용한 정보·통계", "實用資料及統計數字")),
    ("contact", ("Contact Us", "연락처", "聯絡我們")),
]

HERO = ("Serving Baekhyeon Hwarang with Integrity and Efficiency", "성실하고 효율적으로 백현화랑에 봉사합니다", "以誠信高效服務柏峴화랑")
HERO_SUB = ("Visas · Identity Cards · Travel Documents · Right of Abode", "비자 · 신분증 · 여행증명서 · 거주권", "簽證 · 身份證 · 旅行證件 · 居留權")

SERVICES = [  # slug, title, icon id
    ("visas", ("Visas / Entry Permits", "비자·입경허가", "簽證／進入許可證"), "visa"),
    ("identity-cards", ("Identity Cards", "신분증", "身份證"), "idcard"),
    ("right-of-abode", ("Right of Abode", "거주권", "居留權"), "abode"),
    ("travel-documents", ("Travel Documents", "여행증명서", "旅行證件"), "passport"),
    ("nationality", ("Korean Nationality", "대한민국 국적", "大韓民國國籍"), "flag"),
    ("births-deaths", ("Births and Deaths Registration", "출생·사망 등록", "出生及死亡登記"), "baby"),
    ("marriage", ("Marriage Registration", "혼인 등록", "婚姻登記"), "rings"),
    ("clearance", ("Immigration Clearance", "출입경 심사", "入境檢查"), "gate"),
    ("assistance", ("Travel Assistance", "여행 지원", "旅遊支援"), "help"),
    ("severe-weather", ("Severe Weather Arrangement", "악천후 시 운영 안내", "惡劣天氣下的安排"), "cloud"),
]

TD_PAGES = [  # path under services/travel-documents/, title
    ("apply-passport", ("Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照")),
    ("docid", ("Application for Document of Identity for Visa Purposes", "비자용 신분증명서 신청", "申請簽證身份書")),
    ("reentry", ("Application for Re-entry Permit", "재입경 허가증 신청", "申請回港證")),
    ("seaman", ("Application for Seaman's Identity Book", "선원 신분증 신청", "申請海員身份證")),
    ("photo", ("Photograph Requirements for Travel Document", "여행증명서 사진 규격", "旅行證件的照片規格")),
    ("fees", ("Fee Tables", "수수료표", "收費表")),
    ("kiosk", ("Collection via Passport Collection Kiosk / Personal Documentation Collection Kiosk", "여권 수령 키오스크 / 개인 증명서류 수령 키오스크 이용 수령", "使用領取護照服務站／領取個人證件服務站領取")),
    ("faq", ("Frequently Asked Questions - Travel Documents", "자주 묻는 질문 - 여행증명서", "常見問題 - 旅行證件")),
]

ONLINE_ITEMS = [  # (title, e-service path)
    (("Online Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 온라인 신청", "網上申請柏峴화랑特別行政區護照"), "eservices/passport-application"),
    (("Online Appointment Booking for Travel Documents", "여행증명서 신청 온라인 예약", "網上預約申請旅行證件"), "eservices/travel-document-booking"),
    (("Online Appointment Booking for Smart Identity Card", "스마트 신분증 신청 온라인 예약", "網上預約申領智能身份證"), "eservices/idcard-booking"),
    (("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度"), "eservices/travel-document-status"),
    (("Online Application Status Enquiry (Visas / Entry Permits, Right of Abode)", "신청 현황 온라인 조회(비자·입경허가, 거주권)", "網上查詢申請進度（簽證／進入許可證、居留權）"), "eservices/application-status"),
]

# ----------------------------------------------------------------------------- e-service start page (term)
ES_MENU = [
    ("Points to Note", "유의사항", "注意事項"), ("FAQs", "자주 묻는 질문", "常見問題"), ("Terms of Use", "이용 약관", "使用條款"),
    ("Technical Support Hotline", "기술 지원 상담", "技術支援熱線"), ("Service Demo", "서비스 시연", "服務示範"),
    ("Related Information", "관련 정보", "相關資料"), ("Payment / Transaction Status Enquiry", "결제·거래 상태 조회", "付款／交易狀況查詢"),
]
ES_ANN_TITLE = ("Important Announcement", "중요 공지", "重要公告")
ES_ANN = [
    ("You will have 20 minutes to submit an application. Please prepare the required information.", "신청서를 제출할 수 있는 시간은 20분입니다. 필요한 정보를 미리 준비해 주세요.", "你有20分鐘時間遞交申請，請預先準備所需資料。"),
    ("You may save your application by clicking the “Save and Exit” button and a “Retrieval Code” will be generated, if necessary. To retrieve your saved application, you need to input your identity card number and the “Retrieval Code”. Your application record will only be saved up to 7 days.",
     "필요한 경우 \"저장 후 나가기\" 버튼을 눌러 신청서를 저장하면 \"복구 코드\"가 생성됩니다. 저장한 신청서를 불러오려면 신분증 번호와 \"복구 코드\"를 입력해야 합니다. 신청 기록은 최대 7일간만 보관됩니다.",
     "如有需要，你可按「儲存並離開」按鈕儲存申請，系統會產生「取回編號」。如要取回已儲存的申請，你須輸入身份證號碼及「取回編號」。申請紀錄只會保存最多7天。"),
    ("Please note that successful submission of application does not mean that your application has been approved. If necessary, we may request you to submit another photograph or additional documents to process your application.",
     "신청서를 제출했다고 해서 신청이 승인된 것은 아닙니다. 필요한 경우 신청 처리를 위해 사진을 다시 제출하거나 추가 서류를 제출하도록 요청할 수 있습니다.",
     "請注意，成功遞交申請並不代表申請已獲批准。如有需要，本處可能要求你提交另一張照片或補充文件，以便處理你的申請。"),
]
ES_TERMS_TITLE = ("Copyright Notice, Privacy Policy, Statement of Purpose and Disclaimer for GovBHG", "정부포털 BHG 저작권 안내, 개인정보 처리방침, 수집 목적 및 면책 고지", "「BHG政府一站通」版權公告、私隱政策、收集資料目的及免責聲明")
ES_TERMS = [
    (("Copyright Notice", "저작권 안내", "版權公告"),
     ("By accessing GovBHG or any of its webpages, you unconditionally agree to the terms of this Copyright Notice and as they may be modified and/or supplemented from time to time by the Government without prior notice to you. Please check this webpage regularly for any modifications and/or supplements which may be made.",
      "정부포털 BHG 또는 그 웹페이지에 접속함으로써 이 저작권 안내의 조건과, 정부가 사전 통지 없이 수시로 변경·보완하는 내용에 무조건 동의하는 것으로 봅니다. 변경·보완 사항은 이 웹페이지에서 정기적으로 확인하시기 바랍니다.",
      "你一經瀏覽「BHG政府一站通」或其任何網頁，即表示無條件同意本版權公告的條款，以及政府日後不時修改及／或補充而不另行通知你的內容。請定期查閱本網頁，了解有關修改及／或補充。")),
    (("Scope of Copyright Ownership", "저작권 귀속 범위", "版權擁有範圍"),
     ("Unless otherwise indicated, the contents found on GovBHG are subject to copyright owned by the Government of the Baekhyeon Hwarang Special Administrative Region (\"Government\").",
      "달리 표시되지 않는 한, 정부포털 BHG의 내용은 백현화랑 특별행정구 정부(\"정부\")가 저작권을 보유합니다.",
      "除另有說明外，「BHG政府一站通」的內容均受柏峴화랑特別行政區政府（「政府」）所擁有的版權保護。")),
    (("Non-text Contents on GovBHG", "정부포털 BHG의 비문자 콘텐츠", "「BHG政府一站通」的非文字內容"),
     ("Prior written consent of the Government is required if you intend to reproduce, distribute or otherwise use any non-text contents (including but not limited to photographs, graphics, drawings, diagrams, audio files and video files) found on GovBHG in any way or for any purpose.",
      "정부포털 BHG의 비문자 콘텐츠(사진, 그래픽, 도면, 도표, 음성 파일, 동영상 파일 등)를 어떤 방식으로든 어떤 목적으로든 복제·배포하거나 이용하려면 정부의 사전 서면 동의가 필요합니다.",
      "如你擬以任何方式或為任何目的複製、分發或使用「BHG政府一站通」內的任何非文字內容（包括但不限於相片、圖像、繪圖、圖表、音訊檔案及影片檔案），須事先取得政府的書面同意。")),
]
ES_DECLARE = ("I have read and agree to the above Privacy Policy, Statement of Purpose, Copyright Notice and Disclaimer.", "위 개인정보 처리방침, 수집 목적, 저작권 안내 및 면책 고지를 읽고 동의합니다.", "本人已閱讀並同意上述私隱政策、收集資料目的、版權公告及免責聲明。")
ES_BTN_RETRIEVE = ("Retrieve Saved Application", "저장한 신청서 불러오기", "取回已儲存的申請")
ES_BTN_START = ("START", "시작", "開始")
ES_ERR_AGREE = ("Please tick the declaration box to continue.", "계속하려면 선서 확인란에 체크해 주세요.", "請剔選聲明方格以繼續。")
ES_RETRIEVE = {
    "title": ("Retrieve Saved Application", "저장한 신청서 불러오기", "取回已儲存的申請"),
    "id": ("Identity card number", "신분증 번호", "身份證號碼"), "code": ("Retrieval Code", "복구 코드", "取回編號"),
    "go": ("Retrieve", "불러오기", "取回"), "none": ("No saved application was found.", "저장된 신청서를 찾을 수 없습니다.", "找不到已儲存的申請。"),
}
ES_TITLES = {
    "passport-application": ("Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照"),
    "travel-document-booking": ("Appointment Booking for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件"),
    "idcard-booking": ("Appointment Booking for Smart Identity Card", "스마트 신분증 신청 예약", "預約申領智能身份證"),
    "travel-document-status": ("Travel Document Application Status Enquiry", "여행증명서 신청 현황 조회", "旅行證件申請進度查詢"),
    "application-status": ("Application Status Enquiry", "신청 현황 조회", "申請進度查詢"),
}

# ----------------------------------------------------------------------------- Application for passport (tabs)
AP_PLACE_LABEL = ("Place of Application", "신청 장소", "申請地點")
AP_PLACES = [("in", ("In Baekhyeon Hwarang", "백현화랑 내", "於柏峴화랑")), ("out", ("Outside Baekhyeon Hwarang", "백현화랑 밖", "於柏峴화랑以外地區"))]
AP_PLEASE = ("PLEASE SELECT", "선택하세요", "請選擇")
AP_TABS = [("before", ("Before Applying", "신청 전", "申請前")), ("applying", ("Applying", "신청 중", "申請時")), ("after", ("After Applying", "신청 후", "申請後"))]
AP_SECT = {
    "elig": ("Eligibility", "신청 자격", "申請資格"), "proc": ("Processing Time", "처리 기간", "處理時間"),
    "child": ("Accompanying Children", "자녀 동반", "子女同行"), "faq": ("Frequently Asked Questions", "자주 묻는 질문", "常見問題"),
    "apply": ("Apply Now", "지금 신청", "立即申請"), "book": ("Make an Appointment", "예약하기", "預約"),
    "photo": ("Photograph Requirements", "사진 규격", "照片規格"), "fees": ("Fees", "수수료", "費用"),
    "collect": ("Collection Methods", "수령 방법", "領取方法"), "kiosk": ("Collection via Kiosk", "키오스크 수령", "使用服務站領取"),
    "status": ("Application Status Enquiry", "신청 현황 조회", "申請進度查詢"), "lost": ("Lost, Damaged or Defaced Passport", "분실·훼손·오손 여권", "遺失、損毀或殘破的護照"),
}
AP_CHILD = ("Each person must hold his/her own passport. A child, regardless of age, must apply for his/her own passport; a child cannot be included in a parent's passport.",
            "모든 사람은 본인 명의의 여권을 가져야 합니다. 자녀도 나이와 관계없이 본인 명의의 여권을 신청해야 하며, 부모의 여권에 함께 등록할 수 없습니다.",
            "每個人均須持有本人的護照。兒童不論年齡，均須申請本人的護照，不可附載於父母的護照內。")
AP_PROC = ("Processing normally takes 5 working days after all necessary documents, the application fee and the photograph have been received. For application through the Internet, an extra 2 to 3 working days may be required. It will take 10 working days for applications from children aged under 11 not holding a permanent identity card.",
           "필요한 서류, 수수료, 사진이 모두 접수된 후 처리에는 통상 5근무일이 걸립니다. 인터넷 신청은 2~3근무일이 추가될 수 있으며, 영구 신분증이 없는 만 11세 미만 아동의 신청은 10근무일이 걸립니다.",
           "一般而言，收妥全部所需文件、申請費用及照片後，處理申請需時5個工作天。若透過互聯網申請，可能需額外2至3個工作天。未持有永久性居民身份證的十一歲以下兒童申請，則需10個工作天。")
AP_APPLY_NOTE = ("You may apply through the Internet, or make an appointment online and submit your application in person.", "인터넷으로 신청하거나, 온라인으로 예약한 뒤 직접 방문하여 신청할 수 있습니다.", "你可透過互聯網申請，或在網上預約後親身遞交申請。")
AP_BTN_APPLY = ("Application through the Internet", "인터넷으로 신청", "透過互聯網申請")
AP_BTN_BOOK = ("Make an Appointment to Apply for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件")
AP_BTN_STATUS = ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")
