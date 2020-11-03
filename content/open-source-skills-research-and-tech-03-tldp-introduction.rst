Advanced Bash-Scripting Guide 簡介
##################################

:status: published
:date: 2020-10-30 14:00
:tags: open source, code reading, bash
:category: development
:slug: open-source-skills-research-and-tech-03-tldp-introduction


二十一世紀了，來點 Bash Script 吧
*********************************

The Linux Documentation Project (TLDP) 顧名思義就是給 Linux 撰寫文件的專案，內容基本上涵蓋整個 Linux 使用上與原理上的基本概念，有些（其實是大部分）篇章甚至集結成冊，由 O'Reilly 出版成著名的動物系列書之一。其中的 Advanced Bash-Scripting Guide 是我日常中最常從 TLDP 文件中索引的一本。

2020 各種絢麗的技術與程式語言資訊滿天飛的今天，聊聊 Bash 好像是一種老派到浪漫 (？) 的事情。不太有印象有人用中文撰寫、介紹過 TLDP 下的 Advanced Bash-Scripting Guide ，希望這個介紹可以讓中文社群也能多多善用這個資源。


不活躍但已經臻於成熟的 TLDP
***************************

時至今日， TLDP 其實已經是相對不活躍的專案了。最後一次的文件更新大約在 2016 年前後，而最後一份新的的 guide 則是在 2014 前後。一個開源專案逐漸不活躍通常是很多原因綜合結果；我認為 TLDP 專案不活躍了主要是因為相關的基本知識已經逐漸涵蓋與完備，隨著資訊世界的發展，領域的多樣性與特化使得資訊量大幅提昇，這種集中式的文件發展方式沒有跟上的能量可說是理所當然。如果我們把標準放在「涵蓋最基礎需要的、一定深度的知識，有了這些知識之後就可以開始揚帆去探索無邊世界」，或是「出新手村前的準備」的話， TLDP 蒐羅的文件無疑是已經發展成熟。


比 Bash 使用者手冊好讀太多的 Advanced Bash-Scripting Guide
**********************************************************

做研究探索未知領域，例如學術研究，或是掌握既有知識體系，第一手資訊往往理解脈落與細節上最可靠的材料。這類材料，例如說學術研究上有期刊論文、工程上可以是規格手冊、社群經營上則可以是 mailing list archive。但第一手資料往往有過於不夠系統化的門檻在，所以相對難以整合。`Advanced Bash-Scripting Guide <https://tldp.org/LDP/abs/html/index.html>`_ 則是少數將 Bash 語言用一種接近規格書一樣廣泛、但又已經從使用者與學習者的角度來撰寫成類似於教科書風格的文件，在我心目中可說是僅次於 Bash 使用手冊的第一手資訊：兼顧規格書般的完整，又不會像規格書一樣生冷難讀。

Bash 的使用手冊有多生冷難讀呢？你可以打開你系統中的終端機輸入 **man bash** 試著閱讀看看，或是我們也可以參考一下 Joel Spolsky 在他的 `Biculturalism 一文 <https://www.joelonsoftware.com/2003/12/14/biculturalism/>`_ 中提到的一段話：

    Let’s look at another cultural difference. Raymond says, “Classic Unix documentation is written to be telegraphic but complete… The style assumes an active reader, one who is able to deduce obvious unsaid consequences of what is said, and who has the self-confidence to trust those deductions. Read every word carefully, because you will seldom be told anything twice.” Oy vey, I thought, he’s actually teaching young programmers to write more impossible man pages.


呼呼！！


Advanced Bash-Scripting Guide 全文提供 txt 檔
*********************************************

「破碎的知識片段只是方便，遲早要建立自己的工具書與知識庫」這道理相信大家都已經很熟悉了。「遇到什麼語法問題或是程式錯誤訊息，先餵 Google 再說！」這是一個大家都非常熟悉且方便取得答案的作法。透過 Google 取得的答案，往往都是針對自己當下那個問題的答案，知識粒度是相對小的。另外，透過搜尋引擎，再怎麼快取得回傳結果到自己手上，（在現在的科技與商業化程度下）即使捨棄不必要的前端 rederning 與不考量頻寬問題，大概也很難跟自己電腦上使用 grep + SSD 硬碟一樣快 ( grep 實做的數學算法可是人類已知最快的字串匹配算法呢！）； grep 還是離線作業呢！Advanced Bash-Scripting Guide 全文提供 txt 檔 ！還不快點 grep 起來！


固態硬碟和 grep -C 是搜尋筆記的好幫手
=====================================

grep 指令提供了 -C 這個選項，可以在搜到的字串中同時顯示上下行數；如果多年使用 Advanced Bash-Scripting Guide ，自然會對裡面有什麼大概有些印象。這時候只要 grep 關鍵字往往可以馬上取得自己想要索引的資訊。像是

.. code-block:: sh

    $ grep 'Parameter Substitution' abs-guide.txt  -C 3
       B-1. Special Shell Variables
       B-2. TEST Operators: Binary Comparison
       B-3. TEST Operators: Files
       B-4. Parameter Substitution and Expansion
       B-5. String Operations
       B-6. Miscellaneous Constructs
       C-1. Basic sed operators
    --
       10. Manipulating Variables

            10.1. Manipulating Strings
            10.2. Parameter Substitution

       11. Loops and Branches

    --
        7. Example A-41
         ________________________________________________________________

    10.2. Parameter Substitution

       Manipulating and/or expanding variables

    --
    #+ to the person invoking it, for example, bozo@localhost.localdomain.
    #
    #  For more on the ${parameter:-default} construct,
    #+ see the "Parameter Substitution" section
    #+ of the "Variables Revisited" chapter.

    # ============================================================================
    --

       * Binary operator (requires two operands).

       Table B-4. Parameter Substitution and Expansion
       Expression Meaning
       ${var} Value of var (same as $var)


馬上就知道要去哪個章節找自己想知道的使用方式與語法！！這時候再去打開整個手冊查找自己要的章節。不斷迭代這樣的作法，一陣子時間之後就可以在大多數情況下大幅降低 Google 或是問 stackoverflow 的次數，並且讓 Advanced Bash-Scripting Guide 逐漸成為自己的離線知識庫的一部分。有興趣的話你也可以上 `TLDP 的網站 <https://tldp.org>`_ 下載全文 txt ，祝 grep 愉快。
