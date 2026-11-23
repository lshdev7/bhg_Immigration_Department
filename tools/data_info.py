# -*- coding: utf-8 -*-
"""Informational pages that hang off the passport pages and the "Top Online Services" list.
Tuples are (English, Korean, Traditional Chinese). Block types: p h2 h3 ul ol btn link faq table plain strong."""

CUR = "BH$"

# ----------------------------------------------------------------------------- photograph requirements
PHOTO_TITLE = ("Photograph Requirements for Travel Document", "여행증명서 사진 규격", "旅行證件的照片規格")
PHOTO = [
    ("p", ("The photograph should show your full frontal face with clear facial features.", "사진에는 이목구비가 선명하게 보이는 정면 얼굴 전체가 나와야 합니다.", "照片須顯示你的整個正面面容，五官清晰。")),
    ("p", ("The photograph should have a plain white background.", "사진의 배경은 무늬 없는 흰색이어야 합니다.", "照片的背景須為白色，不得有圖案。")),
    ("p", ("The size of the photograph must be 40mm (width) X 50mm (height). The size from chin to crown for the person in the photograph should be 32mm to 36mm. There should be sufficient headroom.",
           "사진 크기는 가로 40mm × 세로 50mm여야 합니다. 사진 속 인물의 턱끝에서 정수리까지는 32mm~36mm여야 하며, 머리 위 여백이 충분해야 합니다.",
           "照片的尺寸必須為40毫米（闊）X 50毫米（高）。照片中人像由下巴至頭頂的長度應為32毫米至36毫米，頭頂上方須預留足夠空間。")),
    ("p", ("When you take the photograph, please do not wear head dress, and avoid heavy make-up and overly dark or overly light-coloured clothing.",
           "사진을 촬영할 때는 모자나 머리 장식을 착용하지 말고, 짙은 화장과 지나치게 어둡거나 밝은 색의 옷을 피해 주세요.",
           "拍攝照片時，請勿戴頭飾，並避免濃妝，以及穿著過深或過淺顏色的衣服。")),
    ("p", ("The photograph will not be accepted if the applicant in the photograph is:", "사진 속 신청인이 다음에 해당하면 사진이 접수되지 않습니다.", "如照片中的申請人有下列情況，照片將不獲接納：")),
    ("ul", [
        ("Not centred", "중앙에 위치하지 않은 경우", "沒有居中"),
        ("Wearing a frame across eyes", "안경테가 눈을 가로지르는 경우", "眼鏡框遮住眼睛"),
        ("With hair across eyes or eyebrows", "머리카락이 눈이나 눈썹을 가리는 경우", "頭髮遮住眼睛或眉毛"),
        ("Seen with flash reflection on face/glasses", "얼굴이나 안경에 플래시 반사가 있는 경우", "面部或眼鏡有閃光燈反光"),
        ("With shadow", "그림자가 있는 경우", "有陰影"),
        ("Too light", "너무 밝은 경우", "過亮"),
        ("Too dark", "너무 어두운 경우", "過暗"),
    ]),
    ("p", ("Your photograph will be personalised on the data page of your passport or Document of Identity for Visa Purposes by laser engraving. The quality of the image that appears on your passport or Document of Identity for Visa Purposes will depend on the quality and colour of the original photograph you furnish.",
           "제출한 사진은 여권 또는 비자용 신분증명서의 정보면에 레이저 각인으로 개인화됩니다. 여권이나 비자용 신분증명서에 나타나는 이미지의 품질은 제출한 원본 사진의 품질과 색상에 따라 달라집니다.",
           "你的照片將以激光雕刻方式印製在護照或簽證身份書的資料頁上。護照或簽證身份書上的影像質素，取決於你所提交的原本照片的質素及顏色。")),
    ("p", ("Please do not fold, staple, or write on the back of the photograph, or attach the photograph to the application form by paper clip. Otherwise, the photograph will become unsuitable for passport or Document of Identity for Visa Purposes personalisation.",
           "사진을 접거나 스테이플러로 찍거나 뒷면에 글씨를 쓰지 말고, 클립으로 신청서에 끼우지 마세요. 그렇게 하면 여권이나 비자용 신분증명서 개인화에 사용할 수 없게 됩니다.",
           "請勿摺疊照片、用釘書機釘照片、在照片背面書寫，亦勿以紙夾將照片夾在申請表格上，否則照片將不適合用作護照或簽證身份書的個人資料印製。")),
    ("p", ("An application submitted by post or drop-in with a substandard photograph will not be processed and will be returned to the applicant.",
           "규격에 맞지 않는 사진으로 우편 또는 직접 투입 방식으로 제출한 신청은 처리되지 않고 신청인에게 반송됩니다.",
           "以郵寄或投遞方式遞交而照片不符合規格的申請，將不獲處理，並會退還申請人。")),
    ("h2", ("Acceptable File Format of Digital Photograph Submitted through Internet and Mobile App of the Immigration Department (For passport application only)",
            "인터넷 및 출입경사무처 모바일 앱으로 제출하는 디지털 사진의 허용 파일 형식(여권 신청에 한함)",
            "透過互聯網及入境事務處流動應用程式遞交的數碼照片可接納的檔案格式（只適用於護照申請）")),
    ("plain", ("Image type: JPEG<br>File size: 5MB or below<br>Acceptable dimension:", "이미지 형식: JPEG<br>파일 크기: 5MB 이하<br>허용 규격:", "圖像類別：JPEG<br>檔案大小：5MB 或以下<br>合適尺寸：")),
    ("ul", [
        ("Captured by scanner (600dpi) - Photograph size: 40 mm(W) x 50 mm(H)", "스캐너(600dpi)로 촬영 - 사진 크기: 40mm(가로) x 50mm(세로)", "由掃瞄器（600dpi）擷取 – 照片大小：40毫米（闊）X 50毫米（高）"),
        ("Captured by digital camera - Image size: at least 1200 px(W) x 1600 px(H)", "디지털 카메라로 촬영 - 이미지 크기: 최소 1200px(가로) x 1600px(세로)", "由數碼相機擷取 – 圖像大小：最少1200像素（闊）X 1600像素（高）"),
    ]),
    ("p", ("Whether the successfully uploaded photograph meets the requirements has yet to be determined. If necessary, we may request you to submit another photograph to process your application.",
           "업로드에 성공했더라도 사진이 규격을 충족하는지는 별도로 확정됩니다. 필요한 경우 신청 처리를 위해 사진을 다시 제출하도록 요청할 수 있습니다.",
           "成功上載的照片是否符合規格仍有待確定。如有需要，本處可能要求你提交另一張照片，以便處理你的申請。")),
]

