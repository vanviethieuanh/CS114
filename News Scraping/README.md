# Báo cáo thu thập dataset cho bài toán "Sarcasm detection in news headline"

**Thành viên nhóm**

19521731 Nguyễn Đại Kỳ

19521225 Văn Viết Hiếu Anh

19522054 Lê Văn Phước 



**Những trang nhóm lấy dữ liệu:**

- Trang chính thống: 
  - https://www.theguardian.com/ 
  - https://www.cbsnews.com 
  - https://www.theaustralian.com.au/ 

- Trang châm biếm: 
  - https://clickhole.com/ 
  - https://thehardtimes.net/ 

  - https://www.thepoke.co.uk/ 
  - https://babylonbee.com/

## Tổng quan dữ liệu thu thập

Gồm **120.000** records từ

| Trang | Số lượng | Châm biếm ? |
| ----- | -------- | ----------- |
|clickhole.com|1771|True|
|thepoke.co.uk|1157|True|
|babylonbee.com|7043|True|
|newyorker.com|13704|True|



## Dataset Format

```json
[
    {
        "article_link": "https:\/\/www.theguardian.com\/law\/2021\/jun\/08\/powerful-new-watchdog-will-target-unscrupulous-employers-says-no-10",
        "headline": " \u2018Powerful\u2019 new watchdog will target unscrupulous employers, says No 10",
        "posted_at": "06-07-2021",
        "is_sarcastic": 0
    },
    ...
]
```

**article_link** Đường dẫn đến bài viết

**headline** Tiêu đề bài viết

**posted_at** Ngày bài viết được đăng

**is_sarcastic** Bài Viết có phải là châm biếm ?



## Quá trình thu thập

### The Guardian

