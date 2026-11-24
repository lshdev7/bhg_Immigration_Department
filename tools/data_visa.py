# -*- coding: utf-8 -*-
"""Visas / Entry Permits - shared by the Immigration Department site and GovBHG (identical copy in both repos).
Text tuples are (English, Korean, Traditional Chinese); Simplified Chinese is derived at build time.
"Mainland" means the Republic of Korea outside the Baekhyeon Hwarang SAR (HK motif: 內地)."""


def F(n, l, t="text", **kw):
    d = {"n": n, "l": l, "t": t}
    d.update(kw)
    return d


YN = [["Y", ("Yes", "예", "是")], ["N", ("No", "아니요", "否")]]

# ----------------------------------------------------------------------------- tabs of the ImmD "Visas / Entry Permits" page
TABS = [
    ("intro", ("Visas / Entry Permits", "비자·입경허가", "簽證／進入許可證")),
    ("talent", ("Talent Admission", "인재 입경", "人才入境")),
    ("labour", ("Foreign Domestic Helpers / Imported Workers", "외국인 가사도우미·수입 노동자", "外籍家庭傭工／輸入勞工")),
    ("invest", ("Investment / Training / Other Employment", "투자·연수·기타 취업", "投資／培訓／其他就業")),
    ("study", ("Study / Residence", "유학·거주", "讀書／居留")),
    ("visit", ("Visit", "방문", "訪問")),
]
INTRO = [
    ("Welcome to the webpages of “Visas / Entry Permits”.", "\"비자·입경허가\" 웹페이지에 오신 것을 환영합니다.", "歡迎瀏覽「簽證／進入許可證」網頁。"),
    ("In general, unless a person has the right of abode or right to land in the Baekhyeon Hwarang Special Administrative Region (BHGSAR), he/she requires a visa/entry permit to work, study, establish or join in any business, take up residence or to stay in the BHGSAR as a visitor longer than the allowed visa free period.",
     "일반적으로 백현화랑 특별행정구에서 거주권이나 입경권이 없는 사람은 취업, 유학, 사업 설립·참여, 거주를 하거나 무비자 허용 기간보다 길게 방문객으로 체류하려면 비자·입경허가가 필요합니다.",
     "一般而言，任何人士除非享有柏峴화랑特別行政區的居留權或入境權，否則須持有簽證／進入許可證，才可在柏峴화랑特別行政區工作、讀書、開辦或參與任何業務、居留，或以訪客身份逗留超過免簽證期限。"),
    ("Detailed information on the various admission schemes / entry arrangements and the relevant application procedures can be found on the sub-pages and the quick links therein to the electronic services for visa applications allow applicants to submit instantly relevant applications for entry or extension of stay.",
     "각종 입경 제도와 입경 절차, 신청 방법은 하위 페이지에서 확인할 수 있습니다. 하위 페이지의 비자 전자신청 바로가기를 이용하면 입경 또는 체류 연장 신청서를 즉시 제출할 수 있습니다.",
     "有關各項入境計劃／入境安排及相關申請程序的詳情，載於各分頁內，而分頁內的簽證電子服務快速連結可讓申請人即時遞交入境或延期逗留申請。"),
]
APPLY_ENTRY = ("Apply entry now", "지금 입경 신청", "立即申請入境")
APPLY_EXT = ("Apply extension now", "지금 체류 연장 신청", "立即申請延期")
APPLY_NOW = ("Apply now", "지금 신청", "立即申請")
SEC_ENTRY = ("Entry Visas / Permits", "입경 비자·허가", "入境簽證／許可證")
SEC_EXT = ("Extension of Stay", "체류 연장", "延期逗留")
PHASES = [("before", ("Before Applying", "신청 전", "申請前")), ("applying", ("Applying", "신청 중", "申請時")), ("after", ("After Applying", "신청 후", "申請後"))]
H = {
    "elig": ("Eligibility Criteria", "신청 자격", "資格準則"),
    "docs": ("Documents to be Uploaded by the Applicant", "신청인이 제출할 서류", "申請人須上載的文件"),
    "depdocs": ("Documents to be Uploaded by Each Accompanying Dependant", "동반 부양가족별 제출 서류", "每名隨行受養人須上載的文件"),
    "how": ("How to Apply", "신청 방법", "申請方法"),
    "proc": ("Processing Time", "처리 기간", "處理時間"),
    "fee": ("Fees", "수수료", "費用"),
    "status": ("Application Status", "신청 현황", "申請進度"),
    "evisa": ("Issue of “e-Visa”", "\"e-Visa\" 발급", "發出「電子簽證」"),
    "stay": ("Stay and Extension of Stay", "체류 및 체류 연장", "逗留及延期逗留"),
    "abode": ("Right of Abode", "거주권", "居留權"),
    "dep": ("Dependants", "부양가족", "受養人"),
}
# common paragraphs ---------------------------------------------------------------------------------
NORMAL = ("While each application is determined on its individual merits, an applicant should meet normal immigration requirements (such as holding a valid travel document with adequate returnability to his/her country of residence or citizenship; be of clear criminal record and raise no security or criminal concerns to the BHGSAR; have no likelihood of becoming a burden on the BHGSAR, etc.) as well as the relevant specific eligibility criteria before he/she may be considered for the grant of a visa/entry permit. The eligibility criteria may be subject to change from time to time without prior notice.",
          "각 신청은 개별 사정에 따라 결정되며, 비자·입경허가를 받으려면 일반 출입경 요건(거주국 또는 국적국으로 돌아갈 수 있는 유효한 여행증명서 소지, 범죄 경력이 없고 백현화랑 특별행정구의 안보·치안에 우려가 없을 것, 백현화랑 특별행정구에 부담이 될 가능성이 없을 것 등)과 해당 제도의 자격 요건을 모두 충족해야 합니다. 자격 요건은 사전 통지 없이 수시로 변경될 수 있습니다.",
          "雖然每宗申請均會按個別情況考慮，但申請人須符合一般入境規定（例如持有有效旅行證件，並確保可返回其居住國家或國籍國家；沒有犯罪紀錄，對柏峴화랑特別行政區沒有構成保安或治安上的疑慮；不大可能成為柏峴화랑特別行政區的負擔等）及上述相關的特定資格準則，方會獲考慮發給簽證／進入許可證。資格準則或會不時更改，而不作事先通知。")
DPRK = ("This entry arrangement does not apply to nationals of Afghanistan, Cuba and Korea (Democratic People's Republic of).",
        "이 입경 절차는 아프가니스탄, 쿠바, 조선민주주의인민공화국 국적자에게는 적용되지 않습니다.",
        "此入境安排不適用於阿富汗、古巴及朝鮮民主主義人民共和國的國民。")
DISCRETION = ("All applications are processed and determined by the Immigration Department. Approval of applications is entirely discretionary and is subject to changes in government policies. The Director of Immigration reserves absolute discretion to approve or refuse any application.",
              "모든 신청은 출입경사무처가 처리하고 결정합니다. 신청 승인은 전적으로 재량 사항이며 정부 정책 변화의 영향을 받습니다. 출입경사무처장은 어떠한 신청이든 승인하거나 거부할 절대적인 재량권을 가집니다.",
              "所有申請均由入境事務處處理及決定。批准申請與否完全屬酌情處理，並受政府政策的轉變所影響。入境事務處處長保留批准或拒絕任何申請的絕對酌情權。")
TRANSL = ("Where a document is not in Korean, Chinese or English, it must be accompanied by a Korean, Chinese or English translation certified as a true translation by a sworn translator, court translator, authorised public translator, certified translator, expert translator or official translator.",
          "서류가 한국어, 중국어 또는 영어로 작성되지 않은 경우, 선서 번역인·법원 번역인·공인 번역인·인증 번역인·전문 번역인 또는 공식 번역인이 정확한 번역임을 인증한 한국어, 중국어 또는 영어 번역본을 함께 제출해야 합니다.",
          "如文件並非以韓文、中文或英文撰寫，必須附連經宣誓翻譯員、法庭翻譯員、認可公共翻譯員、註冊翻譯員、專家翻譯員或官方翻譯員核證為真確譯本的韓文、中文或英文譯本。")
FALSE = ("It is an offence to make false statements or representations to an immigration officer. To verify the authenticity of the information and documents submitted with a visa/entry permit application, field visits may be conducted. A person who makes such statements or representations will be liable to prosecution, and the visa/entry permit granted will be rendered invalid.",
         "출입경 공무원에게 허위 진술이나 허위 표시를 하는 것은 범죄입니다. 비자·입경허가 신청과 함께 제출한 정보와 서류의 진위를 확인하기 위해 현장 방문을 할 수 있습니다. 허위 진술 또는 허위 표시를 한 사람은 기소될 수 있으며, 받은 비자·입경허가는 무효가 됩니다.",
         "向入境事務主任作出虛假陳述或申述，即屬違法。為核實與簽證／進入許可證申請一併遞交的資料及文件的真確性，本處或會進行實地探訪。作出此等陳述或申述的人士可遭檢控，而所獲批的簽證／進入許可證亦會失效。")
STATUS = ("Once the receipt of application has been acknowledged, applicants can enquire about their application status online through the Online Application Status Enquiry service.",
          "신청 접수가 확인되면 신청 현황 온라인 조회 서비스로 처리 현황을 조회할 수 있습니다.",
          "申請一經確認收妥，申請人可透過網上申請進度查詢服務查詢申請進度。")
EVISA_P = ("A visa/entry permit (in the form of “e-Visa”) will be issued upon successful application and payment of fees. Upon immigration arrival clearance in the BHGSAR, the applicant should present his/her valid travel document and the “e-Visa” saved on a personal mobile device or printed on a sheet of A4 white paper, and scan the encrypted QR code on the “e-Visa”.",
           "신청이 승인되고 수수료를 납부하면 비자·입경허가가 \"e-Visa\" 형태로 발급됩니다. 백현화랑 특별행정구 입경 심사 때 유효한 여행증명서와 함께 개인 휴대기기에 저장하거나 A4 흰 종이에 인쇄한 \"e-Visa\"를 제시하고, \"e-Visa\"의 암호화된 QR 코드를 스캔해야 합니다.",
           "申請獲批准並繳付費用後，本處會以「電子簽證」形式發出簽證／進入許可證。申請人在柏峴화랑特別行政區辦理入境檢查時，應出示其有效旅行證件，以及儲存於個人流動裝置內或列印於A4白紙上的「電子簽證」，並掃描「電子簽證」上的加密二維碼。")
EXT_DEADLINE = ("Unless approved by the Director of Immigration under exceptional circumstances, persons subject to a limit of stay must depart the BHGSAR before the expiry of their limit of stay, even if they have applied for an extension of stay. Applicants should submit an application for extension of stay as early as possible within three months before their limit of stay expires, and in all circumstances, at least six weeks before their limit of stay expires. It normally takes four weeks to process an application upon receipt of all the required documents.",
                "예외적인 상황에서 출입경사무처장의 승인을 받은 경우가 아니면, 체류 기한이 있는 사람은 체류 연장을 신청했더라도 체류 기한 만료 전에 백현화랑 특별행정구를 떠나야 합니다. 체류 연장 신청은 체류 기한 만료 3개월 전부터 가능한 한 빨리, 늦어도 만료 6주 전까지 제출해야 합니다. 필요한 서류가 모두 접수된 후 처리에는 통상 4주가 걸립니다.",
                "除非在特殊情況下獲入境事務處處長批准，否則受逗留期限限制的人士即使已申請延期逗留，亦必須在逗留期限屆滿前離開柏峴화랑特別行政區。申請人應盡早在逗留期限屆滿前三個月內，及無論如何須在逗留期限屆滿前最少六星期遞交延期逗留申請。在收到所有所需文件後，處理申請一般需時四星期。")
ROA = ("Persons admitted under this arrangement who have ordinarily resided in the BHGSAR for a continuous period of not less than seven years may apply for the right of abode in the BHGSAR in accordance with the law.",
       "이 제도로 입경하여 백현화랑 특별행정구에 7년 이상 계속하여 통상 거주한 사람은 법에 따라 백현화랑 특별행정구 거주권을 신청할 수 있습니다.",
       "根據此安排獲准入境並在柏峴화랑特別行政區通常居住連續七年或以上的人士，可依法申請柏峴화랑特別行政區的居留權。")
NOROA = ("Persons admitted under this arrangement are not regarded as ordinarily resident in the BHGSAR and may not apply for the right of abode on the basis of such stay.",
         "이 제도로 입경한 사람은 백현화랑 특별행정구에 통상 거주하는 것으로 보지 않으며, 이 기간의 체류를 근거로 거주권을 신청할 수 없습니다.",
         "根據此安排獲准入境的人士不被視為通常居於柏峴화랑特別行政區，亦不可憑該段逗留期申請居留權。")
DEP_P = ("Persons admitted under this arrangement may apply to bring in their spouse or the other party to a civil partnership / civil union legally recognised in the place of celebration, and unmarried dependent children under the age of 18, under the prevailing dependant policy. Dependants may submit their applications together with the principal applicant as a group (maximum nine applications in each group).",
         "이 제도로 입경한 사람은 현행 부양가족 정책에 따라 배우자 또는 혼인 거행지에서 법적으로 인정된 시민 동반자·시민 결합 상대방과 만 18세 미만의 미혼 부양 자녀를 데려오도록 신청할 수 있습니다. 부양가족은 주 신청인과 함께 그룹으로 신청할 수 있습니다(그룹당 최대 9건).",
         "根據此安排獲准入境的人士可按現行受養人政策，申請攜同其配偶或在締結地合法承認的民事伴侶／民事結合的另一方，以及18歲以下未婚而受養的子女來柏峴화랑。受養人可與主申請人一併以組別方式遞交申請（每組最多九宗申請）。")
SPEC_FEE = ("For the purpose of Schedule 2 of the Immigration Regulations, this scheme is a “specified scheme”. For entry visa/permit applications or change of condition of stay (including extension of limit of stay) applications made under a “specified scheme”, the principal applicant and each of his/her dependant(s) (if any) are required to pay an application fee of BH$600 on submission and a visa issuance fee of BH$1,300 (relevant period of more than 180 days) or BH$600 (not more than 180 days) upon approval. The application fee paid is non-refundable in any circumstances.",
            "출입경 규칙 별표 2에 따라 이 제도는 \"지정 제도\"입니다. \"지정 제도\"에 따른 입경 비자·허가 신청 또는 체류 조건 변경(체류 기한 연장 포함) 신청은 주 신청인과 각 부양가족(있는 경우)이 제출할 때 신청 수수료 BH$600을, 승인 시 비자 발급 수수료 BH$1,300(해당 기간 180일 초과) 또는 BH$600(180일 이하)을 내야 합니다. 납부한 신청 수수료는 어떠한 경우에도 환불되지 않습니다.",
            "就《入境規例》附表2而言，此計劃屬「指明計劃」。凡根據「指明計劃」提出的入境簽證／許可證申請或更改逗留條件（包括延長逗留期限）申請，主申請人及其每名受養人（如有）須於遞交時繳付申請費600元，並於獲批時繳付簽證簽發費1,300元（有關期間超過180日）或600元（不超過180日）。已繳付的申請費在任何情況下均不獲退還。")
ORD_FEE = ("A visa issuance fee of BH$230 (entry) or BH$230 (extension of stay / change of condition of stay) is payable for each successful applicant. The fee is paid during the online application process.",
           "승인된 신청인 1명당 비자 발급 수수료 BH$230(입경) 또는 BH$230(체류 연장·체류 조건 변경)을 내야 합니다. 수수료는 온라인 신청 과정에서 납부합니다.",
           "每名獲批准的申請人須繳付簽證簽發費230元（入境）或230元（延期逗留／更改逗留條件）。費用於網上申請過程中繳付。")
APPLY_ONLINE = ("Applicants may submit the application and upload all supporting documents online through the electronic services for visa applications. Click “Apply Now” to read the details of the online service on GovBHG before starting.",
                "비자 전자신청 서비스로 신청서를 제출하고 모든 증빙서류를 온라인으로 올릴 수 있습니다. 시작하기 전에 \"지금 신청\"을 눌러 정부포털 BHG에서 온라인 서비스 안내를 읽어 주세요.",
                "申請人可透過簽證申請電子服務遞交申請及上載所有證明文件。開始前，請按「立即申請」到「BHG政府一站通」閱讀網上服務的詳情。")

# common document items ---------------------------------------------------------------------------
D_PHOTO = ("The applicant’s recent photograph", "신청인의 최근 사진", "申請人的近照")
D_TD = ("The applicant’s valid travel document containing personal particulars, date of issue, date of expiry and/or details of any re-entry visa held (if applicable). For an applicant who is currently staying in the BHGSAR, his/her valid travel document page containing the latest arrival stamp/landing slip/extension of stay label/“e-Visa” (if applicable)",
        "인적사항, 발급일, 만료일, 재입국 비자 내역(해당 시)이 있는 신청인의 유효한 여행증명서. 현재 백현화랑 특별행정구에 체류 중인 신청인은 최근 입경 도장·입경 확인표·체류 연장 라벨·\"e-Visa\"(해당 시)가 있는 여행증명서 면",
        "申請人的有效旅行證件，載有個人資料、簽發日期、屆滿日期及／或所持任何回港簽證的詳情（如適用）。如申請人現正身處柏峴화랑特別行政區，須提供載有最近入境印章／入境標籤／延期逗留標籤／「電子簽證」（如適用）的有效旅行證件頁")
D_ID = ("The applicant’s Baekhyeon Hwarang identity card (if any)", "신청인의 백현화랑 신분증(있는 경우)", "申請人的柏峴화랑身份證（如有）")
D_IDX = ("The applicant’s Baekhyeon Hwarang identity card", "신청인의 백현화랑 신분증", "申請人的柏峴화랑身份證")
D_DEGREE = ("Academic qualification certificate(s) and transcript(s)", "학위증명서 및 성적증명서", "學歷證明文件及成績單")
D_WORK = ("Documentary proof of the applicant’s relevant work experience (e.g. employment certificates)", "신청인의 관련 경력 증빙(재직증명서 등)", "申請人相關工作經驗的證明文件（例如僱傭證明書）")
D_CONTRACT = ("Employment contract or letter of appointment issued by the employer, stating the post, salary and fringe benefits and duration of employment", "직위, 급여·복리후생, 고용 기간이 적힌 고용주 발행 고용계약서 또는 채용 확인서", "由僱主簽發並列明職位、薪酬福利及僱用期的僱傭合約或聘書")
D_COMPANY = ("Documentary proof of the employing company (e.g. business registration certificate, latest audited financial report)", "고용 회사 증빙(사업자 등록증, 최근 감사 재무보고서 등)", "僱用公司的證明文件（例如商業登記證、最近期經審計的財務報告）")
D_REL = ("Evidence of the applicant’s relationship with the dependant (e.g. marriage certificate, birth certificate)", "신청인과 부양가족의 관계 증빙(혼인증명서, 출생증명서 등)", "申請人與受養人關係的證明（例如結婚證書、出生證明書）")
D_DEP_PHOTO = ("The dependant’s recent photograph", "부양가족의 최근 사진", "受養人的近照")
D_DEP_TD = ("The dependant’s valid travel document", "부양가족의 유효한 여행증명서", "受養人的有效旅行證件")
D_FIN = ("Documentary proof of financial means (e.g. bank statements)", "재정 능력 증빙(은행 거래 내역서 등)", "經濟能力證明（例如銀行月結單）")
D_LAST_TD = ("The applicant’s valid travel document and, where applicable, his/her previous travel document showing the latest arrival stamp/landing slip/“e-Visa” in the BHGSAR", "유효한 여행증명서와, 해당 시 백현화랑 특별행정구 최근 입경 도장·입경 확인표·\"e-Visa\"가 있는 이전 여행증명서", "申請人的有效旅行證件，以及（如適用）載有最近在柏峴화랑特別行政區入境印章／入境標籤／「電子簽證」的舊旅行證件")
D_EMP_PROOF = ("Documentary proof of current employment (e.g. latest salary tax demand note, employer’s letter)", "현재 고용 증빙(최근 근로소득세 고지서, 고용주 확인서 등)", "現職證明文件（例如最近期的薪俸稅繳稅通知書、僱主信件）")
D_CONSENT = ("Letter of consent from the applicant’s present working unit or relevant Mainland authorities [for Mainland residents only]", "신청인의 현 근무처 또는 관련 본토 당국의 동의서[본토 주민만 해당]", "申請人現時工作單位或內地有關當局的同意書〔只適用於內地居民〕")
D_OVERSEAS = ("Proof of the applicant’s overseas residence [for overseas Korean nationals holding Republic of Korea passports only]", "신청인의 해외 거주 증빙[대한민국 여권을 소지한 재외국민만 해당]", "申請人海外居留的證明〔只適用於持大韓民國護照的海外韓國籍人士〕")