# ----------------------------------------------------------------------------- online payment FAQ
PAYFAQ_TITLE = ("Online Payment", "온라인 결제", "網上付款")
PAYFAQ = [
    ("faq", [
        (("Will my online payments for government e-services be affected if my computer has Internet security software installed?",
          "컴퓨터에 인터넷 보안 소프트웨어가 설치되어 있으면 정부 전자서비스 온라인 결제에 영향이 있나요?",
          "如我的電腦安裝了互聯網保安軟件，會否影響我使用政府電子服務的網上付款？"),
         ("Given the wide spectrum of functionality of the Internet security software on the market, there is no definite answer to this question. In some cases a window may prompt you to switch to a protection mode during the payment process of some government e-services. If the protection mode is on, the system may display an error message [PAY-E-0000]. We recommend that you add government e-service webpages to the trusted list of your security software before using the online payment function. If you encounter other problems, please contact the corresponding departments for further support.",
          "시중에 나와 있는 인터넷 보안 소프트웨어의 기능이 매우 다양해 일률적으로 답하기는 어렵습니다. 일부 정부 전자서비스의 결제 과정에서 보호 모드로 전환하라는 창이 나타날 수 있으며, 보호 모드가 켜져 있으면 오류 메시지 [PAY-E-0000]이 표시될 수 있습니다. 온라인 결제 기능을 사용하기 전에 정부 전자서비스 웹페이지를 보안 소프트웨어의 신뢰 목록에 추가하시기 바랍니다. 다른 문제가 있으면 해당 기관에 문의해 주세요.",
          "由於市面上互聯網保安軟件的功能種類繁多，本處未能提供肯定的答案。在使用部分政府電子服務的付款過程中，可能會彈出視窗，提示你切換至保護模式；如保護模式已開啟，系統可能顯示錯誤訊息 [PAY-E-0000]。我們建議你在使用網上付款功能前，先將政府電子服務網頁加入保安軟件的信任清單。如遇其他問題，請聯絡相關部門尋求協助。")),
        (("How do I pay for GovBHG online services?", "정부포털 BHG의 온라인 서비스 요금은 어떻게 내나요?", "我如何繳付「BHG政府一站通」網上服務的費用？"),
         ("GovBHG online services generally accept credit cards and OPS (Online Payment Service) payment. To provide more payment options for settlement of fees for online services, instant bank transfer and mobile wallets are also supported for selected services.",
          "정부포털 BHG의 온라인 서비스는 일반적으로 신용카드와 OPS(온라인 결제 서비스)를 받습니다. 온라인 서비스 요금 납부 수단을 늘리기 위해 일부 서비스에서는 계좌 간편이체와 모바일 지갑도 지원합니다.",
          "「BHG政府一站通」網上服務一般接受信用卡及網上繳費服務（OPS）付款。為提供更多繳費選擇，部分服務亦支援即時轉賬及流動錢包。")),
        (("Who will receive my credit card or OPS information when I enter it for a GovBHG online service?",
          "정부포털 BHG 온라인 서비스에 신용카드나 OPS 정보를 입력하면 누가 그 정보를 받나요?",
          "我在「BHG政府一站通」網上服務輸入信用卡或網上繳費服務資料時，誰會收到這些資料？"),
         ("Your credit card or OPS information is captured by the payment service provider (e.g. a credit card acquiring bank). GovBHG and the Government bureau or department that offers the GovBHG online service cannot access such information.",
          "신용카드나 OPS 정보는 결제 서비스 제공업체(예: 카드 매입 은행)가 수집합니다. 정부포털 BHG와 해당 온라인 서비스를 제공하는 정부 부처·기관은 그 정보에 접근할 수 없습니다.",
          "你的信用卡或網上繳費服務資料由付款服務供應商（例如信用卡收單銀行）收取。「BHG政府一站通」及提供該網上服務的政府決策局或部門均無法取得這些資料。")),
        (("What should I do if my browser does not respond during the payment process?", "결제 과정에서 브라우저가 응답하지 않으면 어떻게 해야 하나요?", "如在付款過程中瀏覽器沒有反應，我應怎樣做？"),
         ("The screen that prompts you to select payment method provides a Transaction Reference Number (TRN), with which you could check the status of your payment if you encounter any problems during the payment process. Individual services provide an online function for you to enquire about the status of your payment. Alternatively, you can contact the Help Desk of the service for assistance. Please ensure that your first payment has not been effected before proceeding to make a second attempt.",
          "결제 수단을 선택하는 화면에는 거래 참조번호(TRN)가 표시되며, 결제 중 문제가 생기면 이 번호로 결제 상태를 확인할 수 있습니다. 서비스에 따라 결제 상태를 조회하는 온라인 기능이 있으며, 해당 서비스의 헬프데스크에 문의할 수도 있습니다. 두 번째 결제를 시도하기 전에 첫 번째 결제가 이루어지지 않았는지 반드시 확인해 주세요.",
          "提示你選擇付款方法的畫面會顯示交易參考編號（TRN）。如在付款過程中遇到任何問題，你可憑此編號查詢付款狀況。個別服務設有網上功能供你查詢付款狀況，你亦可聯絡該項服務的服務台尋求協助。在再次嘗試付款前，請確保首次付款並未成功。")),
        (("How do I find out if the Government has received my payment for the online service?", "정부가 온라인 서비스 결제를 받았는지 어떻게 확인하나요?", "我如何得知政府是否已收到我就網上服務所作的付款？"),
         ("After completing an online service, you should print and retain the acknowledgement page, which contains key information about the transaction or a reference number that allows you to check the transaction status with the relevant Government bureau or department when necessary.",
          "온라인 서비스를 마친 후에는 거래의 주요 정보 또는 해당 정부 부처·기관에서 거래 상태를 확인할 때 쓸 수 있는 참조번호가 담긴 확인 페이지를 인쇄해 보관하시기 바랍니다.",
          "完成網上服務後，你應列印並保存確認頁。確認頁載有交易的重要資料或參考編號，需要時可憑此向有關政府決策局或部門查詢交易狀況。")),
        (("How do I make OPS payments for GovBHG online services? Do I need to register?", "정부포털 BHG 온라인 서비스에서 OPS로 결제하려면 어떻게 하나요? 등록해야 하나요?", "我如何以網上繳費服務（OPS）繳付「BHG政府一站通」網上服務的費用？需要登記嗎？"),
         ("When you make online OPS payments, you will need to input both your OPS account number and your OPS Internet password for each payment. Please visit the OPS website to find out how to register for an OPS Internet password, as well as details on browser compatibility and other technical information.",
          "OPS로 온라인 결제할 때는 결제할 때마다 OPS 계좌번호와 OPS 인터넷 비밀번호를 모두 입력해야 합니다. OPS 인터넷 비밀번호 등록 방법과 브라우저 호환성 등 기술 정보는 OPS 웹사이트에서 확인하세요.",
          "以網上繳費服務（OPS）付款時，每次付款均須輸入OPS帳戶號碼及OPS互聯網密碼。有關登記OPS互聯網密碼的方法，以及瀏覽器兼容性等技術資料，請瀏覽OPS網站。")),
        (("Does my computer system need to be of any specific configuration to perform credit card payments for GovBHG online services?",
          "정부포털 BHG 온라인 서비스의 신용카드 결제에 특별한 컴퓨터 환경이 필요한가요?",
          "我的電腦系統是否須有特定配置，才可以信用卡繳付「BHG政府一站通」網上服務的費用？"),
         ("There is generally no system requirement. You are advised to check with your credit card issuer if they have imposed any other specific system requirements.",
          "일반적으로 시스템 요건은 없습니다. 카드 발급사가 별도의 시스템 요건을 두고 있는지는 카드 발급사에 확인하시기 바랍니다.",
          "一般沒有系統要求。你可向信用卡發卡機構查詢，是否另有特定的系統要求。")),
        (("I failed to make a payment when I was using a GovBHG online service. The error message code was \"PAY-E-9017\". What should I do?",
          "정부포털 BHG 온라인 서비스 이용 중 결제에 실패했고 오류 코드가 \"PAY-E-9017\"입니다. 어떻게 해야 하나요?",
          "我使用「BHG政府一站通」網上服務時付款失敗，錯誤訊息編號為「PAY-E-9017」，我應怎樣做？"),
         ("The GovBHG payment system makes use of the certificates issued by the Baekhyeon Hwarang Post and your browser cannot recognise these certificates. Please download and install the Baekhyeon Hwarang Post Root CA Certificates. If the problem persists after installing the certificates, please report the problem to the GovBHG Help Desk.",
          "정부포털 BHG 결제 시스템은 백현화랑 우정국이 발급한 인증서를 사용하는데 브라우저가 이 인증서를 인식하지 못한 경우입니다. 백현화랑 우정국 루트 CA 인증서를 내려받아 설치하세요. 설치 후에도 문제가 계속되면 정부포털 BHG 헬프데스크에 알려 주세요.",
          "「BHG政府一站通」的付款系統使用柏峴화랑郵政署發出的證書，而你的瀏覽器無法識別這些證書。請下載並安裝柏峴화랑郵政署根證書。如安裝後問題仍然存在，請向「BHG政府一站通」服務台報告。")),
        (("If the Government needs to refund to me the money that I paid via online payment, how will the refund be made?", "온라인으로 낸 돈을 정부가 환불해야 할 경우 어떻게 환불되나요?", "如政府須退還我以網上付款方式繳付的款項，會如何退款？"),
         ("If the payment is paid by OPS, the department will normally issue a refund cheque to you. If the payment is made by credit card online, normally, refund can only be made to the credit card account that was used for the payment. Please note that if your credit card account has been cancelled when the refund is made, some card issuing banks may charge you for an administration fee before you can get back the money. It is not possible for the Government to check whether your credit card account is still active before making the refund because the Government does not know your credit card number.",
          "OPS로 결제했다면 해당 기관이 보통 환불 수표를 발행합니다. 신용카드로 온라인 결제했다면 일반적으로 결제에 사용한 카드 계좌로만 환불할 수 있습니다. 환불 시점에 카드 계좌가 해지되어 있으면 일부 카드 발급 은행이 돈을 돌려주기 전에 수수료를 부과할 수 있습니다. 정부는 카드 번호를 알지 못하므로 환불 전에 카드 계좌가 유효한지 확인할 수 없습니다.",
          "如以網上繳費服務（OPS）付款，有關部門一般會向你發出退款支票。如以信用卡在網上付款，一般只能退款至用作付款的信用卡帳戶。請注意，如退款時你的信用卡帳戶已被取消，部分發卡銀行可能會在你取回款項前收取手續費。由於政府並不知道你的信用卡號碼，因此無法在退款前查核你的信用卡帳戶是否仍然有效。")),
        (("When I use my credit card for payment, why am I sometimes required to enter a password for authentication and sometimes not?",
          "신용카드로 결제할 때 어떤 때는 인증 비밀번호를 입력하라고 하고 어떤 때는 그렇지 않은 이유는 무엇인가요?",
          "我以信用卡付款時，為何有時須輸入密碼認證，有時則不須？"),
         ("Visa, Mastercard and JCB offer additional security mechanism to give their cardholders extra protection when they make online payments. More details are available from the websites of the card organisations.",
          "Visa, Mastercard, JCB는 온라인 결제 시 카드 소지자를 추가로 보호하기 위한 보안 체계를 운영합니다. 자세한 내용은 각 카드 회사의 웹사이트에서 확인할 수 있습니다。".replace("。", "."),
          "Visa、萬事達卡及JCB設有額外的保安機制，在持卡人進行網上付款時提供更多保障。詳情請瀏覽有關信用卡機構的網站。")),
    ]),
]

