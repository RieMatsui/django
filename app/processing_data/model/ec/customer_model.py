from processing_data.lib.file import read


class CustomerModel(object):

    @staticmethod
    def get_all():
        return read.csv_read('/data/ec/customer_master.csv')
