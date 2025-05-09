# Tự động tra cứu phạt nguội 

Đây là một công cụ đơn giản sử dụng Python và Selenium để tự động mở trang [CSGT - Tra cứu phương tiện vi phạm](https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html), nhập sẵn thông tin biển số và loại xe, chờ người dùng nhập mã CAPTCHA và tra cứu. Chương trình sẽ tự động chạy vào lúc 6h và 12h mỗi ngày.

## Tính năng

- Tự động mở trang tra cứu vi phạm giao thông.
- Điền sẵn biển số và loại xe.
- Người dùng chỉ cần nhập CAPTCHA và bấm "Tra cứu".
- Hiển thị kết quả tra cứu ra terminal.
- Lặp lại mỗi ngày vào 6h và 12h.

## Cài đặt

### 1. Cài đặt Python

Trước tiên, bạn cần cài đặt Python trên máy tính của mình:

- Tải Python từ [https://www.python.org/downloads/](https://www.python.org/downloads/).
- Trong quá trình cài đặt, **chọn tùy chọn Add Python to PATH** để dễ dàng sử dụng Python từ dòng lệnh.
### 2. Cài đặt thư viện yêu cầu
- Sau khi cài đặt Python, bạn cần cài đặt các thư viện phụ thuộc. Để làm điều này, bạn chỉ cần chạy lệnh dưới đây trong thư mục dự án: 
```bash
pip install -r requirements.txt
```
### 3. Tải về project

- Clone dự án về máy tính của bạn bằng Git:

```bash
git clone https://github.com/Just1ND/BaiTapLon.git
cd BaiTapLon
```