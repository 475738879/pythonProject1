url = 'html/2019-05/06'
# 先根据 / 分割，得到 group1
group1 = url.split('/')
# 分割完后，group1 = ["html","2019-05","06"]
day = group1[2]        # day = "06"

# 将 group1[1]，也就是 2019-05 进行分割，根据 - 分割成 group2
group2 = group1[1].split("-")
# 分割完成后，group2  = ["2019","05"]
year = group2[0]       # year = "2019"
month = group2[1]      # month = "05"
