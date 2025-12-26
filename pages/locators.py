class BasePageLocators:
    CHECKOUT_BASKET_LINK = ('css selector', '.basket-mini a')
    LOGIN_LINK = ('id', 'login_link')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = ('css selector', '#content_inner > p')
    PRODUCTS_IN_BASKET = ('id', 'basket_formset')


class LoginPageLocators:
    LOGIN_FORM = ('id', 'login_form')
    REGISTER_FORM = ('id', 'register_form')


class ProductPageLocators:
    BASKET_PRICE_MESSAGE = ('css selector', '.alert-info strong')
    ADD_TO_BASKET_BUTTON = ('css selector', '.btn-add-to-basket')
    PRODUCT_NAME = ('css selector', '.product_main h1')
    PRODUCT_PRICE = ('css selector', '.product_main .price_color')
    SUCCESS_MESSAGE = (
        'css selector',
        '.alert-success:nth-child(1) .alertinner strong',
    )
