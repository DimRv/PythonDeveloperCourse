class Converter:
    @staticmethod
    def convert(from_val,to_val,money):
        rub_amount = round(money * from_val.course,2)
        to_amount = round(rub_amount / to_val.course,2)
        return to_amount