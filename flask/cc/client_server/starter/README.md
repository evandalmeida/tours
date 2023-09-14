# Models

 - Server
    - **id**   Integer (primary key)
    - **name** String (unqiue, not null)
 - Message
    - **id**        Integer (primary key)
    - **content**   String (not null)
    - **server_id** Integer (not null)
    - **client_id** Integer (not null)
 - Client
    - **id**   (primary key)
    - **name** (unqiue, not null)
# Validation

  - Server
    - names must be all upper case letters
  - Client
    - name must be at least 5 characters and at most 15
# Routes

  - GET /clients
  - POST /messages
  - PATCH /messages/<int:id>
  - DELETE /messages/<int:id>
    

# Response Formats

  - GET /clients
  ```json
  [
      {
          id
          name
          servers: [
              {
                  id
                  name
              }
          ]
      }
  ]
  ```
  - POST /messages
  ```json
      {
          id
          content
          server: {
              id
              name
          }
          client: {
              id
              name
          }
      }
  ```
  - PATCH /messages/<int:id>
  ```json
      {
          id
          content
          server: {
              id
              name
          }
          client: {
              id
              name
          }
      }
  ```