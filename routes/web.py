from masonite.routes import Route

ROUTES = [
  Route.get("/", "BookController@index").name("book.index"),
  Route.post("/create", "BookController@store").name("book.store"),

  Route.get("/edit-form/@id", "BookController@editForm").name("book.edit.form"),
  Route.get("/row/@id", "BookController@row").name("book.row"),
  Route.put("/update/@id", "BookController@update").name("book.update"),
  Route.delete("/delete/@id", "BookController@destroy").name("book.destroy"),
]
