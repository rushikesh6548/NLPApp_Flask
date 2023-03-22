from apikeys import APIKey
import paralleldots


class API:
    @staticmethod
    def sentiment(text):
        print("Yaha agaye ")
        api_key = APIKey.key_returned()
        print(api_key)
        paralleldots.set_api_key(api_key)
        result = paralleldots.sentiment(text)
        return result