# ----------------------------------------------------------------------------- passport fees
FEES_TITLE = ("Fee Tables", "수수료표", "收費表")
_HDR = (("Item", "항목", "項目"), ("Fees", "수수료", "費用"))
FEES = [
    ("h2", ("Travel Documents", "여행증명서", "旅行證件")),
    ("h3", ("Local Application", "특별행정구 내 신청", "於本地申請")),
    ("table", [("No.", "번호", "編號"), ("Item", "항목", "項目"), ("Fees", "수수료", "費用")], [
        (("1.", "1.", "1."), ("Baekhyeon Hwarang Special Administrative Region (Baekhyeon Hwarang SAR) Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照"), ("", "", "")),
        (("(a)", "(a)", "(a)"), ("For persons aged 16 or above (valid for 10 years)", "만 16세 이상(유효기간 10년)", "十六歲或以上人士（有效期10年）"), ("32 pages – BH$430<br>48 pages – BH$520", "32쪽 – BH$430<br>48쪽 – BH$520", "32頁 – BH$430<br>48頁 – BH$520")),
        (("(b)", "(b)", "(b)"), ("For children aged under 16 (valid for 5 years)", "만 16세 미만 아동(유효기간 5년)", "十六歲以下兒童（有效期5年）"), ("32 pages – BH$215<br>48 pages – BH$260", "32쪽 – BH$215<br>48쪽 – BH$260", "32頁 – BH$215<br>48頁 – BH$260")),
        (("(c)", "(c)", "(c)"), ("Amendment of Baekhyeon Hwarang SAR Passport, for each application (including amendment of personal particulars or photograph)", "여권 정정(인적사항 또는 사진 정정 포함), 신청 건당", "修改護照，每宗申請（包括修改個人資料或照片）"), ("BH$110", "BH$110", "BH$110")),
        (("(d)", "(d)", "(d)"), ("Cross link passports (making on both the previous passport and the replacement passport an endorsement)", "여권 연계 표기(이전 여권과 교체 여권 양쪽에 표기)", "連繫護照（在舊護照及換領的護照上互相加註）"), ("BH$200", "BH$200", "BH$200")),
        (("2.", "2.", "2."), ("Multiple Baekhyeon Hwarang SAR Re-entry Permit (whether of full or restricted validity)", "복수 재입경 허가증(완전·제한 유효기간 모두)", "多次有效回港證（不論全期或限期有效）"), ("BH$210", "BH$210", "BH$210")),
        (("3.", "3.", "3."), ("Baekhyeon Hwarang SAR Re-entry Permit valid for 1 visit", "1회 유효 재입경 허가증", "一次有效回港證"), ("BH$70", "BH$70", "BH$70")),
        (("4.", "4.", "4."), ("Baekhyeon Hwarang SAR Document of Identity valid for 7 years (44-page)", "유효기간 7년 비자용 신분증명서(44쪽)", "有效期7年的簽證身份書（44頁）"), ("BH$325", "BH$325", "BH$325")),
        (("5.", "5.", "5."), ("Baekhyeon Hwarang SAR Document of Identity valid for 7 years (92-page)", "유효기간 7년 비자용 신분증명서(92쪽)", "有效期7年的簽證身份書（92頁）"), ("BH$450", "BH$450", "BH$450")),
    ]),
    ("h3", ("Surcharges (additional charge for the delivery of Baekhyeon Hwarang SAR passport)", "추가 요금(특별행정구 여권 배송 추가 요금)", "附加費（遞送護照的額外費用）")),
    ("p", ("An additional charge for the delivery of passport is required if applicant chooses to collect the passport at the Korean Diplomatic and Consular Missions.",
           "재외공관에서 여권을 수령하기로 선택한 경우 여권 배송에 대한 추가 요금이 부과됩니다.",
           "如申請人選擇在大韓民國駐外使領館領取護照，須繳付遞送護照的額外費用。")),
    ("table", [("No.", "번호", "編號"), ("Item", "항목", "項目"), ("Fees", "수수료", "費用")], [
        (("(a)", "(a)", "(a)"), ("Delivery by double registered air mail", "이중 등기 항공우편 배송", "以雙掛號航空郵件遞送"), ("BH$50 (or US$6.5)", "BH$50(또는 US$6.5)", "BH$50（或US$6.5）")),
        (("(b)", "(b)", "(b)"), ("Delivery by express dispatch service", "특급 배송 서비스", "以速遞服務遞送"), ("Asia-Pacific – BH$210 (or US$27)<br>North America and Europe – BH$310 (or US$40)<br>Other areas – BH$300 (or US$38.5)", "아시아·태평양 – BH$210(또는 US$27)<br>북미·유럽 – BH$310(또는 US$40)<br>기타 지역 – BH$300(또는 US$38.5)", "亞太區 – BH$210（或US$27）<br>北美洲及歐洲 – BH$310（或US$40）<br>其他地區 – BH$300（或US$38.5）")),
        (("(c)", "(c)", "(c)"), ("Bank handling charge (if the cheque or bank draft is not drawn on a bank in Baekhyeon Hwarang or not in Baekhyeon Hwarang currency)", "은행 취급 수수료(수표나 은행 어음이 백현화랑 내 은행 발행이 아니거나 백현화랑 통화가 아닌 경우)", "銀行手續費（如支票或銀行匯票並非由柏峴화랑的銀行發出，或並非柏峴화랑貨幣）"), ("BH$250 (or US$32.5)", "BH$250(또는 US$32.5)", "BH$250（或US$32.5）")),
    ]),
    ("p", ("* The fees are payable in Baekhyeon Hwarang Dollars (BH$), the currency issued by the Baekhyeon Hwarang Monetary Authority.",
           "* 수수료는 백현화랑 금융관리국이 발행하는 통화인 백현화랑달러(BH$)로 납부합니다.",
           "* 費用以柏峴화랑金融管理局發行的貨幣柏峴화랑元（BH$）繳付。")),
]

