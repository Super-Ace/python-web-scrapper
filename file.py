import time

def page_down(page):
    for x in range(5):
        time.sleep(5)
        page.keyboard.down("End")

