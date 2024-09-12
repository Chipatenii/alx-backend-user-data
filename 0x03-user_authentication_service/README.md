To declare API routes in a Flask app, you can use the `@app.route()` decorator. Simply define a function and decorate it with `@app.route()` followed by the desired URL path as an argument.

To get and set cookies in Flask, you can use the `request.cookies` dictionary to access existing cookies, and the `response.set_cookie()` method to set new cookies.

To retrieve request form data in Flask, you can use the `request.form` dictionary. This allows you to access data submitted through HTML forms.

To return various HTTP status codes in Flask, you can use the `abort()` function from the `flask` module. Simply call `abort()` with the desired status code as an argument.

Remember to import the necessary modules and libraries before using these functionalities in your Flask app.