# ----------------------------------------------------------------------------- Passport FAQ
FAQ_TITLE = ("Frequently Asked Questions - Travel Documents", "자주 묻는 질문 - 여행증명서", "常見問題 - 旅行證件")
FAQ = [
    ("h2", ("Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照")),
    ("faq", [
        (("Am I eligible for a Baekhyeon Hwarang SAR Passport?", "백현화랑 특별행정구 여권을 신청할 자격이 있나요?", "我是否符合資格申請柏峴화랑特別行政區護照？"),
         ("A Korean citizen who is a permanent resident of Baekhyeon Hwarang and holds a valid Baekhyeon Hwarang permanent identity card is eligible to apply for a Baekhyeon Hwarang SAR Passport.",
          "유효한 백현화랑 영구 신분증을 소지한 백현화랑 영주권자인 대한민국 국민은 백현화랑 특별행정구 여권을 신청할 수 있습니다.",
          "持有有效柏峴화랑永久性居民身份證的柏峴화랑永久性居民，如屬大韓民國國民，便符合資格申請柏峴화랑特別行政區護照。")),
        (("How long does it take to get a Baekhyeon Hwarang SAR Passport?", "백현화랑 특별행정구 여권을 받기까지 얼마나 걸리나요?", "領取柏峴화랑特別行政區護照需時多久？"),
         ("The Immigration Department pledges to complete processing within 5 working days after receipt of all necessary documents, application fee and photograph. For applications through the Internet, an extra 2 to 3 working days may be required. For children aged under 11 not holding a permanent identity card, it takes 10 working days.",
          "출입경사무처는 필요한 서류, 수수료 및 사진이 모두 접수된 후 5근무일 이내에 처리를 마치는 것을 목표로 합니다. 인터넷 신청은 2~3근무일이 추가될 수 있으며, 영구 신분증이 없는 만 11세 미만 아동은 10근무일이 걸립니다.",
          "入境事務處承諾於收妥全部所需文件、申請費用及照片後的5個工作天內完成處理。透過互聯網申請，可能需額外2至3個工作天；未持有永久性居民身份證的十一歲以下兒童，則需10個工作天。")),
        (("Can I ask to include my child in my passport?", "자녀를 제 여권에 함께 등록할 수 있나요?", "我可否要求把子女列入我的護照？"),
         ("No. Each person must hold his/her own passport. A child, regardless of age, must apply for his/her own passport.",
          "아니요. 모든 사람은 자신의 여권을 가져야 하며, 자녀도 나이와 관계없이 본인 명의의 여권을 신청해야 합니다.",
          "不可以。每個人均須持有本人的護照，兒童不論年齡，均須申請本人的護照。")),
        (("What are the features of the Baekhyeon Hwarang SAR Passport?", "백현화랑 특별행정구 여권의 특징은 무엇인가요?", "柏峴화랑特別行政區護照有甚麼特點？"),
         ("The passport complies with the standard of the International Civil Aviation Organization (ICAO). It is an electronic passport with a contactless chip, a polycarbonate data page with the holder's laser-engraved photograph, and multiple security features. It is available in 32-page and 48-page versions.",
          "이 여권은 국제민간항공기구(ICAO) 기준에 부합합니다. 비접촉식 칩이 내장된 전자여권이며, 소지자의 사진이 레이저로 각인된 폴리카보네이트 정보면과 여러 보안 요소를 갖추고 있습니다. 32쪽과 48쪽 두 종류가 있습니다.",
          "護照符合國際民航組織（ICAO）的標準，屬電子護照，內置非接觸式晶片，資料頁為聚碳酸酯材質並以激光雕刻持有人照片，設有多項防偽特徵，並有32頁及48頁兩種。")),
        (("How to apply for a Baekhyeon Hwarang SAR Passport?", "백현화랑 특별행정구 여권은 어떻게 신청하나요?", "如何申請柏峴화랑特別行政區護照？"),
         ("You may apply through the Internet or the Immigration Department Mobile Application, or make an appointment online and submit your application in person at the Immigration Headquarters or any of the Immigration Branch Offices.",
          "인터넷 또는 출입경사무처 모바일 앱으로 신청하거나, 온라인으로 예약한 뒤 출입경사무처 본부나 지소를 직접 방문해 신청할 수 있습니다.",
          "你可透過互聯網或入境事務處流動應用程式申請，或在網上預約後，親身到入境事務處總部或任何一間分區辦事處遞交申請。")),
        (("Does the successful submission of passport application through the Internet or Immigration Department Mobile Application mean that my application is approved?",
          "인터넷이나 출입경사무처 모바일 앱으로 여권 신청을 제출했다면 신청이 승인된 것인가요?",
          "透過互聯網或入境事務處流動應用程式成功遞交護照申請，是否代表申請已獲批准？"),
         ("No. Successful submission only means that the Immigration Department has received your application. Your application will be processed after the Department has received all necessary documents, the photograph and the fee. You will be notified of the result and the collection arrangements.",
          "아니요. 제출에 성공했다는 것은 출입경사무처가 신청을 접수했다는 뜻일 뿐입니다. 필요한 서류, 사진 및 수수료를 모두 받은 후에 처리가 시작되며, 결과와 수령 방법은 별도로 안내됩니다.",
          "不是。成功遞交只代表入境事務處已收到你的申請。待收妥所需文件、照片及費用後，本處才會處理你的申請，並會通知你結果及領證安排。")),
        (("Do I need to make an appointment for collection of my new passport?", "새 여권을 수령하려면 예약이 필요한가요?", "領取新護照是否須預約？"),
         ("No appointment is required. You may collect your new passport at the selected office during the collection period stated in the Collection Notice.",
          "예약은 필요하지 않습니다. 수령 통지서에 적힌 수령 기간에 선택한 사무소에서 새 여권을 수령하면 됩니다.",
          "無須預約。你可在領證通知所列的領證期限內，到所選定的辦事處領取新護照。")),
        (("How can I apply for amendment to my personal particulars in the passport?", "여권의 인적사항을 정정하려면 어떻게 해야 하나요?", "我如何申請修改護照上的個人資料？"),
         ("Please make an appointment online and submit the application form for amendment together with supporting documents and your passport at the Immigration Headquarters or any of the Immigration Branch Offices. A fee applies.",
          "온라인으로 예약한 후 정정 신청서, 증빙서류 및 여권을 지참하여 출입경사무처 본부나 지소에서 신청하세요. 수수료가 부과됩니다.",
          "請在網上預約後，攜同修改申請表格、證明文件及護照，到入境事務處總部或任何一間分區辦事處辦理。須繳付費用。")),
        (("How can I apply for replacement of passport due to loss?", "여권을 분실한 경우 재발급은 어떻게 신청하나요?", "護照遺失後，我如何申請補領？"),
         ("Please report the loss to the Police and the Immigration Department as soon as possible, then make an appointment and apply for a replacement passport in person. The lost passport will be invalidated.",
          "분실 사실을 가능한 한 빨리 경찰과 출입경사무처에 신고한 뒤, 예약하여 직접 방문해 재발급을 신청하세요. 분실한 여권은 무효 처리됩니다.",
          "請盡快向警方及入境事務處報失，然後預約並親身申請補領護照。遺失的護照將會失效。")),
        (("What should I do if I lost my passport while travelling abroad?", "해외 여행 중 여권을 분실했다면 어떻게 해야 하나요?", "如在外遊期間遺失護照，我應怎樣做？"),
         ("Please report the loss to the local police and contact the nearest Korean Diplomatic and Consular Mission for assistance as soon as possible.",
          "현지 경찰에 신고하고 가능한 한 빨리 가까운 대한민국 재외공관에 연락해 도움을 받으세요.",
          "請向當地警方報失，並盡快聯絡就近的大韓民國駐外使領館尋求協助。")),
        (("Children under 11 years of age are not required to hold identity cards. How can they apply for a passport?",
          "만 11세 미만 아동은 신분증을 소지하지 않아도 되는데, 여권은 어떻게 신청하나요?",
          "十一歲以下兒童無須持有身份證，他們如何申請護照？"),
         ("The parent or legal guardian may apply on behalf of the child with the child's birth certificate and other supporting documents, and complete the application for a permanent identity card at the same time where applicable.",
          "부모 또는 법정대리인이 자녀의 출생증명서와 기타 증빙서류를 갖추어 대리 신청할 수 있으며, 해당되는 경우 영구 신분증 신청도 함께 진행합니다.",
          "父、母或合法監護人可攜同兒童的出生證明書及其他證明文件代為申請，如適用，須同時辦理永久性居民身份證的申請。")),
        (("What is Passport Collection Kiosk / Personal Documentation Collection Kiosk?", "여권 수령 키오스크 / 개인 증명서류 수령 키오스크란 무엇인가요?", "領取護照服務站／領取個人證件服務站是甚麼？"),
         ("They are self-service kiosks that allow eligible applicants to collect their new passports by fingerprint verification, without queuing at a counter. See the page on collection via kiosks for details.",
          "자격이 되는 신청인이 창구에서 줄을 서지 않고 지문 인증으로 새 여권을 직접 수령할 수 있는 무인 키오스크입니다. 자세한 내용은 키오스크 수령 안내 페이지를 참고하세요.",
          "這是自助服務站，合資格的申請人可透過指紋核實，無須在櫃枱排隊便可領取新護照。詳情請參閱使用服務站領取護照的頁面。")),
    ]),
]

# ----------------------------------------------------------------------------- Kiosk collection
KIOSK_TITLE = ("Collection of Baekhyeon Hwarang SAR passport via Passport Collection Kiosk / Personal Documentation Collection Kiosk",
               "여권 수령 키오스크 / 개인 증명서류 수령 키오스크를 이용한 백현화랑 특별행정구 여권 수령",
               "使用領取護照服務站／領取個人證件服務站領取柏峴화랑特別行政區護照")
