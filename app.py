from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from sqlalchemy import text
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver

#select
query = ObjectType("Query")
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)


#insert
mutation = ObjectType("Mutation")
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


# ✅ Reemplazo manual de PLAYGROUND_HTML
PLAYGROUND_HTML = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GraphQL Playground</title>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
    <link rel="shortcut icon" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png" />
    <script src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
  </head>
  <body>
    <div id="root">
      <style>
        body {
          background-color: rgb(23,42,58);
          font-family: Open Sans, sans-serif;
          height: 90vh;
        }
        #root {
          height: 100%;
          width: 100%;
        }
      </style>
    </div>
    <script>window.addEventListener('load', function () {
      GraphQLPlayground.init(document.getElementById('root'), {
        endpoint: '/graphql'
      })
    })</script>
  </body>
</html>
"""

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route('/check-db')
def check_db():
    try:
        result = db.session.execute(text("SELECT 1;"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}