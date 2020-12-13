Title: 設計命令列應用程式 - Design CLI Command
Status: published
Date: 2020-12-13 19:00
Tags: programming, design pattern
Category: programming
Slug: programming-code-01-12-factor-cli


![boardroom-meeting-suggestion-meme-awk.png]({static}/images/boardroom-meeting-suggestion-meme-awk.png "boardroom meeting suggestion meme awk")


# 命令列 (commandline, cli) 是眾多人機互動方式 (HCI) 的一種
人要和電腦互動[1]，有眾多方式；若是是透過一個中間者轉發輸入輸出的方式，我們稱中間者叫做「人機互動介面」([HCI](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction))。例如，虛擬實境的裝置中，「揮手」就是一個常見的實做。我們操作手機是透過點選螢幕，那個「點選的動作」與「螢幕上的圖片」則是這個情境下的人機互動實做。所以其實這樣的概念與實做充斥在有著計算機的生活環境中。

對於有些程式開發者，打開終端機之後開始「打字」、輸入命令請電腦/計算機做事情是每天的例行公事。在這樣的情境中，「只顯示文字的終端機」與「輸入的文字命令」本質上也是一種 HCI 實做；和其他的人機互動方式最大的差別則是命令列使用的是「命令」、是文字的 (textual or text-based) ，而不是「點選圖片」或「揮手」。

[1] 達到輸入（人輸入資料給電腦）與輸出（人接收電腦運算完成的資料）


## Textual 的好處使 cli Interface 歷久不衰
雖然相對於直接點選圖片而言， text-based 命令列似乎是較不直觀的 HCI[1]，但是卻一直沒有被時代淘汰。 Eric Steven Raymond 所著作的 [The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/index.html) 或許可以部份回答這個問題。例如書中第五章提到針對資料記載與傳送的 textuality 的部份討論 [2] ，但「透明」（不需要特殊工作就能讀寫）這點所達成的平台可攜性則是異曲同工，此外還有「支援 pipes or filters 」等等的理由 [3][4]，造成實做工具與使用上其他類型的 HCI 難以短時間內取代與普及。[5]


[1] 有時候可能不是事實；圖形介面有時候也並沒有比較直觀好懂。大家可以回想一下自己第一次接觸瀏覽器中自己原本不知道的功能、或是接觸一個自己不懂 domain knowledge 的圖形應用程式時的感覺：畫面上看起來好像每個 label 都知道可以點，但其實我們不知道點下去會發生什麼事情。只是「圖像」本身會給人「自己對這個東西熟悉」的錯覺（進而或許可以有足夠動機跨過基本學習操作的門檻）。

[2] 請參考 [The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/index.html) 第五章 Textuality 的 [The Importance of Being Textual](http://www.catb.org/esr/writings/taoup/html/ch05s01.html) 章節。

[3] [The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/index.html) 第十章 http://www.catb.org/esr/writings/taoup/html/ch10s05.html

[4] 順帶一提，[第十一章的 Language-Based Interface Patterns 段落](http://www.catb.org/esr/writings/taoup/html/ch11s06.html#id2959821)中提到 `One of the most potent Unix design patterns is the combination of a GUI front end with a CLI minilanguage back end.` ，這是一個非常經典且常見的實做 pattern。許多經典服務都有採用這種模式，例如 tftp、 smtp 伺服器。留意到這件事情的話，會對於在選用相關工具與閱讀其程式碼上有所助益。

[5] 這其實是人們一直以來喜歡~~~抬槓~~~討論的議題，例如[這則 Hacker News](https://news.ycombinator.com/item?id=18172689)就是很典型地人們總是會問為什麼一定要 cli command，然後也有人會回答替代方案其實可以是什麼。


# 一些 cli command 的設計原則
關於 cli command 的設計原則，不知道是什麼緣故，或許是看起來不夠時髦（畢竟已經存在幾十年、也已經很普及）、人們對於它的存在足夠熟悉與直觀（像空氣一樣所以不覺得有什麼好討論）、還是這類工具已經有一定的發展與成熟度（所以貿然討論或許會顯示自己不知道的事情 XD），總之相對於其他種程式架構與介面設計，關於 cli 的討論「似乎」是相對少的（誠心發問：有 UX 設計師是在做 cli 設計的嗎？）。少歸少，還是有一些，以下我稍微列舉出一些我曾經看過的；歡迎大家不吝賜教更多好的設計原則與討論。


## Command Line Interface Guidelines
[Command Line Interface Guidelines](https://clig.dev/) 相對新（第一個 commit 是 2020 四月，目前仍在活躍更新中）且完整的討論，值得一讀。另外底下的 Further reading 也很精彩，不要輕易錯過。


## 12 Factor CLI Apps
類似於知名的 [12 Factor App](https://12factor.net/)，Jeff Dickey 寫了[給 cli 的版本](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)。不確定是什麼原因，我個人比較喜歡 [12 Factor App](https://12factor.net/)，[12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)，或許是這篇沒有給我「啊哈」的感覺吧。

另外 [這則 Hacker News](https://news.ycombinator.com/item?id=18172689) 有一些關於這篇文章的討論。


## The Art of Unix Programming
[The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/index.html) 討論整個 unix 系統設計，所以當然也包括 unix 系統設計上慣用的 cli 哲學，比起上面的討論材料，本書更偏向闡述 unix 本身使用的 cli 風格與慣例，適合有使用 unix 或 unix-like 系統的軟體開發者綜覽與了解一些慣例與風格。


# 實做時該參考哪一些原則
跟所有軟體設計一樣，情境是重要的，很多時候也沒有標準答案。一個快速粗糙的答案，我目前會說：

- 時間資源相對不夠、或是要求相對不嚴謹的專案，參考 [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46) 即可。
- 想要相對嚴謹的話，可依循 [Command Line Interface Guidelines](https://clig.dev/) 的建議。

另外各程式語言往往會有自己語言 ecosystem 中受歡迎的用來建立 cli tool 的工具或框架。以 python 為例，除了標準的 argparse 以外，像是 click 、 fire 等等，不同的工具往往透露出不同的設計品味與原則，像是 subcommand 的風格、是不是嚴格要求 flag 一定要 double dash 等等，也不妨自己實際拿來用用看，撰寫與過不同風格的 cli tool 之後，一定會有一套屬於自己的 12 factor for cli app 思維。
