import cv2

age_to_ad = {
    "(0-3) Male":"ads/one.jpg",
    "(4-7) Male":"ads/m_two.jpeg",
    "(8-14) Male":"ads/m_three.jpg",
    "(15-24) Male":"ads/m_four.jpg",
    "(25-37) Male":"ads/m_five.jpg",
    "(38-47) Male":"ads/m_six.jpg",
    "(48-59) Male":"ads/m_seven.jpg",
    "(60-100) Male":"ads/m_eight.jpg",
    "(0-3) Female":"ads/one.jpg",
    "(4-7) Female":"ads/w_two.jpeg",
    "(8-14) Female":"ads/w_three.jpg",
    "(15-24) Female":"ads/w_four.jpg",
    "(25-37) Female":"ads/w_five.jpg",
    "(38-47) Female":"ads/w_six.jpg",
    "(48-59) Female":"ads/w_seven.jpg",
    "(60-100) Female":"ads/w_eight.jpg"
}

def show_add(age, gender):
    img = cv2.imread(age_to_ad[age +" " + gender])
    cv2.imshow("image", img)
    cv2.waitKey(0)