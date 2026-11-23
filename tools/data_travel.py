# -*- coding: utf-8 -*-
"""Content for Baekhyeon Hwarang Travel Documents section: topic page, booking, status enquiry and the
'Application for Baekhyeon Hwarang SAR Passport' guidebook.  Tuples are (English, Korean, Traditional Chinese)."""

# --------------------------------------------------------------------------- travel documents topic page
TD_BANNER = ("Information for Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청 안내", "申請柏峴화랑特別行政區護照資料")

_P = "P:residents/immigration/traveldoc/"
TD_COMMON = [  # (slug, title) shared link rows
    (_P + "faq", ("Frequently Asked Questions", "자주 묻는 질문", "常見問題")),
    (_P + "fees", ("Fees", "수수료", "費用")),
    (_P + "branches", ("Addresses and Working Hours of Branch Offices", "지소 주소 및 근무 시간", "分區辦事處地址及辦公時間")),
    (_P + "hq", ("Addresses and Working Hours of Offices at Headquarters", "본부 사무실 주소 및 근무 시간", "總部辦事處地址及辦公時間")),
    (_P + "lost", ("What to do if You Lose Your Identity Card and Baekhyeon Hwarang SAR Travel Documents", "신분증 및 백현화랑 특별행정구 여행증명서를 분실했을 때", "遺失身份證及柏峴화랑特別行政區旅行證件時應怎麼辦")),
]
TD_GROUPS = [
    # (title, [(path-or-slug, title, is_page_path)])
    (("Passport", "여권", "護照"), [
        ("P:residents/immigration/traveldoc/passport/apply", ("Online Application", "온라인 신청", "網上申請")),
        ("P:residents/immigration/traveldoc/passport/book", ("Online Appointment Booking for Application", "온라인 신청 예약", "網上預約申請")),
        (_P + "aboutpassport", ("About Passport", "여권 안내", "關於護照")),
    ] + TD_COMMON + [
        ("P:residents/immigration/traveldoc/appstatus", ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")),
    ]),
    (("Document of Identity for Visa Purposes", "비자용 신분증명서", "簽證身份書"), [
        ("P:residents/immigration/traveldoc/passport/book", ("Online Appointment Booking for Application", "온라인 신청 예약", "網上預約申請")),
        (_P + "aboutdocid", ("About Document of Identity for Visa Purposes", "비자용 신분증명서 안내", "關於簽證身份書")),
    ] + TD_COMMON[1:] + [
        ("P:residents/immigration/traveldoc/appstatus", ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")),
    ]),
    (("Re-entry Permit", "재입경 허가증", "回港證"), [
        ("P:residents/immigration/traveldoc/passport/book", ("Online Appointment Booking for Application", "온라인 신청 예약", "網上預約申請")),
        (_P + "aboutreentry", ("About Re-entry Permit", "재입경 허가증 안내", "關於回港證")),
    ] + TD_COMMON[1:] + [
        ("P:residents/immigration/traveldoc/appstatus", ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")),
    ]),
    (("Seaman's Identity Book", "선원 신분증", "海員身份證"), [
        (_P + "aboutseaman", ("About Seaman's Identity Book", "선원 신분증 안내", "關於海員身份證")),
    ] + TD_COMMON[1:4]),
]
TD_BLURB = {  # short descriptions shown in the accordion
    "Passport": (
        "You can now apply for a Baekhyeon Hwarang SAR Passport that complies with the standard of the International Civil Aviation Organization (ICAO). Find out more about its security features and the application details here.",
        "국제민간항공기구(ICAO) 기준에 부합하는 백현화랑 특별행정구 여권을 신청할 수 있습니다. 보안 요소와 신청 방법을 여기에서 확인하세요.",
        "你現在可申請符合國際民航組織（ICAO）標準的柏峴화랑特別行政區護照。你可在這裏了解護照的防偽特徵及申請詳情。"),
}

# --------------------------------------------------------------------------- Online Appointment Booking
BOOK_TITLE = ("Book Appointment to Apply for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件")
BOOK_BLOCKS = [
    ("p", ("You can make use of this online service to make an appointment to apply for the following travel documents items (i) to (iii) at the Immigration headquarters or to apply for the following travel documents items (i) to (iv) at any of the Immigration Branch Offices –",
           "이 온라인 서비스로 출입경사무처 본부에서 다음 여행증명서 (i)~(iii)을, 또는 출입경사무처 지소 어디에서나 다음 여행증명서 (i)~(iv)를 신청하기 위한 예약을 할 수 있습니다.",
           "你可使用這項網上服務，預約到入境事務處總部申請下列第(i)至(iii)項旅行證件，或預約到任何一間入境事務處分區辦事處申請下列第(i)至(iv)項旅行證件 –")),
    ("olr", [
        ("Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照"),
        ("Baekhyeon Hwarang SAR Re-entry Permit", "백현화랑 특별행정구 재입경 허가증", "柏峴화랑特別行政區回港證"),
        ("Baekhyeon Hwarang SAR Document of Identity for Visa Purposes", "백현화랑 특별행정구 비자용 신분증명서", "柏峴화랑特別行政區簽證身份書"),
        ("Baekhyeon Hwarang SAR Seaman's Identity Book", "백현화랑 특별행정구 선원 신분증", "柏峴화랑特別行政區海員身份證"),
    ]),
    ("p", ("You can make advance booking within 24 working days for applying for travel documents in immigration offices. You can also change, cancel or enquire about the appointment you have made. This article will tell you what you should know before using the online booking service.",
           "출입경 사무소에서 여행증명서를 신청하기 위해 24근무일 이내로 미리 예약할 수 있습니다. 예약한 내용을 변경·취소하거나 조회할 수도 있습니다. 이 글에서는 온라인 예약 서비스를 이용하기 전에 알아야 할 사항을 안내합니다.",
           "你可預約於24個工作天內到入境事務辦事處申請旅行證件，亦可更改、取消或查詢已作出的預約。本文會告訴你使用網上預約服務前須知道的事項。")),
    ("h2", ("Online Appointment Booking", "온라인 예약", "網上預約")),
    ("p", ("If you know what information is required, you can now click the appropriate link below to make your appointment. Otherwise, please check for the details in the paragraphs below.",
           "필요한 정보를 알고 있다면 아래 링크를 눌러 바로 예약할 수 있습니다. 그렇지 않다면 아래 설명을 먼저 확인해 주세요.",
           "若你已知道所需資料，現可按下列適當的連結預約；否則，請先參閱以下各段的詳細資料。")),
    ("btn", ("Make an Appointment to Apply for Travel Documents", "여행증명서 신청 예약하기", "預約申請旅行證件"), "appointment"),
    ("p", ("To ensure fair use of this online service, an applicant who uses computer programs or automated tools to interfere with the normal operation of the system or to make appointment bookings/online applications shall be deemed to have improperly used the system. The Immigration Department may immediately block his/her access to the system without prior notice.",
           "이 온라인 서비스의 공정한 이용을 위해, 컴퓨터 프로그램이나 자동화 도구로 시스템의 정상 운영을 방해하거나 예약·온라인 신청을 하는 신청인은 시스템을 부당하게 사용한 것으로 봅니다. 출입경사무처는 사전 통지 없이 해당 신청인의 시스템 접근을 즉시 차단할 수 있습니다.",
           "為確保公平使用此項網上服務，申請人如以電腦程式或自動化工具干擾系統的正常運作或進行預約／網上申請，即作不當使用系統論。入境事務處可即時封鎖申請人使用系統的權限，無須預先通知。")),
    ("ulink", ("Information required in appointment booking", "예약 시 필요한 정보", "預約時所需的資料"), "#howtostart"),
    ("strong", ("Change, Cancel or Enquire about the Appointment:", "예약 변경·취소·조회:", "更改、取消或查詢預約：")),
    ("strong", ("If you wish to change, cancel or enquire about the appointment, please click the above appointment booking link.",
                "예약을 변경·취소하거나 조회하려면 위의 예약 링크를 누르세요.",
                "如你想更改、取消或查詢預約，請按上述預約連結。")),
    ("h2id", "howtostart", ("How to Start", "시작하는 방법", "如何開始")),
    ("p", ("Information required in appointment booking", "예약 시 필요한 정보", "預約時所需的資料")),
    ("ol", [
        ("For applicants with Baekhyeon Hwarang SAR identity (BHID) cards, please enter your existing BHID card number and your date of birth. If you are making an appointment for a child, please enter the child's existing BHID card number and date of birth;",
         "백현화랑 특별행정구 신분증(BHID)을 소지한 신청인은 기존 BHID 번호와 생년월일을 입력하세요. 자녀를 위한 예약이라면 자녀의 기존 BHID 번호와 생년월일을 입력하세요.",
         "持有柏峴화랑身份證（BHID）的申請人，請輸入你現有的BHID卡號碼及出生日期。如為兒童預約，請輸入該兒童現有的BHID卡號碼及出生日期；"),
        ("For a child without BHID card, the parent / guardian should enter the BHID card number and date of birth of the applying guardian (i.e. the parent/guardian who is going to sign the application form of the child and accompany him/her to apply) and date of birth of the child; or, if the child's birth has been registered, the child's Baekhyeon Hwarang SAR birth certificate number with its date of registration and the date of birth of the child;",
         "BHID가 없는 자녀의 경우, 부모·보호자는 신청 보호자(자녀의 신청서에 서명하고 동행하여 신청할 부모·보호자)의 BHID 번호와 생년월일 및 자녀의 생년월일을 입력하거나, 자녀의 출생이 등록되어 있다면 자녀의 백현화랑 특별행정구 출생증명서 번호와 등록일, 자녀의 생년월일을 입력하세요.",
         "未持有BHID卡的兒童，其父、母或監護人須輸入申請監護人（即將簽署該兒童申請書並陪同其申請的父、母或監護人）的BHID卡號碼及出生日期，以及該兒童的出生日期；或如該兒童的出生已登記，則輸入該兒童的柏峴화랑特別行政區出生證明書號碼及登記日期，以及該兒童的出生日期；"),
        ("For newborn babies whose mother is a BHID card holder, please enter the BHID card number of the mother and the date of birth of the baby. Information input must match with the birth return of the hospital;",
         "어머니가 BHID 소지자인 신생아의 경우, 어머니의 BHID 번호와 신생아의 생년월일을 입력하세요. 입력 정보는 병원의 출생 신고 내용과 일치해야 합니다.",
         "母親持有BHID卡的初生嬰兒，請輸入母親的BHID卡號碼及嬰兒的出生日期。所輸入的資料必須與醫院的出生報告相符；"),
        ("For newborn babies whose births have not been registered and whose parents do not hold a BHID card, please enter the last six digits of the mother's travel document number and the child's date of birth, which must match with the birth return of the hospital;",
         "출생이 아직 등록되지 않았고 부모가 BHID를 소지하지 않은 신생아의 경우, 어머니의 여행증명서 번호 끝 6자리와 자녀의 생년월일을 입력하세요. 이는 병원의 출생 신고 내용과 일치해야 합니다.",
         "出生尚未登記而父母均沒有BHID卡的初生嬰兒，請輸入母親旅行證件號碼的最後六個數字及該兒童的出生日期，有關資料必須與醫院的出生報告相符；"),
        ("You may book an appointment for up to 4 applicants, with a maximum of 4 applications. Applicants of the same appointment should turn up at the chosen office together at the selected time slot;",
         "한 번에 최대 4명의 신청인, 최대 4건의 신청을 예약할 수 있습니다. 같은 예약의 신청인은 선택한 시간대에 선택한 사무소에 함께 방문해야 합니다.",
         "每次預約最多可為4名申請人預約，最多可作4宗申請。同一預約的申請人須於所選時段一同前往所選辦事處；"),
        ("In one booking, you can make appointment for up to two types of travel documents (e.g. Baekhyeon Hwarang SAR Passport & Baekhyeon Hwarang SAR Re-entry Permit);",
         "한 번의 예약으로 최대 2종류의 여행증명서(예: 백현화랑 특별행정구 여권과 재입경 허가증)를 예약할 수 있습니다.",
         "每次預約最多可預約兩種旅行證件（例如柏峴화랑特別行政區護照及回港證）；"),
        ("For each type of travel document to be applied, you are only required to make one appointment booking for your multiple birth babies; and",
         "신청하려는 여행증명서 종류마다, 다태아 자녀에 대해서는 한 번만 예약하면 됩니다.",
         "就每種申請的旅行證件，如為多胞胎嬰兒，只須預約一次；及"),
        ("For security purpose, you have to enter a 4-digit enquiry code which you set personally for subsequent change, cancel or enquiry of your appointment.",
         "보안을 위해, 이후 예약을 변경·취소·조회할 때 사용할 4자리 조회 코드를 직접 설정하여 입력해야 합니다.",
         "為保安起見，你須自行設定一個4位數字的查詢編號，以便日後更改、取消或查詢預約。"),
    ]),
    ("p", ("(Please also take note of the Guidelines for Appointment)", "(예약 안내 사항도 함께 확인해 주세요)", "（請同時留意預約須知）")),
    ("h2", ("Guidelines for Appointment", "예약 안내 사항", "預約須知")),
    ("ol", [
        ("If the information provided for making an appointment is incorrect, the appointment will be automatically deleted from the system without further notice.",
         "예약 시 제공한 정보가 정확하지 않으면, 예약은 별도 통지 없이 시스템에서 자동 삭제됩니다.",
         "如預約時所提供的資料不正確，預約將會自動從系統中刪除，恕不另行通知。"),
        ("You can make an appointment for the following 24 working days (Monday to Saturday, except General Holidays). The result of booking is subject to availability of quota of each office. You can only make one appointment within the 24-working-day period.",
         "이후 24근무일(월~토요일, 일반 공휴일 제외) 이내로 예약할 수 있습니다. 예약 결과는 사무소별 잔여 인원에 따라 달라집니다. 24근무일 기간 중에는 한 번만 예약할 수 있습니다.",
         "你可預約其後24個工作天（星期一至星期六，公眾假期除外）內的時段。預約結果須視乎各辦事處的名額而定。在24個工作天期間，你只可預約一次。"),
        ("When a successful appointment is made and you have chosen to receive an appointment reminder, an email reminder will be sent to the email address you provided 2 days before the appointment day. You can change your email address or cancel the reminder at least 3 days before the appointment day.",
         "예약이 완료되고 예약 알림을 받기로 선택한 경우, 예약일 2일 전에 입력한 이메일 주소로 알림이 발송됩니다. 이메일 주소 변경 또는 알림 취소는 예약일 3일 전까지 할 수 있습니다.",
         "預約成功後，如你選擇接收預約提示，系統會於預約日期前2日向你所提供的電郵地址發出電郵提示。你可於預約日期前至少3日更改電郵地址或取消提示。"),
        ("After an appointment is made, you may change / cancel the appointment at least 1 day before the appointment date. For changing an appointment, the earliest day will be on next working day (Monday to Saturday, except General Holidays) of the date of changing the appointment. In view of the limited appointment quotas, please change or cancel your appointment at least 1 day before the appointment day if you are not able to attend.",
         "예약 후에는 예약일 1일 전까지 예약을 변경·취소할 수 있습니다. 예약을 변경하는 경우 가장 빠른 날짜는 변경한 날의 다음 근무일(월~토요일, 일반 공휴일 제외)입니다. 예약 인원이 한정되어 있으므로, 참석할 수 없으면 예약일 1일 전까지 예약을 변경하거나 취소해 주세요.",
         "預約後，你可於預約日期前至少1日更改／取消預約。更改預約的最早日期為更改預約當日的下一個工作天（星期一至星期六，公眾假期除外）。由於預約名額有限，如你不能出席，請最少於預約日期前1日更改或取消預約。"),
        ("If you choose to input the travel document number, please only input numerals of your travel document number. If your travel document number is more than six digits, please enter the last six digits. If it is less than six digits, please add leading zeros to make up six digits. For example, input '001023' for travel document number 'AB/10-23-CD'.",
         "여행증명서 번호를 입력하는 경우 번호 중 숫자만 입력하세요. 번호가 6자리를 넘으면 끝 6자리를 입력하고, 6자리 미만이면 앞에 0을 붙여 6자리로 맞추세요. 예: 여행증명서 번호 'AB/10-23-CD'는 '001023'으로 입력합니다.",
         "如你選擇輸入旅行證件號碼，請只輸入旅行證件號碼內的數字。如旅行證件號碼多於六個數字，請輸入最後六個數字；如少於六個數字，請在前面加上「0」補足六個數字。例如，旅行證件號碼「AB/10-23-CD」應輸入「001023」。"),
        ("The births returns from hospitals are updated daily at 12:00 midnight.",
         "병원의 출생 신고 자료는 매일 자정(00:00)에 갱신됩니다.",
         "醫院的出生報告資料每日午夜十二時更新。"),
    ]),
    ("h2", ("Supporting Documents to Take with You", "지참할 증빙서류", "須攜帶的證明文件")),
    ("p", ("You should bring along the supporting documents to your appointment according to what kind of travel document you are going to apply for. Please refer to the following links for more information.",
           "신청하려는 여행증명서의 종류에 따라 필요한 증빙서류를 예약 당일 지참하세요. 자세한 내용은 아래 링크를 참고하세요.",
           "你應按所申請的旅行證件種類，在預約當日攜帶所需的證明文件。詳情請參閱以下連結。")),
    ("links", [
        ("More information on Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 자세히 보기", "更多關於柏峴화랑特別行政區護照的資料"),
        ("More information on Baekhyeon Hwarang SAR Re-entry Permit", "백현화랑 특별행정구 재입경 허가증 자세히 보기", "更多關於柏峴화랑特別行政區回港證的資料"),
        ("More information on Baekhyeon Hwarang SAR Document of Identity for Visa Purposes", "백현화랑 특별행정구 비자용 신분증명서 자세히 보기", "更多關於柏峴화랑特別行政區簽證身份書的資料"),
        ("More information on Baekhyeon Hwarang SAR Seaman's Identity Book", "백현화랑 특별행정구 선원 신분증 자세히 보기", "更多關於柏峴화랑特別行政區海員身份證的資料"),
    ]),
    ("h2", ("Booking through Immigration Department Mobile Application or by Phone", "출입경사무처 모바일 앱 또는 전화로 예약", "透過入境事務處流動應用程式或電話預約")),
    ("p", ("Besides the online booking system, you can also make an appointment to apply for Baekhyeon Hwarang SAR Passport, Baekhyeon Hwarang SAR Re-entry Permit and Baekhyeon Hwarang SAR Document of Identity for Visa Purposes through Immigration Department Mobile Application or via the 24-hour telephone booking system. Appointment for Baekhyeon Hwarang SAR Seaman's Identity Book can be made through the online booking system and Immigration Department Mobile Application.",
           "온라인 예약 시스템 외에도, 출입경사무처 모바일 앱 또는 24시간 전화 예약 시스템으로 백현화랑 특별행정구 여권, 재입경 허가증, 비자용 신분증명서 신청을 예약할 수 있습니다. 백현화랑 특별행정구 선원 신분증 신청은 온라인 예약 시스템과 출입경사무처 모바일 앱으로 예약할 수 있습니다.",
           "除網上預約系統外，你亦可透過入境事務處流動應用程式或24小時電話預約系統，預約申請柏峴화랑特別行政區護照、回港證及簽證身份書。柏峴화랑特別行政區海員身份證可透過網上預約系統及入境事務處流動應用程式預約。")),
    ("h2", ("Immigration Offices for Travel Document Applications", "여행증명서 신청 출입경 사무소", "受理旅行證件申請的入境事務辦事處")),
    ("p", ("Please refer to the following link for the addresses and working hours of Immigration Offices for Travel Document Applications.",
           "여행증명서 신청을 받는 출입경 사무소의 주소와 근무 시간은 아래 링크를 참고하세요.",
           "有關受理旅行證件申請的入境事務辦事處的地址及辦公時間，請參閱以下連結。")),
    ("links", [
        ("Addresses and working hours of Immigration Offices at Immigration Headquarters", "출입경사무처 본부 사무실의 주소 및 근무 시간", "入境事務處總部辦事處的地址及辦公時間"),
        ("Addresses and working hours of Immigration Offices at Immigration Branch Offices", "출입경사무처 지소의 주소 및 근무 시간", "入境事務處分區辦事處的地址及辦公時間"),
    ]),
    ("h2", ("Assistance and Further Information", "지원 및 상세 정보", "支援及詳細資料")),
    ("p", ("If you need technical assistance in using the online service, you can contact the Immigration e-Services Hotline during service hours.",
           "온라인 서비스 이용 중 기술 지원이 필요하면 서비스 운영 시간에 출입경사무처 전자서비스 상담 창구로 문의하세요.",
           "如你於使用網上服務時需要技術支援，可於服務時間內聯絡入境事務處電子服務熱線。")),
    ("p", ("For general enquiries, please contact the Immigration Department during office hours (Monday to Friday, and Saturday morning, except public holidays).",
           "일반 문의는 공휴일을 제외한 월~금요일 및 토요일 오전의 근무 시간에 출입경사무처로 하시기 바랍니다.",
           "一般查詢可於辦公時間（星期一至五及星期六上午，公眾假期除外）向入境事務處查詢。")),
    ("p", ("Further information on this service is also available in a set of helpful Frequently Asked Questions (FAQs).",
           "이 서비스에 대한 추가 정보는 자주 묻는 질문(FAQ)에서도 확인할 수 있습니다.",
           "有關此服務的進一步資料，亦可參閱一系列實用的常見問題。")),
    ("link", ("FAQs about online appointment booking for application for travel documents", "여행증명서 신청 온라인 예약 자주 묻는 질문", "網上預約申請旅行證件常見問題"), "faq"),
]

# --------------------------------------------------------------------------- Status enquiry
STATUS_TITLE = ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")
STATUS_BLOCKS = [
    ("p", ("If you have submitted an application related to a Baekhyeon Hwarang SAR Travel Document to the Immigration Department, you can enquire online about the status of that application. This page will tell you who can use the online service, how to use it and how to obtain further information.",
           "백현화랑 특별행정구 여행증명서와 관련된 신청을 출입경사무처에 제출했다면, 해당 신청의 처리 현황을 온라인으로 조회할 수 있습니다. 이 페이지에서는 이 서비스를 이용할 수 있는 사람, 이용 방법과 추가 정보를 얻는 방법을 안내합니다.",
           "如你已向入境事務處遞交有關柏峴화랑特別行政區旅行證件的申請，你可在網上查詢該申請的進度。本頁會告訴你誰可使用這項網上服務、如何使用及如何取得進一步資料。")),
    ("h2", ("Who Can Use This Service", "이용 대상", "誰可使用此服務")),
    ("p", ("If you have submitted an application for Baekhyeon Hwarang SAR passport, Document of Identity for Visa Purposes or Re-entry Permit, you can use the service to enquire about the status of application.",
           "백현화랑 특별행정구 여권, 비자용 신분증명서 또는 재입경 허가증을 신청했다면 이 서비스로 신청 현황을 조회할 수 있습니다.",
           "如你已遞交柏峴화랑特別行政區護照、簽證身份書或回港證的申請，你可使用此服務查詢申請進度。")),
    ("h2", ("How to Make an Enquiry Online", "온라인으로 조회하는 방법", "如何在網上查詢")),
    ("p", ("You can access the service through the link below. When you have done so, you will need to enter your application reference number and input your day and year of birth. If the information matches the Immigration Department's records, the application status will be shown.",
           "아래 링크로 서비스에 접속하세요. 접속 후 신청 접수번호를 입력하고 생일(일)과 출생 연도를 입력해야 합니다. 입력한 정보가 출입경사무처의 기록과 일치하면 신청 현황이 표시됩니다.",
           "你可透過下面的連結使用此服務。進入後，你須輸入申請的參考編號，以及你出生的日及年。如所輸入的資料與入境事務處的紀錄相符，系統便會顯示申請進度。")),
    ("p", ("If your application has been cancelled or finalised, the record will be purged from the system and you will not be able to enquire about its status.",
           "신청이 취소되었거나 처리가 완료된 경우 해당 기록은 시스템에서 삭제되어 현황을 조회할 수 없습니다.",
           "如你的申請已被取消或已處理完畢，有關紀錄會從系統中清除，你將無法查詢其進度。")),
    ("p", ("The application status enquiry service is also available on “BH Smart” for applications of Baekhyeon Hwarang SAR travel documents submitted on or after 1 January 2026. By registering for a “BH Smart” account and providing user authorisation, you can view the application status under “Status” of the “Personal Assistant” page. To ensure you can receive the latest information, your “BH Smart” account must remain valid.",
           "2026년 1월 1일 이후 제출한 백현화랑 특별행정구 여행증명서 신청은 \"BH 스마트\"에서도 현황을 조회할 수 있습니다. \"BH 스마트\" 계정을 등록하고 이용자 권한 부여를 하면 \"개인 비서\" 페이지의 \"현황\"에서 신청 현황을 볼 수 있습니다. 최신 정보를 받으려면 \"BH 스마트\" 계정이 유효한 상태여야 합니다.",
           "2026年1月1日或以後遞交的柏峴화랑特別行政區旅行證件申請，亦可透過「BH智方便」查詢申請進度。登記「BH智方便」帳戶並提供用戶授權後，你可在「個人助理」頁面的「進度」中查看申請進度。為確保你能收到最新資料，你的「BH智方便」帳戶必須保持有效。")),
    ("link", ("Details on “Personal Assistant” of “BH Smart” and How to Provide User Authorisation", "\"BH 스마트\" \"개인 비서\" 상세 안내 및 이용자 권한 부여 방법", "「BH智方便」「個人助理」詳情及如何提供用戶授權"), "bhsmart"),
    ("btn", STATUS_TITLE, "tdstatus"),
    ("h2", ("Assistance and Further Information", "지원 및 상세 정보", "支援及詳細資料")),
    ("p", ("If you need technical assistance in using the online service, you can contact the Immigration e-Services Hotline during service hours.",
           "온라인 서비스 이용 중 기술 지원이 필요하면 서비스 운영 시간에 출입경사무처 전자서비스 상담 창구로 문의하세요.",
           "如你於使用網上服務時需要技術支援，可於服務時間內聯絡入境事務處電子服務熱線。")),
    ("p", ("For general enquiries, please contact the Immigration Department during office hours (Monday to Friday, and Saturday morning, except public holidays).",
           "일반 문의는 공휴일을 제외한 월~금요일 및 토요일 오전의 근무 시간에 출입경사무처로 하시기 바랍니다.",
           "一般查詢可於辦公時間（星期一至五及星期六上午，公眾假期除外）向入境事務處查詢。")),
]

# --------------------------------------------------------------------------- Guidebook: Application for Baekhyeon Hwarang SAR Passport
GB_TITLE = ("Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照")
GB_INTRO = ("A person is eligible to apply for a Baekhyeon Hwarang Special Administrative Region (Baekhyeon Hwarang SAR) Passport if he/she is:",
            "다음에 해당하는 사람은 백현화랑 특별행정구 여권을 신청할 자격이 있습니다.",
            "符合下列條件的人士可申請柏峴화랑特別行政區護照：")
GB_ELIG = [
    ("a Korean citizen;", "대한민국 국민이고,", "大韓民國國民；"),
    ("a permanent resident of the Baekhyeon Hwarang SAR; and", "백현화랑 특별행정구 영주권자이며,", "柏峴화랑特別行政區永久性居民；及"),
    ("a holder of a valid Baekhyeon Hwarang SAR permanent identity card.", "유효한 백현화랑 특별행정구 영구 신분증을 소지한 사람.", "持有有效柏峴화랑永久性居民身份證。"),
]
GB_MORE_ELIG = ("More on eligibility", "자격 요건 자세히 보기", "更多關於資格的資料")
GB_SEC = {
    "forms": ("Application Forms and Required Supporting Documents", "신청서 및 필요 증빙서류", "申請表格及所需證明文件"),
    "means": ("Means of Application and Payment Methods", "신청 방법 및 납부 방법", "申請途徑及繳費方法"),
    "collect": ("Collection Methods", "수령 방법", "領取方法"),
    "proc": ("Processing Time", "처리 기간", "處理申請的時間"),
}
GB_MORE = {
    "docs": ("More on supporting documents", "증빙서류 자세히 보기", "更多關於證明文件的資料"),
    "means": ("More on means of application and payment methods", "신청·납부 방법 자세히 보기", "更多關於申請途徑及繳費方法的資料"),
    "collect": ("More on collection methods", "수령 방법 자세히 보기", "更多關於領取方法的資料"),
    "proc": ("More on processing time", "처리 기간 자세히 보기", "更多關於處理時間的資料"),
    "photo": ("specifications", "규격", "規格"),
    "faqpay": ("FAQs about Online Payment Service", "온라인 결제 서비스 자주 묻는 질문", "網上付款常見問題"),
}
GB_MOREBTN = ("More Guidebooks", "안내서 더 보기", "更多指南")
GB_SHARE = ("Share:", "공유:", "分享：")

_PHOTO = ("A recent colour photograph with white background that conforms to the specifications.",
          "규격에 맞는, 흰색 배경의 최근 컬러 사진.", "背景為白色的彩色近照，須符合規格。")
_PHOTO3 = ("Three recent colour photographs with white background that conforms to the specifications.",
           "규격에 맞는, 흰색 배경의 최근 컬러 사진 3장.", "背景為白色的彩色近照三張，須符合規格。")
_IDCARD16 = ("Baekhyeon Hwarang SAR permanent identity card / Acknowledgement of application for a Baekhyeon Hwarang SAR permanent identity card.",
             "백현화랑 특별행정구 영구 신분증 / 영구 신분증 신청 확인서.", "柏峴화랑永久性居民身份證／「申請柏峴화랑永久性居民身份證收據」。")
_ADD1617 = ("Additional requirements for applicants aged 16 or 17", "만 16세·17세 신청인의 추가 요건", "十六及十七歲申請人的額外規定")
_PARENTID = ("Consenting parent or legal guardian's Baekhyeon Hwarang SAR identity card or valid travel document(s).",
             "동의하는 부모 또는 법정대리인의 백현화랑 특별행정구 신분증 또는 유효한 여행증명서.",
             "同意這項申請的父、母或合法監護人的柏峴화랑身份證或有效旅行證件。")
_MARRIED = ("If the applicant is married, only his/her marriage certificate (not required if the applicant got married in Baekhyeon Hwarang) is required. Parental or legal guardian's consent and items %s are not required.",
            "신청인이 기혼인 경우 혼인증명서(백현화랑 특별행정구에서 혼인한 경우 불필요)만 필요하며, 부모 또는 법정대리인의 동의와 %s 서류는 필요하지 않습니다.",
            "如申請人已婚，則只須提交其結婚證書（如在柏峴화랑結婚則無需提交），無須父、母或合法監護人的同意及第%s項的文件。")


_PAYCOLS_IN = [
    ("OPS", "온라인 결제 서비스", "網上繳費服務"),
    ("Credit card (VISA, Mastercard and JCB only)", "신용카드(VISA, Mastercard, JCB만 가능)", "信用卡（只接受VISA、萬事達卡及JCB）"),
    ("Cash", "현금", "現金"),
    ("Transit card", "교통카드", "交通卡"),
    ("Debit card", "체크카드", "扣賬卡"),
    ("Instant bank transfer", "계좌 간편이체", "即時轉賬"),
    ("Mobile wallets", "모바일 지갑", "流動錢包"),
    ("Crossed cheque", "선 긋기 수표", "劃線支票"),
]
_ROWS_IN = [
    (("Internet^", "인터넷^", "互聯網^"), [1, 1, 0, 0, 0, 1, 1, 0]),
    (("Immigration Department Mobile Application^", "출입경사무처 모바일 앱^", "入境事務處流動應用程式^"), [0, 1, 0, 0, 0, 1, 1, 0]),
    (("Counter (Book online)", "창구(온라인 예약)", "櫃枱（網上預約）"), [0, 0, 1, 1, 1, 1, 1, 1]),
    (("Travel Document Submission Kiosk", "여행증명서 제출 키오스크", "旅行證件遞交服務站"), [0, 0, 0, 1, 1, 1, 0, 0]),
    (("Personal Documentation Submission Kiosk", "개인 증명서류 제출 키오스크", "個人證件遞交服務站"), [0, 0, 0, 1, 0, 1, 0, 0]),
    (("By post* / Drop-in", "우편* / 직접 투입", "郵寄*／投遞"), [0, 0, 0, 0, 0, 0, 0, 1]),
]
_PAYCOLS_OUT = [
    ("OPS", "온라인 결제 서비스", "網上繳費服務"),
    ("Credit card (VISA, Mastercard and JCB only)", "신용카드(VISA, Mastercard, JCB만 가능)", "信用卡（只接受VISA、萬事達卡及JCB）"),
    ("Cheque", "수표", "支票"),
    ("Bank draft", "은행 어음", "銀行匯票"),
    ("Referee in Baekhyeon Hwarang", "백현화랑 특별행정구 내 보증인", "柏峴화랑特別行政區內的擔保人"),
    ("Instant bank transfer", "계좌 간편이체", "即時轉賬"),
    ("Mobile wallets", "모바일 지갑", "流動錢包"),
]
_ROWS_OUT = [
    (("Internet^", "인터넷^", "互聯網^"), [1, 1, 0, 0, 0, 1, 1]),
    (("Immigration Department Mobile Application^", "출입경사무처 모바일 앱^", "入境事務處流動應用程式^"), [0, 1, 0, 0, 0, 1, 1]),
    (("In person (Korean Diplomatic and Consular Missions)", "직접 방문(대한민국 재외공관)", "親身遞交（大韓民國駐外使領館）"), [0, 0, 1, 1, 1, 0, 0]),
    (("By post*", "우편*", "郵寄*"), [0, 0, 1, 1, 0, 0, 0]),
]
_NOTE_IN = ("^Passport fee is payable at the time of application by paying online through OPS, instant bank transfer, mobile wallets or credit card (VISA, Mastercard and JCB only). For application submitted through the ImmD Mobile Application, it is payable at the time of application through instant bank transfer, mobile wallets or credit card (VISA, Mastercard and JCB only).",
            "^여권 수수료는 신청 시 온라인 결제 서비스, 계좌 간편이체, 모바일 지갑 또는 신용카드(VISA, Mastercard, JCB만 가능)로 온라인 납부합니다. 출입경사무처 모바일 앱으로 신청한 경우에는 신청 시 계좌 간편이체, 모바일 지갑 또는 신용카드(VISA, Mastercard, JCB만 가능)로 납부합니다.",
            "^護照費用須於遞交申請時，透過網上繳費服務、即時轉賬、流動錢包或信用卡（只接受VISA、萬事達卡及JCB）在網上繳付。透過入境事務處流動應用程式遞交的申請，須於遞交申請時透過即時轉賬、流動錢包或信用卡（只接受VISA、萬事達卡及JCB）繳付。")
_NOTE_OUT = ("^Passport fee and the additional charge for the delivery of the passport from the Baekhyeon Hwarang SAR to the Korean Diplomatic and Consular Missions (if applicable) are payable at the time of application by paying online through OPS, instant bank transfer, mobile wallets or credit card (VISA, Mastercard and JCB only). For application submitted through the ImmD Mobile Application, it is payable at the time of application through instant bank transfer, mobile wallets or credit card (VISA, Mastercard and JCB only).",
             "^여권 수수료와 백현화랑 특별행정구에서 재외공관으로 여권을 보내는 데 드는 추가 요금(해당되는 경우)은 신청 시 온라인 결제 서비스, 계좌 간편이체, 모바일 지갑 또는 신용카드(VISA, Mastercard, JCB만 가능)로 온라인 납부합니다. 출입경사무처 모바일 앱으로 신청한 경우에는 신청 시 계좌 간편이체, 모바일 지갑 또는 신용카드(VISA, Mastercard, JCB만 가능)로 납부합니다.",
             "^護照費用及將護照由柏峴화랑特別行政區遞送至大韓民國駐外使領館的額外費用（如適用），須於遞交申請時透過網上繳費服務、即時轉賬、流動錢包或信用卡（只接受VISA、萬事達卡及JCB）在網上繳付。透過入境事務處流動應用程式遞交的申請，須於遞交申請時透過即時轉賬、流動錢包或信用卡（只接受VISA、萬事達卡及JCB）繳付。")
_ADDR = (("*Address:", "*주소:", "*地址："),
         [("Travel Documents and Nationality (Application) Section", "여행증명서·국적(신청) 과", "旅行證件及國籍（申請）組"),
          ("Immigration Headquarters", "출입경사무처 본부", "入境事務處總部"),
          ("Baekhyeon Hwarang Special Administrative Region", "백현화랑 특별행정구", "柏峴화랑特別行政區")])

_COL_IN = (
    ("Collection in Baekhyeon Hwarang", "백현화랑 특별행정구 내 수령", "在柏峴화랑領取"),
    ("After receipt of the Collection Notice issued by the Immigration Department notifying the period and office for collecting the passport, unless receiving further notice from the Immigration Department, the applicant can collect the new passport at the selected office direct according to the prescribed details on the Collection Notice.",
     "출입경사무처가 발급한 수령 통지서(수령 기간 및 수령 사무소 안내)를 받은 후, 출입경사무처의 추가 통지가 없는 한 신청인은 수령 통지서에 적힌 내용에 따라 선택한 사무소에서 직접 새 여권을 수령할 수 있습니다.",
     "收到入境事務處發出的領證通知（列明領取護照的期限及辦事處）後，除非接獲入境事務處的進一步通知，申請人可按領證通知所列的詳情，直接到所選定的辦事處領取新護照。"),
)
_COL_KDCM = (
    ("Collection at Korean Diplomatic and Consular Missions", "재외공관 수령", "在大韓民國駐外使領館領取"),
    ("The applicant should collect the passport according to the instructions of the Korean Diplomatic and Consular Missions.",
     "신청인은 재외공관의 안내에 따라 여권을 수령해야 합니다.",
     "申請人須按大韓民國駐外使領館的指示領取護照。"),
)
_COL_KDCM_CHILD = (
    _COL_KDCM[0],
    ("The consenting parent / legal guardian of the child should collect the passport according to the instructions of the Korean Diplomatic and Consular Missions.",
     "자녀의 동의 부모·법정대리인은 재외공관의 안내에 따라 여권을 수령해야 합니다.",
     "兒童的同意申請的父、母或合法監護人須按大韓民國駐外使領館的指示領取護照。"),
)
_PROC5 = ("The processing time will take 5 working days.", "처리 기간은 5근무일입니다.", "處理時間為5個工作天。")
_PROC10 = ("The processing time will take 5 working days. It will take 10 working days for applications from children aged under 11 not holding a Baekhyeon Hwarang SAR permanent identity card.",
           "처리 기간은 5근무일입니다. 백현화랑 특별행정구 영구 신분증이 없는 만 11세 미만 아동의 신청은 10근무일이 걸립니다.",
           "處理時間為5個工作天。如為未持有柏峴화랑永久性居民身份證的十一歲以下兒童申請，則需10個工作天。")
_PROC_NOTE = ("Note for applicants who choose to collect passport via the Korean Diplomatic and Consular Missions: The time for dispatching the prepared passport is excluded from the processing time listed above. The actual delivery time will be subject to factors including the duration of security checks, air freight capacity, and progress of customs clearance at the destination. Extra time may be necessary for destinations that are more remote. Given it will take time to complete the passport application until the new passport reaches the selected mission, applicants with travel plans are reminded to allow sufficient time for the application for and collection of their new passports.",
              "재외공관 수령을 선택한 신청인 유의사항: 위 처리 기간에는 완성된 여권을 발송하는 데 걸리는 시간이 포함되지 않습니다. 실제 배송 시간은 보안 검색 소요 시간, 항공 화물 여력, 도착지의 통관 진행 상황 등에 따라 달라지며, 먼 지역은 더 오래 걸릴 수 있습니다. 새 여권이 선택한 재외공관에 도착하기까지 시간이 걸리므로, 여행 계획이 있는 신청인은 신청과 수령에 충분한 시간을 두시기 바랍니다.",
              "選擇透過大韓民國駐外使領館領取護照的申請人請注意：以上列明的處理時間並不包括遞送護照所需時間。實際遞送時間須視乎保安檢查所需時間、空運載運能力及目的地清關進度等因素而定，較偏遠的目的地或需更多時間。由於整項護照申請直至新護照送抵所選的使領館需時，若申請人有計劃出行，請預留充足時間遞交申請及領取新護照。")

# each tab: dict(title, forms=[(head, body_or_None)], docs=(head, groups), means=(cols, rows, note, addr?), collect=[...], proc=[...])
GB_TABS = [
    {
        "id": "a",
        "title": ("Persons Aged 16 or Above (Applying in Baekhyeon Hwarang)", "만 16세 이상(백현화랑 특별행정구 내 신청)", "十六歲或以上人士（於柏峴화랑申請）"),
        "forms": [
            (("Application form (ID 841)", "신청서(ID 841)", "申請表格（ID 841）"), None),
            (("Fee payment form for Baekhyeon Hwarang SAR Passport to be collected outside Baekhyeon Hwarang (Form ID 853A) (For applicants who choose to collect the passport at the Korean Diplomatic and Consular Missions)",
              "백현화랑 특별행정구 밖에서 수령하는 백현화랑 특별행정구 여권 수수료 납부서(서식 ID 853A)(재외공관 수령을 선택한 신청인용)",
              "於柏峴화랑以外地區領取的柏峴화랑特別行政區護照費用繳費表格（表格ID 853A）（適用於選擇在大韓民國駐外使領館領取護照的申請人）"), None),
            (("Photograph", "사진", "照片"), _PHOTO),
        ],
        "docs": [
            (("Persons aged 16 or above", "만 16세 이상", "十六歲或以上人士"), [("(a) ", _IDCARD16)]),
            (_ADD1617, [("(b) ", _PARENTID),
                        ("(c) ", ("Birth certificate (not required if the applicant was born in Baekhyeon Hwarang) to prove his/her relationship with the consenting parent, or a court order, if applicable, to prove that the consenting legal guardian concerned has custodial rights in respect of him/her.",
                                  "동의하는 부모와의 관계를 증명하는 출생증명서(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 해당 법정대리인의 양육권을 증명하는 법원 명령서.",
                                  "出生證明書（如申請人在柏峴화랑出生則無需提交），以證明其與同意申請的父、母的關係；或法庭頒令（如適用），以證明有關合法監護人對其擁有管養權。")),
                        ("(d) ", (_MARRIED[0] % "(b) and (c)", _MARRIED[1] % "(b), (c)", _MARRIED[2] % "(b)及(c)"))]),
        ],
        "means": (_PAYCOLS_IN, _ROWS_IN, _NOTE_IN, True, True),
        "collect": [_COL_IN, _COL_KDCM],
        "proc": [(_PROC5, True), (_PROC_NOTE, False)],
    },
    {
        "id": "b",
        "title": ("Children Aged Under 16 (Applying in Baekhyeon Hwarang)", "만 16세 미만 아동(백현화랑 특별행정구 내 신청)", "十六歲以下兒童（於柏峴화랑申請）"),
        "forms": [
            (("Application form (ID 842)", "신청서(ID 842)", "申請表格（ID 842）"), None),
            (("Fee payment form for Baekhyeon Hwarang SAR Passport to be collected outside Baekhyeon Hwarang (ID 853A) (For applicants who choose to collect the passport at the Korean Diplomatic and Consular Missions)",
              "백현화랑 특별행정구 밖에서 수령하는 백현화랑 특별행정구 여권 수수료 납부서(ID 853A)(재외공관 수령을 선택한 신청인용)",
              "於柏峴화랑以外地區領取的柏峴화랑特別行政區護照費用繳費表格（ID 853A）（適用於選擇在大韓民國駐外使領館領取護照的申請人）"), None),
            (("Photograph", "사진", "照片"), _PHOTO),
        ],
        "docs": [
            (("Children aged under 16", "만 16세 미만 아동", "十六歲以下兒童"), [
                ("(a) ", ("The child's Baekhyeon Hwarang SAR permanent identity card / Acknowledgement of application for a Baekhyeon Hwarang SAR permanent identity card.",
                          "자녀의 백현화랑 특별행정구 영구 신분증 / 영구 신분증 신청 확인서.",
                          "該兒童的柏峴화랑永久性居民身份證／「申請柏峴화랑永久性居民身份證收據」。")),
                ("(b) ", _PARENTID),
                ("(c) ", ("The child's birth certificate (not required if the child was born in Baekhyeon Hwarang) to prove the relationship between the parent and the child, or a court order, if applicable, to prove that the consenting legal guardian concerned has custodial rights in respect of the child.",
                          "부모와 자녀의 관계를 증명하는 자녀의 출생증명서(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 해당 법정대리인의 양육권을 증명하는 법원 명령서.",
                          "該兒童的出生證明書（如兒童在柏峴화랑出生則無需提交），以證明父、母與該兒童的關係；或法庭頒令（如適用），以證明有關合法監護人對該兒童擁有管養權。"))]),
            (("Additional requirements for children aged under 11", "만 11세 미만 아동의 추가 요건", "十一歲以下兒童的額外規定"), [
                ("(d) ", ("School document (e.g. a Student's Handbook bearing the child's name, date of birth and photograph that should be certified by a chop of the school) or other proof of identity is required. If such school document or proof of identity is not available, a completed Form for Countersignature (ID 641) together with a photocopy of the countersignatory's Baekhyeon Hwarang SAR identity card or valid travel document(s) bearing the countersignatory's signature.",
                          "학교 서류(자녀의 이름·생년월일·사진이 있고 학교 직인이 찍힌 학생 수첩 등) 또는 기타 신원 증명서가 필요합니다. 이러한 서류가 없는 경우, 작성한 확인 서명 서식(ID 641)과 서명 확인인의 서명이 있는 백현화랑 특별행정구 신분증 또는 유효한 여행증명서 사본을 제출합니다.",
                          "須提交學校證明文件（例如載有兒童姓名、出生日期及照片，並經學校蓋印認證的學生手冊）或其他身份證明文件。若未能提供該等學校證明文件或身份證明，則須提交已填妥的副署事項表格（ID 641），以及載有副署人簽名的副署人柏峴화랑身份證或有效旅行證件副本。"))]),
            (("Additional requirements for children aged under 11 who do not hold Baekhyeon Hwarang SAR permanent identity cards", "백현화랑 특별행정구 영구 신분증이 없는 만 11세 미만 아동의 추가 요건", "未持有柏峴화랑永久性居民身份證的十一歲以下兒童的額外規定"), [
                ("(e) ", ("An additional photograph (two identical photographs should be submitted in total).", "사진 1장 추가(동일한 사진 총 2장 제출).", "額外照片一張（合共須提交兩張相同的照片）。")),
                ("(f) ", ("An application form (ROP 3) for a Baekhyeon Hwarang SAR permanent identity card, duly completed and signed by the parent or legal guardian of the child.",
                          "작성하고 부모 또는 법정대리인이 서명한 백현화랑 특별행정구 영구 신분증 신청서(ROP 3).",
                          "已填妥並由兒童的父、母或合法監護人簽署的柏峴화랑永久性居民身份證申請表格（ROP 3）。")),
                ("(g) ", ("Documents in support of the child's right of abode in the Baekhyeon Hwarang SAR (not required if applicant was born in Baekhyeon Hwarang).",
                          "자녀의 백현화랑 특별행정구 거주권을 증명하는 서류(백현화랑 특별행정구에서 출생한 경우 불필요).",
                          "證明該兒童擁有柏峴화랑特別行政區居留權的文件（如申請人在柏峴화랑出生則無需提交）。"))]),
        ],
        "means": (_PAYCOLS_IN, _ROWS_IN, _NOTE_IN, True, True),
        "collect": [_COL_IN, _COL_KDCM_CHILD],
        "proc": [(_PROC10, True), (_PROC_NOTE, False)],
    },
    {
        "id": "c",
        "title": ("Persons Aged 16 or Above (Applying outside Baekhyeon Hwarang)", "만 16세 이상(백현화랑 특별행정구 밖 신청)", "十六歲或以上人士（於柏峴화랑以外地區申請）"),
        "forms": [
            (("Application form (ID 843)", "신청서(ID 843)", "申請表格（ID 843）"), None),
            (("Fee Payment Form for Baekhyeon Hwarang SAR Passport (ID 853) (For applications submitted to the Korean Diplomatic and Consular Missions)",
              "백현화랑 특별행정구 여권 수수료 납부서(ID 853)(재외공관에 제출하는 신청용)",
              "柏峴화랑特別行政區護照費用繳費表格（ID 853）（適用於向大韓民國駐外使領館遞交的申請）"), None),
            (("Photograph", "사진", "照片"), _PHOTO3),
        ],
        "docs": [
            (("Persons aged 16 or above", "만 16세 이상", "十六歲或以上人士"), [
                ("(a) ", ("Baekhyeon Hwarang SAR permanent identity card / Acknowledgement of application for a Baekhyeon Hwarang SAR permanent identity card (applicable to application submitted directly to the Immigration Department).",
                          "백현화랑 특별행정구 영구 신분증 / 영구 신분증 신청 확인서(출입경사무처에 직접 제출하는 신청에 해당).",
                          "柏峴화랑永久性居民身份證／「申請柏峴화랑永久性居民身份證收據」（適用於直接向入境事務處遞交的申請）。")),
                ("(b) ", ("For first-time application for a passport, his/her previous Baekhyeon Hwarang SAR Document of Identity for Visa Purposes, if any.",
                          "여권을 처음 신청하는 경우, 이전에 발급받은 백현화랑 특별행정구 비자용 신분증명서(있는 경우).",
                          "首次申請護照者，其以往持有的柏峴화랑特別行政區簽證身份書（如有）。")),
                ("(c) ", ("For application for a replacement passport, his/her previous passport.",
                          "여권 교체 발급을 신청하는 경우, 이전 여권.",
                          "申請換領護照者，其以往持有的護照。"))]),
            (_ADD1617, [("(d) ", _PARENTID),
                        ("(e) ", ("Birth certificate (not required if the applicant was born in Baekhyeon Hwarang) to prove his/her relationship with the consenting parent, or a court order, if applicable, to prove that the consenting legal guardian concerned has custodial rights in respect of him/her.",
                                  "동의하는 부모와의 관계를 증명하는 출생증명서(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 해당 법정대리인의 양육권을 증명하는 법원 명령서.",
                                  "出生證明書（如申請人在柏峴화랑出生則無需提交），以證明其與同意申請的父、母的關係；或法庭頒令（如適用），以證明有關合法監護人對其擁有管養權。")),
                        ("(f) ", (_MARRIED[0] % "(d) and (e)", _MARRIED[1] % "(d), (e)", _MARRIED[2] % "(d)及(e)"))]),
        ],
        "means": (_PAYCOLS_OUT, _ROWS_OUT, _NOTE_OUT, False, True),
        "collect": [_COL_IN, _COL_KDCM],
        "proc": [(_PROC5, True), (_PROC_NOTE, False)],
    },
    {
        "id": "d",
        "title": ("Children Aged Under 16 (Applying outside Baekhyeon Hwarang)", "만 16세 미만 아동(백현화랑 특별행정구 밖 신청)", "十六歲以下兒童（於柏峴화랑以外地區申請）"),
        "forms": [
            (("Application form (ID 844)", "신청서(ID 844)", "申請表格（ID 844）"), None),
            (("Fee Payment Form for Baekhyeon Hwarang SAR Passport (ID 853) (For applications submitted to the Korean Diplomatic and Consular Missions)",
              "백현화랑 특별행정구 여권 수수료 납부서(ID 853)(재외공관에 제출하는 신청용)",
              "柏峴화랑特別行政區護照費用繳費表格（ID 853）（適用於向大韓民國駐外使領館遞交的申請）"), None),
            (("Photograph", "사진", "照片"), _PHOTO3),
        ],
        "docs": [
            (("Children aged under 16", "만 16세 미만 아동", "十六歲以下兒童"), [
                ("(a) ", ("The child's Baekhyeon Hwarang SAR permanent identity card / Acknowledgement of application for a Baekhyeon Hwarang SAR permanent identity card (applicable to application submitted directly to the Immigration Department).",
                          "자녀의 백현화랑 특별행정구 영구 신분증 / 영구 신분증 신청 확인서(출입경사무처에 직접 제출하는 신청에 해당).",
                          "該兒童的柏峴화랑永久性居民身份證／「申請柏峴화랑永久性居民身份證收據」（適用於直接向入境事務處遞交的申請）。")),
                ("(b) ", _PARENTID),
                ("(c) ", ("The child's birth certificate (not required if the child was born in Baekhyeon Hwarang) to prove the relationship between the parent and the child, or a court order, if applicable, to prove that the consenting legal guardian concerned has custodial rights in respect of the child.",
                          "부모와 자녀의 관계를 증명하는 자녀의 출생증명서(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 해당 법정대리인의 양육권을 증명하는 법원 명령서.",
                          "該兒童的出生證明書（如兒童在柏峴화랑出生則無需提交），以證明父、母與該兒童的關係；或法庭頒令（如適用），以證明有關合法監護人對該兒童擁有管養權。")),
                ("(d) ", ("For first-time application for a passport, the child's previous Baekhyeon Hwarang SAR Document of Identity for Visa Purposes, if any.",
                          "여권을 처음 신청하는 경우, 자녀가 이전에 발급받은 백현화랑 특별행정구 비자용 신분증명서(있는 경우).",
                          "首次申請護照者，該兒童以往持有的柏峴화랑特別行政區簽證身份書（如有）。")),
                ("(e) ", ("For application for a replacement passport, the child's previous passport.",
                          "여권 교체 발급을 신청하는 경우, 자녀의 이전 여권.",
                          "申請換領護照者，該兒童以往持有的護照。"))]),
            (("Additional requirements for children aged under 11", "만 11세 미만 아동의 추가 요건", "十一歲以下兒童的額外規定"), [
                ("(f) ", ("School document (e.g. a Student's Handbook bearing the child's name, date of birth and photograph that should be certified by a chop of the school) or other proof of identity is required. If such school document or proof of identity is not available, a completed Form for Countersignature (ID 641) together with a photocopy of the countersignatory's Baekhyeon Hwarang SAR identity card or valid travel document(s) bearing the countersignatory's signature.",
                          "학교 서류(자녀의 이름·생년월일·사진이 있고 학교 직인이 찍힌 학생 수첩 등) 또는 기타 신원 증명서가 필요합니다. 이러한 서류가 없는 경우, 작성한 확인 서명 서식(ID 641)과 서명 확인인의 서명이 있는 백현화랑 특별행정구 신분증 또는 유효한 여행증명서 사본을 제출합니다.",
                          "須提交學校證明文件（例如載有兒童姓名、出生日期及照片，並經學校蓋印認證的學生手冊）或其他身份證明文件。若未能提供該等學校證明文件或身份證明，則須提交已填妥的副署事項表格（ID 641），以及載有副署人簽名的副署人柏峴화랑身份證或有效旅行證件副本。"))]),
            (("Additional requirements for children aged under 11 who do not hold Baekhyeon Hwarang SAR permanent identity cards", "백현화랑 특별행정구 영구 신분증이 없는 만 11세 미만 아동의 추가 요건", "未持有柏峴화랑永久性居民身份證的十一歲以下兒童的額外規定"), [
                ("(g) ", ("An additional photograph (four identical photographs should be submitted in total).", "사진 1장 추가(동일한 사진 총 4장 제출).", "額外照片一張（合共須提交四張相同的照片）。")),
                ("(h) ", ("An application form (ROP 144) for a Baekhyeon Hwarang SAR permanent identity card, duly completed and signed by the parent or legal guardian of the child.",
                          "작성하고 부모 또는 법정대리인이 서명한 백현화랑 특별행정구 영구 신분증 신청서(ROP 144).",
                          "已填妥並由兒童的父、母或合法監護人簽署的柏峴화랑永久性居民身份證申請表格（ROP 144）。")),
                ("(i) ", ("Documents in support of the child's right of abode in the Baekhyeon Hwarang SAR.",
                          "자녀의 백현화랑 특별행정구 거주권을 증명하는 서류.",
                          "證明該兒童擁有柏峴화랑特別行政區居留權的文件。"))]),
        ],
        "means": (_PAYCOLS_OUT, _ROWS_OUT, _NOTE_OUT, False, True),
        "collect": [_COL_IN, _COL_KDCM_CHILD],
        "proc": [(_PROC10, True), (_PROC_NOTE, False)],
    },
]
GB_ADDR = _ADDR
GB_CRUMBS = [
    ("guides", ("Guidebooks", "안내서", "指南")),
    ("travel", ("Travel", "여행", "旅遊")),
    ("traveldocument", ("Travel Document", "여행증명서", "旅行證件")),
]
RELATED_LINKS = [
    ("Protection for Travellers Abroad", "해외 여행자 보호", "外遊旅客的保障"),
    ("Notes for Air Passengers", "항공 승객 안내", "飛機乘客須知"),
    ("Immigration Control Points", "출입경 관리소", "出入境管制站"),
    ("World Weather Information", "세계 날씨 정보", "世界天氣資訊"),
    ("Air Passenger Services", "항공 여객 서비스", "航空旅客服務"),
]
