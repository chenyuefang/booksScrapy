from scrapy import cmdline

# 执行文件
cmdline.execute("scrapy crawl books -o books.csv ".split())  # -o: output<输出>   books.csv： 自动生成并保存到 books.csv
