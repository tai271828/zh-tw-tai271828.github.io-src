Title: 第一次透過 Google Tag Manager 給網站設定連接 Google Analysis
Status: published
Date: 2021-1-9 11:00
Tags: SEO, GTM, GA
Category: SEO
Slug: seo-tools-01-gtm-ga-gsearch-console


# 為什麼要做這些設定
理由百百種，本質不外乎是「資訊投放者」想要取得「資訊接受者」的反饋。下面舉兩個常見例子。


## 想知道讀者群是誰的 Blog 作者
一種常見的情境是想知道讀者群來自何方、大多是什麼身份的 Blog 作者，我自己也是這樣開始而完成第一次的設定。對我自己而言，甚至會期許這是一種訓練自己文筆的手段 ~~知道哪種表達方式可能比較迎合目標客群口味~~。


## 想知道客戶行為的商店網頁
就算不是最大宗、我推想像這樣的商業動機也是這一套 toolchain 誕生的最大推力吧。不斷最佳化客戶最後下單採購的用戶體驗，來達成最大收益。


# 名詞與基本概念解釋
在第一次摸索的過程中，我發現對於名詞的定義有清楚認識，而不是含糊使用，對於上手有很大的幫助。這似乎是因為很多概念和名詞是 Google 提供服務時自創的，如果憑空望文生義，可能會產生誤解、讀不懂說明。建議一定要耐心花三分種、或是事後不斷回頭問自己是否真的明確了解每一個名詞定義。

下面根據不同的服務列出對應的重要詞彙。


## Google Tag Manager (GTM) 的核心概念與詞彙
使用 Google Tag Manager (GTM) 的時候，三個最重要的名詞，建議一定要隨時清楚知道自己在設定什麼：
  - container
    - 裝著各種 tag 和 variable 的設定集合，所以使用 "container"/容器 這個名詞。
    - 中文常常聽到「埋 tag」其實是指「透過在網站放入 container，所以很多裝在 container 的 tag 也被埋進網站裡了」。
  - tag
    - 有實際特殊功能、能夠偵測網站中用戶行為的程式碼片段；中文的頁面好像翻譯成「代碼」。
    - 市面上有各種不同的 tag 可以使用，光是 Google Analysis (GA) 系列就有 2020 年底推出的 GA4，以及 GA4 前身的 Universal Analysis (UA)。非 Google 的廠商也有自己實做規格的 tag。
    - 一個完整的 tag 是一個 tag type 加上一個 trigger：某個用戶行為觸發了指定的 tag type 與對應的蒐集資訊行為。
    - 透過 container 管理各種來源與種類的 tag，所以這個服務叫做 Google Tag Manager。
  - variable
    - 給事先定義好的 tag type 與對應的蒐集資訊行為命名，這樣就可以在不同的 container 中重複使用，避免設定過於繁瑣。

其他比較能夠望文生義的名詞像是：
  - workspace
    - 工作區，基本上就是 container 的 configuration。GTM 另外會幫每個 configuration 做版本控制。
    - 每個 configuration 要 submit 了之後才會生效，所以第一次使用 preview 測試前要記得做第一次提交。
  - trigger
    - 觸發 tag 動作的用戶行為


### Google Tag Manager (GTM) 設定流程
整個 GTM 使用流程基本上可以想成「把貨櫃/容器/container放進網站，但貨櫃裡面有什麼東西隨時可以變動」。使用 GTM 的流程與對應權限義務細節如下：
  - gmail 帳號賦予自己使用 GTM 權限
  - 一個 gmail 帳號可以開好幾個 GTM account。注意這裡的 account 比較像是 "管理群組名稱"，不要跟自己的 gmail account 混淆了。
  - 一個 GTM account 會對應一個 workspace，取得 workspace 之後就可以開始透過 variable 組合各種 tag and trigger；variable 的設定只是輔助、方便使用者設定。一開始完全沒有 variable 可用的情況下還是必須至少設定一組。
  - 完成 workspace 對 tag/trigger 的各種組合， submit 讓設定生效。
  - submit 前可以先透過 preview 看網站是否對於自己「埋進去的 tag」(其實是指 GTM container 是否被放入網站)有對應的行為。注意第一次 preview 前要有第一次的 submit。