# common wizard fields (scheme-specific details) ------------------------------------------------------
F_EMPLOYER = F("employer", ("Name of employer / company in Baekhyeon Hwarang", "백현화랑 내 고용주·회사 이름", "柏峴화랑僱主／公司名稱"), req=True, full=True)
F_POST = F("post", ("Post / job title", "직위·직무", "職位"), req=True)
F_SALARY = F("salary", ("Monthly salary (BH$)", "월 급여(BH$)", "每月薪金（柏峴화랑元）"), req=True, v="num", im="numeric")
F_CONTRACT = F("contract", ("Duration of employment contract (months)", "고용계약 기간(개월)", "僱傭合約期（月）"), "select", req=True, o=[["12", "12"], ["24", "24"], ["36", "36"]])
F_QUAL = F("qual", ("Highest academic qualification", "최종 학력", "最高學歷"), "select", req=True, o=[
    ["phd", ("Doctoral degree", "박사", "博士學位")], ["master", ("Master's degree", "석사", "碩士學位")], ["bachelor", ("Bachelor's degree", "학사", "學士學位")],
    ["subdeg", ("Sub-degree / Higher Diploma", "준학사·고등 디플로마", "副學位／高級文憑")], ["other", ("Other", "기타", "其他")]])
F_INST = F("inst", ("Name of university / institution", "대학·기관 이름", "大學／院校名稱"), req=True, full=True)
F_YEARS = F("exp", ("Years of relevant work experience", "관련 경력 연수", "相關工作經驗年數"), "select", req=True, o=[[str(n), str(n)] for n in range(0, 21)])

# ----------------------------------------------------------------------------- schemes
# k: key; tab; abbr; t: title; entry / ext: GovBHG page slugs (None = no online service); spec: specified scheme;
# deps: group submission with dependants; months: limit of stay on e-Visa; slip: (zh, en) condition on e-Visa;
# multi: multiple journeys; evisa: issue e-Visa PDF on completion.
SCHEMES = []


def mandatory(d):
    """Documents marked * on GovBHG and required in the e-service: not "(if any)" and not limited to a group ("... only]")."""
    return "(if any)" not in d[0] and "only]" not in d[0] and "(optional" not in d[0]


def S(**kw):
    kw.setdefault("deps", True)
    kw.setdefault("spec", False)
    kw.setdefault("ext", None)
    kw.setdefault("entry", None)
    kw.setdefault("evisa", True)
    kw.setdefault("multi", True)
    kw.setdefault("roa", True)
    kw.setdefault("fields", [])
    kw.setdefault("docs", [])
    kw.setdefault("ext_docs", [D_LAST_TD, D_IDX])
    kw.setdefault("ext_intro", [])
    kw.setdefault("after", [])
    kw.setdefault("elig", [])
    kw.setdefault("notes", [])
    kw.setdefault("proc", 4)
    kw.setdefault("entry_loc", "nr")
    SCHEMES.append(kw)
    return kw


# ============================================================================= Talent Admission
S(k="ttps", tab="talent", abbr="TTPS", spec=True, months=24, slip=("高端人才通行證計劃", "TOP TALENT PASS SCHEME"),
  t=("Top Talent Pass Scheme", "최고인재 통행증 제도", "高端人才通行證計劃"), entry="applyttps", ext="ttpsentrants",
  intro=[("The Top Talent Pass Scheme (TTPS) seeks to attract top talents with rich work experience and good academic qualifications from all over the world to explore opportunities in Baekhyeon Hwarang. These top talents include high-income talents and graduates from the world’s top universities.",
          "최고인재 통행증 제도(TTPS)는 풍부한 경력과 우수한 학력을 갖춘 세계 각지의 최고 인재가 백현화랑에서 기회를 찾도록 유치하는 제도입니다. 고소득 인재와 세계 최상위 대학 졸업자가 대상입니다.",
          "「高端人才通行證計劃」旨在吸引世界各地具豐富工作經驗及高學歷的頂尖人才來柏峴화랑發掘機會，當中包括高收入人士及全球頂尖大學的畢業生。"),
         ("Applicants are not required to have secured an offer of employment in the BHGSAR upon application. They may be granted 36 months’ (Category A) / 24 months’ (Categories B and C) stay on time limitation only without other conditions of stay.",
          "신청할 때 백현화랑 특별행정구 내 일자리를 확보할 필요가 없습니다. 다른 체류 조건 없이 체류 기한만 붙은 36개월(A유형) 또는 24개월(B·C유형) 체류가 허가될 수 있습니다.",
          "申請人在申請時無須已獲柏峴화랑特別行政區的聘用。他們可獲准逗留36個月（甲類）／24個月（乙類及丙類），只受逗留期限限制而不受其他逗留條件限制。")],
  elig=[("Category A: persons with annual income reaching BH$2.5 million or above, or its equivalent in foreign currency, in the year immediately preceding the date of application;", "A유형: 신청일 직전 1년간 연간 소득이 BH$250만 이상(또는 이에 상당하는 외화)인 사람", "甲類：在緊接申請日期前一年，全年收入達250萬元或以上（或等值外幣）的人士；"),
        ("Category B: degree graduates of eligible universities with at least three years of work experience over the past five years immediately preceding the date of application;", "B유형: 지정 대학 학사 학위 취득자로서 신청일 직전 5년 동안 3년 이상의 경력이 있는 사람", "乙類：合資格大學的學士學位畢業生，並在緊接申請日期前五年內累積最少三年工作經驗；"),
        ("Category C: degree graduates of eligible universities in the past five years immediately preceding the date of application with less than three years of work experience, subject to an annual quota allotted on a first-come, first-served basis;", "C유형: 신청일 직전 5년 이내에 지정 대학을 졸업했고 경력이 3년 미만인 사람(연간 정원 내 선착순 배정)", "丙類：在緊接申請日期前五年內於合資格大學取得學士學位，但工作經驗少於三年的人士，每年設有配額，以先到先得方式分配；"),
        ("there is no security objection and no known record of serious crime in respect of the applicant.", "신청인에 대해 안보상 이의가 없고 알려진 중범죄 기록이 없을 것", "申請人沒有保安方面的疑點及沒有已知的嚴重犯罪紀錄。")],
  docs=[D_PHOTO, D_TD, D_ID, D_DEGREE, D_WORK, ("Documentary proof of the applicant’s annual income of BH$2.5 million or above [Category A]", "연간 소득 BH$250만 이상 증빙[A유형]", "申請人全年收入達250萬元或以上的證明〔甲類〕"), D_CONSENT, D_OVERSEAS],
  ext_intro=[("Persons admitted under the TTPS may apply for extension of stay. For applicants who have taken up employment, the job secured should be at a level commonly taken up by degree holders; for applicants who have established or joined in a business, the business should be operating. Successful applicants will normally be granted an extension of stay of not more than three years on time limitation only.",
              "TTPS로 입경한 사람은 체류 연장을 신청할 수 있습니다. 취업한 신청인은 학위 소지자가 통상 맡는 수준의 일자리여야 하고, 사업을 설립하거나 참여한 신청인은 해당 사업이 실제로 운영 중이어야 합니다. 승인되면 통상 체류 기한만 붙은 3년 이내의 연장이 허가됩니다.",
              "根據「高端人才通行證計劃」獲准入境的人士可申請延期逗留。已就業的申請人所從事的工作應屬學位持有人一般從事的職位；已開辦或參與業務的申請人，其業務應正在運作。申請獲批准的人士一般會獲准延期逗留不超過三年，只受逗留期限限制。")],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF, ("Proof of business operation (for applicants who have established or joined in a business)", "사업 운영 증빙(사업을 설립·참여한 신청인)", "業務運作證明（適用於已開辦或參與業務的申請人）")],
  after=[("Persons admitted under the TTPS, who are on time limitation only without other conditions of stay, are free to take up and change employment or to establish or join in business in the BHGSAR during their permitted stay without the need to seek prior approval from the Immigration Department.",
          "체류 기한만 붙고 다른 체류 조건이 없는 TTPS 입경자는 허가된 체류 기간 동안 출입경사무처의 사전 승인 없이 자유롭게 취업·이직하거나 사업을 설립·참여할 수 있습니다.",
          "根據「高端人才通行證計劃」獲准入境而只受逗留期限限制的人士，在獲准逗留期間可自由受僱、轉換工作或在柏峴화랑特別行政區開辦或參與業務，而無須事先獲得入境事務處批准。")],
  fields=[F("cat", ("Category", "신청 유형", "申請類別"), "radio", req=True, o=[["A", ("Category A – annual income BH$2.5 million or above", "A유형 – 연간 소득 BH$250만 이상", "甲類 – 全年收入250萬元或以上")], ["B", ("Category B – degree graduate with 3+ years’ work experience", "B유형 – 학사 + 경력 3년 이상", "乙類 – 學位畢業生並有三年或以上工作經驗")], ["C", ("Category C – degree graduate with less than 3 years’ work experience", "C유형 – 학사 + 경력 3년 미만", "丙類 – 學位畢業生而工作經驗少於三年")]]),
          F("income", ("Annual income in the preceding year (BH$)", "직전 1년 연간 소득(BH$)", "上一年全年收入（柏峴화랑元）"), req=True, v="num", im="numeric", showIf={"n": "cat", "eq": "A"}),
          F_INST, F("gradyear", ("Year of graduation", "졸업 연도", "畢業年份"), req=True, v="num", im="numeric", ph="2022"), F_YEARS])

S(k="gep", tab="talent", abbr="GEP", spec=True, months=24, slip=("僱傭工作", "EMPLOYMENT"),
  t=("General Employment Policy", "일반 취업 정책", "一般就業政策"), entry="applyemployment", ext="gepentrants",
  intro=[("Applicants who possess special skills, knowledge or experience of value to and not readily available in the BHGSAR may apply to come to work as professionals under the General Employment Policy (GEP). The GEP is quota-free and non-sector specific.",
          "백현화랑 특별행정구에 가치 있고 현지에서 쉽게 구할 수 없는 특별한 기술, 지식 또는 경험을 가진 사람은 일반 취업 정책(GEP)에 따라 전문인력으로 일하러 오도록 신청할 수 있습니다. GEP는 정원과 업종 제한이 없습니다.",
          "具備柏峴화랑特別行政區所需而又缺乏的特別技能、知識或經驗的申請人，可根據「一般就業政策」申請來柏峴화랑以專業人士身份工作。「一般就業政策」不設配額，亦不限行業。"),
         ("This entry arrangement does not apply to Korean residents of the Mainland, who may apply under the Admission Scheme for Mainland Talents and Professionals.", "이 입경 절차는 본토 대한민국 주민에게는 적용되지 않으며, 본토 주민은 본토 인재·전문인력 유입계획으로 신청할 수 있습니다.", "此入境安排不適用於內地韓國居民，他們可根據「輸入內地人才計劃」提出申請。")],
  elig=[("there is no security objection and no known record of serious crime in respect of the applicant;", "신청인에 대해 안보상 이의가 없고 알려진 중범죄 기록이 없을 것", "申請人沒有保安方面的疑點及沒有已知的嚴重犯罪紀錄；"),
        ("the applicant has a good education background, normally a first degree in the relevant field, but in special circumstances, good technical qualifications, proven professional abilities and/or relevant experience and achievements may also be accepted;", "통상 관련 분야 학사 학위 이상의 좋은 학력을 갖출 것. 특별한 경우 우수한 기술 자격, 입증된 전문 능력 또는 관련 경력·성과도 인정될 수 있음", "申請人具備良好的教育背景，一般要有相關範疇的學士學位，但在特殊情況下，良好的技術資歷、經證明的專業能力及／或相關經驗及成就亦可接納；"),
        ("there is a genuine job vacancy;", "실제로 일자리가 비어 있을 것", "確有職位空缺；"),
        ("the applicant has a confirmed offer of employment and is employed in a job relevant to his/her academic qualifications or working experience that cannot be readily taken up by the local work force; and", "확정된 채용 제안이 있고, 학력이나 경력과 관련되며 현지 인력이 쉽게 맡을 수 없는 일자리에 고용될 것", "申請人已獲聘用，而所從事的工作與其學歷或工作經驗有關，且不能輕易在本地覓得適當人選填補；及"),
        ("the remuneration package including income, accommodation, medical and other fringe benefits is broadly commensurate with the prevailing market level for professionals in the BHGSAR.", "소득, 주거, 의료 및 기타 복리후생을 포함한 보수가 백현화랑 특별행정구 전문인력의 시장 수준과 대체로 같을 것", "薪酬福利條件，包括入息、住宿、醫療及其他附帶福利，大致與柏峴화랑特別行政區專業人員的當時市場水平相若。")],
  docs=[D_PHOTO, D_TD, D_ID, D_DEGREE, D_WORK, D_CONTRACT, D_COMPANY, D_OVERSEAS],
  ext_intro=[("Persons admitted under the GEP may apply for extension of stay if they continue to be employed by the same employer in the same capacity. Applications for change of employment should be submitted through the online application for change of employment.", "GEP로 입경한 사람은 같은 고용주에게 같은 직무로 계속 고용된 경우 체류 연장을 신청할 수 있습니다. 이직하려면 고용 변경 온라인 신청을 이용해야 합니다.", "根據「一般就業政策」獲准入境的人士，如繼續以同一身份受僱於同一僱主，可申請延期逗留。如需轉換工作，應透過網上轉換僱主申請服務提出申請。")],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF, ("Employer’s letter confirming continued employment, post and salary", "고용 지속, 직위, 급여를 확인하는 고용주 확인서", "僱主確認繼續僱用、職位及薪酬的信件")],
  after=[("Persons admitted under the GEP are required to take up employment only with the sponsoring employer. Change of employment without the approval of the Director of Immigration is not permitted.", "GEP 입경자는 보증한 고용주에게만 고용되어야 합니다. 출입경사무처장의 승인 없이 이직할 수 없습니다.", "根據「一般就業政策」獲准入境的人士只可受僱於擔保僱主。未得入境事務處處長批准，不得轉換工作。")],
  fields=[F_EMPLOYER, F_POST, F_SALARY, F_CONTRACT, F_QUAL, F_YEARS])

S(k="asmtp", tab="talent", abbr="ASMTP", spec=True, months=24, slip=("輸入內地人才計劃", "ADMISSION SCHEME FOR MAINLAND TALENTS AND PROFESSIONALS"),
  t=("Admission Scheme for Mainland Talents and Professionals", "본토 인재·전문인력 유입계획", "輸入內地人才計劃"), entry="applyemployment", ext="asmtpentrants",
  intro=[("Korean residents of the Mainland who possess special skills, knowledge or experience of value to and not readily available in the BHGSAR may apply to come to work under the Admission Scheme for Mainland Talents and Professionals (ASMTP). The ASMTP is quota-free and non-sector specific.",
          "백현화랑 특별행정구에 가치 있고 현지에서 쉽게 구할 수 없는 특별한 기술, 지식 또는 경험을 가진 본토 대한민국 주민은 본토 인재·전문인력 유입계획(ASMTP)으로 일하러 오도록 신청할 수 있습니다. ASMTP는 정원과 업종 제한이 없습니다.",
          "具備柏峴화랑特別行政區所需而又缺乏的特別技能、知識或經驗的內地韓國居民，可根據「輸入內地人才計劃」申請來柏峴화랑工作。此計劃不設配額，亦不限行業。"),
         ("Overseas Korean nationals holding Republic of Korea passports who have permanent residence overseas, or have been residing overseas for at least one year, may apply under the General Employment Policy instead.", "해외 영주권이 있거나 해외에 1년 이상 거주한 대한민국 여권 소지 재외국민은 대신 일반 취업 정책으로 신청할 수 있습니다.", "持大韓民國護照並擁有海外永久居留權，或已在海外居住最少一年的海外韓國籍人士，可改為根據「一般就業政策」提出申請。")],
  elig=[("there is no security objection and no known record of serious crime in respect of the applicant;", "신청인에 대해 안보상 이의가 없고 알려진 중범죄 기록이 없을 것", "申請人沒有保安方面的疑點及沒有已知的嚴重犯罪紀錄；"),
        ("the applicant has a good education background, normally a first degree in the relevant field;", "통상 관련 분야 학사 학위 이상의 좋은 학력을 갖출 것", "申請人具備良好的教育背景，一般要有相關範疇的學士學位；"),
        ("there is a genuine job vacancy which cannot be readily taken up by the local work force; and", "현지 인력이 쉽게 맡을 수 없는 실제 일자리가 있을 것", "確有職位空缺，而該職位不能輕易在本地覓得適當人選填補；及"),
        ("the remuneration package is broadly commensurate with the prevailing market level for professionals in the BHGSAR.", "보수가 백현화랑 특별행정구 전문인력의 시장 수준과 대체로 같을 것", "薪酬福利條件大致與柏峴화랑特別行政區專業人員的當時市場水平相若。")],
  docs=[D_PHOTO, D_TD, D_DEGREE, D_WORK, D_CONTRACT, D_COMPANY, D_CONSENT],
  ext_intro=[("Persons admitted under the ASMTP may apply for extension of stay if they continue to be employed by the same employer in the same capacity.", "ASMTP로 입경한 사람은 같은 고용주에게 같은 직무로 계속 고용된 경우 체류 연장을 신청할 수 있습니다.", "根據「輸入內地人才計劃」獲准入境的人士，如繼續以同一身份受僱於同一僱主，可申請延期逗留。")],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
  after=[("Successful applicants who are Mainland residents should obtain an Exit-entry Permit for Travelling to and from Baekhyeon Hwarang and a relevant exit endorsement from the relevant Mainland authorities. Change of employment without the approval of the Director of Immigration is not permitted.", "승인된 본토 주민 신청인은 관련 본토 당국에서 백현화랑 왕래 출입경 통행증과 출경 승인을 받아야 합니다. 출입경사무처장의 승인 없이 이직할 수 없습니다.", "獲批准的內地居民申請人應向內地有關當局申領往來柏峴화랑通行證及有關簽注。未得入境事務處處長批准，不得轉換工作。")],
  fields=[F_EMPLOYER, F_POST, F_SALARY, F_CONTRACT, F_QUAL, F_YEARS])

