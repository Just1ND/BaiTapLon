import datetime
import time
import pytesseract
from PIL import Image
from io import BytesIO
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_tra_cuu():
    print("Đang mở trình duyệt và tải trang...")

    driver = webdriver.Chrome()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "BienKiemSoat"))
        )
    except:
        print("Không thể tải được trang. Thử lại sau.")
        driver.quit()
        return

    driver.find_element(By.ID, "BienKiemSoat").send_keys("30A12345")
    driver.find_element(By.ID, "LoaiXe").send_keys("Ô tô")

    # --- Xử lý Captcha ---
    captcha_element = driver.find_element(By.ID, "captchaImage")
    captcha_image = captcha_element.screenshot_as_png
    image = Image.open(BytesIO(captcha_image))

    # OCR không cần tiền xử lý
    captcha_text = pytesseract.image_to_string(image, config='--psm 8').strip()
    captcha_text = ''.join(filter(str.isalnum, captcha_text))  # loại bỏ ký tự lạ
    print(f"Mã Captcha nhận dạng: {captcha_text}")

    # Điền captcha và bấm nút "Tra cứu"
    captcha_input = driver.find_element(By.ID, "CaptchaInput")
    captcha_input.send_keys(captcha_text)
    driver.find_element(By.ID, "btnTraCuu").click()

    # Đợi kết quả hiện ra
    time.sleep(10)

    results = driver.find_elements(By.CLASS_NAME, "btnTraCuu")
    if results:
        print("Kết quả phạt nguội:")
        for result in results:
            print(result.text.strip())
    else:
        print("Không có kết quả hoặc captcha sai.")

    driver.quit()

# Hàm cho đến đúng giờ (ví dụ: 6h hoặc 12h)
def wait_until(target_hour):
    while True:
        now = datetime.datetime.now()
        # Nếu đúng giờ và phút 0 (ví dụ: 6:00 hoặc 12:00)
        if now.hour == target_hour and now.minute == 0:
            print(f"\n--- Bắt đầu tra cứu lúc {target_hour}:00 ---")
            run_tra_cuu()
            print(f"--- Hoàn thành tra cứu lúc {target_hour}:00 ---\n")
            time.sleep(60)  # Chờ qua phút hiện tại để tránh chạy lại
        else:
            time.sleep(20)  # Kiểm tra lại mỗi 20 giây

# Chương trình chính
if __name__ == "__main__":
    print("Đang chạy... Sẽ tự động tra cứu lúc 6h và 12h hàng ngày.")
    while True:
        wait_until(6)  # Chạy vào lúc 6h sáng
        wait_until(12)  # Chạy vào lúc 12h trưa
