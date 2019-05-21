from scrapy import cmdline

# 执行文件
cmdline.execute("scrapy crawl books  ".split())  # -o: output<输出>   books.csv： 自动生成并保存到 books.csv



# 创建项目目录：

   #  cmd *  scapy startproject booksScrapy