from logzero import logger


MENU = {"soda", "fries", "burger", "shake", "cookie", "chicken strips"}


def get_order(test_order=None):
    current_order = []
    # test related: ignore
    order_iter = _get_order_iter(test_order)
    while True:
        if test_order:
            try:
                order = next(order_iter)
            except StopIteration:
                return current_order
        else:
            order = input("What can I get for you?")
        if order in MENU:
            current_order.append(order)
        else:
            logger.info("I'm sorry, we don't serve that.")
            continue
        if test_order:
            continue
        elif is_order_complete():
            return current_order


def _get_order_iter(test_order):
    if test_order:
        return iter(test_order)
    return None


def is_order_complete():
    choice = input("Anything else? yes/no")
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def output_order(order_list):
    logger.info("Okay, so you want")
    for order in order_list:
        logger.info(order)


def main():
    order = get_order()
    output_order(order)
    logger.info("Please drive through to the second window.")


if __name__ == "__main__":
    main()
