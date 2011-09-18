def should_raise(exception):
   def should_raise_decorator(decorated_function):
       def decorated(self, *args, **kwargs):
           self.assertRaises(exception, decorated_function, self, *args, **kwargs)
       return decorated
   return should_raise_decorator
  