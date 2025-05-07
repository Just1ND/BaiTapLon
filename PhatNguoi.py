import datetime
import time
import pytesseract
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hàm thực hiện tra cứu phạt nguội
def run_tra_cuu():
    print("Dang mo trinh duyet va tai trang...")

    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    try:
        # Chờ đợi trang tải xong và ô nhập biển số xuất hiện (tối đa 60 giây)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "BienKiemSoat"))
        )
    except:
        # Nếu không thể tải trang, dừng chương trình và thoát
        print("Khong the tai duoc trang. Thu lai sau.")
        driver.quit()
        return

    # Nhập biển số và loại xe (có thể thay đổi biển số và loại xe trong quá trình sử dụng)
    driver.find_element(By.ID, "BienKiemSoat").send_keys("30A12345")
    driver.find_element(By.ID, "LoaiXe").send_keys("O to")

    # --- Xử lý Captcha ---
    captcha_element = driver.find_element(By.ID, "captchaImage")
    captcha_image = captcha_element.screenshot_as_png  # Lấy ảnh Captcha
    image = Image.open(BytesIO(captcha_image))  # Đọc ảnh captcha

    # Dùng thư viện pytesseract để nhận dạng văn bản trong ảnh (OCR)
    captcha_text = pytesseract.image_to_string(image, config='--psm 8').strip()
    captcha_text = ''.join(filter(str.isalnum, captcha_text))  # Loại bỏ ký tự không hợp lệ
    print(f"Ma Captcha nhan dang: {captcha_text}")

    # Điền captcha vào ô nhập và bấm nút "Tra cứu"
    captcha_input = driver.find_element(By.ID, "CaptchaInput")
    captcha_input.send_keys(captcha_text)
    driver.find_element(By.ID, "btnTraCuu").click()

    # Đợi kết quả tra cứu xuất hiện (10 giây)
    time.sleep(10)

    # Lấy kết quả và in ra
    results = driver.find_elements(By.CLASS_NAME, "btnTraCuu")
    if results:
        print("Ket qua phat nguoi:")
        for result in results:
            print(result.text.strip())  # Hiển thị kết quả
    else:
        print("Khong co ket qua hoac captcha sai.")

    driver.quit()

# Hàm để chờ đến đúng giờ tra cứu (ví dụ: 6h hoặc 12h)
def wait_until(target_hour):
    while True:
        now = datetime.datetime.now()  # Lấy thời gian hiện tại
        # Nếu đúng giờ và phút là 0 (ví dụ: 6:00 hoặc 12:00)
        if now.hour == target_hour and now.minute == 0:
            print(f"\n--- Bat dau tra cuu luc {target_hour}:00 ---")
            run_tra_cuu()  # Gọi hàm tra cứu
            print(f"--- Hoan thanh tra cuu luc {target_hour}:00 ---\n")
            time.sleep(60)  # Chờ 60 giây để tránh chạy lại vào phút sau
        else:
            time.sleep(20)  # Kiểm tra lại mỗi 20 giây

# Chương trình chính, bắt đầu chạy và tự động tra cứu vào các giờ nhất định
if __name__ == "__main__":
    print("Dang chay... Se tu dong tra cuu luc 6h va 12h hang ngay.")
    while True:
        wait_until(6)  # Tra cứu vào lúc 6h sáng
        wait_until(12)  # Tra cứu vào lúc 12h trưa
