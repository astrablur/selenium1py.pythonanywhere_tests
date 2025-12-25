class MainPageLocators:
    LOGIN_LINK = ('id', 'loginlink')


class LoginPageLocators:
    LOGIN_FORM = ('id', 'login_form')
    REGISTER_FORM = ('id', 'register_form')


class ProductPageLocators:
    PRODUCT_NAME = ('css selector', '.product_main h1')
    PRODUCT_PRICE = ('css selector', '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = ('css selector', '.btn-add-to-basket')
    SUCCESS_MSG = (
        'css selector',
        '.alert-success:nth-child(1) .alertinner strong',
    )
    BASKET_PRICE_MSG = ('css selector', '.alert-info strong')
