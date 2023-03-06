RESPONSE = {
  405: { "statusCode": 405, "error": 'Method Not Allowed', "message": 'An invalid operation occurred' },
  500: { "statusCode": 500, "error": 'Internal Server Error', "message": 'An internal server error occurred' },
  505: { "statusCode": 505, "error": 'Unauthorized', "message": 'An internal server unauthorized' },
  200: { "statusCode": 200, "error": None, "message": 'Success', "data": {} },
  400: { "statusCode": 400, "error": None, "message": 'BadRequest' }
}