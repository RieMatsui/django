from processing_data.services.util.data_frame_service import DataFrameService


class CustomerModel(object):

    @staticmethod
    def get_all():
        return DataFrameService.csv_read('processing_data/static/data/ec/customer_master.csv')
