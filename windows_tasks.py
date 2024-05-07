from robocorp.tasks import task
from robocorp import windows
from RPA.Desktop import Desktop
from support import get_locator, print_values


# https://github.com/yinkaisheng/Python-UIAutomation-for-Windows
# https://robocorp.com/docs/visual-studio-code/locators/windows-locators
# https://github.com/robocorp/robocorp/blob/master/windows/docs/api/robocorp.windows.md


@task
def example_on_windows():
    """
    Example on Windows
    """
    calc = windows.find_window("name:Calculator")
    # Press button "0" (the locator may vary based on the Windows version).
    button0 = calc.find("(name:0 or name:Zero) and type:Button")
    button0.click()

    # Clear the Calculator (the locator may vary based on the Windows version).
    calc.click("id:clearEntryButton or name:Clear")

    # Send the keys directly to the Calculator by typing them from the keyboard.
    calc.send_keys(keys="96+4=")

    print_values(calc)

    Desktop().click("alias:image-plus-button")

    calc.send_keys(keys="8=")

    print_values(calc)

    Desktop().click("alias:multi-button")
    calc.send_keys(keys="2=")
    print_values(calc)