KIOSK = [
    ("p", ("Applicants aged 18 or above may choose to collect their Baekhyeon Hwarang SAR passports in person at Passport Collection Kiosk / Personal Documentation Collection Kiosk (PDCK) when they submit their applications.",
           "만 18세 이상 신청인은 신청서를 제출할 때 여권 수령 키오스크 / 개인 증명서류 수령 키오스크(PDCK)에서 직접 여권을 수령하는 방법을 선택할 수 있습니다.",
           "十八歲或以上的申請人在遞交申請時，可選擇親身到領取護照服務站／領取個人證件服務站（PDCK）領取柏峴화랑特別行政區護照。")),
    ("p", ("Please note that applicant is not eligible to use this service if he/she:", "다음에 해당하는 신청인은 이 서비스를 이용할 수 없습니다.", "請注意，如申請人有下列情況，則不能使用此項服務：")),
    ("ul", [
        ("is a holder of a damaged / non-electronic Baekhyeon Hwarang SAR passport or Baekhyeon Hwarang SAR Document of Identity for Visa Purposes (Doc/I); or", "훼손되었거나 전자식이 아닌 특별행정구 여권 또는 비자용 신분증명서(Doc/I)를 소지한 경우, 또는", "持有損毀／非電子的柏峴화랑特別行政區護照或簽證身份書（Doc/I）；或"),
        ("is a holder of a 92-page Baekhyeon Hwarang SAR Doc/I.", "92쪽 비자용 신분증명서(Doc/I)를 소지한 경우.", "持有92頁的柏峴화랑特別行政區簽證身份書（Doc/I）。"),
    ]),
    ("p", ("The collection arrangement will be sent by Short Message Service (SMS) notification prior to the collection period. Applicant is therefore advised to provide a mobile phone number subscribed with SMS. Depending on the circumstances, applicants may still be required to collect the passports at collection counter.",
           "수령 방법은 수령 기간 전에 문자메시지(SMS)로 안내되므로 SMS를 수신할 수 있는 휴대전화 번호를 제공해 주시기 바랍니다. 상황에 따라 창구에서 여권을 수령해야 할 수도 있습니다.",
           "有關領證安排將於領證期限前以短訊方式通知，因此申請人需提供可接收短訊的流動電話號碼。視乎實際情況，申請人或仍須到領證櫃位領取護照。")),
    ("h2", ("Documentary Requirements", "필요 서류", "所需的文件")),
    ("p", ("The applicant must collect the new passport in person via Passport Collection Kiosk / Personal Documentation Collection Kiosk at the selected Immigration Office by producing the following documents:",
           "신청인은 선택한 출입경사무소의 여권 수령 키오스크 / 개인 증명서류 수령 키오스크에서 다음 서류를 제시하고 새 여권을 직접 수령해야 합니다.",
           "申請人必須親身到所選定的入境事務辦事處，透過領取護照服務站／領取個人證件服務站領取新護照，並出示下列文件：")),
    ("ul", [
        ("His/Her Baekhyeon Hwarang permanent identity card; and", "본인의 백현화랑 영구 신분증, 그리고", "其柏峴화랑永久性居民身份證；及"),
        ("His/Her previous Baekhyeon Hwarang SAR passport or Doc/I (if applicable) for cancellation.", "말소할 이전 특별행정구 여권 또는 Doc/I(해당되는 경우).", "其以往持有的柏峴화랑特別行政區護照或簽證身份書（如適用），以供註銷。"),
    ]),
    ("h2", ("Office Location and Service Hours", "사무소 위치 및 서비스 시간", "辦事處地點及服務時間")),
    ("table", [("Office Location", "사무소 위치", "辦事處地點"), ("Number of Passport Collection Kiosks", "여권 수령 키오스크 수", "領取護照服務站數目"), ("Number of Personal Documentation Collection Kiosks#", "개인 증명서류 수령 키오스크 수#", "領取個人證件服務站數目#"), ("Working Hours of Offices*", "사무소 근무 시간*", "辦事處辦公時間*")], [
        (("Immigration Headquarters - Personal Documentation Self-services", "출입경사무처 본부 - 개인 증명서류 셀프서비스", "入境事務處總部 – 個人證件自助服務"), ("-", "-", "-"), ("10", "10", "10"), ("8:45am - 10:00pm (Mon - Fri)<br>9:00am - 10:00pm (Sat)", "오전 8:45 ~ 오후 10:00 (월~금)<br>오전 9:00 ~ 오후 10:00 (토)", "上午8時45分至晚上10時（星期一至五）<br>上午9時至晚上10時（星期六）")),
        (("Immigration - Baekhyeon Maeul Complex 3 Branch Office", "출입경사무처 - 백현마을 3단지 지소", "入境事務處 – 柏峴마을3社區分區辦事處"), ("4", "4", "4"), ("-", "-", "-"), ("9:00am - 4:30pm (Mon - Fri)<br>9:00am - 12:30pm (Sat)", "오전 9:00 ~ 오후 4:30 (월~금)<br>오전 9:00 ~ 낮 12:30 (토)", "上午9時至下午4時30分（星期一至五）<br>上午9時至中午12時30分（星期六）")),
        (("Immigration - Baekhyeon Maeul Complex 4 Branch Office", "출입경사무처 - 백현마을 4단지 지소", "入境事務處 – 柏峴마을4社區分區辦事處"), ("2", "2", "2"), ("-", "-", "-"), ("9:00am - 12:45pm & 2:00pm - 4:30pm (Mon - Fri)<br>9:00am - 12:30pm (Sat)", "오전 9:00 ~ 낮 12:45, 오후 2:00 ~ 4:30 (월~금)<br>오전 9:00 ~ 낮 12:30 (토)", "上午9時至中午12時45分及下午2時至4時30分（星期一至五）<br>上午9時至中午12時30分（星期六）")),
    ]),
    ("p", ("*All offices are closed on Sundays and public holidays. # Personal Documentation Collection Kiosks also provide collection of identity card and one-stop collection of identity card and passport services at the same time.",
           "*모든 사무소는 일요일과 공휴일에 휴무입니다. # 개인 증명서류 수령 키오스크는 신분증 수령과 신분증·여권 원스톱 수령 서비스도 함께 제공합니다.",
           "*所有辦事處在星期日及公眾假期休息。#領取個人證件服務站亦同時提供領取身份證及一併領取身份證和護照的服務。")),
    ("h2", ("Collection Procedures", "수령 절차", "領取程序")),
    ("table", [("Procedures", "순서", "步驟"), ("Description", "내용", "說明")], [
        (("1", "1", "1"), ("Place your Baekhyeon Hwarang identity card according to the instructions (new Smart ID card holder: place the card onto the document reader; Smart ID card holder: insert the card into the card reader)", "안내에 따라 백현화랑 신분증을 놓습니다(새 스마트 신분증: 문서 리더기에 올려놓기, 스마트 신분증: 카드 리더기에 삽입)", "按指示放置柏峴화랑身份證（新智能身份證持有人：將身份證放在證件閱讀器上；智能身份證持有人：將身份證插入讀卡器）")),
        (("2", "2", "2"), ("Perform fingerprint verification", "지문 인증을 합니다", "進行指紋核實")),
        (("3", "3", "3"), ("Declare the data submitted to be correct via fingerprint authentication (only for application submitted through the Internet / Immigration Department Mobile Application)", "지문 인증으로 제출한 정보가 정확함을 선서합니다(인터넷·출입경사무처 모바일 앱으로 제출한 신청에 한함)", "透過指紋認證聲明所遞交的資料正確無誤（只適用於透過互聯網／入境事務處流動應用程式遞交的申請）")),
        (("4", "4", "4"), ("Insert your previous Baekhyeon Hwarang SAR passport or Doc/I for cancellation if you hold such document", "이전 특별행정구 여권이나 Doc/I가 있으면 말소를 위해 삽입합니다", "如持有以往的柏峴화랑特別行政區護照或簽證身份書，須插入以供註銷")),
        (("5", "5", "5"), ("Collect your new passport", "새 여권을 수령합니다", "領取新護照")),
    ]),
]

# ----------------------------------------------------------------------------- Offices
BRANCH_TITLE = ("Immigration Branch Offices", "출입경사무처 지소", "入境事務處分區辦事處")
BRANCH = [
    ("p", ("Immigration Branch Offices accept applications for travel documents by appointment and provide collection services.",
           "출입경사무처 지소에서는 예약제로 여행증명서 신청을 접수하며 수령 서비스도 제공합니다.",
           "入境事務處分區辦事處以預約方式受理旅行證件申請，並提供領證服務。")),
    ("table", [("Office", "사무소", "辦事處"), ("Services", "서비스", "服務"), ("Working Hours*", "근무 시간*", "辦公時間*")], [
        (("Baekhyeon Maeul Complex 3 Branch Office", "백현마을 3단지 지소", "柏峴마을3社區分區辦事處"), ("Application and collection of travel documents; identity card services", "여행증명서 신청·수령, 신분증 서비스", "申請及領取旅行證件；身份證服務"), ("9:00am - 4:30pm (Mon - Fri)<br>9:00am - 12:30pm (Sat)", "오전 9:00 ~ 오후 4:30 (월~금)<br>오전 9:00 ~ 낮 12:30 (토)", "上午9時至下午4時30分（星期一至五）<br>上午9時至中午12時30分（星期六）")),
        (("Baekhyeon Maeul Complex 4 Branch Office", "백현마을 4단지 지소", "柏峴마을4社區分區辦事處"), ("Application and collection of travel documents; identity card services", "여행증명서 신청·수령, 신분증 서비스", "申請及領取旅行證件；身份證服務"), ("9:00am - 12:45pm & 2:00pm - 4:30pm (Mon - Fri)<br>9:00am - 12:30pm (Sat)", "오전 9:00 ~ 낮 12:45, 오후 2:00 ~ 4:30 (월~금)<br>오전 9:00 ~ 낮 12:30 (토)", "上午9時至中午12時45分及下午2時至4時30分（星期一至五）<br>上午9時至中午12時30分（星期六）")),
    ]),
    ("p", ("*All offices are closed on Sundays and public holidays.", "*모든 사무소는 일요일과 공휴일에 휴무입니다.", "*所有辦事處在星期日及公眾假期休息。")),
]
HQ_TITLE = ("Offices in Immigration Headquarters", "출입경사무처 본부 사무실", "入境事務處總部內的辦事處")
HQ = [
    ("p", ("The Immigration Headquarters is located in Baekhyeon Maeul Complex 3, Baekhyeon Hwarang Special Administrative Region.",
           "출입경사무처 본부는 백현화랑 특별행정구 백현마을 3단지에 있습니다.",
           "入境事務處總部位於柏峴화랑特別行政區柏峴마을3社區。")),
    ("table", [("Office", "사무실", "辦事處"), ("Services", "서비스", "服務"), ("Working Hours*", "근무 시간*", "辦公時間*")], [
        (("Travel Documents and Nationality (Application) Section", "여행증명서·국적(신청) 과", "旅行證件及國籍（申請）組"), ("Application for travel documents (by appointment)", "여행증명서 신청(예약제)", "申請旅行證件（須預約）"), ("8:45am - 5:15pm (Mon - Fri)<br>9:00am - 12:00 noon (Sat)", "오전 8:45 ~ 오후 5:15 (월~금)<br>오전 9:00 ~ 낮 12:00 (토)", "上午8時45分至下午5時15分（星期一至五）<br>上午9時至中午12時（星期六）")),
        (("Travel Documents (Issue) Section", "여행증명서(발급) 과", "旅行證件（簽發）組"), ("Collection of travel documents", "여행증명서 수령", "領取旅行證件"), ("9:00am - 4:30pm (Mon - Fri)<br>9:00am - 12:30pm (Sat)", "오전 9:00 ~ 오후 4:30 (월~금)<br>오전 9:00 ~ 낮 12:30 (토)", "上午9時至下午4時30分（星期一至五）<br>上午9時至中午12時30分（星期六）")),
        (("Personal Documentation Self-services", "개인 증명서류 셀프서비스", "個人證件自助服務"), ("Personal Documentation Collection / Submission Kiosks", "개인 증명서류 수령·제출 키오스크", "領取／遞交個人證件服務站"), ("8:45am - 10:00pm (Mon - Fri)<br>9:00am - 10:00pm (Sat)", "오전 8:45 ~ 오후 10:00 (월~금)<br>오전 9:00 ~ 오후 10:00 (토)", "上午8時45分至晚上10時（星期一至五）<br>上午9時至晚上10時（星期六）")),
        (("Right of Abode Section", "거주권 과", "居留權組"), ("Verification of eligibility for permanent identity card", "영구 신분증 자격 확인", "核實永久性居民身份證資格"), ("8:45am - 5:15pm (Mon - Fri)", "오전 8:45 ~ 오후 5:15 (월~금)", "上午8時45分至下午5時15分（星期一至五）")),
    ]),
    ("p", ("*All offices are closed on Sundays and public holidays.", "*모든 사무소는 일요일과 공휴일에 휴무입니다.", "*所有辦事處在星期日及公眾假期休息。")),
]

