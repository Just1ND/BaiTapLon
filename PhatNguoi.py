import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ham thuc hien tra cuu phat nguoi
def run_tra_cuu():
    print("Dang mo trinh duyet va tai trang...")

    # Mo trinh duyet Chrome (can cai ChromeDriver tuong ung voi trinh duyet)
    driver = webdriver.Chrome()

    # Mo trang tra cuu
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    # Doi toi khi truong nhap bien so xuat hien (toi da 60 giay)
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "BienKiemSoat"))
        )
    except:
        print("Khong the tai duoc trang. Thu lai sau.")
        driver.quit()
        return

    # Nhap thong tin bien so va loai xe
    driver.find_element(By.ID, "BienKiemSoat").send_keys("29A12345")
    driver.find_element(By.ID, "LoaiXe").send_keys("O to")

    # Can nguoi dung tu nhap captcha va bam nut tra cuu
    input("Vui long nhap captcha va bam nut 'Tra cuu' tren trinh duyet, sau do nhan Enter tai day de tiep tuc...")

    # Doi ket qua hien ra
    time.sleep(30)  # Co the giam xuong neu ket noi nhanh

    # Tim cac ket qua tra ve
    results = driver.find_elements(By.CLASS_NAME, "btnTraCuu")
    if results:
        print("Ket qua phat nguoi:")
        for result in results:
            print(result.text.strip())
    else:
        print("Khong co ket qua hoac captcha sai.")

    # Dong trinh duyet
    driver.quit()

# Ham cho den dung gio (vi du: 6 hoac 12)
def wait_until(target_hour):
    while True:
        now = datetime.datetime.now()
        # Neu dung gio va phut 0 (vi du: 6:00 hoac 12:00)
        if now.hour == target_hour and now.minute == 0:
            print(f"\n--- Bat dau tra cuu luc {target_hour}:00 ---")
            run_tra_cuu()
            print(f"--- Hoan thanh tra cuu luc {target_hour}:00 ---\n")
            time.sleep(60)  # Cho qua phut hien tai de tranh chay lai
        else:
            time.sleep(20)  # Kiem tra lai moi 20 giay

# Chuong trinh chinh
if __name__ == "__main__":
    print("Dang chay... Se tu dong tra cuu luc 6h va 12h hang ngay.")
    while True:
        wait_until(6)
        wait_until(12)