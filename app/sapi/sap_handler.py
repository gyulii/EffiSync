"""
It will communicate with SAP through API call or through brute force web automatization.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

import pandas as pd
from datetime import datetime, timedelta
import time


import collections


from app.booking import BookingItem

class EssDriver:
    def __init__(self, headless: bool = False):
        self.headless = headless
        self.booking_queue = list()
        self.current_date_formated = get_current_date_formated()

        options = webdriver.EdgeOptions()
        if self.headless == True:
            options.add_argument("--headless=new")

        self.driver = webdriver.Edge(options=options) #ez nyitja meg a browsert

    def add_booking_item_to_queue(self, booking_item: BookingItem):
        self.booking_queue.append(booking_item)

    def quit(self):
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//li[@id="logoff_link"]').click()

        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    '//iframe[@id="iframeLogoffMsgDialog"]',
                )
            )
        )

        self.driver.find_element(By.XPATH, '//li[@id="buttonOK1"]').click()
        self.driver.quit()

    def update_table_and_get_elements(self):

        table = self.driver.find_element(By.XPATH, '//tbody[contains(@id,"-contentTBody")]')
        booking_table_element = table.find_elements(By.XPATH, "//tr[@rr > 0]")

        return table, booking_table_element

    def get_table_data(self):

        table, booking_table_element = self.update_table_and_get_elements()

        table_data = []

        for row in booking_table_element:
            row_data = []
            cells = row.find_elements(By.XPATH, "./td")
            for cell in cells:
                # print(cell.text) # Debug
                row_data.append(cell.text)
            table_data.append(row_data)

        headers = table.find_elements(By.XPATH, "//tr[@rt > 0]/th")
        headers_string = []
        for element in headers:
            headers_string.append(element.text)

        df = pd.DataFrame(table_data)
        df.columns = headers_string

        return table, df, booking_table_element

    def update_ess_table(self, table_element, row, col, value):
        row_element = table_element[row].find_elements(By.XPATH, "./td")  # Get the needed row element
        row_element[col].click()  # Click on the needed row
        ActionChains(self.driver).send_keys(value).perform()

    def book_item(self, df: pd.DataFrame, booking_item: BookingItem):

        table, booking_table_element = self.update_table_and_get_elements()

        # Check if we have the booking text already, it returns row list with the found rows, or an empty list
        row = df[df["Text\n "] == booking_item.text].index
        text_found_in_table = len(row)  # Empty list = Not booked yet
        col_to_write = -1

        if text_found_in_table == 1:
            row_to_write = row[0]

            col_to_write = df.columns.get_loc(self.current_date_formated)  # Get the col number of the given date
            self.update_ess_table(
                booking_table_element,
                row_to_write,
                col_to_write,
                booking_item.booked_hours,
            )
            df.loc[row, self.current_date_formated] = booking_item.booked_hours

        elif text_found_in_table == 0:
            row_to_write = 2

            for row_number, current_row_text in enumerate(df["Att./abs. type\n "].tolist()):
                if row_number >= 2:  # Ignore first two rows Vacation!!!! #TODO
                    if current_row_text == "":  # First empty row
                        row_to_write = row_number
                        col_to_write = df.columns.get_loc(self.current_date_formated)  # Get the col number of the given date

                        self.update_ess_table(
                            table_element=booking_table_element,
                            row=row_to_write,
                            col=col_to_write,
                            value=booking_item.booked_hours,
                        )
                        df.loc[row_to_write, self.current_date_formated] = booking_item.booked_hours

                        self.update_ess_table(
                            table_element=booking_table_element,
                            row=row_to_write,
                            col=df.columns.get_loc("Text\n "),
                            value=booking_item.text,
                        )
                        df.loc[row_to_write, "Text\n "] = booking_item.text

                        self.update_ess_table(
                            table_element=booking_table_element,
                            row=row_to_write,
                            col=df.columns.get_loc("WBS Element\n "),
                            value=booking_item.wbs,
                        )

                        df.loc[row_to_write, "WBS Element\n "] = booking_item.wbs

                        self.update_ess_table(
                            table_element=booking_table_element,
                            row=row_to_write,
                            col=df.columns.get_loc("Att./abs. type\n "),
                            value="1",  # Productive item
                        )

                        df.loc[row_to_write, "Att./abs. type\n "] = booking_item.booked_hours
                        break

        self.driver.find_element(By.XPATH, '//div[@t="Choose Delete to Delete the Row"]').click()  # Reset table
        time.sleep(1)

    def execute_booking(self):

        self.driver.maximize_window()

        self.driver.implicitly_wait(15)
        try:
            self.driver.get("https://desktop.avl.com/corp/01/0062/02/15/PAGES/ESS.aspx")
        except WebDriverException:
            print("Could not open ESS please, check if you are using the right VPN")

        self.driver.find_element(By.LINK_TEXT, "Language: English").click()

        handles = self.driver.window_handles
        new_tab_handle = handles[-1]  # The new tab should be the last one in the list
        self.driver.switch_to.window(new_tab_handle)

        WebDriverWait(self.driver, 120).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    '//iframe[@aria-label="The title of the hosted application within the canvas area: Employee Self-Service AVL Hungary / AVL Zalazone"]',
                )
            )
        )

        self.driver.find_element(By.LINK_TEXT, "Record Working Time").click()

        handles = self.driver.window_handles
        new_tab_handle = handles[-1]  # The new tab should be the last one in the list
        self.driver.switch_to.window(new_tab_handle)

        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    '//iframe[@aria-label="The title of the hosted application within the canvas area: Record Working Time"]',
                )
            )
        )

        self.driver.execute_script("document.body.style.zoom='40%'") # You need this since the whole page is dynamic JS based

        current_ess_date_raw = self.driver.find_element(By.XPATH, "//input[contains(@id, 'WD')]").get_attribute("Value")
        current_ess_date = datetime.strptime(current_ess_date_raw, "%Y.%m.%d")

        current_date = datetime.now()
        monday = current_date - timedelta(days=current_date.weekday())

        if monday > current_ess_date:
            self.driver.find_element(By.XPATH, '//div[@title="Next Period"]').click()

        time.sleep(3)

        table, df, booking_table_element = self.get_table_data()

        for booking_item in self.booking_queue:
            self.book_item(df, booking_item)


def get_current_date_formated():

    current_date = datetime.now()
    monday = current_date - timedelta(days=current_date.weekday())
    date_dict = {}
    for day in range(7):
        day_date = monday + timedelta(day)
        day_name = day_date.strftime("%a").upper()[:2]  # Get the first two letters and make them uppercase
        formatted_date = day_date.strftime("%m.%d\n ")  # Get something like this: '04.14\n '
        date_dict[day_date.date()] = f"{day_name}, {formatted_date}"

    current_date_formated = date_dict[current_date.date()]

    return current_date_formated

# Example usage

if __name__ == "__main__":
    driver = EssDriver(headless=False)
    book1 = BookingItem(text="Booking_text_sample", booked_hours=4)
    driver.add_booking_item_to_queue(book1)
    driver.execute_booking()
    driver.quit()