S(k="tps", tab="talent", abbr="GEP(TP) & ASMTP(TP)", spec=True, months=24, slip=("技術專才", "TECHNICAL PROFESSIONALS STREAM"), ext=None,
  t=("General Employment Policy and Admission Scheme for Mainland Talents and Professionals (Technical Professionals Stream)", "일반 취업 정책 및 본토 인재·전문인력 유입계획(기술전문인력 트랙)", "一般就業政策及輸入內地人才計劃（技術專才類別）"), entry="applytpstream",
  intro=[("To address the shortage of manpower in skilled trades, the Technical Professionals Stream (TP Stream) under the GEP and the ASMTP allows a specified number of young and experienced non-degree professionals to work in the specific skilled trades listed on the Technical Professional List (TP List).",
          "숙련 기술직 인력 부족에 대응하기 위해 GEP와 ASMTP의 기술전문인력 트랙은 기술전문인력 목록(TP 목록)에 오른 숙련 기술직에서 경험 있는 젊은 비학위 전문인력이 정해진 인원만큼 일할 수 있게 합니다.",
          "為紓緩技術行業人手短缺，「一般就業政策」及「輸入內地人才計劃」下的「技術專才類別」容許指定數目年輕而具經驗的非學位專業人士，在「技術專才清單」所列的指定技術工種工作。"),
         ("Applications under the TP Stream are subject to quota and restricted to the specific skilled trades on the TP List.", "TP 트랙 신청은 정원이 있으며 TP 목록의 숙련 기술직으로 제한됩니다.", "「技術專才類別」的申請設有配額，並只限於清單所列的指定技術工種。")],
  elig=[("the applicant is aged between 18 and 40 at the time of submission of an entry application;", "입경 신청 제출 시 만 18세 이상 40세 이하일 것", "申請人在遞交入境申請時年齡介乎18至40歲；"),
        ("the applicant meets the minimum qualification requirements specified for the corresponding skilled trade on the TP List, including academic qualifications, work experience, professional qualifications and skills;", "TP 목록의 해당 숙련 기술직에 정해진 학력, 경력, 전문 자격, 기술 등 최소 요건을 충족할 것", "申請人符合清單內相應技術工種所訂明的最低資歷要求，包括學歷、工作經驗、專業資格及技能等；"),
        ("the applicant has a confirmed offer of employment in a skilled trade on the TP List with a remuneration package broadly commensurate with the prevailing market level.", "TP 목록의 숙련 기술직에 확정된 채용 제안이 있고 보수가 시장 수준과 대체로 같을 것", "申請人已獲聘從事清單所列的技術工種，而薪酬福利條件大致與當時市場水平相若。")],
  docs=[D_PHOTO, D_TD, D_ID, ("Proof of trade qualification, licence or trade test certificate", "기술 자격·면허·기능시험 합격 증빙", "技術資歷、牌照或技能測驗證明"), D_WORK, D_CONTRACT, D_COMPANY],
  fields=[F("trade", ("Skilled trade on the TP List", "TP 목록상의 숙련 기술직", "清單所列的技術工種"), "select", req=True, o=[
      ["elec", ("Electrical engineering technician", "전기공학 기술자", "電機工程技術員")], ["mech", ("Mechanical engineering technician", "기계공학 기술자", "機械工程技術員")],
      ["aviation", ("Aircraft maintenance technician", "항공기 정비 기술자", "飛機維修技術員")], ["chef", ("Chef (specialised cuisine)", "조리사(전문 요리)", "廚師（特色菜式）")],
      ["build", ("Building services technician", "건물설비 기술자", "屋宇設備技術員")], ["it", ("Information technology technician", "정보기술 기술자", "資訊科技技術員")]]),
      F_EMPLOYER, F_POST, F_SALARY, F_YEARS])

S(k="techtas", tab="talent", abbr="TechTAS", spec=True, months=24, slip=("科技人才入境計劃", "TECHNOLOGY TALENT ADMISSION SCHEME"),
  t=("Technology Talent Admission Scheme", "과학기술 인재 입경 제도", "科技人才入境計劃"), entry="applytechtas", ext="ttasentrants",
  intro=[("The Technology Talent Admission Scheme (TechTAS) provides a fast-track arrangement for eligible companies to admit non-local technology talent to undertake research and development (R&D) work in the BHGSAR. A company allotted with a quota by the Innovation and Technology Commission can sponsor an eligible person to apply for an employment visa/entry permit.",
          "과학기술 인재 입경 제도(TechTAS)는 자격을 갖춘 기업이 백현화랑 특별행정구에서 연구개발(R&D) 업무를 맡을 역외 과학기술 인재를 신속히 받아들일 수 있도록 하는 제도입니다. 혁신과기서에서 정원을 배정받은 기업은 자격 있는 사람의 취업 비자·입경허가 신청을 보증할 수 있습니다.",
          "「科技人才入境計劃」為合資格公司提供快速處理安排，以輸入非本地科技人才在柏峴화랑特別行政區從事研發工作。獲創新科技署分配配額的公司可擔保合資格人士申請工作簽證／進入許可證。")],
  elig=[("the employing company has a valid quota allotted by the Innovation and Technology Commission;", "고용 회사가 혁신과기서가 배정한 유효한 정원을 보유할 것", "僱用公司持有由創新科技署分配的有效配額；"),
        ("the applicant is employed to engage in research and development work in a technology area specified for the quota; and", "정원에 지정된 기술 분야의 연구개발 업무를 위해 고용될 것", "申請人受僱從事配額所指明科技範疇的研發工作；及"),
        ("the remuneration package is broadly commensurate with the prevailing market level.", "보수가 시장 수준과 대체로 같을 것", "薪酬福利條件大致與當時市場水平相若。")],
  docs=[D_PHOTO, D_TD, D_ID, ("Quota allotment letter issued by the Innovation and Technology Commission", "혁신과기서 발행 정원 배정 통지서", "創新科技署發出的配額分配信"), D_DEGREE, D_CONTRACT],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
  fields=[F("quota", ("Quota reference number", "정원 배정 번호", "配額編號"), req=True, ph="TTAS-0000"), F("area", ("Technology area", "기술 분야", "科技範疇"), "select", req=True, o=[
      ["ai", ("Artificial intelligence", "인공지능", "人工智能")], ["bio", ("Biotechnology", "바이오기술", "生物科技")], ["fin", ("Financial technologies", "금융기술", "金融科技")],
      ["cyber", ("Cybersecurity", "사이버보안", "網絡安全")], ["micro", ("Microelectronics", "마이크로전자", "微電子")], ["new", ("New energy", "신에너지", "新能源")]]),
      F_EMPLOYER, F_POST, F_SALARY, F_QUAL])

S(k="iang", tab="talent", abbr="IANG", spec=True, months=24, slip=("非本地畢業生留柏峴／回柏峴就業安排", "IMMIGRATION ARRANGEMENTS FOR NON-LOCAL GRADUATES"),
  t=("Immigration Arrangements for Non-local Graduates", "역외 졸업생 출입경 특례", "非本地畢業生留柏峴／回柏峴就業安排"), entry_loc="np", entry="applyiang", ext="iangentrants",
  intro=[("Applicants who are/were non-local students and have obtained an undergraduate or higher qualification in a full-time and locally-accredited programme in the BHGSAR (non-local graduates) may apply to stay/return and work in the BHGSAR under the Immigration Arrangements for Non-local Graduates (IANG). The IANG is quota-free and non-sector specific.",
          "백현화랑 특별행정구에서 현지 인증 전일제 과정의 학사 이상 학위를 취득한 현재·과거 역외 학생(역외 졸업생)은 역외 졸업생 출입경 특례(IANG)로 백현화랑 특별행정구에 남거나 돌아와 일하도록 신청할 수 있습니다. IANG는 정원과 업종 제한이 없습니다.",
          "現時或曾經為非本地學生，並在柏峴화랑特別行政區修讀全日制經本地評審課程而取得學士學位或更高資歷的人士（非本地畢業生），可根據「非本地畢業生留柏峴／回柏峴就業安排」申請留下或回來工作。此安排不設配額，亦不限行業。")],
  elig=[("Fresh graduates (applications submitted within six months after the date of graduation) are not required to have secured an offer of employment upon application;", "신규 졸업생(졸업일로부터 6개월 이내 신청)은 신청 시 채용 제안이 필요하지 않음", "應屆畢業生（在畢業日期後六個月內提出申請）在申請時無須已獲聘用；"),
        ("Returning graduates (applications submitted after six months from the date of graduation) must have secured an offer of employment at a level commonly taken up by degree holders with remuneration at market level;", "복귀 졸업생(졸업일로부터 6개월 이후 신청)은 학위 소지자가 통상 맡는 수준의 일자리와 시장 수준 보수의 채용 제안이 있어야 함", "回柏峴的畢業生（在畢業日期六個月後提出申請）必須已獲聘從事一般由學位持有人擔任的工作，而薪酬福利條件須符合市場水平；"),
        ("there is no security objection and no known record of serious crime in respect of the applicant.", "신청인에 대해 안보상 이의가 없고 알려진 중범죄 기록이 없을 것", "申請人沒有保安方面的疑點及沒有已知的嚴重犯罪紀錄。")],
  docs=[D_PHOTO, D_TD, D_ID, ("Graduation certificate / official transcript showing the qualification obtained in the BHGSAR", "백현화랑 특별행정구에서 취득한 학위의 졸업증명서·공식 성적증명서", "在柏峴화랑特別行政區取得資歷的畢業證書／正式成績單"), ("Employment contract (for returning graduates)", "고용계약서(복귀 졸업생)", "僱傭合約（適用於回柏峴的畢業生）")],
  ext_intro=[("Persons admitted under the IANG may apply for extension of stay if they have taken up employment at a level commonly taken up by degree holders with remuneration at market level.", "IANG로 입경한 사람은 학위 소지자가 통상 맡는 수준의 일자리에 시장 수준 보수로 취업한 경우 체류 연장을 신청할 수 있습니다.", "根據此安排獲准入境的人士，如已受聘從事一般由學位持有人擔任的工作而薪酬福利符合市場水平，可申請延期逗留。")],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
  fields=[F("igtype", ("Type of applicant", "신청인 유형", "申請人類別"), "radio", req=True, o=[["fresh", ("Fresh graduate (within 6 months after graduation)", "신규 졸업생(졸업 후 6개월 이내)", "應屆畢業生（畢業後六個月內）")], ["return", ("Returning graduate", "복귀 졸업생", "回柏峴的畢業生")]]),
          F_INST, F("prog", ("Programme of study", "학위 과정", "修讀課程"), req=True), F("graddate", ("Date of graduation (YYYY-MM-DD)", "졸업일(YYYY-MM-DD)", "畢業日期（YYYY-MM-DD）"), req=True, v="date", ph="YYYY-MM-DD"),
          F("employer", ("Name of employer (returning graduates)", "고용주 이름(복귀 졸업생)", "僱主名稱（回柏峴的畢業生）"), req=True, full=True, showIf={"n": "igtype", "eq": "return"})])

S(k="qmas", tab="talent", abbr="QMAS", spec=True, months=36, slip=("優秀人才入境計劃", "QUALITY MIGRANT ADMISSION SCHEME"),
  t=("Quality Migrant Admission Scheme", "우수 인재 입경 제도", "優秀人才入境計劃"), entry="applyqmas", ext="qmasentrants",
  intro=[("The Quality Migrant Admission Scheme (QMAS) seeks to attract highly skilled or talented persons to settle in the BHGSAR in order to enhance its economic competitiveness. Applicants are not required to have secured an offer of local employment before applying. Applicants have to fulfil a set of prerequisites before they can be awarded points under either the General Points Test or the Achievement-based Points Test, and compete with other applicants for quota allocation.",
          "우수 인재 입경 제도(QMAS)는 고숙련자나 재능 있는 사람이 백현화랑 특별행정구에 정착하도록 유치하여 경제 경쟁력을 높이기 위한 제도입니다. 신청 전에 현지 채용 제안을 받을 필요가 없습니다. 신청인은 기본 요건을 충족한 뒤 일반 점수제 또는 성취 기반 점수제로 점수를 받아 다른 신청인과 정원 배정을 두고 경쟁합니다.",
          "「優秀人才入境計劃」旨在吸引高技術人才或優才來柏峴화랑定居，以提升柏峴화랑的經濟競爭力。申請人無須事先獲得本地僱主聘任。申請人須先符合基本資格，然後選擇以「綜合計分制」或「成就計分制」獲取分數，與其他申請人競爭配額。")],
  elig=[("Age: the applicant must be 18 years old or above at the time of submitting the application;", "나이: 신청 제출 시 만 18세 이상", "年齡：申請人在提交申請時必須年滿18歲或以上；"),
        ("Financial requirement: the applicant must demonstrate that he/she is able to support and accommodate himself/herself and dependants on his/her own;", "재정 요건: 본인과 부양가족을 스스로 부양하고 거처를 마련할 수 있음을 입증", "財政要求：申請人必須證明能獨力承擔其本人及受養人的生活和住宿；"),
        ("Good character: the applicant must not have any criminal record or adverse immigration record;", "품행: 범죄 기록이나 불리한 출입경 기록이 없을 것", "良好品格：申請人不得有任何刑事罪行紀錄或不良入境紀錄；"),
        ("Language proficiency: the applicant must have a good command of written and spoken Korean, Chinese or English;", "언어 능력: 한국어, 중국어 또는 영어 작문·회화에 능통", "語文能力：申請人須具備良好的韓文、中文或英文讀寫和聽說能力；"),
        ("Basic education: the applicant should have a good education background, normally a first degree from a recognised university or tertiary educational institution.", "기본 학력: 통상 인정된 대학이나 고등교육기관의 학사 학위", "基本學歷：申請人須具備良好學歷，一般要求為獲認可大學或高等教育院校所頒授的學士學位。")],
  docs=[D_PHOTO, D_TD, D_ID, D_DEGREE, D_WORK, D_FIN, ("Proof of outstanding achievement (Achievement-based Points Test)", "탁월한 성취 증빙(성취 기반 점수제)", "傑出成就證明（成就計分制）")],
  ext_intro=[("Persons admitted under the QMAS may apply for extension of stay. They should have taken up gainful employment, established or joined in business, or have demonstrated their contribution to the economy of the BHGSAR. Successful applicants will normally be granted an extension of stay of three years.",
              "QMAS로 입경한 사람은 체류 연장을 신청할 수 있습니다. 유급 고용 상태이거나 사업을 설립·참여했거나 백현화랑 특별행정구 경제에 기여했음을 입증해야 합니다. 승인되면 통상 3년의 체류 연장이 허가됩니다.",
              "根據「優秀人才入境計劃」獲准入境的人士可申請延期逗留。他們應已受僱從事有報酬的工作、開辦或參與業務，或已證明對柏峴화랑特別行政區經濟有所貢獻。申請獲批准的人士一般會獲准延期逗留三年。")],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
  fields=[F("track", ("Points test", "점수제 유형", "計分制度"), "radio", req=True, o=[["gpt", ("General Points Test", "일반 점수제", "綜合計分制")], ["apt", ("Achievement-based Points Test", "성취 기반 점수제", "成就計分制")]]),
          F("points", ("Self-assessed points (General Points Test)", "자체 평가 점수(일반 점수제)", "自我評估分數（綜合計分制）"), req=True, v="num", im="numeric", showIf={"n": "track", "eq": "gpt"}),
          F("award", ("Outstanding achievement / award", "탁월한 성취·수상 내역", "傑出成就／獎項"), "textarea", req=True, full=True, showIf={"n": "track", "eq": "apt"}),
          F_QUAL, F_YEARS])

