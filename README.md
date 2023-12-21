# Users API Appication with Swagger.
This is a simple Flask web application for user management.

<p>&nbsp;</p>

<h2>Documentation</h2>


<h3><span style="font-size:18px">About</span></h3>

<p>This simple python app is build on the Flask web framwork.</p>

<p>The purpose of the app is to manage simple user database through exposed API endpoints for CRUD operations.</p>

<h3><span style="font-size:18px">Technical characteristics</span></h3>

<p><strong>Code base: </strong>Python3, CSS, HTML, SQLite, Flask, Swagger.</p>

<p>The backend environment is running Python 3.11.6 in a virtualenv.<br />
The users data is stored in an sqlite instance db file users.db.&nbsp;<br />
Swagger is run by a Flask, API documentation is written in the swagger.json file.<br />
The fronend homepage is a simple HTML which Flusk is running as a template and loads the CSS code from a static directory.&nbsp;&nbsp;<br />
The webserver is running on port 80.</p>

<p><strong>Python virtualenv&nbsp;requirements:</strong><br />
aniso8601==9.0.1<br />
blinker==1.7.0<br />
click==8.1.7<br />
Flask==3.0.0<br />
Flask-RESTful==0.3.10<br />
Flask-SQLAlchemy==3.1.1<br />
flask-swagger==0.2.14<br />
flask-swagger-ui==4.11.1<br />
itsdangerous==2.1.2<br />
Jinja2==3.1.2<br />
MarkupSafe==2.1.3<br />
pytz==2023.3.post1<br />
PyYAML==6.0.1<br />
six==1.16.0<br />
SQLAlchemy==2.0.23<br />
typing_extensions==4.9.0<br />
Werkzeug==3.0.1</p>

<p>&nbsp;</p>

<h3>API endpoints</h3>

<p>They are five endpoints exposed for managing the users in the database.<br />
Request and responce content type is in json format.<br />
Server:&nbsp;<a href="http://localhost:8080/api/users">http://localhost:8080</a></p>

<p>Create a new User:&nbsp;</p>

<pre>
<code class="language-html">/api/new_user</code></pre>

<blockquote>
<p>Example payload: Body</p>

<pre>
<code class="language-html">{
  "first_name": "Tony",
  "last_name": "Stak",
  "username": "aironman"
}</code></pre>
</blockquote>

<blockquote>
<p>Response: 200 OK</p>

<pre>
<code class="language-html">{
  "id": 1,
  "first_name": "Tony",
  "last_name": "Stak",
  "username": "aironman"
}</code></pre>
</blockquote>

<p>&nbsp;</p>

<p>List all users:</p>

<pre>
<code class="language-html">/api/users</code></pre>

<blockquote>
<p>&nbsp;Response: 200 OK</p>

<pre>
<code class="language-html">[	
	{
        "id": 1,
		"username": "aironman",
        "first_name": "Tony",
        "last_name": "Stak"

    }
    {
        "id": 2,
        "username": "jbond",
        "first_name": "James",
        "last_name": "Bond"
    }, {
        "id": 3,
        "username": "malin",
        "first_name": "Malin",
        "last_name": "Markov"
    }
]</code></pre>
</blockquote>

<p>&nbsp;</p>

<p>List user by ID:&nbsp;</p>

<pre>
<code class="language-html">/api/users/user/id={int}</code></pre>

<p>&nbsp;</p>

<p>Update a User:&nbsp;</p>

<pre>
<code class="language-html">/api/users/user/id={int}</code></pre>

<blockquote>
<p>&nbsp;Example payload: Body</p>

<pre>
<code class="language-html">{
  "first_name": "Tony",
  "last_name": "Stak",
  "username": "avenger"
}</code></pre>
</blockquote>

<blockquote>
<p>Response: 200 OK</p>

<pre>
<code class="language-html">{
  "id": 1,
  "first_name": "Tony",
  "last_name": "Stak",
  "username": "avenger"
}</code></pre>
</blockquote>

<p>&nbsp;</p>

<p>Delete a User:&nbsp;</p>

<pre>
<code class="language-html">/api/users/user/delete/id={int}</code></pre>

<p>&nbsp;</p>

<h2>Instalation</h2>
<p>To install and run the app follow the below instruction:</p>

<ol>
	<li>A</li>
	<li>b</li>
</ol>

<p>&nbsp;</p>