# ----------------------------------------------------------------------------- About pages (short)
ABOUT_PASSPORT_TITLE = ("About Passport", "여권 안내", "關於護照")
ABOUT_PASSPORT = [
    ("p", ("You can now apply for a Baekhyeon Hwarang SAR Passport that complies with the standard of the International Civil Aviation Organization (ICAO). Find out more about its security features and the application details here.",
           "국제민간항공기구(ICAO) 기준에 부합하는 백현화랑 특별행정구 여권을 신청할 수 있습니다. 보안 요소와 신청 방법을 여기에서 확인하세요.",
           "你現在可申請符合國際民航組織（ICAO）標準的柏峴화랑特別行政區護照。你可在這裏了解護照的防偽特徵及申請詳情。")),
    ("h2", ("Security Features", "보안 요소", "防偽特徵")),
    ("ul", [
        ("Contactless chip storing the holder's personal data and facial image", "소지자의 인적사항과 얼굴 이미지를 저장한 비접촉식 칩", "非接觸式晶片，儲存持有人的個人資料及面部影像"),
        ("Polycarbonate data page with laser-engraved photograph", "사진이 레이저로 각인된 폴리카보네이트 정보면", "聚碳酸酯資料頁，持有人照片以激光雕刻"),
        ("Machine readable zone complying with ICAO Doc 9303", "ICAO Doc 9303을 준수하는 기계판독영역(MRZ)", "符合ICAO Doc 9303的機讀區"),
        ("Regional emblem and flag as design themes of the visa pages", "사증면의 디자인 주제로 쓰인 특별행정구 휘장과 기", "簽證頁以區徽及區旗為設計主題"),
    ]),
    ("h2", ("Validity and Pages", "유효기간 및 쪽수", "有效期及頁數")),
    ("p", ("A passport issued to a person aged 16 or above is valid for 10 years and one issued to a child aged under 16 is valid for 5 years. Both 32-page and 48-page passports are available.",
           "만 16세 이상에게 발급하는 여권의 유효기간은 10년, 만 16세 미만 아동에게 발급하는 여권은 5년이며, 32쪽과 48쪽 두 종류가 있습니다.",
           "十六歲或以上人士的護照有效期為10年，十六歲以下兒童的護照有效期為5年，並有32頁及48頁兩種。")),
]
ABOUT_DOCID_TITLE = ("About Document of Identity for Visa Purposes", "비자용 신분증명서 안내", "關於簽證身份書")
ABOUT_DOCID = [
    ("p", ("People who are unable to obtain a national passport or a travel document of any other country or territory can apply for a Baekhyeon Hwarang SAR Document of Identity for Visa Purposes (Doc/I) that complies with the standard of the International Civil Aviation Organization (ICAO). Find out who is eligible and how to make an application here.",
           "국가 여권이나 다른 나라·지역의 여행증명서를 발급받을 수 없는 사람은 국제민간항공기구(ICAO) 기준에 부합하는 백현화랑 특별행정구 비자용 신분증명서(Doc/I)를 신청할 수 있습니다. 신청 자격과 방법을 여기에서 확인하세요.",
           "無法取得國家護照或任何其他國家或地區旅行證件的人士，可申請符合國際民航組織（ICAO）標準的柏峴화랑特別行政區簽證身份書（Doc/I）。你可在這裏了解申請資格及申請方法。")),
    ("p", ("Two types are issued: a 44-page and a 92-page document, each valid for 7 years.", "44쪽과 92쪽 두 종류가 발급되며 각각 유효기간은 7년입니다.", "簽證身份書分為44頁及92頁兩種，有效期均為7年。")),
]
ABOUT_REENTRY_TITLE = ("About Re-entry Permit", "재입경 허가증 안내", "關於回港證")
ABOUT_REENTRY = [
    ("p", ("Some Baekhyeon Hwarang residents require Re-entry Permits for travel to other parts of the Republic of Korea. Learn how to make an application, including the supporting documents required and fees payable.",
           "일부 백현화랑 주민은 대한민국의 다른 지역으로 여행할 때 재입경 허가증이 필요합니다. 필요한 증빙서류와 수수료 등 신청 방법을 확인하세요.",
           "部分柏峴화랑居民前往大韓民國其他地區時須持有回港證。你可在這裏了解申請方法，包括所需的證明文件及應繳費用。")),
    ("p", ("A multiple Re-entry Permit and a Re-entry Permit valid for 1 visit are available.", "복수 재입경 허가증과 1회 유효 재입경 허가증이 있습니다.", "回港證分為多次有效及一次有效兩種。")),
]
ABOUT_SEAMAN_TITLE = ("About Seaman's Identity Book", "선원 신분증 안내", "關於海員身份證")
ABOUT_SEAMAN = [
    ("p", ("Some bona fide seafarers are eligible to apply for a Baekhyeon Hwarang Seaman's Identity Book. Find out who is eligible and how to make an application here.",
           "일부 선원은 백현화랑 선원 신분증을 신청할 수 있습니다. 신청 자격과 방법을 여기에서 확인하세요.",
           "部分真正的海員符合資格申請柏峴화랑海員身份證。你可在這裏了解申請資格及申請方法。")),
]
LOST_TITLE = ("What to do if You Lose Your Identity Card and Baekhyeon Hwarang SAR Travel Documents", "신분증과 백현화랑 특별행정구 여행증명서를 분실했을 때", "遺失身份證及柏峴화랑特別行政區旅行證件時應怎麼辦")
LOST = [
    ("p", ("In this article you can learn about how to report loss and apply for replacement of Baekhyeon Hwarang identity card and Baekhyeon Hwarang SAR travel document.",
           "이 글에서는 백현화랑 신분증과 백현화랑 특별행정구 여행증명서를 분실했을 때의 신고 방법과 재발급 신청 방법을 안내합니다.",
           "本文會告訴你如何為柏峴화랑身份證及柏峴화랑特別行政區旅行證件報失及申請補領。")),
    ("ol", [
        ("Report the loss to the Police as soon as possible.", "가능한 한 빨리 경찰에 분실 신고를 합니다.", "盡快向警方報失。"),
        ("Report the loss to the Immigration Department and make an appointment online to apply for a replacement.", "출입경사무처에 분실을 신고하고 온라인으로 예약하여 재발급을 신청합니다.", "向入境事務處報失，並在網上預約申請補領。"),
        ("Bring the report and supporting documents to the appointment and pay the fee for the replacement.", "신고 확인서와 증빙서류를 예약일에 지참하고 재발급 수수료를 납부합니다.", "於預約當日攜帶報失證明及證明文件，並繳付補領費用。"),
    ]),
]

# ----------------------------------------------------------------------------- Smart identity card
SMARTID_TITLE = ("Book Appointment to Apply for Baekhyeon Hwarang Smart Identity Card", "백현화랑 스마트 신분증 신청 예약", "預約申領柏峴화랑智能身份證")
SMARTID = [
    ("p", ("The Baekhyeon Hwarang Smart Identity Card is issued to Baekhyeon Hwarang residents. Applicants must attend the Immigration Department in person for the capture of biometric data. You can make an appointment online for the application or collection of a Smart Identity Card.",
           "백현화랑 스마트 신분증은 백현화랑 주민에게 발급됩니다. 신청인은 생체 정보 등록을 위해 출입경사무처를 직접 방문해야 합니다. 스마트 신분증의 신청 또는 수령을 온라인으로 예약할 수 있습니다.",
           "柏峴화랑智能身份證發給柏峴화랑居民。申請人須親身到入境事務處辦理，以便採集生物特徵資料。你可在網上預約申領或領取智能身份證。")),
    ("btn", ("Book Appointment to Apply for Baekhyeon Hwarang Smart Identity Card", "백현화랑 스마트 신분증 신청 예약", "預約申領柏峴화랑智能身份證"), "idbook"),
    ("h2", ("Who Should Apply", "신청 대상", "誰須申請")),
    ("ul", [
        ("Persons who have reached the age of 11 and are required to register for an identity card", "만 11세가 되어 신분증 등록이 필요한 사람", "年滿11歲而須登記領取身份證的人士"),
        ("Holders who need a replacement of a lost, stolen or damaged identity card", "분실·도난·훼손된 신분증의 재발급이 필요한 소지자", "需補領遺失、被竊或損毀的身份證的持證人"),
        ("Holders of an identity card who need to change particulars", "인적사항을 변경해야 하는 신분증 소지자", "需更改個人資料的持證人"),
    ]),
    ("h2", ("What to Bring", "지참할 서류", "須攜帶的文件")),
    ("ul", [
        ("Your appointment reference number", "예약 접수번호", "預約參考編號"),
        ("Documents proving your identity and right of abode (e.g. birth certificate)", "신원과 거주권을 증명하는 서류(예: 출생증명서)", "證明身份及居留權的文件（例如出生證明書）"),
        ("Your existing identity card, if any", "기존 신분증(있는 경우)", "現有的身份證（如有）"),
    ]),
    ("h2", ("Fees", "수수료", "費用")),
    ("p", ("The first registration for an identity card is free of charge. A fee of BH$370 is payable for replacement of a lost or damaged card.", "신분증 최초 등록은 무료입니다. 분실·훼손 카드의 재발급에는 BH$370의 수수료가 부과됩니다.", "首次登記領取身份證免費。補領遺失或損毀的身份證，須繳付BH$370。")),
]