S(k="assg", tab="talent", abbr="ASSG", spec=True, months=12, slip=("第二代韓籍柏峴화랑永久性居民入境計劃", "ADMISSION SCHEME FOR THE SECOND GENERATION OF KOREAN BHG PERMANENT RESIDENTS"),
  t=("Admission Scheme for the Second Generation of Korean Baekhyeon Hwarang Permanent Residents", "한국계 백현화랑 영주민 2세 입경 제도", "第二代韓籍柏峴화랑永久性居民入境計劃"), entry_loc="np", entry="secondgenerationbhpr", ext="assgentrants",
  intro=[("Persons who are the second generation of emigrated Korean Baekhyeon Hwarang permanent residents from overseas may apply to return to work in the BHGSAR under the Scheme. Applicants are not required to have secured an offer of employment upon application.",
          "해외로 이주한 한국계 백현화랑 영주민의 2세는 이 제도로 백현화랑 특별행정구에 돌아와 일하도록 신청할 수 있습니다. 신청할 때 채용 제안이 필요하지 않습니다.",
          "已移居海外的韓籍柏峴화랑永久性居民的第二代，可根據此計劃申請回來柏峴화랑工作。申請人在申請時無須已獲聘用。")],
  elig=[("aged between 18 and 40 at the time of application;", "신청 시 만 18세 이상 40세 이하", "申請時年齡介乎18至40歲；"),
        ("born overseas (i.e. not in the Mainland, the BHGSAR or other special administrative regions);", "해외 출생(본토, 백현화랑 특별행정구 또는 기타 특별행정구가 아닌 곳)", "在海外出生（即並非在內地、柏峴화랑特別行政區或其他特別行政區出生）；"),
        ("have at least one parent who is a holder of a valid Baekhyeon Hwarang Permanent Identity Card and was a Korean national who had settled overseas at the time of the applicant’s birth;", "부모 중 최소 1명이 유효한 백현화랑 영구 신분증 소지자이고, 신청인 출생 당시 해외에 정착한 대한민국 국민이었을 것", "父母其中最少一方為有效柏峴화랑永久性居民身份證持有人，並在申請人出生時為已在海外定居的大韓民國國民；"),
        ("have a good education background, normally a first degree;", "통상 학사 학위 이상의 좋은 학력", "具備良好的教育背景，一般為學士學位；"),
        ("proficient in written and spoken Korean, Chinese or English; and", "한국어, 중국어 또는 영어 작문·회화에 능통", "具備良好的韓文、中文或英文書寫及口語能力；及"),
        ("have sufficient financial means to meet living expenses without recourse to public funds.", "공적 자금에 의존하지 않고 생활비를 감당할 충분한 재정 능력", "有足夠經濟能力應付生活開支，而無須依賴公共援助。")],
  docs=[D_PHOTO, D_TD, ("The parent’s Baekhyeon Hwarang Permanent Identity Card", "부모의 백현화랑 영구 신분증", "父或母的柏峴화랑永久性居民身份證"), ("The applicant’s birth certificate showing the parent’s particulars", "부모 인적사항이 적힌 신청인의 출생증명서", "載有父或母資料的申請人出生證明書"), D_DEGREE, D_FIN],
  ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
  fields=[F("pname", ("Name of the parent who is a BHG permanent resident", "백현화랑 영주민인 부모의 성명", "屬柏峴화랑永久性居民的父或母姓名"), req=True), F("pid", ("Parent’s identity card number", "부모의 신분증 번호", "父或母的身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True), F_QUAL])

S(k="vpas", tab="talent", abbr="VPAS", spec=True, months=24, slip=("職業專才入境計劃", "VOCATIONAL PROFESSIONALS ADMISSION SCHEME"), deps=True,
  t=("Vocational Professionals Admission Scheme", "직업 전문인력 입경 제도", "職業專才入境計劃"), entry_loc="np", entry="applyvpas", ext=None,
  intro=[("The Vocational Professionals Admission Scheme (VPAS) is a pilot scheme which enables non-local students enrolled in eligible Vocational Training Council (VTC) full-time Higher Diploma programmes to apply upon graduation to remain in the BHGSAR for employment in the skilled trades relevant to their programmes of study.",
          "직업 전문인력 입경 제도(VPAS)는 직업훈련국(VTC)의 지정 전일제 고등 디플로마 과정에 등록한 역외 학생이 졸업 후 전공과 관련된 숙련 기술직에 취업하기 위해 백현화랑 특별행정구에 남도록 신청할 수 있게 하는 시범 제도입니다.",
          "「職業專才入境計劃」是一項試行計劃，讓修讀職業訓練局合資格全日制高級文憑課程的非本地學生，在畢業後申請留在柏峴화랑特別行政區從事與其修讀課程相關的技術工種工作。")],
  elig=[("the applicant has completed an eligible VTC full-time Higher Diploma programme within three academic years after admission;", "입학 후 3학년도 이내에 VTC 지정 전일제 고등 디플로마 과정을 수료할 것", "申請人在入學後三個學年內完成合資格的職業訓練局全日制高級文憑課程；"),
        ("the application is submitted no later than 12 months after the date of graduation; and", "졸업일로부터 12개월 이내에 신청할 것", "申請在畢業日期後12個月內提出；及"),
        ("the applicant has secured an offer of employment in a skilled trade relevant to the programme of study.", "전공과 관련된 숙련 기술직 채용 제안을 받을 것", "申請人已獲聘從事與修讀課程相關的技術工種。")],
  docs=[D_PHOTO, D_TD, D_ID, ("Graduation certificate of the VTC Higher Diploma programme", "VTC 고등 디플로마 졸업증명서", "職業訓練局高級文憑課程畢業證書"), D_CONTRACT],
  fields=[F("prog", ("VTC Higher Diploma programme", "VTC 고등 디플로마 과정", "職業訓練局高級文憑課程"), req=True, full=True), F("graddate", ("Date of graduation (YYYY-MM-DD)", "졸업일(YYYY-MM-DD)", "畢業日期（YYYY-MM-DD）"), req=True, v="date", ph="YYYY-MM-DD"), F_EMPLOYER, F_POST, F_SALARY])


# ============================================================================= Foreign Domestic Helpers / Imported Workers
FDH_ELIG = [("the applicant has the qualifications and relevant working experience as a domestic helper;", "가사도우미로서의 자격과 관련 경력이 있을 것", "申請人具備擔任家庭傭工的資格及相關工作經驗；"),
            ("the employer is a bona fide resident of the BHGSAR and is prepared to offer the helper the Minimum Allowable Wage (currently BH$5,100 per month), free food (or a food allowance of not less than BH$1,236 per month) and suitable accommodation with reasonable privacy;", "고용주가 백현화랑 특별행정구의 실거주자이고 최저 허용 임금(현재 월 BH$5,100), 무료 식사(또는 월 BH$1,236 이상의 식비 수당), 적절한 사생활이 보장되는 숙소를 제공할 것", "僱主為柏峴화랑特別行政區的真正居民，並願意向傭工提供規定最低工資（現時為每月5,100元）、免費膳食（或每月不少於1,236元的膳食津貼）及具合理私隱的合適居所；"),
            ("the employer’s household income is not less than BH$15,000 per month or he/she has assets of equivalent amount to support the employment;", "고용주 가구의 월 소득이 BH$15,000 이상이거나 고용을 뒷받침할 같은 수준의 자산이 있을 것", "僱主的家庭入息不少於每月15,000元，或具備同等金額的資產以支持聘用；"),
            ("the helper and the employer have entered into a Standard Employment Contract (ID 407).", "가사도우미와 고용주가 표준 고용계약서(ID 407)를 체결할 것", "傭工與僱主已簽訂「僱用合約」（ID 407）。")]
FDH_INTRO = [("Foreign domestic helpers may be admitted to work in the BHGSAR under the Standard Employment Contract (ID 407). An application for an employment visa may be favourably considered if the following criteria are met. Successful applicants will normally be admitted for a period of two years or the duration of the employment contract.",
              "외국인 가사도우미는 표준 고용계약서(ID 407)에 따라 백현화랑 특별행정구에서 일하도록 입경이 허가될 수 있습니다. 다음 요건을 충족하면 취업 비자 신청이 긍정적으로 검토됩니다. 승인되면 통상 2년 또는 고용계약 기간 동안 입경이 허가됩니다.",
              "外籍家庭傭工可根據「僱用合約」（ID 407）獲准來柏峴화랑特別行政區工作。如符合以下準則，工作簽證申請可獲考慮。申請獲批准的人士一般會獲准逗留兩年或合約期。")]
FDH_DOCS = [D_PHOTO, D_TD, ("Standard Employment Contract (ID 407) signed by the employer and the helper", "고용주와 가사도우미가 서명한 표준 고용계약서(ID 407)", "由僱主及傭工簽署的「僱用合約」（ID 407）"), ("Schedule of Accommodation and Domestic Duties (ID 407G)", "숙소 및 가사 업무 명세서(ID 407G)", "住宿及家務安排表（ID 407G）"), ("Employer’s proof of income or assets", "고용주의 소득 또는 자산 증빙", "僱主的入息或資產證明"), ("Employer’s Baekhyeon Hwarang identity card", "고용주의 백현화랑 신분증", "僱主的柏峴화랑身份證")]
FDH_FIELDS = [F("emname", ("Name of employer", "고용주 성명", "僱主姓名"), req=True), F("emid", ("Employer’s identity card number", "고용주 신분증 번호", "僱主身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
              F("emaddr", ("Address of employment", "근무지 주소", "工作地址"), "textarea", req=True, full=True),
              F("wage", ("Monthly wage (BH$)", "월 임금(BH$)", "每月工資（柏峴화랑元）"), req=True, v="num", im="numeric", ph="5100"),
              F("cstart", ("Contract commencement date (YYYY-MM-DD)", "계약 시작일(YYYY-MM-DD)", "合約開始日期（YYYY-MM-DD）"), req=True, v="anydate", ph="YYYY-MM-DD")]
S(k="fdh", tab="labour", abbr="FDH", deps=False, roa=False, multi=False, months=24, slip=("外籍家庭傭工", "FOREIGN DOMESTIC HELPER"),
  t=("Entry Visa for New Foreign Domestic Helper", "신규 외국인 가사도우미 입경 비자", "新聘外籍家庭傭工入境簽證"), entry_loc="np", entry="entryvisafornewfdh",
  intro=FDH_INTRO, elig=FDH_ELIG, docs=FDH_DOCS, fields=FDH_FIELDS,
  after=[("Foreign domestic helpers must work and reside in the employer’s residence as specified in the employment contract. They are not allowed to take up any other employment or to start a business. Change of employer within the contract period is normally not permitted except under exceptional circumstances.",
          "외국인 가사도우미는 고용계약서에 적힌 고용주의 주거지에서 일하고 거주해야 합니다. 다른 일자리에 취업하거나 사업을 시작할 수 없습니다. 예외적인 상황을 제외하고 계약 기간 중 고용주 변경은 통상 허용되지 않습니다.",
          "外籍家庭傭工必須按僱傭合約在僱主的住所工作及居住，不得從事其他工作或開辦業務。除特殊情況外，一般不容許在合約期內轉換僱主。")])
for _k, _slug, _t, _p in [
        ("fdhrenew", "fdhcontractrenewal", ("Foreign Domestic Helpers – Contract Renewal (Working for Same Employer)", "외국인 가사도우미 – 계약 갱신(같은 고용주)", "外籍家庭傭工 – 續約（為同一僱主工作）"),
         ("A foreign domestic helper who will continue to work for the same employer upon expiry of the current contract may apply for extension of stay for contract renewal. The “Smart Renewal” service allows the helper to apply online while staying in or outside the BHGSAR.", "현 계약 만료 후 같은 고용주를 위해 계속 일할 외국인 가사도우미는 계약 갱신을 위한 체류 연장을 신청할 수 있습니다. \"스마트 갱신\" 서비스로 백현화랑 특별행정구 안팎에서 온라인으로 신청할 수 있습니다.", "現有合約屆滿後繼續為同一僱主工作的外籍家庭傭工，可就續約申請延期逗留。「智方便續約」服務讓傭工無論身處柏峴화랑特別行政區境內或境外，均可在網上提出申請。")),
        ("fdhcomplete", "fdhcompletecontract", ("Foreign Domestic Helpers – Completion of Remaining Period of Current Contract", "외국인 가사도우미 – 현 계약 잔여 기간 완료", "外籍家庭傭工 – 完成現有合約的餘下期間"),
         ("A foreign domestic helper whose limit of stay was granted short of the contract period (e.g. due to passport validity) may apply for an extension of stay to complete the remaining period of the current contract with the same employer.", "여권 유효기간 등으로 계약 기간보다 짧게 체류 기한을 받은 외국인 가사도우미는 같은 고용주와의 현 계약 잔여 기간을 채우기 위해 체류 연장을 신청할 수 있습니다.", "因護照有效期等原因而獲准逗留期限短於合約期的外籍家庭傭工，可申請延期逗留，以完成與同一僱主的現有合約餘下期間。")),
        ("fdhchange", "fdhchangeofemployer", ("Foreign Domestic Helpers – Change of Employer", "외국인 가사도우미 – 고용주 변경", "外籍家庭傭工 – 轉換僱主"),
         ("A foreign domestic helper whose contract has been prematurely terminated may apply for a change of employer only under exceptional circumstances, such as transfer, migration, death or financial reasons of the original employer, or where there is evidence that the helper has been abused or exploited.", "계약이 조기 해지된 외국인 가사도우미는 원 고용주의 전근·이민·사망·재정 사정이나 가사도우미가 학대·착취당한 증거가 있는 경우 등 예외적인 상황에서만 고용주 변경을 신청할 수 있습니다.", "合約被提前終止的外籍家庭傭工，只可在特殊情況下申請轉換僱主，例如原僱主調職、移民、死亡或因經濟理由，或有證據證明傭工曾受虐待或剝削。")),
        ("fdhvisitor", "fdhvisitor", ("Former Foreign Domestic Helpers – Extension of Stay on Visitor Status", "전 외국인 가사도우미 – 방문객 신분 체류 연장", "前外籍家庭傭工 – 以訪客身份延期逗留"),
         ("A former foreign domestic helper whose contract has expired or been terminated may apply to stay in the BHGSAR as a visitor for a short period, for example to deal with outstanding matters before departure.", "계약이 만료되거나 해지된 전 외국인 가사도우미는 출국 전 남은 일을 처리하는 등의 이유로 단기간 방문객으로 체류하도록 신청할 수 있습니다.", "合約已屆滿或被終止的前外籍家庭傭工，可申請以訪客身份短暫留在柏峴화랑特別行政區，例如在離境前處理未完事項。"))]:
    S(k=_k, tab="labour", abbr="FDH", deps=False, roa=False, multi=False, months=24 if _k != "fdhvisitor" else 1, slip=("外籍家庭傭工", "FOREIGN DOMESTIC HELPER") if _k != "fdhvisitor" else ("訪客", "VISITOR"),
      t=_t, entry=None, ext=_slug, intro=[_p] + FDH_INTRO, elig=FDH_ELIG if _k != "fdhvisitor" else [], ext_intro=[_p],
      ext_docs=[D_LAST_TD, D_IDX] + ([("New Standard Employment Contract (ID 407)", "새 표준 고용계약서(ID 407)", "新的「僱用合約」（ID 407）")] if _k in ("fdhrenew", "fdhchange") else []) + ([("Return air ticket or travel itinerary", "왕복 항공권 또는 여행 일정표", "回程機票或行程表")] if _k == "fdhvisitor" else []),
      fields=FDH_FIELDS if _k != "fdhvisitor" else [F("reason", ("Reason for extension of stay", "체류 연장 사유", "延期逗留的原因"), "textarea", req=True, full=True)], fdhsub=True)

IMP_INTRO = {
    "icw": ("The Special Scheme to Import Care Workers for Residential Care Homes, administered by the Social Welfare Department, allows operators of residential care homes to import care workers. Employers need to first apply for quota(s); upon the grant of quota(s), the employer shall arrange for each prospective care worker to submit a visa/entry permit application to the Immigration Department.",
            "사회복지서가 운영하는 요양시설 돌봄 인력 수입 특별 제도는 요양시설 운영자가 돌봄 인력을 수입할 수 있게 합니다. 고용주는 먼저 정원을 신청해야 하며, 정원을 배정받으면 각 예정 돌봄 인력이 출입경사무처에 비자·입경허가를 신청하도록 해야 합니다.",
            "社會福利署推行的「補充院舍照顧員特別計劃」讓安老及殘疾人士院舍的營辦者輸入照顧員。僱主須先申請配額，獲批配額後，須安排每名擬輸入的照顧員向入境事務處遞交簽證／進入許可證申請。"),
    "slis": ("The Sector-specific Labour Importation Schemes allow employers in specific sectors (e.g. construction, transport, aviation) to import labour. Employers need to first apply to the concerned bureaux/departments for quota(s); upon the grant of quota(s), the employer shall arrange for each prospective worker to submit a visa/entry permit application.",
             "업종별 노동력 수입 제도는 건설, 운수, 항공 등 특정 업종의 고용주가 노동력을 수입할 수 있게 합니다. 고용주는 먼저 관련 정책국·부서에 정원을 신청해야 하며, 정원을 배정받으면 각 예정 노동자가 비자·입경허가를 신청하도록 해야 합니다.",
             "「行業專屬輸入勞工計劃」讓指定行業（例如建造業、運輸業、航空業）的僱主輸入勞工。僱主須先向有關政策局／部門申請配額，獲批配額後，須安排每名擬輸入的勞工遞交簽證／進入許可證申請。"),
    "esls": ("The Enhanced Supplementary Labour Scheme (ESLS), administered by the Labour Department, allows employers with genuine difficulties in recruiting suitable workers locally to import workers at technician level or below. Employers need to first apply for an approval-in-principle.",
             "노동처가 운영하는 강화 보충 노동력 제도(ESLS)는 현지에서 적합한 인력을 구하기 어려운 고용주가 기술자 이하 수준의 노동자를 수입할 수 있게 합니다. 고용주는 먼저 원칙적 승인을 신청해야 합니다.",
             "勞工處推行的「補充勞工優化計劃」讓在本地確實難以招聘合適人手的僱主輸入技術員級別或以下的勞工。僱主須先申請原則上批准。"),
}
for _k, _abbr, _t, _e, _x in [
        ("icw", "ICW", ("Special Scheme to Import Care Workers for Residential Care Homes", "요양시설 돌봄 인력 수입 특별 제도", "補充院舍照顧員特別計劃"), "applyicw", "icwentrants"),
        ("slis", "SLIS", ("Sector-specific Labour Importation Schemes", "업종별 노동력 수입 제도", "行業專屬輸入勞工計劃"), "applyslis", "slisentrants"),
        ("esls", "ESLS", ("Enhanced Supplementary Labour Scheme", "강화 보충 노동력 제도", "補充勞工優化計劃"), "applyimportedworker", "slsentrants")]:
    S(k=_k, tab="labour", abbr=_abbr, deps=False, roa=False, multi=False, months=24, slip=("輸入勞工", "IMPORTED LABOUR"), t=_t, entry=_e, ext=_x,
      intro=[IMP_INTRO[_k]],
      elig=[("the employer has been granted quota(s) / approval-in-principle for the importation;", "고용주가 수입을 위한 정원 또는 원칙적 승인을 받았을 것", "僱主已獲批輸入勞工的配額／原則上批准；"),
            ("the applicant possesses the skills and experience required for the post; and", "신청인이 해당 직위에 필요한 기술과 경력을 갖출 것", "申請人具備有關職位所需的技能及經驗；及"),
            ("the wage and terms of employment are not less favourable than those specified for the quota.", "임금과 고용 조건이 정원에 정해진 것보다 불리하지 않을 것", "工資及僱用條件不遜於配額所訂明者。")],
      docs=[D_PHOTO, D_TD, ("Quota approval letter / approval-in-principle", "정원 승인서·원칙적 승인서", "配額批准信／原則上批准信"), D_CONTRACT, ("Proof of relevant skills and working experience", "관련 기술 및 경력 증빙", "相關技能及工作經驗證明")],
      ext_docs=[D_LAST_TD, D_IDX, D_EMP_PROOF],
      fields=[F("quota", ("Quota / approval reference number", "정원·승인 번호", "配額／批准編號"), req=True), F_EMPLOYER, F_POST, F_SALARY])

# ============================================================================= Investment / Training / Other Employment
S(k="ncies", tab="invest", abbr="New CIES", spec=True, months=24, slip=("新資本投資者入境計劃", "NEW CAPITAL INVESTMENT ENTRANT SCHEME"),
  t=("New Capital Investment Entrant Scheme", "신규 자본 투자자 입경 제도", "新資本投資者入境計劃"), entry="applynewcies", ext="newciesentrants",
  intro=[("The New Capital Investment Entrant Scheme (New CIES) aims to attract more new capital to the BHGSAR. Eligible applicants who have net assets of not less than BH$30 million and make an investment of not less than BH$30 million in permissible investment assets may apply to reside in the BHGSAR. Applicants first apply to Invest Baekhyeon Hwarang for assessment of net assets; upon approval-in-principle, they may apply for an entry visa/permit.",
          "신규 자본 투자자 입경 제도(New CIES)는 더 많은 신규 자본을 백현화랑 특별행정구로 끌어들이기 위한 제도입니다. 순자산 BH$3,000만 이상을 보유하고 허용 투자 자산에 BH$3,000만 이상을 투자하는 사람은 백현화랑 특별행정구 거주를 신청할 수 있습니다. 신청인은 먼저 백현화랑 투자추진처에 순자산 평가를 신청하고, 원칙적 승인을 받으면 입경 비자·허가를 신청할 수 있습니다.",
          "「新資本投資者入境計劃」旨在吸引更多新資金到柏峴화랑特別行政區。淨資產不少於3,000萬元，並在獲許投資資產作出不少於3,000萬元投資的合資格申請人，可申請來柏峴화랑居留。申請人須先向投資推廣署申請淨資產評估，獲原則上批准後，可申請入境簽證／許可證。")],
  elig=[("the applicant is aged 18 or above;", "만 18세 이상일 것", "申請人年滿18歲或以上；"),
        ("the applicant has net assets of not less than BH$30 million throughout the two years before the application;", "신청 전 2년 동안 계속 순자산 BH$3,000만 이상을 보유할 것", "申請人在申請前兩年內一直擁有不少於3,000萬元的淨資產；"),
        ("the applicant has obtained approval-in-principle from Invest Baekhyeon Hwarang and has made the committed investment.", "백현화랑 투자추진처의 원칙적 승인을 받고 약정한 투자를 완료할 것", "申請人已獲投資推廣署原則上批准，並已作出承諾的投資。")],
  docs=[D_PHOTO, D_TD, ("Approval-in-principle letter issued by Invest Baekhyeon Hwarang", "백현화랑 투자추진처 발행 원칙적 승인서", "投資推廣署發出的原則上批准信"), ("Proof of the committed investment", "약정 투자 증빙", "已作出承諾投資的證明"), D_FIN],
  ext_docs=[D_LAST_TD, D_IDX, ("Proof that the investment has been maintained", "투자가 유지되고 있음을 보여 주는 증빙", "投資一直維持的證明")],
  fields=[F("aip", ("Approval-in-principle reference number", "원칙적 승인 번호", "原則上批准編號"), req=True), F("amount", ("Amount invested (BH$)", "투자 금액(BH$)", "投資金額（柏峴화랑元）"), req=True, v="num", im="numeric")])

S(k="cies", tab="invest", abbr="CIES", spec=True, months=24, slip=("資本投資者入境計劃", "CAPITAL INVESTMENT ENTRANT SCHEME"),
  t=("Capital Investment Entrant Scheme", "자본 투자자 입경 제도", "資本投資者入境計劃"), entry=None, ext="ciesentrants",
  intro=[("The Capital Investment Entrant Scheme (CIES) has been suspended for new applications. Persons who were admitted under the CIES and their dependants may continue to apply for extension of stay, provided that they continue to meet the requirements of the scheme, including maintaining the committed investment.",
          "자본 투자자 입경 제도(CIES)는 신규 신청이 중단되었습니다. CIES로 입경한 사람과 그 부양가족은 약정 투자 유지 등 제도 요건을 계속 충족하면 체류 연장을 계속 신청할 수 있습니다.",
          "「資本投資者入境計劃」已暫停接受新申請。根據此計劃獲准入境的人士及其受養人，如繼續符合計劃的規定（包括維持承諾的投資），可繼續申請延期逗留。")],
  ext_docs=[D_LAST_TD, D_IDX, ("Proof that the investment has been maintained", "투자가 유지되고 있음을 보여 주는 증빙", "投資一直維持的證明")],
  fields=[F("amount", ("Amount of investment maintained (BH$)", "유지 중인 투자 금액(BH$)", "維持的投資金額（柏峴화랑元）"), req=True, v="num", im="numeric")])

S(k="inv", tab="invest", abbr="Investment", spec=True, months=12, slip=("投資", "INVESTMENT"),
  t=("Investment as Entrepreneurs", "기업가 투자", "以企業家身份投資"), entry="applyinvestment", ext="gepentrants",
  intro=[("Persons who wish to enter the BHGSAR for investment as entrepreneurs under the General Employment Policy, i.e. to establish or join in business, may apply if they are in a position to make substantial contribution to the economy of the BHGSAR.",
          "일반 취업 정책에 따라 기업가로서 투자하기 위해, 즉 사업을 설립하거나 참여하기 위해 백현화랑 특별행정구에 입경하려는 사람은 백현화랑 특별행정구 경제에 상당한 기여를 할 수 있는 경우 신청할 수 있습니다.",
          "擬根據「一般就業政策」以企業家身份來柏峴화랑投資，即開辦或參與業務的人士，如能對柏峴화랑特別行政區的經濟作出重大貢獻，可提出申請。"), DPRK],
  elig=[("there is no security objection and no known record of serious crime in respect of the applicant;", "신청인에 대해 안보상 이의가 없고 알려진 중범죄 기록이 없을 것", "申請人沒有保安方面的疑點及沒有已知的嚴重犯罪紀錄；"),
        ("the applicant has a good education background, normally a first degree in the relevant field; and", "통상 관련 분야 학사 학위 이상의 좋은 학력", "申請人具備良好的教育背景，一般要有相關範疇的學士學位；及"),
        ("the applicant is in a position to make substantial contribution to the economy, with consideration of the business plan, business turnover, financial resources, number of local jobs created and new technology or skills introduced.", "사업계획, 매출, 재원, 현지 일자리 창출 수, 새로운 기술·노하우 도입 등을 고려할 때 경제에 상당히 기여할 수 있을 것", "申請人能對經濟作出重大貢獻，考慮因素包括業務計劃、營業額、財政資源、為本地創造的職位數目及引進的新技術或技能等。")],
  docs=[D_PHOTO, D_TD, D_ID, ("Business plan with financial projections", "재무 전망을 포함한 사업계획서", "附有財務預測的業務計劃書"), ("Proof of capital / financial resources", "자본·재원 증빙", "資本／財政資源證明"), D_COMPANY],
  ext_docs=[D_LAST_TD, D_IDX, ("Proof of business operation (e.g. audited financial statements, tax returns)", "사업 운영 증빙(감사 재무제표, 세금 신고서 등)", "業務運作證明（例如經審計的財務報表、報稅表）")],
  fields=[F("bizname", ("Name of business", "사업체 이름", "業務名稱"), req=True, full=True), F("capital", ("Capital to be invested (BH$)", "투자할 자본(BH$)", "擬投資資本（柏峴화랑元）"), req=True, v="num", im="numeric"), F("jobs", ("Number of local jobs to be created", "창출할 현지 일자리 수", "擬為本地創造的職位數目"), req=True, v="num", im="numeric")])

S(k="train", tab="invest", abbr="Training", deps=False, roa=False, months=12, slip=("培訓", "TRAINING"),
  t=("Training", "연수", "培訓"), entry="applytraining", ext=None,
  intro=[("Persons who wish to enter the BHGSAR for training to acquire special skills and knowledge not available in their home countries may apply. The training should be of a structured nature and the trainee should return to his/her place of residence upon completion of training.",
          "본국에서 습득할 수 없는 특수 기술과 지식을 배우기 위해 백현화랑 특별행정구에서 연수를 받으려는 사람은 신청할 수 있습니다. 연수는 체계적이어야 하며 연수생은 연수를 마친 뒤 거주지로 돌아가야 합니다.",
          "擬來柏峴화랑特別行政區接受培訓，以掌握在其原居地未能取得的特別技能及知識的人士可提出申請。培訓須有系統，受訓人士須在培訓完成後返回原居地。")],
  elig=[("the training is not available in the applicant’s home country and the applicant will return there after training;", "본국에서 받을 수 없는 연수이고 연수 후 본국으로 돌아갈 것", "有關培訓在申請人原居地未能提供，而申請人會在培訓後返回原居地；"),
        ("the training period is normally not more than 12 months; and", "연수 기간이 통상 12개월 이하일 것", "培訓期一般不超過12個月；及"),
        ("the trainee will not be employed as a worker during the training.", "연수 기간 중 노동자로 고용되지 않을 것", "受訓人士在培訓期間不會受僱為工人。")],
  docs=[D_PHOTO, D_TD, ("Training programme issued by the training company with schedule and contents", "연수 기관이 발행한 일정·내용이 적힌 연수 계획서", "培訓機構發出載有時間表及內容的培訓計劃"), ("Letter from the applicant’s employer outside the BHGSAR", "백현화랑 특별행정구 밖 고용주의 확인서", "申請人在柏峴화랑以外地區的僱主的信件")],
  fields=[F("trainer", ("Name of training company in Baekhyeon Hwarang", "백현화랑 내 연수 기관 이름", "柏峴화랑培訓機構名稱"), req=True, full=True), F("tmonths", ("Training period (months)", "연수 기간(개월)", "培訓期（月）"), "select", req=True, o=[[str(n), str(n)] for n in (1, 3, 6, 9, 12)])])

S(k="whs", tab="invest", abbr="WHS", deps=False, roa=False, months=12, slip=("工作假期", "WORKING HOLIDAY"),
  t=("Working Holiday", "워킹홀리데이", "工作假期"), entry="applyworkingholiday", ext=None,
  intro=[("The Working Holiday Scheme provides an opportunity for young people of partner countries to come to the BHGSAR for holidays for up to 12 months and to take up short-term employment to supplement their travel funds. Annual quotas apply to each partner country.",
          "워킹홀리데이 제도는 협정 국가의 청년이 최대 12개월 동안 백현화랑 특별행정구에서 휴가를 보내며 여행 경비를 보충하기 위해 단기 취업을 할 수 있는 기회를 제공합니다. 협정 국가별 연간 정원이 있습니다.",
          "「工作假期計劃」讓夥伴國家的青年來柏峴화랑特別行政區度假最多12個月，並可從事短期工作以補助旅費。每個夥伴國家設有每年配額。")],
  elig=[("the applicant is a national of a partner country (Australia, Austria, Canada, France, Germany, Hungary, Ireland, Italy, Japan, Netherlands, New Zealand, Sweden, United Kingdom);", "협정 국가(호주, 오스트리아, 캐나다, 프랑스, 독일, 헝가리, 아일랜드, 이탈리아, 일본, 네덜란드, 뉴질랜드, 스웨덴, 영국) 국민일 것", "申請人為夥伴國家（澳洲、奧地利、加拿大、法國、德國、匈牙利、愛爾蘭、意大利、日本、荷蘭、新西蘭、瑞典、英國）的國民；"),
        ("the applicant is aged between 18 and 30 at the time of application;", "신청 시 만 18세 이상 30세 이하", "申請時年齡介乎18至30歲；"),
        ("the main purpose is to holiday in the BHGSAR, with employment being incidental; and", "주목적이 휴가이고 취업은 부수적일 것", "主要目的是在柏峴화랑度假，而就業屬附帶性質；及"),
        ("the applicant has sufficient funds for maintenance during the stay and a return ticket or funds to purchase one.", "체류 중 생활비와 귀국 항공권 또는 그 구입 자금이 있을 것", "申請人有足夠經費應付逗留期間的生活，並持有回程機票或有足夠款項購買回程機票。")],
  docs=[D_PHOTO, D_TD, D_FIN, ("Proof of medical and hospitalisation insurance for the period of stay", "체류 기간 의료·입원 보험 증빙", "逗留期間的醫療及住院保險證明")],
  fields=[F("partner", ("Nationality (partner country)", "국적(협정 국가)", "國籍（夥伴國家）"), "select", req=True, o=[[c, c] for c in ("AU", "AT", "CA", "FR", "DE", "HU", "IE", "IT", "JP", "NL", "NZ", "SE", "GB")])])

S(k="mfd", tab="invest", abbr="MFD", deps=False, roa=False, multi=True, months=12, slip=("內地漁工", "MAINLAND FISHERMAN DECKHAND"),
  t=("Mainland Fisherman Deckhands", "본토 어선 선원", "內地漁工"), entry="applymfd", ext=None,
  intro=[("Local fishermen may employ Mainland fisherman deckhands under the Mainland Fisherman Deckhands Scheme. Mainland fisherman deckhands may enter the BHGSAR waters on board the employer’s fishing vessel and land in the BHGSAR to take rest on the vessel when it berths.",
          "현지 어민은 본토 어선 선원 제도에 따라 본토 어선 선원을 고용할 수 있습니다. 본토 어선 선원은 고용주의 어선에 승선하여 백현화랑 특별행정구 수역에 들어올 수 있고, 어선이 정박하면 상륙하여 선상에서 휴식할 수 있습니다.",
          "本地漁民可根據「內地過港漁工計劃」僱用內地漁工。內地漁工可隨僱主的漁船進入柏峴화랑特別行政區水域，並在漁船停泊時登岸及在船上休息。")],
  elig=[("the employer is a local fisherman holding a valid licence for a local fishing vessel;", "고용주가 유효한 현지 어선 면허를 가진 현지 어민일 것", "僱主為持有本地漁船有效牌照的本地漁民；"),
        ("the deckhand holds a valid Mainland seaman / fisherman certificate; and", "선원이 유효한 본토 선원·어민 증명서를 소지할 것", "漁工持有有效的內地海員／漁民證明；及"),
        ("the deckhand will only work and stay on board the specified fishing vessel.", "선원이 지정 어선에서만 일하고 머무를 것", "漁工只會在指明的漁船上工作及逗留。")],
  docs=[D_PHOTO, D_TD, ("Licence of the local fishing vessel", "현지 어선 면허", "本地漁船牌照"), D_CONTRACT],
  fields=[F("vessel", ("Fishing vessel licence number", "어선 면허 번호", "漁船牌照號碼"), req=True), F_EMPLOYER])

# ============================================================================= Study / Residence
S(k="study", tab="study", abbr="Study", deps=False, roa=False, months=12, slip=("讀書", "STUDY"),
  t=("Students", "유학생", "學生"), entry="applystudy", ext="students",
  intro=[("Persons who wish to enter the BHGSAR for study may apply for a student visa/entry permit. The application should be submitted through a local sponsor, which should normally be the educational institution concerned.",
          "백현화랑 특별행정구에서 공부하려는 사람은 학생 비자·입경허가를 신청할 수 있습니다. 신청은 통상 해당 교육기관인 현지 보증인을 통해 제출해야 합니다.",
          "擬來柏峴화랑特別行政區讀書的人士可申請學生簽證／進入許可證。申請應透過本地擔保人提交，而擔保人一般應為有關教育機構。")],
  elig=[("the applicant is admitted to a full-time locally-accredited post-secondary programme, a private school registered under the Education Ordinance, or a full-time course on the register of non-local courses;", "현지 인증 전일제 고등교육 과정, 교육조례에 등록된 사립학교, 또는 역외 과정 등록부의 전일제 과정에 입학할 것", "申請人獲取錄修讀全日制經本地評審的專上課程、根據《教育條例》註冊的私立學校，或已註冊的非本地全日制課程；"),
        ("the applicant has sufficient funds to pay the tuition fee and to cover living expenses without working; and", "일하지 않고 학비와 생활비를 감당할 충분한 자금이 있을 것", "申請人有足夠經費支付學費及生活開支而無須工作；及"),
        ("the applicant has a confirmed place of study and a genuine intention to study.", "확정된 학교와 실제 학업 의사가 있을 것", "申請人已獲確定學位，並確有讀書的意向。")],
  docs=[D_PHOTO, D_TD, ("Admission letter issued by the educational institution", "교육기관이 발행한 입학 허가서", "教育機構發出的取錄通知書"), D_FIN, ("Academic qualification certificates", "학력 증명서", "學歷證明文件"), ("Consent of parent / guardian (for applicants under 18)", "부모·보호자 동의서(만 18세 미만)", "父母／監護人的同意書（適用於18歲以下的申請人）")],
  ext_intro=[("Students may apply for extension of stay to continue their studies. Students who have completed their studies may apply to stay under the IANG.", "학생은 학업을 계속하기 위해 체류 연장을 신청할 수 있습니다. 학업을 마친 학생은 IANG로 체류를 신청할 수 있습니다.", "學生可申請延期逗留以繼續學業。已完成學業的學生可根據「非本地畢業生留柏峴／回柏峴就業安排」申請逗留。")],
  ext_docs=[D_LAST_TD, D_IDX, ("Confirmation of continued enrolment issued by the institution", "기관이 발행한 재학 확인서", "院校發出的繼續就讀證明")],
  after=[("Non-local students may take up internships which are curriculum-related, and may take up part-time on-campus employment of not more than 20 hours per week throughout the year, and off-campus summer jobs, subject to conditions.", "역외 학생은 조건에 따라 교과 관련 인턴십, 연중 주 20시간 이하의 교내 아르바이트, 교외 여름방학 아르바이트를 할 수 있습니다.", "非本地學生在符合條件下，可從事與課程相關的實習工作、全年每星期不超過20小時的校園兼職工作，以及校外暑期工作。")],
  fields=[F("school", ("Name of educational institution", "교육기관 이름", "教育機構名稱"), req=True, full=True), F("prog", ("Programme / course of study", "과정·전공", "修讀課程"), req=True), F("smonths", ("Duration of study (months)", "학업 기간(개월)", "修讀期（月）"), "select", req=True, o=[[str(n), str(n)] for n in (6, 12, 24, 36, 48)])])

S(k="dep", tab="study", abbr="Dependants", deps=False, roa=True, months=24, slip=("受養人", "DEPENDANT"),
  t=("Dependants", "부양가족", "受養人"), entry="applydependant", ext="dependants",
  intro=[("A person may apply to enter the BHGSAR as a dependant of a sponsor who is a Baekhyeon Hwarang permanent resident or a resident admitted under a talent, employment, investment or study arrangement. The sponsor must be able to support the dependant’s living at a standard well above the subsistence level and provide him/her with suitable accommodation.",
          "백현화랑 영주민이거나 인재·취업·투자·유학 제도로 입경한 주민을 보증인으로 하여 부양가족으로 백현화랑 특별행정구에 입경하도록 신청할 수 있습니다. 보증인은 부양가족이 최저 생계 수준을 훨씬 웃도는 생활을 하도록 부양하고 적절한 숙소를 제공할 수 있어야 합니다.",
          "任何人士可以受養人身份申請來柏峴화랑特別行政區，其擔保人須為柏峴화랑永久性居民，或根據人才、就業、投資或讀書安排獲准入境的居民。擔保人必須有能力支持受養人遠高於基本生活水平的生活，並為其提供合適居所。")],
  elig=[("the applicant is the spouse or the other party to a legally recognised civil partnership / civil union, or an unmarried dependent child under the age of 18, or a parent aged 60 or above of the sponsor (for sponsors who are permanent residents);", "보증인의 배우자 또는 법적으로 인정된 시민 동반자·시민 결합 상대방, 만 18세 미만 미혼 부양 자녀, 또는 만 60세 이상 부모(보증인이 영주민인 경우)일 것", "申請人為擔保人的配偶或合法承認的民事伴侶／民事結合的另一方、18歲以下未婚而受養的子女，或60歲或以上的父母（只適用於擔保人為永久性居民）；"),
        ("there is reasonable proof of a genuine relationship between the applicant and the sponsor; and", "신청인과 보증인의 실제 관계에 대한 합리적인 증빙이 있을 것", "有合理證明確定申請人與擔保人的真正關係；及"),
        ("the sponsor is able to support the applicant’s living at a standard well above the subsistence level and provide suitable accommodation.", "보증인이 최저 생계 수준을 훨씬 웃도는 생활과 적절한 숙소를 제공할 수 있을 것", "擔保人有能力支持申請人遠高於基本生活水平的生活，並提供合適居所。")],
  docs=[D_PHOTO, D_TD, D_REL, ("The sponsor’s Baekhyeon Hwarang identity card and travel document", "보증인의 백현화랑 신분증 및 여행증명서", "擔保人的柏峴화랑身份證及旅行證件"), ("Proof of the sponsor’s financial means and accommodation", "보증인의 재정 능력 및 숙소 증빙", "擔保人的經濟能力及居所證明")],
  ext_docs=[D_LAST_TD, D_IDX, ("The sponsor’s latest proof of employment / income", "보증인의 최근 고용·소득 증빙", "擔保人最近的僱用／入息證明")],
  fields=[F("sname", ("Name of sponsor", "보증인 성명", "擔保人姓名"), req=True), F("sid", ("Sponsor’s identity card number", "보증인 신분증 번호", "擔保人身份證號碼"), req=True, v="bhid", ph="A123456(7)", sens=True),
          F("srel", ("Relationship with sponsor", "보증인과의 관계", "與擔保人的關係"), "select", req=True, o=[["spouse", ("Spouse", "배우자", "配偶")], ["child", ("Child under 18", "만 18세 미만 자녀", "18歲以下子女")], ["parent", ("Parent aged 60 or above", "만 60세 이상 부모", "60歲或以上的父母")]])])

# ============================================================================= Visit
S(k="visit", tab="visit", abbr="Visit", deps=True, roa=False, months=0, days=30, slip=("訪客", "VISIT"),
  t=("Visit / Transit", "방문·경유", "訪問／過境"), entry="applyvisit_transit", ext="visitor",
  intro=[("If a person wishes to visit or transit the BHGSAR but does not enjoy the visa waiver concession, or wishes to stay beyond the entitled visa free period, he/she must obtain a visit/transit visa/entry permit before travelling.",
          "백현화랑 특별행정구를 방문하거나 경유하려는 사람이 무비자 혜택을 받지 못하거나 허용된 무비자 기간을 넘어 체류하려면 여행 전에 방문·경유 비자·입경허가를 받아야 합니다.",
          "任何人士如欲訪問或過境柏峴화랑特別行政區，但不享有免簽證安排，或欲逗留超過可享的免簽證期限，必須在啟程前取得訪問／過境簽證／進入許可證。")],
  elig=[("the applicant’s bona fides are not in doubt;", "신청인의 방문 목적이 진정할 것", "申請人的真正來柏峴目的不成疑問；"),
        ("the applicant has adequate funds to cover the duration of his/her stay without working;", "일하지 않고 체류 기간을 감당할 충분한 자금이 있을 것", "申請人有足夠經費應付逗留期間的開支而無須工作；"),
        ("the applicant holds a valid travel document with adequate returnability; and", "충분한 귀환 가능성이 있는 유효한 여행증명서를 소지할 것", "申請人持有有效的旅行證件，並可返回原居地；及"),
        ("the applicant has an onward booking (for transit) or a return ticket.", "경유의 경우 다음 목적지 예약, 그 밖에는 귀국 항공권이 있을 것", "申請人持有前往目的地的預訂（過境）或回程票。")],
  docs=[D_PHOTO, D_TD, ("Proof of financial means (e.g. bank statements)", "재정 능력 증빙(은행 거래 내역서 등)", "經濟能力證明（例如銀行月結單）"), ("Proof of accommodation and travel itinerary", "숙소 및 여행 일정 증빙", "住宿及行程證明"), ("Invitation letter from the host in the BHGSAR (if any)", "백현화랑 특별행정구 내 초청인의 초청장(있는 경우)", "柏峴화랑特別行政區邀請人的邀請信（如有）")],
  ext_intro=[("Visitors who wish to extend their stay should submit an application before the expiry of their limit of stay with justifications. Extensions are granted only in exceptional circumstances.", "체류를 연장하려는 방문객은 체류 기한 만료 전에 사유를 밝혀 신청해야 합니다. 연장은 예외적인 상황에서만 허가됩니다.", "擬延長逗留期限的訪客應在逗留期限屆滿前提出申請並說明理由。只有在特殊情況下才會獲准延期。")],
  ext_docs=[D_LAST_TD, ("Return ticket / onward booking", "귀국 항공권·다음 목적지 예약", "回程票／前往目的地的預訂"), ("Supporting documents for the reason of extension", "연장 사유 증빙", "延期理由的證明文件")],
  after=[("Visitors are not permitted to take up any employment (paid or unpaid), establish or join in any business, or enter school as a student while in the BHGSAR. See Permissible Activities for Visitors for activities that are generally allowed.", "방문객은 백현화랑 특별행정구에 있는 동안 유급·무급 취업, 사업 설립·참여, 학생으로서 학교 입학을 할 수 없습니다. 일반적으로 허용되는 활동은 방문객 허용 활동 안내를 참고하세요.", "訪客在柏峴화랑期間不得接受任何僱傭工作（不論是否受薪）、開辦或參與任何業務，或以學生身份入學。有關一般獲准的活動，請參閱「訪客可從事的活動」。")],
  fields=[F("purpose", ("Purpose of visit", "방문 목적", "訪問目的"), "select", req=True, o=[["tour", ("Sightseeing", "관광", "觀光")], ["family", ("Visiting relatives / friends", "친지·지인 방문", "探親／訪友")], ["business", ("Business visit", "업무 방문", "商務訪問")], ["transit", ("Transit", "경유", "過境")]]),
          F("days", ("Intended length of stay (days)", "예정 체류 기간(일)", "擬逗留期（日）"), "select", req=True, o=[[str(n), str(n)] for n in (7, 14, 30, 60, 90)]),
          F("arrive", ("Intended date of arrival (YYYY-MM-DD)", "입경 예정일(YYYY-MM-DD)", "預計抵達日期（YYYY-MM-DD）"), req=True, v="anydate", ph="YYYY-MM-DD")])

S(k="tp", tab="visit", abbr="BHGSAR Travel Pass", deps=False, roa=False, months=36, slip=("柏峴화랑特別行政區旅遊通行證", "BHGSAR TRAVEL PASS"),
  t=("BHGSAR Travel Pass", "백현화랑 특별행정구 여행통행증", "柏峴화랑特別行政區旅遊通行證"), entry="applybhgtp", ext=None,
  intro=[("The BHGSAR Travel Pass is issued to eligible frequent visitors to facilitate their travel to and from the BHGSAR. Holders may enter the BHGSAR for visits and are permitted to use the e-Channel service. The Travel Pass is valid for three years or until the expiry of the holder’s passport, whichever is earlier.",
          "백현화랑 특별행정구 여행통행증은 자격을 갖춘 잦은 방문객이 백현화랑 특별행정구를 편리하게 왕래하도록 발급됩니다. 소지자는 방문 목적으로 입경할 수 있고 e-Channel 서비스를 이용할 수 있습니다. 통행증은 3년 또는 소지자 여권 만료일 중 빠른 날까지 유효합니다.",
          "「柏峴화랑特別行政區旅遊通行證」發給合資格的經常訪客，方便他們往來柏峴화랑特別行政區。持證人可以訪客身份入境，並可使用e-道服務。通行證的有效期為三年或至持證人護照屆滿為止，以較早者為準。")],
  elig=[("the applicant has visited the BHGSAR at least three times in the past 12 months;", "최근 12개월 동안 백현화랑 특별행정구를 3회 이상 방문했을 것", "申請人在過去12個月內曾訪問柏峴화랑特別行政區最少三次；"),
        ("the applicant holds a passport valid for at least six months; and", "유효기간이 6개월 이상 남은 여권을 소지할 것", "申請人持有有效期最少六個月的護照；及"),
        ("the applicant has no adverse immigration record.", "불리한 출입경 기록이 없을 것", "申請人沒有不良入境紀錄。")],
  docs=[D_PHOTO, D_TD, ("Proof of business or frequent travel (e.g. company letter)", "업무 또는 잦은 방문 증빙(회사 확인서 등)", "商務或經常訪問的證明（例如公司信件）")],
  fields=[F("visits", ("Number of visits in the past 12 months", "최근 12개월 방문 횟수", "過去12個月訪問次數"), "select", req=True, o=[[str(n), str(n)] for n in (3, 4, 5, 6, 10, 20)])])

S(k="apec", tab="visit", abbr="ABTC", deps=False, roa=False, evisa=False, months=60, slip=("亞太經合組織商務旅遊證", "APEC BUSINESS TRAVEL CARD"),
  t=("APEC Business Travel Card", "APEC 기업인 여행카드", "亞太經合組織商務旅遊證"), entry_loc="np", entry="applyapec", ext=None,
  intro=[("The APEC Business Travel Card (ABTC) allows Baekhyeon Hwarang business people to enjoy visa-free entry and expedited clearance in participating APEC economies. Eligible applicants must hold a Baekhyeon Hwarang permanent identity card and a valid passport, and travel frequently on business in the APEC region.",
          "APEC 기업인 여행카드(ABTC)는 백현화랑 기업인이 APEC 참여 경제권에서 무비자 입국과 신속 심사를 받을 수 있게 합니다. 백현화랑 영구 신분증과 유효한 여권을 소지하고 APEC 지역으로 업무 출장을 자주 가는 사람이 신청할 수 있습니다.",
          "「亞太經合組織商務旅遊證」讓柏峴화랑商務人士在參與的亞太經合組織經濟體享有免簽證入境及快速通關。合資格申請人須持有柏峴화랑永久性居民身份證及有效護照，並經常因公幹往來亞太經合組織地區。")],
  elig=[("the applicant is a Baekhyeon Hwarang permanent resident holding a valid passport;", "유효한 여권을 소지한 백현화랑 영주민일 것", "申請人為持有效護照的柏峴화랑永久性居民；"),
        ("the applicant is a bona fide business person engaged in trade or investment in the APEC region; and", "APEC 지역에서 무역·투자에 종사하는 진정한 기업인일 것", "申請人為在亞太經合組織地區從事貿易或投資的真正商務人士；及"),
        ("the applicant has no criminal record.", "범죄 기록이 없을 것", "申請人沒有刑事紀錄。")],
  docs=[D_PHOTO, ("The applicant’s Baekhyeon Hwarang SAR passport", "신청인의 백현화랑 특별행정구 여권", "申請人的柏峴화랑特別行政區護照"), D_IDX, ("Letter from the applicant’s company confirming business travel", "출장을 확인하는 회사 확인서", "申請人公司確認商務出行的信件")],
  fields=[F("company", ("Name of company", "회사 이름", "公司名稱"), req=True, full=True), F_POST])

for _k, _abbr, _t, _slug, _days, _intro in [
        ("pri", "PAR (Indian nationals)", ("Pre-arrival Registration for Indian Nationals", "인도 국적자 사전 입경 등록", "印度國民入境前登記"), "applypri", 14,
         ("Indian nationals who wish to visit the BHGSAR visa-free for up to 14 days must apply for and successfully complete pre-arrival registration online before visiting. A successful registration is valid for six months and for multiple visits.",
          "백현화랑 특별행정구를 최대 14일 무비자로 방문하려는 인도 국적자는 방문 전에 온라인으로 사전 입경 등록을 신청하여 완료해야 합니다. 등록은 6개월 동안 여러 차례 방문에 유효합니다.",
          "擬免簽證訪問柏峴화랑特別行政區最多14日的印度國民，必須在訪問前於網上申請並成功完成入境前登記。成功登記的有效期為六個月，並可多次使用。")),
        ("prt", "PAR (Taiwan residents)", ("Pre-arrival Registration for Taiwan Residents", "대만 주민 사전 입경 등록", "台灣居民預辦入境登記"), "applyprt", 30,
         ("Taiwan residents may visit the BHGSAR for up to 30 days after successfully completing pre-arrival registration online. A successful registration is valid for two months and for two visits.",
          "대만 주민은 온라인 사전 입경 등록을 완료하면 백현화랑 특별행정구를 최대 30일 방문할 수 있습니다. 등록은 2개월 동안 2회 방문에 유효합니다.",
          "台灣居民在網上成功預辦入境登記後，可訪問柏峴화랑特別行政區最多30日。成功登記的有效期為兩個月，可使用兩次。")),
        ("twn", "Taiwan entry permit", ("Entry Permit to Visit the BHGSAR from Taiwan (One Entry / Multiple Entries)", "대만발 백현화랑 특별행정구 방문 입경허가(1회·복수)", "台灣居民來往柏峴화랑特別行政區進入許可證（一次／多次入境）"), "applytwnvisit", 30,
         ("Taiwan residents who do not wish to use pre-arrival registration may apply for a one-entry or multiple-entry permit to visit the BHGSAR for up to 30 days on each visit.",
          "사전 입경 등록을 이용하지 않으려는 대만 주민은 방문 1회당 최대 30일 체류할 수 있는 1회 또는 복수 입경허가를 신청할 수 있습니다.",
          "不擬使用預辦入境登記的台灣居民，可申請一次或多次入境許可證來柏峴화랑訪問，每次最多逗留30日。"))]:
    S(k=_k, tab="visit", abbr=_abbr, deps=False, roa=False, months=6 if _k == "pri" else 2, days=_days, slip=("訪客", "VISIT"), t=_t, entry=_slug, ext=None, intro=[_intro],
      elig=[("the applicant holds a valid passport / travel document;", "유효한 여권·여행증명서를 소지할 것", "申請人持有有效的護照／旅行證件；"), ("the visit is for leisure, social or business purposes; and", "여가·친교·업무 목적의 방문일 것", "訪問目的為消閒、社交或商務；及"), ("the applicant has no adverse immigration record.", "불리한 출입경 기록이 없을 것", "申請人沒有不良入境紀錄。")],
      docs=[D_PHOTO, D_TD], fields=[F("arrive", ("Intended date of arrival (YYYY-MM-DD)", "입경 예정일(YYYY-MM-DD)", "預計抵達日期（YYYY-MM-DD）"), req=True, v="anydate", ph="YYYY-MM-DD")])

SCHEME = {s["k"]: s for s in SCHEMES}
TAB_ITEMS = {   # ImmD services/visas tab -> ordered list of scheme keys (FDH extension services shown as sub-items)
    "talent": ["ttps", "gep", "asmtp", "tps", "techtas", "iang", "qmas", "assg", "vpas"],
    "labour": ["fdh", "fdhrenew", "fdhcomplete", "fdhchange", "fdhvisitor", "icw", "slis", "esls"],
    "invest": ["ncies", "cies", "inv", "train", "whs", "mfd"],
    "study": ["study", "dep"],
    "visit": ["visit", "whs", "tp", "apec", "pri", "prt", "twn"],
}


# ============================================================================= link targets ("immd:path" = Immigration Department site, "gov:path" = GovBHG)
NP = "gov:residents/immigration/nonpermanent"
VEP = "gov:nonresidents/visarequire/visasentrypermits"
EXTP = NP + "/applyextensionstay"
INFO = "immd:services/visas/info"


def entry_target(s):
    return (NP if s["entry_loc"] == "np" else VEP) + "/" + s["entry"]


def ext_target(s):
    return EXTP + "/" + s["ext"]


LINK_GROUPS = [
    (("Immigration Guidelines for Entry", "입경 지침", "入境指引"), [
        (("New Fee Structure for Visa Applications under Specified Schemes", "지정 제도 비자 신청의 새 수수료 체계", "指明計劃下簽證申請的新收費架構"), INFO + "/specified-schemes"),
        (("Admission Schemes for Talent, Professionals and Entrepreneurs", "인재·전문인력·기업가 입경 제도", "人才、專業人士及企業家入境計劃"), INFO + "/admission-schemes"),
        (("Visit Visa / Entry Permit Requirements for the Baekhyeon Hwarang Special Administrative Region", "백현화랑 특별행정구 방문 비자·입경허가 요건", "柏峴화랑特別行政區訪問簽證／進入許可證規定"), INFO + "/visit-visa-entry-permit"),
        (("Immigration Guidelines for Entry to the Baekhyeon Hwarang Special Administrative Region of the Republic of Korea", "대한민국 백현화랑 특별행정구 입경 지침", "大韓民國柏峴화랑特別行政區入境指引"), INFO + "/entry-guidelines"),
        (("Entry Arrangements for Mainland & Overseas Korean Residents", "본토·재외 대한민국 주민 입경 절차", "內地及海外韓國居民入境安排"), INFO + "/mainland-entry"),
        (("Permissible Activities for Visitors", "방문객 허용 활동", "訪客可從事的活動"), INFO + "/permissible-activities"),
        (("Re-entry into Baekhyeon Hwarang", "백현화랑 재입경", "再次入境柏峴화랑"), INFO + "/re-entry"),
        (("Arrangements for “e-Visa” Issuance", "\"e-Visa\" 발급 안내", "發出「電子簽證」的安排"), INFO + "/e-visa"),
        (("Electronic Services for Visa Application", "비자 신청 전자 서비스", "簽證申請電子服務"), INFO + "/evisa-online"),
    ]),
    (("Enquiry / Submission of Document", "조회·서류 제출", "查詢／遞交文件"), [
        (("Enquiry of Application Status", "신청 현황 조회", "查詢申請進度"), NP + "/appstatus"),
        (("Submission of Supplementary document(s)", "추가 서류 제출", "遞交補充文件"), EXTP + "/submitsupplementdoc"),
    ]),
    (("Payment and Visa Collection", "결제 및 비자 수령", "付款及領取簽證"), [
        (("Online Payment for “e-Visa”", "\"e-Visa\" 온라인 결제", "網上繳付「電子簽證」費用"), NP + "/onlinepaymentforevisa"),
        (("Download “e-Visa”", "\"e-Visa\" 내려받기", "下載「電子簽證」"), NP + "/downloadevisa"),
        (("“e-Visa” Enquiry", "\"e-Visa\" 조회", "「電子簽證」查詢"), NP + "/evisaenquiry"),
    ]),
    (("Other Visa Services", "기타 비자 서비스", "其他簽證服務"), [
        (("Appointment Booking for Submission of Application", "신청서 제출 예약", "預約遞交申請"), NP + "/bookextensionstay"),
        (("Termination of Sponsorship", "보증 종료", "終止擔保"), INFO + "/termination-of-sponsorship"),
        (("Transfer of Endorsement", "날인 이전", "轉移簽注"), INFO + "/transfer-of-endorsement"),
        (("Online Application for Change of Employment / Investment / Educational Institution", "고용·투자·교육기관 변경 온라인 신청", "網上申請轉換僱主／投資／教育院校"), NP + "/changeofsponsorship"),
    ]),
]
FDH_EXTRA = [
    (("Smart Renewal", "스마트 갱신", "智方便續約"), INFO + "/smart-renewal"),
    (("Online Submission of Revised Schedule of Accommodation and Domestic Duties (ID 407G)", "숙소 및 가사 업무 명세서 변경 온라인 제출(ID 407G)", "網上遞交經修訂的住宿及家務安排表（ID 407G）"), NP + "/id407g"),
    (("Notification of Premature Termination of Employment Contract", "고용계약 조기 해지 통보", "通知提前終止僱傭合約"), NP + "/terminateforeignhelper"),
]
COE_LINK = (("Certificate of Entitlement (COE)", "거주권 자격증명서(COE)", "居留權證明書"), "immd:services/right-of-abode")
INVITED_LINK = (("Immigration Facilitation Scheme for Invited Persons", "초청 인사 출입경 편의 제도", "受邀人士入境便利計劃"), INFO + "/invited-persons")
DISCLAIM_ROW = None

# ============================================================================= ImmD information articles (blocks: p / h2 / h3 / ul / table / go / golinks)
ARTICLES = {}


def A(slug, title, blocks):
    ARTICLES[slug] = (title, blocks)


A("specified-schemes", LINK_GROUPS[0][1][0][0], [
    ("p", ("On making an application under a Specified Scheme for entry or a change of condition of stay (including an extension of limit of stay), the applicant, whether as a principal applicant or a dependant, shall pay an application fee. Upon approval of the application, the applicant shall pay the relevant visa issuance fee.", "지정 제도에 따라 입경 또는 체류 조건 변경(체류 기한 연장 포함)을 신청할 때 신청인은 주 신청인이든 부양가족이든 신청 수수료를 내야 합니다. 신청이 승인되면 해당 비자 발급 수수료를 내야 합니다.", "根據指明計劃申請入境或更改逗留條件（包括延長逗留期限）時，申請人不論是主申請人或受養人，均須繳付申請費。申請獲批准後，申請人須繳付有關簽證簽發費。")),
    ("h3", ("Table 1 – Specified Schemes", "표 1 – 지정 제도", "表一 – 指明計劃")),
    ("ul", [SCHEME[k]["t"] for k in ("ttps", "gep", "asmtp", "qmas", "iang", "assg", "ncies", "cies", "techtas", "vpas")]),
    ("h3", ("Table 2 – Fees", "표 2 – 수수료", "表二 – 費用")),
    ("table", [("Type of applicant", "신청인 유형", "申請人類別"), ("Item", "항목", "項目"), ("Fee (for each application)", "수수료(신청 1건당)", "費用（每宗申請）")],
     [[("Principal applicant or Dependant", "주 신청인 또는 부양가족", "主申請人或受養人"), ("Application fee (non-refundable)", "신청 수수료(환불 불가)", "申請費（不設退款）"), ("BH$600", "BH$600", "600元")],
      [("", "", ""), ("Visa issuance fee – relevant period of more than 180 days", "비자 발급 수수료 – 해당 기간 180일 초과", "簽證簽發費 – 有關期間超過180日"), ("BH$1,300", "BH$1,300", "1,300元")],
      [("", "", ""), ("Visa issuance fee – relevant period of not more than 180 days", "비자 발급 수수료 – 해당 기간 180일 이하", "簽證簽發費 – 有關期間不超過180日"), ("BH$600", "BH$600", "600元")]]),
    ("p", ("The relevant period means the fixed period of limit of stay stated on the visa / entry permit (e.g. 36 months / 24 months / 2 weeks), or, for an extension of stay, the period between the last date under the original limit of stay and the last date under the new limit of stay.", "해당 기간은 비자·입경허가에 적힌 고정 체류 기한(예: 36개월, 24개월, 2주)을 말하며, 체류 연장의 경우 원래 체류 기한 마지막 날부터 새 체류 기한 마지막 날까지의 기간을 말합니다.", "有關期間指簽證／進入許可證上所列明的固定逗留期限（例如36個月／24個月／2星期），如屬延期逗留，則指原有逗留期限的最後一日至新逗留期限的最後一日之間的期間。")),
])
A("admission-schemes", LINK_GROUPS[0][1][1][0], [
    ("p", ("The BHGSAR Government offers a range of admission schemes to attract talent, professionals and entrepreneurs from around the world. The table below summarises the main features of each scheme. Please refer to the relevant scheme page for the detailed eligibility criteria and application procedures.", "백현화랑 특별행정구 정부는 세계 각지의 인재, 전문인력, 기업가를 유치하기 위해 다양한 입경 제도를 운영합니다. 아래 표는 각 제도의 주요 특징을 요약한 것입니다. 자세한 자격 요건과 신청 절차는 각 제도 페이지를 참고하세요.", "柏峴화랑特別行政區政府推行多項入境計劃，吸引世界各地的人才、專業人士及企業家。下表概述各計劃的主要特點，詳細的資格準則及申請程序請參閱各計劃的網頁。")),
    ("table", [("Scheme", "제도", "計劃"), ("Offer of employment required?", "채용 제안 필요 여부", "是否須已獲聘用"), ("Quota", "정원", "配額")],
     [[SCHEME["ttps"]["t"], ("No", "아니요", "否"), ("Category C only", "C유형만", "只限丙類")],
      [SCHEME["gep"]["t"], ("Yes", "예", "是"), ("No", "없음", "否")],
      [SCHEME["asmtp"]["t"], ("Yes", "예", "是"), ("No", "없음", "否")],
      [SCHEME["tps"]["t"], ("Yes", "예", "是"), ("Yes", "있음", "是")],
      [SCHEME["techtas"]["t"], ("Yes", "예", "是"), ("Company quota", "기업별 정원", "公司配額")],
      [SCHEME["iang"]["t"], ("Returning graduates only", "복귀 졸업생만", "只限回柏峴的畢業生"), ("No", "없음", "否")],
      [SCHEME["qmas"]["t"], ("No", "아니요", "否"), ("Yes", "있음", "是")],
      [SCHEME["assg"]["t"], ("No", "아니요", "否"), ("No", "없음", "否")],
      [SCHEME["vpas"]["t"], ("Yes", "예", "是"), ("No", "없음", "否")],
      [SCHEME["ncies"]["t"], ("No", "아니요", "否"), ("No", "없음", "否")]]),
])
A("visit-visa-entry-permit", LINK_GROUPS[0][1][2][0], [
    ("p", ("Nationals of about 170 countries and territories may visit the BHGSAR visa-free for a period ranging from 7 days to 180 days. Persons who are not eligible for visa-free entry, or who wish to stay beyond the visa-free period, must obtain a visa / entry permit before arrival.", "약 170개 국가·지역 국민은 7일에서 180일까지 백현화랑 특별행정구를 무비자로 방문할 수 있습니다. 무비자 입경 대상이 아니거나 무비자 기간을 넘어 체류하려는 사람은 도착 전에 비자·입경허가를 받아야 합니다.", "約170個國家及地區的國民可免簽證訪問柏峴화랑特別行政區，為期7日至180日。不享有免簽證入境安排，或擬逗留超過免簽證期限的人士，須在抵達前取得簽證／進入許可證。")),
    ("table", [("Visa-free period", "무비자 기간", "免簽證期限"), ("Examples of countries / territories", "국가·지역 예시", "國家／地區例子")],
     [[("180 days", "180일", "180日"), ("United Kingdom", "영국", "英國")],
      [("90 days", "90일", "90日"), ("Australia, Canada, France, Germany, Japan, Singapore, United States, most European countries", "호주, 캐나다, 프랑스, 독일, 일본, 싱가포르, 미국, 대부분의 유럽 국가", "澳洲、加拿大、法國、德國、日本、新加坡、美國及大部分歐洲國家")],
      [("30 days", "30일", "30日"), ("Indonesia, Mongolia, Philippines, Thailand, Malaysia, Viet Nam", "인도네시아, 몽골, 필리핀, 태국, 말레이시아, 베트남", "印尼、蒙古、菲律賓、泰國、馬來西亞、越南")],
      [("14 days", "14일", "14日"), ("India (pre-arrival registration required), Cambodia, Laos", "인도(사전 입경 등록 필요), 캄보디아, 라오스", "印度（須辦理入境前登記）、柬埔寨、老撾")],
      [("Visa required", "비자 필요", "須申請簽證"), ("Afghanistan, Cuba, Korea (Democratic People's Republic of), Nepal, Nigeria, Pakistan and others", "아프가니스탄, 쿠바, 조선민주주의인민공화국, 네팔, 나이지리아, 파키스탄 등", "阿富汗、古巴、朝鮮民主主義人民共和國、尼泊爾、尼日利亞、巴基斯坦等")]]),
    ("p", ("Korean residents of the Mainland require an Exit-entry Permit for Travelling to and from Baekhyeon Hwarang with a valid endorsement. Holders of Republic of Korea passports who reside overseas may visit visa-free for 14 days.", "본토 대한민국 주민은 유효한 승인이 있는 백현화랑 왕래 출입경 통행증이 필요합니다. 해외에 거주하는 대한민국 여권 소지자는 14일간 무비자로 방문할 수 있습니다.", "內地韓國居民須持有附有效簽注的往來柏峴화랑通行證。在海外居住的大韓民國護照持有人可免簽證訪問14日。")),
    ("go", ("Apply for a visit / transit visa", "방문·경유 비자 신청", "申請訪問／過境簽證"), "gov:nonresidents/visarequire/visasentrypermits/applyvisit_transit"),
])
A("entry-guidelines", LINK_GROUPS[0][1][3][0], [
    ("p", ("This page provides general guidelines on entry to the BHGSAR for leisure, social or business visits, employment, investment, training, study and residence.", "이 페이지는 여가·친교·업무 방문, 취업, 투자, 연수, 유학, 거주를 위한 백현화랑 특별행정구 입경에 관한 일반 지침을 제공합니다.", "本頁提供有關以消閒、社交或商務訪問、就業、投資、培訓、讀書及居留為目的來柏峴화랑特別行政區的一般入境指引。")),
    ("h3", ("Visit", "방문", "訪問")), ("p", ("Visitors should hold a valid travel document, adequate funds and an onward / return ticket. Visitors may not take up employment, establish or join in business, or study.", "방문객은 유효한 여행증명서, 충분한 자금, 다음 목적지·귀국 항공권을 소지해야 합니다. 방문객은 취업, 사업 설립·참여, 학업을 할 수 없습니다.", "訪客應持有有效旅行證件、足夠經費及前往其他地方／回程的票據。訪客不得就業、開辦或參與業務或讀書。")),
    ("h3", ("Employment and investment", "취업 및 투자", "就業及投資")), ("p", ("Persons who wish to work or invest in the BHGSAR should apply under the appropriate talent, employment or investment scheme before arrival.", "백현화랑 특별행정구에서 일하거나 투자하려는 사람은 도착 전에 해당 인재·취업·투자 제도로 신청해야 합니다.", "擬在柏峴화랑特別行政區工作或投資的人士，應在抵達前根據適當的人才、就業或投資計劃提出申請。")),
    ("h3", ("Study", "유학", "讀書")), ("p", ("Non-local students must obtain a student visa / entry permit through a local sponsoring institution.", "역외 학생은 현지 보증 기관을 통해 학생 비자·입경허가를 받아야 합니다.", "非本地學生須透過本地擔保院校取得學生簽證／進入許可證。")),
    ("h3", ("Residence as dependants", "부양가족 거주", "以受養人身份居留")), ("p", ("Dependants of BHG residents may apply to join their sponsor in the BHGSAR under the dependant policy.", "백현화랑 주민의 부양가족은 부양가족 정책에 따라 백현화랑 특별행정구의 보증인과 함께 살도록 신청할 수 있습니다.", "柏峴화랑居民的受養人可根據受養人政策申請來柏峴화랑與擔保人團聚。")),
    ("p", NORMAL),
])
A("mainland-entry", LINK_GROUPS[0][1][4][0], [
    ("h3", ("Mainland residents", "본토 주민", "內地居民")),
    ("p", ("Korean residents of the Mainland who wish to come to the BHGSAR for settlement, visits, transit, employment, training or study should apply to the relevant Mainland authorities for an Exit-entry Permit for Travelling to and from Baekhyeon Hwarang with the appropriate exit endorsement. Applications for employment, training and study must first be approved by the Immigration Department.", "백현화랑 특별행정구에 정착, 방문, 경유, 취업, 연수, 유학을 위해 오려는 본토 대한민국 주민은 관련 본토 당국에 적절한 출경 승인이 있는 백현화랑 왕래 출입경 통행증을 신청해야 합니다. 취업·연수·유학은 먼저 출입경사무처의 승인을 받아야 합니다.", "擬來柏峴화랑特別行政區定居、訪問、過境、就業、培訓或讀書的內地韓國居民，應向內地有關當局申請往來柏峴화랑通行證及適當的簽注。就業、培訓及讀書的申請須先獲入境事務處批准。")),
    ("h3", ("Overseas Korean nationals", "재외 대한민국 국민", "海外韓國籍人士")),
    ("p", ("Holders of Republic of Korea passports who reside overseas may visit the BHGSAR visa-free for 14 days. For employment, study or residence, they should apply for the appropriate visa / entry permit and may be required to provide proof of overseas residence.", "해외에 거주하는 대한민국 여권 소지자는 백현화랑 특별행정구를 14일간 무비자로 방문할 수 있습니다. 취업·유학·거주를 위해서는 적절한 비자·입경허가를 신청해야 하며 해외 거주 증빙을 요구받을 수 있습니다.", "在海外居住的大韓民國護照持有人可免簽證訪問柏峴화랑特別行政區14日。如擬就業、讀書或居留，應申請適當的簽證／進入許可證，並可能須提供海外居留證明。")),
])
A("permissible-activities", LINK_GROUPS[0][1][5][0], [
    ("p", ("Visitors are generally allowed to undertake the following activities in the BHGSAR without a work visa:", "방문객은 일반적으로 취업 비자 없이 백현화랑 특별행정구에서 다음 활동을 할 수 있습니다.", "訪客一般可在柏峴화랑特別行政區從事以下活動，而無須申請工作簽證："), ),
    ("ul", [("entering into contracts or submitting tenders;", "계약 체결 또는 입찰 제출", "簽訂合約或遞交標書；"), ("examining or supervising the installation / packaging of goods or equipment;", "물품·장비의 설치·포장 검사 또는 감독", "視察或監督貨物或機器的安裝／包裝；"),
            ("participating in exhibitions or trade fairs (except selling goods or supplying services direct to the general public);", "전시회·박람회 참가(일반 대중에게 직접 물품을 팔거나 서비스를 제공하는 것은 제외)", "參加展覽或商品交易會（直接向公眾售賣貨品或提供服務除外）；"),
            ("settling claims or other disputes;", "청구 또는 기타 분쟁 해결", "處理索償或其他糾紛；"), ("attending meetings, conferences or seminars;", "회의·컨퍼런스·세미나 참석", "出席會議、研討會或講座；"),
            ("receiving briefings on the requirements of BHG-based clients;", "백현화랑 고객의 요구 사항에 관한 설명 청취", "聽取柏峴화랑客戶就其要求所作的簡介；"), ("participating in short-term training not exceeding 14 days in total within any 12-month period.", "12개월 동안 총 14일 이하의 단기 연수 참가", "參加在任何12個月內合共不超過14日的短期培訓。")]),
    ("p", ("Visitors are not allowed to take up any employment (whether paid or unpaid), establish or join in any business, or enter school as a student.", "방문객은 유급·무급을 불문하고 취업, 사업 설립·참여, 학생으로서 학교 입학을 할 수 없습니다.", "訪客不得接受任何僱傭工作（不論是否受薪）、開辦或參與任何業務，或以學生身份入學。")),
])
A("re-entry", LINK_GROUPS[0][1][6][0], [
    ("p", ("Non-permanent residents of the BHGSAR (including persons admitted under talent, employment, investment and study arrangements and their dependants), irrespective of their nationality and type of travel document held, do not require a re-entry visa / entry permit to enter the BHGSAR during their permitted limit of stay.", "백현화랑 특별행정구의 비영주 주민(인재·취업·투자·유학 제도로 입경한 사람과 그 부양가족 포함)은 국적이나 여행증명서 종류와 관계없이 허가된 체류 기한 내에는 재입경 비자·입경허가 없이 백현화랑 특별행정구에 입경할 수 있습니다.", "柏峴화랑特別行政區的非永久性居民（包括根據人才、就業、投資及讀書安排獲准入境的人士及其受養人），不論國籍及所持旅行證件類別，在獲准逗留期限內再次入境柏峴화랑特別行政區無須申領回柏峴簽證／進入許可證。")),
    ("p", ("They should present their valid travel document and Baekhyeon Hwarang identity card for arrival clearance. Their limit and conditions of stay remain applicable to any subsequent landing within the currency of the limit of stay.", "입경 심사 때 유효한 여행증명서와 백현화랑 신분증을 제시해야 합니다. 체류 기한과 조건은 체류 기한 내 다음 입경에도 계속 적용됩니다.", "他們在辦理入境檢查時應出示有效旅行證件及柏峴화랑身份證。其逗留期限及條件在逗留期限內再次入境時仍然適用。")),
])
A("e-visa", LINK_GROUPS[0][1][7][0], [
    ("p", ("An applicant for an entry visa/permit, extension of stay or change of status, etc. will be issued with an “e-Visa”, such as a “Notification Slip for Entry Visa/Permit” or a “Notification Slip for Conditions of Stay”, upon approval of the application and payment of the relevant fee (where applicable). “e-Visa” is a collective term for the relevant notification slips in PDF file format. The Immigration Department does not issue sticker-type physical labels for entry visa/permit and extension of stay.",
           "입경 비자·허가, 체류 연장, 신분 변경 등을 신청한 사람은 신청이 승인되고 해당 수수료(있는 경우)를 내면 \"입경 비자·허가 통지서\" 또는 \"체류 조건 통지서\" 같은 \"e-Visa\"를 받습니다. \"e-Visa\"는 PDF 형식의 통지서를 통틀어 이르는 말입니다. 출입경사무처는 입경 비자·허가와 체류 연장에 스티커형 라벨을 발급하지 않습니다.",
           "入境簽證／許可證、延期逗留或轉換身份等申請人，在申請獲批准並繳付有關費用（如適用）後，會獲發「電子簽證」，例如「入境簽證／進入許可通知書」或「逗留條件通知書」。「電子簽證」是PDF檔案格式的有關通知書的統稱。入境事務處不會就入境簽證／許可證及延期逗留發出貼紙式標籤。")),
    ("h3", ("Online payment and download", "온라인 결제 및 내려받기", "網上付款及下載")),
    ("p", ("Applicants may pay online and then download or print the “e-Visa” by themselves. An “e-Visa” holder may re-download or re-print a valid “e-Visa” through GovBHG at any time.", "신청인은 온라인으로 결제한 뒤 직접 \"e-Visa\"를 내려받거나 인쇄할 수 있습니다. \"e-Visa\" 소지자는 정부포털 BHG에서 유효한 \"e-Visa\"를 언제든 다시 내려받거나 인쇄할 수 있습니다.", "申請人可在網上付款，然後自行下載或列印「電子簽證」。「電子簽證」持有人可隨時透過「BHG政府一站通」重新下載或列印有效的「電子簽證」。")),
    ("p", ("An “e-Visa” contains an encrypted QR code for verification of its information. Persons concerned, such as a potential employer, can verify the information through the “e-Visa” Enquiry service.", "\"e-Visa\"에는 정보 확인용 암호화 QR 코드가 있습니다. 예비 고용주 등 관계자는 \"e-Visa\" 조회 서비스로 정보를 확인할 수 있습니다.", "「電子簽證」載有加密二維碼，以核實其資料。有關人士（例如準僱主）可透過「電子簽證」查詢服務核實資料。")),
    ("golinks", LINK_GROUPS[2][1]),
])
A("evisa-online", LINK_GROUPS[0][1][8][0], [
    ("p", ("Applicants may submit applications for entry and extension of stay under the following schemes / arrangements online, and upload the required documents. The online services are available 24 hours a day.", "다음 제도·절차에 따른 입경 및 체류 연장 신청은 온라인으로 제출하고 필요한 서류를 올릴 수 있습니다. 온라인 서비스는 24시간 이용할 수 있습니다.", "申請人可在網上遞交以下計劃／安排的入境及延期逗留申請，並上載所需文件。網上服務全日24小時提供。")),
    ("schemes", None),
])
A("termination-of-sponsorship", LINK_GROUPS[3][1][1][0], [
    ("p", ("An employer or educational institution which sponsored a person’s visa / entry permit should notify the Immigration Department in writing within seven working days when the employment or study is terminated. The sponsored person should also notify the Department, and leave the BHGSAR before the expiry of his/her limit of stay or within 14 days from the day following the termination, whichever is earlier, unless a fresh application is approved.", "비자·입경허가를 보증한 고용주나 교육기관은 고용이나 학업이 끝나면 7근무일 이내에 출입경사무처에 서면으로 알려야 합니다. 피보증인도 출입경사무처에 알려야 하며, 새 신청이 승인되지 않는 한 체류 기한 만료일과 종료 다음 날부터 14일 중 빠른 날 이전에 백현화랑 특별행정구를 떠나야 합니다.", "曾擔保任何人士簽證／進入許可證的僱主或教育院校，須在僱傭或學業終止後七個工作天內以書面通知入境事務處。受擔保人亦須通知本處，並在逗留期限屆滿前或由終止日翌日起計14日內（以較早者為準）離開柏峴화랑特別行政區，除非新的申請獲得批准。")),
])
A("transfer-of-endorsement", LINK_GROUPS[3][1][2][0], [
    ("p", ("Since the implementation of the “e-Visa” arrangement, the “e-Visa” remains valid when the holder obtains a new travel document; transfer of endorsement is not required. Holders of sticker-type labels issued before the arrangement may apply to transfer the endorsement to a new travel document at an Immigration Office.", "\"e-Visa\" 제도 시행 이후에는 소지자가 새 여행증명서를 받아도 \"e-Visa\"가 계속 유효하므로 날인 이전이 필요하지 않습니다. 제도 시행 전에 발급된 스티커형 라벨 소지자는 출입경사무처 사무소에서 새 여행증명서로 날인 이전을 신청할 수 있습니다.", "自實施「電子簽證」安排後，持有人換領新旅行證件時「電子簽證」仍然有效，無須轉移簽注。持有安排實施前發出的貼紙式標籤的人士，可到入境事務處辦事處申請把簽注轉移至新旅行證件。")),
])
A("extension-of-stay-others", (("Extension of Stay for Non-Permanent Residents", "비영주 주민 체류 연장", "非永久性居民延期逗留")), [
    ("p", ("Non-permanent residents may apply for extension of stay online. Select the scheme under which you were admitted.", "비영주 주민은 온라인으로 체류 연장을 신청할 수 있습니다. 입경할 때 적용된 제도를 선택하세요.", "非永久性居民可在網上申請延期逗留。請選擇你獲准入境時所根據的計劃。")),
    ("extlist", None),
])
A("smart-renewal", FDH_EXTRA[0][0], [
    ("p", ("“Smart Renewal” allows a foreign domestic helper who will continue to work for the same employer to submit the contract renewal application online, pay the fee and download the “e-Visa”, without attending an Immigration Office in person.", "\"스마트 갱신\"은 같은 고용주를 위해 계속 일할 외국인 가사도우미가 출입경사무처 사무소를 방문하지 않고 온라인으로 계약 갱신을 신청하고 수수료를 내며 \"e-Visa\"를 내려받을 수 있게 합니다.", "「智方便續約」讓繼續為同一僱主工作的外籍家庭傭工，無須親身前往入境事務處辦事處，即可在網上遞交續約申請、繳費及下載「電子簽證」。")),
    ("go", APPLY_EXT, EXTP + "/fdhcontractrenewal"),
])
A("visa-fees", (("Fee Tables – Visas", "수수료표 – 비자", "收費表 – 簽證")), [
    ("table", [("Item", "항목", "項目"), ("Fee", "수수료", "費用")],
     [[("Ordinary visa – single journey", "일반 비자 – 단수", "普通簽證 – 單程"), ("BH$230", "BH$230", "230元")],
      [("Ordinary visa – multiple journeys", "일반 비자 – 복수", "普通簽證 – 多次"), ("BH$460", "BH$460", "460元")],
      [("Transit visa", "경유 비자", "過境簽證"), ("BH$170", "BH$170", "170元")],
      [("Change of condition of stay (including extension of limit of stay)", "체류 조건 변경(체류 기한 연장 포함)", "更改逗留條件（包括延長逗留期限）"), ("BH$230", "BH$230", "230元")],
      [("Application fee for a specified scheme application", "지정 제도 신청 수수료", "指明計劃申請費"), ("BH$600", "BH$600", "600元")],
      [("Visa issuance fee for a specified scheme (more than 180 days / not more than 180 days)", "지정 제도 비자 발급 수수료(180일 초과·이하)", "指明計劃簽證簽發費（超過180日／不超過180日）"), ("BH$1,300 / BH$600", "BH$1,300 / BH$600", "1,300元／600元")]]),
])
A("invited-persons", INVITED_LINK[0], [
    ("p", ("The Immigration Facilitation Scheme for Invited Persons provides facilitation to persons invited by government bureaux / departments, statutory bodies and recognised organisations to visit the BHGSAR for official, academic, cultural or sports exchanges. The inviting organisation submits the application on behalf of the invited persons.", "초청 인사 출입경 편의 제도는 정부 부처·법정 기구·공인 단체가 공무, 학술, 문화, 체육 교류를 위해 초청한 사람의 백현화랑 특별행정구 방문을 지원합니다. 초청 기관이 초청 인사를 대신해 신청서를 제출합니다.", "「受邀人士入境便利計劃」為獲政府政策局／部門、法定組織及認可機構邀請來柏峴화랑特別行政區進行公務、學術、文化或體育交流的人士提供便利。邀請機構會代受邀人士提交申請。")),
])


# ============================================================================= GovBHG service pages (template text)
GOVT = {
    "who": ("Who can Use this Service", "이용 대상", "誰可使用此服務"),
    "elig": ("Eligibility Criteria", "신청 자격", "資格準則"),
    "docs": ("Documents to be Submitted Online", "온라인 제출 서류", "須於網上遞交的文件"),
    "mand": ("Documents marked with * are mandatory.", "*표시가 있는 서류는 필수입니다.", "註有＊號的文件必須遞交。"),
    "docA": ("A. Applicant", "A. 신청인", "甲. 申請人"),
    "docB": ("B. Each accompanying dependant", "B. 각 동반 부양가족", "乙. 每名隨行受養人"),
    "colDoc": ("Documents", "서류", "文件"), "colMax": ("Maximum no. of files for upload", "업로드 가능한 최대 파일 수", "可上載檔案的最高數目"),
    "form": ("In the online application process, the applicant and the dependant (if applicable) will be required to fill in an online application form and sign to confirm that all information given is correct, complete and true. If the dependant is under the age of 16, the online application form must be signed by his/her parent or legal guardian.",
             "온라인 신청 과정에서 신청인과 부양가족(해당 시)은 온라인 신청서를 작성하고 모든 정보가 정확하고 완전하며 사실임을 확인하는 서명을 해야 합니다. 부양가족이 만 16세 미만이면 부모나 법정대리인이 서명해야 합니다.",
             "在網上申請過程中，申請人及受養人（如適用）須填寫網上申請表，並簽署確認所提供的資料全部正確、完整及真實。如受養人未滿16歲，網上申請表必須由其父母或合法監護人簽署。"),
    "fmt": ("File Formats", "파일 형식", "檔案格式"),
    "fmtP": ("File type: JPEG, PDF, GIF, PNG or TIF. File size: 5 MB or below for each file. Colour depth: grayscale (for documents without photos) or colour (for documents with photos).", "파일 종류: JPEG, PDF, GIF, PNG 또는 TIF. 파일 크기: 파일당 5MB 이하. 색상: 사진이 없는 서류는 흑백, 사진이 있는 서류는 컬러.", "檔案類型：JPEG、PDF、GIF、PNG或TIF。檔案大小：每個檔案5MB或以下。色彩：灰階（沒有相片的文件）或彩色（附有相片的文件）。"),
    "pay": ("Payment Method", "결제 방법", "付款方法"),
    "payP": ("The fee shall be paid in the online application process by credit card (VISA, Mastercard and JCB only), Online Payment Service (OPS), instant bank transfer or mobile wallet. The application fee paid is non-refundable in any circumstances irrespective of the application result.", "수수료는 온라인 신청 과정에서 신용카드(VISA, Mastercard, JCB만 가능), 온라인 결제 서비스(OPS), 계좌 간편이체 또는 모바일 지갑으로 냅니다. 납부한 신청 수수료는 신청 결과와 관계없이 어떠한 경우에도 환불되지 않습니다.", "費用須於網上申請過程中以信用卡（只接受VISA、萬事達卡及JCB）、網上繳費服務、即時轉賬或流動錢包繳付。已繳付的申請費不論申請結果如何，在任何情況下均不獲退還。"),
    "payfaq": ("FAQs about Online Payment Service", "온라인 결제 서비스 자주 묻는 질문", "網上付款服務常見問題"),
    "start": ("How to Start", "시작하기", "如何開始"),
    "startP": ("Once you have prepared your supplementary documents, you can access the online service through the following link.", "증빙서류를 준비했다면 아래 링크로 온라인 서비스에 들어갈 수 있습니다.", "準備好證明文件後，你可透過以下連結使用網上服務。"),
    "startN": ("Please ensure that the information you provide is correct. Incorrect information may render your submission invalid.", "입력한 정보가 정확한지 확인하세요. 잘못된 정보는 제출을 무효로 만들 수 있습니다.", "請確保你提供的資料正確。不正確的資料或會令你的遞交無效。"),
    "group": ("Group Submission", "그룹 제출", "以組別方式遞交"),
    "groupP": ("If your accompanying dependants are also applying for the visa / entry permit, you can submit their applications with yours as a group. The maximum number of applications that can be submitted in each group is nine. The system will guide you through the steps of providing the personal information of each applicant and uploading the documents required.", "동반 부양가족도 비자·입경허가를 신청한다면 본인 신청과 함께 그룹으로 제출할 수 있습니다. 그룹당 최대 9건까지 제출할 수 있습니다. 시스템이 각 신청인의 인적사항 입력과 필요한 서류 업로드 단계를 안내합니다.", "如你的隨行受養人亦申請簽證／進入許可證，你可把他們的申請與你的申請以組別方式一併遞交。每組最多可遞交九宗申請。系統會引導你提供每名申請人的個人資料及上載所需文件。"),
    "supp": ("Supplementary Document Submission", "추가 서류 제출", "遞交補充文件"),
    "suppP": ("If you have submitted an application and received a notification letter from the Immigration Department asking you to provide supplementary documents, you can use the online submission service.", "신청서를 제출한 뒤 출입경사무처에서 추가 서류 제출을 요청하는 통지서를 받았다면 온라인 제출 서비스를 이용할 수 있습니다.", "如你已遞交申請，並收到入境事務處要求你提供補充文件的通知信，你可使用網上遞交服務。"),
    "suppL": ("Online supplementary document submission", "추가 서류 온라인 제출", "網上遞交補充文件"),
    "help": ("Assistance and Further Information", "지원 및 추가 정보", "協助及更多資料"),
    "helpP": ("If you need technical assistance in using the online service, you can call the Immigration e-Services Hotline between 7 am and 11 pm daily. For general enquiries, please call the Immigration Department during office hours (8:45 am to 5:15 pm, Monday to Friday; 9 am to 12 noon on Saturday, except public holidays).", "온라인 서비스 이용에 기술 지원이 필요하면 매일 오전 7시부터 오후 11시까지 출입경 전자서비스 상담전화로 연락하세요. 일반 문의는 근무 시간(월~금 오전 8시 45분~오후 5시 15분, 토요일 오전 9시~정오, 공휴일 제외)에 출입경사무처로 연락하세요.", "如在使用網上服務時需要技術支援，可於每日上午7時至晚上11時致電入境事務處電子服務熱線。一般查詢請於辦公時間（星期一至五上午8時45分至下午5時15分；星期六上午9時至中午12時，公眾假期除外）致電入境事務處。"),
    "seeElig": ("To find out if you are eligible, please visit the Immigration Department website:", "신청 자격은 출입경사무처 웹사이트에서 확인하세요.", "如欲知道你是否符合資格，請瀏覽入境事務處網站："),
    "entryT": ("Online Application for Entry to Baekhyeon Hwarang under the {s}", "{s} 백현화랑 입경 온라인 신청", "網上申請根據{s}來柏峴화랑"),
    "extT": ("Online Application for Extension of Stay for Persons Admitted under the {s} or Their Dependants", "{s} 입경자 및 그 부양가족의 체류 연장 온라인 신청", "網上申請延期逗留（根據{s}獲准入境的人士或其受養人）"),
    "fdhExtT": ("Online Application for Extension of Stay – {s}", "체류 연장 온라인 신청 – {s}", "網上申請延期逗留 – {s}"),
    "whoEntry": ("You can use this online service to submit an application for entry to the Baekhyeon Hwarang Special Administrative Region under the {s}. This online service is not applicable to extension of stay applications.", "이 온라인 서비스로 {s}에 따른 백현화랑 특별행정구 입경 신청서를 제출할 수 있습니다. 체류 연장 신청에는 이 서비스를 이용할 수 없습니다.", "你可使用此網上服務，根據{s}遞交來柏峴화랑特別行政區的入境申請。此網上服務不適用於延期逗留申請。"),
    "whoExt": ("You can use this online service to apply for extension of stay if you were admitted under the {s} (or as a dependant of such a person) and your limit of stay is going to expire.", "{s}로 입경했거나 그 부양가족으로 입경했고 체류 기한이 곧 만료된다면 이 온라인 서비스로 체류 연장을 신청할 수 있습니다.", "如你是根據{s}（或以該等人士的受養人身份）獲准入境，而你的逗留期限即將屆滿，你可使用此網上服務申請延期逗留。"),
    "startEntry": ("Online application for entry to Baekhyeon Hwarang under the {s}", "{s} 백현화랑 입경 온라인 신청", "網上申請根據{s}來柏峴화랑"),
    "startExt": ("Online application for extension of stay", "체류 연장 온라인 신청", "網上申請延期逗留"),
}
GOV_TITLE = {"applyemployment": ("Online Application for Entry to Baekhyeon Hwarang for Employment as Professionals (GEP and ASMTP)", "전문인력 취업을 위한 백현화랑 입경 온라인 신청(GEP·ASMTP)", "網上申請來柏峴화랑以專業人士身份就業（一般就業政策及輸入內地人才計劃）")}

# common e-services: key -> (GovBHG path, title, intro paragraphs)
COMMON = [
    ("evisa-payment", NP + "/onlinepaymentforevisa", ("Online Payment for “e-Visa”", "\"e-Visa\" 온라인 결제", "網上繳付「電子簽證」費用"),
     [("If your application for a visa / entry permit has been approved, you can pay the visa issuance fee online through the link provided in the notification of the application result, and then download or print the “e-Visa” by yourself.", "비자·입경허가 신청이 승인되었다면 신청 결과 통지에 있는 링크로 비자 발급 수수료를 온라인으로 내고 직접 \"e-Visa\"를 내려받거나 인쇄할 수 있습니다.", "如你的簽證／進入許可證申請已獲批准，你可透過申請結果通知內的連結在網上繳付簽證簽發費，然後自行下載或列印「電子簽證」。"),
      ("You will need the application reference number and the date of birth of the applicant.", "신청 접수번호와 신청인의 생년월일이 필요합니다.", "你需要申請參考編號及申請人的出生日期。")]),
    ("evisa-download", NP + "/downloadevisa", ("Download “e-Visa”", "\"e-Visa\" 내려받기", "下載「電子簽證」"),
     [("You can download and print your valid “e-Visa” at any time. The “e-Visa” may be saved in soft copy on a personal mobile device or printed on a sheet of A4 white paper for inspection when necessary.", "유효한 \"e-Visa\"는 언제든 내려받아 인쇄할 수 있습니다. \"e-Visa\"는 필요할 때 제시할 수 있도록 개인 휴대기기에 저장하거나 A4 흰 종이에 인쇄해 둘 수 있습니다.", "你可隨時下載及列印有效的「電子簽證」。「電子簽證」可儲存於個人流動裝置內或列印於A4白紙上，以便在有需要時出示以供查閱。"),
      ("You will need the application reference number and the date of birth of the applicant.", "신청 접수번호와 신청인의 생년월일이 필요합니다.", "你需要申請參考編號及申請人的出生日期。")]),
    ("evisa-enquiry", NP + "/evisaenquiry", ("“e-Visa” Enquiry", "\"e-Visa\" 조회", "「電子簽證」查詢"),
     [("Persons concerned, such as a potential employer of an “e-Visa” holder, can enquire the information of an “e-Visa” by inputting the application reference number and the date of birth printed on the “e-Visa”.", "\"e-Visa\" 소지자의 예비 고용주 등 관계자는 \"e-Visa\"에 인쇄된 신청 접수번호와 생년월일을 입력하여 \"e-Visa\" 정보를 조회할 수 있습니다.", "有關人士（例如「電子簽證」持有人的準僱主）可輸入「電子簽證」上的申請參考編號及出生日期，查詢「電子簽證」的資料。")]),
    ("supplementary-documents", EXTP + "/submitsupplementdoc", ("Online Submission of Supplementary Documents (for Applications Relating to a Visa/Entry Permit)", "추가 서류 온라인 제출(비자·입경허가 관련 신청)", "網上遞交補充文件（適用於與簽證／進入許可證有關的申請）"),
     [("If you have submitted an application for a visa / entry permit (including applications for an entry visa / permit, extension of stay or change of status, etc.) and, upon receipt of a notification letter from the Immigration Department, need to provide supplementary documents for the application, you can use the online submission service to submit the relevant documents.", "비자·입경허가(입경 비자·허가, 체류 연장, 신분 변경 등) 신청서를 제출한 뒤 출입경사무처 통지서를 받고 추가 서류를 내야 한다면 온라인 제출 서비스로 해당 서류를 제출할 수 있습니다.", "如你已遞交簽證／進入許可證申請（包括申請入境簽證／許可證、延期逗留或轉換身份等），並在收到入境事務處的通知信後須為申請提供補充文件，你可使用網上遞交服務遞交有關文件。")]),
    ("extension-booking", NP + "/bookextensionstay", ("Online Appointment Booking for Submission of Application", "신청서 제출 온라인 예약", "網上預約遞交申請"),
     [("You can make an appointment to submit in person an application for extension of stay, change of employment or other visa-related applications at the Immigration Headquarters.", "출입경사무처 본부에서 체류 연장, 고용 변경 등 비자 관련 신청서를 직접 제출하기 위한 예약을 할 수 있습니다.", "你可預約親身到入境事務處總部遞交延期逗留、轉換僱主或其他與簽證有關的申請。")]),
    ("change-sponsorship", NP + "/changeofsponsorship", ("Online Application for Change of Employment / Investment / Educational Institution", "고용·투자·교육기관 변경 온라인 신청", "網上申請轉換僱主／投資／教育院校"),
     [("Persons admitted for employment, investment or study who wish to change their employer, business or educational institution may apply online. They must not take up the new employment, business or study before the application is approved.", "취업·투자·유학으로 입경한 사람이 고용주, 사업 또는 교육기관을 바꾸려면 온라인으로 신청할 수 있습니다. 신청이 승인되기 전에는 새 일자리, 사업, 학업을 시작할 수 없습니다.", "以就業、投資或讀書身份獲准入境的人士，如欲轉換僱主、業務或教育院校，可在網上申請。在申請獲批准前，他們不得開始新的工作、業務或學業。")]),
    ("fdh-termination", NP + "/terminateforeignhelper", ("Online Notification of Premature Termination of Employment Contracts of Foreign Domestic Helpers", "외국인 가사도우미 고용계약 조기 해지 온라인 통보", "網上通知提前終止外籍家庭傭工僱傭合約"),
     [("Employers and foreign domestic helpers should notify the Immigration Department within seven days of the date of termination of the employment contract. You can submit the notification online.", "고용주와 외국인 가사도우미는 고용계약 해지일로부터 7일 이내에 출입경사무처에 알려야 합니다. 온라인으로 통보할 수 있습니다.", "僱主及外籍家庭傭工須在僱傭合約終止日期起計七日內通知入境事務處。你可在網上遞交通知。")]),
    ("id407g", NP + "/id407g", ("Online Submission of Revised Schedule of Accommodation and Domestic Duties (ID 407G)", "숙소 및 가사 업무 명세서 변경 온라인 제출(ID 407G)", "網上遞交經修訂的住宿及家務安排表（ID 407G）"),
     [("If there is any change in the accommodation or domestic duties of a foreign domestic helper during the contract period, the employer should submit a revised Schedule of Accommodation and Domestic Duties (ID 407G).", "계약 기간 중 외국인 가사도우미의 숙소나 가사 업무가 바뀌면 고용주는 변경된 숙소 및 가사 업무 명세서(ID 407G)를 제출해야 합니다.", "如在合約期內外籍家庭傭工的住宿或家務安排有任何改變，僱主應遞交經修訂的住宿及家務安排表（ID 407G）。")]),
]
NP_INDEX = ("applyextensionstay", ("Online Application for Extension of Stay", "체류 연장 온라인 신청", "網上申請延期逗留"),
            ("If you are applying to extend your stay in Baekhyeon Hwarang you can do so through a convenient online service. Here you can learn about who is eligible to use the service, how to use it and where to go for further information.", "백현화랑 체류를 연장하려면 편리한 온라인 서비스를 이용할 수 있습니다. 이용 대상, 이용 방법, 추가 정보를 얻는 곳을 안내합니다.", "如你擬申請延長在柏峴화랑的逗留期限，可使用方便的網上服務。你可在此了解誰可使用此服務、如何使用及從何取得更多資料。"))
VEP_CARDS = [  # GovBHG "Introduction & Application for Visas / Entry Permits"
    (TABS[1][1], ("Find out more about the information of the visa / entry permit for talent admission here.", "인재 입경 비자·입경허가 정보를 확인하세요.", "在此了解有關人才入境的簽證／進入許可證資料。"), "immd:services/visas#tab_talent"),
    (TABS[2][1], ("Find out more about the information of the visa / entry permit for foreign domestic helpers / imported workers here.", "외국인 가사도우미·수입 노동자 비자·입경허가 정보를 확인하세요.", "在此了解有關外籍家庭傭工／輸入勞工的簽證／進入許可證資料。"), "immd:services/visas#tab_labour"),
    (TABS[3][1], ("Find out more about the information of the visa / entry permit for investment / training and other employment here.", "투자·연수·기타 취업 비자·입경허가 정보를 확인하세요.", "在此了解有關投資／培訓及其他就業的簽證／進入許可證資料。"), "immd:services/visas#tab_invest"),
    (TABS[4][1], ("Find out more about the information of the visa / entry permit for residence / studying in Baekhyeon Hwarang here.", "백현화랑 거주·유학 비자·입경허가 정보를 확인하세요.", "在此了解有關在柏峴화랑居留／讀書的簽證／進入許可證資料。"), "immd:services/visas#tab_study"),
    (TABS[5][1], ("Find out more about the information of the visa / entry permit for visiting Baekhyeon Hwarang here.", "백현화랑 방문 비자·입경허가 정보를 확인하세요.", "在此了解有關訪問柏峴화랑的簽證／進入許可證資料。"), "immd:services/visas#tab_visit"),
]
GENERAL_CARDS = [  # GovBHG "General Visa Requirements"
    (LINK_GROUPS[0][1][3][0], ("Check out the entry visa / permit requirements for persons who wish to enter Baekhyeon Hwarang for visits, employment, investment, training, study and residence.", "방문, 취업, 투자, 연수, 유학, 거주를 위해 백현화랑에 입경하려는 사람의 입경 비자·허가 요건을 확인하세요.", "查閱擬以訪問、就業、投資、培訓、讀書及居留為目的來柏峴화랑人士的入境簽證／許可證規定。"), INFO + "/entry-guidelines"),
    (LINK_GROUPS[0][1][2][0], ("Nationals of about 170 countries and territories may visit Baekhyeon Hwarang visa-free for 7 to 180 days. Check whether you need a visa or entry permit.", "약 170개 국가·지역 국민은 백현화랑을 7~180일 무비자로 방문할 수 있습니다. 비자나 입경허가가 필요한지 확인하세요.", "約170個國家及地區的國民可免簽證訪問柏峴화랑7至180日。查閱你是否需要簽證或進入許可證。"), INFO + "/visit-visa-entry-permit"),
    (LINK_GROUPS[0][1][4][0], ("Find out the arrangements for Mainland and overseas Korean residents to enter Baekhyeon Hwarang.", "본토·재외 대한민국 주민의 백현화랑 입경 절차를 확인하세요.", "了解內地及海外韓國居民來柏峴화랑的入境安排。"), INFO + "/mainland-entry"),
    ((("Fee for Visa Applications", "비자 신청 수수료", "簽證申請費用")), ("Check out the fees payable for different types of visas and applications for extension of stay.", "비자 종류별 수수료와 체류 연장 신청 수수료를 확인하세요.", "查閱各類簽證及延期逗留申請的費用。"), INFO + "/visa-fees"),
    (LINK_GROUPS[0][1][7][0], ("Learn how the “e-Visa” is issued, paid for and downloaded.", "\"e-Visa\"의 발급, 결제, 내려받기 방법을 알아보세요.", "了解「電子簽證」的簽發、付款及下載方法。"), INFO + "/e-visa"),
]
