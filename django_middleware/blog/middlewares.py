# creating function based middleware

# def my_middleware(get_response):
#     print("One time Initialization")
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function

#creating class based middleware
class mymiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response