### 檢查 GTM 設定是否正確
- 使用 preview 功能
- 使用 chrome plugin "Google Tag Assistant"
  - (稍微有點不太確定) 如果 GA property (名詞意義見下方 GA session) 是透過 GTM 放進去， Tag Assistant 會顯示 GA propery 對應到的 (html) tag 是「藍色」（ tag 生效但不保證未來也會正常工作）；但 GTM tag 本身則是「綠色」（正常工作）。
    - 從前端的 code 來看，會有這樣的結果很合理。畢竟我推想 tag assistant 不能直接透過 GTM 呼叫 GA tag 後取得所有詳細的資訊來確定 GA tag 是否完全正常工作、而只能取得部份 debug 用的資訊。


## Google Analysis (GA) 的基本概念與詞彙
在最一開始要稍微留意一下 2020 年底 Google Analysis 推出 Google Analysis 4 (GA4 or GA 4)，視為原本 Google Universal Analysis (UA) 下一代的產品，相當於原本只針對 web 分析的 UA 另外自動整合好行動裝置分析的功能。在這時間點之後建立的 property (名詞意義見下方說明)，預設 type 是 GA 4，不過使用者可以選擇 UA。**畢竟是剛開始的新功能，截至下筆本文時不時聽到有使用者反應 GA4 與 UA 兩者行為不太一致；所以建議在埋 property 的時候兩個都要裝到網站上同時參考兩者結果。**

使用 Google Analysis (GA) 的時候，有兩個重要的名詞：
  - property or app
    - 一個分析的「錨點」，是放在網站中執行分析時的最小執行單元。把一個 property 放進一個網站之後就可以開始分析網站了。
    - property 可以透過 GTM container 來放，或是自己直接放進網站。
      - 在最一開始沒有自己一套管理 GA property 方法的時候，可以考慮透過 GTM 統一管理自己放進網站的 property。
  - view (GA4 中沒有)
    - 呈現 property 資料的方式，中文介面翻譯成「報表」。
      - 一個 property 可以有很多種 view
    - view 屬性在 GA 4 中直接被整合進 property 定義好了；所以 GA admin 查閱 GA 4 property 的時候不會看到屬於該 property 的 view 可以選。
  - tracking ID (UA) 和 meansurement ID
    - property 下追蹤、分析、評估的 instance ID。要埋進網站的代號。
    - 我猜 UA 因為只有追蹤功能，所以 tracking ID 直接等於 UA property ID
    - 而 GA 4 因為同時強調「評估各種裝置與行為表現」，所以另外賦予 measurement ID


### Google Analysis (GA) 設定流程
設定流程大概是：
  - 建立新的 property；建立的時候就必須決定是 property type 是 GA 4 還是 UA (universal analysis)。
    - 也可以選「都建立」，這樣 GA4 property 會自動加上 suffix "- GA 4"
    - admin dashboard 中可以直接透過 property ID 看出兩者差異；如果是 UA type ，對應的 property ID 會有 prefix "UA-" (同時也是對應的 tracking ID)。 GA 4 對應的 ID 則是純整數 (要另外進去翻對應的 meansurement ID，有點小麻煩)。
  - (透過 tag 管理服務或是自己手動寫進網站 html 中來) 埋進網站
  - deploy 網站
  - 開始收資料


### 檢查 Google Analysis (GA) 設定結果
參考上面 "檢查 GTM 設定是否正確" ，使用 GTM preview 的時候同時打開 GA 的頁面看是不是有資料近來。


# 其他更多相關資訊
## 實做一瞥
- GTM 是在 html 中插入程式碼來取得對應 GTM ID (容器 ID) 的內容
  - head 中透過 javascript 呼叫
  - body 中透過 no script iframe
- UA 透過 gtag.js
- 另外似乎還有可以兼容更多 tag type 的 analysis.js 的用法，還需要另外理解中。


## 報表分析
這篇講最基本的設定而已，報表分析設定完全沒有提到。這邊可以另外開一個主題來聊。


## 其他容易混淆的概念與詞彙
html tag 與 GTM 的 tag 不是指同一件事情；雖然命名上可能是來自「在 html 插入一段特別的 html tag 來實做 GTM」的關係。
