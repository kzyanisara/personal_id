def is_valid(my_pid: str) -> bool:
    """
    ฟังก์ชันตรวจสอบเลข ปชช ว่า ถูกต้องหรือไม่ โดยการตรวจสอบ check digit
    :param my_pid: เลข ปชช ที่ต้องการทดสอบ
    :return: ผลลัพธ์ถูกหรือผิด
    """
    #
    first_12 = my_pid[0:12]
    chk_digit = my_pid[-1]
    sum = 0
    j = 13

    # sum ผลคูณของเลขประจำหลักและเลขบัตร
    for i in first_12:
        i = int(i)
        sum = sum + (i * j)
        j = j - 1

    # หารเอาเศษด้วย 11
    fract = sum % 11
    # เอา 11 ตั้ง ลบด้วยเศษ แล้วเอาเฉพาะหลักหน่วย โดยการแปลงเป็น str แล้วเอาตัวที่ -1 (หลักหน่วย)
    # our_chk_digit = str(11 - fract)[-1]
    # การหาหลักหน่วยใช้ mod 10 ก็ได้ โดยผลลัพจะเป็นตัวเลข int
    our_chk_digit = str( (11 - fract)%10 )
    # เอา check digit ที่คำนวณได้ มาเทียบกับ เลขบัตร ปชช หลักสุดท้ายที่ได้รับ
    if our_chk_digit == chk_digit:
        return True
    else:
        return False


def is_bkk(my_pid: str) -> bool:
    """
    ฟังก์ชั่นทดสอบว่าเป็นคน กทม ไหม
    :param my_pid: เลข ปชช ที่ต้องการทดสอบ
    :return: ผลลัพธ์ถูกหรือผิด
    """
    first_digit = my_pid[0]
    if first_digit == '1':
        return True
    else:
        return False