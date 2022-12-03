from pypasser import reCaptchaV3

# # Open target
# driver.get('https://www.google.com/recaptcha/api2/demo')

def test():
    # Solve reCaptcha v2 via PyPasser
    is_checked = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdyC2cUAAAAACGuDKpXeDorzUDWXmdqeg-xy696&co=aHR0cHM6Ly9yZWNhcHRjaGEtZGVtby5hcHBzcG90LmNvbTo0NDM.&hl=en&v=Km9gKuG06He-isPsP6saG8cn&size=invisible&cb=p9lqe5u8j7ix')

    if is_checked:
        # Click submit button
        # driver.find_element(By.CSS_SELECTOR, '#recaptcha-demo-submit').click()
        # if 'Verification Success' in driver.page_source:
        print('SUCCESS')

    else:
        print('FAIL')

if __name__ == '__main__':
    test()