# ----------------------------------------------------------------------------- Application status enquiry (visa / entry permit)
NONPERM_TITLE = ("Online Application Status Enquiry", "신청 현황 온라인 조회", "網上查詢申請進度")
NONPERM = [
    ("p", ("If you have submitted an application related to a visa/entry permit (including applications for an entry visa/permit, extension of stay or change of status, etc.), verification of eligibility for permanent identity card, Request for Personal Data / Information of Immigration Department or Korean nationality to the Immigration Department, you can enquire online about the status of that application. This page will tell you who can use the online service, how to use it and how to obtain further information.",
           "비자·입경허가(입국 비자·허가, 체류 연장, 체류 자격 변경 등 신청 포함), 영구 신분증 자격 확인, 출입경사무처 개인정보·자료 신청 또는 대한민국 국적과 관련한 신청을 출입경사무처에 제출했다면, 해당 신청의 처리 현황을 온라인으로 조회할 수 있습니다. 이 페이지에서는 이용 대상, 이용 방법과 추가 정보를 얻는 방법을 안내합니다.",
           "如你已向入境事務處遞交有關簽證／進入許可證（包括申請入境簽證／許可證、延長逗留期限或轉換身份等）、核實永久性居民身份證資格、申請入境事務處的個人資料／資訊或大韓民國國籍的申請，你可在網上查詢該申請的進度。本頁會告訴你誰可使用這項網上服務、如何使用及如何取得進一步資料。")),
    ("h2", ("Who Can Use This Service", "이용 대상", "誰可使用此服務")),
    ("p", ("You can use the service to enquire about the status of applications related to visas/entry permits submitted to the:", "다음 부서에 제출한 비자·입경허가 관련 신청의 현황을 조회할 수 있습니다.", "你可使用此服務查詢向下列單位遞交的簽證／進入許可證申請的進度：")),
    ("ul", [
        ("Employment and Visit Visas Section", "고용·방문 비자 과", "僱傭及探訪簽證組"),
        ("Extension Section", "체류 연장 과", "延期逗留組"),
        ("Other Visas and Permits Section", "기타 비자·허가 과", "其他簽證及許可證組"),
        ("Certificate of Entitlement Section", "자격증명서 과", "登記證組"),
        ("Admission of Labour Section", "노동자 입경 과", "輸入勞工組"),
    ]),
    ("p", ("The service can also be used if you have submitted an application related to Verification of Eligibility for Permanent Identity Card (Right of Abode Section), Request for Personal Data / Information of Immigration Department or Korean nationality.",
           "영구 신분증 자격 확인(거주권 과), 출입경사무처 개인정보·자료 신청 또는 대한민국 국적과 관련한 신청을 한 경우에도 이 서비스를 이용할 수 있습니다.",
           "如你已遞交有關核實永久性居民身份證資格（居留權組）、申請入境事務處的個人資料／資訊或大韓民國國籍的申請，亦可使用此服務。")),
    ("h2", ("How to Make an Enquiry Online", "온라인으로 조회하는 방법", "如何在網上查詢")),
    ("p", ("You can access the service through the link below. When you have done so, you will need to enter the application reference number and your date of birth. If the information matches the Immigration Department's records, the application status will be shown. If your application has been closed or finalised for 1 month, the record will be purged from the system and you will not be able to enquire about its status.",
           "아래 링크로 서비스에 접속하세요. 접속 후 신청 접수번호와 생년월일을 입력해야 하며, 입력한 정보가 출입경사무처 기록과 일치하면 신청 현황이 표시됩니다. 신청이 종결되거나 처리가 완료된 후 1개월이 지나면 기록이 시스템에서 삭제되어 현황을 조회할 수 없습니다.",
           "你可透過下面的連結使用此服務。進入後，你須輸入申請的參考編號及你的出生日期。如所輸入的資料與入境事務處的紀錄相符，系統便會顯示申請進度。如你的申請已結案或處理完畢滿1個月，有關紀錄會從系統中清除，你將無法查詢其進度。")),
    ("btn", ("Online application status enquiry", "신청 현황 온라인 조회", "網上查詢申請進度"), "appstatussvc"),
    ("p", ("The application status enquiry service is also available on “BH Smart” for applications related to a visa / entry permit, verification of eligibility for permanent identity card or Korean nationality submitted on or after 1 January 2026. By registering for a “BH Smart” account and providing user authorisation, you can view the application status under “Status” of the “Personal Assistant” page.",
           "2026년 1월 1일 이후 제출한 비자·입경허가, 영구 신분증 자격 확인 또는 대한민국 국적 관련 신청은 \"BH 스마트\"에서도 현황을 조회할 수 있습니다. \"BH 스마트\" 계정을 등록하고 이용자 권한을 부여하면 \"개인 비서\" 페이지의 \"현황\"에서 신청 현황을 볼 수 있습니다.",
           "2026年1月1日或以後遞交的有關簽證／進入許可證、核實永久性居民身份證資格或大韓民國國籍的申請，亦可透過「BH智方便」查詢申請進度。登記「BH智方便」帳戶並提供用戶授權後，你可在「個人助理」頁面的「進度」中查看申請進度。")),
    ("h2", ("Enquiries by Phone", "전화 문의", "電話查詢")),
    ("p", ("Apart from using the online service, you can enquire about the status of your application through the 24-hour telephone enquiry system of the Immigration Department.", "온라인 서비스 외에 출입경사무처의 24시간 전화 문의 시스템으로도 신청 현황을 조회할 수 있습니다.", "除使用網上服務外，你亦可透過入境事務處的24小時電話查詢系統查詢申請進度。")),
    ("h2", ("Assistance and Further Information", "지원 및 상세 정보", "支援及詳細資料")),
    ("p", ("If you need technical assistance in using the online service, you can contact the Immigration e-Services Hotline during service hours. For general enquiries, please contact the Immigration Department during office hours.",
           "온라인 서비스 이용 중 기술 지원이 필요하면 서비스 운영 시간에 출입경사무처 전자서비스 상담 창구로 문의하세요. 일반 문의는 근무 시간에 출입경사무처로 하시기 바랍니다.",
           "如你於使用網上服務時需要技術支援，可於服務時間內聯絡入境事務處電子服務熱線。一般查詢可於辦公時間向入境事務處查詢。")),
]

