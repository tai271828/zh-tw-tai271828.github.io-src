Title: 進階使用 Matplotlib 需要的核心概念
Date: 2020-12-26 21:30
Tags: python, matplotlib, plotting
Category: python
Slug: python-matplotlib

# 你也可以創造範例之外更客製化的圖表
使用 matplotlib 一段時間的使用者，可能都會有「常常要搜索 stackoverflow 上的答案才能畫出範例沒有提到的圖表」[這種困擾](https://stackoverflow.com/questions/35677767/understanding-matplotlib-plt-figure-axarr)，有沒有可能只靠查閱 matplotlib 技術手冊或是原始碼，就找出自己畫自己想要的那種圖表呢？

答案是 yes；根據我自己的經驗，如果能夠了解 matplotlib 的圖表/畫布 (figure/canvas) 的三層結構，以及封裝 API 時物件導向 (OOP) 的方式，對於自己組合出自己想要的圖片會有很大的幫助。下面歸納了一些我認為有幫助的思維。


## 試著忘記 scripting 的使用方式
大多數人初學時、以及大多數範例往往是透過直接操作 `plt` 的方式來畫圖，這種方式與範例的好處是相對直觀、容易理解，而且程式碼較少、可能心裡障礙相對低一些、也比較快有成就感。不過解讀 matplotlib 的 render 機制時採用「操作 `plt` 來下指令」的思維，或許會阻礙更精緻的操作方式。要畫更客製化的圖表時，可能要忍住直接操作 `plt` 的衝動，這或許能夠避免掉很多繪製圖表的過程中有不預期的行為與奇怪的結果，例如圖片缺腳、顯示範圍沒有跟著變動等等，甚至避開網路上良莠不齊硬幹出來的「範例」（例如硬是把 text legend 當 title 用）。


## 樹狀且物件導向的結構
matplotlib 畫出的圖，上面每個元素都是對應到一個物件，例如 [figure、axis、text 等等](https://nbviewer.jupyter.org/github/WeatherGod/AnatomyOfMatplotlib/blob/master/AnatomyOfMatplotlib-Part1-Figures_Subplots_and_layouts.ipynb#Anatomy-of-a-%22Plot%22)。繪製客製化圖片的時候可以試著把這些元件叫出來後直接操作他們。查詢或是「猜」某些元件是否有某個 function 可以用的時候，也可以往物件間彼此繼承的方式去查（或猜）。matplotlib 的圖表是樹狀的，root 元素一定是 figure 物件，裡面「裝」上述各種物件（axis、text ......等等），所以 figure 是一種 `container` (matplotlib 語境下的術語)。


## 三層結構的 matplotlib API
物件間彼此的溝通透過 matplotlib API， 其 API 運作則是 [FigureCanvas、Renderer 與 Artist 三層之間彼此協力](https://matplotlib.org/tutorials/intermediate/artists.html)。這裡要稍微注意不要把用來裝東西的 figure 物件與 FigureCanvas layer 混淆了，前者是屬於 Artist layer 的 figure 物件，後者則是三大 layer 的其中一層。這個觀念在 [matplotlib 裡 tutorial 中對於 Artist 的說明](https://matplotlib.org/tutorials/intermediate/artists.html)有更詳細具體的說明，值得一讀。


# 總之務必讀過 Artist Tutorial
因為使用者大多數時候需要操作的 API 落在 Artist layer，其中又以 Axes class 物件最需要客製化操作，所以 [matplotlib 裡 tutorial 中對於 Artist 的說明](https://matplotlib.org/tutorials/intermediate/artists.html) 絕對不能錯過。最後附上這個週末完成的小範例：[一個 3x3 subplots 動畫](https://github.com/tai271828/shock-tube-cli/blob/dev/scripts/compare-1d.py)。
