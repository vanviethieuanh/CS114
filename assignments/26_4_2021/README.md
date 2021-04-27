# Tìm một số bài toán sử dụng Regression trong thực tế.
#### 1. Bài toán dự đoán giá vàng.
+ Input: 

#### 2. Dự đoán mức lương cơ bản của một nhân viên để cho người phỏng vấn biết cần phải cho người ứng tuyển mức lương tối đa anh ta nhận được. (Mặc dù khi phỏng vấn, người ứng tuyển có thể deal lương của mình với công ty nhưng kết quả dự đoán này cho biết người phỏng vấn phải biết tối đa mức lương của người xin việc nhận được tương ứng với năng lực của người đó)
+ Input: 
  - Mức độ học vấn
  - Kinh nghiệm
  - Những công ty đã từng làm và chức vụ
  - Các chứng chỉ đi kèm hoặc các kỹ năng mềm hiện có.
+ Output:
  - Mức lương khi mới vào của nhân viên
 
+ Data:
  - Lấy từ hồ sơ phỏng vấn của người ứng tuyển khi mới nộp vào.
  - Đối với Mức độ học vấn thì ta sẽ quy định với trình độ học vấn nào thì ứng với con số nào để máy tính hiểu được
  - Kinh nghiệm thì bằng dữ liệu số
  - Những công ty đã từng làm và chức vụ thì ta cũng quy định đối với công ty như thế nào thì ứng với con số nhất định, chức vụ cũng vậy (Đối với mục này thì bạn cần phải có một dữ liệu công ty ngành công nghệ thông tin lớn và số chức vụ trong ngành công nghệ thông tin)
  - Các chứng chỉ thì tương ưng với số điềm có quy định.

#### 3. Dự đoán mức độ lạm phát của VNĐ trong quý tiếp theo
  + Input:
    - Tổng sản phẩm nội địa (GDP)
    - Mức độ tăng của lạm phát theo từng tháng
    - Official development assistance (ODA)
    - Foreign direct investment (FDI)
  + Output:
    - Mức độ lạm phát của quý tiếp theo
  + Data:
    - https://finance.vietstock.vn/du-lieu-vi-mo
