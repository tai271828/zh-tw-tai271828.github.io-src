Title: Reflection of My First Airflow DAG Implementation
Date: 2021-1-2 15:00
Tags: template, <string to fill>, <string to fill>
Category: <string to fill>
Slug: software-engineering-01-airflow-jenkins

# <This head is important to make the following contents explicit>

順手分享一下寫第一個  airflow dag 的感覺 vs. jenkins XD

在實做第一個 dag 前會覺得「除了介面不一樣，不都是排程工具？」實做後就可以感受到細節的差異，像是硬要 code as configuration

暫時覺得可以這樣區分：
airflow - 適合接近 application 或以上的工作排程（難怪被人們拿來做 ELT）
jenkins - 老牌、泛用性高