# ----------------------------------------------------------------------------- eTAX
ETAX_TITLE = ("eTAX – Individual Tax Portal (ITP)", "eTAX – 개인 납세 포털(ITP)", "稅務易 – 個人稅務入門網站（ITP）")
ETAX = [
    ("h2", ("I Want To", "원하는 서비스", "我想")),
    ("links2", [
        (("Login ITP Account to view Tax Position and Messages", "ITP 계정에 로그인해 납세 현황과 메시지 보기", "登入ITP帳戶查閱稅務狀況及訊息"), "etaxlogin"),
        (("Open ITP Account OR Complete ITP Account Registration Process", "ITP 계정 만들기 또는 계정 등록 절차 완료", "開立ITP帳戶或完成ITP帳戶登記程序"), "etaxreg"),
        (("Calculate tax liability under Salaries Tax and Personal Assessment", "근로소득세 및 개인 과세 납부 세액 계산", "計算薪俸稅及個人入息課稅的稅款"), "taxcalc"),
        (("Know more about my Entitlement to Allowance", "공제·감면 자격 알아보기", "了解我享有的免稅額"), "allowance"),
        (("Pay Tax by Electronic Payment Methods", "전자 결제로 세금 납부", "以電子付款方式繳付稅款"), "taxpay"),
    ]),
    ("h2", ("eTAX – Individual Tax Portal (ITP) Login & Information", "eTAX – 개인 납세 포털(ITP) 로그인 및 안내", "稅務易 – 個人稅務入門網站（ITP）登入及資料")),
    ("p", ("ITP is the gateway to the Inland Revenue Department's (IRD) electronic services. It offers you an EASY, SECURE and ENVIRONMENT-FRIENDLY means to facilitate your compliance with the tax law.",
           "ITP는 국세청(IRD) 전자서비스로 들어가는 관문입니다. 납세 의무를 쉽고 안전하며 친환경적으로 이행할 수 있게 해 줍니다.",
           "ITP是通往稅務局（IRD）電子服務的入口，為你提供簡便、安全及環保的途徑，以便你遵守稅務法例。")),
    ("h2", ("eTAX – Individual Tax Portal (ITP) Account", "eTAX – 개인 납세 포털(ITP) 계정", "稅務易 – 個人稅務入門網站（ITP）帳戶")),
    ("p", ("ITP Account is your online personal account with IRD through which you can have access to the services provided under ITP.", "ITP 계정은 ITP에서 제공하는 서비스를 이용할 수 있는 국세청의 온라인 개인 계정입니다.", "ITP帳戶是你在稅務局的網上個人帳戶，你可透過此帳戶使用ITP提供的服務。")),
    ("h2", ("eTAX – Individual Tax Portal (ITP) Password", "eTAX – 개인 납세 포털(ITP) 비밀번호", "稅務易 – 個人稅務入門網站（ITP）密碼")),
    ("p", ("ITP Password is an authentication means for you to login your ITP Account. You can apply for it online under ITP.", "ITP 비밀번호는 ITP 계정에 로그인하기 위한 인증 수단이며, ITP에서 온라인으로 신청할 수 있습니다.", "ITP密碼是你登入ITP帳戶的認證方式，你可在ITP網上申請。")),
    ("h2", ("Services Available under eTAX – Individual Tax Portal (ITP)", "ITP에서 이용할 수 있는 서비스", "ITP提供的服務")),
    ("p", ("ITP provides you with a wide range of tax services relating to employment, businesses and properties.", "ITP는 고용, 사업, 부동산과 관련한 다양한 세무 서비스를 제공합니다.", "ITP為你提供與僱傭、業務及物業有關的多種稅務服務。")),
    ("h2", ("Electronic Notices, Documents and Alert Messages", "전자 고지서·문서·알림 메시지", "電子通知書、文件及提示訊息")),
    ("p", ("You may select to receive notices and documents relating to tax return filing, assessment and tax payment in the form of electronic records instead of paper. You will also receive e-Alert messages before the due dates for filing tax returns or making tax payment.",
           "세금 신고, 부과, 납부와 관련한 고지서와 문서를 종이 대신 전자 기록으로 받도록 선택할 수 있습니다. 신고·납부 기한 전에 e-알림 메시지도 받게 됩니다.",
           "你可選擇以電子記錄代替紙張，接收與報稅、評稅及繳稅有關的通知書及文件。在報稅表及稅款的到期日前，你亦會收到電子提示訊息。")),
]
TAXCALC_INFO_TITLE = ("Tax Computation of Salaries Tax and Personal Assessment", "근로소득세 및 개인 과세 세액 산정", "薪俸稅及個人入息課稅的稅款計算")
TAXCALC_INFO = [
    ("p", ("You can calculate your tax liability under salaries tax or personal assessment by using a simple Tax Calculator developed by the Inland Revenue Department.", "국세청이 개발한 간편 세액 계산기로 근로소득세 또는 개인 과세 납부 세액을 계산할 수 있습니다.", "你可使用稅務局開發的簡易稅款計算機，計算你在薪俸稅或個人入息課稅下的稅款。")),
    ("h2", ("How Salaries Tax is computed", "근로소득세 산정 방법", "薪俸稅如何計算")),
    ("p", ("Salaries Tax payable is calculated at progressive rates on your net chargeable income or at standard rate on your net income, whichever is lower.", "납부할 근로소득세는 순과세소득에 누진세율을 적용한 금액과 순소득에 표준세율을 적용한 금액 중 낮은 쪽으로 산정합니다.", "應繳薪俸稅按你的應課稅入息實額以累進稅率計算，或按入息淨額以標準稅率計算，以較低者為準。")),
    ("ul", [
        ("Net Chargeable Income = Total Income - Deductions - Allowances", "순과세소득 = 총소득 − 공제액 − 인적 공제", "應課稅入息實額 = 總入息 − 扣除額 − 免稅額"),
        ("Net Income = Total Income - Deductions", "순소득 = 총소득 − 공제액", "入息淨額 = 總入息 − 扣除額"),
    ]),
    ("p", ("A year of assessment runs from 1 April to 31 March of the following year. Provisional Salaries Tax for a year is usually based on the income less the allowances of the preceding year.",
           "과세연도는 4월 1일부터 다음 해 3월 31일까지입니다. 연도별 잠정 근로소득세는 보통 직전 연도의 소득에서 인적 공제를 뺀 금액을 기준으로 합니다.",
           "課稅年度由4月1日開始至翌年3月31日止。某年度的暫繳薪俸稅，通常以上一個年度的入息減去免稅額為基礎計算。")),
    ("h2", ("Points to Note When Using Tax Calculator", "세액 계산기 이용 시 유의사항", "使用稅款計算機的注意事項")),
    ("p", ("The tax payable figure produced by the Tax Calculator is for your information only. Its correctness always depends on whether you have entered the correct income figure, deductions, your marital status and the number of your dependants. The Inland Revenue Department accepts no liability whatsoever for any loss or damage which may be incurred by its use.",
           "세액 계산기가 산출한 납부 세액은 참고용입니다. 정확성은 소득, 공제, 혼인 여부, 부양가족 수를 올바르게 입력했는지에 달려 있습니다. 국세청은 이 계산기 사용으로 발생할 수 있는 어떠한 손실이나 손해에 대해서도 책임지지 않습니다.",
           "稅款計算機所得出的應繳稅款數字只供參考，其準確程度取決於你所輸入的入息、扣除額、婚姻狀況及受養人數目是否正確。稅務局對使用本計算機可能引致的任何損失或損害概不負責。")),
    ("h2", ("Tax Computation", "세액 산정", "稅款計算")),
    ("p", ("To calculate the tax payable under salaries tax or personal assessment, please select the link for the relevant year of assessment. Select your marital status and input the total income and other information on the input page. Then press the ‘Compute’ button at the bottom.",
           "근로소득세 또는 개인 과세 세액을 계산하려면 해당 과세연도의 링크를 선택하세요. 입력 화면에서 혼인 여부를 선택하고 총소득과 기타 정보를 입력한 뒤 맨 아래의 '계산' 버튼을 누르면 됩니다.",
           "如要計算薪俸稅或個人入息課稅的應繳稅款，請選擇有關課稅年度的連結。在輸入頁面選擇婚姻狀況，並輸入總入息及其他資料，然後按下方的「計算」按鈕。")),
    ("h3", ("Calculating Your Tax under Salaries Tax", "근로소득세 세액 계산", "計算你的薪俸稅")),
    ("calclinks", ["2026/27", "2025/26", "2024/25", "2023/24", "2022/23", "2021/22", "2020/21"]),
    ("h3", ("Calculating Your Tax under Personal Assessment", "개인 과세 세액 계산", "計算你的個人入息課稅")),
    ("calclinks", ["2026/27", "2025/26", "2024/25", "2023/24", "2022/23", "2021/22", "2020/21"]),
]
ALLOWANCE_TITLE = ("Know more about my Entitlement to Allowance", "공제·감면 자격 알아보기", "了解我享有的免稅額")
ALLOWANCE = [
    ("p", ("Allowances are deducted from your net income in arriving at your net chargeable income. The main allowances for the year of assessment 2025/26 are as follows.", "인적 공제는 순소득에서 차감하여 순과세소득을 산정합니다. 2025/26 과세연도의 주요 인적 공제는 다음과 같습니다.", "免稅額會從你的入息淨額中扣除，以得出應課稅入息實額。2025/26課稅年度的主要免稅額如下。")),
    ("table", [("Allowance", "공제 항목", "免稅額"), ("Amount", "금액", "金額")], [
        (("Basic allowance", "기본 공제", "基本免稅額"), ("BH$132,000", "BH$132,000", "BH$132,000")),
        (("Married person's allowance", "기혼자 공제", "已婚人士免稅額"), ("BH$264,000", "BH$264,000", "BH$264,000")),
        (("Single parent allowance", "한부모 공제", "單親免稅額"), ("BH$132,000", "BH$132,000", "BH$132,000")),
        (("Child allowance (each child)", "자녀 공제(자녀 1인당)", "子女免稅額（每名子女）"), ("BH$130,000", "BH$130,000", "BH$130,000")),
        (("Dependent parent / grandparent allowance (aged 60 or above)", "부양 부모·조부모 공제(만 60세 이상)", "供養父母／祖父母免稅額（60歲或以上）"), ("BH$50,000", "BH$50,000", "BH$50,000")),
        (("Dependent parent / grandparent allowance (aged 55 to 59)", "부양 부모·조부모 공제(만 55~59세)", "供養父母／祖父母免稅額（55至59歲）"), ("BH$25,000", "BH$25,000", "BH$25,000")),
        (("Dependent brother / sister allowance", "부양 형제·자매 공제", "供養兄弟姊妹免稅額"), ("BH$37,500", "BH$37,500", "BH$37,500")),
        (("Disabled dependant / disability allowance", "장애 부양가족·장애인 공제", "傷殘受養人／傷殘免稅額"), ("BH$75,000", "BH$75,000", "BH$75,000")),
    ]),
    ("p", ("The amounts are in Baekhyeon Hwarang Dollars (BH$), the currency issued by the Baekhyeon Hwarang Monetary Authority.", "금액은 백현화랑 금융관리국이 발행하는 통화인 백현화랑달러(BH$) 기준입니다.", "金額以柏峴화랑金融管理局發行的貨幣柏峴화랑元（BH$）為單位。")),
]
