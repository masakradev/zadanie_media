
class JSONResponse:

    @staticmethod
    def success(data):
        schema = {
            "status": "success",
            "data": data
        }
        return schema

    @staticmethod
    def error(error):
        schema = {
            "status": "error",
            "message": error
        }
        return schema