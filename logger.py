import logging
add=logging.getLogger(__name__)
add.setLevel(logging.INFO)
handler=logging.FileHandler("logs.log")
handler.setFormatter(logging.Formatter("%(asctime)s:%(filename)s:%(funcName)s:%(message)s"))
add.addHandler(handler)
