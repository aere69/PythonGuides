# Activity/Habit Tracking

Use [Pixela](https://pixe.la/) to create an activity/habit tracking app.
Use Post, Put, Delete and Headers

## How to use

1. Create a user account

    Call [/v1/users](https://docs.pixe.la/entry/post-user) API by `HTTP POST`.

    ```sh
    $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
    
    {"message":"Success.","isSuccess":true}
    ```

2. Create a graph definition

    Call [/v1/users/<username>/graphs](https://docs.pixe.la/entry/post-graph) by `HTTP POST`.

    ```sh
    $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

    {"message":"Success.","isSuccess":true}
    ```
3. Get the graph

    Browse [https://pixe.la/v1/users/a-know/graphs/test-graph]([https://pixe.la/v1/users/a-know/graphs/test-graph) ! This is also [/v1/users/<username>/graphs/<graphID>](https://docs.pixe.la/entry/post-graph) `API`.

4. Post value to the graph

    Call [/v1/users/<username>/graphs/<graphID>](https://docs.pixe.la/entry/post-pixel) by `HTTP POST`.

    ```sh
    $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

    {"message":"Success.","isSuccess":true}
    ```

5. Browse again!

    Browse [https://pixe.la/v1/users/a-know/graphs/test-graph](https://pixe.la/v1/users/a-know/graphs/test-graph), again!

6. You can also find out more about.

    You can get more information by adding .html to the end of the URL on Step.6 at it in your browser! [(https://pixe.la/v1/users/a-know/graphs/test-graph.html)](https://pixe.la/v1/users/a-know/graphs/test-graph.html)

[PIXELA DOCS](https://docs.pixe.la/)