from gui import *

def main():
    """
    code for creating the window and running the application
    :return:
    """
    window = Tk()
    window.title("Weather")
    window.geometry("300x100")
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
